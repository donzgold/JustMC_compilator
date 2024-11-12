import json
import os

import requests

import nbtworker
from jmcc import translate, minecraft_based_text, color_codes, allowed_symbols, Properties

actions = {}
origin_actions = {}
events = {}
values = {}
items = json.load(open("data/items.json"))
blocks = json.load(open("data/blocks.json"))
particles = json.load(open("data/particles.json"))
potions = json.load(open("data/potions.json"))
objects = set()

for i in json.load(open("data/actions.json")):
    actions[i["object"] + "::" + i["name"]] = i
    objects.add(i["object"])
    if "origin" in i:
        origin_actions[i["name"]] = i["object"] + "::" + i["name"]
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


class Token:

    def __init__(self, token_type: int, token_value: str, starting_pos: int, ending_pos: int, source: str):
        self.type = token_type
        self.value = token_value
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source

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
                f"&c{translate('compilator.file')} \"{source}\":\n{start_line}:{starting_pos - start_line_index} - " +
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
        while self.current_char == " " or self.current_char == "\n" or self.current_char == "\t":
            self.advance()
        starting_pos = self.current_pos
        sign_mode = False
        token_value = ""
        if self.current_char.isalpha() or self.current_char == "_":
            while self.current_char != "" and (
                    self.current_char.isalpha() or self.current_char.isdigit() or self.current_char == "_"):
                token_value += self.current_char
                self.advance()
            if token_value == "if":
                return Token(Tokens.IF, token_value, starting_pos, self.current_pos - 1, self.source)
            if token_value == "else":
                return Token(Tokens.ELSE, token_value, starting_pos, self.current_pos - 1, self.source)
            if token_value == "function":
                return Token(Tokens.FUNCTION_DEFINE, token_value, starting_pos, self.current_pos - 1, self.source)
            if token_value == "process":
                return Token(Tokens.PROCESS_DEFINE, token_value, starting_pos, self.current_pos - 1, self.source)
            if token_value == "var":
                return Token(Tokens.VAR_DEFINE, token_value, starting_pos, self.current_pos - 1, self.source)
            if token_value == "inline":
                return Token(Tokens.INLINE_DEFINE, token_value, starting_pos, self.current_pos - 1, self.source)
            if token_value == "local":
                return Token(Tokens.LOCAL_DEFINE, token_value, starting_pos, self.current_pos - 1, self.source)
            if token_value == "game":
                return Token(Tokens.GAME_DEFINE, token_value, starting_pos, self.current_pos - 1, self.source)
            if token_value == "save":
                return Token(Tokens.SAVE_DEFINE, token_value, starting_pos, self.current_pos - 1, self.source)
            if token_value == "class":
                return Token(Tokens.CLASS_DEFINE, token_value, starting_pos, self.current_pos - 1, self.source)
            if token_value == "event":
                return Token(Tokens.EVENT_DEFINE, token_value, starting_pos, self.current_pos - 1, self.source)
            if token_value == "import":
                return Token(Tokens.IMPORT, token_value, starting_pos, self.current_pos - 1, self.source)
            if token_value == "and":
                return Token(Tokens.AND, token_value, starting_pos, self.current_pos - 1, self.source)
            if token_value == "or":
                return Token(Tokens.OR, token_value, starting_pos, self.current_pos - 1, self.source)
            if token_value == "not":
                return Token(Tokens.NOT, token_value, starting_pos, self.current_pos - 1, self.source)
            if token_value == "return":
                return Token(Tokens.RETURN, token_value, starting_pos, self.current_pos - 1, self.source)
            if token_value == "elif":
                return Token(Tokens.ELIF, token_value, starting_pos, self.current_pos - 1, self.source)
            if token_value == "as":
                return Token(Tokens.AS, token_value, starting_pos, self.current_pos - 1, self.source)
            sign_mode = True

        if self.current_char == "\"" or self.current_char == "\'" or self.current_char == "`":
            mode = self.current_char
            if sign_mode:
                if mode == "`" and token_value in {"l", "local", "g", "game", "s", "save", "i", "inline", "line"}:
                    token_type = Tokens.LOCAL_VARIABLE if token_value in {"l", "local"} else (
                        Tokens.INLINE_VARIABLE if token_value in {"i", "inline"} else (
                            Tokens.LINE_VARIABLE if token_value == "line" else (
                                Tokens.GAME_VARIABLE if token_value in {"g", "game"} else Tokens.SAVE_VARIABLE)))
                elif token_value in {"p", "plain", "l", "legacy", "m", "minimessage", "j", "json"}:
                    token_type = Tokens.PLAIN_STRING if token_value in {"p", "plain"} else (
                        Tokens.MINIMESSAGE_STRING if token_value in {"m", "minimessage"} else (
                            Tokens.LEGACY_STRING if token_value in {"l", "legacy"} else Tokens.JSON_STRING))
                else:
                    return Token(Tokens.VARIABLE, token_value, starting_pos, self.current_pos - 1, self.source)
            else:
                if mode == "`":
                    token_type = Tokens.VARIABLE
                else:
                    token_type = Tokens.STRING
            self.advance()
            token_value = ""
            block_next_symbol = False
            while self.current_char != "" and (self.current_char != mode or block_next_symbol is True):
                if block_next_symbol:
                    block_next_symbol = False
                    token_value += self.current_char
                elif self.current_char == "\\":
                    block_next_symbol = True
                else:
                    token_value += self.current_char
                self.advance()
            if self.current_char == mode:
                self.advance()
                return Token(token_type, token_value, starting_pos,
                             self.current_pos - 1, self.source)
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

        if self.current_char == "<":
            self.advance()
            token_value = ""
            while self.current_char != "" and self.current_char != " " and self.current_char != ">":
                token_value += self.current_char
                self.advance()
            if self.current_char == ">":
                self.advance()
                return Token(Tokens.SUBSTRING, token_value, starting_pos, self.current_pos - 1, self.source)
            elif self.current_char == " " and token_value == "":
                self.advance()
                return Token(Tokens.LESS, "<", starting_pos, self.current_pos - 1, self.source)
            elif self.current_char == " " and token_value == "=":
                self.advance()
                return Token(Tokens.LESS_OR_EQUALS, "<=", starting_pos, self.current_pos - 1, self.source)
            else:
                error("SyntaxError", translate("error.syntaxerror.substring_wasnt_closed"), starting_pos,
                      self.current_pos, self.source)
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
        return Token(Tokens.EOF, "None", starting_pos, starting_pos, self.source)

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
            return Token(Tokens.EOF, "None", -1, -1, self.source)
        return self.tokens[index]

    def eat(self, token_type: int) -> None:
        if self.current_token.type == token_type:
            self.index += 1
            self.current_token = self.token(self.index)
        else:
            error_from_object(self.current_token, "SyntaxError", translate("error.syntaxerror.wrong_token", {
                0: translate('token.' + str(token_type) + '.name'),
                1: translate('token.' + str(self.current_token.type) + '.name')}))

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
        elif token.type == Tokens.STRING:
            self.eat(Tokens.STRING)
            return text(token.value, Texts.LEGACY, token.starting_pos, token.ending_pos, token.source)
        elif token.type == Tokens.LEGACY_STRING:
            self.eat(Tokens.LEGACY_STRING)
            return text(token.value, Texts.LEGACY, token.starting_pos, token.ending_pos, token.source)
        elif token.type == Tokens.PLAIN_STRING:
            self.eat(Tokens.PLAIN_STRING)
            return text(token.value, Texts.PLAIN, token.starting_pos, token.ending_pos, token.source)
        elif token.type == Tokens.MINIMESSAGE_STRING:
            self.eat(Tokens.MINIMESSAGE_STRING)
            return text(token.value, Texts.MINIMESSAGE, token.starting_pos, token.ending_pos, token.source)
        elif token.type == Tokens.JSON_STRING:
            self.eat(Tokens.JSON_STRING)
            return text(token.value, Texts.JSON, token.starting_pos, token.ending_pos, token.source)
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
                args = self.get_args()
                ending_pos = self.current_token.ending_pos
                self.eat(Tokens.RPAREN)
                return calling_object(token.value, args, token.starting_pos, ending_pos, token.source).change()
            elif self.current_token.type == Tokens.DOUBLE_COLON:
                self.eat(Tokens.DOUBLE_COLON)
                act = self.current_token
                self.eat(Tokens.VARIABLE)
                if self.current_token.type == Tokens.SUBSTRING:
                    selector = self.current_token.value
                    self.eat(Tokens.SUBSTRING)
                else:
                    selector = None
                if token.value == "value" and (act.value in values):
                    value_type = values[act.value]["type"]
                    return value(act.value, act.starting_pos, act.ending_pos, token.source, selector=selector,
                                 value_type=value_type)
                if (token.value not in objects) or (not token.value + "::" + act.value in actions):
                    error("SyntaxErrror",
                          translate("error.syntaxerror.action_cant_be_called_from_this_object",
                                    {0: act.value, 1: token.value}), token.starting_pos, act.ending_pos, token.source)
                self.eat(Tokens.LPAREN)
                args = self.get_args()
                ending_pos = self.current_token.ending_pos
                self.eat(Tokens.RPAREN)
                if actions[token.value + "::" + act.value]["type"].startswith(
                        "container"):
                    if self.current_token.type == Tokens.LCPAREN and (
                            not actions[token.value + "::" + act.value].setdefault("boolean", False)):
                        self.eat(Tokens.LCPAREN)
                        if "lambda" in actions[token.value + "::" + act.value]:
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
                            if (a := self.statement()) is not None:
                                self.context.add_operation(a)
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
                return action(token.value, act.value, args, token.starting_pos, ending_pos, self.source,
                              operations=ops, lambd=lambd, selector=selector)
            else:
                if not self.context.has_variable(token.value):
                    self.context.set_variable(token.value, Vars.LOCAL)
                    var_type = Vars.LOCAL
                else:
                    var_type = self.context.get_variable(token.value)
                return var(token.value, var_type, token.starting_pos, token.ending_pos, token.source)
        elif token.type == Tokens.LOCAL_VARIABLE:
            self.eat(Tokens.LOCAL_VARIABLE)
            if not self.context.has_variable(token.value):
                self.context.set_variable(token.value, Vars.LOCAL)
            return var(token.value, Vars.LOCAL, token.starting_pos, token.ending_pos, token.source)
        elif token.type == Tokens.LINE_VARIABLE:
            self.eat(Tokens.LINE_VARIABLE)
            if not self.context.has_variable(token.value):
                self.context.set_variable(token.value, Vars.LINE)
            return var(token.value, Vars.LINE, token.starting_pos, token.ending_pos, token.source)
        elif token.type == Tokens.INLINE_VARIABLE:
            self.eat(Tokens.INLINE_VARIABLE)
            if not self.context.has_variable(token.value):
                self.context.set_variable(token.value, Vars.INLINE)
            return var(token.value, Vars.INLINE, token.starting_pos, token.ending_pos, token.source)
        elif token.type == Tokens.GAME_VARIABLE:
            self.eat(Tokens.GAME_VARIABLE)
            if not self.context.has_variable(token.value):
                self.context.set_variable(token.value, Vars.GAME)
            return var(token.value, Vars.GAME, token.starting_pos, token.ending_pos, token.source)
        elif token.type == Tokens.SAVE_VARIABLE:
            self.eat(Tokens.SAVE_VARIABLE)
            if not self.context.has_variable(token.value):
                self.context.set_variable(token.value, Vars.SAVE)
            return var(token.value, Vars.SAVE, token.starting_pos, token.ending_pos, token.source)
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
                    args.unpositional[actions[origin_actions[act.value]]["origin"]] = result
                    ending_pos = self.current_token.ending_pos
                    self.eat(Tokens.RPAREN)
                    obj, act = origin_actions[act.value].split("::")
                    return self.up_factor(action(obj, act, args, result.starting_pos, ending_pos, self.source))
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
            return self.up_factor(subscript(result, arg1, arg2, result.starting_pos, ending_pos, self.source))
        else:
            return result

    def get_args(self, reason_to_stop=Tokens.RPAREN, save_types=False):
        starting_pos = self.current_token.starting_pos
        ending_pos = self.current_token.ending_pos
        pos = []
        unpos = {}
        while (self.current_token.type != Tokens.EOF) and (self.current_token.type != reason_to_stop):
            if self.current_token.type == Tokens.VARIABLE and self.token(self.index + 1).type == Tokens.ASSIGN:
                token = self.current_token
                self.eat(Tokens.VARIABLE)
                self.eat(Tokens.ASSIGN)
                if (arg := self.expr()) is not None:
                    ending_pos = arg.ending_pos
                    unpos[token.value] = arg
            else:
                if (arg := self.expr()) is not None:
                    if arg.type == "variable" and self.current_token.type == Tokens.COLON and save_types:
                        self.eat(Tokens.COLON)
                        arg.value_type = self.current_token.value
                        self.eat(Tokens.VARIABLE)
                    ending_pos = arg.ending_pos
                    pos.append(arg)
            if self.current_token.type != reason_to_stop:
                self.eat(Tokens.COMMA)
        return calling_args(pos, unpos, starting_pos, ending_pos, self.source)

    def expr(self, lvl=0, result=None):
        if self.current_token.type == Tokens.NOT:
            token = self.current_token
            self.eat(Tokens.NOT)
            result = self.expr()
            return calling_function(result, "__invert__",
                                    calling_args([], {}, token.starting_pos, result.ending_pos, token.source),
                                    token.starting_pos, result.ending_pos, token.source)
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
            variable = self.current_token
            self.eat(Tokens.VARIABLE)
            variable = var(variable.value, Vars.SAVE, variable.starting_pos, variable.ending_pos, self.source)
            self.context.set_variable(variable.value, Vars.SAVE)
        elif self.current_token.type == Tokens.GAME_DEFINE:
            self.eat(Tokens.GAME_DEFINE)
            self.eat(Tokens.VAR_DEFINE)
            variable = self.current_token
            self.eat(Tokens.VARIABLE)
            variable = var(variable.value, Vars.GAME, variable.starting_pos, variable.ending_pos, self.source)
            self.context.set_variable(variable.value, Vars.GAME)
        elif self.current_token.type == Tokens.LOCAL_DEFINE:
            self.eat(Tokens.LOCAL_DEFINE)
            self.eat(Tokens.VAR_DEFINE)
            variable = self.current_token
            variable = var(variable.value, Vars.LOCAL, variable.starting_pos, variable.ending_pos, self.source)
            self.context.set_variable(variable.value, Vars.LOCAL)
        elif self.current_token.type == Tokens.VAR_DEFINE:
            self.eat(Tokens.VAR_DEFINE)
            variable = self.current_token
            self.eat(Tokens.VARIABLE)
            variable = var(variable.value, Vars.LOCAL, variable.starting_pos, variable.ending_pos, self.source)
            self.context.set_variable(variable.value, Vars.LOCAL)
        elif self.current_token.type == Tokens.LINE_DEFINE:
            self.eat(Tokens.LINE_DEFINE)
            self.eat(Tokens.VAR_DEFINE)
            variable = self.current_token
            self.eat(Tokens.VARIABLE)
            variable = var(variable.value, Vars.LINE, variable.starting_pos, variable.ending_pos, self.source)
            self.context.set_variable(variable.value, Vars.LINE)
        elif self.current_token.type == Tokens.INLINE_DEFINE:
            self.eat(Tokens.INLINE_DEFINE)
            self.eat(Tokens.VAR_DEFINE)
            variable = self.current_token
            self.eat(Tokens.VARIABLE)
            variable = var(variable.value, Vars.INLINE, variable.starting_pos, variable.ending_pos, self.source)
            self.context.set_variable(variable.value, Vars.INLINE)
        elif self.current_token.type in {Tokens.VARIABLE, Tokens.LOCAL_VARIABLE, Tokens.SAVE_VARIABLE,
                                         Tokens.GAME_VARIABLE, Tokens.LINE_VARIABLE, Tokens.INLINE_VARIABLE}:
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

    def statement(self):
        if self.current_token.type == Tokens.SEMICOLON:
            self.eat(Tokens.SEMICOLON)
            return
        if self.current_token.type == Tokens.IMPORT and self.context.context_lvl == 0:
            self.eat(Tokens.IMPORT)
            thing = self.current_token
            self.eat(Tokens.STRING)
            if os.path.exists(thing.value):
                fil_source = os.path.abspath(thing.value)
                if (fil_source in Context.context) and (not Context(fil_source).compiled):
                    error_from_object(thing, "ImportError", translate("error.importerror.recursion"))
                self.context.extend(parse_from_file(open(thing.value, "r", encoding="UTF-8")))
            else:
                error_from_object(thing, "UnexistsFile", translate("error.unexistsfile", {0: thing.value}))
            return
        elif ((self.current_token.type == Tokens.FUNCTION_DEFINE and self.context.context_lvl == 0)
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
            self.eat(Tokens.LPAREN)
            args = self.get_args(save_types=True)
            self.eat(Tokens.RPAREN)
            self.eat(Tokens.LCPAREN)
            self.context.next_lvl()
            return_var = var(f"jmcc.{new('var')}", Vars.LOCAL, token.starting_pos, token.ending_pos, token.source)
            self.context.settings["allow_returns"] = return_var
            if not inline:
                self.context.set_special(token.value, {"type": "function", "name": token.value, "args": args.set_args(),
                                                       "return_var": return_var, "inline": inline})
            while (self.current_token.type != Tokens.EOF) and (self.current_token.type != Tokens.RCPAREN):
                if (a := self.statement()) is not None:
                    self.context.add_operation(a)
                self.context.update()
            self.context.settings["allow_returns"] = None
            ops = self.context.get_operations()
            self.context.previous_lvl()
            self.eat(Tokens.RCPAREN)
            result = function(token.value, ops, args, self.source, inline=inline, return_var=return_var)
            if inline:
                self.context.set_special(token.value, result.special())
            return result if result.inline is False else None
        elif self.current_token.type == Tokens.PROCESS_DEFINE and self.context.context_lvl == 0:
            self.eat(Tokens.PROCESS_DEFINE)
            token = self.current_token
            self.eat(Tokens.VARIABLE)
            self.eat(Tokens.LPAREN)
            args = self.get_args(save_types=True)
            self.eat(Tokens.RPAREN)
            self.eat(Tokens.LCPAREN)
            self.context.next_lvl()
            self.context.set_special(token.value, {"type": "process", "name": token.value, "args": args.set_args()})
            while (self.current_token.type != Tokens.EOF) and (self.current_token.type != Tokens.RCPAREN):
                if (a := self.statement()) is not None:
                    self.context.add_operation(a)
                self.context.update()
            ops = self.context.get_operations()
            self.context.previous_lvl()
            self.eat(Tokens.RCPAREN)
            result = process(token.value, ops, args, self.source)
            return result
        elif self.current_token.type == Tokens.EVENT_DEFINE and self.context.context_lvl == 0:
            self.eat(Tokens.EVENT_DEFINE)
            token = self.current_token
            self.eat(Tokens.SUBSTRING)
            self.eat(Tokens.LCPAREN)
            self.context.next_lvl()
            while (self.current_token.type != Tokens.EOF) and (self.current_token.type != Tokens.RCPAREN):
                if (a := self.statement()) is not None:
                    self.context.add_operation(a)
                self.context.update()
            ops = self.context.get_operations()
            self.context.previous_lvl()
            self.eat(Tokens.RCPAREN)
            return event(token.value, ops, self.source)
        elif self.current_token.type == Tokens.IF:
            token = self.current_token
            self.eat(Tokens.IF)
            main_condition = self.expr()
            self.eat(Tokens.LCPAREN)
            self.context.next_lvl()
            while (self.current_token.type != Tokens.EOF) and (self.current_token.type != Tokens.RCPAREN):
                if (a := self.statement()) is not None:
                    self.context.add_operation(a)
                self.context.update()
            main_ops = self.context.get_operations()
            self.context.previous_lvl()
            ending_pos = self.current_token.ending_pos
            self.eat(Tokens.RCPAREN)
            eli = []
            if self.current_token.type == Tokens.ELIF:
                while (self.current_token.type != Tokens.EOF) and (self.current_token.type == Tokens.ELIF):
                    self.eat(Tokens.ELIF)
                    condition = self.expr()
                    self.eat(Tokens.LCPAREN)
                    self.context.next_lvl()
                    while (self.current_token.type != Tokens.EOF) and (self.current_token.type != Tokens.RCPAREN):
                        if (a := self.statement()) is not None:
                            self.context.add_operation(a)
                        self.context.update()
                    ops = self.context.get_operations()
                    self.context.previous_lvl()
                    ending_pos = self.current_token.ending_pos
                    self.eat(Tokens.RCPAREN)
                    eli.append([condition, ops])
            els = []
            if self.current_token.type == Tokens.ELSE:
                self.eat(Tokens.ELSE)
                self.eat(Tokens.LCPAREN)
                self.context.next_lvl()
                while (self.current_token.type != Tokens.EOF) and (self.current_token.type != Tokens.RCPAREN):
                    if (a := self.statement()) is not None:
                        self.context.add_operation(a)
                    self.context.update()
                els.extend(self.context.get_operations())
                self.context.previous_lvl()
                ending_pos = self.current_token.ending_pos
                self.eat(Tokens.RCPAREN)
            return if_(main_condition, main_ops, eli, els, token.starting_pos, ending_pos, self.source)
        elif self.current_token.type == Tokens.RETURN and self.context.settings["allow_returns"] is not None:
            starting_pos = self.current_token.starting_pos
            self.eat(Tokens.RETURN)
            obj = self.expr()
            return return_(obj, starting_pos, obj.ending_pos, self.source,
                           in_var=self.context.settings["allow_returns"])
        else:
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
                obj = self.expr()
                return assign(variables, assign_type, obj, variables[0].starting_pos, obj.ending_pos, self.source)

        return self.expr()

    def parse(self):
        while self.current_token.type != Tokens.EOF:
            if (jmcc_obj := self.statement()) is not None:
                self.context.add_operation(jmcc_obj)
            self.context.update()
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

    def __init__(self, source):
        self.source = source
        if self.source not in self.context:
            self.context[self.source] = {"context_lvl": 0, 0: {"operations": [], "variables": {},
                                                               "vars": {0: {}, 1: {}, 2: {}, 3: {}, 4: {}},
                                                               "inline_vars": {}, "callable": {}},
                                         "settings": {"allow_returns": None},
                                         "cur_context": {"operations": [], "variables": {},
                                                         "vars": {0: {}, 1: {}, 2: {}, 3: {}, 4: {}}, "inline_vars": {},
                                                         "callable": {}},
                                         "compiled": False,
                                         "properties": {}}
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
        if jmcc_obj.is_independent():
            if jmcc_obj.is_simple():
                if self.context_lvl == 0 and not (jmcc_obj.type in ("function", "process", "event")):
                    if len(self.cur_context["operations"]) == 0:
                        self.cur_context["operations"].append(event("world_start", [], self.source))
                    elif self.cur_context["operations"][0].type != "event":
                        self.cur_context["operations"].insert(0, event("world_start", [], self.source))
                    elif self.cur_context["operations"][0].name != "world_start":
                        self.cur_context["operations"].insert(0, event("world_start", [], self.source))
                    self.cur_context["operations"][0].operations.append(jmcc_obj)
                else:
                    self.cur_context["operations"].append(jmcc_obj)
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
        return var_name in self.context[self.source][self.context_lvl]["variables"]

    def get_variable(self, var_name):
        if var_name not in self.context[self.source][self.context_lvl]["variables"]:
            return
        return self.context[self.source][self.context_lvl]["variables"][var_name]

    def get_variables(self):
        return self.context[self.source][self.context_lvl]["variables"]

    def set_variable_type(self, var_type, var_name, value_type):
        self.cur_context["vars"][var_type][var_name] = value_type

    def get_variable_type(self, var_type, var_name):
        if var_name not in self.context[self.source][self.context_lvl]["vars"][var_type]:
            return
        return self.context[self.source][self.context_lvl]["vars"][var_type][var_name]

    def set_inline(self, var_name, var_object):
        self.cur_context["inline_vars"][var_name] = var_object

    def get_inline(self, var_name):
        if var_name not in self.context[self.source][self.context_lvl]["inline_vars"]:
            return
        return self.context[self.source][self.context_lvl]["inline_vars"][var_name]

    def has_inline(self, var_name):
        return var_name in self.context[self.source][self.context_lvl]["inline_vars"]

    def get_inlines(self):
        return self.context[self.source][self.context_lvl]["inline_vars"]

    def set_special(self, var_name, var_object):
        self.cur_context["callable"][var_name] = var_object

    def get_special(self, var_name):
        if var_name not in self.context[self.source][self.context_lvl]["callable"]:
            return
        return self.context[self.source][self.context_lvl]["callable"][var_name]

    def has_special(self, var_name):
        return var_name in self.context[self.source][self.context_lvl]["callable"]

    def get_specials(self):
        return self.context[self.source][self.context_lvl]["callable"]

    def next_lvl(self):
        self.context_lvl += 1
        self.context[self.source][self.context_lvl] = self.context[self.source][
            self.context_lvl - 1].copy()
        self.context[self.source][self.context_lvl]["operations"] = []
        self.cur_context = self.context[self.source][self.context_lvl].copy()

    def previous_lvl(self):
        del self.context[self.source][self.context_lvl]
        self.context_lvl -= 1
        if self.context_lvl not in self.context[self.source]:
            self.context[self.source][self.context_lvl] = {"operations": [], "variables": {},
                                                           "vars": {0: {}, 1: {}, 2: {}, 3: {}, 4: {}},
                                                           "inline_vars": {},
                                                           "callable": {}}
        self.cur_context = self.context[self.source][self.context_lvl].copy()

    def update(self):
        self.context[self.source][self.context_lvl] = self.cur_context

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
                        "is_hidden": False, "name": f"jmcc.{func_count}"}
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
        if len(self.context[self.source]["cur_context"]["operations"]) == 0:
            self.context[self.source]["cur_context"]["operations"].append(event("world_start", [], self.source))
        elif self.context[self.source]["cur_context"]["operations"][0].type != "event":
            self.context[self.source]["cur_context"]["operations"].insert(0, event("world_start", [], self.source))
        elif self.context[self.source]["cur_context"]["operations"][0].name != "world_start":
            self.context[self.source]["cur_context"]["operations"].insert(0, event("world_start", [], self.source))
        if len(another_context.context[another_context.source][another_context.context_lvl]["operations"]) == 0:
            another_context.context[another_context.source][another_context.context_lvl]["operations"].append(
                event("world_start", [], self.source))
        elif another_context.context[another_context.source][another_context.context_lvl]["operations"][0].type != "event":
            another_context.context[another_context.source][another_context.context_lvl]["operations"].insert(0, event(
                "world_start", [], self.source))
        elif another_context.context[another_context.source][another_context.context_lvl]["operations"][0].name != "world_start":
            another_context.context[another_context.source][another_context.context_lvl]["operations"].insert(0, event(
                "world_start", [], self.source))
        self.context[self.source]["cur_context"]["operations"][0].operations.extend(
            another_context.context[another_context.source][another_context.context_lvl]["operations"].pop(0).operations)
        self.context[self.source]["cur_context"]["operations"].extend(
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

    @staticmethod
    def is_simple():
        return True

    @staticmethod
    def is_independent():
        return False

    json = None

    def remove_inlines(self):
        return self


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

    @staticmethod
    def is_simple():
        return True

    def json(self):
        return {"type": "text", "text": self.value, "parsing": Texts.changer[self.value_type].lower()}

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
                len_limit = actions["variable::create_list"]["args"][1]["array"]
                self.values = new_lst[:len_limit]
                del new_lst[:len_limit]
                previous_operations.append(action("variable", "create_list",
                                                  calling_args([], {"variable": current_operation,
                                                                    "values": lst(self.values, self.starting_pos,
                                                                                  self.ending_pos, self.source)},
                                                               self.starting_pos,
                                                               self.ending_pos, self.source), self.starting_pos,
                                                  self.ending_pos, self.source))
                len_limit = actions["variable::append_value"]["args"][1]["array"]
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

    def remove_inlines(self):
        for i1 in range(len(self.values)):
            self.values[i1] = self.values[i1].remove_inlines()
        return self


class dct:
    type = "map"

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

    def json(self):
        return {"type": "map", "keys": [i3.json() for i3 in self.keys],
                "values": [i3.json() for i3 in self.values]}

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
            len_limit = actions["variable::create_map_from_values"]["args"][1]["array"]
            if len(self.keys) > len_limit:
                len_limit = actions["variable::create_list"]["args"][1]["array"]
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
                len_limit = actions["variable::append_value"]["args"][1]["array"]
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

    def simplify(self, mode=None, work_with=None):
        if "id" in self.value and "Count" in self.value:
            return item(calling_args([], {
                "id": text(self.value["id"].value, Texts.PLAIN, self.starting_pos, self.ending_pos, self.source),
                "count": number(self.value["Count"].value, self.starting_pos, self.ending_pos, self.source),
                "nbt": NBT(self.value["tag"], self.starting_pos, self.ending_pos,
                           self.source) if "tag" in self.value else None},
                                     self.starting_pos, self.ending_pos, self.source), self.starting_pos,
                        self.ending_pos, self.source).simplify(mode=mode, work_with=work_with)
        else:
            error_from_object(self, "SimplifyError", translate("error.simplifyerror", {0: self}))

    def remove_inlines(self):
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
        self.simple = self.var_type not in {0, 1}

    def __str__(self):
        return f'var(`{self.value}`,{self.var_type})'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def is_independent():
        return False

    def is_simple(self):
        return self.simple

    def simplify(self, mode=None, work_with=None):
        if self.var_type == Vars.INLINE:
            val = Context(self.source).get_inline(self.value)
            val.starting_pos = self.starting_pos
            val.ending_pos = self.ending_pos
            val.source = self.source
            if val.is_simple():
                return [], val, []
            return val.simplify(mode=0)
        elif self.var_type == Vars.LINE:
            self.var_type = Vars.LOCAL
            self.value = f"{self.value}_%var_local(var_depth)"
            self.simple = True
            return [], self, []
        else:
            error_from_object(self, "SimplifyError", translate("error.simplifyerror", {0: self}))

    def json(self):
        return {"type": "variable", "variable": self.value, "scope": Vars.changer[self.var_type].lower()}

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

    def get_args(self, template: list) -> (dict | default_jmcc_object):
        args = {i1: None for i1 in template}
        for k1, v1 in self.unpositional.items():
            if k1 in args:
                args[k1] = v1
            else:
                error_from_object(self, "ArgumentError", translate("error.argumenterror.argument_with_wrong_name",
                                                                   {0: k1, 1: ", ".join(
                                                                       map(lambda x: "'" + str(x) + "'", template))}))
        positional = self.positional.copy()
        if len(positional) > 0:
            for k1, v1 in args.items():
                if v1 is None:
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
        for i1 in self.positional:
            if i1.type == "variable":
                arg = {"id": i1.value, "type": i1.value_type, "optional": None}
            else:
                error_from_object(self, "ArgumentError",
                                  translate("error.argumenterror.wrong_argument", {0: i1, 1: "variable"}))
                exit()
            args.append(arg)
        for k1, v1 in self.unpositional.items():
            if not v1.is_simple():
                error_from_object(self, "ArgumentError",
                                  translate("error.jsonerror.object_isnt_simple", {0: v1}))
            arg = {"id": k1, "type": v1.type, "optional": v1}
            args.append(arg)
        return args

    def remove_inlines(self):
        for i1 in range(len(self.positional)):
            self.positional[i1] = self.positional[i1].remove_inlines()
        for i1 in self.unpositional:
            self.unpositional[i1] = self.unpositional[i1].remove_inlines()
        return self


class value:
    type = "value"

    def __init__(self, val: str, starting_pos: int, ending_pos: int, source: str, selector=None, value_type=None):
        self.value = val
        self.value_type = value_type
        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.source = source
        self.selector = selector

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

    def json(self):
        return {"type": "game_value", "game_value": values[self.value]["id"],
                "selection": json.dumps({"type": self.selector},
                                        separators=(',', ':')) if self.selector is not None else "null"}

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

    def simplify(self, mode=None, work_with=None):
        self.args: calling_args
        if mode == 1:
            error_from_object(self, "ActionError", translate("error.actionerror.action_cant_be_setter", {0: self}))
        context = Context(self.source)
        if actions[self.object + "::" + self.name]["type"].endswith("conditional"):
            thing = self.args.get_args(["conditional"])["conditional"]
            a1, thing, a2 = thing.simplify()
            if not thing.type == "action":
                error_from_object(thing, "", "ебанутый?")
            if not actions[thing.object + "::" + thing.name].setdefault("boolean", False):
                error_from_object(thing, "", "ебанутый?")
            if len(a1) + len(a2) > 0:
                error_from_object(thing, "", "ебанутый?")
            self.conditional = thing
            self.simple = True
            self.args = thing.args
            return [], self, []
        else:
            arges = {i1["id"]: i1 for i1 in actions[self.object + "::" + self.name]["args"]}
            previous_operations = []
            next_operations = []
            inline = False
            if mode == 0:
                if "assign" in actions[self.object + "::" + self.name]:
                    if isinstance(work_with, list):
                        for i2 in range(len(actions[self.object + "::" + self.name]["assign"])):
                            if i2 < len(work_with):
                                if work_with[i2].type == "variable" and work_with[i2].var_type == Vars.INLINE:
                                    inline = True
                                    break
                                else:
                                    self.args.unpositional[
                                        actions[self.object + "::" + self.name]["assign"][i2]["id"]] = \
                                        work_with[i2]
                            else:
                                break
                    else:
                        if not isinstance(work_with, var):
                            work_with = var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos,
                                            self.source)
                        self.args.unpositional[actions[self.object + "::" + self.name]["assign"][0]["id"]] = work_with

                elif actions[self.object + "::" + self.name].setdefault("boolean", False):
                    if not isinstance(work_with, var):
                        work_with = var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos,
                                        self.source)
                    previous_operations.append(action("variable", "set_value", calling_args([], {
                        "variable": work_with, "value": number(0, self.starting_pos, self.ending_pos, self.source)},
                                                                                            self.starting_pos,
                                                                                            self.ending_pos,
                                                                                            self.source),
                                                      self.starting_pos, self.ending_pos, self.source))
                    nani, cur_thing, nani2 = action("variable", "set_value", calling_args([], {
                        "variable": work_with, "value": number(1, self.starting_pos, self.ending_pos, self.source)},
                                                                                          self.starting_pos,
                                                                                          self.ending_pos,
                                                                                          self.source),
                                                    self.starting_pos, self.ending_pos, self.source).simplify()
                    if len(nani) + len(nani2) > 0:
                        error_from_object(self, "", "ебанутый?")
                    self.operations = [cur_thing]
                else:
                    error_from_object(self, "ActionError", translate("error.actionerror.action_has_no_value",
                                                                     {0: f"{self.object}::{self.name}"}))
            if "lambda" in actions[self.object + "::" + self.name]:
                if isinstance(self.lambd, list):
                    for i2 in range(len(actions[self.object + "::" + self.name]["lambda"])):
                        if i2 < len(self.lambd):
                            self.args.unpositional[actions[self.object + "::" + self.name]["lambda"][i2]["id"]] = \
                                self.lambd[i2]
                        else:
                            break
            load_args = self.args.get_args(list(arges))
            if (self.object + "::" + self.name) == "variable::set_value":
                if inline:
                    context.set_inline(work_with[0].value, load_args["value"].remove_inlines())
                    return [], default_jmcc_object, []
                if load_args["value"].type in {"array", "map", "subscript", "calling_argument", "calling_function",
                                               "calling_object", "action"}:
                    return load_args["value"].simplify(mode=0, work_with=load_args["variable"])
                if load_args["variable"].type in {"subscript", "calling_argument"}:
                    return load_args["variable"].simplify(mode=1, work_with=load_args["value"])
                load_args["variable"].value_type = load_args["value"].type
            if inline:
                context.set_inline(work_with[0].value, self.remove_inlines())
                return [], default_jmcc_object, []
            if (self.object + "::" + self.name) == "variable::create_list":
                if load_args["values"].type == "array" and len(load_args["values"].values) > arges["values"]["array"]:
                    return (load_args["values"] if load_args["values"] is not None else
                            lst([], self.starting_pos, self.ending_pos, self.source)).simplify(
                        mode=0, work_with=load_args["variable"], len_limit=arges["values"]["array"])
            if (self.object + "::" + self.name) == "variable::create_map_from_values":
                if (len(load_args["values"].values) > arges["values"]["array"] and len(load_args["keys"].values) >
                        arges["keys"]["array"]):
                    return dct(load_args["keys"].values, load_args["values"].values, self.starting_pos, self.ending_pos,
                               self.source).simplify(mode=0, work_with=load_args["variable"])
            args = {}
            if "assign" in actions[self.object + "::" + self.name]:
                assigning = {i2["id"]: i2["type"] for i2 in actions[self.object + "::" + self.name]["assign"]}
            else:
                assigning = {}
            v1: default_jmcc_object
            for k1, v1 in load_args.items():
                if v1 is None:
                    if "array" in arges[k1]:
                        args[k1] = lst([], self.starting_pos, self.ending_pos, self.source)
                    continue
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
                    continue
                if need_typ in ("enum", "boolean"):
                    if args[k1].type == "text":
                        possible_enumeration = [i1 for i1 in arges[k1]["values"]] if need_typ == "enum" else ["TRUE",
                                                                                                              "FALSE"]
                        if not args[k1].value in possible_enumeration:
                            error_from_object(args[k1], "ArgumentError", translate("error.argumenterror.unknown_enum",
                                                                                   {0: args[k1].value, 1: ", ".join(
                                                                                       map(lambda x: "'" + str(x) + "'",
                                                                                           possible_enumeration))}))
                        args[k1] = enum_(args[k1].value, args[k1].starting_pos, args[k1].ending_pos, args[k1].source)
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
        a = {"action": actions[self.object + "::" + self.name]["id"],
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
        for k1, v1 in self.args.get_args(list(arges)).items():
            if v1 is None:
                v1 = arges[k1]["optional"]
                if v1 is None:
                    error_from_object(self, "ArgumentError",
                                      translate("error.argumenterror.argument_is_not_specified", {0: k1}))
            if v1.is_simple():
                args[k1] = v1
            else:
                prev_ops, args[k1], next_ops = v1.simplify(mode=0)
                prev_ops.extend(previous_operations)
                previous_operations = prev_ops
                next_operations.extend(next_ops)
            if not (args[k1].type == "variable" and args[k1].value == k1):
                previous_operations.append(action("variable", "set_value", calling_args([], {
                    "variable": var(k1, Vars.LOCAL, self.starting_pos, self.ending_pos, self.source),
                    "value": args[k1]},
                                                                                        self.starting_pos,
                                                                                        self.ending_pos,
                                                                                        self.source), self.starting_pos,
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
            if special["inline"]:
                previous_operations.extend(special["operations"])
            else:
                previous_operations.append(action("code", "call_function", calling_args([], {
                    "function_name": text(self.value, Texts.LEGACY, self.starting_pos, self.ending_pos, self.source)},
                                                                                        self.starting_pos,
                                                                                        self.ending_pos,
                                                                                        self.source), self.starting_pos,
                                                  self.ending_pos, self.source))
            if mode == 0:
                if not isinstance(work_with, var):
                    work_with = var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)
                previous_operations.append(action("variable", "set_value", calling_args([], {
                    "variable": work_with, "value": special["return_var"]}, self.starting_pos, self.ending_pos,
                                                                                        self.source),
                                                  self.starting_pos, self.ending_pos, self.source))
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
            error_from_object(self, "", "Не поддерживается")
        return previous_operations, default_jmcc_object, next_operations

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
        error_from_object(self, "", "Не поддерживается")

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

    def simplify(self, mode=None, work_with=None):
        previous_operations = []
        next_operations = []
        if mode == 0 or mode is None:
            if not isinstance(work_with, var):
                work_with = var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)
            if self.value in {"__or__", "__and__"}:
                if not self.args.positional[0].is_simple():
                    prev_ops, self.args.positional[0], next_ops = self.args.positional[0].simplify(mode=0)
                    prev_ops.extend(previous_operations)
                    previous_operations = prev_ops
                    next_operations = next_ops
                if not ((self.args.positional[0].type == "action") or (self.args.positional[0].type == "variable" and self.args.positional[0].value_type == "number") or (self.args.positional[0].type == "number")):
                    error_from_object(self.args.positional[0], "ArgumentError",
                                      translate("error.argumenterror.wrong_argument",
                                                {0: self.args.positional[0].type, 1: "boolean"}))
                if not self.args.positional[1].is_simple():
                    prev_ops, self.args.positional[1], next_ops = self.args.positional[1].simplify(mode=0)
                    prev_ops.extend(previous_operations)
                    previous_operations = prev_ops
                    next_operations = next_ops
                if not ((self.args.positional[1].type == "action") or (
                        (self.args.positional[1].type == "variable") and (
                        self.args.positional[1].value_type == "number")) or (self.args.positional[1].type == "number")):
                    error_from_object(self.args.positional[1], "ArgumentError",
                                      translate("error.argumenterror.wrong_argument",
                                                {0: self.args.positional[1].type, 1: "boolean"}))
            if self.value == "__or__":
                new_var = var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)
                previous_operations.append(action("variable", "add", calling_args([], {"variable": new_var,
                                                                                       "value": lst(
                                                                                           [self.args.positional[0],
                                                                                            self.args.positional[1]],
                                                                                           self.starting_pos,
                                                                                           self.ending_pos,
                                                                                           self.source)},
                                                                                  self.starting_pos, self.ending_pos,
                                                                                  self.source), self.starting_pos,
                                                  self.ending_pos, self.source))
                previous_operations.append(action("variable", "set_value", calling_args([], {"variable": work_with,
                                                                                             "value": number(0,
                                                                                                             self.starting_pos,
                                                                                                             self.ending_pos,
                                                                                                             self.source)},
                                                                                        self.starting_pos,
                                                                                        self.ending_pos, self.source),
                                                  self.starting_pos, self.ending_pos, self.source))
                nani, cur_thing, nani2 = action("variable", "set_value", calling_args([], {"variable": work_with,
                                                                                           "value": number(1,
                                                                                                           self.starting_pos,
                                                                                                           self.ending_pos,
                                                                                                           self.source)},
                                                                                      self.starting_pos,
                                                                                      self.ending_pos, self.source),
                                                self.starting_pos, self.ending_pos, self.source).simplify()
                nani, cur_thing, nani2 = action("variable", "greater", calling_args([], {"value": new_var,
                                                                                         "compare": number(0,
                                                                                                           self.starting_pos,
                                                                                                           self.ending_pos,
                                                                                                           self.source)},
                                                                                    self.starting_pos, self.ending_pos,
                                                                                    self.source), self.starting_pos,
                                                self.ending_pos, self.source, operations=[cur_thing]).simplify()
                previous_operations.append(cur_thing)

                return previous_operations, work_with, next_operations
            elif self.value == "__and__":
                new_var = var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)
                previous_operations.append(action("variable", "add", calling_args([], {"variable": new_var,
                                                                                       "value": lst(
                                                                                           [self.args.positional[0],
                                                                                            self.args.positional[1]],
                                                                                           self.starting_pos,
                                                                                           self.ending_pos,
                                                                                           self.source)},
                                                                                  self.starting_pos, self.ending_pos,
                                                                                  self.source), self.starting_pos,
                                                  self.ending_pos, self.source))
                previous_operations.append(action("variable", "set_value", calling_args([], {"variable": work_with,
                                                                                             "value": number(0,
                                                                                                             self.starting_pos,
                                                                                                             self.ending_pos,
                                                                                                             self.source)},
                                                                                        self.starting_pos,
                                                                                        self.ending_pos, self.source),
                                                  self.starting_pos, self.ending_pos, self.source))
                nani, cur_thing, nani2 = action("variable", "set_value", calling_args([], {"variable": work_with,
                                                                                           "value": number(1,
                                                                                                           self.starting_pos,
                                                                                                           self.ending_pos,
                                                                                                           self.source)},
                                                                                      self.starting_pos,
                                                                                      self.ending_pos, self.source),
                                                self.starting_pos, self.ending_pos, self.source).simplify()
                nani, cur_thing, nani2 = action("variable", "equals", calling_args([], {"value": new_var,
                                                                                        "compare": lst([number(2,
                                                                                                               self.starting_pos,
                                                                                                               self.ending_pos,
                                                                                                               self.source)],
                                                                                                       self.starting_pos,
                                                                                                       self.ending_pos,
                                                                                                       self.source)},
                                                                                   self.starting_pos, self.ending_pos,
                                                                                   self.source), self.starting_pos,
                                                self.ending_pos, self.source, operations=[cur_thing]).simplify()
                previous_operations.append(cur_thing)

                return previous_operations, work_with, next_operations
            elif self.value == "__invert__":
                self.object.invert = not self.object.invert
                if self.object.is_simple():
                    return [], self.object, []
                else:
                    return self.object.simplify(mode=mode, work_with=work_with)
            else:
                error_from_object(self, "", "Не поддерживается")
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
        error_from_object(self, "", "Не поддерживается")

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

    def simplify(self):
        previous_operations = []
        next_operations = []
        if not self.condition.is_simple():
            prev_ops, self.condition, next_ops = self.condition.simplify()
            prev_ops.extend(previous_operations)
            previous_operations = prev_ops
            next_operations.extend(next_ops)
        if self.condition.type == "action":
            if not actions[self.condition.object + "::" + self.condition.name].setdefault("boolean", False):
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
                error_from_object(self, "", "ебанутый?")
        else:
            cur_thing = None
        for k, v in self.eli[::-1]:
            if not k.is_simple():
                prev_ops, k, next_ops = k.simplify()
                prev_ops.extend(previous_operations)
                previous_operations = prev_ops
                next_operations.extend(next_ops)
            if k.type == "action":
                if not actions[k.object + "::" + k.name].setdefault("boolean", False):
                    error_from_object(k, "ArgumentError",
                                      translate("error.argumenterror.expected_boolean"))
                else:
                    k.operations = v
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
                k.operations = v
            else:
                error_from_object(k, "ArgumentError", translate("error.argumenterror.wrong_argument",
                                                                {0: k.type, 1: "boolean"}))
            if cur_thing is None:
                cur_thing = k
            else:
                nani, cur_thing, nani2 = action("code", "else",
                                                calling_args([], {}, self.starting_pos, self.ending_pos,
                                                             self.source),
                                                self.starting_pos, self.ending_pos, self.source,
                                                operations=[k, cur_thing]).simplify()
                if len(nani) + len(nani2) > 0:
                    error_from_object(self, "", "ебанутый?")
        if cur_thing is not None:
            previous_operations.append(cur_thing)
        if len(next_operations) > 0:
            error_from_object(self, "", "ебанутый?")
        return previous_operations, default_jmcc_object, next_operations


class function:
    type = "function"

    def __init__(self, name: str, operations: list, args: calling_args, source, inline=False, return_var=None):
        self.name = name
        if len(operations) > 0:
            while (operations[-1].type == "action") and (
                    operations[-1].object + "::" + operations[-1].name == "code::return_function"):
                del operations[-1]
        self.operations = operations
        self.args = args
        self.source = source
        self.inline = inline
        self.return_var = return_var

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

    def special(self):
        a = {"type": "function", "name": self.name, "args": self.args.set_args(), "return_var": self.return_var,
             "inline": self.inline}
        if self.inline:
            a["operations"] = self.operations
        return a

    def json(self):
        return {"type": "function", "position": new("event"), "operations": [i3.json() for i3 in self.operations],
                "is_hidden": False, "name": self.name}


class process:
    type = "process"

    def __init__(self, name: str, operations: list, args: calling_args, source):
        self.name = name
        self.operations = operations
        self.args = args
        self.source = source

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
        return {"type": "process", "name": self.name, "args": self.args.set_args()}

    def json(self):
        return {"type": "process", "position": new('event'), "operations": [i3.json() for i3 in self.operations],
                "name": self.name, "is_hidden": False}


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

    def simplify(self, mode=None, work_with=None):
        previous_operations = []
        next_operations = []
        if mode == 0:
            if not isinstance(work_with, var):
                work_with = var(f"jmcc.{new('var')}", Vars.LOCAL, self.starting_pos, self.ending_pos, self.source)
            else:
                work_with = self.in_var
        else:
            work_with = self.in_var
        if not work_with.is_simple():
            prev_ops, work_with, next_ops = work_with.simplify()
            prev_ops.extend(previous_operations)
            previous_operations = prev_ops
            next_operations.extend(next_ops)
        if not self.object.is_simple():
            prev_ops, cur_op, next_ops = self.object.simplify(mode=0, work_with=work_with)
            prev_ops.extend(previous_operations)
            previous_operations = prev_ops
            next_operations.extend(next_ops)
        else:
            cur_op = action("variable", "set_value",
                            calling_args([], {"variable": work_with, "value": self.object}, self.starting_pos,
                                         self.ending_pos,
                                         self.source), self.starting_pos, self.ending_pos, self.source)
        next_operations.append(
            action("code", "return_function", calling_args([], {}, self.starting_pos, self.ending_pos, self.source),
                   self.starting_pos, self.ending_pos, self.source))
        return previous_operations, cur_op, next_operations

    def remove_inlines(self):
        self.object = self.object.remove_inlines()
        return self


class event:
    type = "event"

    def __init__(self, name: str, operations: list, source):
        self.name = name
        self.operations = operations
        self.source = source

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

    def json(self):
        return {"type": "event", "event": self.name, "position": new("event"),
                "operations": [i3.json() for i3 in self.operations]}


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
        # world::set_block([location(0, 0, 0, 0, 0), location(0, 0, 0, 0, 0)], item("stone"), "FALSE");

    def __str__(self):
        return f'block({self.id})'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def is_simple():
        return True

    def json(self):
        return {"type": "block", "block": self.id}

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
        previous_operations = []
        next_operations = []
        self.args = self.args.get_args(list(self.type_args.keys()))
        for k1 in self.args:
            if self.args[k1] is None:
                continue
            if not self.args[k1].is_simple():
                if self.args[k1].type == "snbt":
                    continue
                prev_ops, self.args[k1], next_ops = self.args[k1].simplify()
                previous_operations.extend(prev_ops)
                next_operations.extend(next_ops)
            if isinstance(self.type_args[k1], str):
                if self.args[k1].type == self.type_args[k1]:
                    continue
            elif isinstance(self.type_args[k1], (list, tuple)):
                if self.args[k1].type in self.type_args[k1]:
                    continue
            error_from_object(self.args[k1], "ArgumentError", translate("error.argumenterror.wrong_argument",
                                                                        {0: self.args[k1].type, 1: self.type_args[k1]}))
        self.args["id"].value = self.args["id"].value.lower().replace("minecraft:", "")
        if self.args["id"].value not in items:
            error_from_object(self.args["id"], "ArgumentError",
                              translate("error.unexistsitem", {0: self.args["id"].value}))
        self.item = nbtworker.Compound(
            id=nbtworker.String(self.args["id"].value if self.args["id"] is not None else ""),
            count=nbtworker.Int(self.args["count"].value if self.args["count"] is not None else 1))
        if self.args["nbt"] is not None:
            self.item["components"] = self.args["nbt"].value
        if self.args["name"] is not None or self.args["lore"] is not None:
            if "components" not in self.item:
                self.item["components"] = nbtworker.Compound()
            if self.args["name"] is not None:
                self.item["components"]["minecraft:custom_name"] = nbtworker.String(
                    json.dumps(minecraft_text(self.args["name"].value), ensure_ascii=False, separators=(',', ':')))
            if self.args["lore"] is not None:
                if self.args["lore"].type != "array":
                    lore = self.args["lore"].value.split("\\n")
                else:
                    lore = [i1.value for i1 in self.args["lore"].values]
                self.item["components"]["minecraft:lore"] = nbtworker.List(
                    *map(nbtworker.String, [json.dumps(i2, ensure_ascii=False, separators=(',', ':')) for i2 in
                                            map(minecraft_text, lore)]))
        if self.args["custom_tags"] is not None:
            if "components" not in self.item:
                self.item["components"] = nbtworker.Compound()
            if "custom_data" not in self.item:
                self.item["components"]["minecraft:custom_data"] = nbtworker.Compound()
            if "PublicBukkitValues" not in self.item["components"]:
                self.item["components"]["minecraft:custom_data"]["PublicBukkitValues"] = nbtworker.Compound()
            for ind in range(len(self.args["custom_tags"].keys)):
                k1, v1 = self.args["custom_tags"].keys[ind].value, self.args["custom_tags"].values[ind].value
                self.item["components"]["minecraft:custom_data"]["PublicBukkitValues"][
                    f"justcreativeplus:{k1}"] = nbtworker.String(str(v1))
        self.simple = True
        return previous_operations, self, next_operations

    def json(self):
        return {"type": "item", "item": str(self.item)}

    def remove_inlines(self):
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

    def remove_inlines(self):
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

    def simplify(self, mode=None, work_with=None):
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

    def simplify(self, mode=None, work_with=None):
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

    def simplify(self, mode=None, work_with=None):
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

    def simplify(self, mode=None, work_with=None):
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

    def remove_inlines(self):
        self.args = self.args.remove_inlines()
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
    if not upload:
        if properties.setdefault("compact", False):
            open(source + ".json", "w").write(json.dumps(code, separators=(',', ':'), ensure_ascii=False))
        else:
            open(source + ".json", "w").write(json.dumps(code, indent=2, ensure_ascii=False))
    else:
        response = requests.post('https://m.justmc.ru/api/upload', json=code).json()
        print(minecraft_based_text(f"&aФайл успешно загружен\n\n&7Используйте данную команду на сервере для загрузки "
                                   f"модуля:\n&9/module loadUrl force https://m.justmc.ru/api/{response['id']}\n"
                                   f"\n&eВажно &fМодуль по ссылке удалится через &c3 минуты!"
                                   f"\n      &fУспейте использовать команду на сервере за данное время"))
