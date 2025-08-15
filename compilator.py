from time import time

start_time = time()
import json
from sys import setrecursionlimit

setrecursionlimit(999)
import os
import copy

import requests

import nbtworker
from jmcc import translate, minecraft_based_text, color_codes, allowed_symbols, Properties

origin_actions = {}
events = {}
values = {}
items = json.load(open("data/items.json"))
blocks = json.load(open("data/blocks.json"))
particles = json.load(open("data/particles.json"))
potions = json.load(open("data/potions.json"))
objects = set()
actions = {}
for i in json.load(open("data/actions.json")):
    objects.add(i["object"])
    if i["object"] not in actions:
        actions[i["object"]] = {}
    new_args = {}
    arg_index = 0
    for arg in i["args"]:
        arg["pos"] = arg_index
        new_args[arg["id"]] = arg
        arg_index += 1
        i["args"] = new_args
    actions[i["object"]][i["name"]] = i
    if "origin" in i:
        origin_actions[i["name"]] = i["object"]
for i in json.load(open("data/events.json")):
    events[i["id"]] = i
for i in json.load(open("data/values.json")):
    values[i["id"]] = i

global_text = {}
global_new = {}


def new(source):
    global global_new
    global_new[source] = global_new.setdefault(source, -1) + 1
    return global_new[source]


class Tokens:
    __slots__ = ()
    NONE: int = -1
    NUMBER: int = 0
    PLUS_NUMBER: int = 1
    MINUS_NUMBER: int = 2
    STRING: int = 3
    SUBSTRING: int = 4
    LPAREN: int = 5
    RPAREN: int = 6
    LSPAREN: int = 7
    RSPAREN: int = 8
    LCPAREN: int = 9
    RCPAREN: int = 10
    VARIABLE: int = 11
    COMMA: int = 12
    DOT: int = 13
    COLON: int = 14
    SEMICOLON: int = 15
    ASSIGN: int = 16
    PLUS: int = 17
    MINUS: int = 18
    MULTIPLY: int = 19
    DIVIDE: int = 20
    DEG: int = 21
    PR: int = 22
    INLINE_VARIABLE: int = 23
    LOCAL_VARIABLE: int = 24
    GAME_VARIABLE: int = 25
    SAVE_VARIABLE: int = 26
    BRACKET_VARIABLE: int = 27
    PLAIN_STRING: int = 28
    LEGACY_STRING: int = 29
    MINIMESSAGE_STRING: int = 30
    JSON_STRING: int = 31
    SNBT: int = 32
    IF: int = 33
    ELSE: int = 34
    FUNCTION_DEFINE: int = 35
    PROCESS_DEFINE: int = 36
    VAR_DEFINE: int = 37
    INLINE_DEFINE: int = 38
    LOCAL_DEFINE: int = 39
    GAME_DEFINE: int = 40
    SAVE_DEFINE: int = 41
    CLASS_DEFINE: int = 42
    EVENT_DEFINE: int = 43
    IMPORT: int = 44
    AND: int = 45
    OR: int = 46
    NOT: int = 47
    RETURN: int = 48
    GREATER: int = 49
    LESS: int = 50
    DOUBLE_COLON: int = 51
    CYCLE_THING: int = 52
    EOF: int = 53
    ELIF: int = 54
    BRACKET_DEFINE: int = 55
    AS: int = 56
    DECORATOR: int = 57
    LESS_OR_EQUALS: int = 58
    MINUS_ASSIGN: int = 59
    PLUS_ASSIGN: int = 60
    EQUALS: int = 61
    DIVIDE_ASSIGN: int = 62
    PR_ASSIGN: int = 63
    DEG_ASSIGN: int = 64
    GREATER_OR_EQUALS: int = 65
    NOT_EQUALS: int = 66
    MULTIPLY_ASSIGN: int = 67
    QUESTION_MARK: int = 68
    DOUBLE_MULTIPLY: int = 69
    NEXT_LINE: int = 70
    JMCC_DEFINE: int = 71
    JMCC_VARIABLE: int = 72
    IN: int = 73


class Token:
    __slots__ = ("type", "value", "starting_pos", "ending_pos", "source", "giga")

    def __init__(self, token_type: int, token_value: str, starting_pos: int, ending_pos: int, source: str, giga=None):
        self.type = token_type
        self.value = token_value
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        self.giga = giga

    def __str__(self):
        return f"Token({self.type},\"{self.value}\")"

    def __repr__(self):
        return self.__str__()


def error(error_type="", error_message="", starting_pos=-1, ending_pos=-1, source=None, txt=None):
    if source is None:
        print(minecraft_based_text(f"&c{error_type} : {error_message}"))
    else:
        if txt is None:
            txt = global_text.setdefault(source, "")
        start_line_index = txt.rfind("\n", 0, starting_pos)
        start_line = txt.count("\n", 0, starting_pos)
        ending_line_index = txt.find("\n", ending_pos)
        if ending_line_index == -1:
            ending_line_index = len(txt)
        if start_line_index == -1:
            start_line_index = 0
        elif start_line_index > 0:
            start_line_index += 1
        msg = (
                f"&c{translate('compilator.file')} \"{source}\":\n{start_line + 1}:{starting_pos - start_line_index + 1} - " +
                txt[start_line_index:starting_pos] + "&4&n" +
                txt[starting_pos:ending_pos + 1] + "&r&c" +
                txt[ending_pos + 1:ending_line_index] + f"\n{error_type} : {error_message}")
        print(minecraft_based_text(msg))
    exit(0)


def error_from_object(obj, error_type="", error_message=""):
    return error(error_type, error_message, obj.starting_pos, obj.ending_pos, obj.source)


class Lexer:
    __slots__ = ("current_pos", "current_char", "allow_jmcc", "source", "text")

    def __init__(self, txt, source, allow_jmcc=False):
        self.current_pos = -1
        self.current_char = ""
        self.source = source
        self.text = txt
        self.allow_jmcc = allow_jmcc
        self.advance()

    def advance(self):
        self.current_pos += 1
        if self.current_pos < len(self.text):
            self.current_char = self.text[self.current_pos]
        else:
            self.current_char = ""

    @property
    def next_token(self) -> Token:
        while self.current_char == " ":
            self.advance()
        starting_pos = self.current_pos
        sign_mode = False
        token_value = ""
        if self.current_char.isalpha() or self.current_char == "_":
            while self.current_char != "" and (
                    self.current_char.isalpha() or self.current_char.isdigit() or self.current_char == "_"):
                token_value += self.current_char
                self.advance()
            token_type = None
            match token_value:
                case "if":
                    token_type = Tokens.IF
                case "else":
                    token_type = Tokens.ELSE
                case "function":
                    token_type = Tokens.FUNCTION_DEFINE
                case "process":
                    token_type = Tokens.PROCESS_DEFINE
                case "var":
                    token_type = Tokens.VAR_DEFINE
                case "inline":
                    token_type = Tokens.INLINE_DEFINE
                case "jmcc":
                    token_type = Tokens.JMCC_DEFINE
                case "bracket":
                    token_type = Tokens.BRACKET_DEFINE
                case "local":
                    token_type = Tokens.LOCAL_DEFINE
                case "game":
                    token_type = Tokens.GAME_DEFINE
                case "save":
                    token_type = Tokens.SAVE_DEFINE
                case "class":
                    token_type = Tokens.CLASS_DEFINE
                case "event":
                    token_type = Tokens.EVENT_DEFINE
                case "import":
                    token_type = Tokens.IMPORT
                case "and":
                    token_type = Tokens.AND
                case "or":
                    token_type = Tokens.OR
                case "not":
                    token_type = Tokens.NOT
                case "return":
                    token_type = Tokens.RETURN
                case "elif":
                    token_type = Tokens.ELIF
                case "as":
                    token_type = Tokens.AS
                case "in":
                    token_type = Tokens.IN
            if token_type is not None:
                return Token(token_type, token_value, starting_pos, self.current_pos - 1, self.source)
            sign_mode = True

        if self.current_char == "\"" or self.current_char == "\'" or self.current_char == "`" or self.current_char == "<":
            mode = self.current_char
            if sign_mode:
                if mode == "`":
                    dect = {"bracket": Tokens.BRACKET_VARIABLE, "inline": Tokens.INLINE_VARIABLE,
                            "local": Tokens.LOCAL_VARIABLE, "game": Tokens.GAME_VARIABLE, "save": Tokens.SAVE_VARIABLE,
                            "jmcc": Tokens.JMCC_VARIABLE}
                    res = find_value_from_list(token_value, dect)
                elif mode in {'"', "'"}:
                    dect = {"plain": Tokens.PLAIN_STRING, "minimessage": Tokens.MINIMESSAGE_STRING,
                            "legacy": Tokens.LEGACY_STRING, "json": Tokens.JSON_STRING}
                    res = find_value_from_list(token_value, dect)
                else:
                    dect = {}
                    res = -1
                if res == -1:
                    return Token(Tokens.VARIABLE, token_value, starting_pos, self.current_pos - 1, self.source)
                token_type = dect[res]
            else:
                if mode == "`":
                    token_type = Tokens.VARIABLE
                elif mode == "<":
                    mode = ">"
                    token_type = Tokens.SUBSTRING
                else:
                    token_type = Tokens.STRING
            self.advance()
            if mode == ">" and self.current_char == "=":
                self.advance()
                return Token(Tokens.LESS_OR_EQUALS, "<=", starting_pos, self.current_pos - 1, self.source)
            if mode == ">" and self.current_char in {" ", "\n"}:
                self.advance()
                return Token(Tokens.LESS, "<", starting_pos, self.current_pos - 1, self.source)
            giga_token = []
            token_value = ""
            block_next_symbol = False
            while self.current_char != "" and (self.current_char != mode or block_next_symbol is True):
                if block_next_symbol:
                    block_next_symbol = False
                    if self.current_char == "n":
                        token_value += "\\"
                    if self.current_char not in {"\n", "\t"}:
                        token_value += self.current_char
                elif self.current_char == "\\":
                    block_next_symbol = True
                elif self.current_char in {"\n", "\t"}:
                    token_value += "\\n"
                elif self.current_char == "$":
                    if len(token_value) > 0:
                        giga_token.append(
                            [Token(Tokens.STRING, token_value, starting_pos, self.current_pos - 1, self.source),
                             Token(Tokens.NONE, "${", self.current_pos, self.current_pos, self.source)])
                    token_value = ""
                    new_starting_pos = self.current_pos
                    self.advance()
                    var_value = ""
                    if self.current_char == "{":
                        self.advance()
                        thing = []
                        counter = 1
                        while self.current_char != "" and not (self.current_char == "}" and counter == 1):
                            if self.current_char == "{":
                                counter += 1
                            elif self.current_char == "}":
                                counter -= 1
                            a = self.next_token
                            if a.type != Tokens.EOF:
                                thing.append(a)
                        if self.current_char == "}":
                            self.advance()
                        if len(thing) > 0:
                            thing.append(Token(Tokens.NONE, "}", self.current_pos, self.current_pos, self.source))
                            giga_token.append(thing)
                    else:
                        while self.current_char != "" and (
                                self.current_char.isalpha() or self.current_char.isdigit() or self.current_char == "_"):
                            var_value += self.current_char
                            self.advance()
                        if len(var_value) > 0:
                            giga_token.append([
                                Token(Tokens.VARIABLE, var_value, new_starting_pos, self.current_pos - 1, self.source),
                                Token(Tokens.NONE, "}", self.current_pos, self.current_pos, self.source)])
                        else:
                            token_value = "$"
                    continue
                else:
                    token_value += self.current_char
                self.advance()
            if self.current_char == mode:
                self.advance()
                if len(giga_token) == 0:
                    if token_value.startswith("jmcc.") and mode not in {"\"", "\'"} and not self.allow_jmcc:
                        error("NameError", translate("error.nameerror.cant_use_jmcc"), starting_pos,
                              self.current_pos - 1, self.source)
                    return Token(token_type, token_value, starting_pos,
                                 self.current_pos - 1, self.source)
                else:
                    if len(token_value) > 0:
                        giga_token.append([
                            Token(Tokens.STRING, token_value, starting_pos, self.current_pos - 1, self.source),
                            Token(Tokens.NONE, "}", self.current_pos, self.current_pos, self.source)])
                    release_index = global_text[self.source].index(mode if mode != ">" else "<", starting_pos,
                                                                   self.current_pos - 1) + 1
                    release = global_text[self.source][release_index:self.current_pos - 1]
                    if release.startswith("jmcc.") and mode not in {"\"", "\'"}:
                        error("NameError", translate("error.nameerror.cant_use_jmcc"), starting_pos,
                              self.current_pos - 1, self.source)
                    return Token(token_type, release, starting_pos, self.current_pos - 1, self.source, giga=giga_token)
            else:
                error("SyntaxError", translate("error.syntaxerror.string_wasnt_closed"), starting_pos, self.current_pos,
                      self.source)

        if self.current_char == "{":
            if sign_mode:
                if token_value in {"minecraft_nbt", "nbt", "m", "n"}:
                    self.advance()
                    count = 1
                    token_value = "{"
                    while self.current_char != "" and (count != 0):
                        token_value += self.current_char
                        if self.current_char == "{":
                            count += 1
                        elif self.current_char == "}":
                            count -= 1
                        self.advance()
                    return Token(Tokens.SNBT, token_value, starting_pos, self.current_pos - 1, self.source)
                else:
                    return Token(Tokens.VARIABLE, token_value, starting_pos, self.current_pos - 1, self.source)

            self.advance()
            return Token(Tokens.LCPAREN, "{", starting_pos, starting_pos, self.source)

        if sign_mode:
            return Token(Tokens.VARIABLE, token_value, starting_pos, self.current_pos - 1, self.source)
        if self.current_char.isdigit() or self.current_char == "-" or self.current_char == "+":
            minus = False
            plus = False
            es = False
            dot = False
            if self.current_char == "-":
                minus = True
            if self.current_char == "+":
                plus = True
            starting_pos = self.current_pos
            token_value = self.current_char
            self.advance()
            while self.current_char != "" and self.current_char.isdigit() or (
                    es is False and self.current_char == "e") or (
                    dot is False and self.current_char == "." and es is False) or (self.current_char == "_"):
                if es is False and self.current_char == "e":
                    es = True
                if dot is False and self.current_char == "." and es is False:
                    dot = True
                if self.current_char == "_":
                    self.advance()
                    continue
                token_value += self.current_char
                self.advance()
            if token_value == "-":
                if self.current_char == ">":
                    self.advance()
                    return Token(Tokens.CYCLE_THING, "->", starting_pos, self.current_pos - 1, self.source)
                if self.current_char == "=":
                    self.advance()
                    return Token(Tokens.MINUS_ASSIGN, "-=", starting_pos, self.current_pos - 1, self.source)
                return Token(Tokens.MINUS, "-", starting_pos, starting_pos, self.source)
            elif token_value == "+":
                if self.current_char == "=":
                    self.advance()
                    return Token(Tokens.PLUS_ASSIGN, "+=", starting_pos, self.current_pos - 1, self.source)
                return Token(Tokens.PLUS, "+", starting_pos, starting_pos, self.source)
            try:
                return Token(Tokens.PLUS_NUMBER if plus else (Tokens.MINUS_NUMBER if minus else Tokens.NUMBER),
                             int(token_value),
                             starting_pos, self.current_pos - 1, self.source)
            except Exception:
                return Token(Tokens.PLUS_NUMBER if plus else (Tokens.MINUS_NUMBER if minus else Tokens.NUMBER),
                             float(token_value),
                             starting_pos, self.current_pos - 1, self.source)

        if self.current_char == "(":
            self.advance()
            return Token(Tokens.LPAREN, ")", starting_pos, starting_pos, self.source)
        if self.current_char == ")":
            self.advance()
            return Token(Tokens.RPAREN, ")", starting_pos, starting_pos, self.source)
        if self.current_char == ",":
            self.advance()
            return Token(Tokens.COMMA, ",", starting_pos, starting_pos, self.source)
        if self.current_char == ":":
            self.advance()
            if self.current_char == ":":
                self.advance()
                return Token(Tokens.DOUBLE_COLON, "::", starting_pos, self.current_pos - 1, self.source)
            return Token(Tokens.COLON, ":", starting_pos, starting_pos, self.source)
        if self.current_char == ".":
            self.advance()
            return Token(Tokens.DOT, ".", starting_pos, starting_pos, self.source)
        if self.current_char == ";":
            self.advance()
            return Token(Tokens.SEMICOLON, ";", starting_pos, starting_pos, self.source)
        if self.current_char == "[":
            self.advance()
            return Token(Tokens.LSPAREN, "[", starting_pos, starting_pos, self.source)
        if self.current_char == "]":
            self.advance()
            return Token(Tokens.RSPAREN, "]", starting_pos, starting_pos, self.source)
        if self.current_char == "}":
            self.advance()
            return Token(Tokens.RCPAREN, "}", starting_pos, starting_pos, self.source)
        if self.current_char == "=":
            self.advance()
            if self.current_char == "=":
                self.advance()
                return Token(Tokens.EQUALS, "==", starting_pos, self.current_pos - 1, self.source)
            return Token(Tokens.ASSIGN, "=", starting_pos, starting_pos, self.source)
        if self.current_char == "*":
            self.advance()
            if self.current_char == "*":
                self.advance()
                return Token(Tokens.DOUBLE_MULTIPLY, "**", starting_pos, starting_pos + 1, self.source)
            return Token(Tokens.MULTIPLY, "*", starting_pos, starting_pos, self.source)
        if self.current_char == "/":
            self.advance()
            if self.current_char == "/":
                while self.current_char != "":
                    if self.current_char == "\n" or self.current_char == "\t":
                        return self.next_token
                    self.advance()
                return Token(Tokens.EOF, "None", starting_pos, starting_pos, self.source)
            elif self.current_char == "*":
                while self.current_char != "":
                    if self.current_char == "*":
                        self.advance()
                        if self.current_char == "/":
                            self.advance()
                            return self.next_token
                    self.advance()
                return Token(Tokens.EOF, "None", starting_pos, starting_pos, self.source)
            elif self.current_char == "=":
                self.advance()
                return Token(Tokens.DIVIDE_ASSIGN, "/=", starting_pos, self.current_pos - 1, self.source)
            return Token(Tokens.DIVIDE, "/", starting_pos, starting_pos, self.source)
        if self.current_char == "%":
            self.advance()
            if self.current_char == "=":
                self.advance()
                return Token(Tokens.PR_ASSIGN, "%=", starting_pos, self.current_pos - 1, self.source)
            return Token(Tokens.PR, "%", starting_pos, starting_pos, self.source)
        if self.current_char == "^":
            self.advance()
            if self.current_char == "=":
                self.advance()
                return Token(Tokens.DEG_ASSIGN, "^=", starting_pos, self.current_pos - 1, self.source)
            return Token(Tokens.DEG, "^", starting_pos, starting_pos, self.source)
        if self.current_char == ">":
            self.advance()
            if self.current_char == "=":
                self.advance()
                return Token(Tokens.GREATER_OR_EQUALS, ">=", starting_pos, self.current_pos - 1, self.source)
            return Token(Tokens.GREATER, ">", starting_pos, starting_pos, self.source)
        if self.current_char == "!":
            self.advance()
            if self.current_char == "=":
                self.advance()
                return Token(Tokens.NOT_EQUALS, "!=", starting_pos, self.current_pos - 1, self.source)
            return Token(Tokens.NOT, ">", starting_pos, starting_pos, self.source)
        if self.current_char == "@":
            self.advance()
            return Token(Tokens.DECORATOR, "@", starting_pos, starting_pos, self.source)
        if self.current_char == "&":
            self.advance()
            return Token(Tokens.AND, "and", starting_pos, starting_pos, self.source)
        if self.current_char == "|":
            self.advance()
            return Token(Tokens.OR, "or", starting_pos, starting_pos, self.source)
        if self.current_char == "?":
            self.advance()
            return Token(Tokens.QUESTION_MARK, "?", starting_pos, starting_pos, self.source)
        if self.current_char == "\\":
            self.advance()
            while self.current_char == " ":
                self.advance()
            if self.current_char in {"\n", "\t"}:
                self.advance()
                return self.next_token
            else:
                error("SyntaxError", translate("error.syntaxerror.wrong_symbol", {0: "\\n", 1: self.current_char}),
                      self.current_pos,
                      self.current_pos, source=self.source)
        if self.current_char == "\n" or self.current_char == "\t":
            self.advance()
            return Token(Tokens.NEXT_LINE, "\n", starting_pos, starting_pos, self.source)
        if self.current_char == "":
            return Token(Tokens.EOF, "None", starting_pos, starting_pos, self.source)
        else:
            error("SyntaxError", translate("error.syntaxerror.unexpected_symbol", {0: self.current_char}), starting_pos,
                  starting_pos, source=self.source)

    def get_remaining_tokens(self) -> list:
        lest = []
        while (token := self.next_token).type != Tokens.EOF:
            lest.append(token)
        return lest


def tokenize(txt, source=None, allow_jmcc=False):
    if source is None:
        source = new("source")
    if source not in global_text:
        global_text[source] = txt
    return Lexer(txt, source, allow_jmcc=allow_jmcc).get_remaining_tokens()


def tokenize_from_file(file1):
    global global_text
    source = os.path.abspath(file1.name)
    if source not in global_text:
        global_text[source] = file1.read()
    return tokenize(global_text[source], source)


class Parser:
    Expr_priorities = [Tokens.IN, Tokens.AND, Tokens.OR, Tokens.LESS, Tokens.GREATER, Tokens.EQUALS,
                       Tokens.LESS_OR_EQUALS,
                       Tokens.GREATER_OR_EQUALS, Tokens.PLUS, Tokens.MINUS, Tokens.MINUS_NUMBER, Tokens.PLUS_NUMBER,
                       Tokens.MULTIPLY, Tokens.DIVIDE, Tokens.PR, Tokens.DEG]
    Expr_operations = {Tokens.AND: "__and__", Tokens.OR: "__or__", Tokens.LESS: "__less__",
                       Tokens.GREATER: "__greater__", Tokens.EQUALS: "__equals__",
                       Tokens.LESS_OR_EQUALS: "__less_or_equals__",
                       Tokens.GREATER_OR_EQUALS: "__greater_or_equals__", Tokens.PLUS: "__add__",
                       Tokens.MINUS: "__subtract__",
                       Tokens.MULTIPLY: "__multiply__", Tokens.DIVIDE: "__divide__", Tokens.PR: "__remainder__",
                       Tokens.DEG: "__pow__", Tokens.IN: "__contains__"}
    __slots__ = ("tokens", "source", "index", "current_token", "context", "parser_id")

    def __init__(self, tokens: list, source: str):
        self.tokens = tokens
        self.source = source
        self.index = 0
        self.current_token = self.token(self.index)
        self.context = Context(self.source)
        self.parser_id = new("parser")
        Context.sources.append(self.source)

    def token(self, index: int) -> Token:
        if index >= len(self.tokens):
            if len(self.tokens) == 0:
                return Token(Tokens.EOF, None, -1, -1,
                             self.source)
            return Token(Tokens.EOF, None, self.tokens[-1].ending_pos + 2, self.tokens[-1].ending_pos + 2,
                         self.source)
        return self.tokens[index]

    def eat(self, token_type: int, ignore_next_lines=False) -> None:
        if self.current_token.type == token_type:
            self.index += 1
            self.current_token = self.token(self.index)
            if ignore_next_lines:
                self.skip_next_lines()

        else:
            error_from_object(self.current_token, "SyntaxError", translate("error.syntaxerror.wrong_token", {
                0: translate('token.' + str(token_type) + '.name'),
                1: translate('token.' + str(self.current_token.type) + '.name')}))

    def get_giga_token(self, giga):
        giga_acts = []
        for giga_token in giga:
            parser = Parser(giga_token, self.source)
            self.context.next_lvl()
            giga_acts.append(parser.expr())
            parser.eat(Tokens.NONE)
            self.context.previous_lvl()
            del Context.sources[-1]
        return giga_acts

    def factor(self):
        token = self.current_token
        if token.type == Tokens.NUMBER:
            self.eat(Tokens.NUMBER)
            return number(token.value, token.starting_pos, token.ending_pos, token.source)
        elif token.type == Tokens.PLUS_NUMBER:
            self.eat(Tokens.PLUS_NUMBER)
            return number(token.value, token.starting_pos, token.ending_pos, token.source)
        elif token.type == Tokens.MINUS_NUMBER:
            self.eat(Tokens.MINUS_NUMBER)
            return number(token.value, token.starting_pos, token.ending_pos, token.source)
        elif token.type in {Tokens.STRING, Tokens.LEGACY_STRING, Tokens.PLAIN_STRING, Tokens.MINIMESSAGE_STRING,
                            Tokens.JSON_STRING, Tokens.SUBSTRING}:
            if token.type in {Tokens.STRING, Tokens.LEGACY_STRING, Tokens.SUBSTRING}:
                self.eat(self.current_token.type)
                text_type = Texts.LEGACY
            elif token.type == Tokens.PLAIN_STRING:
                self.eat(Tokens.PLAIN_STRING)
                text_type = Texts.PLAIN
            elif token.type == Tokens.MINIMESSAGE_STRING:
                self.eat(Tokens.MINIMESSAGE_STRING)
                text_type = Texts.MINIMESSAGE
            elif token.type == Tokens.JSON_STRING:
                self.eat(Tokens.JSON_STRING)
                text_type = Texts.JSON
            else:
                text_type = Texts.NONE
            if token.giga is not None:
                token.value = self.get_giga_token(token.giga)
            return text(token.value, text_type, token.starting_pos, token.ending_pos, token.source)
        elif token.type == Tokens.LPAREN:
            self.eat(Tokens.LPAREN, True)
            result = self.expr()
            self.skip_next_lines()
            result.starting_pos = token.starting_pos
            result.ending_pos = self.current_token.ending_pos
            self.eat(Tokens.RPAREN)
            return result
        elif token.type == Tokens.LSPAREN:
            self.eat(Tokens.LSPAREN, True)
            vals = []
            while (self.current_token.type is not None) and self.current_token.type != Tokens.RSPAREN:
                vals.append(self.expr())
                self.skip_next_lines()
                if self.current_token.type != Tokens.RSPAREN:
                    self.eat(Tokens.COMMA, True)
            ending_pos = self.current_token.ending_pos
            self.eat(Tokens.RSPAREN)
            return lst(vals, token.starting_pos, ending_pos, token.source)
        elif token.type == Tokens.LCPAREN:
            self.eat(Tokens.LCPAREN, True)
            keys = []
            vals = []
            while (self.current_token.type is not None) and (self.current_token.type != Tokens.RCPAREN):
                keys.append(self.expr())
                self.eat(Tokens.COLON)
                vals.append(self.expr())
                self.skip_next_lines()
                if self.current_token.type != Tokens.RCPAREN:
                    self.eat(Tokens.COMMA, True)
            ending_pos = self.current_token.ending_pos
            self.eat(Tokens.RCPAREN)
            return dct(keys, vals, token.starting_pos, ending_pos, token.source)
        elif token.type == Tokens.SNBT:
            self.eat(Tokens.SNBT)
            return NBT(nbtworker.load(token.value), token.starting_pos, token.ending_pos, token.source)
        elif token.type == Tokens.VARIABLE:
            self.eat(Tokens.VARIABLE)
            if self.current_token.type == Tokens.LPAREN:
                self.eat(Tokens.LPAREN)
                sargs = self.get_args()
                ending_pos = self.current_token.ending_pos
                self.eat(Tokens.RPAREN)
                if token.giga is not None:
                    previous_operations, token.value, next_operations = giga_value(token,
                                                                                   self.get_giga_token(token.giga))
                    if len(previous_operations) + len(next_operations) > 0:
                        error_from_object(token, "", translate("error.unknown1"))
                res = calling_object(token.value, sargs, token.starting_pos, ending_pos, token.source).change()
                return res
            elif self.current_token.type == Tokens.DOUBLE_COLON:
                self.eat(Tokens.DOUBLE_COLON)
                act = self.current_token
                self.eat(Tokens.VARIABLE)
                if self.current_token.type == Tokens.SUBSTRING:
                    selector = self.current_token
                    self.eat(Tokens.SUBSTRING)
                    if selector.giga is not None:
                        selector.value = self.get_giga_token(selector.giga)
                else:
                    selector = None
                if token.value == "value" and (act.value in values):
                    value_type = values[act.value]["type"]
                    return value(act.value, token.starting_pos, act.ending_pos, token.source, selector=selector,
                                 value_type=value_type)
                if (token.value not in objects) or (not act.value in actions[token.value]):
                    error("SyntaxErrror",
                          translate("error.syntaxerror.action_cant_be_called_from_this_object",
                                    {0: act.value, 1: token.value}), token.starting_pos, act.ending_pos, token.source)
                self.eat(Tokens.LPAREN)
                args = self.get_args()
                ending_pos = self.current_token.ending_pos
                self.eat(Tokens.RPAREN)
                return action(token.value, act.value, args, token.starting_pos, ending_pos, self.source,
                              selector=selector)
            else:
                if not self.context.has_variable(token.value):
                    self.context.set_variable(token.value, Vars.LOCAL)
                    var_type = Vars.LOCAL
                    value_type = None
                else:
                    var_type = self.context.get_variable(token.value)
                    value_type = self.context.get_variable_type(var_type, token.value)
                return var(token.value if token.giga is None else self.get_giga_token(token.giga), var_type,
                           token.starting_pos, token.ending_pos, token.source,
                           value_type=value_type)
        elif token.type in {Tokens.LOCAL_VARIABLE, Tokens.BRACKET_VARIABLE, Tokens.INLINE_VARIABLE,
                            Tokens.GAME_VARIABLE,
                            Tokens.SAVE_VARIABLE}:
            if token.type == Tokens.LOCAL_VARIABLE:
                self.eat(Tokens.LOCAL_VARIABLE)
                var_type = Vars.LOCAL
            elif token.type == Tokens.BRACKET_VARIABLE:
                self.eat(Tokens.BRACKET_VARIABLE)
                var_type = Vars.BRACKET
            elif token.type == Tokens.INLINE_VARIABLE:
                self.eat(Tokens.INLINE_VARIABLE)
                var_type = Vars.INLINE
            elif token.type == Tokens.GAME_VARIABLE:
                self.eat(Tokens.GAME_VARIABLE)
                var_type = Vars.GAME
            elif token.type == Tokens.SAVE_VARIABLE:
                self.eat(Tokens.SAVE_VARIABLE)
                var_type = Vars.SAVE
            else:
                var_type = Vars.NONE
            if not self.context.has_variable(token.value):
                self.context.set_variable(token.value, var_type)
                value_type = None
            else:
                value_type = self.context.get_variable_type(var_type, token.value)
            return var(token.value if token.giga is None else self.get_giga_token(token.giga), var_type,
                       token.starting_pos, token.ending_pos, token.source, value_type=value_type)
        elif token.type == Tokens.IF:
            self.eat(Tokens.IF)
            cond = self.expr()
            true = self.expr()
            self.eat(Tokens.ELSE)
            false = self.expr()
            return if_else_expr(cond, true, false, true.starting_pos, false.ending_pos, true.source)
        else:
            error_from_object(token, "SyntaxError", translate("error.syntaxerror.unexpected_token",
                                                              {0: translate("token." + str(token.type) + ".name")}))

    def up_factor(self, result=None):
        if result is None:
            result = self.factor()
        if self.current_token.type == Tokens.DOT:
            self.eat(Tokens.DOT)
            act = self.current_token
            self.eat(Tokens.VARIABLE)
            if self.current_token.type == Tokens.LPAREN:
                if act.value in origin_actions:
                    self.eat(Tokens.LPAREN)
                    args = self.get_args()
                    obj = origin_actions[act.value]
                    args.unpositional[actions[obj][act.value]["origin"]] = result
                    ending_pos = self.current_token.ending_pos
                    self.eat(Tokens.RPAREN)
                    return self.up_factor(action(obj, act.value, args, result.starting_pos, ending_pos, self.source))
                else:
                    self.eat(Tokens.LPAREN)
                    args = self.get_args()
                    ending_pos = self.current_token.ending_pos
                    self.eat(Tokens.RPAREN)
                    args.positional.insert(0, result)
                    return self.up_factor(
                        calling_function(result, act.value, args, result.starting_pos, ending_pos, self.source))
            else:
                return self.up_factor(
                    calling_argument(result, act.value, result.starting_pos, act.ending_pos, self.source))
        elif self.current_token.type == Tokens.LSPAREN:
            self.eat(Tokens.LSPAREN)
            arg1 = self.up_factor()
            if self.current_token.type != Tokens.RSPAREN:
                self.eat(Tokens.COLON)
                arg2 = self.up_factor()
            else:
                arg2 = None
            ending_pos = self.current_token.ending_pos
            self.eat(Tokens.RSPAREN)
            return self.up_factor(subscript(result, arg1, arg2, result.starting_pos, ending_pos, result.source))
        elif self.current_token.type == Tokens.IF:
            self.eat(Tokens.IF)
            cond = self.expr()
            self.eat(Tokens.ELSE)
            false = self.expr()
            return if_else_expr(cond, result, false, result.starting_pos, false.ending_pos, result.source)
        elif self.current_token.type == Tokens.QUESTION_MARK:
            self.eat(Tokens.QUESTION_MARK)
            true = self.expr()
            self.eat(Tokens.COLON)
            false = self.expr()
            return if_else_expr(result, true, false, result.starting_pos, false.ending_pos, result.source)

        else:
            return result

    def get_args(self, reason_to_stop=Tokens.RPAREN, save_types=False):
        starting_pos = self.current_token.starting_pos
        ending_pos = self.current_token.ending_pos
        pos = []
        unpos = {}
        multi = 0
        now = False
        self.skip_next_lines()
        while (self.current_token.type != Tokens.EOF) and (self.current_token.type != reason_to_stop):
            if self.current_token.type == Tokens.VARIABLE and self.token(self.index + 1).type == Tokens.ASSIGN:
                token = self.current_token
                self.eat(Tokens.VARIABLE)
                self.eat(Tokens.ASSIGN)
                if (arg1 := self.expr()) is not None:
                    ending_pos = arg1.ending_pos
                    unpos[token.value] = arg1
            else:
                if self.current_token.type == Tokens.MULTIPLY and multi == 0:
                    self.eat(Tokens.MULTIPLY)
                    multi = 1
                    now = True
                elif self.current_token.type == Tokens.DOUBLE_MULTIPLY and multi < 2:
                    self.eat(Tokens.DOUBLE_MULTIPLY)
                    multi = 2
                    now = True
                if (arg1 := self.expr()) is not None:
                    if multi > 0 and not now:
                        error_from_object(arg1, "", translate("error.unknown2"))
                    if arg1.type == "variable" and self.current_token.type == Tokens.COLON and save_types:
                        self.eat(Tokens.COLON)
                        arg1.value_type = self.current_token.value
                        self.eat(Tokens.VARIABLE)
                    ending_pos = arg1.ending_pos
                    if now:
                        arg1 = unpacked_args(arg1, arg1.starting_pos, arg1.ending_pos, arg1.source, multi)
                    pos.append(arg1)
            self.skip_next_lines()
            if self.current_token.type != reason_to_stop:
                self.eat(Tokens.COMMA, True)
            now = False
        return calling_args(pos, unpos, starting_pos, ending_pos, self.source)

    def expr(self, lvl=-1, result=None):
        if self.current_token.type == Tokens.NOT:
            token = self.current_token
            self.eat(Tokens.NOT)
            result = self.expr()
            return calling_function(result, "__invert__",
                                    calling_args([], {}, token.starting_pos, result.ending_pos, token.source),
                                    token.starting_pos, result.ending_pos, token.source)
        if lvl == -1:
            result = self.expr(lvl + 1)
            if self.current_token.type == Tokens.IF:
                self.eat(Tokens.IF)
                cond = self.expr()
                self.eat(Tokens.ELSE)
                false = self.expr()
                return if_else_expr(cond, result, false, result.starting_pos, false.ending_pos, result.source)
            return result
        if lvl < len(self.Expr_priorities):
            if result is None:
                result = self.expr(lvl + 1)
            check_token = self.Expr_priorities[lvl]
            while (self.current_token.type != Tokens.EOF) and (
                    self.current_token.type == check_token):
                if self.current_token.type == Tokens.MINUS_NUMBER:
                    operation = "__subtract__"
                elif self.current_token.type == Tokens.PLUS_NUMBER:
                    operation = "__add__"
                else:
                    operation = self.Expr_operations[self.current_token.type]
                    self.eat(self.current_token.type)
                second = self.expr(lvl + 1)
                if check_token == Tokens.IN:
                    result, second = second, result
                result = calling_function(result, operation,
                                          calling_args([result, second], {}, result.starting_pos, second.ending_pos,
                                                       result.source), result.starting_pos, second.ending_pos,
                                          result.source)
            return result
        else:
            return self.up_factor(result)

    def get_vars(self):
        variables = []
        if self.current_token.type == Tokens.JMCC_DEFINE:
            self.eat(Tokens.JMCC_DEFINE)
            self.eat(Tokens.VAR_DEFINE)
            token = self.current_token
            self.eat(Tokens.VARIABLE)
            variable = var(token.value if token.giga is None else self.get_giga_token(token.giga), Vars.JMCC,
                           token.starting_pos, token.ending_pos, self.source)
            self.context.set_variable(token.value, Vars.JMCC)
        elif self.current_token.type == Tokens.SAVE_DEFINE:
            self.eat(Tokens.SAVE_DEFINE)
            self.eat(Tokens.VAR_DEFINE)
            token = self.current_token
            self.eat(Tokens.VARIABLE)
            variable = var(token.value if token.giga is None else self.get_giga_token(token.giga), Vars.SAVE,
                           token.starting_pos, token.ending_pos, self.source)
            self.context.set_variable(token.value, Vars.SAVE)
        elif self.current_token.type == Tokens.GAME_DEFINE:
            self.eat(Tokens.GAME_DEFINE)
            self.eat(Tokens.VAR_DEFINE)
            token = self.current_token
            self.eat(Tokens.VARIABLE)
            variable = var(token.value if token.giga is None else self.get_giga_token(token.giga), Vars.GAME,
                           token.starting_pos, token.ending_pos, self.source)
            self.context.set_variable(token.value, Vars.GAME)
        elif self.current_token.type == Tokens.LOCAL_DEFINE:
            self.eat(Tokens.LOCAL_DEFINE)
            self.eat(Tokens.VAR_DEFINE)
            token = self.current_token
            self.eat(Tokens.VARIABLE)
            variable = var(token.value if token.giga is None else self.get_giga_token(token.giga), Vars.LOCAL,
                           token.starting_pos, token.ending_pos, self.source)
            self.context.set_variable(token.value, Vars.LOCAL)
        elif self.current_token.type == Tokens.VAR_DEFINE:
            self.eat(Tokens.VAR_DEFINE)
            token = self.current_token
            self.eat(Tokens.VARIABLE)
            variable = var(token.value if token.giga is None else self.get_giga_token(token.giga), Vars.LOCAL,
                           token.starting_pos, token.ending_pos, self.source)
            self.context.set_variable(token.value, Vars.LOCAL)
        elif self.current_token.type == Tokens.BRACKET_DEFINE:
            self.eat(Tokens.BRACKET_DEFINE)
            self.eat(Tokens.VAR_DEFINE)
            token = self.current_token
            self.eat(Tokens.VARIABLE)
            variable = var(token.value if token.giga is None else self.get_giga_token(token.giga), Vars.BRACKET,
                           token.starting_pos, token.ending_pos, self.source)
            self.context.set_variable(token.value, Vars.BRACKET)
        elif self.current_token.type == Tokens.INLINE_DEFINE:
            self.eat(Tokens.INLINE_DEFINE)
            self.eat(Tokens.VAR_DEFINE)
            token = self.current_token
            self.eat(Tokens.VARIABLE)
            variable = var(token.value if token.giga is None else self.get_giga_token(token.giga), Vars.INLINE,
                           token.starting_pos, token.ending_pos, self.source)
            self.context.set_variable(token.value, Vars.INLINE)
        elif self.current_token.type in {Tokens.VARIABLE, Tokens.LOCAL_VARIABLE, Tokens.SAVE_VARIABLE,
                                         Tokens.GAME_VARIABLE, Tokens.BRACKET_VARIABLE,
                                         Tokens.INLINE_VARIABLE} and self.token(
            self.index + 1).type != Tokens.DOUBLE_COLON:
            variable = self.factor()
        else:
            return variables
        if self.current_token.type == Tokens.COLON:
            self.eat(Tokens.COLON)
            variable.value_type = self.current_token.value
            if variable.var_type == Vars.INLINE:
                spec = self.context.get_inline(variable.value)
                if isinstance(spec, var):
                    spec.value_type = variable.get_real_type()
                    self.context.set_variable_type(spec.var_type, spec.value, spec.get_real_type())
            self.context.set_variable_type(variable.var_type, variable.value, variable.get_real_type())
            self.eat(Tokens.VARIABLE)
        if self.current_token.type == Tokens.COMMA:
            variables.append(self.up_factor(variable))
            self.eat(Tokens.COMMA)
            variables.extend(self.get_vars())
        else:
            variables.append(self.up_factor(variable))
        return variables

    def try_get_function(self):
        used_decorators = False
        overload = None
        description = None
        icon = None
        hide = False
        arg_description = None
        return_var = None
        return_var_description = None
        property_ = None
        while self.current_token.type == Tokens.DECORATOR:
            used_decorators = True
            self.eat(Tokens.DECORATOR)
            name = self.current_token
            if self.current_token.type != Tokens.VARIABLE:
                self.eat(Tokens.VARIABLE)
            if name.value == "overload":
                self.eat(Tokens.VARIABLE)
                overload = True
            elif name.value == "hidden":
                self.eat(Tokens.VARIABLE)
                hide = True
            elif name.value == "description":
                self.eat(Tokens.VARIABLE)
                self.eat(Tokens.LPAREN)
                description = []
                while self.current_token.type != Tokens.RPAREN:
                    description.append(self.expr())
                    if self.current_token.type != Tokens.RPAREN:
                        self.eat(Tokens.COMMA)
                self.eat(Tokens.RPAREN)
            elif name.value == "item" and self.token(self.index + 1).type == Tokens.LPAREN:
                icon = self.expr()
            elif name.value == "args":
                self.eat(Tokens.VARIABLE)
                self.eat(Tokens.LPAREN)
                arg_description = {}
                while self.current_token.type != Tokens.RPAREN:
                    key = self.current_token.value
                    self.eat(Tokens.VARIABLE)
                    self.eat(Tokens.COLON)
                    value = self.current_token.value
                    self.eat(Tokens.STRING)
                    arg_description[key] = value
                    if self.current_token.type != Tokens.RPAREN:
                        self.eat(Tokens.COMMA)
                self.eat(Tokens.RPAREN)
            elif name.value == "returns":
                self.eat(Tokens.VARIABLE)
                self.eat(Tokens.LPAREN)
                if self.current_token.type in {Tokens.VARIABLE, Tokens.BRACKET_VARIABLE, Tokens.SAVE_VARIABLE,
                                               Tokens.LOCAL_VARIABLE, Tokens.GAME_VARIABLE}:
                    return_var = self.expr()
                    if self.current_token.type != Tokens.RPAREN:
                        self.eat(Tokens.COMMA)
                if self.current_token.type != Tokens.RPAREN:
                    return_var_description = self.current_token.value
                    self.eat(Tokens.STRING)
                self.eat(Tokens.RPAREN)
            elif name.value in ("setter", "getter") and len(self.context.settings["class_define"]) > 0:
                property_ = name.value
                self.eat(Tokens.VARIABLE)
            else:
                error_from_object(name, "", translate("error.unknown3"))
            self.eat(Tokens.NEXT_LINE)
        if ((self.current_token.type == Tokens.FUNCTION_DEFINE and (
                self.context.context_lvl == 0 or len(self.context.settings["class_define"]) > 0))
                or (self.current_token.type == Tokens.INLINE_DEFINE
                    and self.token(self.index + 1).type == Tokens.FUNCTION_DEFINE)):
            if self.current_token.type == Tokens.INLINE_DEFINE:
                self.eat(Tokens.INLINE_DEFINE)
                inline = True
            else:
                inline = True in self.context.settings["inline_define"]
            self.eat(Tokens.FUNCTION_DEFINE)
            token = self.current_token
            self.eat(Tokens.VARIABLE)
            if self.current_token.type == Tokens.LPAREN:
                self.eat(Tokens.LPAREN)
                args = self.get_args(save_types=True)
                self.eat(Tokens.RPAREN)
            else:
                args = calling_args([], {}, token.starting_pos, token.ending_pos, token.source)
            if self.current_token.type == Tokens.CYCLE_THING:
                self.eat(Tokens.CYCLE_THING)
                return_var_type = self.current_token.value
                self.eat(Tokens.VARIABLE)
            else:
                return_var_type = None
            token_value = [self.current_token]
            self.eat(Tokens.LCPAREN)
            count = 1
            allow_return = False
            while (self.current_token.type != Tokens.EOF) and (count != 0):
                token_value.append(self.current_token)
                if self.current_token.type == Tokens.LCPAREN:
                    count += 1
                elif self.current_token.type == Tokens.RCPAREN:
                    count -= 1
                if self.current_token.type == Tokens.RETURN and (
                        self.token(self.index + 1).type not in {Tokens.NEXT_LINE, Tokens.SEMICOLON}):
                    allow_return = True
                self.eat(self.current_token.type)
            if allow_return or return_var_type is not None:
                if return_var is None:
                    return_var = var(f"jmcc.{new('var')}", Vars.LOCAL if not inline else Vars.INLINE,
                                     token.starting_pos, token.ending_pos,
                                     token.source)
                return_var.value_type = return_var_type
                if return_var_description is not None and return_var is not None:
                    if arg_description is None:
                        arg_description = {}
                    arg_description[return_var.value] = return_var_description
            if property_ is not None:
                token.value = f"{token.value}.{property_}"
            result = function(token.value, token_value, args, self.source, inline=inline, return_var=return_var,
                              ready=False, description=description, icon=icon, hide=hide,
                              args_description=arg_description, property_=property_)
            if len(self.context.settings["class_define"]) > 0:
                result.name = f"{self.context.settings['class_define'][-1]}.{result.name}"
            if self.context.has_special(result.name):
                if not overload:
                    error_from_object(token, "NameError", translate("error.nameerror.special_cant_be_rewritten"))
                else:
                    result.name = f"{result.name}.{new('function_' + result.name)}"
                    self.context.set_special(token.value,
                                             self.context.get_special(token.value).add_overload(result.special()))
            elif result.name in {"block", "enum"}:
                error_from_object(token, "NameError", translate("error.nameerror.special_cant_be_rewritten"))
            else:
                self.context.set_special(token.value, result.special())
            return result if not result.inline else None
        elif self.current_token.type == Tokens.PROCESS_DEFINE and (
                self.context.context_lvl == 0 or len(self.context.settings["class_define"]) > 0):
            self.eat(Tokens.PROCESS_DEFINE)
            token = self.current_token
            self.eat(Tokens.VARIABLE)
            if self.current_token.type == Tokens.LPAREN:
                self.eat(Tokens.LPAREN)
                args = self.get_args(save_types=True)
                self.eat(Tokens.RPAREN)
            else:
                args = calling_args([], {}, token.starting_pos, token.ending_pos, token.source)
            token_value = [self.current_token]
            self.eat(Tokens.LCPAREN)
            count = 1
            while (self.current_token.type != Tokens.EOF) and (count != 0):
                token_value.append(self.current_token)
                if self.current_token.type == Tokens.LCPAREN:
                    count += 1
                elif self.current_token.type == Tokens.RCPAREN:
                    count -= 1
                self.eat(self.current_token.type)
            result = process(token.value, token_value, args, self.source, ready=False, description=description,
                             icon=icon, hide=hide, args_description=arg_description)
            if len(self.context.settings["class_define"]) > 0:
                result.name = f"{self.context.settings['class_define'][-1]}.{result.name}"
            if self.context.has_special(token.value):
                if not overload:
                    error_from_object(token, "NameError", translate("error.nameerror.special_cant_be_rewritten"))
                else:
                    result.name = f"{result.name}.{new(result.name)}"
                    self.context.set_special(token.value,
                                             self.context.get_special(token.value).add_overload(result.special()))
            elif result.name in {"block", "enum"}:
                error_from_object(token, "NameError", translate("error.nameerror.special_cant_be_rewritten"))
            else:
                self.context.set_special(token.value, result.special())
            return result
        if used_decorators:
            error_from_object(self.current_token, "FunctionError", translate("error.classerror.expected_function", {
                0: translate('token.' + str(self.current_token.type) + '.name')}))
        return 0

    def statement(self):
        if (self.current_token.type == Tokens.IMPORT or (self.current_token.type == Tokens.INLINE_DEFINE and self.token(
                self.index + 1).type == Tokens.IMPORT)) and self.context.context_lvl == 0:
            if self.current_token.type == Tokens.INLINE_DEFINE:
                inline = True
                self.eat(Tokens.INLINE_DEFINE)
            else:
                inline = False
            self.eat(Tokens.IMPORT)
            thing = self.current_token
            self.eat(Tokens.STRING)
            if os.path.exists(thing.value):
                fil_source = os.path.abspath(thing.value)
                if (fil_source in Context.context) and (not Context(fil_source).compiled):
                    error_from_object(thing, "RecursionError", translate("error.importerror.recursion"))
                if os.path.isfile(thing.value):
                    if thing.value.endswith(".jc"):
                        self.context.extend(parse_from_file(open(thing.value, "r", encoding="UTF-8")))
                    elif thing.value.endswith(".json") and False:
                        self.context.extend(parse_from_json(open(thing.value, "r", encoding="UTF-8")))
                    else:
                        error_from_object(thing, "UnknownFileFormat",
                                          translate("error.unknownfileformat", {0: thing.value}))
                elif os.path.isdir(thing.value):
                    self.context.extend(parse_from_directory(thing.value))
                else:
                    error_from_object(thing, "UnknownFile", translate("error.unknownfile", {0: thing.value}))
            else:
                error_from_object(thing, "UnexistsFile", translate("error.unexistsfile", {0: thing.value}))
            return
        elif self.current_token.type == Tokens.EVENT_DEFINE and self.context.context_lvl == 0 and len(
                self.context.settings["class_define"]) == 0:
            self.eat(Tokens.EVENT_DEFINE)
            token = self.current_token
            self.eat(Tokens.SUBSTRING)
            token_value = [self.current_token]
            self.eat(Tokens.LCPAREN)
            count = 1
            while (self.current_token.type != Tokens.EOF) and (count != 0):
                token_value.append(self.current_token)
                if self.current_token.type == Tokens.LCPAREN:
                    count += 1
                elif self.current_token.type == Tokens.RCPAREN:
                    count -= 1
                self.eat(self.current_token.type)
            if token.value not in events:
                error_from_object(token, "NameError", translate("error.unexistsevent", insert={0: token.value}))
            return event(token.value, token_value, self.source, ready=False)
        elif self.current_token.type == Tokens.IF:
            token = self.current_token
            self.eat(Tokens.IF)
            main_condition = self.expr()
            if self.current_token.type != Tokens.LCPAREN:
                self.context.next_lvl()
                main_op = self.statement()
                if main_op is None:
                    self.eat(Tokens.LCPAREN)
                self.context.add_operation(main_op)
                self.context.update()
                main_ops = self.context.get_operations()
                self.context.previous_lvl()
                if self.current_token.type == Tokens.ELSE:
                    self.eat(Tokens.ELSE)
                    self.context.next_lvl()
                    else_op = self.statement()
                    if else_op is None:
                        self.eat(Tokens.LCPAREN)
                    self.context.add_operation(else_op)
                    self.context.update()
                    els = self.context.get_operations()
                    self.context.previous_lvl()
                    ending_pos = else_op.ending_pos
                else:
                    els = []
                    ending_pos = main_op.ending_pos
                eli = []
            else:
                self.eat(Tokens.LCPAREN)
                self.context.next_lvl()
                while (self.current_token.type != Tokens.EOF) and (self.current_token.type != Tokens.RCPAREN):
                    self.context.add_operation(self.up_statement(Tokens.RCPAREN))
                    self.context.update()
                main_ops = self.context.get_operations()
                self.context.previous_lvl()
                ending_pos = self.current_token.ending_pos
                self.eat(Tokens.RCPAREN)
                found = False
                cur_index = self.index
                self.skip_next_lines()
                eli = []
                while (self.current_token.type != Tokens.EOF) and (
                        self.current_token.type == Tokens.ELIF or (self.current_token.type == Tokens.ELSE
                                                                   and self.token(self.index + 1).type == Tokens.IF)):
                    found = True

                    if self.current_token.type == Tokens.ELIF:
                        self.eat(Tokens.ELIF)
                    else:
                        self.eat(Tokens.ELSE)
                        self.eat(Tokens.IF)
                    condition = self.expr()
                    self.eat(Tokens.LCPAREN)
                    self.context.next_lvl()
                    while (self.current_token.type != Tokens.EOF) and (self.current_token.type != Tokens.RCPAREN):
                        self.context.add_operation(self.up_statement(Tokens.RCPAREN))
                        self.context.update()
                    ops = self.context.get_operations()
                    self.context.previous_lvl()
                    ending_pos = self.current_token.ending_pos
                    self.eat(Tokens.RCPAREN)
                    eli.append([condition, ops])
                    cur_index = self.index
                    self.skip_next_lines()
                els = []
                if self.current_token.type == Tokens.ELSE:
                    found = True
                    self.eat(Tokens.ELSE)
                    self.eat(Tokens.LCPAREN)
                    self.context.next_lvl()
                    while (self.current_token.type != Tokens.EOF) and (self.current_token.type != Tokens.RCPAREN):
                        self.context.add_operation(self.up_statement(Tokens.RCPAREN))
                        self.context.update()
                    els.extend(self.context.get_operations())
                    self.context.previous_lvl()
                    ending_pos = self.current_token.ending_pos
                    self.eat(Tokens.RCPAREN)
                if not found:
                    self.index = cur_index
                    self.current_token = self.token(self.index)
            return if_(main_condition, main_ops, eli, els, token.starting_pos, ending_pos, self.source)
        elif self.current_token.type == Tokens.RETURN and len(self.context.settings["allow_returns"]) > 0:
            starting_pos = self.current_token.starting_pos
            ending_pos = self.current_token.ending_pos
            self.eat(Tokens.RETURN)
            if self.current_token.type == Tokens.NEXT_LINE:
                obj = None
                self.eat(Tokens.NEXT_LINE)
            elif self.current_token.type == Tokens.SEMICOLON:
                obj = None
                self.eat(Tokens.SEMICOLON)
            else:
                obj = self.expr()
                ending_pos = obj.ending_pos
            if obj is not None:
                obej = return_(obj, starting_pos, ending_pos, self.source,
                               in_var=self.context.settings["allow_returns"][-1])
            else:
                obej = action("code", "return_function", calling_args([], {}, starting_pos, ending_pos, self.source),
                              starting_pos, ending_pos, self.source)
            return obej
        elif self.current_token.type == Tokens.CLASS_DEFINE or (self.current_token.type == Tokens.INLINE_DEFINE
                                                                and self.token(
                    self.index + 1).type == Tokens.CLASS_DEFINE):
            if self.current_token.type == Tokens.INLINE_DEFINE:
                self.eat(Tokens.INLINE_DEFINE)
                inline = True
            else:
                inline = True in self.context.settings["inline_define"]
            self.eat(Tokens.CLASS_DEFINE)
            token = self.current_token
            self.eat(Tokens.VARIABLE)
            self.context.next_lvl()
            if self.current_token.type == Tokens.LPAREN:
                self.eat(Tokens.LPAREN)
                parent = self.current_token.value
                if not self.context.has_special(parent):
                    error_from_object(self.current_token, "", translate("ашипка нет атца", {0: parent}))
                self.eat(Tokens.VARIABLE)
                self.eat(Tokens.RPAREN)
            else:
                parent = None
            class_ind = new(f"class_{token.value}")
            self.context.settings["class_define"].append(f"{token.value}{class_ind if class_ind != 0 else ''}")
            self.context.settings["inline_define"].append(inline)
            self.eat(Tokens.LCPAREN)
            functions = []
            class_obj = None
            while (self.current_token.type != Tokens.EOF) and (self.current_token.type != Tokens.RCPAREN):
                if (a := self.up_statement(Tokens.RCPAREN)) is not None:
                    if isinstance(a, (function, process, class_)):
                        functions.append(a)
                    else:
                        if isinstance(a, assign) and a.assign_type is None and len(a.variables) == 1 and a.variables[
                            -1].value in {"__dict__", "__custom__", "__slots__"}:
                            if a.variables[-1].value == "__dict__":
                                if isinstance(a.object, (dct, lst)):
                                    def_values = {a.object.keys[index1].value: a.object.values[index1] for index1 in
                                                  range(len(a.object.values))} if isinstance(a.object, dct) else {
                                        a.object.values[index1].value: None for index1 in range(len(a.object.values))}
                                    class_obj = class_object(token.value,
                                                             dct([], [], token.starting_pos, token.ending_pos,
                                                                 token.source), def_values, token.starting_pos,
                                                             token.ending_pos, self.source)
                            elif a.variables[-1].value == "__slots__":
                                if isinstance(a.object, (dct, lst)):
                                    def_values = {a.object.keys[index1].value: a.object.values[index1] for index1 in
                                                  range(len(a.object.values))} if isinstance(a.object, dct) else {
                                        a.object.values[index1].value: None for index1 in range(len(a.object.values))}
                                    class_obj = class_object(token.value, lst([], token.starting_pos, token.ending_pos,
                                                                              token.source), def_values,
                                                             token.starting_pos,
                                                             token.ending_pos, self.source)
                            else:
                                class_obj = class_object(token.value, a.object, {}, token.starting_pos,
                                                         token.ending_pos, self.source)
                        self.context.add_operation(a)
                self.context.update()
            self.eat(Tokens.RCPAREN)
            ops = self.context.get_operations()
            del self.context.settings["class_define"][-1]
            del self.context.settings["inline_define"][-1]
            specials = self.context.get_specials()
            if class_obj is None and parent is None:
                class_obj = class_object(token.value, dct([], [], token.starting_pos, token.ending_pos, token.source),
                                         {}, token.starting_pos, token.ending_pos, token.source)
            self.context.previous_lvl()
            result = class_(token.value, parent, ops, functions, specials, self.source, class_obj, inline)
            if len(self.context.settings["class_define"]) > 0:
                result.name = f"{self.context.settings['class_define'][-1]}.{result.name}"
            if self.context.has_special(token.value) and token.value != parent:
                error_from_object(token, "NameError", translate("error.nameerror.special_cant_be_rewritten"))
            if token.value in {"block", "enum"}:
                error_from_object(token, "NameError", translate("error.nameerror.special_cant_be_rewritten"))
            self.context.set_special(token.value, result.special())
            return result if result.inline is False else None

        else:
            result = self.try_get_function()
            if result != 0:
                return result
            variables = self.get_vars()
            if len(variables) == 1:
                if variables[0].is_independent():
                    return variables[0]
            if len(variables) > 0:
                if self.current_token.type == Tokens.ASSIGN:
                    self.eat(Tokens.ASSIGN)
                    assign_type = None
                elif self.current_token.type == Tokens.PLUS_ASSIGN:
                    self.eat(Tokens.PLUS_ASSIGN)
                    assign_type = "__add__"
                elif self.current_token.type == Tokens.MINUS_ASSIGN:
                    self.eat(Tokens.MINUS_ASSIGN)
                    assign_type = "__minus__"
                elif self.current_token.type == Tokens.MULTIPLY_ASSIGN:
                    self.eat(Tokens.MULTIPLY_ASSIGN)
                    assign_type = "__subtract__"
                elif self.current_token.type == Tokens.DIVIDE_ASSIGN:
                    self.eat(Tokens.DIVIDE_ASSIGN)
                    assign_type = "__divide__"
                elif self.current_token.type == Tokens.PR_ASSIGN:
                    self.eat(Tokens.PR_ASSIGN)
                    assign_type = "__remainder__"
                elif self.current_token.type == Tokens.DEG_ASSIGN:
                    self.eat(Tokens.DEG_ASSIGN)
                    assign_type = "__pow__"
                else:
                    for i3 in variables:
                        if i3.get_type() == "variable":
                            if i3.value_type is not None:
                                self.context.set_variable_type(i3.var_type, i3.value, i3.value_type)
                    return
                obj = self.expr()
                return assign(variables, assign_type, obj, variables[0].starting_pos, obj.ending_pos, self.source)

        if len(self.context.settings["class_define"]) > 0:
            error_from_object(self.current_token, "ClassError", translate("error.classerror.expected_function", {
                0: translate('token.' + str(self.current_token.type) + '.name')}))
        obj = self.expr()
        if obj.type == "action":
            if actions[obj.object][obj.name]["type"].startswith(
                    "container"):
                if self.current_token.type == Tokens.LCPAREN and (
                        not actions[obj.object][obj.name].setdefault("boolean", False)):
                    self.eat(Tokens.LCPAREN)
                    if "lambda" in actions[obj.object][obj.name] and self.current_token.type != Tokens.NEXT_LINE:
                        lambd = []
                        while (self.current_token.type != Tokens.EOF) and (
                                self.current_token.type != Tokens.CYCLE_THING):
                            if (a := self.expr()) is not None:
                                lambd.append(a)
                            if self.current_token.type != Tokens.CYCLE_THING:
                                self.eat(Tokens.COMMA)
                        self.eat(Tokens.CYCLE_THING)
                    else:
                        lambd = None
                    self.context.next_lvl()
                    while (self.current_token.type != Tokens.EOF) and (self.current_token.type != Tokens.RCPAREN):
                        self.context.add_operation(self.up_statement(Tokens.RCPAREN))
                        self.context.update()
                    ops = self.context.get_operations()
                    self.context.previous_lvl()
                    self.eat(Tokens.RCPAREN)
                else:
                    ops = None
                    lambd = None
            else:
                ops = None
                lambd = None
            obj.operations = ops
            obj.lambd = lambd
        return obj

    def skip_next_lines(self):
        while self.current_token.type == Tokens.NEXT_LINE:
            self.eat(self.current_token.type)

    def up_statement(self, end_reason=None):
        self.skip_next_lines()
        if self.current_token.type == Tokens.EOF or (end_reason is not None and self.current_token.type == end_reason):
            return
        jmcc_obj = self.statement()
        if end_reason is not None:
            cur_index = self.index
            self.skip_next_lines()
            if self.current_token.type == end_reason:
                return jmcc_obj
            else:
                self.index = cur_index
                self.current_token = self.token(self.index)
        if self.current_token.type == Tokens.NEXT_LINE:
            self.eat(Tokens.NEXT_LINE)
        elif self.current_token.type == Tokens.SEMICOLON:
            self.eat(Tokens.SEMICOLON)
        elif self.current_token.type != Tokens.EOF:
            error_from_object(self.current_token, "SyntaxError",
                              translate("error.syntaxerror.statements_not_separated"))
        return jmcc_obj

    def parse(self):
        while self.current_token.type != Tokens.EOF:
            self.context.add_operation(self.up_statement())
            self.context.update()
        for i1 in self.context.get_operations():
            if not i1.is_ready():
                self.index = 0
                self.tokens = i1.operations
                self.current_token = self.token(self.index)
                self.eat(Tokens.LCPAREN)
                self.context.next_lvl()
                self.context.next_jmcc_lvl()
                if isinstance(i1, function):
                    for i2 in i1.special().args:
                        self.context.set_variable_type(Vars.LOCAL, i2["id"], i2["type"])
                        self.context.set_variable(i2["id"], Vars.LOCAL)
                    self.context.update()
                    self.context.settings["allow_returns"].append(i1.return_var)
                    while (self.current_token.type != Tokens.EOF) and (self.current_token.type != Tokens.RCPAREN):
                        self.context.add_operation(self.up_statement(Tokens.RCPAREN))
                        self.context.update()
                    del self.context.settings["allow_returns"][-1]
                elif isinstance(i1, (process, event)):
                    if isinstance(i1, process):
                        for i2 in i1.special().args:
                            self.context.set_variable_type(Vars.LOCAL, i2["id"], i2["type"])
                            self.context.set_variable(i2["id"], Vars.LOCAL)
                        self.context.update()
                    while (self.current_token.type != Tokens.EOF) and (self.current_token.type != Tokens.RCPAREN):
                        self.context.add_operation(self.up_statement(Tokens.RCPAREN))
                        self.context.update()
                else:
                    error_from_object(i1, "", translate("error.unknown4"))
                self.context.previous_jmcc_lvl()
                ops = self.context.get_operations()
                i1.operations = ops
                self.context.previous_lvl()
                self.eat(Tokens.RCPAREN)
                i1.ready = True
        self.context.compiled = True
        if self.context.get_property("create_world_restart_function", False):
            cringe = {"start": [], "stop": [], "join": [], "quit": []}
            for i1 in self.context.get_operations():
                if i1.type == "event":
                    if i1.name == "world_start":
                        cringe["start"].append(i1.operations)
                    elif i1.name == "world_stop":
                        cringe["stop"].append(i1.operations)
                    elif i1.name == "player_join":
                        new_ops = []
                        for op in i1.operations:
                            if not (op.type == "action" and op.object == "world" and op.name == "hide_event_message"):
                                new_ops.append(op)
                        cringe["join"].append(new_ops)
                    elif i1.name == "player_quit":
                        new_ops = []
                        for op in i1.operations:
                            if not (op.type == "action" and op.object == "world" and op.name == "hide_event_message"):
                                new_ops.append(op)
                        cringe["quit"].append(new_ops)
            self.context.next_lvl()
            self.context.add_operations(
                [action("code", "wait", calling_args([number(20, -1, -1, None)], {}, -1, -1, None), -1, -1, None)])
            waiter_ops = self.context.get_operations()
            self.context.previous_lvl()
            waiter = action("repeat", "while",
                            calling_args([], {"conditional": action("variable", "greater_or_equals", calling_args(
                                [value("cpu_usage", -1, -1, None), number(40, -1, -1, None)], {}, -1, -1, None), -1, -1,
                                                                    None)}, -1, -1, None), -1, -1, None,
                            operations=waiter_ops)
            self.context.next_lvl()
            self.context.next_lvl()
            quit_ops = []
            for i1 in cringe["quit"]:
                quit_ops.append(action("variable", "purge", calling_args(
                    [text("", Texts.PLAIN, -1, -1, None), enum_("LOCAL", -1, -1, None),
                     enum_("NAME_CONTAINS", -1, -1, None), enum_("TRUE", -1, -1, None)], {}, -1, -1, None),
                                       -1, -1, None))
                quit_ops.extend(i1)
                quit_ops.append(waiter)
            quit_ops.append(
                action("player", "clear_inventory", calling_args([enum_("ENTIRE", -1, -1, None)], {}, -1, -1, None), -1,
                       -1, None, selector="default_player"))
            quit_ops.append(
                action("player", "teleport", calling_args(
                    [value("spawn_location", -1, -1, None), enum_("FALSE", -1, -1, None), enum_("FALSE", -1, -1, None),
                     enum_("TRUE", -1, -1, None)], {}, -1, -1, None), -1,
                       -1, None, selector="default_player"))
            self.context.add_operations(quit_ops)
            quit_ops = self.context.get_operations()
            self.context.previous_lvl()
            self.context.next_lvl()
            join_ops = []
            for i1 in cringe["join"]:
                join_ops.append(action("variable", "purge", calling_args(
                    [text("", Texts.PLAIN, -1, -1, None), enum_("LOCAL", -1, -1, None),
                     enum_("NAME_CONTAINS", -1, -1, None), enum_("TRUE", -1, -1, None)], {}, -1, -1, None),
                                       -1, -1, None))
                join_ops.extend(i1)
                join_ops.append(waiter)
            self.context.add_operations(join_ops)
            join_ops = self.context.get_operations()
            self.context.previous_lvl()
            player_quit_process = f"jmcc.{new('process')}"
            player_join_process = f"jmcc.{new('process')}"
            ops = [action("select", "all_players", calling_args([], {}, -1, -1, None), -1, -1, None),
                   action("code", "start_process", calling_args([], {
                       "process_name": text(player_quit_process, Texts.LEGACY, -1, -1, None),
                       "target_mode": enum_("FOR_EACH_IN_SELECTION", -1, -1, None),
                       "local_variables_mode": enum_("DONT_COPY", -1, -1, None)}, -1, -1, None), -1, -1, None)]
            player_quit = process(player_quit_process, quit_ops, calling_args([], {}, -1, -1, None), self.source)
            player_join = process(player_join_process, join_ops, calling_args([], {}, -1, -1, None), self.source)
            for i1 in cringe["stop"]:
                ops.append(action("variable", "purge", calling_args(
                    [text("", Texts.PLAIN, -1, -1, None), enum_("LOCAL", -1, -1, None),
                     enum_("NAME_CONTAINS", -1, -1, None), enum_("TRUE", -1, -1, None)], {}, -1, -1, None),
                                  -1, -1, None))
                ops.extend(i1)
                ops.append(waiter)
            ops.append(
                action("code", "wait", calling_args([number(5, -1, -1, None)], {}, -1, -1, None), -1, -1, None))
            ops.append(action("variable", "purge", calling_args(
                [text("", Texts.PLAIN, -1, -1, None), enum_("GAME", -1, -1, None),
                 enum_("NAME_CONTAINS", -1, -1, None), enum_("TRUE", -1, -1, None)], {}, -1, -1, None),
                              -1, -1, None))
            ops.append(
                action("player", "message", calling_args(
                    [text("&9Creative &8» &fМир запущен в режиме строительства", Texts.LEGACY, -1, -1, None)], {}, -1,
                    -1, None), -1, -1, None, selector="all_players"))
            ops.append(
                action("code", "wait", calling_args([number(95, -1, -1, None)], {}, -1, -1, None), -1, -1, None))
            ops.append(waiter)
            ops.append(
                action("player", "message", calling_args(
                    [text("&9Creative &8» &fМир запущен в режиме игры", Texts.LEGACY, -1, -1, None)], {}, -1,
                    -1, None), -1, -1, None, selector="all_players"))
            for i1 in cringe["start"]:
                ops.append(action("variable", "purge", calling_args(
                    [text("", Texts.PLAIN, -1, -1, None), enum_("LOCAL", -1, -1, None),
                     enum_("NAME_CONTAINS", -1, -1, None), enum_("TRUE", -1, -1, None)], {}, -1, -1, None),
                                  -1, -1, None))
                ops.extend(i1)
                ops.append(waiter)
            ops.append(action("variable", "purge", calling_args(
                [text("", Texts.PLAIN, -1, -1, None), enum_("LOCAL", -1, -1, None),
                 enum_("NAME_CONTAINS", -1, -1, None), enum_("TRUE", -1, -1, None)], {}, -1, -1, None),
                              -1, -1, None))
            ops.extend([action("select", "all_players", calling_args([], {}, -1, -1, None), -1, -1, None),
                        action("code", "start_process", calling_args([], {
                            "process_name": text(player_join_process, Texts.LEGACY, -1, -1, None),
                            "target_mode": enum_("FOR_EACH_IN_SELECTION", -1, -1, None),
                            "local_variables_mode": enum_("DONT_COPY", -1, -1, None)}, -1, -1, None), -1, -1, None)])
            self.context.add_operations(ops)
            ops = self.context.get_operations()
            self.context.previous_lvl()
            a = function("world_restart", ops, calling_args([], {}, -1, -1, None), self.source)
            self.context.add_operation(player_join)
            self.context.add_operation(player_quit)
            self.context.add_operation(a)
            self.context.update()

        del Context.sources[-1]
        return self.context


class Context:
    __slots__ = ("source", "idx", "json_obj")
    context = {}
    sources = []
    default_context = {"operations": [], "variables": {}, "vars": {0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}},
                       "inline_vars": {}, "callable": {}}
    default_cur_context = copy.deepcopy(default_context)
    ignore_next_else = False
    abort_current_context = False
    del default_cur_context["operations"]

    def __init__(self, source):
        self.source = source
        if self.source not in self.context:
            self.context[self.source] = {"context_lvl": 0, 0: copy.deepcopy(self.default_context),
                                         "cur_context": None,
                                         "compiled": False,
                                         "settings": {"allow_returns": [], "inline": [],
                                                      "class_define": [], "inline_define": []},
                                         "properties": {},
                                         "jmcc_lvl": 0,
                                         "jmcc": {0: {}}}
            self.context[self.source]["cur_context"] = {0: copy.deepcopy(self.default_cur_context)}
        self.idx = 0
        self.json_obj = {}

    @property
    def cur_context(self):
        return self.context[self.source]["cur_context"][self.context_lvl]

    @cur_context.setter
    def cur_context(self, val):
        self.context[self.source]["cur_context"][self.context_lvl] = val

    @property
    def context_lvl(self):
        return self.context[self.source]["context_lvl"]

    @context_lvl.setter
    def context_lvl(self, val):
        self.context[self.source]["context_lvl"] = val

    @property
    def jmcc_lvl(self):
        return self.context[self.source]["jmcc_lvl"]

    @jmcc_lvl.setter
    def jmcc_lvl(self, val):
        self.context[self.source]["jmcc_lvl"] = val

    @property
    def compiled(self):
        return self.context[self.source]["compiled"]

    @compiled.setter
    def compiled(self, val):
        self.context[self.source]["compiled"] = val

    @property
    def settings(self):
        return self.context[self.source]["settings"]

    @settings.setter
    def settings(self, val):
        self.context[self.source]["settings"] = val

    def add_operation(self, jmcc_obj):
        if jmcc_obj is None:
            return
        if jmcc_obj.is_independent():
            if jmcc_obj.is_simple():
                if self.context_lvl == 0 and not (jmcc_obj.type in ("function", "process", "event")):
                    if len(self.context[self.source][self.context_lvl]["operations"]) == 0:
                        self.context[self.source][self.context_lvl]["operations"].append(
                            event("world_start", [], self.source))
                    elif self.context[self.source][self.context_lvl]["operations"][0].type != "event":
                        self.context[self.source][self.context_lvl]["operations"].insert(0, event("world_start", [],
                                                                                                  self.source))
                    elif self.context[self.source][self.context_lvl]["operations"][0].name != "world_start":
                        self.context[self.source][self.context_lvl]["operations"].insert(0, event("world_start", [],
                                                                                                  self.source))
                    self.context[self.source][self.context_lvl]["operations"][0].operations.append(jmcc_obj)
                else:
                    self.context[self.source][self.context_lvl]["operations"].append(jmcc_obj)
            else:
                prev_ops, cur_op, next_ops = jmcc_obj.simplify()
                self.add_operations(prev_ops)
                self.add_operation(cur_op)
                self.add_operations(next_ops)

    def add_operations(self, lst1):
        for jmc_obj in lst1:
            self.add_operation(jmc_obj)

    def get_operations(self):
        return self.context[self.source][self.context_lvl]["operations"]

    def clear_operations(self):
        self.context[self.source][self.context_lvl]["operations"] = []

    def set_variable(self, var_name, var_type):
        self.cur_context["variables"][var_name] = var_type

    def set_properties(self, properties):
        self.context[self.source]["properties"] = properties

    def get_jmcc(self, var_name):
        if var_name in self.context[self.source]["jmcc"][self.jmcc_lvl]:
            return self.context[self.source]["jmcc"][self.jmcc_lvl][var_name]
        self.context[self.source]["jmcc"][self.jmcc_lvl][var_name] = f"jmcc.{new('var')}"
        return self.context[self.source]["jmcc"][self.jmcc_lvl][var_name]

    def next_jmcc_lvl(self):
        self.jmcc_lvl += 1
        self.context[self.source]["jmcc"][self.jmcc_lvl] = {}

    def previous_jmcc_lvl(self):
        del self.context[self.source]["jmcc"][self.jmcc_lvl]
        self.jmcc_lvl -= 1
        if self.jmcc_lvl not in self.context[self.source]["jmcc"]:
            self.context[self.source]["jmcc"][self.jmcc_lvl] = {}

    def get_property(self, prop, default=None):
        if prop in self.context[self.source]["properties"]:
            return self.context[self.source]["properties"][prop]
        return default

    def get_properties(self):
        return self.context[self.source]["properties"]

    def has_variable(self, var_name):
        if isinstance(var_name, list):
            return False
        for cur_context_lvl in range(self.context_lvl + 1):
            if var_name in self.context[self.source][cur_context_lvl]["variables"]:
                return True
        return False

    def get_variable(self, var_name):
        if isinstance(var_name, list):
            return None
        for cur_context_lvl in range(self.context_lvl, -1, -1):
            if var_name in self.context[self.source][cur_context_lvl]["variables"]:
                return self.context[self.source][cur_context_lvl]["variables"][var_name]

    def get_variables(self):
        return self.context[self.source][self.context_lvl]["variables"]

    def set_variable_type(self, var_type, var_name, value_type):
        if isinstance(var_name, list):
            return None
        self.cur_context["vars"][var_type][var_name] = value_type

    def get_variable_type(self, var_type, var_name):
        if isinstance(var_name, list):
            return None
        for cur_context_lvl in range(self.context_lvl, -1, -1):
            if var_name in self.context[self.source][cur_context_lvl]["vars"][var_type]:
                return self.context[self.source][cur_context_lvl]["vars"][var_type][var_name]

    def set_inline(self, var_name, var_object):
        self.cur_context["inline_vars"][var_name] = var_object
        self.set_variable_type(Vars.INLINE, var_name, var_object.get_real_type())

    def get_inline(self, var_name):
        for cur_context_lvl in range(self.context_lvl, -1, -1):
            if var_name in self.context[self.source][cur_context_lvl]["inline_vars"]:
                return self.context[self.source][cur_context_lvl]["inline_vars"][var_name].copy()

    def has_inline(self, var_name):
        for cur_context_lvl in range(self.context_lvl + 1):
            if var_name in self.context[self.source][cur_context_lvl]["inline_vars"]:
                return True
        return False

    def get_inlines(self):
        return {k1: v1.copy() for k1, v1 in self.context[self.source][self.context_lvl]["inline_vars"].items()}

    def set_special(self, var_name, var_object):
        self.cur_context["callable"][var_name] = var_object

    def get_special(self, var_name):
        for cur_context_lvl in range(self.context_lvl, -1, -1):
            if var_name in self.context[self.source][cur_context_lvl]["callable"]:
                return self.context[self.source][cur_context_lvl]["callable"][var_name]

    def has_special(self, var_name):
        for cur_context_lvl in range(self.context_lvl + 1):
            if var_name in self.context[self.source][cur_context_lvl]["callable"]:
                return True
        return False

    def get_specials(self):
        return self.context[self.source][self.context_lvl]["callable"]

    def next_lvl(self):
        self.context_lvl += 1
        self.context[self.source][self.context_lvl] = copy.deepcopy(self.default_context)
        self.cur_context = copy.deepcopy(self.default_cur_context)

    def previous_lvl(self):
        del self.context[self.source][self.context_lvl]
        self.context_lvl -= 1
        if self.context_lvl not in self.context[self.source]:
            self.context[self.source][self.context_lvl] = copy.deepcopy(self.default_context)
            self.cur_context = copy.deepcopy(self.default_cur_context)

    def update(self):
        self.context[self.source][self.context_lvl]["variables"].update(self.cur_context["variables"])
        for vars_type in range(5):
            self.context[self.source][self.context_lvl]["vars"][vars_type].update(self.cur_context["vars"][vars_type])
        self.context[self.source][self.context_lvl]["inline_vars"].update(self.cur_context["inline_vars"])
        self.context[self.source][self.context_lvl]["callable"].update(self.cur_context["callable"])
        self.cur_context = copy.deepcopy(self.default_cur_context)

    def get_json(self):
        self.json_obj = {"handlers": []}
        for i1 in self.context[self.source][self.context_lvl]["operations"]:
            if i1.is_simple():
                self.json_obj["handlers"].append(i1.json())
            else:
                prev_ops, cur_op, next_ops = i1.simplify()
                for i2 in prev_ops:
                    self.json_obj["handlers"].append(i2.json())
                if cur_op.is_independant():
                    self.json_obj["handlers"].append(cur_op.json())
                for i2 in next_ops:
                    self.json_obj["handlers"].append(i2.json())
        i1 = 0
        while i1 < len(self.json_obj["handlers"]):
            self.idx = 0
            self.json_obj["handlers"][i1] = self.walk(self.json_obj["handlers"][i1], 43)
            i1 += 1
        return self.json_obj

    def walk(self, act, max_length):
        if "operations" in act:
            acts = act["operations"]
        else:
            return act
        for actionIdx in range(len(acts)):
            acti = acts[actionIdx]
            isContainer = "operations" in acti
            actionLength = 2 if isContainer else 1
            newIdx = self.idx + actionLength
            hasNext = actionIdx + 1 < len(acts)
            hasContents = isContainer and len(acti["operations"]) > 0
            next_acti = acts[actionIdx + 1] if hasNext else None
            reserved = 0
            if hasNext:
                reserved += 1
            if hasNext and isContainer and "operations" in next_acti and next_acti["action"] == "else":
                reserved += 2
                if len(next_acti["operations"]) > 0:
                    reserved += 1
                if actionIdx + 2 < len(acts):
                    reserved += 1
            containerMaxLength = max_length - reserved - hasContents
            if newIdx > containerMaxLength:
                func_count = new('function')
                call_func = {"action": "call_function", "values": [{"name": "function_name",
                                                                    "value": {"type": "text",
                                                                              "text": f"jmcc.{func_count}",
                                                                              "parsing": "legacy"}}]}
                func = {"type": "function", "position": new("event"), "operations": acts[actionIdx:],
                        "name": f"jmcc.{func_count}", "values": [{"name": "description", "value": {"type": "array",
                                                                                                   "values": [
                                                                                                       {"type": "text",
                                                                                                        "parsing": "legacy",
                                                                                                        "text": translate(
                                                                                                            "function.generator.new_function")}]}}]}
                acts = acts[:actionIdx]
                acts.append(call_func)
                self.json_obj["handlers"].append(func)
                self.idx += 1
                break
            self.idx = newIdx
            if isContainer:
                acts[actionIdx] = self.walk(acti, max_length - reserved)
        act["operations"] = acts
        return act

    def extend(self, another_context):
        self.context[self.source]["cur_context"][self.context_lvl]["variables"].update(
            another_context.context[another_context.source][another_context.context_lvl]["variables"])
        self.context[self.source]["cur_context"][self.context_lvl]["vars"][0].update(
            another_context.context[another_context.source][another_context.context_lvl]["vars"][0])
        self.context[self.source]["cur_context"][self.context_lvl]["vars"][1].update(
            another_context.context[another_context.source][another_context.context_lvl]["vars"][1])
        self.context[self.source]["cur_context"][self.context_lvl]["vars"][2].update(
            another_context.context[another_context.source][another_context.context_lvl]["vars"][2])
        self.context[self.source]["cur_context"][self.context_lvl]["vars"][3].update(
            another_context.context[another_context.source][another_context.context_lvl]["vars"][3])
        self.context[self.source]["cur_context"][self.context_lvl]["vars"][4].update(
            another_context.context[another_context.source][another_context.context_lvl]["vars"][4])
        self.context[self.source]["cur_context"][self.context_lvl]["vars"][5].update(
            another_context.context[another_context.source][another_context.context_lvl]["vars"][5])
        self.context[self.source]["cur_context"][self.context_lvl]["inline_vars"].update(
            another_context.context[another_context.source][another_context.context_lvl]["inline_vars"])
        self.context[self.source]["cur_context"][self.context_lvl]["callable"].update(
            another_context.context[another_context.source][another_context.context_lvl]["callable"])
        if len(self.context[self.source][self.context_lvl]["operations"]) == 0:
            self.context[self.source][self.context_lvl]["operations"].append(event("world_start", [], self.source))
        elif self.context[self.source][self.context_lvl]["operations"][0].type != "event":
            self.context[self.source][self.context_lvl]["operations"].insert(0, event("world_start", [], self.source))
        elif self.context[self.source][self.context_lvl]["operations"][0].name != "world_start":
            self.context[self.source][self.context_lvl]["operations"].insert(0, event("world_start", [], self.source))
        if len(another_context.context[another_context.source][another_context.context_lvl]["operations"]) == 0:
            another_context.context[another_context.source][another_context.context_lvl]["operations"].append(
                event("world_start", [], self.source))
        elif another_context.context[another_context.source][another_context.context_lvl]["operations"][
            0].type != "event":
            another_context.context[another_context.source][another_context.context_lvl]["operations"].insert(0, event(
                "world_start", [], self.source))
        elif another_context.context[another_context.source][another_context.context_lvl]["operations"][
            0].name != "world_start":
            another_context.context[another_context.source][another_context.context_lvl]["operations"].insert(0, event(
                "world_start", [], self.source))
        self.context[self.source][self.context_lvl]["operations"][0].operations.extend(
            another_context.context[another_context.source][another_context.context_lvl]["operations"].pop(
                0).operations)
        self.context[self.source][self.context_lvl]["operations"].extend(
            another_context.context[another_context.source][another_context.context_lvl]["operations"])

    def __str__(self):
        return f"Context: {self.context}"

    def __repr__(self):
        return self.__str__()


class default_jmcc_object:
    __slots__ = ()
    starting_pos = 0
    ending_pos = 0
    source = None
    type = None
    simplify = None
    value = None
    cast_as = None

    get_type = None
    get_real_type = None
    args = None
    object = None
    invert = None

    @staticmethod
    def is_simple():
        return True

    @staticmethod
    def is_independent():
        return False

    @staticmethod
    def can_cast_as(typ):
        return 0

    json = None

    def remove_inlines(self):
        return self

    copy = None

    @staticmethod
    def in_text():
        return None


class number:  # is_jmcc_object
    type = "number"
    __slots__ = ("value", "starting_pos", "ending_pos", "source")

    def __init__(self, val: float, starting_pos: int, ending_pos: int, source: str):
        self.value = val
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source

    def __str__(self):
        return f'number({self.value})'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def is_independent():
        return False

    @staticmethod
    def is_simple():
        return True

    def in_text(self):
        return str(self.value)

    def json(self):
        return {"type": "number", "number": self.value}

    def copy(self):
        return self

    def remove_inlines(self):
        return self

    def get_type(self):
        return self.type

    def get_real_type(self):
        return self.get_type()

    def can_cast_as(self, typ):
        if typ in "enum":
            return True
        return try_cast_as_class(self.get_real_type(), typ)

    def cast_as(self, typ, arg_thing):
        if typ == "enum":
            return text("FALSE" if self.value == 0 else "TRUE", Texts.PLAIN, self.starting_pos, self.ending_pos,
                        self.source).cast_as(typ, arg_thing)
        else:
            return self


class Texts:
    __slots__ = ()
    NONE: int = None
    LEGACY: int = "legacy"
    PLAIN: int = "plain"
    MINIMESSAGE: int = "minimessage"
    JSON: int = "json"


class text:  # is_jmcc_object
    type = "text"
    __slots__ = ("value", "simple", "value_type", "starting_pos", "ending_pos", "source")

    def __init__(self, val: str, val_type: int, starting_pos: int, ending_pos: int, source: str):
        self.value = val
        self.simple = isinstance(val, str)
        self.value_type = val_type
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source

    def __str__(self):
        return f'text(\"{self.value}\",{self.value_type})'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def is_independent():
        return False

    def is_simple(self):
        return self.simple

    def in_text(self):
        return self.value

    def simplify(self, mode=None, work_with=None):
        if isinstance(self.value, list):
            previous_operations, self.value, next_operations = giga_value(self, self.value)
        else:
            previous_operations = []
            next_operations = []
        return previous_operations, self, next_operations

    def json(self):
        return {"type": "text", "text": self.value, "parsing": self.value_type}

    def copy(self):
        return self

    def remove_inlines(self):
        if isinstance(self.value, list):
            self.value = [i2.remove_inlines() for i2 in self.value]
        return self

    def get_type(self):
        return self.type

    def get_real_type(self):
        return self.get_type()

    def can_cast_as(self, typ):
        if typ in ("enum", "block"):
            return 1
        return try_cast_as_class(self.get_real_type(), typ)

    def cast_as(self, typ, arg_thing=None):
        if typ == "enum":
            possible_enumeration = {i1 for i1 in arg_thing["values"]}
            val1 = find_value_from_list(self.value, possible_enumeration)
            if val1 == -1:
                error_from_object(self, "ArgumentError", translate("error.argumenterror.unknown_enum",
                                                                   {0: self.value, 1: ", ".join(
                                                                       map(lambda x: "'" + str(x) + "'",
                                                                           possible_enumeration))}))
            return enum_(val1, self.starting_pos, self.ending_pos, self.source)
        elif typ == "block":
            return block(self.value, self.starting_pos, self.ending_pos, self.source)
        else:
            return self


class lst:  # is_jmcc_object
    type = "array"
    __slots__ = ("values", "simple", "starting_pos", "ending_pos", "source")

    def __init__(self, vals, starting_pos: int, ending_pos: int, source: str):
        self.values = list(vals)
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        self.simple = False

    def __str__(self):
        return f'lst({self.values})'

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return self.values.__len__()

    def __iter__(self):
        return self.values.__iter__()

    def __contains__(self, item):
        for item2 in self.values:
            if item == item2:
                return True
        return False

    @staticmethod
    def is_independent():
        return False

    def is_simple(self):
        return self.simple

    def in_text(self):
        return None

    def simplify(self, mode=None, work_with=None, len_limit=None):
        new_lst = []
        previous_operations = []
        next_operations = []
        for val in self.values:
            if val.is_simple():
                new_lst.append(val)
            else:
                prev_ops, cur_op, next_ops = val.simplify(mode=0)
                previous_operations.extend(prev_ops)
                next_ops.extend(next_operations)
                next_operations = next_ops
                new_lst.append(cur_op)
        self.values = new_lst
        self.simple = True
        if (mode == 0 or (len_limit is not None and (len(new_lst) > len_limit))):
            if isinstance(work_with, var):
                current_operation = work_with
            else:
                current_operation = var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos,
                                        self.source)
            current_operation.value_type = "array"
            Context(Context.sources[-1]).set_variable_type(current_operation.var_type, current_operation.value,
                                                           current_operation.value_type)
            if len_limit is not None:
                len_limit = actions["variable"]["create_list"]["args"]["values"]["array"]
                self.values = new_lst[:len_limit]
                del new_lst[:len_limit]
                previous_operations.append(action("variable", "create_list",
                                                  calling_args([], {"variable": current_operation,
                                                                    "values": lst(self.values, self.starting_pos,
                                                                                  self.ending_pos, self.source)},
                                                               self.starting_pos,
                                                               self.ending_pos, self.source), self.starting_pos,
                                                  self.ending_pos, self.source))
                len_limit = actions["variable"]["append_value"]["args"]["values"]["array"]
                while len(new_lst) > len_limit:
                    self.values = new_lst[:len_limit]
                    del new_lst[:len_limit]
                    previous_operations.append(action("variable", "append_value",
                                                      calling_args([], {"variable": current_operation,
                                                                        "values": lst(self.values, self.starting_pos,
                                                                                      self.ending_pos, self.source)},
                                                                   self.starting_pos,
                                                                   self.ending_pos, self.source), self.starting_pos,
                                                      self.ending_pos, self.source))
                self.values = new_lst
                if len(self.values) > 0:
                    previous_operations.append(action("variable", "append_value",
                                                      calling_args([], {"variable": current_operation,
                                                                        "values": lst(self.values, self.starting_pos,
                                                                                      self.ending_pos, self.source)},
                                                                   self.starting_pos,
                                                                   self.ending_pos, self.source), self.starting_pos,
                                                      self.ending_pos, self.source))

            else:
                previous_operations.append(action("variable", "create_list",
                                                  calling_args([], {"variable": current_operation,
                                                                    "values": self},
                                                               self.starting_pos,
                                                               self.ending_pos, self.source), self.starting_pos,
                                                  self.ending_pos, self.source))
        else:
            self.values = new_lst
            current_operation = self
        return previous_operations, current_operation, next_operations

    def json(self):
        return {"type": "array", "values": [i3.json() for i3 in self.values]}

    def copy(self):
        return lst([i3.copy() for i3 in self.values], self.starting_pos, self.ending_pos, self.source)

    def remove_inlines(self):
        for i1 in range(len(self.values)):
            self.values[i1] = self.values[i1].remove_inlines()
        return self

    def get_type(self):
        return self.type

    def get_real_type(self):
        return self.get_type()

    def can_cast_as(self, typ):
        return try_cast_as_class(self.get_real_type(), typ)

    def cast_as(self, typ, arges):
        return self


class dct:  # is_jmcc_object
    type = "map"
    __slots__ = ("keys", "values", "starting_pos", "ending_pos", "source")

    def __init__(self, keys, val, starting_pos: int, ending_pos: int, source: str):
        self.keys = list(keys)
        self.values = list(val)
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source

    def __str__(self):
        return f'dct(keys={self.keys},values={self.values})'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def is_independent():
        return False

    @staticmethod
    def is_simple():
        return False

    def in_text(self):
        return None

    def copy(self):
        return dct([i3.copy() for i3 in self.keys], [i3.copy() for i3 in self.values], self.starting_pos,
                   self.ending_pos, self.source)

    def simplify(self, mode=None, work_with=None):
        new_keys = []
        new_values = []
        previous_operations = []
        next_operations = []
        for key in self.keys:
            if key.is_simple():
                new_keys.append(key)
            else:
                prev_ops, cur_op, next_ops = key.simplify(mode=0)
                previous_operations.extend(prev_ops)
                next_ops.extend(next_operations)
                next_operations = next_ops
                new_keys.append(cur_op)
        self.keys = new_keys
        for val in self.values:
            if val.is_simple():
                new_values.append(val)
            else:
                prev_ops, cur_op, next_ops = val.simplify(mode=0)
                previous_operations.extend(prev_ops)
                next_ops.extend(next_operations)
                next_operations = next_ops
                new_values.append(cur_op)
        self.values = new_values
        if mode == 0:
            if isinstance(work_with, var):
                current_operation = work_with
            else:
                current_operation = var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos,
                                        self.source)
            current_operation.value_type = "map"
            Context(Context.sources[-1]).set_variable_type(current_operation.var_type, current_operation.value,
                                                           current_operation.value_type)
            len_limit = actions["variable"]["create_map_from_values"]["args"]["values"]["array"]
            if len(self.keys) > len_limit:
                len_limit = actions["variable"]["create_list"]["args"]["values"]["array"]
                self.keys = new_keys[:len_limit]
                del new_keys[:len_limit]
                self.values = new_values[:len_limit]
                del new_values[:len_limit]
                var1 = var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)
                var2 = var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)
                previous_operations.append(action("variable", "create_list",
                                                  calling_args([], {"variable": var1, "values":
                                                      lst(self.keys, self.starting_pos, self.ending_pos,
                                                          self.source)},
                                                               self.starting_pos, self.ending_pos, self.source),
                                                  self.starting_pos, self.ending_pos, self.source))
                previous_operations.append(action("variable", "create_list",
                                                  calling_args([], {"variable": var2, "values":
                                                      lst(self.values, self.starting_pos, self.ending_pos,
                                                          self.source)},
                                                               self.starting_pos, self.ending_pos, self.source),
                                                  self.starting_pos, self.ending_pos, self.source))
                len_limit = actions["variable"]["append_value"]["args"]["values"]["array"]
                while len(new_keys) > len_limit:
                    self.keys = new_keys[:len_limit]
                    del new_keys[:len_limit]
                    self.values = new_values[:len_limit]
                    del new_values[:len_limit]
                    previous_operations.append(action("variable", "append_value",
                                                      calling_args([], {"variable": var1, "values":
                                                          lst(self.keys, self.starting_pos, self.ending_pos,
                                                              self.source)},
                                                                   self.starting_pos, self.ending_pos, self.source),
                                                      self.starting_pos, self.ending_pos, self.source))
                    previous_operations.append(action("variable", "append_value",
                                                      calling_args([], {"variable": var2, "values":
                                                          lst(self.values, self.starting_pos, self.ending_pos,
                                                              self.source)},
                                                                   self.starting_pos, self.ending_pos, self.source),
                                                      self.starting_pos, self.ending_pos, self.source))
                self.keys = new_keys
                self.values = new_values
                if len(self.keys) > 0:
                    previous_operations.append(action("variable", "append_value",
                                                      calling_args([], {"variable": var1, "values":
                                                          lst(self.keys, self.starting_pos, self.ending_pos,
                                                              self.source)},
                                                                   self.starting_pos, self.ending_pos, self.source),
                                                      self.starting_pos, self.ending_pos, self.source))
                    previous_operations.append(action("variable", "append_value",
                                                      calling_args([], {"variable": var2,
                                                                        "values": lst(self.values, self.starting_pos,
                                                                                      self.ending_pos, self.source)},
                                                                   self.starting_pos,
                                                                   self.ending_pos, self.source), self.starting_pos,
                                                      self.ending_pos, self.source))
                previous_operations.append(action("variable", "create_map",
                                                  calling_args([], {"variable": current_operation, "keys": var1,
                                                                    "values": var2},
                                                               self.starting_pos,
                                                               self.ending_pos, self.source), self.starting_pos,
                                                  self.ending_pos, self.source))
            else:
                previous_operations.append(action("variable", "create_map_from_values",
                                                  calling_args([], {"variable": current_operation,
                                                                    "keys": lst(self.keys, self.starting_pos,
                                                                                self.ending_pos, self.source),
                                                                    "values": lst(self.values, self.starting_pos,
                                                                                  self.ending_pos, self.source)},
                                                               self.starting_pos,
                                                               self.ending_pos, self.source), self.starting_pos,
                                                  self.ending_pos, self.source))
        else:
            current_operation = self
        return previous_operations, current_operation, next_operations

    def remove_inlines(self):
        for i1 in range(len(self.values)):
            self.values[i1] = self.values[i1]
        for i1 in range(len(self.keys)):
            self.keys[i1] = self.keys[i1]
        return self

    def json(self):
        return {"type": "map",
                "values": {json.dumps(self.keys[i1].json(), separators=(',', ':')): self.values[i1].json() for i1 in
                           range(min(len(self.keys), len(self.values)))}}

    def get_type(self):
        return self.type

    def get_real_type(self):
        return self.get_type()

    def can_cast_as(self, typ):
        return try_cast_as_class(self.get_real_type(), typ)

    def cast_as(self, typ, arges):
        return self


class NBT:  # is_jmcc_object
    type = "snbt"
    __slots__ = ("value", "value_type", "starting_pos", "ending_pos", "source")

    def __init__(self, val, starting_pos: int, ending_pos: int, source: str):
        self.value = val
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.value_type = "item"
        self.source = source

    def __str__(self):
        return f'NBT({self.value})'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def is_independent():
        return False

    @staticmethod
    def is_simple():
        return False

    def in_text(self):
        return "m" + str(self.value)

    def simplify(self, mode=None, work_with=None):
        if "id" in self.value and "count" in self.value:
            return item(calling_args([], {
                "id": text(self.value["id"].value, Texts.PLAIN, self.starting_pos, self.ending_pos, self.source),
                "count": number(self.value["count"].value, self.starting_pos, self.ending_pos, self.source),
                "nbt": NBT(self.value["components"], self.starting_pos, self.ending_pos,
                           self.source) if "components" in self.value else None},
                                     self.starting_pos, self.ending_pos, self.source), self.starting_pos,
                        self.ending_pos, self.source).simplify(mode=mode, work_with=work_with)
        return [], self, []

    def remove_inlines(self):
        return self

    def copy(self):
        return self

    def get_type(self):
        return self.type

    def get_real_type(self):
        return self.value_type

    def can_cast_as(self, typ):
        return 0

    def cast_as(self, typ, arges):
        return self

    def json(self):
        error_from_object(self, "SimplifyError", translate("error.simplifyerror", {0: self}))


class Vars:
    __slots__ = ()
    NONE: int = -1
    BRACKET: int = 0
    INLINE: int = 1
    LOCAL: int = 2
    GAME: int = 3
    SAVE: int = 4
    JMCC: int = 5
    changer = {-1: "NONE", 0: "BRACKET", 1: "INLINE", 2: "LOCAL", 3: "GAME", 4: "SAVE", 5: "JMCC"}


class var:  # is_jmcc_object
    __slots__ = ("value", "var_type", "starting_pos", "ending_pos", "source", "value_type", "simple")
    type = "variable"

    def __init__(self, val: str, val_type: Vars, starting_pos: int, ending_pos: int, source: str, value_type=None):
        self.value = val
        self.var_type = val_type
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        self.value_type = value_type
        self.simple = self.var_type not in (Vars.INLINE, Vars.JMCC) and isinstance(self.value, str)
        if self.var_type == Vars.BRACKET:
            error_from_object(self, "", "nah bro")

    def __str__(self):
        return f'var(`{self.value}`,{self.var_type})'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def is_independent():
        return False

    def is_simple(self):
        return self.simple

    def in_text(self):
        if self.var_type == Vars.LOCAL:
            var_prefix = "%var_local("
        elif self.var_type == Vars.GAME:
            var_prefix = "%var("
        elif self.var_type == Vars.SAVE:
            var_prefix = "%var_save("
        elif self.var_type == Vars.BRACKET:
            var_prefix = "%var_bracket("
        else:
            error_from_object(self, "", translate("error.unknown5"))
            var_prefix = ""
        return var_prefix + self.value + ")"

    def simplify(self, mode=None, work_with=None):
        previous_operations = []
        next_operations = []
        if isinstance(self.value, list):
            previous_operations, self.value, next_operations = giga_value(self, self.value)
        if self.var_type == Vars.INLINE:
            if len(previous_operations) + len(next_operations) > 0:
                error_from_object(self, "", translate("error.unknown6"))
            val = Context(Context.sources[-1]).get_inline(self.value)
            if not isinstance(val, var) and mode == 1:
                return [], self, []
            val.starting_pos = self.starting_pos
            val.ending_pos = self.ending_pos
            val.source = self.source
            if isinstance(val, var) and self.get_real_type() is not None:
                val.value_type = self.get_real_type()
            if val.is_simple():
                return [], val, []
            return val.simplify(mode=mode, work_with=work_with)
        if self.var_type == Vars.JMCC:
            self.value = Context(Context.sources[-1]).get_jmcc(self.value)
        return previous_operations, self, next_operations

    def json(self):
        return {"type": "variable", "variable": self.value, "scope": Vars.changer[self.var_type].lower()}

    def copy(self):
        return self

    def remove_inlines(self):
        if isinstance(self.value, list):
            self.value = [i2.remove_inlines() for i2 in self.value]
        if self.var_type == Vars.INLINE:
            if Context(Context.sources[-1]).has_inline(self.value):
                val = Context(Context.sources[-1]).get_inline(self.value)
                val.starting_pos = self.starting_pos
                val.ending_pos = self.ending_pos
                val.source = self.source
                return val
        if isinstance(self.value, list):
            prev_ops, a, next_ops = giga_value(self, self.value)
            if len(prev_ops) == 0 and len(next_ops) == 0:
                self.value = a
        return self

    def get_type(self):
        return self.type

    def get_real_type(self):
        if self.var_type == Vars.INLINE:
            if self.value_type is None:
                self.value_type = Context(Context.sources[-1]).get_variable_type(Vars.INLINE, self.value)
                if self.value_type is None and Context(Context.sources[-1]).has_inline(self.value):
                    self.value_type = Context(Context.sources[-1]).get_inline(self.value).get_real_type()
        return self.value_type

    def can_cast_as(self, typ):
        if typ == "enum" and self.get_real_type() in ("text", "any", None):
            return 1
        if typ == "block" and self.get_real_type() in ("text", "item", "any", None):
            return 1
        return try_cast_as_class(self.get_real_type(), typ, 2)

    def cast_as(self, typ, arg_thing=None):
        if typ == "enum":
            return enum_(arg_thing["values"][0], self.starting_pos, self.ending_pos, self.source, self)
        return self


class calling_args:
    __slots__ = ("positional", "unpositional", "starting_pos", "ending_pos", "source")
    type = None

    def __init__(self, positional: list, unpositional: dict, starting_pos: int, ending_pos: int,
                 source: str):
        self.positional = positional
        self.unpositional = unpositional
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source

    def __str__(self):
        return f'args(`{self.positional}`,{self.unpositional})'

    def __repr__(self):
        return self.__str__()

    def get_args(self, template: list, func=None) -> (dict | default_jmcc_object):
        args = {i1: None for i1 in template}
        have_kwargs = None
        if func is not None:
            for k1, v1 in func.items():
                if v1 == 2:
                    have_kwargs = k1
        for k1, v1 in self.unpositional.items():
            if k1 in args:
                args[k1] = v1
                if k1 == have_kwargs:
                    have_kwargs = None
            elif have_kwargs is not None:
                if args[have_kwargs] is None:
                    args[have_kwargs] = dct([], [], self.starting_pos, self.ending_pos, self.source)
                args[have_kwargs].keys.append(text(k1, Texts.LEGACY, v1.starting_pos, v1.ending_pos, v1.source))
                args[have_kwargs].values.append(v1)
            else:
                return None, (self, "ArgumentError", translate("error.argumenterror.argument_with_wrong_name",
                                                               {0: k1, 1: ", ".join(
                                                                   map(lambda x: "'" + str(x) + "'", template))}))
        positional = self.positional.copy()
        if len(positional) > 0:
            for k1, v1 in args.items():
                if func is not None and k1 in func:
                    typ = func[k1]
                else:
                    typ = 0
                if v1 is None:
                    if isinstance(positional[0], unpacked_args) and positional[0].value_type == typ:
                        args[k1] = positional[0].value
                        del positional[0]
                        if len(positional) == 0:
                            break
                    if typ == 1:
                        args[k1] = lst(positional, positional[0].starting_pos, positional[-1].ending_pos,
                                       positional[0].source)
                        positional = []
                        break
                    else:
                        args[k1] = positional[0]
                        del positional[0]
                        if len(positional) == 0:
                            break
            if len(positional) > 0:
                return None, (self, "ArgumentError", translate("error.argumenterror.too_many_arguments", {
                    0: ", ".join(map(lambda x: "'" + str(x) + "'", template))}))
        return args, None

    def set_args(self):
        args = []
        arg_names = set()
        for i1 in self.positional:
            if i1.type == "variable":
                arg = {"id": i1.value, "type": i1.get_real_type() if i1.get_real_type() is not None else "any",
                       "default_value": None, "unpacked": 0}
            elif i1.type == "unpacked_value" and i1.value.type == "variable":
                arg = {"id": i1.value.value,
                       "type": i1.value.get_real_type() if i1.value.get_real_type() is not None else "any",
                       "default_value": None, "unpacked": i1.value_type}
            else:
                error_from_object(self, "ArgumentError",
                                  translate("error.argumenterror.wrong_argument", {0: i1.type, 1: "variable"}))
            if arg["id"] in arg_names:
                error_from_object(i1, "", translate("error.unknown7"))
            args.append(arg)
            arg_names.add(arg["id"])
        for k1, v1 in self.unpositional.items():
            arg = {"id": k1, "type": v1.type, "default_value": v1, "unpacked": 0}
            if k1 in arg_names:
                error_from_object(v1, "", translate("error.unknown8"))
            args.append(arg)
            arg_names.add(k1)
        return args

    def remove_inlines(self):
        for i1 in range(len(self.positional)):
            self.positional[i1] = self.positional[i1].remove_inlines()
        for i1 in self.unpositional:
            self.unpositional[i1] = self.unpositional[i1].remove_inlines()
        return self

    def copy(self):
        return self


class unpacked_args:
    type = "unpacked_value"
    __slots__ = ("value", "value_type", "starting_pos", "ending_pos", "source")

    def __init__(self, val: default_jmcc_object, starting_pos: int, ending_pos: int, source: str, type=1):
        self.value = val
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        self.value_type = type

    def __str__(self):
        return f'*{self.value}'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def is_independent():
        return False

    @staticmethod
    def is_simple():
        return False

    def remove_inlines(self):
        self.value = self.value.remove_inlines()
        return self

    def simplify(self, mode=None, work_with=None):
        if self.value.is_simple():
            return [], self.value, []
        return self.value.simplify(mode=mode, work_with=work_with)

    def get_type(self):
        return self.type

    def get_real_type(self):
        return self.get_type()

    def can_cast_as(self, typ):
        return try_cast_as_class(self.get_real_type(), typ)

    def cast_as(self, typ, arges):
        return self


def giga_value(self, giga):
    new_text = ""
    previous_operations = []
    next_operations = []
    for op in giga:
        op: default_jmcc_object
        if not op.is_simple():
            prev_ops, op, next_ops = op.simplify(mode=0)
            previous_operations.extend(prev_ops)
            next_ops.extend(next_operations)
            next_operations = next_ops
        in_text = op.in_text()
        if in_text is None:
            prev_ops, op, next_ops = assign(
                [var(f'jmcc.{new("var")}', Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)],
                None, op,
                self.starting_pos, self.ending_pos, self.source).simplify(mode=0)
            previous_operations.extend(prev_ops)
            next_ops.extend(next_operations)
            next_operations = next_ops
            in_text = op.in_text()
        new_text += in_text
    return previous_operations, new_text, next_operations


def find_value_from_list(val, possible_list=None):
    if possible_list is None:
        possible_list = set()
    check_enum = 0
    ret_val = val
    for i1 in possible_list:
        if i1.lower().startswith(val.lower()):
            check_enum += 1
            ret_val = i1
        if i1.lower() == val.lower():
            return i1

    if check_enum != 1:
        return -1
    return ret_val


class value:  # is_jmcc_object
    type = "value"
    possible_selectors = {"current", "default", "default_entity", "killer_entity", "damager_entity", "victim_entity",
                          "shooter_entity", "projectile", "last_entity"}
    __slots__ = ("value", "value_type", "starting_pos", "ending_pos", "source", "selector")

    def __init__(self, val: str, starting_pos: int, ending_pos: int, source: str, selector=None, value_type=None):
        self.value = val
        self.value_type = value_type
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        if selector is not None:
            if isinstance(selector.value, list):
                previous_operations, selector.value, next_operations = giga_value(self, selector.value)
                if len(previous_operations) + len(next_operations) > 0:
                    error_from_object(self, "", translate("error.unknown9"))
            self.selector = find_value_from_list(selector.value, self.possible_selectors)
            if self.selector == -1:
                error_from_object(selector, "SelectorError", translate("error.argumenterror.unknown_selector",
                                                                       {0: selector.value, 1: ", ".join(
                                                                           map(lambda x: "'" + str(x) + "'",
                                                                               self.possible_selectors))}))
        else:
            self.selector = None

    def __str__(self):
        return f'value::{self.value}'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def is_independent():
        return False

    @staticmethod
    def is_simple():
        return True

    def simplify(self, mode=None, work_with=None):
        if isinstance(work_with, var):
            work_with = var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)
        return assign(work_with, None, self, self.starting_pos, self.ending_pos, self.source).simplify()

    def in_text(self):
        return None

    def json(self):
        return {"type": "game_value", "game_value": values[self.value]["id"],
                "selection": json.dumps({"type": self.selector},
                                        separators=(',', ':')) if self.selector is not None else "null"}

    def copy(self):
        return self

    def remove_inlines(self):
        return self

    def get_type(self):
        return self.type

    def get_real_type(self):
        return self.value_type

    def can_cast_as(self, typ):
        return try_cast_as_class(self.get_real_type(), typ)

    def cast_as(self, typ, arges):
        return self


class action:  # is_jmcc_object
    type = "action"
    __slots__ = (
        "object", "name", "args", "arges", "new_args", "template", "operations", "lambd", "selector", "invert",
        "simple",
        "conditional", "value_type", "starting_pos", "ending_pos", "source")

    def __init__(self, act_obj: str, act_name: str, args: calling_args, starting_pos: int, ending_pos: int,
                 source: object,
                 operations=None, lambd=None, selector=None, inver=None, simple=False, conditional=None):
        self.object = act_obj
        self.name = act_name
        self.args = args
        self.arges = {}
        self.new_args = {}
        self.template = {}
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        self.operations = operations
        self.lambd = lambd
        self.selector = selector
        self.invert = inver
        self.simple = simple
        self.conditional = conditional
        if "assign" in actions[self.object][self.name]:
            if self.object == "variable" and self.name == "set_value":
                self.value_type = self.args.unpositional["value"].get_real_type()
            else:
                self.value_type = actions[self.object][self.name]["assign"][0]["type"]
        else:
            self.value_type = None

    def __str__(self):
        return f'action({self.object}::{self.name}, {self.args})'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def is_independent():
        return True

    def is_simple(self):
        return self.simple

    def in_text(self):
        return None

    def simplify(self, mode=None, work_with=None):
        var_based = "var" if mode != -1 else "fake_var"
        self.args: calling_args
        if mode == 1:
            error_from_object(self, "ActionError", translate("error.actionerror.action_cant_be_setter", {0: self}))
        if self.selector is not None:
            if isinstance(self.selector.value, list):
                previous_operations, self.selector.value, next_operations = giga_value(self, self.selector)
                if len(previous_operations) + len(next_operations) > 0:
                    error_from_object(self, "", translate("error.unknown10"))
            if self.object == "player":
                possible_selectors = {"current", "default_player", "killer_player", "damager_player", "shooter_player",
                                      "victim_player", "random_player", "all_players"}
            elif self.object == "entity":
                possible_selectors = {"current", "default_entity", "killer_entity", "shooter_entity", "projectile",
                                      "victim_entity", "random_entity", "all_mobs", "all_entities", "last_entity"}
            else:
                error_from_object(self.selector, "SelectorError", translate("error.argumenterror.no_selector"))
                possible_selectors = None
            val1 = find_value_from_list(self.selector.value, possible_selectors)

            if val1 == -1:
                error_from_object(self.selector, "SelectorError", translate("error.argumenterror.unknown_selector",
                                                                            {0: self.selector, 1: ", ".join(
                                                                                map(lambda x: "'" + str(x) + "'",
                                                                                    possible_selectors))}))
            self.selector = val1
        context = Context(Context.sources[-1])
        if actions[self.object][self.name]["type"].endswith("conditional"):
            thing, error_message = self.args.get_args(["conditional"])
            if thing is None:
                error(*error_message)
            thing = thing["conditional"]
            a1, thing, a2 = thing.simplify()
            if not thing.type == "action":
                error_from_object(thing, "ArgumentError",
                                  translate("error.argumenterror.wrong_argument", {0: thing.type, 1: "action"}))
            if not actions[thing.object][thing.name].setdefault("boolean", False):
                error_from_object(thing, "ArgumentError", translate("error.argumenterror.expected_boolean"))
            if len(a1) > 0 or len(a2) > 0:
                error_from_object(thing, "ArgumentError", translate("error.jsonerror.object_isnt_simple"))
            self.conditional = thing
            self.simple = True
            self.args = thing.args
            self.new_args = thing.new_args
            return [], self, []
        else:
            self.arges = actions[self.object][self.name]["args"]
            previous_operations = []
            next_operations = []
            inline = False
            if mode == 0 or mode == -1:
                if "assign" in actions[self.object][self.name]:
                    if not isinstance(work_with, list):
                        if not isinstance(work_with, var):
                            work_with = var(f"jmcc.{new(var_based)}", Vars.LOCAL, self.starting_pos, self.ending_pos,
                                            self.source)
                        work_with = [work_with]
                    for i2 in range(len(actions[self.object][self.name]["assign"])):
                        if i2 < len(work_with):
                            self.args.unpositional[
                                actions[self.object][self.name]["assign"][i2]["id"]] = \
                                work_with[i2]
                        else:
                            break

                elif actions[self.object][self.name].setdefault("boolean", False) and mode == 0:
                    return if_else_expr(self, number(1, self.starting_pos, self.ending_pos, self.source),
                                        number(0, self.starting_pos, self.ending_pos, self.source), self.starting_pos,
                                        self.ending_pos, self.source).simplify(mode=mode, work_with=work_with)
                else:
                    error_from_object(self, "ActionError", translate("error.actionerror.action_has_no_value",
                                                                     {0: f"{self.object}::{self.name}"}))
            if "lambda" in actions[self.object][self.name]:
                if isinstance(self.lambd, list):
                    for i2 in range(len(actions[self.object][self.name]["lambda"])):
                        if i2 < len(self.lambd):
                            self.args.unpositional[actions[self.object][self.name]["lambda"][i2]["id"]] = \
                                self.lambd[i2]
                        else:
                            break
            x, error_message, load_args, nun = check_args(self, self.args, True)
            if x is None:
                error_from_object(*error_message)
            if "assign" in actions[self.object][self.name]:
                if work_with is None or len(work_with) == 0:
                    work_with = []
                for i2 in actions[self.object][self.name]["assign"]:
                    if load_args[i2["id"]] is None:
                        continue
                    if load_args[i2["id"]].type == "variable" and load_args[i2["id"]].var_type == Vars.INLINE:
                        inline = True
                if inline:
                    for i2 in set(load_args):
                        if load_args[i2] is None:
                            del load_args[i2]
            self.args = calling_args([], load_args, self.args.starting_pos, self.args.ending_pos, self.args.source)
            if self.object == "variable":
                if self.name == "set_value":
                    if inline and not (
                            context.jmcc_lvl > 0 and isinstance(context.get_inline(load_args["variable"].value), var)):
                        context.set_inline(load_args["variable"].value, load_args["value"].remove_inlines())
                        return [], None, []
                    if load_args["value"].type in {"subscript", "calling_argument", "calling_function",
                                                   "calling_object", "action", "if_else_expr", "array", "map"} or (
                            load_args["value"].type in {"location", "vector"} and not load_args["value"].is_simple()):
                        if len(work_with) < 2:
                            work_with = load_args["variable"]
                        return load_args["value"].simplify(mode=0, work_with=work_with)
                    if load_args["variable"].type in {"subscript", "calling_argument"}:
                        return load_args["variable"].simplify(mode=1, work_with=load_args["value"])
            if inline and not (
                    context.jmcc_lvl > 0 and isinstance(context.get_inline(load_args["variable"].value), var)):
                context.set_inline(work_with[0].value, self.remove_inlines())
                return [], None, []
            if self.object == "variable":
                if self.name == "create_list":
                    if load_args["values"].type == "array" and len(load_args["values"].values) > self.arges["values"][
                        "array"]:
                        return (load_args["values"] if load_args["values"] is not None else
                                lst([], self.starting_pos, self.ending_pos, self.source)).simplify(
                            mode=0, work_with=load_args["variable"], len_limit=self.arges["values"]["array"])
                elif self.name == "create_map_from_values":
                    if (len(load_args["values"].values) > self.arges["values"]["array"] and len(
                            load_args["keys"].values) >
                            self.arges["keys"]["array"]):
                        return dct(load_args["keys"].values, load_args["values"].values, self.starting_pos,
                                   self.ending_pos,
                                   self.source).simplify(mode=0, work_with=load_args["variable"])
                elif self.name in {"add", "subtract", "multiply", "divide"}:
                    new_value = []
                    spec_number = None

                    def add_number(new_value, spec_numba, numba, method):
                        if numba.get_type() == "number" and isinstance(numba.value, (int, float)):
                            if spec_numba is None:
                                spec_numba = numba
                                new_value.append(spec_numba)
                            else:
                                match method:
                                    case "add":
                                        spec_numba.value += numba.value
                                    case "subtract":
                                        spec_numba.value -= numba.value
                                    case "multiply":
                                        spec_numba.value *= numba.value
                                    case "divide":
                                        spec_numba.value /= numba.value
                                    case "remainder":
                                        spec_numba.value %= numba.value
                                    case "pow":
                                        spec_numba.value **= numba.value
                        return spec_numba

                    if self.name in {"add", "subtract", "multiply", "divide"}:
                        for i1 in range(len(load_args["value"].values)):
                            act = load_args["value"].values[i1]
                            if act.get_type() == "action":
                                prev_ops, act, next_ops = act.simplify(mode=-1)
                                previous_operations.extend(prev_ops)
                                next_ops.extend(next_operations)
                                next_operations = next_ops
                            if act.get_type() == "action" and act.object == self.object and act.name == self.name and act.name in {
                                "add", "multiply"}:
                                for i2 in range(len(act.new_args["value"].values)):
                                    act2 = act.new_args["value"].values[i2]
                                    if act2.get_type() == "number":
                                        spec_number = add_number(new_value, spec_number, act2, self.name)
                                    else:
                                        new_value.append(act2)
                            elif act.get_type() == "number":
                                spec_number = add_number(new_value, spec_number, act, self.name)
                            else:
                                new_value.append(act)
                    elif self.name in {"remainder", "pow"}:
                        pass
                    if len(new_value) == 1 and spec_number is not None:
                        if "jmcc." not in work_with[0].value:
                            prev_ops, act, next_ops = assign(work_with, None, spec_number, self.starting_pos,
                                                             self.ending_pos, self.source).simplify()
                            previous_operations.extend(prev_ops)
                            next_ops.extend(next_operations)
                            next_operations = next_ops
                            return previous_operations, act, next_operations
                        else:
                            return previous_operations, spec_number, next_operations
                    load_args["value"].values = new_value

            if "assign" in actions[self.object][self.name]:
                assigning = {i2["id"]: i2["type"] for i2 in actions[self.object][self.name]["assign"]}
            else:
                assigning = {}
            v1: default_jmcc_object
            prev_ops, args, next_ops = fix_args(self, load_args, True, assigning=assigning)
            previous_operations.extend(prev_ops)
            next_ops.extend(next_operations)
            next_operations = next_ops
            if self.object == "variable":
                if self.name == "set_value":
                    if load_args["value"].get_type() == "value":
                        load_args["variable"].value_type = load_args["value"].get_real_type()
                    else:
                        load_args["variable"].value_type = load_args["value"].get_type() if load_args[
                                                                                                "value"].get_real_type() in (
                                                                                                None, "any") else \
                            load_args[
                                "value"].get_real_type()
                    context.set_variable_type(load_args["variable"].var_type, load_args["variable"].value,
                                              load_args["variable"].get_real_type())
                    if load_args["value"] == load_args["variable"]:
                        return [], None, []
            self.new_args = args
            if mode != -1:
                self.simple = True
            if mode == 0:
                if isinstance(work_with, list):
                    work_with = work_with[0]
                previous_operations.append(self)
                return previous_operations, work_with, next_operations
        return previous_operations, self, next_operations

    def json(self):
        a = {"action": actions[self.object][self.name]["id"],
             "values": [{"name": key1, "value": val1.json()} for key1, val1 in self.new_args.items()]}
        if self.invert is not None:
            a["is_inverted"] = self.invert
        if self.operations is not None:
            a["operations"] = [i3.json() for i3 in self.operations]
        if self.selector is not None:
            a["selection"] = {"type": self.selector}
        if self.conditional is not None:
            b = self.conditional.json()
            del b["values"]
            if "is_inverted" not in b:
                b["is_inverted"] = False
            a["conditional"] = b
        return a

    def copy(self):
        return action(self.object, self.name, self.args, self.starting_pos, self.ending_pos, self.source,
                      self.operations, self.lambd, self.selector, self.invert, conditional=self.conditional)

    def remove_inlines(self):
        self.args = self.args.remove_inlines()
        return self

    def get_type(self):
        return self.type

    def get_real_type(self):
        return self.value_type

    def can_cast_as(self, typ):
        return try_cast_as_class(self.get_real_type(), typ)

    def cast_as(self, typ, arges):
        return self


class calling_object:  # is_jmcc_object
    type = "calling_object"
    __slots__ = ("value", "value_type", "args", "special", "starting_pos", "ending_pos", "source")
    changeable = {"item", "sound", "particle", "location", "vector", "potion"}

    def __init__(self, val: str, args: calling_args, starting_pos: int, ending_pos: int, source: str, special=None):
        self.value = val
        self.args = args
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        self.special = special
        self.value_type = None
        if self.special is None:
            self.special = Context(Context.sources[-1])
        if self.value not in self.changeable:
            if self.special.has_special(self.value):
                spec, error_message, args1, nun = self.special.get_special(self.value).check_args(args)
                if spec is not None:
                    self.value_type = spec.get_real_type()

    def __str__(self):
        return f'calling_object({self.value}, {self.args})'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def is_independent():
        return True

    @staticmethod
    def is_simple():
        return False

    def in_text(self):
        return None

    def change(self):
        if self.value == "item":
            return item(self.args, self.starting_pos, self.ending_pos, self.source)
        elif self.value == "sound":
            return sound(self.args, self.starting_pos, self.ending_pos, self.source)
        elif self.value == "vector":
            return vector(self.args, self.starting_pos, self.ending_pos, self.source)
        elif self.value == "location":
            return location(self.args, self.starting_pos, self.ending_pos, self.source)
        elif self.value == "particle":
            return particle(self.args, self.starting_pos, self.ending_pos, self.source)
        elif self.value == "potion":
            return potion(self.args, self.starting_pos, self.ending_pos, self.source)
        return self

    def simplify(self, mode=None, work_with=None):
        if mode == 1:
            error_from_object(self, "ActionError", translate("error.actionerror.action_cant_be_setter", {0: self}))
        if not self.special.has_special(self.value):
            if isinstance(self.special, special_class):
                error_from_object(self, "ActionError",
                                  translate("error.actionerror.unexists_calling_object_in_class",
                                            {0: self.value, 1: self.special.name}))
            error_from_object(self, "ActionError",
                              translate("error.actionerror.unexists_calling_object", {0: self.value}))
        special = self.special.get_special(self.value)
        previous_operations = []
        next_operations = []
        special, error_message, args, nun = special.check_args(self.args)
        if error_message is not None:
            error_from_object(*error_message)
        if special.type == "function" and special.inline:
            context = Context(Context.sources[-1])
            context.next_lvl()
        prev_ops, args, next_ops = special.fix_args(args)
        previous_operations.extend(prev_ops)
        next_ops.extend(next_operations)
        next_operations = next_ops
        if special.type == "function" and special.inline:
            context.update()
            context.next_jmcc_lvl()
            parser = Parser(special.operations, Context.sources[-1])
            context.settings["inline"].append(self.value)
            if context.settings["inline"].count(self.value) > 100:
                error_from_object(self, "RecursionError",
                                  translate("error.recursionerror.limit_reached", {0: self.value, 1: 100}))
            return_var = var(f"var.{new('inline')}", Vars.INLINE, self.starting_pos, self.ending_pos, self.source,
                             value_type=special.get_real_type())
            context.settings["allow_returns"].append(return_var)
            parser.current_token = parser.token(parser.index)
            context.add_operations(previous_operations)
            context.update()
            parser.eat(Tokens.LCPAREN)
            while (parser.current_token.type != Tokens.EOF) and (parser.current_token.type != Tokens.RCPAREN):
                context.add_operation(parser.up_statement(Tokens.RCPAREN))
                context.update()
            parser.eat(Tokens.RCPAREN)
            del Context.sources[-1]
            del parser
            previous_operations = context.get_operations()
            del context.settings["inline"][-1]
            del context.settings["allow_returns"][-1]
            data = context.get_inline(return_var.value)
            context.previous_lvl()
            context.previous_jmcc_lvl()
            if isinstance(data, var):
                data.value_type = return_var.get_real_type()
            if data is not None:
                if work_with is not None:
                    prev_ops, data, next_ops = assign([work_with], None, data, data.starting_pos, data.ending_pos,
                                                      data.source).simplify()
                elif not data.is_simple() and mode == 0:
                    prev_ops, data, next_ops = data.simplify(mode=0)
                else:
                    prev_ops, next_ops = [], []
                previous_operations.extend(prev_ops)
                next_ops.extend(next_operations)
                next_operations = next_ops
            return previous_operations, data, next_operations
        elif special.type == "function" and not special.inline:
            previous_operations.append(action("code", "call_function", calling_args([], {
                "function_name": text(special.name, Texts.LEGACY, self.starting_pos, self.ending_pos, self.source)},
                                                                                    self.starting_pos,
                                                                                    self.ending_pos,
                                                                                    self.source), self.starting_pos,
                                              self.ending_pos, self.source))
            if mode == 0:
                if special.return_var is None:
                    error_from_object(self, "ActionError",
                                      translate("error.actionerror.action_has_no_value", {0: self.value}))
                if isinstance(work_with, var):
                    if work_with.value != special.return_var.value:
                        previous_operations.append(action("variable", "set_value", calling_args([], {
                            "variable": work_with, "value": special.return_var}, self.starting_pos, self.ending_pos,
                                                                                                self.source),
                                                          self.starting_pos, self.ending_pos, self.source))
                else:
                    work_with = special.return_var
                return previous_operations, work_with, next_operations
        elif special.type == "process":
            previous_operations.append(action("code", "start_process", calling_args([], {
                "process_name": text(special.name, Texts.LEGACY, self.starting_pos, self.ending_pos, self.source),
                "target_mode": enum_("CURRENT_TARGET", self.starting_pos, self.ending_pos, self.source),
                "local_variables_mode": enum_("COPY", self.starting_pos, self.ending_pos, self.source)},
                                                                                    self.starting_pos,
                                                                                    self.ending_pos,
                                                                                    self.source), self.starting_pos,
                                              self.ending_pos, self.source))
            if mode == 0:
                error_from_object(self, "ActionError", translate("error.actionerror.action_has_no_value", {0: self}))
        else:
            error_from_object(self, "", translate("error.unknown11"))
        return previous_operations, None, next_operations

    def remove_inlines(self):
        self.args = self.args.remove_inlines()
        return self

    def get_type(self):
        return self.type

    def get_real_type(self):
        return self.value_type

    def can_cast_as(self, typ):
        return try_cast_as_class(self.get_real_type(), typ)

    def cast_as(self, typ, arges):
        return self


class calling_argument:  # is_jmcc_object
    type = "calling_argument"
    __slots__ = ("object", "arg", "value_type", "spec", "starting_pos", "ending_pos", "source")

    def __init__(self, obj: object, arg: str, starting_pos: int, ending_pos: int, source: str):
        self.object = obj
        self.arg = arg
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        self.value_type = None
        context = Context(Context.sources[-1])
        if not context.has_special(self.object.get_real_type()):
            error_from_object(self.object, "312", f"нету {self.object.get_real_type()}")
        self.spec = context.get_special(self.object.get_real_type())
        self.value_type = None
        if self.spec.has_special(f"{self.arg}.getter"):
            spec, error_message, args1, nun = self.spec.get_special(f"{self.arg}.getter").check_args(
                calling_args([self.object], {}, self.starting_pos, self.ending_pos,
                             self.source))
            if spec is not None:
                self.value_type = spec.get_real_type()
        elif self.spec.has_special(f"__get_attribute__"):
            spec, error_message, args1, nun = self.spec.get_special(f"__get_attribute__").check_args(
                calling_args([self.object, text(self.arg, Texts.LEGACY, self.starting_pos, self.ending_pos,
                                                self.source)], {}, self.starting_pos, self.ending_pos,
                             self.source))
            if spec is not None:
                self.value_type = spec.get_real_type()

    def __str__(self):
        return f'call_argument({self.object}, {self.arg})'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def is_independent():
        return False

    @staticmethod
    def is_simple():
        return False

    def simplify(self, mode=None, work_with=None):
        if mode == 1:
            if self.spec.has_special(f"{self.arg}.setter"):
                obj = calling_object(f"{self.arg}.setter",
                                     calling_args([self.object, work_with], {}, self.starting_pos, self.ending_pos,
                                                  self.source), self.starting_pos, self.ending_pos, self.source,
                                     self.spec)
            else:
                obj = calling_object(f"__set_attribute__",
                                     calling_args([self.object,
                                                   text(self.arg, Texts.LEGACY, self.starting_pos, self.ending_pos,
                                                        self.source), work_with], {}, self.starting_pos,
                                                  self.ending_pos,
                                                  self.source), self.starting_pos, self.ending_pos, self.source,
                                     self.spec)
            return obj.simplify()
        elif mode == 0:
            if self.spec.has_special(f"{self.arg}.getter"):
                obj = calling_object(f"{self.arg}.getter",
                                     calling_args([self.object], {}, self.starting_pos, self.ending_pos,
                                                  self.source), self.starting_pos, self.ending_pos, self.source,
                                     self.spec)
            else:
                obj = calling_object(f"__get_attribute__",
                                     calling_args([self.object,
                                                   text(self.arg, Texts.LEGACY, self.starting_pos, self.ending_pos,
                                                        self.source)], {}, self.starting_pos,
                                                  self.ending_pos,
                                                  self.source), self.starting_pos, self.ending_pos, self.source,
                                     self.spec)
            return obj.simplify(mode=0, work_with=work_with)

    def in_text(self):
        return None

    def remove_inlines(self):
        return self

    def get_type(self):
        return self.type

    def get_real_type(self):
        return self.value_type

    def can_cast_as(self, typ):
        return try_cast_as_class(self.get_real_type(), typ)

    def cast_as(self, typ, arges):
        return self


class calling_function:  # is_jmcc_object
    type = "calling_function"
    __slots__ = ("object", "value", "value_type", "args", "starting_pos", "ending_pos", "source")

    def __init__(self, obj: default_jmcc_object, val: str, args: calling_args, starting_pos: int, ending_pos: int,
                 source: str):
        self.object = obj
        self.value = val
        self.args = args
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        self.value_type = None
        if Context(Context.sources[-1]).has_special(self.object.get_real_type()):
            spec = Context(Context.sources[-1]).get_special(self.object.get_real_type())
            if spec.has_special(self.value):
                spec, error_message, args1, nun = spec.get_special(self.value).check_args(args)
                if spec is not None:
                    self.value_type = spec.get_real_type()
        elif self.value in {"__or__", "__and__", "__not__"}:
            self.value_type = "number"

    def __str__(self):
        return f'calling_function({self.object}, {self.value}, {self.args})'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def is_independent():
        return True

    @staticmethod
    def is_simple():
        return False

    def in_text(self):
        return None

    def simplify(self, mode=None, work_with=None):
        if mode == 0 or mode is None:
            if self.value in {"__or__", "__and__"}:
                if not isinstance(work_with, var):
                    work_with = var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)
                work_with.value_type = "number"
                true = number(1, self.starting_pos, self.ending_pos, self.source)
                false = number(0, self.starting_pos, self.ending_pos, self.source)
                false_thing = \
                    assign([work_with], None, false, self.starting_pos, self.ending_pos, self.source).simplify()[0]
                true_thing = assign([work_with], None, true, self.starting_pos, self.ending_pos,
                                    self.source).simplify()[0]
                if self.value == "__or__":
                    prev_ops, cur_var, next_ops = if_else_expr(self.args.positional[1], true, false, self.starting_pos,
                                                               self.ending_pos, self.source).simplify(mode=0,
                                                                                                      work_with=work_with)
                    prev_ops.extend(next_ops)
                    thing = assign([cur_var], None, true, self.starting_pos, self.ending_pos, self.source).simplify()
                    prev_ops, thing2, next_ops = if_(self.args.positional[0], thing[0], [], prev_ops,
                                                     self.starting_pos, self.ending_pos, self.source).simplify(mode=0)
                    return prev_ops, cur_var, next_ops
                elif self.value == "__and__":
                    prev_ops, thing2, next_ops = if_(self, true_thing, [], [], self.starting_pos,
                                                     self.ending_pos, self.source).simplify()
                    prev_ops.insert(0, false_thing[0])
                    return prev_ops, work_with, next_ops
            elif self.value == "__invert__":
                if not self.object.is_simple():
                    previous_operations, cur_op, next_operations = self.object.simplify(mode=mode, work_with=work_with)
                else:
                    previous_operations, cur_op, next_operations = [], self.object, []
                if not actions[cur_op.object][cur_op.name].setdefault("boolean", False):
                    error_from_object(self.object, "ArgumentError", translate("error.argumenterror.expected_boolean"))
                cur_op.invert = not cur_op.invert
                if cur_op.is_simple():
                    return previous_operations, cur_op, next_operations
                else:
                    prev_ops, cur_op, next_ops = cur_op.simplify(mode=mode, work_with=work_with)
                    previous_operations.extend(prev_ops)
                    next_ops.extend(next_operations)
                    next_operations = next_ops
                    return previous_operations, cur_op, next_operations
            elif Context(Context.sources[-1]).has_special(self.object.get_real_type()):
                special = Context(Context.sources[-1]).get_special(self.object.get_real_type())
                return calling_object(self.value, self.args, self.starting_pos, self.ending_pos, self.source,
                                      special).simplify(mode=mode, work_with=work_with)
            else:
                error_from_object(self.object, "NameError",
                                  translate("error.nameerror.special_not_found", {0: self.object.get_real_type()}))
        if mode == 1:
            error_from_object(self, "ActionError", translate("error.actionerror.action_cant_be_setter", {0: self}))

    def remove_inlines(self):
        self.args = self.args.remove_inlines()
        self.object = self.object.remove_inlines()
        return self

    def copy(self):
        return calling_function(self.object.copy(), self.value, self.args.copy(), self.starting_pos, self.ending_pos,
                                self.source)

    def get_type(self):
        return self.type

    def get_real_type(self):
        return self.value_type

    def can_cast_as(self, typ):
        return try_cast_as_class(self.get_real_type(), typ)

    def cast_as(self):
        return self


class subscript:  # is_jmcc_object
    type = "subscript"
    __slots__ = ("object", "arg1", "arg2", "value_type", "starting_pos", "ending_pos", "source", "spec")

    def __init__(self, obj: object, arg1: number, arg2: number, starting_pos: int, ending_pos: int, source: str):
        self.object = obj
        self.arg1 = arg1
        self.arg2 = arg2
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        context = Context(Context.sources[-1])
        if not context.has_special(self.object.get_real_type()):
            error_from_object(self.object, "", "найди отца")
        self.spec = context.get_special(self.object.get_real_type())
        self.value_type = None
        if self.spec is not None:
            if self.arg2 is None:
                if self.spec.has_special(f"__subscript__.getter"):
                    spec, error_message, args1, nun = self.spec.get_special(f"__subscript__.getter").check_args(
                        calling_args([self.object, self.arg1], {}, self.starting_pos, self.ending_pos,
                                     self.source))
                    if spec is not None:
                        self.value_type = spec.get_real_type()
            else:
                if self.spec.has_special(f"__slice__.getter"):
                    spec, error_message, args1, nun = self.spec.get_special(f"__slice__.getter").check_args(
                        calling_args([self.object, self.arg1, self.arg2], {}, self.starting_pos,
                                     self.ending_pos,
                                     self.source))
                    if spec is not None:
                        self.value_type = spec.get_real_type()

    def __str__(self):
        return f'subscript({self.object}, {self.arg1}:{self.arg2})'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def is_independent():
        return False

    @staticmethod
    def is_simple():
        return False

    def simplify(self, mode=None, work_with=None):
        if mode == 1:
            if self.arg2 is None:
                obj = calling_object(f"__subscript__.setter",
                                     calling_args([self.object, self.arg1, work_with], {}, self.starting_pos,
                                                  self.ending_pos,
                                                  self.source), self.starting_pos, self.ending_pos, self.source,
                                     self.spec)
            else:
                obj = calling_object(f"__slice__.setter",
                                     calling_args([self.object, self.arg1, self.arg2, work_with], {}, self.starting_pos,
                                                  self.ending_pos,
                                                  self.source), self.starting_pos, self.ending_pos, self.source,
                                     self.spec)
            return obj.simplify()
        else:
            if self.arg2 is None:
                obj = calling_object(f"__subscript__.getter",
                                     calling_args([self.object, self.arg1], {}, self.starting_pos, self.ending_pos,
                                                  self.source), self.starting_pos, self.ending_pos, self.source,
                                     self.spec)
            else:
                obj = calling_object(f"__slice__.getter",
                                     calling_args([self.object, self.arg1, self.arg2], {}, self.starting_pos,
                                                  self.ending_pos,
                                                  self.source), self.starting_pos, self.ending_pos, self.source,
                                     self.spec)
            return obj.simplify(mode=0, work_with=work_with)

    def in_text(self):
        return None

    def remove_inlines(self):
        return self

    def get_type(self):
        return self.type

    def get_real_type(self):
        return self.value_type

    def can_cast_as(self, typ):
        return try_cast_as_class(self.get_real_type(), typ)


def try_cast_as_class(class_typ, typ, additional=0):
    context = Context(Context.sources[-1])
    if not context.has_special(class_typ):
        return 0
    spec = context.get_special(class_typ)
    if not isinstance(spec, special_class):
        return 0
    return spec.can_cast_as(typ, additional=additional)


class if_:
    type = "if"
    __slots__ = ("condition", "operations", "eli", "els", "starting_pos", "ending_pos", "source")

    def __init__(self, condition: default_jmcc_object, operations: list, eli: list, els: list, starting_pos: int,
                 ending_pos: int,
                 source: str):
        self.condition = condition
        self.operations = operations
        self.eli = eli
        self.els = els
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source

    def __str__(self):
        return f'if({self.condition} {self.operations})'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def is_independent():
        return True

    @staticmethod
    def is_simple():
        return False

    def in_text(self):
        return None

    def simplify(self, mode=None, work_with=None):
        if self.condition.type == "calling_function" and self.condition.value == "__and__" and mode is None:
            prev_ops, thing, next_ops = if_(self.condition.args.positional[1], self.operations, self.eli, self.els,
                                            self.starting_pos,
                                            self.ending_pos, self.source).simplify()
            prev_ops.extend(next_ops)
            return if_(self.condition.args.positional[0], prev_ops, [], [], self.starting_pos, self.ending_pos,
                       self.source).simplify()
        previous_operations = []
        next_operations = []
        if not self.condition.is_simple():
            a = self.condition.simplify()
            prev_ops, self.condition, next_ops = a
            previous_operations.extend(prev_ops)
            next_ops.extend(next_operations)
            next_operations = next_ops
        if self.condition.type == "action":
            if not actions[self.condition.object][self.condition.name].setdefault("boolean", False):
                error_from_object(self.condition, "ArgumentError", translate("error.argumenterror.expected_boolean"))
            else:
                self.condition.operations = self.operations
            previous_operations.append(self.condition)
        elif (self.condition.type == "variable" and self.condition.value_type == "number") or (
                self.condition.type == "number"):
            nani, self.condition, nani2 = action("variable", "equals", calling_args([], {"value": self.condition,
                                                                                         "compare": lst([number(1,
                                                                                                                self.starting_pos,
                                                                                                                self.ending_pos,
                                                                                                                self.source)],
                                                                                                        self.starting_pos,
                                                                                                        self.ending_pos,
                                                                                                        self.source)},
                                                                                    self.starting_pos, self.ending_pos,
                                                                                    self.source), self.starting_pos,
                                                 self.ending_pos, self.source).simplify()
            self.condition.operations = self.operations
            previous_operations.append(self.condition)
        else:
            error_from_object(self.condition, "ArgumentError",
                              translate("error.argumenterror.wrong_argument", {0: self.condition.type, 1: "boolean"}))
        if (len(self.eli) > 0) or (len(self.els) > 0):
            nani, cur_thing, nani2 = action("code", "else",
                                            calling_args([], {}, self.starting_pos, self.ending_pos, self.source),
                                            self.starting_pos, self.ending_pos, self.source).simplify()
            if len(nani) + len(nani2) > 0:
                error_from_object(self, "", translate("error.unknown12"))
        else:
            cur_thing = None
        if len(self.eli) > 0:
            prev_ops, zap, next_ops = if_(self.eli[0][0], self.eli[0][1], self.eli[1:], self.els, self.starting_pos,
                                          self.ending_pos, self.source).simplify()
            cur_thing.operations = prev_ops
        elif len(self.els) > 0:
            cur_thing.operations = self.els
        if cur_thing is not None:
            previous_operations.append(cur_thing)
        if len(next_operations) > 0:
            error_from_object(self, "", translate("error.unknown13"))
        return previous_operations, None, next_operations


class function:
    type = "function"
    __slots__ = (
        "name", "operations", "args", "inline", "return_var", "ready", "description", "icon", "hide",
        "args_description",
        "source", "property", "specials")

    def __init__(self, name: str, operations: list, args: calling_args, source, inline=False, return_var=None,
                 ready=True, description=None, icon=None, hide=None, args_description=None, property_=None):
        self.name = name
        self.operations = operations
        self.args = args
        self.source = source
        self.inline = inline
        self.return_var = return_var
        self.ready = ready
        self.description = description
        self.icon = icon
        self.hide = hide
        self.args_description = args_description
        self.property = property_
        if self.inline and self.return_var is not None:
            self.return_var.var_type = Vars.INLINE
        self.specials = None

    def __str__(self):
        return f'function({self.name} {self.args} {self.operations})'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def is_independent():
        return True

    @staticmethod
    def is_simple():
        return True

    def is_ready(self):
        return self.ready

    def special(self):
        if self.specials is None:
            args = self.args.set_args()
            unpacked = {}
            if len(args) > 0:
                description = [(text(translate("function.generator.arguments"), Texts.LEGACY, -1, -1, self.source))]
                for i1 in args:
                    unpacked[i1["id"]] = i1["unpacked"]
                    argument = "argument." + str(i1['type']).lower() + ".name"
                    argument_type = translate(argument, fallback=i1['type'])
                    description_line = f" {i1['id']}: {argument_type}"
                    if self.args_description is not None and i1["id"] in self.args_description:
                        description_line += f" - {self.args_description[i1['id']]}"
                    description.append(text(description_line, Texts.LEGACY, -1, -1, self.source))
                if self.description is None:
                    self.description = []
                self.description.extend(description)
            self.specials = special_function(self.name, args, unpacked, self.return_var, self.inline,
                                 self.operations if self.inline else None)
        return self.specials

    def json(self):
        while len(self.operations) > 0 and self.operations[-1].type == "action" and (
                self.operations[-1].object == "code" and self.operations[-1].name == "return_function"):
            del self.operations[-1]
        a = {"type": "function", "position": new("event"), "operations": [i3.json() for i3 in self.operations],
             "name": self.name}
        args = {}
        if self.hide:
            args["is_hidden"] = enum_("TRUE", -1, -1, self.source)
        else:
            if self.return_var is not None:
                description = [text(translate("function.generator.return_var"), Texts.LEGACY, -1, -1, self.source)]
                argument = "argument." + str(self.return_var.value_type).lower() + ".name"
                argument_type = translate(argument, fallback=self.return_var.value_type)
                description_line = f" {self.return_var.value}: {argument_type}"
                if self.args_description is not None and self.return_var.value in self.args_description:
                    description_line += f" - {self.args_description[self.return_var.value]}"
                description.append(text(description_line, Texts.LEGACY, -1, -1, self.source))
                if self.description is None:
                    self.description = []
                self.description.extend(description)
            if self.description is not None:
                nani1, args["description"], nani2 = lst(self.description, -1, -1, self.source).simplify()
                if len(nani1) + len(nani2) > 0:
                    error_from_object(self, "", translate("error.unknown14"))
                for i1 in args["description"].values:
                    if not i1.type == "text":
                        error_from_object(i1, "", translate("error.unknown15"))
            if self.icon is not None:
                if not self.icon.is_simple():
                    nani1, args["icon"], nani2 = self.icon.simplify()
                    if len(nani1) + len(nani2) > 0:
                        error_from_object(self, "", translate("error.unknown16"))
                else:
                    args["icon"] = self.icon
                if not args["icon"].type == "item":
                    error_from_object(args["icon"], "", translate("error.unknown17"))
        if len(args) > 0:
            a["values"] = [{"name": k1, "value": v1.json()} for k1, v1 in args.items()]
        return a

    def copy(self):
        return self


class process:
    type = "process"
    __slots__ = ("name", "operations", "args", "ready", "description", "icon", "hide", "args_description", "source")

    def __init__(self, name: str, operations: list, args: calling_args, source, ready=True, hide=None, description=None,
                 icon=None, args_description=None):
        self.name = name
        self.operations = operations
        self.args = args
        self.source = source
        self.ready = ready
        self.hide = hide
        self.description = description
        self.icon = icon
        self.args_description = args_description

    def __str__(self):
        return f'process({self.name} {self.args} {self.operations})'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def is_independent():
        return True

    @staticmethod
    def is_simple():
        return True

    def special(self):
        args = self.args.set_args()
        unpacked = {}
        if len(args) > 0:
            description = [(text(translate("function.generator.arguments"), Texts.LEGACY, -1, -1, self.source))]
            for i1 in args:
                unpacked[i1["id"]] = i1["unpacked"]
                argument = "argument." + str(i1['type']).lower() + ".name"
                argument_type = translate(argument, fallback=i1['type'])
                description_line = f" {i1['id']}: {argument_type}"
                if self.args_description is not None and i1["id"] in self.args_description:
                    description_line += f" - {self.args_description[i1['id']]}"
                description.append(text(description_line, Texts.LEGACY, -1, -1, self.source))
            if self.description is None:
                self.description = []
            self.description.extend(description)
        return special_process(self.name, args, unpacked)

    def is_ready(self):
        return self.ready

    def json(self):
        a = {"type": "process", "position": new('event'), "operations": [i3.json() for i3 in self.operations],
             "name": self.name}
        args = {}
        if self.hide:
            args["is_hidden"] = enum_("TRUE", -1, -1, self.source)
        else:
            if self.description is not None:
                nani1, args["description"], nani2 = lst(self.description, -1, -1, self.source).simplify()
                if len(nani1) + len(nani2) > 0:
                    error_from_object(self, "", translate("error.unknown18"))
                for i1 in args["description"].values:
                    if not i1.type == "text":
                        error_from_object(i1, "", translate("error.unknown19"))
            if self.icon is not None:
                if not self.icon.is_simple():
                    nani1, args["icon"], nani2 = self.icon.simplify()
                    if len(nani1) + len(nani2) > 0:
                        error_from_object(self, "", translate("error.unknown20"))
                else:
                    args["icon"] = self.icon
                if not args["icon"].type == "item":
                    error_from_object(args["icon"], "", translate("error.unknown21"))
        if len(args) > 0:
            a["values"] = [{"name": k1, "value": v1.json()} for k1, v1 in args.items()]
        return a

    def copy(self):
        return self


class return_:
    type = None
    __slots__ = ("object", "in_var", "starting_pos", "ending_pos", "source")

    def __init__(self, obj: default_jmcc_object, starting_pos: int, ending_pos: int,
                 source: str, in_var=None):
        self.object = obj
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        self.in_var = in_var

    def __str__(self):
        return f'return({self.object})'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def is_independent():
        return True

    @staticmethod
    def is_simple():
        return False

    def in_text(self):
        return None

    def simplify(self, mode=None, work_with=None):
        previous_operations = []
        next_operations = []
        if mode == 0:
            if not isinstance(work_with, var):
                if len(Context(Context.sources[-1]).settings["inline"]) == 0:
                    work_with = var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)
                else:
                    work_with = var(f"var.{new('inline')}", Vars.INLINE, self.starting_pos, self.ending_pos,
                                    self.source)
            else:
                work_with = self.in_var
        else:
            work_with = self.in_var
        prev_ops, cur_op, next_ops = action("variable", "set_value",
                                            calling_args([], {"variable": work_with, "value": self.object},
                                                         self.starting_pos,
                                                         self.ending_pos,
                                                         self.source), self.starting_pos, self.ending_pos,
                                            self.source).simplify()
        previous_operations.extend(prev_ops)
        next_ops.extend(next_operations)
        next_operations = next_ops
        if len(Context(Context.sources[-1]).settings["inline"]) == 0:
            next_operations.append(
                action("code", "return_function", calling_args([], {}, self.starting_pos, self.ending_pos, self.source),
                       self.starting_pos, self.ending_pos, self.source))
        return previous_operations, cur_op, next_operations

    def remove_inlines(self):
        self.object = self.object.remove_inlines()
        return self


class event:
    type = "event"
    __slots__ = ("name", "operations", "ready", "source")

    def __init__(self, name: str, operations: list, source, ready=True):
        self.name = name
        self.operations = operations
        self.source = source
        self.ready = ready

    def __str__(self):
        return f'event({self.name} {self.operations})'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def is_independent():
        return True

    @staticmethod
    def is_simple():
        return True

    def is_ready(self):
        return self.ready

    def json(self):
        if self.name not in events:
            error_from_object(self, "NameError", translate("error.unexistsevent", {0: self.name}))
        return {"type": "event", "event": self.name, "position": new("event"),
                "operations": [i3.json() for i3 in self.operations]}

    def copy(self):
        return self


class assign:
    type = "assign"
    __slots__ = ("variables", "object", "assign_type", "starting_pos", "ending_pos", "source")

    def __init__(self, variables: list, assign_type: str, obj: default_jmcc_object, starting_pos: int, ending_pos: int,
                 source: str):
        self.variables = variables
        self.object = obj
        self.assign_type = assign_type
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source

    def __str__(self):
        return f'assign({self.variables} {self.assign_type} {self.object})'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def is_independent():
        return True

    @staticmethod
    def is_simple():
        return False

    def in_text(self):
        return None

    def simplify(self, mode=None, work_with=None):
        if self.assign_type is None:
            if self.object.get_type() == "action":
                return self.object.simplify(mode=0, work_with=self.variables)
            return action("variable", "set_value",
                          calling_args([], {"value": self.object}, self.starting_pos, self.ending_pos, self.source),
                          self.starting_pos, self.ending_pos, self.source).simplify(mode=0, work_with=self.variables)
        else:
            return action("variable", "set_value",
                          calling_args([], {"value": calling_function(self.variables[0], self.assign_type,
                                                                      calling_args([self.variables[0], self.object], {},
                                                                                   self.starting_pos, self.ending_pos,
                                                                                   self.source), self.starting_pos,
                                                                      self.ending_pos, self.source)}, self.starting_pos,
                                       self.ending_pos, self.source),
                          self.starting_pos, self.ending_pos, self.source).simplify(mode=0, work_with=self.variables)


def check_args(self, args, casts_allowed, strict_check=False):
    args1 = {}
    args2, error_message = args.get_args(list(self.arges), func=self.template)
    if args2 is None:
        return None, error_message, None, 0
    identity_counter = 0
    len_ = len(args2) if len(args2) > 0 else 1
    if args2 is None:
        return None, error_message, None, 0
    for k1, v1 in args2.items():
        if v1 is None:
            if "array" in self.arges[k1] and not strict_check:
                args1[k1] = lst([], self.starting_pos, self.ending_pos, self.source)
                continue
            elif len(self.template) > 0:
                v1 = self.arges[k1]["default_value"] if "default_value" in self.arges[k1] else None
                if v1 is None:
                    return None, (
                        args, "ArgumentError",
                        translate("error.argumenterror.argument_is_not_specified", {0: k1})), None, 0
            args1[k1] = v1
            continue
        if v1.get_type() == "variable" and v1.get_real_type() is None:
            v2 = v1.remove_inlines()
            v1.value_type = Context(v2.source).get_variable_type(v2.var_type, v2.value)
        args1[k1] = v1
        if "array" in self.arges[k1] and self.arges[k1]["type"] != "array" and v1.get_type() != "array":
            args1[k1] = lst([v1], v1.starting_pos, v1.ending_pos, v1.source)
            identity_counter += 1
            continue
        if (v1.get_type() == self.arges[k1]["type"] or (
                isinstance(self.arges[k1]["type"], (tuple, list, set)) and v1.get_type() in self.arges[k1]["type"])) or \
                self.arges[k1]["type"] == "any":
            identity_counter += 1
            continue
        elif (v1.get_real_type() == self.arges[k1]["type"] or (
                isinstance(self.arges[k1]["type"], (tuple, list, set)) and v1.get_real_type() in self.arges[k1][
            "type"])) or (
                v1.get_real_type() == "any" or v1.get_real_type() is None) and not strict_check:
            identity_counter += 1
            continue
        elif "array" in self.arges[k1] and v1.get_type() == "array":
            identity_counter += 1
            continue
        elif self.arges[k1]["type"] == "text":
            continue
        elif v1.get_real_type() == "text":
            continue
        else:
            if casts_allowed and not isinstance(self.arges[k1]["type"], (tuple, list, set)):
                cast = v1.can_cast_as(self.arges[k1]["type"])
                if cast != 0:
                    identity_counter += cast
                    continue
            return None, (v1, "ArgumentError", translate("error.argumenterror.wrong_argument", {0: v1.get_type() + (
                f"[{v1.get_real_type()}]" if v1.get_real_type() not in {None, "any", v1.get_type()} else ""),
                                                                                                1: self.arges[k1][
                                                                                                    "type"]})), None, 0
    return self, None, args1, identity_counter / len_


def fix_args(self, args, casts_allowed, inline=False, assigning=None, strict_check=False):
    previous_operations = []
    next_operations = []
    remove_keys = set()
    super_args = []
    for k1, v1 in args.items():
        if v1 is None:
            remove_keys.add(k1)
            continue
        if assigning is None:
            var_thing = var(k1, Vars.LOCAL if not inline else Vars.INLINE, v1.starting_pos, v1.ending_pos, v1.source,
                            value_type=self.arges[k1]["type"])
            if inline:
                Context(v1.source).set_variable(k1, var_thing.var_type)
        else:
            var_thing = None
        if v1.is_simple():
            args[k1] = v1
        else:
            if "array" in self.arges[k1] and v1.type == "array":
                prev_ops, args[k1], next_ops = v1.simplify(len_limit=self.arges[k1]["array"])
            elif assigning is not None and self.arges[k1]["type"] == "variable" and k1 in assigning:
                prev_ops, args[k1], next_ops = v1.simplify(mode=1)
            elif (v1.type in ("map", "array")) and strict_check:
                prev_ops, args[k1], next_ops = v1.simplify()
            else:
                prev_ops, args[k1], next_ops = v1.simplify(mode=0)
            previous_operations.extend(prev_ops)
            next_ops.extend(next_operations)
            next_operations = next_ops
        if casts_allowed and args[k1].can_cast_as(self.arges[k1]["type"]) != 0:
            args[k1] = args[k1].cast_as(self.arges[k1]["type"], self.arges[k1])
        if not (args[k1].type == "variable" and args[k1].value == k1) and assigning is None:
            if not v1.is_simple() and not inline:
                prev_ops, args[k1], next_ops = action("variable", "set_value",
                                                      calling_args([], {"value": args[k1]}, args[k1].starting_pos,
                                                                   args[k1].ending_pos, args[k1].source),
                                                      args[k1].starting_pos, args[k1].ending_pos,
                                                      args[k1].source).simplify(mode=0)
                previous_operations.extend(prev_ops)
                next_ops.extend(next_operations)
                next_operations = next_ops
            super_args.append((var_thing, k1))
        elif assigning is not None and k1 in assigning:
            if args[k1].get_real_type() in ("any", None):
                args[k1].value_type = assigning[k1]
        if self.arges[k1]["type"] == "variable" and not "array" in self.arges[k1]:
            Context(Context.sources[-1]).set_variable_type(v1.var_type, v1.value, v1.get_real_type())
    for var_thing, k1 in super_args:
        prev_ops, args[k1], next_ops = assign([var_thing], None, args[k1], args[k1].starting_pos, args[k1].ending_pos,
                                              args[k1].source).simplify()
        previous_operations.extend(prev_ops)
        next_ops.extend(next_operations)
        next_operations = next_ops
        var_thing.value_type = self.arges[k1]["type"]
        Context(var_thing.source).set_variable_type(var_thing.var_type, var_thing.value, var_thing.get_real_type())
    for k1 in remove_keys:
        del args[k1]
    return previous_operations, args, next_operations


class special_function:
    __slots__ = ("name", "args", "arges", "template", "return_var", "inline", "operations")
    type = "function"

    def __init__(self, name, args, template, return_var, inline, operations=None):
        self.name = name
        self.args = args
        self.arges = {i1["id"]: i1 for i1 in self.args}
        self.template = template
        self.return_var = return_var
        self.inline = inline
        self.operations = operations

    def add_overload(self, jmcc_special):
        return special_overload(self.name, [self, jmcc_special])

    def fix_args(self, args, casts_allowed=True):
        return fix_args(self, args, casts_allowed, self.inline)

    def check_args(self, args, casts_allowed=True):
        return check_args(self, args, casts_allowed)

    def get_real_type(self):
        return self.return_var.value_type if self.return_var is not None else None


class special_process:
    __slots__ = ("name", "args", "arges", "template")
    type = "process"

    def __init__(self, name, args, template):
        self.name = name
        self.args = args
        self.arges = {i1["id"]: i1 for i1 in self.args}
        self.template = template

    def add_overload(self, jmcc_special):
        return special_overload(self.name, [self, jmcc_special])

    def fix_args(self, args, casts_allowed=True):
        return fix_args(self, args, casts_allowed)

    def check_args(self, args, casts_allowed=True):
        return check_args(self, args, casts_allowed)


class special_class:
    type = "class"
    __slots__ = ("name", "functions", "class_obj", "parents")

    def __init__(self, name, functions, class_obj, parents):
        self.name = name
        self.functions = functions
        self.class_obj = class_obj
        self.parents: list = parents

    def get_special(self, name):
        return self.functions[name]

    def has_special(self, name):
        return name in self.functions

    def check_args(self, args, casts_allowed=True):
        if self.class_obj not in args.positional:
            args.positional.insert(0, self.class_obj)
        return self.functions["__init__"].check_args(args, casts_allowed)

    def can_cast_as(self, typ, additional=0):
        if typ in self.parents:
            return (self.parents.index(typ) + 1) / (len(self.parents) + additional)
        return 0


class special_overload:
    __slots__ = ("name", "overload_list")
    type = "overload"

    def __init__(self, name, overload_list):
        self.name = name
        self.overload_list = overload_list

    def add_overload(self, jmcc_special):
        self.overload_list.append(jmcc_special)
        return self

    def get_special(self, name):
        for i1 in self.overload_list:
            if i1.name == name:
                return i1
        return None

    def has_special(self, name):
        for i1 in self.overload_list:
            if i1.name == name:
                return True
        return False

    def check_args(self, args, casts_allowed=False):
        ret_special, ret_error_message, ret_args1, pow_index = None, None, None, -1
        index_ = 0
        for i1 in range(len(self.overload_list)):
            special, error_message, args1, power_index = self.overload_list[i1].check_args(args, casts_allowed)
            if power_index > pow_index:
                ret_special, ret_error_message, ret_args1 = special, error_message, args1
                index_ = i1 + 1
        return ret_special, ret_error_message, ret_args1, index_ / len(self.overload_list)


class enum_:  # is_jmcc_object
    type = "enum"
    __slots__ = ("value", "var", "simple", "starting_pos", "ending_pos", "source")

    def __init__(self, val: str, starting_pos: int, ending_pos: int, source: str, variable=None):
        self.value = val
        self.var = variable
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        self.simple = (variable is None) or (variable.is_simple())

    def __str__(self):
        return f'enum({self.value})'

    def __repr__(self):
        return self.__str__()

    def is_simple(self):
        return self.simple

    def simplify(self):
        prev_ops, self.var, next_ops = self.var.simplify()
        return prev_ops, self, next_ops

    def json(self):
        a = {"type": "enum", "enum": self.value}
        if self.var is not None:
            a["variable"] = self.var.value
            a["scope"] = Vars.changer[self.var.var_type].lower()
        return a

    def copy(self):
        return self

    @staticmethod
    def is_independent():
        return False

    def remove_inlines(self):
        if self.var is not None:
            self.var = self.var.remove_inlines()
        return self

    def get_type(self):
        return self.type

    def get_real_type(self):
        return self.get_type()


class block:  # is_jmcc_object
    type = "block"
    __slots__ = ("id", "starting_pos", "ending_pos", "source")

    def __init__(self, id_: str, starting_pos: int, ending_pos: int, source: str):
        self.id = id_.lower().replace("minecraft:", "")
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        self.check_block()

    def check_block(self):
        if "%" in self.id:
            return
        parameters = self.id.find("[")
        if parameters == -1:
            if self.id not in blocks:
                error_from_object(self, "ArgumentError",
                                  translate("error.unexistsblock", {0: self.id}))
            return
        block_id = self.id[:self.id.find("[")]
        if block_id not in blocks:
            error_from_object(self, "ArgumentError",
                              translate("error.unexistsblock", {0: block_id}))
        if self.id[-1] != "]":
            error_from_object(self, "ArgumentError",
                              translate("error.wrongblock", {0: self.id}))
        parameters = self.id[parameters + 1:-1]
        states = blocks[block_id]
        for data in parameters.split(","):
            k, v = data.split("=")
            if k not in states:
                error_from_object(self, "ArgumentError",
                                  translate("error.wrongblock_state", {0: k, 1: ", ".join(states)}))
            if v not in states[k]:
                error_from_object(self, "ArgumentError",
                                  translate("error.wrongblock_state_value", {0: v, 1: ", ".join(states[k])}))

    def __str__(self):
        return f'block({self.id})'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def is_simple():
        return True

    @staticmethod
    def is_independent():
        return False

    def json(self):
        return {"type": "block", "block": self.id}

    def copy(self):
        return self

    def remove_inlines(self):
        return self

    def get_type(self):
        return self.type

    def get_real_type(self):
        return self.get_type()


def minecraft_text(text1):
    def next_symbol(afsd, fdsa):
        if fdsa >= len(afsd):
            return fdsa + 1, None
        return fdsa + 1, afsd[fdsa]

    pos = 0
    msg = ""
    full_msg = nbtworker.List()

    def add(txt):
        new_txt = nbtworker.Compound()
        for i1 in txt.keys():
            if (i1 == "italic" and txt[i1].value == 0) or txt[i1].value != 0:
                new_txt[i1] = txt[i1]
        full_msg.append(new_txt)

    italic = False
    obfuscated = False
    underlined = False
    strikethrough = False
    color = color_codes["f"]
    bold = False
    while (s := next_symbol(text1, pos))[1] is not None:
        pos, symbol = s[0], s[1]
        if symbol == "&" and (s := next_symbol(text1, pos))[1] is not None:
            pos, symbol = s[0], s[1]
            if symbol in color_codes:
                if msg != "":
                    old_msg = nbtworker.Compound(
                        text=nbtworker.String(msg),
                        italic=nbtworker.Byte(int(italic)),
                        obfuscated=nbtworker.Byte(int(obfuscated)),
                        underlined=nbtworker.Byte(int(underlined)),
                        strikethrough=nbtworker.Byte(int(strikethrough)),
                        bold=nbtworker.Byte(int(bold)),
                        color=nbtworker.String(color))
                    add(old_msg)
                    msg = ""
                italic = False
                obfuscated = False
                underlined = False
                strikethrough = False
                color = color_codes[symbol]
                bold = False
                continue
            elif symbol == "r":
                if msg != "":
                    old_msg = nbtworker.Compound(
                        text=nbtworker.String(msg),
                        italic=nbtworker.Byte(int(italic)),
                        obfuscated=nbtworker.Byte(int(obfuscated)),
                        underlined=nbtworker.Byte(int(underlined)),
                        strikethrough=nbtworker.Byte(int(strikethrough)),
                        bold=nbtworker.Byte(int(bold)),
                        color=nbtworker.String(color))
                    add(old_msg)
                    msg = ""
                italic = False
                obfuscated = False
                underlined = False
                strikethrough = False
                color = color_codes["f"]
                bold = False
                continue
            elif symbol == "n":
                if msg != "":
                    old_msg = nbtworker.Compound(
                        text=nbtworker.String(msg),
                        italic=nbtworker.Byte(int(italic)),
                        obfuscated=nbtworker.Byte(int(obfuscated)),
                        underlined=nbtworker.Byte(int(underlined)),
                        strikethrough=nbtworker.Byte(int(strikethrough)),
                        bold=nbtworker.Byte(int(bold)),
                        color=nbtworker.String(color))
                    add(old_msg)
                    msg = ""
                underlined = True
                continue
            elif symbol == "m":
                if msg != "":
                    old_msg = nbtworker.Compound(
                        text=nbtworker.String(msg),
                        italic=nbtworker.Byte(int(italic)),
                        obfuscated=nbtworker.Byte(int(obfuscated)),
                        underlined=nbtworker.Byte(int(underlined)),
                        strikethrough=nbtworker.Byte(int(strikethrough)),
                        bold=nbtworker.Byte(int(bold)),
                        color=nbtworker.String(color))
                    add(old_msg)
                    msg = ""
                strikethrough = True
                continue
            elif symbol == "o":
                if msg != "":
                    old_msg = nbtworker.Compound(
                        text=nbtworker.String(msg),
                        italic=nbtworker.Byte(int(italic)),
                        obfuscated=nbtworker.Byte(int(obfuscated)),
                        underlined=nbtworker.Byte(int(underlined)),
                        strikethrough=nbtworker.Byte(int(strikethrough)),
                        bold=nbtworker.Byte(int(bold)),
                        color=nbtworker.String(color))
                    add(old_msg)
                    msg = ""
                italic = True
                continue
            elif symbol == "l":
                if msg != "":
                    old_msg = nbtworker.Compound(
                        text=nbtworker.String(msg),
                        italic=nbtworker.Byte(int(italic)),
                        obfuscated=nbtworker.Byte(int(obfuscated)),
                        underlined=nbtworker.Byte(int(underlined)),
                        strikethrough=nbtworker.Byte(int(strikethrough)),
                        bold=nbtworker.Byte(int(bold)),
                        color=nbtworker.String(color))
                    add(old_msg)
                    msg = ""
                bold = True
                continue
            elif symbol == "k":
                if msg != "":
                    old_msg = nbtworker.Compound(
                        text=nbtworker.String(msg),
                        italic=nbtworker.Byte(int(italic)),
                        obfuscated=nbtworker.Byte(int(obfuscated)),
                        underlined=nbtworker.Byte(int(underlined)),
                        strikethrough=nbtworker.Byte(int(strikethrough)),
                        bold=nbtworker.Byte(int(bold)),
                        color=nbtworker.String(color))
                    add(old_msg)
                    msg = ""
                obfuscated = True
                continue
            elif symbol == "#":
                thing = "#"
                if (s := next_symbol(text1, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if symbol not in allowed_symbols:
                        msg += "&" + thing
                        continue
                if (s := next_symbol(text1, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if symbol not in allowed_symbols:
                        msg += "&" + thing
                        continue
                if (s := next_symbol(text1, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if symbol not in allowed_symbols:
                        msg += "&" + thing
                        continue
                if (s := next_symbol(text1, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if symbol not in allowed_symbols:
                        msg += "&" + thing
                        continue
                if (s := next_symbol(text1, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if symbol not in allowed_symbols:
                        msg += "&" + thing
                        continue
                if (s := next_symbol(text1, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if symbol not in allowed_symbols:
                        msg += "&" + thing
                        continue
                if msg != "":
                    old_msg = nbtworker.Compound(
                        text=nbtworker.String(msg),
                        italic=nbtworker.Byte(int(italic)),
                        obfuscated=nbtworker.Byte(int(obfuscated)),
                        underlined=nbtworker.Byte(int(underlined)),
                        strikethrough=nbtworker.Byte(int(strikethrough)),
                        bold=nbtworker.Byte(int(bold)),
                        color=nbtworker.String(color))
                    add(old_msg)
                    msg = ""
                color = thing.upper()
                continue
            msg += "&" + symbol
            continue

        msg += symbol
        continue
    if msg != "":
        old_msg = nbtworker.Compound(
            text=nbtworker.String(msg),
            italic=nbtworker.Byte(int(italic)),
            obfuscated=nbtworker.Byte(int(obfuscated)),
            underlined=nbtworker.Byte(int(underlined)),
            strikethrough=nbtworker.Byte(int(strikethrough)),
            bold=nbtworker.Byte(int(bold)),
            color=nbtworker.String(color))
        add(old_msg)
    if len(full_msg.values) > 1:
        real_msg = full_msg[0]
        full_msg.values = full_msg.values[1:]
        real_msg["extra"] = full_msg
        return real_msg
    elif len(full_msg.values) == 1:
        return full_msg[0]
    else:
        return nbtworker.Compound(text=nbtworker.String(""))


# noinspection PyUnresolvedReferences
class item:  # is_jmcc_object
    type = "item"
    arges = {"id": {"id": "id", "type": "text", "pos": 0},
             "name": {"id": "name", "type": "text", "default_value": default_jmcc_object, "pos": 1},
             "count": {"id": "count", "type": "number", "default_value": number(1, -1, -1, None), "pos": 2},
             "lore": {"id": "lore", "type": "array", "default_value": default_jmcc_object, "pos": 3},
             "nbt": {"id": "nbt", "type": "snbt", "default_value": default_jmcc_object, "pos": 4},
             "custom_tags": {"id": "custom_tags", "type": "map", "default_value": default_jmcc_object, "pos": 5}}
    template = {"id": 0, "name": 0, "count": 0, "lore": 0, "nbt": 0, "custom_tags": 0}
    __slots__ = ("args", "new_args", "item", "simple", "starting_pos", "ending_pos", "source")

    def __init__(self, args: calling_args, starting_pos: int, ending_pos: int, source: str):
        self.args = args
        self.new_args = {}
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        self.item = nbtworker.Compound()
        self.simple = False

    def __str__(self):
        return f'item({self.args})'

    def __repr__(self):
        return self.__str__()

    def is_simple(self):
        return self.simple

    def simplify(self, mode=None, work_with=None):
        ret = built_in_simplify(self, mode, work_with)
        if ret[1] is self:
            self.new_args["id"].value = self.new_args["id"].value.lower().replace("minecraft:", "")
            if self.new_args["id"].value not in items:
                error_from_object(self.new_args["potion"], "ArgumentError",
                                  translate("error.unexistsitem", {0: self.new_args["id"].value}))
            self.item = nbtworker.Compound(
                id=nbtworker.String(self.new_args["id"].value),
                count=nbtworker.Int(self.new_args["count"].value))
            if self.new_args["nbt"] is not default_jmcc_object:
                self.item["components"] = self.new_args["nbt"].value
            if self.new_args["name"] is not default_jmcc_object or self.new_args["lore"] is not default_jmcc_object or \
                    self.new_args["custom_tags"] is not default_jmcc_object:
                if "components" not in self.item:
                    self.item["components"] = nbtworker.Compound()
                if self.new_args["name"] is not default_jmcc_object:
                    self.item["components"]["minecraft:custom_name"] = minecraft_text(self.new_args["name"].value)
                if self.new_args["lore"] is not default_jmcc_object:
                    self.item["components"]["minecraft:lore"] = nbtworker.List(
                        *map(minecraft_text, [i1.value for i1 in self.new_args["lore"].values]))
                if self.new_args["custom_tags"] is not default_jmcc_object:
                    if "custom_data" not in self.item:
                        self.item["components"]["minecraft:custom_data"] = nbtworker.Compound()
                    if "PublicBukkitValues" not in self.item["components"]:
                        self.item["components"]["minecraft:custom_data"]["PublicBukkitValues"] = nbtworker.Compound()
                    for ind in range(len(self.new_args["custom_tags"].keys)):
                        k1, v1 = self.new_args["custom_tags"].keys[ind].value, self.new_args["custom_tags"].values[
                            ind].value
                        self.item["components"]["minecraft:custom_data"]["PublicBukkitValues"][
                            f"justcreativeplus:{k1}"] = nbtworker.String(str(v1))
        return ret

    def in_text(self):
        return None

    def json(self):
        return {"type": "item", "item": str(self.item)}

    def copy(self):
        return self

    def remove_inlines(self):
        if self.simple:
            return self
        self.args = self.args.remove_inlines()
        return self

    @staticmethod
    def is_independent():
        return False

    def get_type(self):
        return self.type

    def get_real_type(self):
        return self.get_type()

    def can_cast_as(self, typ):
        if typ in ("block", "text"):
            return 1
        return try_cast_as_class(self.get_real_type(), typ, 2)

    def cast_as(self, typ, arg_thing=None):
        if typ == "block":
            block_id = self.item["id"].value
            if "components" in self.item and "minecraft:block_state" in self.item["components"] and isinstance(
                    self.item["components"]["minecraft:block_state"], nbtworker.Compound):
                block_id += "[" + ",".join([f"{k1}={v1.value}" for k1, v1 in self.item["components"][
                    "minecraft:block_state"].values.items()]) + "]"
            return block(block_id, self.starting_pos, self.ending_pos, self.source)
        elif typ == "text":
            item_data = str(self.item).replace("\"", "\\\"")
            return text(f"\"{item_data}\"", Texts.LEGACY, self.starting_pos, self.ending_pos, self.source)


# noinspection PyUnresolvedReferences
class location:  # is_jmcc_object
    type = "location"
    arges = {"x": {"id": "x", "type": "number", "default_value": number(0, -1, -1, None), "pos": 0},
             "y": {"id": "y", "type": "number", "default_value": number(0, -1, -1, None), "pos": 1},
             "z": {"id": "z", "type": "number", "default_value": number(0, -1, -1, None), "pos": 2},
             "yaw": {"id": "yaw", "type": "number", "default_value": number(0, -1, -1, None), "pos": 3},
             "pitch": {"id": "pitch", "type": "number", "default_value": number(0, -1, -1, None), "pos": 4}}
    template = {"x": 0, "y": 0, "z": 0, "yaw": 0, "pitch": 0}
    __slots__ = ("args", "new_args", "simple", "starting_pos", "ending_pos", "source")

    def __init__(self, args: calling_args, starting_pos: int, ending_pos: int, source: str):
        self.args = args
        self.new_args = {}
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        self.simple = False

    def __str__(self):
        return f'location({self.args})'

    def __repr__(self):
        return self.__str__()

    def is_simple(self):
        return self.simple

    def simplify(self, mode=None, work_with=None):
        return built_in_simplify(self, mode, work_with)

    def json(self):
        return {"type": "location", "x": self.new_args["x"].value, "y": self.new_args["y"].value,
                "z": self.new_args["z"].value, "yaw": self.new_args["yaw"].value, "pitch": self.new_args["pitch"].value}

    def in_text(self):
        return None

    def copy(self):
        return self

    @staticmethod
    def is_independent():
        return False

    def remove_inlines(self):
        if self.simple:
            return self
        self.args = self.args.remove_inlines()
        return self

    def get_type(self):
        return self.type

    def get_real_type(self):
        return self.get_type()

    def can_cast_as(self, typ):
        return try_cast_as_class(self.get_real_type(), typ)

    def cast_as(self, typ, arges):
        return self


def built_in_simplify(self, mode, work_with):
    special, error_message, args1, nun = check_args(self, self.args, True, strict_check=True)
    if error_message is not None:
        spec = Context(Context.sources[-1])
        if spec.has_special(self.type):
            spec = spec.get_special(self.type)
            if spec.has_special("__init__"):
                return calling_object(self.type, self.args.copy(), self.starting_pos, self.ending_pos,
                                      self.source).simplify(mode=mode, work_with=work_with)
        error_from_object(*error_message)
    previous_operations, self.new_args, next_operations = fix_args(self, args1, True, assigning={}, strict_check=True)
    if len(previous_operations) == 0 and len(next_operations) == 0:
        self.simple = True
        if work_with is not None:
            return assign([work_with], None, self, self.starting_pos, self.ending_pos, self.source).simplify()
        return previous_operations, self, next_operations
    else:
        error_from_object(self, "", "ты чо как это сделал")


# noinspection PyUnresolvedReferences
class vector:  # is_jmcc_object
    type = "vector"
    arges = {"x": {"id": "x", "type": "number", "default_value": number(0, -1, -1, None), "pos": 0},
             "y": {"id": "y", "type": "number", "default_value": number(0, -1, -1, None), "pos": 1},
             "z": {"id": "z", "type": "number", "default_value": number(0, -1, -1, None), "pos": 2}}
    template = {"x": 0, "y": 0, "z": 0}
    __slots__ = ("args", "new_args", "simple", "starting_pos", "ending_pos", "source")

    def __init__(self, args: calling_args, starting_pos: int, ending_pos: int, source: str):
        self.args = args
        self.new_args = {}
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        self.simple = False

    def __str__(self):
        return f'vector({self.args})'

    def __repr__(self):
        return self.__str__()

    def is_simple(self):
        return self.simple

    def in_text(self):
        return None

    @staticmethod
    def is_independent():
        return False

    def simplify(self, mode=None, work_with=None):
        return built_in_simplify(self, mode, work_with)

    def json(self):
        return {"type": "vector", "x": self.new_args["x"].value, "y": self.new_args["y"].value,
                "z": self.new_args["z"].value}

    def copy(self):
        return self

    def remove_inlines(self):
        if self.is_simple():
            return self
        self.args = self.args.remove_inlines()
        return self

    def get_type(self):
        return self.type

    def get_real_type(self):
        return self.get_type()

    def can_cast_as(self, typ):
        return try_cast_as_class(self.get_real_type(), typ)

    def cast_as(self, typ, arges):
        return self


# noinspection PyUnresolvedReferences
class potion:  # is_jmcc_object
    type = "potion"
    arges = {"potion": {"id": "potion", "type": "text", "pos": 0},
             "amplifier": {"id": "amplifier", "type": "number", "default_value": number(1, -1, -1, None), "pos": 1},
             "duration": {"id": "duration", "type": "number", "default_value": number(-1, -1, -1, None), "pos": 2}}
    template = {"potion": 0, "amplifier": 0, "duration": 0}
    __slots__ = ("args", "new_args", "simple", "starting_pos", "ending_pos", "source")

    def __init__(self, args: calling_args, starting_pos: int, ending_pos: int, source: str):
        self.args = args
        self.new_args = {}
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        self.simple = False

    def __str__(self):
        return f'potion({self.args})'

    def __repr__(self):
        return self.__str__()

    def is_simple(self):
        return self.simple

    def in_text(self):
        return None

    @staticmethod
    def is_independent():
        return False

    def simplify(self, mode=None, work_with=None):
        ret = built_in_simplify(self, mode, work_with)
        if ret[1] is self:
            self.new_args["potion"].value = self.new_args["potion"].value.lower().replace("minecraft:", "")
            if self.new_args["potion"].value not in potions:
                error_from_object(self.new_args["potion"], "ArgumentError",
                                  translate("error.unexistspotion", {0: self.new_args["potion"].value}))
        return ret

    def json(self):
        return {"type": "potion", "potion": self.new_args["potion"].value,
                "amplifier": self.new_args["amplifier"].value, "duration": self.new_args["duration"].value}

    def copy(self):
        return self

    def remove_inlines(self):
        self.args = self.args.remove_inlines()
        return self

    def get_type(self):
        return self.type

    def get_real_type(self):
        return self.get_type()

    def can_cast_as(self, typ):
        return try_cast_as_class(self.get_real_type(), typ)

    def cast_as(self, typ, arges):
        return self


# noinspection PyUnresolvedReferences
class sound:  # is_jmcc_object
    type = "sound"
    arges = {"sound": {"id": "sound", "type": "text", "pos": 0},
             "volume": {"id": "volume", "type": "number", "default_value": number(0, -1, -1, None), "pos": 1},
             "pitch": {"id": "pitch", "type": "number", "default_value": number(0, -1, -1, None), "pos": 2},
             "variation": {"id": "variation", "type": "text", "default_value": text("", Texts.LEGACY, -1, -1, None),
                           "pos": 3},
             "source": {"id": "source", "type": "enum", "default_value": text("MASTER", Texts.LEGACY, -1, -1, None),
                        "values": ["AMBIENT", "BLOCK", "HOSTILE", "MASTER", "MUSIC", "NEUTRAL", "PLAYER", "RECORD",
                                   "VOICE", "WEATHER"],
                        "pos": 4}}
    template = {"sound": 0, "volume": 0, "pitch": 0, "variation": 0, "source": 0}

    __slots__ = ("args", "new_args", "simple", "starting_pos", "ending_pos", "source")

    def __init__(self, args: calling_args, starting_pos: int, ending_pos: int, source: str):
        self.args = args
        self.new_args = {}
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        self.simple = False

    def __str__(self):
        return f'sound({self.args})'

    def __repr__(self):
        return self.__str__()

    def is_simple(self):
        return self.simple

    @staticmethod
    def is_independent():
        return False

    def in_text(self):
        return None

    def simplify(self, mode=None, work_with=None):
        return built_in_simplify(self, mode, work_with)

    def json(self):
        return {"type": "sound", "sound": self.new_args["sound"].value,
                "volume": self.new_args["volume"].value,
                "pitch": self.new_args["pitch"].value, "variation": self.new_args["variation"].value,
                "source": self.new_args["source"].value}

    def copy(self):
        return self

    def remove_inlines(self):
        self.args = self.args.remove_inlines()
        return self

    def get_type(self):
        return self.type

    def get_real_type(self):
        return self.get_type()

    def can_cast_as(self, typ):
        return try_cast_as_class(self.get_real_type(), typ)

    def cast_as(self, typ, arges):
        return self


# noinspection PyUnresolvedReferences
class particle:  # is_jmcc_object
    type = "particle"
    arges = {"particle": {"id": "particle", "type": "text", "pos": 0},
             "count": {"id": "count", "type": "number", "default_value": number(1, -1, -1, None), "pos": 1},
             "spread_x": {"id": "spread_x", "type": "number", "default_value": number(0, -1, -1, None), "pos": 2},
             "spread_y": {"id": "spread_y", "type": "number", "default_value": number(0, -1, -1, None), "pos": 3},
             "motion_x": {"id": "motion_x", "type": "number", "default_value": number(0, -1, -1, None), "pos": 4},
             "motion_y": {"id": "motion_y", "type": "number", "default_value": number(0, -1, -1, None), "pos": 5},
             "motion_z": {"id": "motion_z", "type": "number", "default_value": number(0, -1, -1, None), "pos": 6},
             "material": {"id": "material", "type": "text", "default_value": text("", Texts.LEGACY, -1, -1, None),
                          "pos": 7},
             "color": {"id": "color", "type": ("number", "text"), "default_value": number(16777215, -1, -1, None),
                       "pos": 8},
             "size": {"id": "size", "type": "number", "default_value": number(0, -1, -1, None), "pos": 9},
             "to_color": {"id": "to_color", "type": ("number", "text"), "default_value": number(0, -1, -1, None),
                          "pos": 9}}
    template = {"particle": 0, "count": 0, "spread_x": 0, "spread_y": 0, "motion_x": 0, "motion_y": 0, "motion_z": 0,
                "material": 0, "color": 0, "size": 0, "to_color": 0}
    __slots__ = ("args", "new_args", "starting_pos", "ending_pos", "source", "simple")

    def __init__(self, args: calling_args, starting_pos: int, ending_pos: int, source: str):
        self.args = args
        self.new_args = {}
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        self.simple = False

    def __str__(self):
        return f'particle({self.args})'

    def __repr__(self):
        return self.__str__()

    def is_simple(self):
        return self.simple

    def in_text(self):
        return None

    @staticmethod
    def is_independent():
        return False

    def simplify(self, mode=None, work_with=None):
        ret = built_in_simplify(self, mode, work_with)
        if ret[1] is self:
            self.new_args["particle"].value = self.new_args["particle"].value.lower().replace("minecraft:", "")
            if self.new_args["particle"].value not in particles:
                error_from_object(self.new_args["particle"], "ArgumentError",
                                  translate("error.unexistsparticle", {0: self.new_args["particle"].value}))
            if self.new_args["color"].get_type() == "text":
                if len(self.new_args["color"].value) == 7 and self.new_args["color"].value[0] == "#" and \
                        self.new_args["color"].value[1] in allowed_symbols and self.new_args["color"].value[
                    2] in allowed_symbols and self.new_args["color"].value[3] in allowed_symbols and \
                        self.new_args["color"].value[4] in allowed_symbols and self.new_args["color"].value[
                    5] in allowed_symbols and self.new_args["color"].value[6] in allowed_symbols:
                    self.new_args["color"].value = int(self.new_args["color"].value[1:], 16)
                else:
                    error_from_object(self.new_args["color"], "ArgumentError",
                                      "неверный формат цвета '{0}', ожидался: '#FFFFFF'")
            if self.new_args["to_color"].get_type() == "text":
                if len(self.new_args["to_color"].value) == 7 and self.new_args["to_color"].value[0] == "#" and \
                        self.new_args["to_color"].value[1] in allowed_symbols and self.new_args["to_color"].value[
                    2] in allowed_symbols and self.new_args["to_color"].value[3] in allowed_symbols and \
                        self.new_args["to_color"].value[4] in allowed_symbols and self.new_args["to_color"].value[
                    5] in allowed_symbols and self.new_args["to_color"].value[6] in allowed_symbols:
                    self.new_args["to_color"].value = int(self.new_args["to_color"].value[1:], 16)
                else:
                    error_from_object(self.new_args["to_color"], "ArgumentError",
                                      "неверный формат цвета '{0}', ожидался: '#FFFFFF'")
        return ret

    def json(self):
        return {"type": "particle", "particle_type": self.new_args["particle"].value,
                "count": self.new_args["count"].value, "first_spread": self.new_args["spread_x"].value,
                "second_spread": self.new_args["spread_y"].value, "x_motion": self.new_args["motion_x"].value,
                "y_motion": self.new_args["motion_y"].value, "z_motion": self.new_args["motion_z"].value,
                "color": self.new_args["color"].value, "material": self.new_args["material"].value,
                "size": self.new_args["size"].value, "to_color": self.new_args["to_color"].value}

    def copy(self):
        return self

    def remove_inlines(self):
        self.args = self.args.remove_inlines()
        return self

    def get_type(self):
        return self.type

    def get_real_type(self):
        return self.get_type()

    def can_cast_as(self, typ):
        return try_cast_as_class(self.get_real_type(), typ)

    def cast_as(self, typ, arges):
        return self


class if_else_expr:
    type = "if_else_expr"
    __slots__ = ("conditional", "true", "false", "value_type", "starting_pos", "ending_pos", "source")

    def __init__(self, cond: default_jmcc_object, true: default_jmcc_object, false: default_jmcc_object,
                 starting_pos: int, ending_pos: int, source: str):
        self.conditional = cond
        self.true = true
        self.false = false
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        self.value_type = self.true.get_real_type() if self.true.get_real_type() == self.false.get_real_type() else "any"

    def __str__(self):
        return f'if_else({self.true}, {self.conditional},{self.false})'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def is_simple():
        return False

    @staticmethod
    def is_independent():
        return False

    def in_text(self):
        return None

    def simplify(self, mode=None, work_with=None):
        if mode == 1:
            exit()
        if not isinstance(work_with, var):
            work_with = var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)
        Context(Context.sources[-1]).next_lvl()
        Context(Context.sources[-1]).add_operation(
            assign([work_with], None, self.true, self.starting_pos, self.ending_pos,
                   self.source))
        Context(Context.sources[-1]).update()
        true = Context(Context.sources[-1]).get_operations()
        Context(Context.sources[-1]).previous_lvl()
        Context(Context.sources[-1]).next_lvl()
        Context(Context.sources[-1]).add_operation(
            assign([work_with], None, self.false, self.starting_pos, self.ending_pos,
                   self.source))
        Context(Context.sources[-1]).update()
        false = Context(Context.sources[-1]).get_operations()
        Context(Context.sources[-1]).previous_lvl()
        prev_ops, cur_op, next_ops = if_(self.conditional, true, [], false, self.starting_pos, self.ending_pos,
                                         self.source).simplify()
        return prev_ops, work_with, next_ops

    def get_type(self):
        return self.type

    def get_real_type(self):
        return self.value_type

    def can_cast_as(self, typ):
        return try_cast_as_class(self.get_real_type(), typ)

    def cast_as(self, typ, arges):
        return self


class class_object:
    type = "class_object"
    __slots__ = ("value_type", "object", "default_values", "simple", "starting_pos", "ending_pos", "source")

    def __init__(self, class_type, object, default_values, starting_pos, ending_pos, source):
        self.value_type = class_type
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        self.object = object
        self.default_values = default_values
        if isinstance(self.object, dct):
            for obj in self.default_values:
                if self.default_values[obj] is not None:
                    self.object.keys.append(text(obj, Texts.LEGACY, self.default_values[obj].starting_pos,
                                                 self.default_values[obj].ending_pos, self.default_values[obj].source))
                    self.object.values.append(self.default_values[obj])
        if isinstance(self.object, lst):
            for obj in self.default_values:
                if self.default_values[obj] is not None:
                    self.object.values.append(self.default_values[obj])
                else:
                    self.object.values.append(number(0, self.starting_pos, self.ending_pos, self.source))
        self.simple = False

    def is_simple(self):
        return self.simple

    @staticmethod
    def is_independent():
        return False

    def in_text(self):
        return None

    def simplify(self, mode=None, work_with=None):
        if not self.object.is_simple():
            return self.object.simplify(mode=mode, work_with=work_with)
        else:
            if not isinstance(work_with, var):
                work_with = var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)
            return assign([work_with], None, self.object, self.starting_pos, self.ending_pos, self.source).simplify()

    def copy(self):
        return self

    def can_cast_as(self, typ):
        return try_cast_as_class(self.get_real_type(), typ)

    def cast_as(self, typ, arges):
        return self

    def remove_inlines(self):
        return self

    def get_type(self):
        return self.type

    def get_real_type(self):
        return self.value_type


class class_:
    type = None
    __slots__ = ("parent", "operations", "functions", "specials", "inline", "name", "source", "class_obj")

    def __init__(self, name: str, parent: str, operations: list, functions: list, specials: dict, source: str,
                 class_obj: class_object, inline=False):
        self.source = source
        self.parent = parent
        self.operations = operations
        self.functions = functions
        self.specials = specials
        self.inline = inline
        self.name = name
        self.class_obj = class_obj
        if self.class_obj is None and self.parent is not None:
            self.class_obj = Context(Context.sources[-1]).get_special(self.parent).class_obj
        if self.class_obj.object.get_type() == "map":
            if len(self.class_obj.default_values) == 0:
                if "__set_attribute__" not in self.specials:
                    jmcc_var1, jmcc_var2, jmcc_var3 = new("var"), new("var"), new("var")
                    self.specials["__set_attribute__"] = function("__set_attribute__", tokenize(
                        "{" + f"`jmcc.{jmcc_var1}`:any;`jmcc.{jmcc_var1}`=`jmcc.{jmcc_var1}`.set_map_value(`jmcc.{jmcc_var2}`,`jmcc.{jmcc_var3}`);`jmcc.{jmcc_var1}`: {self.name}" + "}",
                        self.source, allow_jmcc=True), calling_args([var(f"jmcc.{jmcc_var1}", Vars.LOCAL,
                                                                         self.class_obj.starting_pos,
                                                                         self.class_obj.ending_pos,
                                                                         self.class_obj.source, value_type="any"),
                                                                     var(f"jmcc.{jmcc_var2}", Vars.LOCAL,
                                                                         self.class_obj.starting_pos,
                                                                         self.class_obj.ending_pos,
                                                                         self.class_obj.source, value_type="text"),
                                                                     var(f"jmcc.{jmcc_var3}", Vars.LOCAL,
                                                                         self.class_obj.starting_pos,
                                                                         self.class_obj.ending_pos,
                                                                         self.class_obj.source, value_type="any")], {},
                                                                    self.class_obj.starting_pos,
                                                                    self.class_obj.ending_pos, self.class_obj.source),
                                                                  self.class_obj.source, True, ready=False).special()
                if "__get_attribute__" not in self.specials:
                    jmcc_var1, jmcc_var2 = new("var"), new("var")
                    self.specials["__get_attribute__"] = function("__get_attribute__", tokenize(
                        "{" + f"`jmcc.{jmcc_var1}`:any;return `jmcc.{jmcc_var1}`.get_map_value(`jmcc.{jmcc_var2}`)" + "}",
                        self.source, allow_jmcc=True), calling_args([var(f"jmcc.{jmcc_var1}", Vars.LOCAL,
                                                                         self.class_obj.starting_pos,
                                                                         self.class_obj.ending_pos,
                                                                         self.class_obj.source, value_type="any"),
                                                                     var(f"jmcc.{jmcc_var2}", Vars.LOCAL,
                                                                         self.class_obj.starting_pos,
                                                                         self.class_obj.ending_pos,
                                                                         self.class_obj.source, value_type="text")], {},
                                                                    self.class_obj.starting_pos,
                                                                    self.class_obj.ending_pos, self.class_obj.source),
                                                                  self.class_obj.source, True, ready=False).special()
            else:
                for obj in self.class_obj.default_values:
                    obj_typ = self.class_obj.default_values[obj].get_real_type() if self.class_obj.default_values[
                                                                                        obj] is not None else "any"
                    if f"{obj}.setter" not in self.specials:
                        jmcc_var1, jmcc_var2 = new("var"), new("var")
                        self.specials[f"{obj}.setter"] = function(f"{obj}.setter", tokenize(
                            "{" + f"`jmcc.{jmcc_var1}`:any;`jmcc.{jmcc_var1}`=`jmcc.{jmcc_var1}`.set_map_value('{obj}',`jmcc.{jmcc_var2}`);`jmcc.{jmcc_var1}`: {self.name}" + "}",
                            self.source, allow_jmcc=True), calling_args([var(f"jmcc.{jmcc_var1}", Vars.LOCAL,
                                                                             self.class_obj.starting_pos,
                                                                             self.class_obj.ending_pos,
                                                                             self.class_obj.source, value_type="any"),
                                                                         var(f"jmcc.{jmcc_var2}", Vars.LOCAL,
                                                                             self.class_obj.starting_pos,
                                                                             self.class_obj.ending_pos,
                                                                             self.class_obj.source,
                                                                             value_type=obj_typ)],
                                                                        {}, self.class_obj.starting_pos,
                                                                        self.class_obj.ending_pos,
                                                                        self.class_obj.source), self.class_obj.source,
                                                                  True, ready=False).special()
                    if f"{obj}.getter" not in self.specials:
                        jmcc_var1 = new("var")
                        return_var = var(f"jmcc.{new('var')}", Vars.LOCAL if not inline else Vars.INLINE,
                                         self.class_obj.starting_pos, self.class_obj.ending_pos,
                                         self.class_obj.source, value_type=obj_typ)
                        self.specials[f"{obj}.getter"] = function(f"{obj}.getter", tokenize(
                            "{" + f"`jmcc.{jmcc_var1}`:any;return `jmcc.{jmcc_var1}`.get_map_value('{obj}')" + "}",
                            self.source, allow_jmcc=True), calling_args([var(f"jmcc.{jmcc_var1}", Vars.LOCAL,
                                                                             self.class_obj.starting_pos,
                                                                             self.class_obj.ending_pos,
                                                                             self.class_obj.source, value_type="any")],
                                                                        {}, self.class_obj.starting_pos,
                                                                        self.class_obj.ending_pos,
                                                                        self.class_obj.source), self.class_obj.source,
                                                                  True, ready=False, return_var=return_var).special()
        elif self.class_obj.object.get_type() == "array":
            default_values = list(self.class_obj.default_values.keys())
            for obj in default_values:
                obj_typ = self.class_obj.default_values[obj].get_real_type() if self.class_obj.default_values[
                                                                                    obj] is not None else "any"
                if f"{obj}.setter" not in self.specials:
                    jmcc_var1, jmcc_var2 = new("var"), new("var")
                    self.specials[f"{obj}.setter"] = function(f"{obj}.setter", tokenize(
                        "{" + f"`jmcc.{jmcc_var1}`:any;`jmcc.{jmcc_var1}`=`jmcc.{jmcc_var1}`.set_list_value({default_values.index(obj)},`jmcc.{jmcc_var2}`);`jmcc.{jmcc_var1}`: {self.name}" + "}",
                        self.source, allow_jmcc=True), calling_args([var(f"jmcc.{jmcc_var1}", Vars.LOCAL,
                                                                         self.class_obj.starting_pos,
                                                                         self.class_obj.ending_pos,
                                                                         self.class_obj.source, value_type="any"),
                                                                     var(f"jmcc.{jmcc_var2}", Vars.LOCAL,
                                                                         self.class_obj.starting_pos,
                                                                         self.class_obj.ending_pos,
                                                                         self.class_obj.source, value_type=obj_typ)],
                                                                    {}, self.class_obj.starting_pos,
                                                                    self.class_obj.ending_pos,
                                                                    self.class_obj.source), self.class_obj.source,
                                                              True, ready=False).special()
                if f"{obj}.getter" not in self.specials:
                    jmcc_var1 = new("var")
                    return_var = var(f"jmcc.{new('var')}", Vars.LOCAL if not inline else Vars.INLINE,
                                     self.class_obj.starting_pos, self.class_obj.ending_pos,
                                     self.class_obj.source, value_type=obj_typ)
                    self.specials[f"{obj}.getter"] = function(f"{obj}.getter", tokenize(
                        "{" + f"`jmcc.{jmcc_var1}`:any;return `jmcc.{jmcc_var1}`.get_list_value({default_values.index(obj)})" + "}",
                        self.source, allow_jmcc=True), calling_args([var(f"jmcc.{jmcc_var1}", Vars.LOCAL,
                                                                         self.class_obj.starting_pos,
                                                                         self.class_obj.ending_pos,
                                                                         self.class_obj.source, value_type="any")],
                                                                    {}, self.class_obj.starting_pos,
                                                                    self.class_obj.ending_pos,
                                                                    self.class_obj.source), self.class_obj.source,
                                                              True, ready=False, return_var=return_var).special()


    def __str__(self):
        return f'class({self.name})'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def is_simple():
        return False

    @staticmethod
    def is_independent():
        return True

    def simplify(self, mode=None, work_with=None):
        return self.functions, None, []

    def copy(self):
        return self

    def special(self):
        if self.parent is not None:
            all_funcs_before = Context(Context.sources[-1]).get_special(self.parent).functions
            all_parents_before = Context(Context.sources[-1]).get_special(self.parent).parents
            if len(all_parents_before) > 0 and all_parents_before[0] != self.parent:
                all_parents_before.insert(0, self.parent)
            else:
                all_parents_before.append(self.parent)
        else:
            all_funcs_before = {}
            all_parents_before = []
            if self.class_obj.get_real_type() != self.name:
                all_parents_before.append(self.class_obj.get_real_type())
        all_funcs_before.update(self.specials)
        return special_class(self.name, all_funcs_before, self.class_obj, parents=all_parents_before)


def parse(tokens, source):
    return Parser(tokens, source).parse()


def parse_from_text(txt, source=None, properties=None):
    if properties is None:
        properties = {}
    global global_text
    if source is None:
        source = new("source")
    if len(properties) > 0:
        Context(source).set_properties(properties)
    if (source not in Context.context) or (Context(source).compiled is False):
        global_text[source] = txt
        return parse(tokenize(txt, source), source)
    else:
        Context(source).clear_operations()
        return Context(source)


def parse_from_file(file1, properties=None):
    if properties is None:
        properties = {}
    global global_text
    source = os.path.abspath(file1.name)
    if len(properties) > 0:
        Context(source).set_properties(properties)
    if (source not in Context.context) or (Context(source).compiled is False):
        path = os.path.dirname(source)
        global_text[source] = file1.read()
        earlier = os.getcwd()
        os.chdir(path)
        ret = parse(tokenize(global_text[source], source), source)
        os.chdir(earlier)
        return ret
    else:
        Context(source).clear_operations()
        return Context(source)


def parse_from_directory(directory_path, properties=None):
    if properties is None:
        properties = {}
    global global_text
    source = os.path.abspath(directory_path)
    if len(properties) > 0:
        Context(source).set_properties(properties)
    if (source not in Context.context) or (Context(source).compiled is False):
        files = get_all_jc_files(directory_path)
        code_text = ";".join(["import \"" + path.replace("\\", "\\\\").replace("\"", "\\\"") + "\"" for path in files])
        path = os.path.dirname(source)
        global_text[source] = code_text
        earlier = os.getcwd()
        os.chdir(path)
        ret = parse(tokenize(global_text[source], source), source)
        os.chdir(earlier)
        return ret
    else:
        Context(source).clear_operations()
        return Context(source)


def try_upload(code):
    try:
        print(minecraft_based_text(translate("compilator.code_uploading_message")))
        start_time1 = time()
        response = requests.post('https://m.justmc.ru/api/upload', json=code)
        response = response.json()
        end_time1 = time()
        print(minecraft_based_text(translate("compilator.code_uploading_time", {0: round(end_time1 - start_time1, 3)})))
        print(minecraft_based_text(translate("compilator.code_uploaded_message", {0: response['id']})))
    except Exception as e:
        print(minecraft_based_text("&c" + translate("compilator.uploading_error_message")))
        print(error("UploadingError", translate(f"error.uploadingerror.{e.__class__.__name__}",
                                                {i: e.args[i] for i in range(len(e.args))})))


end_time = time()
print(minecraft_based_text(translate("compilator.prepare_data_time", {0: round(end_time - start_time, 3)})))


def get_all_jc_files(directory):
    files = []
    all_files = os.listdir(directory)
    for file1 in all_files:
        file2 = f"{directory}\\{file1}"
        if os.path.isfile(file2):
            if file2.endswith(".jc"):
                files.append(file2)
            elif file2.endswith(".json") and file1[:file1.rfind(".json")] not in all_files:
                files.append(file2)
        elif os.path.isdir(file2):
            files.extend(get_all_jc_files(file2))
    return files


def compile_file(file_path, upload=False, properties=None):
    start_time = time()
    if properties is None:
        properties = {}
    if not os.path.exists(file_path):
        error_from_object(default_jmcc_object, "UnexistsFile", translate("error.unexistsfile", {0: file_path}))
    mode = None
    source = None
    pr_source = None
    file = None
    context = None
    if os.path.isfile(file_path):
        if file_path.endswith(".jc"):
            file = open(file_path, encoding="UTF-8")
            source = os.path.abspath(file.name)
            pr_source = source.replace(".jc", ".properties", 1)
            mode = 0
        elif file_path.endswith(".json") and False:
            file = open(file_path, encoding="UTF-8")
            source = os.path.abspath(file.name)
            mode = 2
        else:
            error_from_object(default_jmcc_object, "UnknownFileFormat",
                              translate("error.unknownfileformat", {0: file_path}))
    elif os.path.isdir(file_path):
        source = file_path
        pr_source = source + ".properties"
        mode = 1
    else:
        error_from_object(default_jmcc_object, "UnknownFile", translate("error.unknownfile", {0: file_path}))
    if pr_source is not None and os.path.exists(pr_source):
        properties.update(Properties(text=open(pr_source, "r", encoding="UTF-8").read()).properties)
    if mode == 0:
        context = parse_from_file(file, properties)
    elif mode == 1:
        context = parse_from_directory(file_path, properties)
    elif mode == 2:
        context = parse_from_json(file, properties)
    code = context.get_json()
    end_time = time()
    print(minecraft_based_text(translate("compilator.code_compilation_time", {0: round(end_time - start_time, 3)})))
    if not upload or properties.setdefault("save", False):
        if "output" in properties:
            output = properties["output"]
            if os.path.isdir(output):
                output += "/" + os.path.basename(source) + ".json"
            elif not output.endswith(".json"):
                output += ".json"
        else:
            output = source + ".json"
        if properties.setdefault("compact", False):
            open(output, "w").write(json.dumps(code, separators=(',', ':')))
        else:
            open(output, "w").write(json.dumps(code, indent=2))
    if upload:
        try_upload(code)
