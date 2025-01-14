import json
import os
import copy

import requests

import nbtworker
from jmcc import translate, minecraft_based_text, color_codes, allowed_symbols, Properties
from time import time
start_time = time()
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
    LINE_VARIABLE: int = 27
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
    LINE_DEFINE: int = 55
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


class Token:

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

    def __init__(self, txt, source):
        self.current_pos = -1
        self.current_char = ""
        self.source = source
        self.text = txt
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
            if token_type is not None:
                return Token(token_type, token_value, starting_pos, self.current_pos - 1, self.source)
            sign_mode = True

        if self.current_char == "\"" or self.current_char == "\'" or self.current_char == "`" or self.current_char == "<":
            mode = self.current_char
            if sign_mode:
                if mode == "`" and token_value in {"l", "local", "g", "game", "s", "save", "i", "inline", "line"}:
                    token_type = Tokens.LOCAL_VARIABLE if token_value in {"l", "local"} else (
                        Tokens.INLINE_VARIABLE if token_value in {"i", "inline"} else (
                            Tokens.LINE_VARIABLE if token_value == "line" else (
                                Tokens.GAME_VARIABLE if token_value in {"g", "game"} else Tokens.SAVE_VARIABLE)))
                elif mode in {'"', "'"} and token_value in {"p", "plain", "l", "legacy", "m", "minimessage", "j",
                                                            "json"}:
                    token_type = Tokens.PLAIN_STRING if token_value in {"p", "plain"} else (
                        Tokens.MINIMESSAGE_STRING if token_value in {"m", "minimessage"} else (
                            Tokens.LEGACY_STRING if token_value in {"l", "legacy"} else Tokens.JSON_STRING))
                else:
                    return Token(Tokens.VARIABLE, token_value, starting_pos, self.current_pos - 1, self.source)
            else:
                if mode == "`":
                    token_type = Tokens.VARIABLE
                elif mode == "<":
                    mode = ">"
                    token_type = Tokens.SUBSTRING
                else:
                    token_type = Tokens.STRING
            self.advance()
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
                    token_value+="\\n"
                elif self.current_char == "$":
                    if len(token_value) > 0:
                        giga_token.append(
                            Token(Tokens.STRING, token_value, starting_pos, self.current_pos - 1, self.source))
                    token_value = ""
                    new_starting_pos = self.current_pos
                    self.advance()
                    var_value = ""
                    if self.current_char == "{":
                        self.advance()
                        thing = []
                        counter = 0
                        while self.current_char != "" and (
                                self.current_char != "}" or counter > 0) and self.current_char != mode:
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
                        giga_token.append([
                            Token(Tokens.VARIABLE, var_value, new_starting_pos, self.current_pos - 1, self.source),
                            Token(Tokens.NONE, "}", self.current_pos, self.current_pos, self.source)])
                    continue
                else:
                    token_value += self.current_char
                self.advance()
            if self.current_char == mode:
                self.advance()
                if len(giga_token) == 0:
                    if token_value.startswith("jmcc.") and mode not in {"\"", "\'"}:
                        error("NameError", translate("error.nameerror.cant_use_jmcc"), starting_pos,
                              self.current_pos - 1, self.source)
                    return Token(token_type, token_value, starting_pos,
                                 self.current_pos - 1, self.source)
                else:
                    if len(token_value) > 0:
                        giga_token.append(
                            Token(Tokens.STRING, token_value, starting_pos, self.current_pos - 1, self.source))
                    release_index = global_text[self.source].index(mode if mode != ">" else "<", starting_pos,
                                                                   self.current_pos - 1) + 1
                    release = global_text[self.source][release_index:self.current_pos - 1]
                    if release.startswith("jmcc.") and mode not in {"\"", "\'"}:
                        error("NameError", translate("error.nameerror.cant_use_jmcc"), starting_pos,
                              self.current_pos - 1, self.source)
                    return Token(token_type, release, starting_pos, self.current_pos - 1, self.source, giga=giga_token)
            elif mode == ">" and token_value == "":
                self.advance()
                return Token(Tokens.LESS, "<", starting_pos, self.current_pos - 1, self.source)
            elif mode == ">" and token_value == "=":
                self.advance()
                return Token(Tokens.LESS_OR_EQUALS, "<=", starting_pos, self.current_pos - 1, self.source)
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
                        self.advance()
                        return self.next_token
                    self.advance()
                return Token(Tokens.EOF, "None", starting_pos, starting_pos, self.source)
            elif self.current_char == "*":
                while self.current_char is not None:
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
            if self.text[self.current_pos+1] in {"\n","\t"}:
                self.advance()
                self.advance()
                return self.next_token
        if self.current_char == "\n" or self.current_char == "\t":
            self.advance()
            return Token(Tokens.NEXT_LINE, "\n", starting_pos, starting_pos, self.source)
        if self.current_char == "":
            return Token(Tokens.EOF, "None", starting_pos, starting_pos, self.source)
        else:
            error("SyntaxError",translate("error.syntaxerror.unexpected_symbol", {0: self.current_char}),starting_pos,starting_pos,source=self.source)

    def get_remaining_tokens(self) -> list:
        lest = []
        while (token := self.next_token).type != Tokens.EOF:
            lest.append(token)
        return lest


def tokenize(txt, source=None):
    if source is None:
        source = new("source")
    global_text[source] = txt
    return Lexer(txt, source).get_remaining_tokens()


def tokenize_from_file(file1):
    global global_text
    source = os.path.abspath(file1.name)
    global_text[source] = file1.read()
    return tokenize(global_text[source], source)


class Parser:
    Expr_priorities = [Tokens.AND, Tokens.OR, Tokens.LESS, Tokens.GREATER, Tokens.EQUALS, Tokens.LESS_OR_EQUALS,
                       Tokens.GREATER_OR_EQUALS, Tokens.PLUS, Tokens.MINUS, Tokens.MINUS_NUMBER, Tokens.PLUS_NUMBER,
                       Tokens.MULTIPLY, Tokens.DIVIDE, Tokens.PR, Tokens.DEG]
    Expr_operations = {Tokens.AND: "__and__", Tokens.OR: "__or__", Tokens.LESS: "__less__",
                       Tokens.GREATER: "__greater__", Tokens.EQUALS: "__equals__",
                       Tokens.LESS_OR_EQUALS: "__less_or_equals__",
                       Tokens.GREATER_OR_EQUALS: "__greater_or_equals__", Tokens.PLUS: "__add__",
                       Tokens.MINUS: "__subtract__",
                       Tokens.MULTIPLY: "__multiply__", Tokens.DIVIDE: "__divide__", Tokens.PR: "__remainder__",
                       Tokens.DEG: "__pow__"}

    def __init__(self, tokens: list, source: str):
        self.tokens = tokens
        self.source = source
        self.index = 0
        self.current_token = self.token(self.index)
        self.context = Context(self.source)

    def token(self, index: int) -> Token:
        if index >= len(self.tokens):
            if len(self.tokens) == 0:
                return Token(Tokens.EOF, None, -1, -1,
                         self.source)
            return Token(Tokens.EOF, None, self.tokens[-1].ending_pos + 2, self.tokens[-1].ending_pos + 2,
                         self.source)
        return self.tokens[index]

    def eat(self, token_type: int) -> None:
        if self.current_token.type == token_type:
            self.index += 1
            self.current_token = self.token(self.index)
            if len(self.context.settings["ignore_next_lines"]) > 0:
                while self.current_token.type == Tokens.NEXT_LINE:
                    self.index += 1
                    self.current_token = self.token(self.index)

        else:
            error_from_object(self.current_token, "SyntaxError", translate("error.syntaxerror.wrong_token", {
                0: translate('token.' + str(token_type) + '.name'),
                1: translate('token.' + str(self.current_token.type) + '.name')}))

    def get_giga_token(self, giga):
        giga_acts = []
        for giga_token in giga:
            self.context.next_lvl()
            if isinstance(giga_token, list):
                for op in giga_token[::-1]:
                    self.tokens.insert(self.index, op)
                self.current_token = self.token(self.index)
                giga_acts.append(self.expr())
                self.eat(Tokens.NONE)
            else:
                self.tokens.insert(self.index, giga_token)
                self.current_token = self.token(self.index)
                giga_acts.append(self.expr())
                self.eat(Tokens.NONE)
            self.context.previous_lvl()
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
                            Tokens.JSON_STRING}:
            if token.type == Tokens.STRING:
                self.eat(Tokens.STRING)
                text_type = Texts.LEGACY
            elif token.type == Tokens.LEGACY_STRING:
                self.eat(Tokens.LEGACY_STRING)
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
            self.eat(Tokens.LPAREN)
            result = self.expr()
            result.starting_pos = token.starting_pos
            result.ending_pos = self.current_token.ending_pos
            self.eat(Tokens.RPAREN)
            return result
        elif token.type == Tokens.LSPAREN:
            self.eat(Tokens.LSPAREN)
            vals = []
            while (self.current_token.type is not None) and self.current_token.type != Tokens.RSPAREN:
                vals.append(self.expr())
                if self.current_token.type != Tokens.RSPAREN:
                    self.eat(Tokens.COMMA)
            ending_pos = self.current_token.ending_pos
            self.eat(Tokens.RSPAREN)
            return lst(vals, token.starting_pos, ending_pos, token.source)
        elif token.type == Tokens.LCPAREN:
            self.eat(Tokens.LCPAREN)
            keys = []
            vals = []
            while (self.current_token.type is not None) and (self.current_token.type != Tokens.RCPAREN):
                keys.append(self.expr())
                self.eat(Tokens.COLON)
                vals.append(self.expr())
                if self.current_token.type != Tokens.RCPAREN:
                    self.eat(Tokens.COMMA)
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
                tru = self.context.get_special(token.value)
                if tru is not None and tru["type"] == "function" and tru["inline"]:
                    self.context.next_lvl()
                    self.context.settings["inline"].append(token.value)
                    if self.context.settings["inline"].count(token.value) > 100:
                        error("RecursionError",
                              translate("error.recursionerror.limit_reached", {0: token.value, 1: 100}),
                              token.starting_pos, ending_pos, token.source)
                    arges = {i1["id"]: i1 for i1 in tru["args"]}
                    args = {}
                    previous_operations = []
                    next_operations = []
                    for k1, v1 in sargs.get_args(list(arges), func=tru["template"]).items():
                        if v1 is None:
                            v1 = arges[k1]["optional"]
                            if v1 is None:
                                error("ArgumentError",
                                      translate("error.argumenterror.argument_is_not_specified", {0: k1}),
                                      token.starting_pos, ending_pos, token.source)
                        args[k1] = v1.remove_inlines()
                        arg_type = args[k1].type
                        self.context.set_inline(k1, args[k1])
                        self.context.set_variable(k1, Vars.INLINE)
                        need_typ = arges[k1]["type"]
                        if need_typ is None:
                            continue
                        if "array" in arges[k1]:
                            if args[k1].type == "array":
                                continue
                            args[k1] = lst([args[k1]], args[k1].starting_pos, args[k1].ending_pos, args[k1].source)
                            self.context.set_inline(k1, args[k1])
                        if args[k1].type in {"variable", "value"}:
                            if args[k1].value_type is None:
                                continue
                            if args[k1].value_type == "any":
                                continue
                            if args[k1].value_type == need_typ:
                                continue
                            arg_type = args[k1].value_type
                        if need_typ == "any":
                            continue
                        if need_typ == "variable" and args[k1].type == "variable":
                            self.context.set_variable_type(args[k1].var_type, args[k1].value, args[k1].value_type)
                            continue
                        if need_typ == args[k1].type:
                            continue
                        error_from_object(args[k1], "ArgumentError",
                                          translate("error.argumenterror.wrong_argument",
                                                    {0: arg_type, 1: need_typ}))
                    return_var = var(f"var.{new('inline')}", Vars.INLINE, token.starting_pos, ending_pos, token.source)
                    self.context.settings["allow_returns"].append(return_var)
                    for op in tru["operations"][::-1]:
                        self.tokens.insert(self.index, op)
                    self.current_token = self.token(self.index)
                    self.context.update()
                    self.context.add_operations(previous_operations)
                    self.eat(Tokens.LCPAREN)
                    while (self.current_token.type != Tokens.EOF) and (self.current_token.type != Tokens.RCPAREN):
                        self.context.add_operation(self.up_statement())
                        self.context.update()
                    self.eat(Tokens.RCPAREN)
                    ops = self.context.get_operations().copy()
                    del self.context.settings["inline"][-1]
                    del self.context.settings["allow_returns"][-1]
                    data = self.context.get_inline(return_var.value)
                    self.context.previous_lvl()
                    self.context.set_inline(return_var.value, data)
                    self.context.add_operations(ops)
                    self.context.add_operations(next_operations)
                    self.context.update()
                    return return_var
                return calling_object(token.value, sargs, token.starting_pos, ending_pos, token.source).change()
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
                return action(token.value, act.value, args, token.starting_pos, ending_pos, self.source, selector=selector)
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
        elif token.type in {Tokens.LOCAL_VARIABLE, Tokens.LINE_VARIABLE, Tokens.INLINE_VARIABLE, Tokens.GAME_VARIABLE,
                            Tokens.SAVE_VARIABLE}:
            if token.type == Tokens.LOCAL_VARIABLE:
                self.eat(Tokens.LOCAL_VARIABLE)
                var_type = Vars.LOCAL
            elif token.type == Tokens.LINE_VARIABLE:
                self.eat(Tokens.LINE_VARIABLE)
                var_type = Vars.LINE
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
                    return calling_function(result, act.value, args, result.starting_pos, ending_pos, self.source)
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
                        error_from_object(arg1, "", translate("error.unknown"))
                    if arg1.type == "variable" and self.current_token.type == Tokens.COLON and save_types:
                        self.eat(Tokens.COLON)
                        arg1.value_type = self.current_token.value
                        self.eat(Tokens.VARIABLE)
                    ending_pos = arg1.ending_pos
                    if now:
                        arg1 = unpacked_args(arg1, arg1.starting_pos, arg1.ending_pos, arg1.source, multi)
                    pos.append(arg1)
            if self.current_token.type != reason_to_stop:
                self.eat(Tokens.COMMA)
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
                result = calling_function(result, operation,
                                          calling_args([result, second], {}, result.starting_pos, second.ending_pos,
                                                       result.source), result.starting_pos, second.ending_pos,
                                          result.source)
            return result
        else:
            return self.up_factor(result)

    def get_vars(self):
        variables = []
        if self.current_token.type == Tokens.SAVE_DEFINE:
            self.eat(Tokens.SAVE_DEFINE)
            self.eat(Tokens.VAR_DEFINE)
            token = self.current_token
            self.eat(Tokens.VARIABLE)
            variable = var(token.value if token.giga is None else self.get_giga_token(token.giga), Vars.SAVE,
                           token.starting_pos, token.ending_pos, self.source)
            self.context.set_variable(variable.value, Vars.SAVE)
        elif self.current_token.type == Tokens.GAME_DEFINE:
            self.eat(Tokens.GAME_DEFINE)
            self.eat(Tokens.VAR_DEFINE)
            token = self.current_token
            self.eat(Tokens.VARIABLE)
            variable = var(token.value if token.giga is None else self.get_giga_token(token.giga), Vars.GAME,
                           token.starting_pos, token.ending_pos, self.source)
            self.context.set_variable(variable.value, Vars.GAME)
        elif self.current_token.type == Tokens.LOCAL_DEFINE:
            self.eat(Tokens.LOCAL_DEFINE)
            self.eat(Tokens.VAR_DEFINE)
            token = self.current_token
            self.eat(Tokens.VARIABLE)
            variable = var(token.value if token.giga is None else self.get_giga_token(token.giga), Vars.LOCAL,
                           token.starting_pos, token.ending_pos, self.source)
            self.context.set_variable(variable.value, Vars.LOCAL)
        elif self.current_token.type == Tokens.VAR_DEFINE:
            self.eat(Tokens.VAR_DEFINE)
            token = self.current_token
            self.eat(Tokens.VARIABLE)
            variable = var(token.value if token.giga is None else self.get_giga_token(token.giga), Vars.LOCAL,
                           token.starting_pos, token.ending_pos, self.source)
            self.context.set_variable(variable.value, Vars.LOCAL)
        elif self.current_token.type == Tokens.LINE_DEFINE:
            self.eat(Tokens.LINE_DEFINE)
            self.eat(Tokens.VAR_DEFINE)
            token = self.current_token
            self.eat(Tokens.VARIABLE)
            variable = var(token.value if token.giga is None else self.get_giga_token(token.giga), Vars.LINE,
                           token.starting_pos, token.ending_pos, self.source)
            self.context.set_variable(variable.value, Vars.LINE)
        elif self.current_token.type == Tokens.INLINE_DEFINE:
            self.eat(Tokens.INLINE_DEFINE)
            self.eat(Tokens.VAR_DEFINE)
            token = self.current_token
            self.eat(Tokens.VARIABLE)
            variable = var(token.value if token.giga is None else self.get_giga_token(token.giga), Vars.INLINE,
                           token.starting_pos, token.ending_pos, self.source)
            self.context.set_variable(variable.value, Vars.INLINE)
        elif self.current_token.type in {Tokens.VARIABLE, Tokens.LOCAL_VARIABLE, Tokens.SAVE_VARIABLE,
                                         Tokens.GAME_VARIABLE, Tokens.LINE_VARIABLE, Tokens.INLINE_VARIABLE} and self.token(self.index+1).type != Tokens.DOUBLE_COLON:
            variable = self.factor()
        else:
            return variables
        if self.current_token.type == Tokens.COLON:
            self.eat(Tokens.COLON)
            variable.value_type = self.current_token.value
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
                if self.current_token.type in {Tokens.VARIABLE, Tokens.LINE_VARIABLE, Tokens.SAVE_VARIABLE,
                                               Tokens.LOCAL_VARIABLE, Tokens.GAME_VARIABLE}:
                    return_var = self.expr()
                    if self.current_token.type != Tokens.RPAREN:
                        self.eat(Tokens.COMMA)
                if self.current_token.type != Tokens.RPAREN:
                    return_var_description = self.current_token.value
                    self.eat(Tokens.STRING)
                self.eat(Tokens.RPAREN)
            else:
                error_from_object(name, "", translate("error.unknown"))
        if ((self.current_token.type == Tokens.FUNCTION_DEFINE and (
                self.context.context_lvl == 0 or len(self.context.settings["class_define"]) > 0))
                or (self.current_token.type == Tokens.INLINE_DEFINE
                    and self.token(self.index + 1).type == Tokens.FUNCTION_DEFINE)):
            if self.current_token.type == Tokens.INLINE_DEFINE:
                self.eat(Tokens.INLINE_DEFINE)
                inline = True
            else:
                inline = False
            self.eat(Tokens.FUNCTION_DEFINE)
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
            allow_return = False
            while (self.current_token.type != Tokens.EOF) and (count != 0):
                token_value.append(self.current_token)
                if self.current_token.type == Tokens.LCPAREN:
                    count += 1
                elif self.current_token.type == Tokens.RCPAREN:
                    count -= 1
                if self.current_token.type == Tokens.RETURN and (self.token(self.index+1).type not in {Tokens.NEXT_LINE, Tokens.SEMICOLON}):
                    allow_return = True
                self.eat(self.current_token.type)
            if allow_return:
                if not inline:
                    if return_var is None:
                        return_var = var(f"jmcc.{new('var')}", Vars.LOCAL, token.starting_pos, token.ending_pos,
                                         token.source)
                else:
                    return_var = None
                if return_var_description is not None and return_var is not None:
                    if arg_description is None:
                        arg_description = {}
                    arg_description[return_var.value] = return_var_description
            result = function(token.value, token_value, args, self.source, inline=inline, return_var=return_var,
                              ready=False, description=description, icon=icon, hide=hide,
                              args_description=arg_description)
            if len(self.context.settings["class_define"]) == 0:
                if self.context.has_special(token.value):
                    error_from_object(token, "NameError",translate("error.nameerror.special_cant_be_rewritten"))
                self.context.set_special(token.value, result.special())
            return result if result.inline is False else None
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
            if len(self.context.settings["class_define"]) == 0:
                if self.context.has_special(token.value):
                    error_from_object(token, "NameError",translate("error.nameerror.special_cant_be_rewritten"))
                self.context.set_special(token.value, result.special())
            return result
        if used_decorators:
            error_from_object(self.current_token, "FunctionError", translate("error.classerror.expected_function", {
                0: translate('token.' + str(self.current_token.type) + '.name')}))
        return 0

    def statement(self):
        if self.current_token.type == Tokens.IMPORT and self.context.context_lvl == 0 and len(
                self.context.settings["class_define"]) == 0:
            self.eat(Tokens.IMPORT)
            thing = self.current_token
            self.eat(Tokens.STRING)
            if os.path.exists(thing.value):
                fil_source = os.path.abspath(thing.value)
                if (fil_source in Context.context) and (not Context(fil_source).compiled):
                    error_from_object(thing, "RecursionError", translate("error.importerror.recursion"))
                self.context.extend(parse_from_file(open(thing.value, "r", encoding="UTF-8")))
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
            if len(self.context.settings["inline"]) > 0:
                self.context.settings["return_counter"] += 1
                if self.context.settings["return_counter"] > 1:
                    error_from_object(obej, "SyntaxError", translate("error.unknown"))
            return obej
        elif self.current_token.type == Tokens.CLASS_DEFINE or (self.current_token.type == Tokens.INLINE_DEFINE
                                                                and self.token(
                    self.index + 1).type == Tokens.CLASS_DEFINE):
            if self.current_token.type == Tokens.INLINE_DEFINE:
                self.eat(Tokens.INLINE_DEFINE)
                inline = True
            else:
                inline = False
            self.eat(Tokens.CLASS_DEFINE)
            token = self.current_token
            self.eat(Tokens.VARIABLE)
            self.context.next_lvl()
            if self.current_token.type == Tokens.LPAREN:
                self.eat(Tokens.LPAREN)
                parent = self.current_token.value
                self.eat(Tokens.VARIABLE)
                self.eat(Tokens.RPAREN)
            else:
                parent = None
            self.context.settings["class_define"].append(token.value)
            if inline:
                self.context.settings["inline"].append(token.value)

            self.eat(Tokens.LCPAREN)
            functions = []
            while (self.current_token.type != Tokens.EOF) and (self.current_token.type != Tokens.RCPAREN):
                if (a := self.up_statement()) is not None:
                    if isinstance(a, (function, process, class_)):
                        functions.append(a)
                    else:
                        self.context.add_operation(a)
                self.context.update()

            self.eat(Tokens.RCPAREN)
            ops = self.context.get_operations()
            if inline:
                del self.context.settings["inline"][-1]
            del self.context.settings["class_define"][-1]
            self.context.previous_lvl()
            return None

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
                        if i3.type == "variable":
                            if i3.value_type is not None:
                                self.context.set_variable_type(i3.var_type, i3.value, i3.value_type)
                    return
                self.context.settings["ignore_next_lines"].append(None)
                obj = self.expr()
                del self.context.settings["ignore_next_lines"][-1]
                return assign(variables, assign_type, obj, variables[0].starting_pos, obj.ending_pos, self.source)

        if len(self.context.settings["class_define"]) > 0:
            error_from_object(self.current_token, "ClassError", translate("error.classerror.expected_function", {
                0: translate('token.' + str(self.current_token.type) + '.name')}))
        self.context.settings["ignore_next_lines"].append(None)
        obj = self.expr()
        del self.context.settings["ignore_next_lines"][-1]
        if obj.type == "action":
            if actions[obj.object][obj.name]["type"].startswith(
                    "container"):
                if self.current_token.type == Tokens.LCPAREN and (
                        not actions[obj.object][obj.name].setdefault("boolean", False)):
                    self.eat(Tokens.LCPAREN)
                    if "lambda" in actions[obj.object][obj.name]:
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
            error_from_object(self.current_token, "SyntaxError", translate("error.syntaxerror.statements_not_separated"))
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
                if isinstance(i1, function):
                    for i2 in self.context.get_special(i1.name)["args"]:
                        self.context.set_variable_type(Vars.LOCAL, i2["id"], i2["type"])
                    self.context.update()
                    self.context.settings["allow_returns"].append(i1.return_var)
                    while (self.current_token.type != Tokens.EOF) and (self.current_token.type != Tokens.RCPAREN):
                        self.context.add_operation(self.up_statement(Tokens.RCPAREN))
                        self.context.update()
                    del self.context.settings["allow_returns"][-1]
                elif isinstance(i1, (process, event)):
                    if isinstance(i1, process):
                        for i2 in self.context.get_special(i1.name)["args"]:
                            self.context.set_variable_type(Vars.LOCAL, i2["id"], i2["type"])
                        self.context.update()
                    while (self.current_token.type != Tokens.EOF) and (self.current_token.type != Tokens.RCPAREN):
                        self.context.add_operation(self.up_statement(Tokens.RCPAREN))
                        self.context.update()
                else:
                    error_from_object(i1, "", translate("error.unknown"))
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
        return self.context


class Context:
    context = {}
    default_context = {"operations": [], "variables": {}, "vars": {0: {}, 1: {}, 2: {}, 3: {}, 4: {}}, "inline_vars": {}, "callable": {}}
    default_cur_context = copy.deepcopy(default_context)
    del default_cur_context["operations"]

    def __init__(self, source):
        self.source = source
        if self.source not in self.context:
            self.context[self.source] = {"context_lvl": 0, 0: copy.deepcopy(self.default_context),
                                         "cur_context": None,
                                         "compiled": False,
                                         "settings": {"allow_returns": [], "inline": [], "return_counter": 0,
                                                      "class_define": [], "ignore_next_lines": []},
                                         "properties": {}}
            self.context[self.source]["cur_context"] = copy.deepcopy(self.default_cur_context)
        self.idx = 0
        self.json_obj = {}

    @property
    def cur_context(self):
        return self.context[self.source]["cur_context"]

    @cur_context.setter
    def cur_context(self, val):
        self.context[self.source]["cur_context"] = val

    @property
    def context_lvl(self):
        return self.context[self.source]["context_lvl"]

    @property
    def compiled(self):
        return self.context[self.source]["compiled"]

    @compiled.setter
    def compiled(self, val):
        self.context[self.source]["compiled"] = val

    @context_lvl.setter
    def context_lvl(self, val):
        self.context[self.source]["context_lvl"] = val

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
                        self.context[self.source][self.context_lvl]["operations"].append(event("world_start", [], self.source))
                    elif self.context[self.source][self.context_lvl]["operations"][0].type != "event":
                        self.context[self.source][self.context_lvl]["operations"].insert(0, event("world_start", [], self.source))
                    elif self.context[self.source][self.context_lvl]["operations"][0].name != "world_start":
                        self.context[self.source][self.context_lvl]["operations"].insert(0, event("world_start", [], self.source))
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

    def get_property(self, prop, default=None):
        if prop in self.context[self.source]["properties"]:
            return self.context[self.source]["properties"][prop]
        return default

    def get_properties(self):
        return self.context[self.source]["properties"]

    def has_variable(self, var_name):
        for cur_context_lvl in range(self.context_lvl+1):
            if var_name in self.context[self.source][cur_context_lvl]["variables"]:
                return True
        return False

    def get_variable(self, var_name):
        for cur_context_lvl in range(self.context_lvl, -1, -1):
            if var_name in self.context[self.source][cur_context_lvl]["variables"]:
                return self.context[self.source][cur_context_lvl]["variables"][var_name]

    def get_variables(self):
        return self.context[self.source][self.context_lvl]["variables"]

    def set_variable_type(self, var_type, var_name, value_type):
        self.cur_context["vars"][var_type][var_name] = value_type

    def get_variable_type(self, var_type, var_name):
        for cur_context_lvl in range(self.context_lvl, -1, -1):
            if var_name in self.context[self.source][cur_context_lvl]["vars"][var_type]:
                return self.context[self.source][cur_context_lvl]["vars"][var_type][var_name]

    def set_inline(self, var_name, var_object):
        self.cur_context["inline_vars"][var_name] = var_object

    def get_inline(self, var_name):
        for cur_context_lvl in range(self.context_lvl, -1, -1):
            if var_name in self.context[self.source][cur_context_lvl]["inline_vars"]:
                return self.context[self.source][cur_context_lvl]["inline_vars"][var_name].copy()

    def has_inline(self, var_name):
        for cur_context_lvl in range(self.context_lvl+1):
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
        for cur_context_lvl in range(self.context_lvl+1):
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
        #{"operations": [], "variables": {}, "vars": {0: {}, 1: {}, 2: {}, 3: {}, 4: {}}, "inline_vars": {}, "callable": {}}
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
        self.context[self.source]["cur_context"]["variables"].update(
            another_context.context[another_context.source][another_context.context_lvl]["variables"])
        self.context[self.source]["cur_context"]["vars"][0].update(
            another_context.context[another_context.source][another_context.context_lvl]["vars"][0])
        self.context[self.source]["cur_context"]["vars"][1].update(
            another_context.context[another_context.source][another_context.context_lvl]["vars"][1])
        self.context[self.source]["cur_context"]["vars"][2].update(
            another_context.context[another_context.source][another_context.context_lvl]["vars"][2])
        self.context[self.source]["cur_context"]["vars"][3].update(
            another_context.context[another_context.source][another_context.context_lvl]["vars"][3])
        self.context[self.source]["cur_context"]["vars"][4].update(
            another_context.context[another_context.source][another_context.context_lvl]["vars"][4])
        self.context[self.source]["cur_context"]["inline_vars"].update(
            another_context.context[another_context.source][another_context.context_lvl]["inline_vars"])
        self.context[self.source]["cur_context"]["callable"].update(
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
    starting_pos = 0
    ending_pos = 0
    source = None
    type = None
    simplify = None
    value = None

    @staticmethod
    def is_simple():
        return True

    @staticmethod
    def is_independent():
        return False

    json = None

    def remove_inlines(self):
        return self

    copy = None

    @staticmethod
    def in_text():
        return None


class number:
    type = "number"

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

    def json(self):
        return {"type": "number", "number": self.value}

    def copy(self):
        return self

    def remove_inlines(self):
        return self


class Texts:
    NONE: int = -1
    LEGACY: int = 0
    PLAIN: int = 1
    MINIMESSAGE: int = 2
    JSON: int = 3
    changer = {-1: "NONE", 0: "LEGACY", 1: "PLAIN", 2: "MINIMESSAGE", 3: "JSON"}


class text:
    type = "text"

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
        return {"type": "text", "text": self.value, "parsing": Texts.changer[self.value_type].lower()}

    def copy(self):
        return self

    def remove_inlines(self):
        return self


class lst:
    type = "array"

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
                prev_ops.extend(previous_operations)
                previous_operations = prev_ops
                next_operations.extend(next_ops)
                new_lst.append(cur_op)
        self.values = new_lst
        self.simple = True
        if mode == 0 or (len_limit is not None and (len(new_lst) > len_limit)):
            if isinstance(work_with, var):
                current_operation = work_with
            else:
                current_operation = var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos,
                                        self.source)
            current_operation.value_type = "array"
            Context(self.source).set_variable_type(current_operation.var_type, current_operation.value,
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
                                                                    "values": lst(self.values, self.starting_pos,
                                                                                  self.ending_pos, self.source)},
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


class dct:
    type = "map"

    def __init__(self, keys, val, starting_pos: int, ending_pos: int, source: str):
        self.keys = list(keys)
        self.old_keys = self.keys.copy()
        self.values = list(val)
        self.old_values = self.values.copy()
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

    def json(self):
        return {"type": "map", "keys": [i3.json() for i3 in self.keys],
                "values": [i3.json() for i3 in self.values]}

    def copy(self):
        return dct([i3.copy() for i3 in self.old_keys], [i3.copy() for i3 in self.old_values], self.starting_pos,
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
                prev_ops.extend(previous_operations)
                previous_operations = prev_ops
                next_operations.extend(next_ops)
                new_keys.append(cur_op)
        self.keys = new_keys
        for val in self.values:
            if val.is_simple():
                new_values.append(val)
            else:
                prev_ops, cur_op, next_ops = val.simplify(mode=0)
                prev_ops.extend(previous_operations)
                previous_operations = prev_ops
                next_operations.extend(next_ops)
                new_values.append(cur_op)
        self.values = new_values
        if mode == 0:
            if isinstance(work_with, var):
                current_operation = work_with
            else:
                current_operation = var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos,
                                        self.source)
            current_operation.value_type = "map"
            Context(self.source).set_variable_type(current_operation.var_type, current_operation.value,
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
            self.values[i1] = self.values[i1].remove_inlines()
        for i1 in range(len(self.keys)):
            self.keys[i1] = self.keys[i1].remove_inlines()
        return self


class NBT:
    type = "snbt"

    def __init__(self, val, starting_pos: int, ending_pos: int, source: str):
        self.value = val
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
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
        else:
            error_from_object(self, "SimplifyError", translate("error.simplifyerror", {0: self}))

    def remove_inlines(self):
        return self

    def copy(self):
        return self


class Vars:
    NONE: int = -1
    LINE: int = 0
    INLINE: int = 1
    LOCAL: int = 2
    GAME: int = 3
    SAVE: int = 4
    changer = {-1: "NONE", 0: "LINE", 1: "INLINE", 2: "LOCAL", 3: "GAME", 4: "SAVE"}


class var:
    type = "variable"

    def __init__(self, val: str, val_type: Vars, starting_pos: int, ending_pos: int, source: str, value_type=None):
        self.value = val
        self.var_type = val_type
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        self.value_type = value_type
        self.simple = (self.var_type not in {0, 1}) and isinstance(self.value, str)

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
        else:
            error_from_object(self, "", translate("error.unknown"))
            var_prefix = ""
        return var_prefix + self.value + ")"

    def simplify(self, mode=None, work_with=None):
        previous_operations = []
        next_operations = []
        if isinstance(self.value, list):
            previous_operations, self.value, next_operations = giga_value(self, self.value)
        if self.var_type == Vars.INLINE:
            if len(previous_operations) + len(next_operations) > 0:
                error_from_object(self, "", translate("error.unknown"))
            val = Context(self.source).get_inline(self.value)
            val.starting_pos = self.starting_pos
            val.ending_pos = self.ending_pos
            val.source = self.source
            if val.is_simple():
                return [], val, []
            return val.simplify(mode=mode, work_with=work_with)
        elif self.var_type == Vars.LINE:
            self.var_type = Vars.LOCAL
            self.value = f"{self.value}_%var_local(var_depth)"
            self.simple = True
        return previous_operations, self, next_operations

    def json(self):
        return {"type": "variable", "variable": self.value, "scope": Vars.changer[self.var_type].lower()}

    def copy(self):
        return self

    def remove_inlines(self):
        if self.var_type == Vars.INLINE:
            val = Context(self.source).get_inline(self.value)
            val.starting_pos = self.starting_pos
            val.ending_pos = self.ending_pos
            val.source = self.source
            return val
        return self


class calling_args:
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
            for k1,v1 in func.items():
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
                args[have_kwargs].keys.append(text(k1,Texts.LEGACY, v1.starting_pos, v1.ending_pos, v1.source))
                args[have_kwargs].values.append(v1)
            else:
                error_from_object(self, "ArgumentError", translate("error.argumenterror.argument_with_wrong_name",
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
                error_from_object(self, "ArgumentError", translate("error.argumenterror.too_many_arguments", {
                    0: ", ".join(map(lambda x: "'" + str(x) + "'", template))}))
        return args

    def set_args(self):
        args = []
        arg_names = set()
        for i1 in self.positional:
            if i1.type == "variable":
                arg = {"id": i1.value, "type": i1.value_type, "optional": None, "unpacked": 0}
            elif i1.type == "unpacked_value" and i1.value.type == "variable":
                arg = {"id": i1.value.value, "type": i1.value.value_type, "optional": None, "unpacked": i1.value_type}
            else:
                error_from_object(self, "ArgumentError",
                                  translate("error.argumenterror.wrong_argument", {0: i1.type, 1: "variable"}))
                exit()
            if arg["id"] in arg_names:
                error_from_object(i1, "", translate("error.unknown"))
            args.append(arg)
            arg_names.add(arg["id"])
        for k1, v1 in self.unpositional.items():
            if not v1.is_simple():
                error_from_object(self, "ArgumentError",
                                  translate("error.jsonerror.object_isnt_simple", {0: v1}))
            arg = {"id": k1, "type": v1.type, "optional": v1, "unpacked": 0}
            if k1 in arg_names:
                error_from_object(v1, "", translate("error.unknown"))
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


def giga_value(self, giga):
    new_text = ""
    previous_operations = []
    next_operations = []
    for op in giga:
        op: default_jmcc_object
        if not op.is_simple():
            prev_ops, op, next_ops = op.simplify(mode=0)
            prev_ops.extend(previous_operations)
            previous_operations = prev_ops
            next_operations.extend(next_ops)
        in_text = op.in_text()
        if in_text is None:
            prev_ops, op, next_ops = assign(
                [var(f'jmcc.{new("var")}', Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)],
                None, op,
                self.starting_pos, self.ending_pos, self.source).simplify(mode=0)
            prev_ops.extend(previous_operations)
            previous_operations = prev_ops
            next_operations.extend(next_ops)
            in_text = op.in_text()
        new_text += in_text
    return previous_operations, new_text, next_operations


def find_value_from_list(val, possible_list=None):
    if possible_list is None:
        possible_list = {}
    check_enum = 0
    for i1 in possible_list:
        if i1.lower().startswith(val.lower()):
            check_enum += 1
            val = i1
        if i1.lower() == val.lower():
            return i1

    if check_enum != 1:
        return -1
    return val


class value:
    type = "value"
    possible_selectors = {"current", "default", "default_entity", "killer_entity", "damager_entity", "victim_entity",
                          "shooter_entity", "projectile", "last_entity"}

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
                    error_from_object(self, "", translate("error.unknown"))
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


class action:
    type = "action"

    def __init__(self, act_obj: str, act_name: str, args: calling_args, starting_pos: int, ending_pos: int,
                 source: object,
                 operations=None, lambd=None, selector=None, inver=None, simple=False, conditional=None):
        self.object = act_obj
        self.name = act_name
        self.args = args
        self.old_args = self.args.copy()
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        self.operations = operations
        self.lambd = lambd
        self.selector = selector
        self.invert = inver
        self.simple = simple
        self.conditional = conditional
        self.return_type = set()

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
        self.args: calling_args
        if mode == 1:
            error_from_object(self, "ActionError", translate("error.actionerror.action_cant_be_setter", {0: self}))
        if self.selector is not None:
            if isinstance(self.selector.value, list):
                previous_operations, self.selector.value, next_operations = giga_value(self, self.selector)
                if len(previous_operations) + len(next_operations) > 0:
                    error_from_object(self, "", translate("error.unknown"))
            if self.object == "player":
                possible_selectors = {"current", "default_player", "killer_player", "damager_player", "shooter_player",
                                      "victim_player", "random_player", "all_players"}
            elif self.object == "entity":
                possible_selectors = {"current", "default_entity", "killer_entity", "shooter_entity", "projectile",
                                      "victim_entity", "random_entity", "all_mobs", "all_entities", "last_entity"}
            else:
                possible_selectors = None
            val1 = find_value_from_list(self.selector.value, possible_selectors)

            if val1 == -1:
                error_from_object(self.selector, "SelectorError", translate("error.argumenterror.unknown_selector",
                                                                            {0: self.selector, 1: ", ".join(
                                                                                map(lambda x: "'" + str(x) + "'",
                                                                                    possible_selectors))}))
            self.selector = val1

        context = Context(self.source)
        if actions[self.object][self.name]["type"].endswith("conditional"):
            thing = self.args.get_args(["conditional"])["conditional"]
            a1, thing, a2 = thing.simplify()
            if not thing.type == "action":
                error_from_object(thing, "ArgumentError", translate("error.argumenterror.wrong_argument",{0:thing.type,1:"action"}))
            if not actions[thing.object][thing.name].setdefault("boolean", False):
                error_from_object(thing, "ArgumentError", translate("error.argumenterror.expected_boolean"))
            if len(a1) + len(a2) > 0:
                error_from_object(thing, "ArgumentError", translate("error.jsonerror.object_isnt_simple"))
            self.conditional = thing
            self.simple = True
            self.args = thing.args
            return [], self, []
        else:
            arges = actions[self.object][self.name]["args"]
            previous_operations = []
            next_operations = []
            inline = False
            if mode == 0:
                if "assign" in actions[self.object][self.name]:
                    if not isinstance(work_with, list):
                        if not isinstance(work_with, var):
                            work_with = var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos,
                                            self.source)
                        work_with = [work_with]
                    for i2 in range(len(actions[self.object][self.name]["assign"])):
                        if i2 < len(work_with):
                            if work_with[i2].type == "variable" and work_with[i2].var_type == Vars.INLINE:
                                inline = True
                                break
                            else:
                                self.args.unpositional[
                                    actions[self.object][self.name]["assign"][i2]["id"]] = \
                                    work_with[i2]
                        else:
                            break

                elif actions[self.object][self.name].setdefault("boolean", False):
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
            load_args = self.args.get_args(list(arges))
            if "assign" in actions[self.object][self.name]:
                if work_with is None or len(work_with) == 0:
                    work_with = []
                for i2 in actions[self.object][self.name]["assign"]:
                    if load_args[i2["id"]] is None:
                        continue
                    if load_args[i2["id"]].type == "variable" and load_args[i2["id"]].var_type == Vars.INLINE:
                        work_with.append(load_args[i2["id"]])
                        del load_args[i2["id"]]
                        inline = True
                if inline:
                    for i2 in set(load_args):
                        if load_args[i2] is None:
                            del load_args[i2]
                self.args = calling_args([], load_args, self.args.starting_pos, self.args.ending_pos, self.args.source)
            if self.object == "variable":
                if self.name == "set_value":
                    if inline:
                        context.set_inline(work_with[0].value, load_args["value"].remove_inlines())
                        return [], None, []
                    if load_args["value"].type in {"array", "map", "subscript", "calling_argument", "calling_function",
                                                   "calling_object", "action", "if_else_expr"}:
                        if len(work_with) < 2:
                            work_with = load_args["variable"]
                        return load_args["value"].simplify(mode=0, work_with=work_with)
                    if load_args["variable"].type in {"subscript", "calling_argument"}:
                        return load_args["variable"].simplify(mode=1, work_with=load_args["value"])
                    if load_args["value"].type == "variable":
                        load_args["variable"].value_type = load_args["value"].value_type if load_args["value"].value_type is not None else context.get_variable_type(load_args["value"].var_type, load_args["value"].value)
                    elif load_args["value"].type == "value":
                        load_args["variable"].value_type = load_args["value"].value_type
            if inline:
                context.set_inline(work_with[0].value, self.remove_inlines())
                return [], None, []
            if self.object == "variable":
                if self.name == "create_list":
                    if load_args["values"].type == "array" and len(load_args["values"].values) > arges["values"][
                        "array"]:
                        return (load_args["values"] if load_args["values"] is not None else
                                lst([], self.starting_pos, self.ending_pos, self.source)).simplify(
                            mode=0, work_with=load_args["variable"], len_limit=arges["values"]["array"])
                if self.name == "create_map_from_values":
                    if (len(load_args["values"].values) > arges["values"]["array"] and len(load_args["keys"].values) >
                            arges["keys"]["array"]):
                        return dct(load_args["keys"].values, load_args["values"].values, self.starting_pos,
                                   self.ending_pos,
                                   self.source).simplify(mode=0, work_with=load_args["variable"])
            args = {}
            if "assign" in actions[self.object][self.name]:
                assigning = {i2["id"]: i2["type"] for i2 in actions[self.object][self.name]["assign"]}
            else:
                assigning = {}
            v1: default_jmcc_object
            for k1, v1 in load_args.items():
                if v1 is None:
                    if "array" in arges[k1]:
                        args[k1] = lst([], self.starting_pos, self.ending_pos, self.source)
                    continue
                v1 = v1.remove_inlines()
                if v1.is_simple():
                    args[k1] = v1
                else:
                    if "array" in arges[k1] and v1.type == "array":
                        prev_ops, args[k1], next_ops = v1.simplify(len_limit=arges[k1]["array"])
                    elif arges[k1]["type"] == "variable" and k1 in assigning:
                        prev_ops, args[k1], next_ops = v1.simplify(mode=1)
                    else:
                        prev_ops, args[k1], next_ops = v1.simplify(mode=0)
                    prev_ops.extend(previous_operations)
                    previous_operations = prev_ops
                    next_operations.extend(next_ops)
                    v1 = args[k1]
                need_typ = arges[k1]["type"]
                if args[k1].type == "variable":
                    if k1 in assigning:
                        if assigning[k1] != "any":
                            args[k1].value_type = assigning[k1]
                            context.set_variable_type(args[k1].var_type, args[k1].value, args[k1].value_type)
                            self.return_type.add(args[k1].value_type)
                    if need_typ == "variable":
                        context.set_variable_type(args[k1].var_type, args[k1].value, args[k1].value_type)
                        continue
                if args[k1].type in {"variable", "value"}:
                    if args[k1].value_type is None:
                        continue
                    if args[k1].value_type == "any":
                        continue
                    if args[k1].value_type == "text":
                        continue
                    if args[k1].value_type == need_typ:
                        continue
                if need_typ == "any":
                    continue
                if need_typ == "text":
                    if args[k1].type == "number":
                        args[k1] = text(args[k1].value, Texts.LEGACY, args[k1].starting_pos, args[k1].ending_pos,
                                        args[k1].source)
                    continue
                if need_typ in ("enum", "boolean"):
                    if args[k1].type == "number":
                        args[k1] = text("FALSE" if args[k1].value == 0 else "TRUE", Texts.PLAIN, args[k1].starting_pos,
                                        args[k1].ending_pos, args[k1].source)
                    if args[k1].type == "text":
                        if args[k1].value == "0":
                            args[k1].value = "FALSE"
                        elif args[k1].value == "1":
                            args[k1].value = "TRUE"
                        possible_enumeration = {i1 for i1 in arges[k1]["values"]} if need_typ == "enum" else {"TRUE",
                                                                                                              "FALSE"}
                        val1 = find_value_from_list(args[k1].value, possible_enumeration)

                        if val1 == -1:
                            error_from_object(args[k1], "ArgumentError", translate("error.argumenterror.unknown_enum",
                                                                                   {0: args[k1].value, 1: ", ".join(
                                                                                       map(lambda x: "'" + str(x) + "'",
                                                                                           possible_enumeration))}))
                        args[k1] = enum_(val1, args[k1].starting_pos, args[k1].ending_pos, args[k1].source)
                        continue
                    if args[k1].type == "variable":
                        if need_typ == "enum":
                            enu = arges[k1]["values"][0]
                        else:
                            enu = "FALSE"
                        args[k1] = enum_(enu, args[k1].starting_pos, args[k1].ending_pos, args[k1].source, args[k1])
                        continue
                if need_typ == "block":
                    if args[k1].type == "block":
                        continue
                    if args[k1].type == "item":
                        block_id = args[k1].item["id"].value
                        if "components" in args[k1].item and "minecraft:block_state" in args[k1].item[
                            "components"] and isinstance(args[k1].item["components"]["minecraft:block_state"],
                                                         nbtworker.Compound):
                            block_id += "[" + ",".join([f"{k1}={v1.value}" for k1, v1 in args[k1].item["components"][
                                "minecraft:block_state"].values.items()]) + "]"
                        args[k1] = block(block_id, args[k1].starting_pos,
                                         args[k1].ending_pos, args[k1].source)
                        continue
                    if args[k1].type == "text":
                        args[k1] = block(args[k1].value, args[k1].starting_pos,
                                         args[k1].ending_pos, args[k1].source)
                        continue
                if args[k1].type == "text":
                    continue
                if need_typ == args[k1].type:
                    continue
                if "array" in arges[k1]:
                    if v1.type == "array":
                        continue
                    args[k1] = lst([args[k1]], args[k1].starting_pos, args[k1].ending_pos, args[k1].source)
                    continue
                error_from_object(args[k1], "ArgumentError",
                                  translate("error.argumenterror.wrong_argument", {0: args[k1].type, 1: need_typ}))
            self.args = args
            self.simple = True
            if mode == 0:
                if isinstance(work_with, list):
                    work_with = work_with[0]
                previous_operations.append(self)
                return previous_operations, work_with, next_operations
        return previous_operations, self, next_operations

    def json(self):
        self.args: dict
        a = {"action": actions[self.object][self.name]["id"],
             "values": [{"name": key1, "value": val1.json()} for key1, val1 in self.args.items()]}
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
        return action(self.object, self.name, self.old_args, self.starting_pos, self.ending_pos, self.source,
                      self.operations, self.lambd, self.selector, self.invert, conditional=self.conditional)

    def remove_inlines(self):
        self.args = self.args.remove_inlines()
        return self


class calling_object:
    type = "calling_object"

    def __init__(self, val: str, args: calling_args, starting_pos: int, ending_pos: int, source: str):
        self.value = val
        self.args = args
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source

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
        context = Context(self.source)
        if context.has_special(self.value):
            pass
        elif self.value == "item":
            return item(self.args, self.starting_pos, self.ending_pos, self.source).simplify(mode=mode,
                                                                                             work_with=work_with)
        elif self.value == "sound":
            return sound(self.args, self.starting_pos, self.ending_pos, self.source).simplify(mode=mode,
                                                                                              work_with=work_with)
        elif self.value == "vector":
            return vector(self.args, self.starting_pos, self.ending_pos, self.source).simplify(mode=mode,
                                                                                               work_with=work_with)
        elif self.value == "location":
            return location(self.args, self.starting_pos, self.ending_pos, self.source).simplify(mode=mode,
                                                                                                 work_with=work_with)
        elif self.value == "particle":
            return particle(self.args, self.starting_pos, self.ending_pos, self.source).simplify(mode=mode,
                                                                                                 work_with=work_with)
        elif self.value == "potion":
            return potion(self.args, self.starting_pos, self.ending_pos, self.source).simplify(mode=mode,
                                                                                               work_with=work_with)
        else:
            error_from_object(self, "ActionError",
                              translate("error.actionerror.unexists_calling_object", {0: self.value}))
        special = context.get_special(self.value)
        previous_operations = []
        next_operations = []
        arges = {i1["id"]: i1 for i1 in special["args"]}
        args = {}
        for k1, v1 in self.args.get_args(list(arges), func=special["template"]).items():
            if v1 is None:
                v1 = arges[k1]["optional"]
                if v1 is None:
                    error_from_object(self, "ArgumentError",
                                      translate("error.argumenterror.argument_is_not_specified", {0: k1}))
            var_thing = var(k1, Vars.LOCAL, self.starting_pos, self.ending_pos, self.source,
                                    value_type=arges[k1]["type"])
            if v1.is_simple():
                args[k1] = v1
            else:
                prev_ops, args[k1], next_ops = v1.simplify(mode=0, work_with = var_thing)
                prev_ops.extend(previous_operations)
                previous_operations = prev_ops
                next_operations.extend(next_ops)
            if not (args[k1].type == "variable" and args[k1].value == k1):
                previous_operations.append(action("variable", "set_value", calling_args([], {
                    "variable": var_thing,
                    "value": args[k1]},
                                                                                        self.starting_pos,
                                                                                        self.ending_pos,
                                                                                        self.source),
                                                  self.starting_pos,
                                                  self.ending_pos, self.source))
            need_typ = arges[k1]["type"]
            if need_typ is None:
                continue
            if "array" in arges[k1]:
                if args[k1].type == "array":
                    continue
                args[k1] = lst([args[k1]], args[k1].starting_pos, args[k1].ending_pos, args[k1].source)
            if args[k1].type == "variable":
                if args[k1].value_type is None:
                    continue
                if args[k1].value_type == "any":
                    continue
                if args[k1].value_type == "text":
                    continue
                if args[k1].value_type == need_typ:
                    continue
            if need_typ == "any":
                continue
            if need_typ == "text":
                continue
            if need_typ == "variable" and args[k1].type == "variable":
                context.set_variable_type(args[k1].var_type, args[k1].value, args[k1].value_type)
                continue
            if need_typ == args[k1].type:
                continue
            error_from_object(args[k1], "ArgumentError",
                              translate("error.argumenterror.wrong_argument", {0: args[k1].type, 1: need_typ}))

        if special["type"] == "function":
            previous_operations.append(action("code", "call_function", calling_args([], {
                "function_name": text(self.value, Texts.LEGACY, self.starting_pos, self.ending_pos, self.source)},
                                                                                    self.starting_pos,
                                                                                    self.ending_pos,
                                                                                    self.source), self.starting_pos,
                                              self.ending_pos, self.source))
            if mode == 0:
                if isinstance(work_with, var):
                    if work_with.value != special["return_var"].value:
                        previous_operations.append(action("variable", "set_value", calling_args([], {
                            "variable": work_with, "value": special["return_var"]}, self.starting_pos, self.ending_pos,
                                                                                                self.source),
                                                          self.starting_pos, self.ending_pos, self.source))
                else:
                    work_with = special["return_var"]
                return previous_operations, work_with, next_operations
        elif special["type"] == "process":
            previous_operations.append(action("code", "start_process", calling_args([], {
                "process_name": text(self.value, Texts.LEGACY, self.starting_pos, self.ending_pos, self.source),
                "target_mode": enum_("CURRENT_TARGET", self.starting_pos, self.ending_pos, self.source),
                "local_variables_mode": enum_("COPY", self.starting_pos, self.ending_pos, self.source)},
                                                                                    self.starting_pos,
                                                                                    self.ending_pos,
                                                                                    self.source), self.starting_pos,
                                              self.ending_pos, self.source))
            if mode == 0:
                error_from_object(self, "ActionError", translate("error.actionerror.action_has_no_value", {0: self}))
        else:
            error_from_object(self, "", translate("error.unknown"))
        return previous_operations, None, next_operations

    def remove_inlines(self):
        self.args = self.args.remove_inlines()
        return self


class calling_argument:
    type = "calling_argument"

    def __init__(self, obj: object, arg: str, starting_pos: int, ending_pos: int, source: str):
        self.object = obj
        self.arg = arg
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        error_from_object(self, "", translate("error.unknown"))

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

    def in_text(self):
        return None

    def remove_inlines(self):
        return self


class calling_function:
    type = "calling_function"

    def __init__(self, obj: default_jmcc_object, val: str, args: calling_args, starting_pos: int, ending_pos: int,
                 source: str):
        self.object = obj
        self.value = val
        self.args = args
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source

    def __str__(self):
        return f'call_function({self.object}, {self.value}, {self.args})'

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
        if mode == 0 or mode is None:
            if not isinstance(work_with, var):
                work_with = var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)
            if self.value in {"__or__", "__and__"}:
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
            if self.value == "__invert__":
                self.object.invert = not self.object.invert
                if self.object.is_simple():
                    return [], self.object, []
                else:
                    return self.object.simplify(mode=mode, work_with=work_with)
            else:
                error_from_object(self, "", translate("error.unknown"))
        if mode == 1:
            error_from_object(self, "ActionError", translate("error.actionerror.action_cant_be_setter", {0: self}))

    def remove_inlines(self):
        self.args = self.args.remove_inlines()
        self.object = self.object.remove_inlines()
        return self


class subscript:
    type = "subscript"

    def __init__(self, obj: object, arg1: number, arg2: number, starting_pos: int, ending_pos: int, source: str):
        self.object = obj
        self.arg1 = arg1
        self.arg2 = arg2
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        error_from_object(self, "", translate("error.unknown"))

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

    def in_text(self):
        return None


class if_:
    type = "if"

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
            prev_ops, self.condition, next_ops = self.condition.simplify()
            prev_ops.extend(previous_operations)
            previous_operations = prev_ops
            next_operations.extend(next_ops)
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
        if len(self.els) > 0:
            nani, cur_thing, nani2 = action("code", "else",
                                            calling_args([], {}, self.starting_pos, self.ending_pos, self.source),
                                            self.starting_pos, self.ending_pos, self.source,
                                            operations=self.els).simplify()
            if len(nani) + len(nani2) > 0:
                error_from_object(self, "", translate("error.unknown"))
        else:
            cur_thing = None
        for k, v in self.eli[::-1]:
            if not k.is_simple():
                prev_ops, k, next_ops = k.simplify()
                prev_ops.extend(previous_operations)
                previous_operations = prev_ops
                next_operations.extend(next_ops)
            if k.type == "action":
                if not actions[k.object][k.name].setdefault("boolean", False):
                    error_from_object(k, "ArgumentError",
                                      translate("error.argumenterror.expected_boolean"))
            elif (k.type == "variable" and k.value_type == "number") or (
                    k.type == "number"):
                nani, k, nani2 = action("variable", "equals", calling_args([], {"value": k,
                                                                                "compare": lst([number(1,
                                                                                                       self.starting_pos,
                                                                                                       self.ending_pos,
                                                                                                       self.source)],
                                                                                               self.starting_pos,
                                                                                               self.ending_pos,
                                                                                               self.source)},
                                                                           self.starting_pos,
                                                                           self.ending_pos,
                                                                           self.source), self.starting_pos,
                                        self.ending_pos, self.source).simplify()
            else:
                error_from_object(k, "ArgumentError", translate("error.argumenterror.wrong_argument",
                                                                {0: k.type, 1: "boolean"}))
            k.operations = v
            if cur_thing is None:
                nani, cur_thing, nani2 = action("code", "else",
                                                calling_args([], {}, self.starting_pos, self.ending_pos,
                                                             self.source),
                                                self.starting_pos, self.ending_pos, self.source,
                                                operations=[k]).simplify()
            else:
                nani, cur_thing, nani2 = action("code", "else",
                                                calling_args([], {}, self.starting_pos, self.ending_pos,
                                                             self.source),
                                                self.starting_pos, self.ending_pos, self.source,
                                                operations=[k, cur_thing]).simplify()
            if len(nani) + len(nani2) > 0:
                error_from_object(self, "", translate("error.unknown"))
        if cur_thing is not None:
            previous_operations.append(cur_thing)
        if len(next_operations) > 0:
            error_from_object(self, "", translate("error.unknown"))
        return previous_operations, None, next_operations


class function:
    type = "function"

    def __init__(self, name: str, operations: list, args: calling_args, source, inline=False, return_var=None,
                 ready=True, description=None, icon=None, hide=None, args_description=None):
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
        args = self.args.set_args()
        unpacked = {}
        if len(args) > 0:
            description = [(text(translate("function.generator.arguments"), Texts.LEGACY, -1, -1, self.source))]
            for i1 in args:
                unpacked[i1["id"]] = i1["unpacked"]
                argument = "argument." + str(i1['type']).lower() + ".name"
                argument_type = translate(argument)
                if argument == argument_type:
                    argument_type = i1['type']
                description_line = f" {i1['id']}: {argument_type}"
                if self.args_description is not None and i1["id"] in self.args_description:
                    description_line += f" - {self.args_description[i1['id']]}"
                description.append(text(description_line, Texts.LEGACY, -1, -1, self.source))
            if self.description is None:
                self.description = []
            self.description.extend(description)
        a = {"type": "function", "name": self.name, "args": args, "template": unpacked, "return_var": self.return_var,
             "inline": self.inline, "completed": False}
        if self.inline:
            a["operations"] = self.operations
        return a

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
                argument_type = translate(argument)
                if argument == argument_type:
                    argument_type = self.return_var.value_type
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
                    error_from_object(self, "", translate("error.unknown"))
                for i1 in args["description"].values:
                    if not i1.type == "text":
                        error_from_object(i1, "", translate("error.unknown"))
            if self.icon is not None:
                if not self.icon.is_simple():
                    nani1, args["icon"], nani2 = self.icon.simplify()
                    if len(nani1) + len(nani2) > 0:
                        error_from_object(self, "", translate("error.unknown"))
                else:
                    args["icon"] = self.icon
                if not args["icon"].type == "item":
                    error_from_object(args["icon"], "", translate("error.unknown"))
        if len(args) > 0:
            a["values"] = [{"name": k1, "value": v1.json()} for k1, v1 in args.items()]
        return a

    def copy(self):
        return self


class process:
    type = "process"

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
                argument_type = translate(argument)
                if argument == argument_type:
                    argument_type = i1['type']
                description_line = f" {i1['id']}: {argument_type}"
                if self.args_description is not None and i1["id"] in self.args_description:
                    description_line += f" - {self.args_description[i1['id']]}"
                description.append(text(description_line, Texts.LEGACY, -1, -1, self.source))
            self.description.extend(description)
        return {"type": "process", "name": self.name, "args": args, "template": unpacked}

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
                    error_from_object(self, "", translate("error.unknown"))
                for i1 in args["description"].values:
                    if not i1.type == "text":
                        error_from_object(i1, "", translate("error.unknown"))
            if self.icon is not None:
                if not self.icon.is_simple():
                    nani1, args["icon"], nani2 = self.icon.simplify()
                    if len(nani1) + len(nani2) > 0:
                        error_from_object(self, "", translate("error.unknown"))
                else:
                    args["icon"] = self.icon
                if not args["icon"].type == "item":
                    error_from_object(args["icon"], "", translate("error.unknown"))
        if len(args) > 0:
            a["values"] = [{"name": k1, "value": v1.json()} for k1, v1 in args.items()]
        return a

    def copy(self):
        return self


class return_:
    type = None

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
                if len(Context(self.source).settings["inline"]) == 0:
                    work_with = var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)
                else:
                    work_with = var(f"var.{new('inline')}", Vars.INLINE, self.starting_pos, self.ending_pos,
                                    self.source)
            else:
                work_with = self.in_var
        else:
            work_with = self.in_var
        if len(Context(self.source).settings["inline"]) > 0:
            Context(self.source).set_inline(work_with.value, self.object)
            return [], None, []
        if not self.object.is_simple():
            prev_ops, cur_op, next_ops = self.object.simplify(mode=0, work_with=work_with)
            prev_ops.extend(previous_operations)
            previous_operations = prev_ops
            next_operations.extend(next_ops)
        else:
            prev_ops, cur_op, next_ops = action("variable", "set_value",
                                                calling_args([], {"variable": work_with, "value": self.object},
                                                             self.starting_pos,
                                                             self.ending_pos,
                                                             self.source), self.starting_pos, self.ending_pos,
                                                self.source).simplify()
            prev_ops.extend(previous_operations)
            previous_operations = prev_ops
            next_operations.extend(next_ops)
        if len(Context(self.source).settings["inline"]) == 0:
            next_operations.append(
                action("code", "return_function", calling_args([], {}, self.starting_pos, self.ending_pos, self.source),
                       self.starting_pos, self.ending_pos, self.source))
        return previous_operations, cur_op, next_operations

    def remove_inlines(self):
        self.object = self.object.remove_inlines()
        return self


class event:
    type = "event"

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
        return {"type": "event", "event": self.name, "position": new("event"),
                "operations": [i3.json() for i3 in self.operations]}

    def copy(self):
        return self


class assign:
    type = "assign"

    def __init__(self, variables: list, assign_type: str, obj: default_jmcc_object, starting_pos: int, ending_pos: int,
                 source: str):
        self.variables = variables
        self.object = obj
        self.assign_type = assign_type
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source

    def __str__(self):
        return f'{self.variables} {self.assign_type} {self.object})'

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


class enum_:
    type = "enum"

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

    def remove_inlines(self):
        self.var = self.var.remove_inlines()
        return self


class block:
    type = "block"

    def __init__(self, id_: str, starting_pos: int, ending_pos: int, source: str):
        self.id = id_.lower().replace("minecraft:", "")
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        self.check_block()

    def check_block(self):
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

    def json(self):
        return {"type": "block", "block": self.id}

    def copy(self):
        return self

    def remove_inlines(self):
        return self


def get_value(jmcc_object, base_value=None):
    if jmcc_object is not None:
        return jmcc_object.value
    return base_value


def minecraft_text(text1):
    def next_symbol(afsd, fdsa):
        if fdsa >= len(afsd):
            return fdsa + 1, None
        return fdsa + 1, afsd[fdsa]

    pos = 0
    msg = ""
    full_msg = {"text": "", "extra": []}

    def add(txt):
        new_txt = {}
        for i1 in txt.keys():
            if (i1 == "italic" and not txt[i1]) or txt[i1]:
                new_txt[i1] = txt[i1]
        full_msg["extra"].append(new_txt)

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
                    old_msg = {"text": msg, "italic": italic, "obfuscated": obfuscated, "underlined": underlined,
                               "strikethrough": strikethrough, "color": color, "bold": bold}
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
                    old_msg = {"text": msg, "italic": italic, "obfuscated": obfuscated, "underlined": underlined,
                               "strikethrough": strikethrough, "color": color, "bold": bold}
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
                    old_msg = {"text": msg, "italic": italic, "obfuscated": obfuscated, "underlined": underlined,
                               "strikethrough": strikethrough, "color": color, "bold": bold}
                    add(old_msg)
                    msg = ""
                underlined = True
                continue
            elif symbol == "m":
                if msg != "":
                    old_msg = {"text": msg, "italic": italic, "obfuscated": obfuscated, "underlined": underlined,
                               "strikethrough": strikethrough, "color": color, "bold": bold}
                    add(old_msg)
                    msg = ""
                strikethrough = True
                continue
            elif symbol == "o":
                if msg != "":
                    old_msg = {"text": msg, "italic": italic, "obfuscated": obfuscated, "underlined": underlined,
                               "strikethrough": strikethrough, "color": color, "bold": bold}
                    add(old_msg)
                    msg = ""
                italic = True
                continue
            elif symbol == "l":
                if msg != "":
                    old_msg = {"text": msg, "italic": italic, "obfuscated": obfuscated, "underlined": underlined,
                               "strikethrough": strikethrough, "color": color, "bold": bold}
                    add(old_msg)
                    msg = ""
                bold = True
                continue
            elif symbol == "k":
                if msg != "":
                    old_msg = {"text": msg, "italic": italic, "obfuscated": obfuscated, "underlined": underlined,
                               "strikethrough": strikethrough, "color": color, "bold": bold}
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
                    old_msg = {"text": msg, "italic": italic, "obfuscated": obfuscated, "underlined": underlined,
                               "strikethrough": strikethrough, "color": color, "bold": bold}
                    add(old_msg)
                    msg = ""
                color = thing.upper()
                continue
            msg += "&" + symbol
            continue

        msg += symbol
        continue
    if msg != "":
        old_msg = {"text": msg, "italic": italic, "obfuscated": obfuscated, "underlined": underlined,
                   "strikethrough": strikethrough, "color": color, "bold": bold}
        add(old_msg)
    if len(full_msg["extra"]) > 0:
        new_msg = full_msg["extra"][0]
        del full_msg["extra"][0]
        new_msg["extra"] = full_msg["extra"]
        if len(new_msg["extra"]) == 0:
            del new_msg["extra"]
        full_msg = new_msg
    else:
        del full_msg["extra"]
    return full_msg


# noinspection PyUnresolvedReferences
class item:
    type = "item"
    type_args = {"id": "text", "name": "text", "count": "number", "lore": ("array", "text"), "nbt": "snbt",
                 "custom_tags": "map"}

    def __init__(self, args: calling_args, starting_pos: int, ending_pos: int, source: str):
        self.args = args
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
        if self.simple:
            return assign([var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)],
                          None, self, self.starting_pos, self.ending_pos, self.source).simplify(mode=mode,
                                                                                                work_with=work_with)
        previous_operations = []
        next_operations = []
        args = self.args.get_args(list(self.type_args.keys()))
        for k1 in args:
            if args[k1] is None:
                continue
            if not args[k1].is_simple():
                if args[k1].type == "snbt":
                    continue
                prev_ops, args[k1], next_ops = args[k1].simplify()
                previous_operations.extend(prev_ops)
                next_operations.extend(next_ops)
            if isinstance(self.type_args[k1], str):
                if args[k1].type == self.type_args[k1]:
                    continue
            elif isinstance(self.type_args[k1], (list, tuple)):
                if args[k1].type in self.type_args[k1]:
                    continue
            error_from_object(args[k1], "ArgumentError", translate("error.argumenterror.wrong_argument",
                                                                        {0: args[k1].type, 1: self.type_args[k1]}))
        args["id"].value = args["id"].value.lower().replace("minecraft:", "")
        if args["id"].value not in items:
            error_from_object(args["id"], "ArgumentError",
                              translate("error.unexistsitem", {0: args["id"].value}))
        self.item = nbtworker.Compound(
            id=nbtworker.String(args["id"].value if args["id"] is not None else ""),
            count=nbtworker.Int(args["count"].value if args["count"] is not None else 1))
        if args["nbt"] is not None:
            self.item["components"] = args["nbt"].value
        if args["name"] is not None or args["lore"] is not None:
            if "components" not in self.item:
                self.item["components"] = nbtworker.Compound()
            if args["name"] is not None:
                self.item["components"]["minecraft:custom_name"] = nbtworker.String(
                    json.dumps(minecraft_text(args["name"].value), ensure_ascii=False, separators=(',', ':')))
            if args["lore"] is not None:
                if args["lore"].type != "array":
                    lore = args["lore"].value.split("\\n")
                else:
                    lore = [i1.value for i1 in args["lore"].values]
                self.item["components"]["minecraft:lore"] = nbtworker.List(
                    *map(nbtworker.String, [json.dumps(i2, ensure_ascii=False, separators=(',', ':')) for i2 in
                                            map(minecraft_text, lore)]))
        if args["custom_tags"] is not None:
            if "components" not in self.item:
                self.item["components"] = nbtworker.Compound()
            if "custom_data" not in self.item:
                self.item["components"]["minecraft:custom_data"] = nbtworker.Compound()
            if "PublicBukkitValues" not in self.item["components"]:
                self.item["components"]["minecraft:custom_data"]["PublicBukkitValues"] = nbtworker.Compound()
            for ind in range(len(args["custom_tags"].keys)):
                k1, v1 = args["custom_tags"].keys[ind].value, args["custom_tags"].values[ind].value
                self.item["components"]["minecraft:custom_data"]["PublicBukkitValues"][
                    f"justcreativeplus:{k1}"] = nbtworker.String(str(v1))
        self.simple = True
        return previous_operations, self, next_operations

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


# noinspection PyUnresolvedReferences
class location:
    type = "location"
    type_args = {"x": "number", "y": "number", "z": "number", "yaw": "number", "pitch": "number"}

    def __init__(self, args: calling_args, starting_pos: int, ending_pos: int, source: str):
        self.args = args
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
        if self.simple:
            return assign([var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)],
                          None, self, self.starting_pos, self.ending_pos, self.source).simplify(mode=mode,
                                                                                                work_with=work_with)
        previous_operations = []
        next_operations = []
        self.args = self.args.get_args(list(self.type_args.keys()))
        is_simple = True
        for k1 in self.args:
            if self.args[k1] is None:
                continue
            if not self.args[k1].is_simple():
                prev_ops, self.args[k1], next_ops = self.args[k1].simplify(mode=0)
                previous_operations.extend(prev_ops)
                next_operations.extend(next_ops)
            if isinstance(self.type_args[k1], str):
                if self.args[k1].type == self.type_args[k1]:
                    continue
            elif isinstance(self.type_args[k1], (list, tuple)):
                if self.args[k1].type in self.type_args[k1]:
                    continue
            is_simple = False
        self.simple = True
        if len(previous_operations) == 0 and len(next_operations) == 0 and is_simple:
            return previous_operations, self, next_operations
        if isinstance(work_with, var):
            current_operation = work_with
        else:
            current_operation = var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)
        previous_operations.append(action("variable", "set_all_coordinates", calling_args([], {
            "variable": current_operation, "x": self.args["x"], "y": self.args["y"], "z": self.args["z"],
            "yaw": self.args["yaw"], "pitch": self.args["pitch"]}, self.starting_pos, self.ending_pos, self.source),
                                          self.starting_pos, self.ending_pos, self.source))
        return previous_operations, current_operation, next_operations

    def json(self):
        return {"type": "location", "x": get_value(self.args["x"], 0), "y": get_value(self.args["y"], 0),
                "z": get_value(self.args["z"], 0), "yaw": get_value(self.args["yaw"], 0),
                "pitch": get_value(self.args["pitch"], 0)}

    def in_text(self):
        return None

    def copy(self):
        return self

    def remove_inlines(self):
        if self.simple:
            return self
        self.args = self.args.remove_inlines()
        return self


# noinspection PyUnresolvedReferences
class vector:
    type = "vector"
    type_args = {"x": "number", "y": "number", "z": "number"}

    def __init__(self, args: calling_args, starting_pos: int, ending_pos: int, source: str):
        self.args = args
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

    def simplify(self, mode=None, work_with=None):
        if self.simple:
            return assign([var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)],
                          None, self, self.starting_pos, self.ending_pos, self.source).simplify(mode=mode,
                                                                                                work_with=work_with)
        previous_operations = []
        next_operations = []
        self.args = self.args.get_args(list(self.type_args.keys()))
        is_simple = True
        for k1 in self.args:
            if self.args[k1] is None:
                continue
            if not self.args[k1].is_simple():
                prev_ops, self.args[k1], next_ops = self.args[k1].simplify(mode=0)
                previous_operations.extend(prev_ops)
                next_operations.extend(next_ops)
            if isinstance(self.type_args[k1], str):
                if self.args[k1].type == self.type_args[k1]:
                    continue
            elif isinstance(self.type_args[k1], (list, tuple)):
                if self.args[k1].type in self.type_args[k1]:
                    continue
            is_simple = False
        self.simple = True
        if len(previous_operations) == 0 and len(next_operations) == 0 and is_simple:
            return previous_operations, self, next_operations
        if isinstance(work_with, var):
            current_operation = work_with
        else:
            current_operation = var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)
        previous_operations.append(action("variable", "set_vector", calling_args([], {
            "variable": current_operation, "x": self.args["x"], "y": self.args["y"], "z": self.args["z"]},
                                                                                 self.starting_pos, self.ending_pos,
                                                                                 self.source),
                                          self.starting_pos, self.ending_pos, self.source))
        return previous_operations, current_operation, next_operations

    def json(self):
        return {"type": "vector", "x": get_value(self.args["x"], 0), "y": get_value(self.args["y"], 0),
                "z": get_value(self.args["z"], 0)}

    def copy(self):
        return self

    def remove_inlines(self):
        self.args = self.args.remove_inlines()
        return self


# noinspection PyUnresolvedReferences
class potion:
    type = "potion"
    type_args = {"potion": "text", "amplifier": "number", "duration": "number"}

    def __init__(self, args: calling_args, starting_pos: int, ending_pos: int, source: str):
        self.args = args
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

    def simplify(self, mode=None, work_with=None):
        if self.simple:
            return assign([var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)],
                          None, self, self.starting_pos, self.ending_pos, self.source).simplify(mode=mode,
                                                                                                work_with=work_with)
        previous_operations = []
        next_operations = []
        self.args = self.args.get_args(list(self.type_args.keys()))
        is_simple = True
        for k1 in self.args:
            if self.args[k1] is None:
                continue
            if not self.args[k1].is_simple():
                prev_ops, self.args[k1], next_ops = self.args[k1].simplify(mode=0)
                previous_operations.extend(prev_ops)
                next_operations.extend(next_ops)
            if isinstance(self.type_args[k1], str):
                if self.args[k1].type == self.type_args[k1]:
                    continue
            elif isinstance(self.type_args[k1], (list, tuple)):
                if self.args[k1].type in self.type_args[k1]:
                    continue
            is_simple = False
        self.args["potion"].value = self.args["potion"].value.lower().replace("minecraft:", "")
        if self.args["potion"].value not in potions:
            error_from_object(self.args["potion"], "ArgumentError",
                              translate("error.unexistspotion", {0: self.args["potion"].value}))
        self.simple = True
        if len(previous_operations) == 0 and len(next_operations) == 0 and is_simple:
            return previous_operations, self, next_operations
        error_from_object(self, "SimplifyError", translate("error.simplifyerror", {0: self}))
        if isinstance(work_with, var):
            current_operation = work_with
        else:
            current_operation = var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)
        return previous_operations, current_operation, next_operations

    def json(self):
        return {"type": "potion", "potion": get_value(self.args["potion"], ""),
                "amplifier": get_value(self.args["amplifier"], 0), "duration": get_value(self.args["duration"], 0)}

    def copy(self):
        return self

    def remove_inlines(self):
        self.args = self.args.remove_inlines()
        return self


# noinspection PyUnresolvedReferences
class sound:
    type = "sound"
    type_args = {"sound": "text", "volume": "number", "pitch": "number", "variation": "text", "source": "text"}

    def __init__(self, args: calling_args, starting_pos: int, ending_pos: int, source: str):
        self.args = args
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

    def in_text(self):
        return None

    def simplify(self, mode=None, work_with=None):
        if self.simple:
            return assign([var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)],
                          None, self, self.starting_pos, self.ending_pos, self.source).simplify(mode=mode,
                                                                                                work_with=work_with)
        previous_operations = []
        next_operations = []
        self.args = self.args.get_args(list(self.type_args.keys()))
        is_simple = True
        for k1 in self.args:
            if self.args[k1] is None:
                continue
            if not self.args[k1].is_simple():
                prev_ops, self.args[k1], next_ops = self.args[k1].simplify(mode=0)
                previous_operations.extend(prev_ops)
                next_operations.extend(next_ops)
            if isinstance(self.type_args[k1], str):
                if self.args[k1].type == self.type_args[k1]:
                    continue
            elif isinstance(self.type_args[k1], (list, tuple)):
                if self.args[k1].type in self.type_args[k1]:
                    continue
            is_simple = False
        self.simple = True
        if len(previous_operations) == 0 and len(next_operations) == 0 and is_simple:
            return previous_operations, self, next_operations
        error_from_object(self, "SimplifyError", translate("error.simplifyerror", {0: self}))
        if isinstance(work_with, var):
            current_operation = work_with
        else:
            current_operation = var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)
        return previous_operations, current_operation, next_operations

    def json(self):
        return {"type": "sound", "sound": get_value(self.args["sound"], ""),
                "volume": get_value(self.args["volume"], 0),
                "pitch": get_value(self.args["pitch"], 0), "variation": get_value(self.args["variation"], ""),
                "source": get_value(self.args["source"], "MASTER")}

    def copy(self):
        return self

    def remove_inlines(self):
        self.args = self.args.remove_inlines()
        return self


# noinspection PyUnresolvedReferences
class particle:
    type = "particle"
    type_args = {"particle": "text", "count": "number", "spread_x": "number", "spread_y": "number",
                 "motion_x": "number", "motion_y": "number", "motion_z": "number", "material": "text",
                 "color": "number",
                 "size": "number", "to_color": "number"}

    def __init__(self, args: calling_args, starting_pos: int, ending_pos: int, source: str):
        self.args = args
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

    def simplify(self, mode=None, work_with=None):
        if self.simple:
            return assign([var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)],
                          None, self, self.starting_pos, self.ending_pos, self.source).simplify(mode=mode,
                                                                                                work_with=work_with)
        previous_operations = []
        next_operations = []
        self.args = self.args.get_args(list(self.type_args.keys()))
        is_simple = True
        for k1 in self.args:
            if self.args[k1] is None:
                continue
            if not self.args[k1].is_simple():
                prev_ops, self.args[k1], next_ops = self.args[k1].simplify(mode=0)
                previous_operations.extend(prev_ops)
                next_operations.extend(next_ops)
            if isinstance(self.type_args[k1], str):
                if self.args[k1].type == self.type_args[k1]:
                    continue
            elif isinstance(self.type_args[k1], (list, tuple)):
                if self.args[k1].type in self.type_args[k1]:
                    continue
            is_simple = False
        self.args["particle"].value = self.args["particle"].value.lower().replace("minecraft:", "")
        if self.args["particle"].value not in particles:
            error_from_object(self.args["particle"], "ArgumentError",
                              translate("error.unexistsparticle", {0: self.args["particle"].value}))
        self.simple = True
        if len(previous_operations) == 0 and len(next_operations) == 0 and is_simple:
            return previous_operations, self, next_operations
        error_from_object(self, "SimplifyError", translate("error.simplifyerror", {0: self}))
        if isinstance(work_with, var):
            current_operation = work_with
        else:
            current_operation = var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)
        return previous_operations, current_operation, next_operations

    def json(self):
        return {"type": "particle", "particle_type": get_value(self.args["particle"], ""),
                "count": get_value(self.args["count"], 0), "first_spread": get_value(self.args["spread_x"], 0),
                "second_spread": get_value(self.args["spread_y"], 0), "x_motion": get_value(self.args["motion_x"], ""),
                "y_motion": get_value(self.args["motion_y"], 0), "z_motion": get_value(self.args["motion_z"], 0),
                "color": get_value(self.args["color"], 0), "material": get_value(self.args["material"], ""),
                "size": get_value(self.args["size"], 0), "to_color": get_value(self.args["to_color"], 0)}

    def copy(self):
        return self

    def remove_inlines(self):
        self.args = self.args.remove_inlines()
        return self


class if_else_expr:
    type = "if_else_expr"

    def __init__(self, cond: default_jmcc_object, true: default_jmcc_object, false: default_jmcc_object,
                 starting_pos: int, ending_pos: int, source: str):
        self.conditional = cond
        self.true = true
        self.false = false
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source

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
        Context(self.source).next_lvl()
        Context(self.source).add_operation(assign([work_with], None, self.true, self.starting_pos, self.ending_pos,
                                                  self.source))
        Context(self.source).update()
        true = Context(self.source).get_operations()
        Context(self.source).previous_lvl()
        Context(self.source).next_lvl()
        Context(self.source).add_operation(assign([work_with], None, self.false, self.starting_pos, self.ending_pos,
                                                  self.source))
        Context(self.source).update()
        false = Context(self.source).get_operations()
        Context(self.source).previous_lvl()
        prev_ops, cur_op, next_ops = if_(self.conditional, true, [], false, self.starting_pos, self.ending_pos,
                                         self.source).simplify()
        return prev_ops, work_with, next_ops


class class_:
    type = None

    def __init__(self, name: str, parent: str, operations: list, source, inline=False, return_var=None):
        self.source = source
        self.name = name

    def __str__(self):
        return f'class({self.name})'

    def __repr__(self):
        return self.__str__()

    def is_simple(self):
        return False

    def simplify(self, mode=None, work_with=None):
        return [], None, []

    def copy(self):
        return self


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


def compile_file(file_path, upload=False, properties=None):
    if properties is None:
        properties = {}
    if not os.path.exists(file_path):
        error_from_object(default_jmcc_object, "UnexistsFile", translate("error.unexistsfile", {0: file_path}))
    file = open(file_path, encoding="UTF-8")
    source = os.path.abspath(file.name)
    pr_source = source.replace(".jc", ".properties", 1)
    if os.path.exists(pr_source):
        properties = Properties(text=open(pr_source, "r", encoding="UTF-8").read()).properties
    code = parse_from_file(file, properties)
    code = code.get_json()
    end_time = time()
    print(minecraft_based_text(f"&fКомпиляция кода заняла: &e{round(end_time-start_time,3)} &fсекунд."))
    if not upload:
        if properties.setdefault("compact", False):
            open(source + ".json", "w").write(json.dumps(code, separators=(',', ':')))
        else:
            open(source + ".json", "w").write(json.dumps(code, indent=2))
    else:
        response = requests.post('https://m.justmc.ru/api/upload', json=code).json()
        print(minecraft_based_text(f"&aФайл успешно загружен\n\n&7Используйте данную команду на сервере для загрузки "
                                   f"модуля:\n&9/module loadUrl force https://m.justmc.ru/api/{response['id']}\n"
                                   f"\n&eВажно &fМодуль по ссылке удалится через &c3 минуты!"
                                   f"\n      &fУспейте использовать команду на сервере за данное время"))
