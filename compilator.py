import gzip
import json
import os
import requests
import sys
from math import ceil, floor

NUMBER = "NUMBER"
MINUS_NUMBER = "MINUS_NUMBER"
PLUS_NUMBER = "PLUS_NUMBER"
STRING = "STRING"
MINUS = "MINUS"
ASSIGN = "ASSIGN"
PLUS = "PLUS"
ELSE = "ELSE"
MULTIPLY = "MULTIPLY"
SELECT = "SELECT"
DIVIDE = "DIVIDE"
COLON = "COLON"
CODE = "CODE"
VARIABLE = "VARIABLE"
INT_DIVIDE = "INT_DIVIDE"
MINUS_WITH_ASSIGN = "MINUS_WITH_ASSIGN"
PLUS_WITH_ASSIGN = "PLUS_WITH_ASSIGN"
MULTIPLY_WITH_ASSIGN = "MULTIPLY_WITH_ASSIGN"
DIVIDE_WITH_ASSIGN = "DIVIDE_WITH_ASSIGN"
INT_DIVIDE_WITH_ASSIGN = "INT_DIVIDE_WITH_ASSIGN"
PR_WITH_ASSIGN = "PR_WITH_ASSIGN"
DEG_WITH_ASSIGN = "DEG_WITH_ASSIGN"
CYCLE_THING = "CYCLE_THING"
VALUE = "VALUE"
REPEAT = "REPEAT"
CONTROLLER = "CONTROLLER"
SELECTOR = "SELECTOR"
LOCATION = "LOCATION"
PARTICLE = "PARTICLE"
ITEM = "ITEM"
SOUND = "SOUND"
VECTOR = "VECTOR"
POTION = "POTION"
IMPORT = "IMPORT"
WORLD = "WORLD"
NOT = "NOT"
FUNCTION = "FUNCTION"
PROCESS = "PROCESS"
DOT = "DOT"
PR = "PR"
LPAREN = "LPAREN"
RPAREN = "RPAREN"
LSPAREN = "LSPAREN"
RSPAREN = "RSPAREN"
LCPAREN = "LCPAREN"
RCPAREN = "RCPAREN"
PLAYER = "PLAYER"
EVENT = "EVENT"
DEG = "DEG"
COMMA = "COMMA"
IF = "IF"
NONE = "NONE"
VAR = "VAR"
LOCAL_VAR = "LOCAL_VAR"
GAME_VAR = "GAME_VAR"
SAVE_VAR = "SAVE_VAR"
INLINE_VAR = "INLINE_VAR"
PLAIN_STRING = "PLAIN_STRING"
LEGACY_STRING = "LEGACY_STRING"
MINIMESSAGE_STRING = "MINIMESSAGE_STRING"
JSON_STRING = "JSON_STRING"
SAVE_DEFINE = "SAVE_DEFINE"
GAME_DEFINE = "GAME_DEFINE"
LOCAL_DEFINE = "LOCAL_DEFINE"
INLINE_DEFINE = "INLINE_DEFINE"
VAR_DEFINE = "VAR_DEFINE"
COMMENT = "COMMENT"
ENTITY = "ENTITY"
EL = "EL"
OEL = "OEL"
EOF = "EOF"
open_files = dict()
color_codes = {"0": "#000000", "1": "#0000AA", "2": "#00AA00", "3": "#00AAAA", "4": "#AA0000", "5": "#AA00AA",
               "6": "#FFAA00", "7": "#AAAAAA", "8": "#555555", "9": "#5555FF", "a": "#55FF55", "b": "#55FFFF",
               "c": "#FF5555", "d": "#FF55FF", "e": "#FFFF55", "f": "#FFFFFF"}
codes = {"r": "\x1b[0m", "l": "\x1b[1m", "o": "\x1b[3m", "n": "\x1b[4m", "k": "\x1b[40m"}
for k, v in color_codes.items():
    r, g, b = [int(v[i:i + 2], 16) for i in range(1, len(v), 2)]
    codes[k] = f"\x1b[38;2;{r};{g};{b}m"
allowed_symbols = "0123456789abcdefABCDEF"


def minecraft_based_text(text1, ignore_last_symbol=False):
    if ignore_last_symbol is False:
        text1 += "&r"

    def next_symbol(afsd, fdsa):
        if fdsa >= len(afsd):
            return fdsa + 1, None
        return fdsa + 1, afsd[fdsa]

    pos = 0
    msg = ""
    while (s := next_symbol(text1, pos))[1] is not None:
        pos, symbol = s[0], s[1]
        if symbol == "&" and (s := next_symbol(text1, pos))[1] is not None:
            pos, symbol = s[0], s[1]
            if symbol in codes:
                msg += codes[symbol]
                continue
            elif symbol == "#":
                thing = "#"
                if (s := next_symbol(text1, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if not symbol in allowed_symbols:
                        msg += "&" + thing
                        continue
                if (s := next_symbol(text1, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if not symbol in allowed_symbols:
                        msg += "&" + thing
                        continue
                if (s := next_symbol(text1, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if not symbol in allowed_symbols:
                        msg += "&" + thing
                        continue
                if (s := next_symbol(text1, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if not symbol in allowed_symbols:
                        msg += "&" + thing
                        continue
                if (s := next_symbol(text1, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if not symbol in allowed_symbols:
                        msg += "&" + thing
                        continue
                if (s := next_symbol(text1, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if not symbol in allowed_symbols:
                        msg += "&" + thing
                        continue
                a_as, gds, bdsa = [int(thing[i:i + 2], 16) for i in range(1, len(thing), 2)]
                msg += f"\x1b[38;2;{a_as};{gds};{bdsa}m"
                continue
            msg += "&" + symbol
            continue

        msg += symbol
        continue
    return msg


def create_path(now_path, need_path):
    if os.path.isfile(need_path):
        full_path = os.path.abspath(need_path).replace("\\", "/").split("/")
        dir_path = full_path[:len(full_path) - 1]
        dir_path, full_path = "/".join(dir_path), "/".join(full_path)
        return dir_path, full_path
    else:
        a = now_path.replace("\\", "/").split("/")
        a2 = need_path.replace("\\", "/").split("/")
        if a2[0].count(".") == len(a2[0]):
            back = len(a2[0]) - 1
            del a2[0]
        else:
            back = 0

        full_path = a[:len(a) - back]
        full_path.extend(a2)
        dir_path = full_path.copy()
        del dir_path[-1]
        dir_path, full_path = "/".join(dir_path), "/".join(full_path)
        if os.path.isfile(full_path):
            return dir_path, full_path
    return None


def error(error_type, arg="None", start_line=0, end_line=0, offset_pos=0, limit_offset_pos=0, file="None"):
    txt = open_files[file]
    if end_line == 0:
        end_line = start_line
    if limit_offset_pos == 0:
        limit_offset_pos = offset_pos + 1
    if start_line == end_line:
        msg = (f"&cФайл \"{file}\":\n{start_line}:{offset_pos} - " + txt.splitlines()[start_line][
                                                                     :offset_pos] + "&4&n" +
               txt.splitlines()[start_line][offset_pos:limit_offset_pos] + "&r&c" +
               txt.splitlines()[start_line][limit_offset_pos:] + f"\n{error_type} : {arg}")
    else:
        msg = (f"&cText:\n{start_line}:{offset_pos} - " + '\n'.join(txt.splitlines()[start_line:])[:offset_pos] +
               "&4&n" + '\n'.join(txt.splitlines()[start_line:end_line])[:] + "\n" +
               '\n'.join(txt.splitlines()[end_line])[offset_pos:limit_offset_pos] + "&r&c" +
               txt.splitlines()[end_line][limit_offset_pos:] +
               f"\n{error_type} : {arg}")
    print(minecraft_based_text(msg))
    sys.exit()


class Token:
    global open_files

    def __init__(self, token_type, val, start_line=0, end_line=0, offset_pos=0, limit_offset_pos=0, file=""):
        self.type = token_type
        self.value = val
        self.start_line = start_line
        if end_line == 0:
            end_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        if limit_offset_pos == 0:
            limit_offset_pos = offset_pos + 1
        else:
            limit_offset_pos += 1
        self.limit_offset_pos = limit_offset_pos
        self.file = file

    def equals(self, *arg, need=False):
        for i in arg:
            if self.type == i:
                return True
        if need:
            error("SyntaxError", "Ожидался один из токенов (" + ', '.join(arg) + f"), но был получен {self.type}",
                  start_line=self.start_line, end_line=self.end_line,
                  offset_pos=self.offset_pos, limit_offset_pos=self.limit_offset_pos,
                  file=self.file)
        return False

    def __str__(self):
        return f'Token({self.type}, {self.value})'

    def __repr__(self):
        return self.__str__()


class Lexer:
    global open_files

    def __init__(self, file, work_dir=os.getcwd()):
        self.file = file
        self.work_dir = work_dir
        open_files[self.file] = open(self.file, "r", encoding="UTF-8").read()
        self.pos = 0
        self.current_char = self.text()[self.pos]
        self.last_token = Token(OEL, "OEL", start_line=0, offset_pos=0, file=self.file)
        self.line = 0
        self.offset_pos = 0

    def text(self):
        return open_files[self.file]

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text()):
            self.current_char = self.text()[self.pos]
            self.line = self.text()[:self.pos + 1].count("\n")
            if self.line != 0:
                self.offset_pos = len(self.text()[self.text().rfind("\n", 0, self.pos):self.pos - 1])
            else:
                self.offset_pos = self.pos
        else:
            self.current_char = None

    def return_pos(self, pos):
        self.offset_pos -= self.pos - pos
        self.pos = pos
        if self.pos < len(self.text()):
            self.current_char = self.text()[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and (self.current_char.isspace() or self.current_char == ";"):
            if self.current_char == "\n" or self.current_char == "\t":
                self.last_token = Token(OEL, "OEL", start_line=self.line, offset_pos=self.offset_pos, file=self.file)
                self.advance()
                return self.last_token
            elif self.current_char == ";":
                self.last_token = Token(EL, "EL", start_line=self.line, offset_pos=self.offset_pos, file=self.file)
                self.advance()
                return self.last_token
            self.advance()
        return None

    @property
    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace() or self.current_char == ";":
                a = self.skip_whitespace()
                if a is not None:
                    return a
                continue

            if self.current_char.isdigit() or self.current_char == "-" or self.current_char == "+":
                token_value = ""
                start_pos = self.offset_pos
                start_line = self.line
                end_line = self.line
                end_pos = self.offset_pos
                minus = False
                plus = False
                es = False
                dot = False
                if self.current_char == "-":
                    minus = True
                if self.current_char == "+":
                    plus = True
                if self.current_char == ".":
                    token_value = "0"
                    dot = True
                token_type = None
                while self.current_char is not None and self.current_char.isdigit() or (
                        es is False and self.current_char == "e") or (plus is True and self.current_char == "+") or (
                        minus is True and self.current_char == "-") or (
                        dot is False and self.current_char == "." and es is False):
                    if es is False and self.current_char == "e":
                        es = True
                    if dot is False and self.current_char == "." and es is False:
                        dot = True
                    token_value += self.current_char
                    end_line = self.line
                    end_pos = self.offset_pos
                    self.advance()
                    if minus:
                        token_type = MINUS_NUMBER
                    elif plus:
                        token_type = PLUS_NUMBER
                    else:
                        token_type = NUMBER
                try:
                    self.last_token = Token(token_type, int(token_value), start_line=start_line, end_line=end_line,
                                            offset_pos=start_pos, limit_offset_pos=end_pos, file=self.file)
                    return self.last_token
                except:
                    try:
                        self.last_token = Token(token_type, float(token_value), start_line=start_line,
                                                end_line=end_line,
                                                offset_pos=start_pos, limit_offset_pos=end_pos, file=self.file)
                        return self.last_token
                    except:
                        if len(token_value) == 1:
                            self.return_pos(self.pos - 1)
                        if self.current_char is not None and (self.current_char.isspace() or self.current_char == ";"):
                            a = self.skip_whitespace()
                            if a is not None:
                                return a

            if self.current_char == "'":
                start_pos = self.offset_pos
                start_line = self.line
                self.advance()
                string_value = ""
                block_next_symbol = False
                while self.current_char is not None and (self.current_char != '\'' or block_next_symbol is True):
                    if block_next_symbol:
                        block_next_symbol = False
                        string_value += self.current_char
                    elif self.current_char == "\\":
                        block_next_symbol = True
                    else:
                        string_value += self.current_char
                    self.advance()
                if self.current_char == "'":
                    end_line = self.line
                    end_pos = self.offset_pos
                    self.advance()
                    self.last_token = Token(STRING, string_value, start_line=start_line, end_line=end_line,
                                            offset_pos=start_pos, limit_offset_pos=end_pos, file=self.file)
                    return self.last_token
                else:
                    error("IncorrectSymbol", "Строка не была закрыта", start_line=start_line, end_line=self.line,
                          offset_pos=start_pos, limit_offset_pos=self.offset_pos + 1, file=self.file)
            if self.current_char == '"':
                start_pos = self.offset_pos
                start_line = self.line
                self.advance()
                string_value = ""
                block_next_symbol = False
                while self.current_char is not None and (self.current_char != '"' or block_next_symbol is True):
                    if block_next_symbol:
                        block_next_symbol = False
                        string_value += self.current_char
                    elif self.current_char == "\\":
                        block_next_symbol = True
                    else:
                        string_value += self.current_char
                    self.advance()
                if self.current_char == '"':
                    end_line = self.line
                    end_pos = self.offset_pos
                    self.advance()
                    self.last_token = Token(STRING, string_value, start_line=start_line, end_line=end_line,
                                            offset_pos=start_pos, limit_offset_pos=end_pos, file=self.file)
                    return self.last_token
                else:
                    error("IncorrectSymbol", "Строка не была закрыта", start_line=start_line, end_line=self.line,
                          offset_pos=start_pos, limit_offset_pos=self.offset_pos + 1, file=self.file)
            if self.current_char == '`':
                start_pos = self.offset_pos
                start_line = self.line
                self.advance()
                var_name = ""
                block_next_symbol = False
                while self.current_char is not None and (self.current_char != '`' or block_next_symbol is True):
                    if block_next_symbol:
                        block_next_symbol = False
                        var_name += self.current_char
                    elif self.current_char == "\\":
                        block_next_symbol = True
                    else:
                        var_name += self.current_char
                    self.advance()
                if self.current_char == '`':
                    end_line = self.line
                    end_pos = self.offset_pos
                    self.advance()
                    self.last_token = Token(VAR, var_name, start_line=start_line, end_line=end_line,
                                            offset_pos=start_pos,
                                            limit_offset_pos=end_pos, file=self.file)
                    return self.last_token
                else:
                    error("IncorrectSymbol", "Переменная не была закрыта", start_line=start_line, end_line=self.line,
                          offset_pos=start_pos, limit_offset_pos=self.offset_pos + 1, file=self.file)
            if self.current_char == "<":
                start_pos = self.offset_pos
                start_line = self.line
                self.advance()
                selector = ""
                while self.current_char is not None and self.current_char != '>':
                    selector += self.current_char
                    self.advance()
                if self.current_char == '>':
                    end_line = self.line
                    end_pos = self.offset_pos
                    self.advance()
                    self.last_token = Token(SELECTOR, selector, start_line=start_line, end_line=end_line,
                                            offset_pos=start_pos,
                                            limit_offset_pos=end_pos, file=self.file)
                    return self.last_token
                else:
                    error("IncorrectSymbol", "Селектор не был закрыт", start_line=start_line, end_line=self.line,
                          offset_pos=start_pos, limit_offset_pos=self.offset_pos + 1, file=self.file)
            if self.current_char == '=':
                end_line = self.line
                end_pos = self.offset_pos
                self.last_token = Token(ASSIGN, '=', start_line=end_line, offset_pos=end_pos, file=self.file)
                self.advance()
                return self.last_token
            if self.current_char in ('+', '-', '*', '/', '%', '^'):
                action_type = self.current_char
                end_line = self.line
                end_pos = self.offset_pos
                self.advance()
                if action_type == "/" and self.current_char == "/":
                    action_type = "//"
                    end_line = self.line
                    end_pos = self.offset_pos
                    self.advance()
                if action_type == "-" and self.current_char == ">":
                    end_line = self.line
                    end_pos = self.offset_pos
                    self.advance()
                    self.last_token = Token(CYCLE_THING, '->', start_line=end_line, offset_pos=end_pos - 1,
                                            limit_offset_pos=end_pos, file=self.file)
                    return self.last_token
                if self.current_char == "=":
                    if action_type == '+':
                        end_line = self.line
                        end_pos = self.offset_pos
                        self.advance()
                        self.last_token = Token(PLUS_WITH_ASSIGN, '+=', start_line=end_line, offset_pos=end_pos - 1,
                                                limit_offset_pos=end_pos, file=self.file)
                        return self.last_token

                    if action_type == '-':
                        end_line = self.line
                        end_pos = self.offset_pos
                        self.advance()
                        self.last_token = Token(MINUS_WITH_ASSIGN, '-=', start_line=end_line, offset_pos=end_pos - 1,
                                                limit_offset_pos=end_pos, file=self.file)
                        return self.last_token

                    if action_type == '*':
                        end_line = self.line
                        end_pos = self.offset_pos
                        self.advance()
                        self.last_token = Token(MULTIPLY_WITH_ASSIGN, '*=', start_line=end_line, offset_pos=end_pos - 1,
                                                limit_offset_pos=end_pos, file=self.file)
                        return self.last_token

                    if action_type == '/':
                        end_line = self.line
                        end_pos = self.offset_pos
                        self.advance()
                        self.last_token = Token(DIVIDE_WITH_ASSIGN, '/=', start_line=end_line, offset_pos=end_pos - 1,
                                                limit_offset_pos=end_pos, file=self.file)
                        return self.last_token
                    if action_type == '//':
                        end_line = self.line
                        end_pos = self.offset_pos
                        self.advance()
                        self.last_token = Token(INT_DIVIDE_WITH_ASSIGN, '//=', start_line=end_line,
                                                offset_pos=end_pos - 2,
                                                limit_offset_pos=end_pos, file=self.file)
                        return self.last_token

                    if action_type == '%':
                        end_line = self.line
                        end_pos = self.offset_pos
                        self.advance()
                        self.last_token = Token(PR_WITH_ASSIGN, '%=', start_line=end_line, offset_pos=end_pos - 1,
                                                limit_offset_pos=end_pos, file=self.file)
                        return self.last_token

                    if action_type == '^':
                        end_line = self.line
                        end_pos = self.offset_pos
                        self.advance()
                        self.last_token = Token(DEG_WITH_ASSIGN, '^=', start_line=end_line, offset_pos=end_pos - 1,
                                                limit_offset_pos=end_pos, file=self.file)
                        return self.last_token
                else:
                    if action_type == '+':
                        self.last_token = Token(PLUS, '+', start_line=end_line, offset_pos=end_pos, file=self.file)
                        return self.last_token

                    if action_type == '-':
                        self.last_token = Token(MINUS, '-', start_line=end_line, offset_pos=end_pos, file=self.file)
                        return self.last_token

                    if action_type == '*':
                        self.last_token = Token(MULTIPLY, '*', start_line=end_line, offset_pos=end_pos, file=self.file)
                        return self.last_token

                    if action_type == '/':
                        self.last_token = Token(DIVIDE, '/', start_line=end_line, offset_pos=end_pos, file=self.file)
                        return self.last_token
                    if action_type == '//':
                        self.last_token = Token(INT_DIVIDE, '//', start_line=end_line, offset_pos=end_pos - 1,
                                                limit_offset_pos=end_pos, file=self.file)
                        return self.last_token

                    if action_type == '%':
                        self.last_token = Token(PR, '%', start_line=end_line, offset_pos=end_pos, file=self.file)
                        return self.last_token

                    if action_type == '^':
                        self.last_token = Token(DEG, '^', start_line=end_line, offset_pos=end_pos, file=self.file)
                        return self.last_token
            if self.current_char == '#':
                while self.current_char is not None:
                    if self.current_char == "\n" or self.current_char == "\t":
                        self.last_token = Token(OEL, "OEL", start_line=self.line,
                                                offset_pos=self.offset_pos, file=self.file)
                        self.advance()
                        return self.last_token
                    self.advance()
                self.last_token = Token(EOF, None, start_line=self.line, offset_pos=self.offset_pos,
                                        file=self.file)
                return Token(EOF, None)
            if self.current_char == '(':
                self.last_token = Token(LPAREN, '(', start_line=self.line, offset_pos=self.offset_pos, file=self.file)
                self.advance()
                return self.last_token
            if self.current_char == ':':
                self.last_token = Token(COLON, ':', start_line=self.line, offset_pos=self.offset_pos, file=self.file)
                self.advance()
                return self.last_token
            if self.current_char == ')':
                self.last_token = Token(RPAREN, ')', start_line=self.line, offset_pos=self.offset_pos, file=self.file)
                self.advance()
                return self.last_token
            if self.current_char == '[':
                self.last_token = Token(LSPAREN, '[', start_line=self.line, offset_pos=self.offset_pos, file=self.file)
                self.advance()
                return self.last_token
            if self.current_char == ']':
                self.last_token = Token(RSPAREN, ']', start_line=self.line, offset_pos=self.offset_pos, file=self.file)
                self.advance()
                return self.last_token
            if self.current_char == '{':
                self.last_token = Token(LCPAREN, '{', start_line=self.line, offset_pos=self.offset_pos, file=self.file)
                self.advance()
                return self.last_token
            if self.current_char == '}':
                self.last_token = Token(RCPAREN, '}', start_line=self.line, offset_pos=self.offset_pos, file=self.file)
                self.advance()
                return self.last_token
            if self.current_char == ',':
                self.last_token = Token(COMMA, ',', start_line=self.line, offset_pos=self.offset_pos, file=self.file)
                self.advance()
                return self.last_token
            if self.current_char == ".":
                self.last_token = Token(DOT, '.', start_line=self.line, offset_pos=self.offset_pos, file=self.file)
                self.advance()
                return self.last_token
            if self.current_char.isalpha() or self.current_char == "_":
                token_value = ""
                start_pos = self.offset_pos
                start_line = self.line
                end_line = start_line
                end_pos = start_pos
                while self.current_char is not None and (
                        self.current_char.isalpha() or self.current_char.isdigit() or self.current_char == "_"):
                    token_value += self.current_char
                    end_line = self.line
                    end_pos = self.offset_pos
                    self.advance()

                if self.current_char == '`' and token_value in ("l", "local", "g", "game", "s", "save", "i", "inline"):
                    self.advance()
                    var_name = ""
                    block_next_symbol = False
                    while self.current_char is not None and (self.current_char != '`' or block_next_symbol is True):
                        if block_next_symbol:
                            block_next_symbol = False
                            var_name += self.current_char
                        elif self.current_char == "\\":
                            block_next_symbol = True
                        else:
                            var_name += self.current_char
                        self.advance()
                    if self.current_char == '`':
                        end_line = self.line
                        end_pos = self.offset_pos
                        self.advance()
                        if token_value in ("l", "local"):
                            self.last_token = Token(LOCAL_VAR, var_name, start_line=start_line, end_line=end_line,
                                                    offset_pos=start_pos,
                                                    limit_offset_pos=end_pos, file=self.file)
                            return self.last_token
                        if token_value in ("g", "game"):
                            self.last_token = Token(GAME_VAR, var_name, start_line=start_line, end_line=end_line,
                                                    offset_pos=start_pos,
                                                    limit_offset_pos=end_pos, file=self.file)
                            return self.last_token
                        if token_value in ("s", "save"):
                            self.last_token = Token(SAVE_VAR, var_name, start_line=start_line, end_line=end_line,
                                                    offset_pos=start_pos,
                                                    limit_offset_pos=end_pos, file=self.file)
                            return self.last_token
                        if token_value in ("i", "inline"):
                            self.last_token = Token(INLINE_VAR, var_name, start_line=start_line, end_line=end_line,
                                                    offset_pos=start_pos,
                                                    limit_offset_pos=end_pos, file=self.file)
                            return self.last_token
                    else:
                        error("IncorrectSymbol", "Переменная не была закрыта", start_line=start_line,
                              end_line=self.line, offset_pos=start_pos, limit_offset_pos=self.offset_pos,
                              file=self.file)
                if self.current_char == "\"" and token_value in (
                        "p", "plain", "l", "legacy", "m", "minimessage", "j", "json"):
                    self.advance()
                    string_value = ""
                    block_next_symbol = False
                    while self.current_char is not None and (self.current_char != '"' or block_next_symbol is True):
                        if block_next_symbol:
                            block_next_symbol = False
                            string_value += self.current_char
                        elif self.current_char == "\\":
                            block_next_symbol = True
                        else:
                            string_value += self.current_char
                        self.advance()
                    if self.current_char == '"':
                        end_line = self.line
                        end_pos = self.offset_pos
                        self.advance()
                        if token_value in ("p", "plain"):
                            self.last_token = Token(PLAIN_STRING, string_value, start_line=start_line,
                                                    end_line=end_line,
                                                    offset_pos=start_pos, limit_offset_pos=end_pos, file=self.file)
                            return self.last_token
                        if token_value in ("l", "legacy"):
                            self.last_token = Token(LEGACY_STRING, string_value, start_line=start_line,
                                                    end_line=end_line,
                                                    offset_pos=start_pos, limit_offset_pos=end_pos, file=self.file)
                            return self.last_token
                        if token_value in ("m", "minimessage"):
                            self.last_token = Token(MINIMESSAGE_STRING, string_value, start_line=start_line,
                                                    end_line=end_line,
                                                    offset_pos=start_pos, limit_offset_pos=end_pos, file=self.file)
                            return self.last_token
                        if token_value in ("j", "json"):
                            self.last_token = Token(JSON_STRING, string_value, start_line=start_line,
                                                    end_line=end_line,
                                                    offset_pos=start_pos, limit_offset_pos=end_pos, file=self.file)
                            return self.last_token
                    else:
                        error("IncorrectSymbol", "Строка не была закрыта", start_line=start_line, end_line=self.line,
                              offset_pos=start_pos, limit_offset_pos=self.offset_pos, file=self.file)
                if self.current_char == "\'" and token_value in (
                        "p", "plain", "l", "legacy", "m", "minimessage", "j", "json"):
                    self.advance()
                    string_value = ""
                    block_next_symbol = False
                    while self.current_char is not None and (self.current_char != '\'' or block_next_symbol is True):
                        if block_next_symbol:
                            block_next_symbol = False
                            string_value += self.current_char
                        elif self.current_char == "\\":
                            block_next_symbol = True
                        else:
                            string_value += self.current_char
                        self.advance()
                    if self.current_char == '\'':
                        end_line = self.line
                        end_pos = self.offset_pos
                        self.advance()
                        if token_value in ("p", "plain"):
                            self.last_token = Token(PLAIN_STRING, string_value, start_line=start_line,
                                                    end_line=end_line,
                                                    offset_pos=start_pos, limit_offset_pos=end_pos, file=self.file)
                            return self.last_token
                        if token_value in ("l", "legacy"):
                            self.last_token = Token(LEGACY_STRING, string_value, start_line=start_line,
                                                    end_line=end_line,
                                                    offset_pos=start_pos, limit_offset_pos=end_pos, file=self.file)
                            return self.last_token
                        if token_value in ("m", "minimessage"):
                            self.last_token = Token(MINIMESSAGE_STRING, string_value, start_line=start_line,
                                                    end_line=end_line,
                                                    offset_pos=start_pos, limit_offset_pos=end_pos, file=self.file)
                            return self.last_token
                        if token_value in ("j", "json"):
                            self.last_token = Token(JSON_STRING, string_value, start_line=start_line,
                                                    end_line=end_line,
                                                    offset_pos=start_pos, limit_offset_pos=end_pos, file=self.file)
                            return self.last_token
                    else:
                        error("IncorrectSymbol", "Строка не была закрыта", start_line=start_line, end_line=self.line,
                              offset_pos=start_pos, limit_offset_pos=self.offset_pos, file=self.file)
                if self.current_char == "<" and token_value == "event":
                    self.advance()
                    event_name = ""
                    while self.current_char is not None and self.current_char != '>':
                        event_name += self.current_char
                        self.advance()
                    if self.current_char == '>':
                        end_line = self.line
                        end_pos = self.offset_pos
                        self.advance()
                        self.last_token = Token(EVENT, event_name, start_line=start_line, end_line=end_line,
                                                offset_pos=start_pos,
                                                limit_offset_pos=end_pos, file=self.file)
                        return self.last_token
                    else:
                        error("IncorrectSymbol", "Значение ивента не было закрыто", start_line=start_line,
                              end_line=self.line,
                              offset_pos=start_pos, limit_offset_pos=self.offset_pos, file=self.file)
                if self.current_char == ":" and token_value in (
                        "value", "player", "variable", "code", "repeat", "entity", "world", "select", "controller"):
                    act = token_value
                    self.advance()
                    if self.current_char == ":":
                        self.advance()
                        if self.current_char.isalpha():
                            sub_action = ""
                            while (self.current_char is not None
                                   and (self.current_char.isalpha()
                                        or self.current_char.isdigit() or self.current_char == "_")):
                                sub_action += self.current_char
                                end_line = self.line
                                end_pos = self.offset_pos
                                self.advance()
                            self.last_token = Token(act.upper(), sub_action, start_line=start_line,
                                                    end_line=end_line,
                                                    offset_pos=start_pos, limit_offset_pos=end_pos, file=self.file)
                            return self.last_token
                if token_value == "if":
                    self.last_token = Token(IF, "if", start_line=start_line, end_line=end_line, offset_pos=start_pos,
                                            limit_offset_pos=end_pos, file=self.file)
                    return self.last_token
                elif token_value == "else":
                    self.last_token = Token(ELSE, "ELSE", start_line=start_line, end_line=end_line,
                                            offset_pos=start_pos,
                                            limit_offset_pos=end_pos, file=self.file)
                    return self.last_token
                elif token_value == "not":
                    self.last_token = Token(NOT, "NOT", start_line=start_line, end_line=end_line, offset_pos=start_pos,
                                            limit_offset_pos=end_pos, file=self.file)
                    return self.last_token
                elif token_value == "function":
                    self.last_token = Token(FUNCTION, "function", start_line=start_line, end_line=end_line,
                                            offset_pos=start_pos,
                                            limit_offset_pos=end_pos, file=self.file)
                    return self.last_token
                elif token_value == "None":
                    self.last_token = Token(NONE, "", start_line=start_line, end_line=end_line, offset_pos=start_pos,
                                            limit_offset_pos=end_pos, file=self.file)
                    return self.last_token
                elif token_value == "process":
                    self.last_token = Token(PROCESS, "process", start_line=start_line, end_line=end_line,
                                            offset_pos=start_pos,
                                            limit_offset_pos=end_pos, file=self.file)
                    return self.last_token
                elif token_value == "location":
                    self.last_token = Token(LOCATION, "location", start_line=start_line, end_line=end_line,
                                            offset_pos=start_pos,
                                            limit_offset_pos=end_pos, file=self.file)
                    return self.last_token
                elif token_value == "sound":
                    self.last_token = Token(SOUND, "sound", start_line=start_line, end_line=end_line,
                                            offset_pos=start_pos,
                                            limit_offset_pos=end_pos, file=self.file)
                    return self.last_token
                elif token_value == "vector":
                    self.last_token = Token(VECTOR, "vector", start_line=start_line, end_line=end_line,
                                            offset_pos=start_pos,
                                            limit_offset_pos=end_pos, file=self.file)
                    return self.last_token
                elif token_value == "particle":
                    self.last_token = Token(PARTICLE, "particle", start_line=start_line, end_line=end_line,
                                            offset_pos=start_pos,
                                            limit_offset_pos=end_pos, file=self.file)
                    return self.last_token
                elif token_value == "item":
                    self.last_token = Token(ITEM, "item", start_line=start_line, end_line=end_line,
                                            offset_pos=start_pos,
                                            limit_offset_pos=end_pos, file=self.file)
                    return self.last_token
                elif token_value == "potion":
                    self.last_token = Token(POTION, "potion", start_line=start_line, end_line=end_line,
                                            offset_pos=start_pos,
                                            limit_offset_pos=end_pos, file=self.file)
                    return self.last_token
                elif token_value == "import":
                    self.last_token = Token(IMPORT, "import", start_line=start_line, end_line=end_line,
                                            offset_pos=start_pos,
                                            limit_offset_pos=end_pos, file=self.file)
                    return self.last_token
                elif token_value == "save":
                    self.last_token = Token(SAVE_DEFINE, "save", start_line=start_line, end_line=end_line,
                                            offset_pos=start_pos,
                                            limit_offset_pos=end_pos, file=self.file)
                    return self.last_token
                elif token_value == "game":
                    self.last_token = Token(GAME_DEFINE, "game", start_line=start_line, end_line=end_line,
                                            offset_pos=start_pos,
                                            limit_offset_pos=end_pos, file=self.file)
                    return self.last_token
                elif token_value == "local":
                    self.last_token = Token(LOCAL_DEFINE, "local", start_line=start_line, end_line=end_line,
                                            offset_pos=start_pos,
                                            limit_offset_pos=end_pos, file=self.file)
                    return self.last_token
                elif token_value == "inline":
                    self.last_token = Token(INLINE_DEFINE, "inline", start_line=start_line, end_line=end_line,
                                            offset_pos=start_pos,
                                            limit_offset_pos=end_pos, file=self.file)
                    return self.last_token
                elif token_value == "var":
                    self.last_token = Token(VAR_DEFINE, "var", start_line=start_line, end_line=end_line,
                                            offset_pos=start_pos,
                                            limit_offset_pos=end_pos, file=self.file)
                    return self.last_token
                else:
                    self.last_token = Token(VAR, token_value, start_line=start_line, end_line=end_line,
                                            offset_pos=start_pos,
                                            limit_offset_pos=end_pos, file=self.file)
                    return self.last_token
            error("SyntaxError", f"Неизвестный символ &4&n{self.current_char}", start_line=self.line,
                  offset_pos=self.offset_pos, file=self.file)
        self.last_token = Token(EOF, None, start_line=self.line, offset_pos=self.offset_pos, file=self.file)
        return self.last_token


def minecraft_text(text1):
    def next_symbol(afsd, fdsa):
        if fdsa >= len(afsd):
            return fdsa + 1, None
        return fdsa + 1, afsd[fdsa]

    pos = 0
    msg = ""
    full_msg = {"text": "", "extra": []}
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
                    full_msg["extra"].append(old_msg)
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
                    full_msg["extra"].append(old_msg)
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
                    full_msg["extra"].append(old_msg)
                    msg = ""
                underlined = True
                continue
            elif symbol == "m":
                if msg != "":
                    old_msg = {"text": msg, "italic": italic, "obfuscated": obfuscated, "underlined": underlined,
                               "strikethrough": strikethrough, "color": color, "bold": bold}
                    full_msg["extra"].append(old_msg)
                    msg = ""
                strikethrough = True
                continue
            elif symbol == "o":
                if msg != "":
                    old_msg = {"text": msg, "italic": italic, "obfuscated": obfuscated, "underlined": underlined,
                               "strikethrough": strikethrough, "color": color, "bold": bold}
                    full_msg["extra"].append(old_msg)
                    msg = ""
                italic = True
                continue
            elif symbol == "l":
                if msg != "":
                    old_msg = {"text": msg, "italic": italic, "obfuscated": obfuscated, "underlined": underlined,
                               "strikethrough": strikethrough, "color": color, "bold": bold}
                    full_msg["extra"].append(old_msg)
                    msg = ""
                bold = True
                continue
            elif symbol == "k":
                if msg != "":
                    old_msg = {"text": msg, "italic": italic, "obfuscated": obfuscated, "underlined": underlined,
                               "strikethrough": strikethrough, "color": color, "bold": bold}
                    full_msg["extra"].append(old_msg)
                    msg = ""
                obfuscated = True
                continue
            elif symbol == "#":
                thing = "#"
                if (s := next_symbol(text1, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if not symbol in allowed_symbols:
                        msg += "&" + thing
                        continue
                if (s := next_symbol(text1, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if not symbol in allowed_symbols:
                        msg += "&" + thing
                        continue
                if (s := next_symbol(text1, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if not symbol in allowed_symbols:
                        msg += "&" + thing
                        continue
                if (s := next_symbol(text1, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if not symbol in allowed_symbols:
                        msg += "&" + thing
                        continue
                if (s := next_symbol(text1, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if not symbol in allowed_symbols:
                        msg += "&" + thing
                        continue
                if (s := next_symbol(text1, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if not symbol in allowed_symbols:
                        msg += "&" + thing
                        continue
                if msg != "":
                    old_msg = {"text": msg, "italic": italic, "obfuscated": obfuscated, "underlined": underlined,
                               "strikethrough": strikethrough, "color": color, "bold": bold}
                    full_msg["extra"].append(old_msg)
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
        full_msg["extra"].append(old_msg)
    return full_msg


def fix_operations_len(operations, limit=43):
    global global_func_count, global_count

    def get_operations(ops):
        cont = 0
        for op in ops:
            cont += 1
            op["weight"] = 1
            if "operations" in op:
                op_opers, cont_op = get_operations(op["operations"])
                op["operations"] = op_opers
                cont += cont_op + 1
                op["weight"] += cont_op + 1
        return ops, cont

    def remove_weight(ops):
        for op in ops:
            if "weight" in op:
                del op["weight"]
            if "operations" in op:
                op["operations"] = remove_weight(op["operations"])
        return ops

    operations, op_count = get_operations(operations)
    additional_events = []
    if op_count > limit:

        def spl(ops, curr_limit=43, lim=43):
            global global_func_count, global_count
            additional2 = []
            i = 0
            cur_weight = 0
            new_ops = []
            while i < len(ops):
                op = ops[i]
                weight = op["weight"]
                next_weight = cur_weight + weight
                if next_weight >= curr_limit - 1:
                    if weight <= lim:
                        if i != 0:
                            save_ops = ops[:i]
                            ops = ops[i:]
                            i = 0
                            cur_weight = 1
                            new_ops.append(save_ops)
                        else:
                            cur_weight = 1
                            new_ops.append(ops)
                            ops = []
                    else:
                        next_l = curr_limit - (cur_weight + 3 + len(ops))
                        if next_l <= 0:
                            save_ops, additional3, thing2 = spl(op["operations"], curr_limit=lim - 3, lim=lim)
                            global_func_count += 1
                            global_count += 1
                            additional2.extend(additional3)
                            ops[i] = {"action": "call_function", "values": [{"name": "function_name",
                                                                             "value": {"type": "text",
                                                                                       "text": f"jmcc.{global_func_count}",
                                                                                       "parsing": "legacy"}}]}
                            additional2.append(
                                {"type": "function", "position": global_count, "operations": remove_weight([op]),
                                 "is_hidden": False, "name": f"jmcc.{global_func_count}"})
                            cur_weight += 1
                        else:
                            save_ops, additional3, thing2 = spl(op["operations"], curr_limit=next_l, lim=lim)
                            additional2.extend(additional3)
                            if cur_weight + thing2 + 2 > curr_limit:
                                cur_weight += 1
                                global_func_count += 1
                                global_count += 1
                                ops[i] = {"action": "call_function", "values": [{"name": "function_name",
                                                                                 "value": {"type": "text",
                                                                                           "text": f"jmcc.{global_func_count}",
                                                                                           "parsing": "legacy"}}]}
                                additional2.append(
                                    {"type": "function", "position": global_count, "operations": remove_weight([op]),
                                     "is_hidden": False, "name": f"jmcc.{global_func_count}"})
                            else:
                                op["operations"] = save_ops
                                cur_weight += thing2 + 2
                        i += 1
                else:
                    cur_weight = next_weight
                    i += 1
            if len(ops) > 0:
                new_ops.append(ops)
            else:
                new_ops.insert(0, [])
            for i in range(1, len(new_ops)):
                global_func_count += 1
                global_count += 1
                new_ops[i - 1].append({"action": "call_function", "values": [{"name": "function_name",
                                                                              "value": {"type": "text",
                                                                                        "text": f"jmcc.{global_func_count}",
                                                                                        "parsing": "legacy"}}]})
                additional2.append(
                    {"type": "function", "position": global_count, "operations": remove_weight(new_ops[i]),
                     "is_hidden": False, "name": f"jmcc.{global_func_count}"})
            return remove_weight(new_ops[0]), additional2, cur_weight

        operations, additional_events, thing = spl(operations, lim=limit, curr_limit=limit)
    else:
        operations = remove_weight(operations)
    return operations, additional_events


class assign:
    def __init__(self, key, val, start_line=None, end_line=None, offset_pos=None, limit_offset_pos=None, file=None):
        self.key = key
        self.value = val
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file

    def __str__(self):
        return f'assign({self.key}={self.value})'

    def __repr__(self):
        return self.__str__()


class args:
    def __init__(self, arg_list=None, positional=None, unpositional=None, start_line=None, end_line=None,
                 offset_pos=None,
                 limit_offset_pos=None, file=None, assigning=None, origin=None, lamba=None):
        self.args = dict()
        if unpositional is None:
            unpositional = []
        if positional is None:
            positional = []
        self.positional = positional
        self.unpositional = unpositional
        self.arg_list = arg_list
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        self.assigning = assigning
        self.origin = origin
        self.lamba = lamba

    def get_args(self):
        self.args = dict()
        if self.arg_list is not None:
            dect = [None] * len(self.arg_list)
            for i in self.unpositional:
                if i.key == "assigning" and self.assigning is not None:
                    for i1 in range(len(i.value)):
                        key = list(self.assigning[i1].keys())[0]
                        val = i.value[i1]
                        if not isinstance(key, var):
                            if key in self.arg_list:
                                dect[self.arg_list.index(key)] = val
                            else:
                                error("UnexistsArgument", f"Указан несуществующий аргумент : {i.value[i1]}",
                                      i.value[i1].start_line, i.value[i1].end_line, i.value[i1].offset_pos,
                                      i.value[i1].limit_offset_pos, i.value[i1].file)
                        else:
                            dect[self.arg_list.index(key.name)] = val
                    continue
                elif i.key == "origin" and self.origin is not None:
                    i.key = self.origin
                elif i.key == "lambda" and self.lamba is not None:
                    i.key = self.lamba
                    for i1 in range(len(i.value)):
                        key = list(self.lamba[i1].keys())[0]
                        val = i.value[i1]
                        if not isinstance(key, var):
                            if key in self.arg_list:
                                dect[self.arg_list.index(key)] = val
                            else:
                                error("UnexistsArgument", f"Указан несуществующий аргумент : {i.value[i1]}",
                                      i.value[i1].start_line, i.value[i1].end_line, i.value[i1].offset_pos,
                                      i.value[i1].limit_offset_pos, i.value[i1].file)
                        else:
                            dect[self.arg_list.index(key.name)] = val
                    continue
                if not isinstance(i.key, var):
                    if i.key in self.arg_list:
                        dect[self.arg_list.index(i.key)] = i.value
                    else:
                        error("UnexistsArgument", f"Указан несуществующий аргумент : {i.key}", i.start_line, i.end_line,
                              i.offset_pos, i.limit_offset_pos, i.file)
                else:
                    dect[self.arg_list.index(i.key.name)] = i.value
            i1 = 0
            if len(dect) != 0:
                for i in self.positional:
                    while dect[i1] is not None:
                        i1 += 1
                    dect[i1] = i
                for i in range(len(dect)):
                    self.args[self.arg_list[i]] = dect[i]
        return self.args

    def __str__(self):
        return f'args(unpos={self.unpositional},pos={self.positional})'

    def __repr__(self):
        return self.__str__()


class text:
    def __init__(self, txt, text_type="legacy", start_line=None, end_line=None, offset_pos=None, limit_offset_pos=None,
                 file=None):
        self.text_type = text_type
        self.text = txt
        self.type = "text"
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file

    def __str__(self):
        return f'text({self.text}, {self.text_type})'

    def __repr__(self):
        return self.__str__()

    def json(self, normal=False):
        if not normal:
            return {"type": "text", "text": self.text, "parsing": self.text_type}
        return self.text


class number:
    def __init__(self, val, start_line=None, end_line=None, offset_pos=None, limit_offset_pos=None, file=None):
        self.type = "number"
        self.value = val
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file

    def __str__(self):
        return f'number({self.value})'

    def __repr__(self):
        return self.__str__()

    def json(self, normal=False, in_text=False):
        if in_text:
            return str(self.value)
        if not normal:
            return {"type": "number", "number": self.value}
        return self.value


class lst:
    def __init__(self, vals, start_line=None, end_line=None, offset_pos=None, limit_offset_pos=None, file=None):
        self.type = "array"
        self.values = vals
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file

    def __str__(self):
        return "lst(" + ",".join(list(map(str, self.values))) + ")"

    def __repr__(self):
        return self.__str__()

    def json(self, normal=False, full_normal=False, with_ret=False):
        if with_ret:
            additional_events = []
            vals = []
            for i in self.values:
                if isinstance(i, lst):
                    val, additional2 = i.json(normal=full_normal, full_normal=full_normal)
                elif isinstance(i, dct):
                    val, additional2 = i.json(normal=full_normal, full_normal=full_normal)
                else:
                    val, additional2 = i.json(normal=full_normal)
                additional_events.extend(additional2)
                vals.append(val)
            if not normal and not full_normal:
                return {"type": "array", "values": vals}, additional_events
            return vals, additional_events
        if not normal and not full_normal:
            return {"type": "array", "values": [i.json() for i in self.values]}
        vals = []
        for i in self.values:
            if isinstance(i, lst):
                vals.append(i.json(normal=full_normal, full_normal=full_normal))
            elif isinstance(i, dct):
                vals.append(i.json(normal=full_normal, full_normal=full_normal))
            else:
                vals.append(i.json(normal=full_normal))
        return vals


class dct:
    def __init__(self, keys, vals, start_line=None, end_line=None, offset_pos=None, limit_offset_pos=None, file=None):
        self.type = "map"
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        self.keys = keys
        self.values = vals

    def __str__(self):
        return "dct(" + ",".join([str(self.keys[i]) + ":" + str(self.values[i]) for i in range(len(self.keys))]) + ")"

    def __repr__(self):
        return self.__str__()

    def json(self, normal=True, full_normal=False):
        if not normal:
            return None
        dect = dict()
        for i in range(len(self.keys)):
            dect[self.keys[i].json(normal=True, full_normal=full_normal) if type(self.keys[i]) in (lst, dct) else
            self.keys[i].json(normal=True)] = self.values[i].json(normal=True, full_normal=full_normal) \
                if type(self.values[i]) in (lst, dct) else self.values[i].json(normal=True)
        return dect


def check(checking=None, *arg):
    if checking is None:
        return checking
    for i2 in arg:
        if checking.type == i2:
            return checking
    error("TypeError", "Ожидался объект типа (" + ",".join(arg) + f"), но был получен {checking.type}",
          start_line=checking.start_line, end_line=checking.end_line, offset_pos=checking.offset_pos,
          limit_offset_pos=checking.limit_offset_pos, file=checking.file)


class item:
    def __init__(self, item_id=None, name=None, count=None, lore=None, nbt=None, arg=None, start_line=None,
                 end_line=None,
                 offset_pos=None, limit_offset_pos=None, file=None):
        self.type = "item"
        if arg is not None:
            arg.arg_list = ["id", "name", "count", "lore", "nbt"]
            arg = arg.get_args()
            for k1, v1 in arg.items():
                if v1 is not None and v1.type == "variable" and v1.var_type == "INLINE":
                    arg[k1] = symbol_table["inlines"][v1.name]
            item_id = arg["id"]
            name = arg["name"]
            count = arg["count"]
            if count is None:
                count = number(1)
            lore = arg["lore"]
            nbt = arg["nbt"]
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        self.id = check(item_id, "variable", "text")
        self.name = check(name, "text")
        self.count = check(count, "number")
        self.lore = check(lore, "text", "array")
        self.nbt = check(nbt, "map")

    def __str__(self):
        return f'item({self.id},{self.name},{self.lore},{self.nbt})'

    def __repr__(self):
        return self.__str__()

    def json(self, normal=None):
        a = {"id": self.id.json(normal=True), "Count": self.count.json(normal=True)}
        if self.nbt is not None:
            a["tag"] = self.nbt.json(full_normal=True)
        if self.name is not None or self.lore is not None:
            if not "tag" in a:
                a["tag"] = {}
            if not "display" in a:
                a["tag"]["display"] = {}
            if self.name is not None:
                a["tag"]["display"]["Name"] = json.dumps(minecraft_text(self.name.json(normal=True)))
            if self.lore is not None:
                if self.lore.type != "array":
                    lore = self.lore.json(full_normal=True, normal=True).split("\\n")
                else:
                    lore = self.lore.json(full_normal=True, normal=True)
                a["tag"]["display"]["Lore"] = list(map(json.dumps, map(minecraft_text, lore)))
        return {"type": "item", "item": json.dumps(a)}


class location:
    def __init__(self, x=None, y=None, z=None, yaw=number(0), pitch=number(0), arg=None, start_line=None,
                 end_line=None, offset_pos=None, limit_offset_pos=None, file=None):
        self.type = "location"
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        if arg is not None:
            arg.arg_list = ["x", "y", "z", "yaw", "pitch"]
            arg = arg.get_args()
            for k1, v1 in arg.items():
                if v1 is not None and v1.type == "variable" and v1.var_type == "INLINE":
                    arg[k1] = symbol_table["variables"][v1.name][1]
            x = arg["x"]
            y = arg["y"]
            z = arg["z"]
            yaw = arg["yaw"]
            if yaw is None:
                yaw = number(0)
            pitch = arg["pitch"]
            if pitch is None:
                pitch = number(0)
        self.x = check(x, "variable", "number")
        self.y = check(y, "number")
        self.z = check(z, "number")
        self.yaw = check(yaw, "number")
        self.pitch = check(pitch, "number")

    def __str__(self):
        return f'location({self.x},{self.y},{self.z},{self.yaw},{self.pitch})'

    def __repr__(self):
        return self.__str__()

    def json(self, normal=None):
        return {"type": "location", "x": self.x.json(normal=True), "y": self.y.json(normal=True),
                "z": self.z.json(normal=True), "yaw": self.yaw.json(normal=True), "pitch": self.pitch.json(normal=True)}


class vector:
    def __init__(self, x=None, y=None, z=None, arg=None, start_line=None, end_line=None, offset_pos=None,
                 limit_offset_pos=None, file=None):
        self.type = "vector"
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        if arg is not None:
            arg.arg_list = ["x", "y", "z"]
            arg = arg.get_args()
            for k1, v1 in arg.items():
                if v1 is not None and v1.type == "variable" and v1.var_type == "INLINE":
                    arg[k1] = symbol_table["inlines"][v1.name]
            x = arg["x"]
            y = arg["y"]
            z = arg["z"]
        self.x = check(x, "number")
        self.y = check(y, "number")
        self.z = check(z, "number")

    def __str__(self):
        return f'vector({self.x},{self.y},{self.z})'

    def __repr__(self):
        return self.__str__()

    def json(self, normal=None):
        return {"type": "vector", "x": self.x.json(normal=True), "y": self.y.json(normal=True),
                "z": self.z.json(normal=True)}


class potion:
    def __init__(self, potion_type=None, amplifier=number(0), duration=number(0), arg=None, start_line=None,
                 end_line=None,
                 offset_pos=None, limit_offset_pos=None, file=None):
        self.type = "potion"
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        if arg is not None:
            arg.arg_list = ["potion", "amplifier", "duration"]
            arg = arg.get_args()
            potion_type = arg["potion"]
            amplifier = arg["amplifier"]
            if amplifier is None:
                amplifier = number(0)
            duration = arg["duration"]
            if duration is None:
                duration = number(0)
        self.potion = check(potion_type, "text")
        self.amplifier = check(amplifier, "number")
        self.duration = check(duration, "number")

    def __str__(self):
        return f'potion({self.potion},{self.amplifier},{self.duration})'

    def __repr__(self):
        return self.__str__()

    def json(self, normal=None):
        return {"type": "potion", "potion": self.potion.json(normal=True),
                "amplifier": self.amplifier.json(normal=True), "duration": self.duration.json(normal=True)}


class sound:
    def __init__(self, sound_id=None, volume=number(0), pitch=number(0), variation=text(""), source=text("MASTER"),
                 arg=None, start_line=None, end_line=None,
                 offset_pos=None, limit_offset_pos=None, file=None):
        self.type = "sound"
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        if arg is not None:
            arg.arg_list = ["sound", "volume", "pitch", "variation", "source"]
            arg = arg.get_args()
            for k1, v1 in arg.items():
                if v1 is not None and v1.type == "variable" and v1.var_type == "INLINE":
                    arg[k1] = symbol_table["inlines"][v1.name]
            sound_id = arg["sound"]
            volume = arg["volume"]
            if volume is None:
                volume = number(0)
            pitch = arg["pitch"]
            if pitch is None:
                pitch = number(0)
            variation = arg["variation"]
            if variation is None:
                variation = text("")
        self.sound = check(sound_id, "text")
        self.volume = check(volume, "number")
        self.pitch = check(pitch, "number")
        self.variation = check(variation, "text")
        self.source = check(source, "text")

    def __str__(self):
        return f'sound({self.sound},{self.volume},{self.pitch})'

    def __repr__(self):
        return self.__str__()

    def json(self, normal=None):
        return {"type": "sound", "sound": self.sound.json(normal=True), "volume": self.volume.json(normal=True),
                "pitch": self.pitch.json(normal=True), "variation": self.variation.json(normal=True),
                "source": self.source.json(normal=True)}


class particle:
    def __init__(self, particle_type=None, count=number(0), spread_x=number(0), spread_y=number(0), motion_x=number(0),
                 motion_y=number(0), motion_z=number(0), material=None, color=None, arg=None, size=None,
                 start_line=None,
                 end_line=None,
                 offset_pos=None, limit_offset_pos=None, file=None):
        self.type = "sound"
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        if arg is not None:
            arg.arg_list = ["particle", "count", "spread_x", "spread_y", "motion_x", "motion_y", "motion_z",
                            "material", "color", "size"]
            arg = arg.get_args()
            for k1, v1 in arg.items():
                if v1 is not None and v1.type == "variable" and v1.var_type == "INLINE":
                    arg[k1] = symbol_table["inlines"][v1.name]
            particle_type = arg["particle"]
            count = arg["count"]
            if count is None:
                count = number(1)
            spread_x = arg["spread_x"]
            if spread_x is None:
                spread_x = number(0)
            spread_y = arg["spread_y"]
            if spread_y is None:
                spread_y = number(0)
            motion_x = arg["motion_x"]
            if motion_x is None:
                motion_x = number(0)
            motion_y = arg["motion_y"]
            if motion_y is None:
                motion_y = number(0)
            motion_z = arg["motion_z"]
            if motion_z is None:
                motion_z = number(0)
            material = arg["material"]
            color = arg["color"]
            size = arg["size"]
            if size is None:
                size = number(0)
        self.particle = check(particle_type, "text")
        self.count = check(count, "number")
        self.spread_x = check(spread_x, "number")
        self.spread_y = check(spread_y, "number")
        self.motion_x = check(motion_x, "number")
        self.motion_y = check(motion_y, "number")
        self.motion_z = check(motion_z, "number")
        self.material = check(material, "text")
        self.color = check(color, "text")
        self.size = check(size, "number")

    def __str__(self):
        return (f'particle({self.particle},{self.count},{self.spread_x},'
                f'{self.spread_y},{self.motion_x},{self.motion_y},{self.material},{self.color},{self.size})')

    def __repr__(self):
        return self.__str__()

    def json(self, normal=None):
        a = {"type": "particle", "particle_type": self.particle.json(normal=True),
             "count": self.count.json(normal=True), "first_spread": self.spread_x.json(normal=True),
             "second_spread": self.spread_y.json(normal=True), "x_motion": self.motion_x.json(normal=True),
             "y_motion": self.motion_y.json(normal=True), "z_motion": self.motion_z.json(normal=True)}
        if self.color is not None:
            a["color"] = self.color.json(normal=True)
        if self.material is not None:
            a["material"] = self.material.json(normal=True)
        if self.size is not None:
            a["size"] = self.size.json(normal=True)
        return a


class value:
    def __init__(self, name, selector=None, start_line=None, end_line=None, offset_pos=None, limit_offset_pos=None,
                 file=None):
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        if not name in values:
            error("UnexistsValue", f"Указано несуществующее игровое значение {name}", start_line, end_line, offset_pos,
                  limit_offset_pos, file)
        self.name = name
        if selector is None:
            selector = "default"
        if not selector in (
                "current", "default", "default_entity", "killer_entity", "damager_entity", "victim_entity",
                "shooter_entity",
                "projectile", "last_entity"):
            error("UnexistsSelector", f"Указан несуществующий селектор {selector}", start_line, end_line, offset_pos,
                  limit_offset_pos, file)
        self.selector = selector
        self.type = values[name]["type"]

    def __str__(self):
        return f'value({self.name},{self.selector})'

    def __repr__(self):
        return self.__str__()

    def json(self, normal=None):
        return {"type": "game_value", "game_value": values[self.name]["id"],
                "selection": json.dumps({"type": self.selector})}


def try_action(act, in_var=False, set_var=False, ignore_lst=False):
    global var_count
    additional_acts = []
    after_acts = []
    if set_var:
        if isinstance(act, slice):
            act.obj, additional2 = try_action(act.obj, set_var=True)
            additional_acts.extend(additional2)
            act.arg["start"], additional2 = try_action(act.arg["start"], in_var=True)
            additional_acts.extend(additional2)
            if act.obj.type_hint in ("array", "any"):
                if act.arg["end"] is None:
                    spec_var = var("jmcc." + str(var_count := var_count + 1), "LOCAL", act.start_line, act.end_line,
                                   act.offset_pos, act.limit_offset_pos, act.file)
                    additional_acts.append(action("variable", "set_list_value", args(
                        unpositional=[assign("variable", act.obj), assign("list", act.obj),
                                      assign("number", act.arg["start"]), assign("value", spec_var)]), None, None,
                                                  act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos,
                                                  act.file))
                    return spec_var, additional_acts
                else:
                    act.arg["end"], additional2 = try_action(act.arg["end"], in_var=True)
                    additional_acts.extend(additional2)
                    spec_var = var("jmcc." + str(var_count := var_count + 1), "LOCAL", act.start_line, act.end_line,
                                   act.offset_pos, act.limit_offset_pos, act.file)
                    spec_var1 = var("jmcc." + str(var_count := var_count + 1), "LOCAL", act.start_line, act.end_line,
                                    act.offset_pos, act.limit_offset_pos, act.file)
                    additional_acts.append(action("variable", "trim_list", args(
                        unpositional=[assign("variable", spec_var1), assign("list", act.obj),
                                      assign("start", number(0)),
                                      assign("end", act.arg["start"])]), None, None,
                                                  act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos,
                                                  act.file))
                    spec_var3 = var("jmcc." + str(var_count := var_count + 1), "LOCAL", act.start_line, act.end_line,
                                    act.offset_pos, act.limit_offset_pos, act.file)
                    additional_acts.append(action("variable", "get_list_length", args(
                        unpositional=[assign("variable", spec_var3), assign("list", act.obj)]), None, None,
                                                  act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos,
                                                  act.file))
                    spec_var2 = var("jmcc." + str(var_count := var_count + 1), "LOCAL", act.start_line, act.end_line,
                                    act.offset_pos, act.limit_offset_pos, act.file)
                    additional_acts.append(action("variable", "trim_list", args(
                        unpositional=[assign("variable", spec_var2), assign("list", act.obj),
                                      assign("start", act.arg["end"]),
                                      assign("end", spec_var3)]), None, None,
                                                  act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos,
                                                  act.file))
                    additional_acts.append(action("variable", "append_list", args(
                        unpositional=[assign("variable", act.obj), assign("list_1", spec_var1),
                                      assign("list_2", spec_var)]), None, None,
                                                  act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos,
                                                  act.file))
                    additional_acts.append(action("variable", "append_list", args(
                        unpositional=[assign("variable", act.obj), assign("list_1", act.obj),
                                      assign("list_2", spec_var2)]), None, None,
                                                  act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos,
                                                  act.file))
                return spec_var, additional_acts
            elif act.obj.type_hint == "map":
                if act.arg["end"] is None:
                    spec_var = var("jmcc." + str(var_count := var_count + 1), "LOCAL", act.start_line, act.end_line,
                                   act.offset_pos, act.limit_offset_pos, act.file)
                    additional_acts.append(action("variable", "set_map_value", args(
                        unpositional=[assign("variable", act.obj), assign("map", act.obj),
                                      assign("key", act.arg["start"]), assign("value", spec_var)]), None, None,
                                                  act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos,
                                                  act.file))
                    return spec_var, additional_acts
                else:
                    error("UnsupportedOperation", "", act.start_line, act.end_line, act.offset_pos,
                          act.limit_offset_pos, act.file)
            elif act.obj.type_hint == "text":
                if act.arg["end"] is not None:
                    act.arg["end"], additional2 = try_action(act.arg["end"], in_var=True)
                    additional_acts.extend(additional2)
                spec_var = var("jmcc." + str(var_count := var_count + 1), "LOCAL", act.start_line, act.end_line,
                               act.offset_pos, act.limit_offset_pos, act.file)
                spec_var1 = var("jmcc." + str(var_count := var_count + 1), "LOCAL", act.start_line, act.end_line,
                                act.offset_pos, act.limit_offset_pos, act.file)
                additional_acts.append(action("variable", "trim_text", args(
                    unpositional=[assign("variable", spec_var1), assign("text", act.obj),
                                  assign("start", number(0)),
                                  assign("end", act.arg["start"])]), None, None,
                                              act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos,
                                              act.file))
                spec_var3 = var("jmcc." + str(var_count := var_count + 1), "LOCAL", act.start_line, act.end_line,
                                act.offset_pos, act.limit_offset_pos, act.file)
                additional_acts.append(action("variable", "get_text_length", args(
                    unpositional=[assign("variable", spec_var3), assign("text", act.obj)]), None, None,
                                              act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos,
                                              act.file))
                spec_var2 = var("jmcc." + str(var_count := var_count + 1), "LOCAL", act.start_line, act.end_line,
                                act.offset_pos, act.limit_offset_pos, act.file)
                additional_acts.append(action("variable", "trim_text", args(
                    unpositional=[assign("variable", spec_var2), assign("text", act.obj),
                                  assign("start", act.arg["end"]),
                                  assign("end", spec_var3)]), None, None,
                                              act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos,
                                              act.file))
                additional_acts.append(action("variable", "set_text", args(
                    unpositional=[assign("variable", act.obj), assign("text", lst([spec_var1, spec_var, spec_var2])),
                                  assign("merging", text("CONCATENATION"))]), None, None,
                                              act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos,
                                              act.file))
                return spec_var, additional_acts
        return act, additional_acts
    if in_var:
        if isinstance(act, slice):
            act.obj, additional2 = try_action(act.obj, set_var=True)
            additional_acts.extend(additional2)
            act.arg["start"], additional2 = try_action(act.arg["start"], in_var=True)
            additional_acts.extend(additional2)
            if act.obj.type_hint in ("array", "any"):
                if act.arg["end"] is None:
                    spec_var = var("jmcc." + str(var_count := var_count + 1), "LOCAL", act.start_line, act.end_line,
                                   act.offset_pos, act.limit_offset_pos, act.file)
                    additional_acts.append(action("variable", "get_list_value", args(
                        unpositional=[assign("variable", spec_var), assign("list", act.obj),
                                      assign("number", act.arg["start"])]), None, None,
                                                  act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos,
                                                  act.file))
                    return spec_var, additional_acts
                else:
                    act.arg["end"], additional2 = try_action(act.arg["end"], in_var=True)
                    additional_acts.extend(additional2)
                    spec_var = var("jmcc." + str(var_count := var_count + 1), "LOCAL", act.start_line, act.end_line,
                                   act.offset_pos, act.limit_offset_pos, act.file)
                    additional_acts.append(action("variable", "trim_list", args(
                        unpositional=[assign("variable", spec_var), assign("list", act.obj),
                                      assign("start", act.arg["start"]),
                                      assign("end", act.arg["end"])]), None, None,
                                                  act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos,
                                                  act.file))
                    return spec_var, additional_acts
            elif act.obj.type_hint == "map":
                if act.arg["end"] is None:
                    spec_var = var("jmcc." + str(var_count := var_count + 1), "LOCAL", act.start_line, act.end_line,
                                   act.offset_pos, act.limit_offset_pos, act.file)
                    additional_acts.append(action("variable", "get_map_value", args(
                        unpositional=[assign("variable", spec_var), assign("map", act.obj),
                                      assign("key", act.arg["start"])]), None, None,
                                                  act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos,
                                                  act.file))
                    return spec_var, additional_acts
                else:
                    error("UnsupportedOperation", "", act.start_line, act.end_line, act.offset_pos,
                          act.limit_offset_pos, act.file)
            elif act.obj.type_hint == "text":
                if act.arg["end"] is None:
                    spec_var = var("jmcc." + str(var_count := var_count + 1), "LOCAL", act.start_line, act.end_line,
                                   act.offset_pos, act.limit_offset_pos, act.file)
                    action("variable", "get_char_at",
                           args(unpositional=[assign("text", act.obj), assign("index", act.arg["start"]),
                                              assign("variable", spec_var)], start_line=act.start_line,
                                end_line=act.end_line,
                                offset_pos=act.offset_pos, limit_offset_pos=act.limit_offset_pos,
                                file=act.file),
                           None, None, act.start_line, act.end_line, act.offset_pos,
                           act.limit_offset_pos,
                           act.file)
                    return spec_var, additional_acts
                else:
                    act.arg["end"], additional2 = try_action(act.arg["end"], in_var=True)
                    additional_acts.extend(additional2)
                    spec_var = var("jmcc." + str(var_count := var_count + 1), "LOCAL", act.start_line, act.end_line,
                                   act.offset_pos, act.limit_offset_pos, act.file)
                    additional_acts.append(action("variable", "trim_text", args(
                        unpositional=[assign("variable", spec_var),
                                      assign("text", act.obj),
                                      assign("start", act.arg["start"]),
                                      assign("end", act.arg["end"])]), None, None,
                                                  act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos,
                                                  act.file))
                    return spec_var, additional_acts
        elif isinstance(act, lst):
            if not ignore_lst:
                spec_var = var("jmcc." + str(var_count := var_count + 1), "LOCAL", act.start_line, act.end_line,
                               act.offset_pos, act.limit_offset_pos, act.file)
                for i in range(len(act.values)):
                    act.values[i], additional2 = try_action(act.values[i], in_var=True)
                    additional_acts.extend(additional2)
                additional_acts.append(action("variable", "create_list",
                                              args(
                                                  unpositional=[assign("assigning", [spec_var]), assign("values", act)],
                                                  start_line=act.start_line, end_line=act.end_line,
                                                  offset_pos=act.offset_pos, limit_offset_pos=act.limit_offset_pos,
                                                  file=act.file),
                                              None, None, act.start_line, act.end_line, act.offset_pos,
                                              act.limit_offset_pos,
                                              act.file))
                return spec_var, additional_acts
            else:
                for i in range(len(act.values)):
                    act.values[i], additional2 = try_action(act.values[i], in_var=True)
                    additional_acts.extend(additional2)
        elif isinstance(act, dct):
            spec_var = var("jmcc." + str(var_count := var_count + 1), "LOCAL", act.start_line, act.end_line,
                           act.offset_pos, act.limit_offset_pos, act.file)
            for i in range(len(act.values)):
                act.values[i], additional2 = try_action(act.values[i], in_var=True)
                additional_acts.extend(additional2)
            for i in range(len(act.keys)):
                act.keys[i], additional2 = try_action(act.keys[i], in_var=True)
                additional_acts.extend(additional2)
            additional_acts.append(action("variable", "create_map_from_values",
                                          args(
                                              unpositional=[assign("variable", spec_var), assign("keys", lst(act.keys)),
                                                            assign("values", lst(act.values))],
                                              start_line=act.start_line, end_line=act.end_line,
                                              offset_pos=act.offset_pos, limit_offset_pos=act.limit_offset_pos,
                                              file=act.file),
                                          None, None, act.start_line, act.end_line, act.offset_pos,
                                          act.limit_offset_pos,
                                          act.file))
            return spec_var, additional_acts
        elif isinstance(act, action):
            spec_var = var("jmcc." + str(var_count := var_count + 1), "LOCAL", act.start_line, act.end_line,
                           act.offset_pos, act.limit_offset_pos, act.file)
            act.args.unpositional.append(assign("assigning", [spec_var]))
            unpositional = []
            for k1, v1 in act.args.get_args().items():
                if v1 is not None:
                    v1, additional2 = try_action(v1, ignore_lst=not "array" in act.arg_list, in_var=True)
                    additional_acts.extend(additional2)
                    unpositional.append(assign(k1, v1))
            act.args.unpositional = unpositional
            act.args.positional = []
            additional_acts.append(act)
            return spec_var, additional_acts
        elif isinstance(act, math):
            act, additional2 = try_math(act)
            additional_acts.extend(additional2)

        return act, additional_acts

    if isinstance(act, true_assign):
        if len(act.args["first"]) == 1:
            if act.args["first"][0].type == "INLINE":
                if act.assign_type == "=":
                    symbol_table["inlines"][act.args["first"]] = try_action(act.args["second"])
                    return
                elif act.assign_type == "+=":
                    symbol_table["inlines"][act.args["first"]] += try_action(act.args["second"])
                    return
                elif act.assign_type == "*=":
                    symbol_table["inlines"][act.args["first"]] *= try_action(act.args["second"])
                    return
                elif act.assign_type == "/=":
                    symbol_table["inlines"][act.args["first"]] /= try_action(act.args["second"])
                    return
                elif act.assign_type == "//=":
                    symbol_table["inlines"][act.args["first"]] //= try_action(act.args["second"])
                    return
                elif act.assign_type == "^=":
                    symbol_table["inlines"][act.args["first"]] **= try_action(act.args["second"])
                    return
            if not isinstance(act.args["first"][0], var) or isinstance(act.args["second"], math):
                act.args["second"], additional2 = try_action(act.args["second"], in_var=True)
                additional_acts.extend(additional2)
            if act.assign_type == "=":
                if isinstance(act.args["first"][0], slice):
                    if (type(act.args["second"]) in
                            (number, text, item, sound, particle, vector, location, potion, value, var, math)):
                        act.args["first"][0].obj, additional2 = try_action(act.args["first"][0].obj, set_var=True)
                        additional_acts.extend(additional2)
                        act.args["first"][0].arg["start"], additional2 = try_action(act.args["first"][0].arg["start"],
                                                                                    in_var=True)
                        additional_acts.extend(additional2)
                        if act.args["first"][0].obj.type_hint in ("array", "any"):
                            if act.args["first"][0].arg["end"] is None:
                                return action("variable", "set_list_value", args(
                                    unpositional=[assign("variable", act.args["first"][0].obj),
                                                  assign("list", act.args["first"][0].obj),
                                                  assign("number", act.args["first"][0].arg["start"]),
                                                  assign("value", act.args["second"])]), None, None, act.start_line,
                                              act.end_line, act.offset_pos, act.limit_offset_pos,
                                              act.file), additional_acts, after_acts
                            else:
                                act.args["first"][0].arg["end"], additional2 = try_action(
                                    act.args["first"][0].arg["end"], in_var=True)
                                additional_acts.extend(additional2)
                                spec_var1 = var("jmcc." + str(var_count := var_count + 1), "LOCAL",
                                                act.args["first"][0].start_line, act.args["first"][0].end_line,
                                                act.args["first"][0].offset_pos, act.args["first"][0].limit_offset_pos,
                                                act.args["first"][0].file)
                                additional_acts.append(action("variable", "trim_list", args(
                                    unpositional=[assign("variable", spec_var1),
                                                  assign("list", act.args["first"][0].obj),
                                                  assign("start", number(0)),
                                                  assign("end", act.args["first"][0].arg["start"])]), None, None,
                                                              act.start_line, act.end_line, act.offset_pos,
                                                              act.limit_offset_pos,
                                                              act.file))
                                spec_var3 = var("jmcc." + str(var_count := var_count + 1), "LOCAL", act.start_line,
                                                act.end_line,
                                                act.offset_pos, act.limit_offset_pos, act.file)
                                additional_acts.append(action("variable", "get_list_length", args(
                                    unpositional=[assign("variable", spec_var3),
                                                  assign("list", act.args["first"][0].obj)]),
                                                              None, None,
                                                              act.start_line, act.end_line, act.offset_pos,
                                                              act.limit_offset_pos,
                                                              act.file))
                                spec_var2 = var("jmcc." + str(var_count := var_count + 1), "LOCAL", act.start_line,
                                                act.end_line,
                                                act.offset_pos, act.limit_offset_pos, act.file)
                                additional_acts.append(action("variable", "trim_list", args(
                                    unpositional=[assign("variable", spec_var2),
                                                  assign("list", act.args["first"][0].obj),
                                                  assign("start", act.args["first"][0].arg["end"]),
                                                  assign("end", spec_var3)]), None, None,
                                                              act.start_line, act.end_line, act.offset_pos,
                                                              act.limit_offset_pos,
                                                              act.file))
                                after_acts.append(action("variable", "append_list", args(
                                    unpositional=[assign("variable", act.args["first"][0].obj),
                                                  assign("list_1", act.args["first"][0].obj),
                                                  assign("list_2", spec_var2)]), None, None,
                                                         act.start_line, act.end_line, act.offset_pos,
                                                         act.limit_offset_pos,
                                                         act.file))
                            return action("variable", "append_list", args(
                                unpositional=[assign("variable", act.args["first"][0].obj), assign("list_1", spec_var1),
                                              assign("list_2", act.args["second"])]), None, None,
                                          act.start_line, act.end_line, act.offset_pos,
                                          act.limit_offset_pos,
                                          act.file), additional_acts, after_acts
                        elif act.obj.type_hint == "map":
                            if act.args["first"][0].arg["end"] is None:
                                spec_var = var("jmcc." + str(var_count := var_count + 1), "LOCAL", act.start_line,
                                               act.end_line,
                                               act.offset_pos, act.limit_offset_pos, act.file)
                                additional_acts.append(action("variable", "set_map_value", args(
                                    unpositional=[assign("variable", act.obj), assign("map", act.obj),
                                                  assign("key", act.args["first"][0].arg["start"]),
                                                  assign("value", spec_var)]), None, None,
                                                              act.start_line, act.end_line, act.offset_pos,
                                                              act.limit_offset_pos,
                                                              act.file))
                                return spec_var, additional_acts
                            else:
                                error("UnsupportedOperation", "", act.start_line, act.end_line, act.offset_pos,
                                      act.limit_offset_pos, act.file)
                        elif act.obj.type_hint == "text":
                            if act.args["first"][0].arg["end"] is not None:
                                act.args["first"][0].arg["end"], additional2 = try_action(
                                    act.args["first"][0].arg["end"], in_var=True)
                                additional_acts.extend(additional2)
                            spec_var = var("jmcc." + str(var_count := var_count + 1), "LOCAL", act.start_line,
                                           act.end_line,
                                           act.offset_pos, act.limit_offset_pos, act.file)
                            spec_var1 = var("jmcc." + str(var_count := var_count + 1), "LOCAL", act.start_line,
                                            act.end_line,
                                            act.offset_pos, act.limit_offset_pos, act.file)
                            additional_acts.append(action("variable", "trim_text", args(
                                unpositional=[assign("variable", spec_var1), assign("text", act.obj),
                                              assign("start", number(0)),
                                              assign("end", act.args["first"][0].arg["start"])]), None, None,
                                                          act.start_line, act.end_line, act.offset_pos,
                                                          act.limit_offset_pos,
                                                          act.file))
                            spec_var3 = var("jmcc." + str(var_count := var_count + 1), "LOCAL", act.start_line,
                                            act.end_line,
                                            act.offset_pos, act.limit_offset_pos, act.file)
                            additional_acts.append(action("variable", "get_text_length", args(
                                unpositional=[assign("variable", spec_var3), assign("text", act.obj)]), None, None,
                                                          act.start_line, act.end_line, act.offset_pos,
                                                          act.limit_offset_pos,
                                                          act.file))
                            spec_var2 = var("jmcc." + str(var_count := var_count + 1), "LOCAL", act.start_line,
                                            act.end_line,
                                            act.offset_pos, act.limit_offset_pos, act.file)
                            additional_acts.append(action("variable", "trim_text", args(
                                unpositional=[assign("variable", spec_var2), assign("text", act.obj),
                                              assign("start", act.args["first"][0].arg["end"]),
                                              assign("end", spec_var3)]), None, None,
                                                          act.start_line, act.end_line, act.offset_pos,
                                                          act.limit_offset_pos,
                                                          act.file))
                            additional_acts.append(action("variable", "set_text", args(
                                unpositional=[assign("variable", act.obj),
                                              assign("text", lst([spec_var1, spec_var, spec_var2])),
                                              assign("merging", text("CONCATENATION"))]), None, None,
                                                          act.start_line, act.end_line, act.offset_pos,
                                                          act.limit_offset_pos,
                                                          act.file))
        variables = []
        for v2 in act.args["first"]:
            v2, additional2 = try_action(v2, set_var=True)
            variables.append(v2)
            after_acts.extend(additional2)
        act.args["first"] = variables
        if act.assign_type == "=":
            if type(act.args["second"]) in (number, text, item, sound, particle, vector, location, potion, value, var, math):
                return action("variable", "set_value", args(
                    unpositional=[assign("assigning", act.args["first"]), assign("value", act.args["second"])]),
                              None, None, act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos,
                              act.file), additional_acts, after_acts
            if isinstance(act.args["second"], action):
                act.args["second"].args.unpositional.append(assign("assigning", act.args["first"]))
                unpositional = []
                for k1, v1 in act.args["second"].args.get_args().items():
                    if v1 is not None:
                        v1, additional2 = try_action(v1, ignore_lst=not "array" in act.args["second"].arg_list,
                                                     in_var=True)
                        additional_acts.extend(additional2)
                        unpositional.append(assign(k1, v1))
                act.args["second"].args.unpositional = unpositional
                act.args["second"].args.positional = []
                return act.args["second"], additional_acts, after_acts
            elif isinstance(act.args["second"], lst):
                for i in range(len(act.args["second"].values)):
                    act.args["second"].values[i], additional2 = try_action(act.args["second"].values[i], in_var=True)
                    additional_acts.extend(additional2)
                unpositional = [assign("assigning", act.args["first"]), assign("values", act.args["second"])]
                return action("variable", "create_list",
                              args(unpositional=unpositional, start_line=act.start_line, end_line=act.end_line,
                                   offset_pos=act.offset_pos, limit_offset_pos=act.limit_offset_pos, file=act.file),
                              None, None, act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos,
                              act.file), additional_acts, after_acts
            elif isinstance(act.args["second"], dct):
                for i in range(len(act.args["second"].values)):
                    act.args["second"].values[i], additional2 = try_action(act.args["second"].values[i], in_var=True)
                    additional_acts.extend(additional2)
                for i in range(len(act.args["second"].keys)):
                    act.args["second"].values[i], additional2 = try_action(act.args["second"].values[i], in_var=True)
                    additional_acts.extend(additional2)
                unpositional = [assign("assigning", act.args["first"]), assign("keys", lst(act.args["second"].keys)),
                                assign("values", lst(act.args["second"].values))]
                return action("variable", "create_map_from_values",
                              args(unpositional=unpositional, start_line=act.start_line, end_line=act.end_line,
                                   offset_pos=act.offset_pos, limit_offset_pos=act.limit_offset_pos, file=act.file),
                              None, None, act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos,
                              act.file), additional_acts, after_acts
            elif isinstance(act.args["second"], slice):
                act.args["second"].arg["start"], additional2 = try_action(act.args["second"].arg["start"], in_var=True)
                additional_acts.extend(additional2)
                if act.args["second"].arg["end"] is None:
                    if act.args["second"].obj.type_hint in ("array", "any"):
                        unpositional = [assign("assigning", act.args["first"]),
                                        assign("list", act.args["second"].obj),
                                        assign("number", act.args["second"].arg["start"])]
                        return action("variable", "get_list_value",
                                      args(unpositional=unpositional, start_line=act.start_line,
                                           end_line=act.end_line,
                                           offset_pos=act.offset_pos, limit_offset_pos=act.limit_offset_pos,
                                           file=act.file),
                                      None, None, act.start_line, act.end_line, act.offset_pos,
                                      act.limit_offset_pos,
                                      act.file), additional_acts, after_acts
                    elif act.args["second"].obj.type_hint == "map":
                        unpositional = [assign("assigning", act.args["first"]),
                                        assign("map", act.args["second"].obj),
                                        assign("key", act.args["second"].arg["start"])]
                        return action("variable", "get_map_value",
                                      args(unpositional=unpositional, start_line=act.start_line,
                                           end_line=act.end_line,
                                           offset_pos=act.offset_pos, limit_offset_pos=act.limit_offset_pos,
                                           file=act.file),
                                      None, None, act.start_line, act.end_line, act.offset_pos,
                                      act.limit_offset_pos,
                                      act.file), additional_acts, after_acts
                    elif act.args["second"].obj.type_hint == "text":
                        unpositional = [assign("assigning", act.args["first"]),
                                        assign("text", act.args["second"].obj),
                                        assign("index", act.args["second"].arg["start"])]
                        return action("variable", "get_char_at",
                                      args(unpositional=unpositional, start_line=act.start_line,
                                           end_line=act.end_line,
                                           offset_pos=act.offset_pos, limit_offset_pos=act.limit_offset_pos,
                                           file=act.file),
                                      None, None, act.start_line, act.end_line, act.offset_pos,
                                      act.limit_offset_pos,
                                      act.file), additional_acts, after_acts
                    else:
                        error("UnsupportedOperation", "", act.start_line, act.end_line, act.offset_pos,
                              act.limit_offset_pos, act.file)
                else:
                    if act.args["second"].obj.type_hint in ("array", "any"):
                        return action("variable", "trim_list", args(
                            unpositional=[assign("assigning", act.args["first"]),
                                          assign("list", act.args["second"].obj),
                                          assign("start", act.args["second"].arg["start"]),
                                          assign("end", act.args["second"].arg["end"])]), None, None,
                                      act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos,
                                      act.file), additional_acts, after_acts
                    elif act.args["second"].obj.type_hint == "text":
                        return action("variable", "trim_text", args(
                            unpositional=[assign("assigning", act.args["first"]),
                                          assign("text", act.args["second"].obj),
                                          assign("start", act.args["second"].arg["start"]),
                                          assign("end", act.args["second"].arg["end"])]), None, None,
                                      act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos,
                                      act.file), additional_acts, after_acts
                    else:
                        error("UnsupportedOperation", "", act.start_line, act.end_line, act.offset_pos,
                              act.limit_offset_pos, act.file)
        else:
            act.args["second"], additional2 = try_action(act.args["second"], in_var=True)
            additional_acts.extend(additional2)
            if act.assign_type == "+=":
                return action("variable", "increment", args(
                    unpositional=[assign("assigning", act.args["first"]), assign("number", act.args["second"])],
                    start_line=act.start_line, end_line=act.end_line, offset_pos=act.offset_pos,
                    limit_offset_pos=act.limit_offset_pos, file=act.file),
                              None, None, act.start_line, act.end_line, act.offset_pos,
                              act.limit_offset_pos,
                              act.file), additional_acts, after_acts
            elif act.assign_type == "-=":
                return action("variable", "decrement", args(
                    unpositional=[assign("assigning", act.args["first"]), assign("number", act.args["second"])],
                    start_line=act.start_line, end_line=act.end_line, offset_pos=act.offset_pos,
                    limit_offset_pos=act.limit_offset_pos, file=act.file),
                              None, None, act.start_line, act.end_line, act.offset_pos,
                              act.limit_offset_pos,
                              act.file), additional_acts, after_acts
            elif act.assign_type == "*=":
                return action("variable", "multiply", args(unpositional=[assign("assigning", act.args["first"]),
                                                                         assign("value", lst([act.args["first"][0],
                                                                                              act.args["second"]]))],
                                                           start_line=act.start_line, end_line=act.end_line,
                                                           offset_pos=act.offset_pos,
                                                           limit_offset_pos=act.limit_offset_pos, file=act.file),
                              None, None, act.start_line, act.end_line, act.offset_pos,
                              act.limit_offset_pos,
                              act.file), additional_acts, after_acts
            elif act.assign_type == "/=":
                return action("variable", "divide", args(unpositional=[assign("assigning", act.args["first"]),
                                                                       assign("value", lst([act.args["first"][0],
                                                                                            act.args["second"]]))],
                                                         start_line=act.start_line, end_line=act.end_line,
                                                         offset_pos=act.offset_pos,
                                                         limit_offset_pos=act.limit_offset_pos, file=act.file),
                              None, None, act.start_line, act.end_line, act.offset_pos,
                              act.limit_offset_pos,
                              act.file), additional_acts, after_acts
            elif act.assign_type == "//=":
                return action("variable", "divide", args(
                    unpositional=[assign("division_mode", text("FLOOR")), assign("assigning", act.args["first"]),
                                  assign("value", lst([act.args["first"][0], act.args["second"]]))],
                    start_line=act.start_line, end_line=act.end_line, offset_pos=act.offset_pos,
                    limit_offset_pos=act.limit_offset_pos, file=act.file),
                              None, None, act.start_line, act.end_line, act.offset_pos,
                              act.limit_offset_pos,
                              act.file), additional_acts, after_acts
            elif act.assign_type == "%=":
                return action("variable", "remainder", args(
                    unpositional=[assign("assigning", act.args["first"]), assign("divisor", act.args["first"][0]),
                                  assign("dividend", act.args["second"])], start_line=act.start_line,
                    end_line=act.end_line, offset_pos=act.offset_pos, limit_offset_pos=act.limit_offset_pos,
                    file=act.file),
                              None, None, act.start_line, act.end_line, act.offset_pos,
                              act.limit_offset_pos,
                              act.file), additional_acts, after_acts
            elif act.assign_type == "^=":
                return action("variable", "pow", args(
                    unpositional=[assign("assigning", act.args["first"]), assign("base", act.args["first"][0]),
                                  assign("power", act.args["second"])], start_line=act.start_line,
                    end_line=act.end_line, offset_pos=act.offset_pos, limit_offset_pos=act.limit_offset_pos,
                    file=act.file),
                              None, None, act.start_line, act.end_line, act.offset_pos,
                              act.limit_offset_pos,
                              act.file), additional_acts, after_acts

    if isinstance(act, action):
        unpositional = []
        for k1, v1 in act.args.get_args().items():
            if v1 is not None:
                v1, additional2 = try_action(v1, ignore_lst=not "array" in act.arg_list, in_var=True)
                additional_acts.extend(additional2)
                unpositional.append(assign(k1, v1))
        act.args.unpositional = unpositional
        act.args.positional = []
    return act, additional_acts, after_acts


class slice:
    def __init__(self, obj, arg, start_line=None, end_line=None,
                 offset_pos=None, limit_offset_pos=None, file=None):
        self.type = "slice"
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        self.obj = obj
        arg.arg_list = ["start", "end"]
        self.arg = arg.get_args()

    def __str__(self):
        return f'slice({self.obj},{self.arg["start"]}:{self.arg["end"]})'

    def __repr__(self):
        return self.__str__()


class atribute:
    def __init__(self, obj, atr, start_line=None, end_line=None,
                 offset_pos=None, limit_offset_pos=None, file=None):
        self.type = "argument"
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        self.obj = obj
        self.atr = atr

    def __str__(self):
        return f'atribute({self.obj},{self.atr})'

    def __repr__(self):
        return self.__str__()


class true_assign:
    def __init__(self, assign_type, arg=None, start_line=None, end_line=None, offset_pos=None, limit_offset_pos=None,
                 file=None):
        self.type = "true_assign"
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        self.assign_type = assign_type
        arg.arg_list = ["first", "second"]
        self.args = arg.get_args()

    def __str__(self):
        return f'true_assign({self.args["first"]}{self.assign_type}{self.args["second"]})'

    def __repr__(self):
        return self.__str__()


class enum:
    def __init__(self, enu, start_line=None, end_line=None, offset_pos=None, limit_offset_pos=None,
                 file=None, vare=None):
        self.type = "enum"
        self.enum = enu
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        self.var = vare

    def __str__(self):
        return f'enum({self.enum})'

    def __repr__(self):
        return self.__str__()

    def json(self, normal=False):
        a = {"type": "enum", "enum": self.enum}
        if self.var is not None:
            a["variable"] = self.var.name
            a["scope"] = self.var.var_type.lower()
        return a


class action:
    def __init__(self, act_type, sub_action, arg=None, selector=None, no=None, start_line=None, end_line=None,
                 offset_pos=None, limit_offset_pos=None, file=None, operations=None, conditional=None):
        self.type = "action"
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        if not (act_type == "special" and sub_action in origin_actions) and not (
                act_type + "::" + sub_action in actions):
            if sub_action in non_origin_actions:
                error("Cringe",
                      "Действие " + actions[non_origin_actions[sub_action]]["object"] + "::" + sub_action + "(" +
                      actions[non_origin_actions[sub_action]][
                          "localized_name"] + ") не может быть вызвано от переменной", start_line, end_line,
                      offset_pos,
                      limit_offset_pos, file)
            else:
                error("UnexistsAction", f"Указано несуществующее действие {sub_action}", start_line, end_line,
                      offset_pos,
                      limit_offset_pos, file)
        elif act_type == "special":
            act_type = actions[origin_actions[sub_action]]["object"]
        self.act_type = act_type
        self.sub_action = sub_action
        arg.origin = actions[act_type + "::" + sub_action].setdefault("origin", None)
        arg.assigning = actions[act_type + "::" + sub_action].setdefault("assign", None)
        arg.lamba = actions[act_type + "::" + sub_action].setdefault("lambda", None)
        arg.arg_list = [i["id"] for i in actions[act_type + "::" + sub_action]["args"]]
        self.args = arg
        self.arg_list = {i["id"]: i for i in actions[self.act_type + "::" + self.sub_action]["args"]}
        if selector is not None:
            if act_type == "player":
                if not selector in (
                        "current", "default_player", "killer_player", "damager_player", "shooter_player",
                        "victim_player",
                        "random_player", "all_players"):
                    error("UnexistsSelector", f"Указан несуществующий селектор {selector}", start_line, end_line,
                          offset_pos,
                          limit_offset_pos, file)
            elif act_type == "entity":
                if not selector in (
                        "current", "default_entity", "killer_entity", "damager_entity", "shooter_entity", "projectile",
                        "victim_entity", "random_entity", "all_mobs", "all_entities", "last_entity"):
                    error("UnexistsSelector", f"Указан несуществующий селектор {selector}", start_line, end_line,
                          offset_pos,
                          limit_offset_pos, file)
            else:
                selector = None
        self.selector = selector
        self.operations = operations
        self.conditional = conditional
        self.no = no

    def __str__(self):
        return f'action({self.act_type},{self.sub_action},{self.args},{self.selector},{self.no})'

    def __repr__(self):
        return self.__str__()

    def json(self, normal=None):
        act_id = actions[self.act_type + "::" + self.sub_action]["id"]
        arg = []
        self.args = self.args.get_args()
        for k1, v1 in self.args.items():
            if v1 is None:
                continue
            if self.arg_list[k1]["type"] == "variable":
                if isinstance(v1, var):
                    continue
                else:
                    error("TypeError",
                          "Ожидался объект типа " + self.arg_list[k1]["type"] + f", но был получен {v1.type}",
                          v1.start_line, v1.end_line, v1.offset_pos, v1.limit_offset_pos, v1.file)
            if isinstance(v1, var):
                typ = v1.type_hint
            elif v1 is not None:
                typ = v1.type
            else:
                continue
            if "array" in self.arg_list[k1] and v1.type == "array":
                if len(v1.values) > self.arg_list[k1]["array"]:
                    error("SizeError",
                          f"Был указан слишком большой список({len(v1.values)}), когда максимальный - " + str(
                              self.arg_list[k1]["array"]),
                          v1.start_line, v1.end_line, v1.offset_pos, v1.limit_offset_pos, v1.file)
                continue
            if self.arg_list[k1]["type"] in ("enum", "boolean"):
                if isinstance(v1, text):
                    if (self.arg_list[k1]["type"] == "enum" and not v1.text in [i["value"] for i in
                                                                                self.arg_list[k1]["values"]]) or (
                            self.arg_list[k1]["type"] == "boolean" and not v1.text in ("TRUE", "FALSE")):
                        error("UnknownArgument",
                              f"Неизвестный тип перечисления {v1.text}",
                              v1.start_line, v1.end_line, v1.offset_pos, v1.limit_offset_pos, v1.file)
                    self.args[k1] = enum(v1.text, v1.start_line, v1.end_line, v1.offset_pos, v1.limit_offset_pos,
                                         v1.file)
                    continue
                elif isinstance(v1, var):
                    if self.arg_list[k1]["type"] == "enum":
                        enu = list(self.arg_list[k1]["values"][0].keys())[0]
                    else:
                        enu = "FALSE"
                    self.args[k1] = enum(enu, v1.start_line, v1.end_line, v1.offset_pos, v1.limit_offset_pos, v1.file,
                                         vare=v1)
                    continue
            if not (typ == "any" or self.arg_list[k1]["type"] == typ or
                    self.arg_list[k1]["type"] == "any" or typ == "text" or self.arg_list[k1]["type"] == "text"):
                error("TypeError", "Ожидался объект типа " + self.arg_list[k1]["type"] + f", но был получен {v1.type}",
                      v1.start_line, v1.end_line, v1.offset_pos, v1.limit_offset_pos, v1.file)
        for kay, val in self.args.items():
            if val is not None:
                arg.append({"name": kay, "value": val.json()})
        a = {"action": act_id, "values": arg}
        if self.no is not None:
            a["is_inverted"] = self.no
        if self.conditional is not None:
            self.conditional.operations = lst([])
            if self.conditional.no is not None:
                if self.no is None:
                    self.no = self.conditional.no
            else:
                if self.no is not None:
                    self.conditional.no = self.no
                else:
                    self.conditional.no = False
            a["conditional"] = self.conditional.json()
            a["values"].extend(a["conditional"]["values"])
        if self.operations is not None:
            a["operations"] = self.operations.json(normal=True)

        return a


class var:
    def __init__(self, name, var_type=None, start_line=None, end_line=None, offset_pos=None, limit_offset_pos=None,
                 file=None, type_hint=None):
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        self.type = "variable"
        self.name = name
        if var_type is None:
            if name in symbol_table["variables"].keys():
                var_type = symbol_table["variables"][name][0]
            else:
                var_type = "LOCAL"
        if type_hint is None:
            if name in symbol_table["variables"].keys():
                type_hint = symbol_table["variables"][name][1]
            else:
                type_hint = "any"
        self.var_type = var_type
        self.type_hint = type_hint

    def __str__(self):
        return f'var({self.name},{self.var_type})'

    def __repr__(self):
        return self.__str__()

    def json(self, in_text=False, normal=None):
        if normal:
            return self.name
        if in_text:
            if self.var_type == "LOCAL":
                return f"%var_local({self.name})"
            elif self.var_type == "GAME":
                return f"%var({self.name})"
            elif self.var_type == "SAVE":
                return f"%var_save({self.name})"
        if self.var_type == "INLINE":
            error("UnknownError", "Обнаружена переменная типа INLINE", self.start_line, self.end_line, self.offset_pos,
                  self.limit_offset_pos, self.file)
        return {"type": "variable", "variable": self.name, "scope": self.var_type.lower()}


class if_:
    def __init__(self, act, operations, start_line=None, end_line=None, offset_pos=None, limit_offset_pos=None,
                 file=None):
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        self.act = act
        self.type = "if"
        self.operations = operations

    def __str__(self):
        return f'if({self.act},{self.operations})'

    def __repr__(self):
        return self.__str__()

    def json(self, normal=None):
        act = self.act.json()
        act["operations"] = self.operations.json(normal=True)
        return act


class else_:
    def __init__(self, operations, start_line=None, end_line=None, offset_pos=None, limit_offset_pos=None, file=None):
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        self.type = "else"
        self.operations = operations

    def __str__(self):
        return f'else({self.operations})'

    def __repr__(self):
        return self.__str__()

    def json(self, normal=None):
        return {"action": "else", "values": [], "operations": self.operations.json(normal=True)}


class event:
    def __init__(self, name, operations, start_line=None, end_line=None, offset_pos=None, limit_offset_pos=None,
                 file=None):
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        self.name = name
        if not self.name in events:
            error("UnexistsEvent", f"Указан несуществующий ивент {self.name}", start_line=self.start_line,
                  end_line=self.end_line, offset_pos=self.offset_pos, limit_offset_pos=self.limit_offset_pos,
                  file=self.file)
        self.operations = operations

    def __str__(self):
        return f'event({self.name},{self.operations})'

    def __repr__(self):
        return self.__str__()

    def json(self, normal=None):
        global global_count
        global_count += 1
        a = {"type": "event", "event": self.name, "position": global_count, "operations": []}
        additional_events = []
        operations, additional2 = fix_operations_len(self.operations.json(normal=True))
        additional_events.extend(additional2)
        a["operations"] = operations
        return a, additional_events


def try_math(mat):
    global var_count
    additional_actions = []
    if isinstance(mat.first, math):
        mat.first, additional2 = try_math(mat.first)
        additional_actions.extend(additional2)
    elif type(mat.first) in (slice, atribute, action, lst, dct):
        mat.first, additional2 = try_action(mat.first, in_var=True)
        additional_actions.extend(additional2)
    elif type(mat.first) in (item, location, vector, sound, particle, potion, value):
        print("thing")
        spec_var = var("jmcc." + str(var_count := var_count + 1), "LOCAL", mat.start_line, mat.end_line,
                       mat.offset_pos, mat.limit_offset_pos, mat.file)
        additional_actions.append(action("variable", "set_value", args(
            unpositional=[assign("assigning", [spec_var]), assign("value", mat.first)]),
                                         None, None, mat.start_line, mat.end_line, mat.offset_pos, mat.limit_offset_pos,
                                         mat.file))
        mat.first = spec_var
    if isinstance(mat.second, math):
        mat.second, additional2 = try_math(mat.second)
        additional_actions.extend(additional2)
    elif type(mat.second) in (slice, atribute, action, lst, dct):
        mat.second, additional2 = try_action(mat.second, in_var=True)
        additional_actions.extend(additional2)
    elif type(mat.second) in (item, location, vector, sound, particle, potion, value):
        spec_var = var("jmcc." + str(var_count := var_count + 1), "LOCAL", mat.start_line, mat.end_line,
                       mat.offset_pos, mat.limit_offset_pos, mat.file)
        additional_actions.append(action("variable", "set_value", args(
            unpositional=[assign("assigning", [spec_var]), assign("value", mat.second)]),
                                         None, None, mat.start_line, mat.end_line, mat.offset_pos, mat.limit_offset_pos,
                                         mat.file))
        mat.second = spec_var
    if isinstance(mat.first, number) and isinstance(mat.second, number):
        if mat.operation == "*":
            return number(mat.first.value * mat.second.value, mat.start_line, mat.end_line, mat.offset_pos,
                          mat.limit_offset_pos, mat.file), additional_actions
        elif mat.operation == "+":
            return number(mat.first.value + mat.second.value, mat.start_line, mat.end_line, mat.offset_pos,
                          mat.limit_offset_pos, mat.file), additional_actions
        elif mat.operation == "/":
            return number(mat.first.value / mat.second.value, mat.start_line, mat.end_line, mat.offset_pos,
                          mat.limit_offset_pos, mat.file), additional_actions
        elif mat.operation == "//":
            return number(mat.first.value // mat.second.value, mat.start_line, mat.end_line, mat.offset_pos,
                          mat.limit_offset_pos, mat.file), additional_actions
        elif mat.operation == "-":
            return number(mat.first.value - mat.second.value, mat.start_line, mat.end_line, mat.offset_pos,
                          mat.limit_offset_pos, mat.file), additional_actions
        elif mat.operation == "%":
            return number(mat.first.value % mat.second.value, mat.start_line, mat.end_line, mat.offset_pos,
                          mat.limit_offset_pos, mat.file), additional_actions
        elif mat.operation == "^":
            return number(mat.first.value ** mat.second.value, mat.start_line, mat.end_line, mat.offset_pos,
                          mat.limit_offset_pos, mat.file), additional_actions
    else:
        return mat, additional_actions
    error("UnsopportedOperand",
          f"Действие {mat.operation} невозможно между {mat.first.type} и {mat.second.type}", mat.start_line,
          mat.end_line, mat.offset_pos, mat.limit_offset_pos, mat.file)


class math:
    def __init__(self, operation, first=None, second=None, start_line=None, end_line=None, offset_pos=None,
                 limit_offset_pos=None, file=None):
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        self.operation = operation
        if isinstance(first, var) and first.var_type == "INLINE":
            first = symbol_table["inlines"][first.name]
        self.first = first
        if isinstance(second, var) and second.var_type == "INLINE":
            second = symbol_table["inlines"][second.name]
        self.second = second
        self.type = "number"

    def __str__(self):
        return f'math({self.first}{self.operation}{self.second})'

    def __repr__(self):
        return self.__str__()

    def json(self, in_text=False):
        if in_text:
            if self.operation == "//":
                return f"floor({self.first.json(in_text=True)}/{self.second.json(in_text=True)})"
            if self.operation == "^":
                return f"pow({self.first.json(in_text=True)},{self.second.json(in_text=True)})"
            return f"({self.first.json(in_text=True)}{self.operation}{self.second.json(in_text=True)})"

        return {"type": "number",
                "number": f"%math({self.first.json(in_text=True)}{self.operation}{self.second.json(in_text=True)})"}


class function:
    def __init__(self, name, operations=None, arg=None, start_line=None, end_line=None, offset_pos=None,
                 limit_offset_pos=None, file=None):
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        self.name = name
        self.actions = operations
        symbol_table["functions"][name] = arg

    def __str__(self):
        return f'function({self.name},{self.actions})'

    def __repr__(self):
        return self.__str__()

    def json(self, normal=None):
        global global_count
        global_count += 1
        a = {"type": "function", "position": global_count, "operations": [], "is_hidden": False, "name": self.name}
        additional_events = []
        operations, additional2 = fix_operations_len(self.actions.json(normal=True))
        additional_events.extend(additional2)
        a["operations"] = operations
        return a, additional_events


def try_function(call_func):
    if call_func.name in allowed_actions:
        if call_func.name == "round":
            if isinstance(call_func.args.args["first"], number):
                if call_func.args.args["second"] is None:
                    call_func.args.args["second"] = number(0)
                if isinstance(call_func.args.args["second"], number):
                    return number(round(call_func.args.args["first"].value, call_func.args.args["second"].value),
                                  call_func.start_line, call_func.end_line, call_func.offset_pos,
                                  call_func.limit_offset_pos, call_func.file)
    return call_func


class call_function:
    def __init__(self, name, arg, start_line=None, end_line=None, offset_pos=None, limit_offset_pos=None,
                 file=None):
        self.type = "number"
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        self.name = name
        if name in math_functions.keys():
            arg.arg_list = math_functions[name]
            arg.get_args()
        self.args = arg

    def __str__(self):
        return f'call_function({self.name},{self.args})'

    def __repr__(self):
        return self.__str__()

    def json(self, in_text=False, normal=None):
        if in_text:
            arg = []
            for k1, v1 in self.args.args.items():
                if v1 is not None:
                    arg.append(v1.json(in_text=True))
            return f"{self.name}(" + ", ".join(arg) + ")"
        return action("code", "call_function", args(positional=[text(self.name)]), None, None, self.start_line,
                      self.end_line, self.offset_pos, self.limit_offset_pos, self.file).json()


class process:
    def __init__(self, name, operations, start_line=None, end_line=None, offset_pos=None, limit_offset_pos=None,
                 file=None):
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        self.name = name
        self.actions = operations

    def __str__(self):
        return f'process({self.name},{self.actions})'

    def __repr__(self):
        return self.__str__()

    def json(self, normal=None):
        global global_count
        global_count += 1
        a = {"type": "process", "position": global_count, "operations": [], "name": self.name, "is_hidden": False}
        additional_events = []
        operations, additional2 = fix_operations_len(self.actions.json(normal=True))
        additional_events.extend(additional2)
        a["operations"] = operations
        return a, additional_events


class Parser:
    global open_files

    def __init__(self, lexer, tree):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token
        self.tree = tree

    def eat(self, token_type):
        if token_type != "OEL":
            while self.current_token.type == "OEL":
                self.current_token = self.lexer.get_next_token
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token
        else:
            error("SyntaxError", f"Ожидался объект типа {token_type}, но был встречен {self.current_token.type}",
                  start_line=self.current_token.start_line, end_line=self.current_token.end_line,
                  offset_pos=self.current_token.offset_pos, limit_offset_pos=self.current_token.limit_offset_pos,
                  file=self.lexer.file)

    def factor(self, var_types=False):
        token = self.current_token
        if token.equals(PLUS_NUMBER, MINUS_NUMBER, NUMBER):
            self.eat(token.type)
            return number(token.value, start_line=token.start_line, end_line=token.end_line,
                          offset_pos=token.offset_pos, limit_offset_pos=token.limit_offset_pos, file=self.lexer.file)
        elif token.equals(STRING, MINIMESSAGE_STRING, PLAIN_STRING, LEGACY_STRING, JSON_STRING):
            if token.equals(PLAIN_STRING):
                text_type = "plain"
            elif token.equals(MINIMESSAGE_STRING):
                text_type = "minimessage"
            elif token.equals(STRING, LEGACY_STRING):
                text_type = "legacy"
            elif token.equals(JSON_STRING):
                text_type = "json"
            else:
                text_type = "None"
            self.eat(token.type)
            return text(token.value, text_type=text_type, start_line=token.start_line, end_line=token.end_line,
                        offset_pos=token.offset_pos, limit_offset_pos=token.limit_offset_pos, file=self.lexer.file)
        elif token.type == NONE:
            self.eat(NONE)
            return text(token.value, start_line=token.start_line, end_line=token.end_line, offset_pos=token.offset_pos,
                        limit_offset_pos=token.limit_offset_pos, file=self.lexer.file)
        elif token.equals(VAR, LOCAL_VAR, GAME_VAR, SAVE_VAR, INLINE_VAR):
            if token.type == VAR:
                self.eat(VAR)
                if self.current_token.equals(LPAREN):
                    start_line = token.start_line
                    offset_pos = token.offset_pos
                    self.eat(LPAREN)
                    positional = []
                    unpositional = []
                    while self.current_token.type != EOF and self.current_token.type != RPAREN:
                        a = self.expr(assigning=True)
                        if isinstance(a, assign):
                            unpositional.append(a)
                        else:
                            positional.append(a)
                        if self.current_token.type == COMMA:
                            self.eat(COMMA)
                    end_line = self.current_token.end_line
                    limit_offset_pos = self.current_token.limit_offset_pos
                    self.eat(RPAREN)
                    return try_function(
                        call_function(token.value,
                                      arg=args(positional=positional, unpositional=unpositional, start_line=start_line,
                                               end_line=end_line, offset_pos=offset_pos,
                                               limit_offset_pos=limit_offset_pos, file=self.lexer.file),
                                      start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                      limit_offset_pos=limit_offset_pos, file=self.lexer.file))
                if self.current_token.equals(COLON) and var_types:
                    self.eat(COLON)
                    type_hint = self.current_token.value
                    self.eat(VAR)
                else:
                    type_hint = None
                return var(token.value, start_line=token.start_line, end_line=token.end_line,
                           offset_pos=token.offset_pos, limit_offset_pos=token.limit_offset_pos, file=self.lexer.file,
                           type_hint=type_hint)
            elif token.type == LOCAL_VAR:
                self.eat(LOCAL_VAR)
                if self.current_token.equals(COLON) and var_types:
                    self.eat(COLON)
                    type_hint = self.current_token.value
                    self.eat(VAR)
                else:
                    type_hint = None
                return var(token.value, var_type="LOCAL", start_line=token.start_line, end_line=token.end_line,
                           offset_pos=token.offset_pos, limit_offset_pos=token.limit_offset_pos, file=self.lexer.file,
                           type_hint=type_hint)
            elif token.type == GAME_VAR:
                self.eat(GAME_VAR)
                if self.current_token.equals(COLON) and var_types:
                    self.eat(COLON)
                    type_hint = self.current_token.value
                    self.eat(VAR)
                else:
                    type_hint = None
                return var(token.value, var_type="GAME", start_line=token.start_line, end_line=token.end_line,
                           offset_pos=token.offset_pos, limit_offset_pos=token.limit_offset_pos, file=self.lexer.file,
                           type_hint=type_hint)
            elif token.type == SAVE_VAR:
                self.eat(SAVE_VAR)
                if self.current_token.equals(COLON) and var_types:
                    self.eat(COLON)
                    type_hint = self.current_token.value
                    self.eat(VAR)
                else:
                    type_hint = None
                return var(token.value, var_type="SAVE", start_line=token.start_line, end_line=token.end_line,
                           offset_pos=token.offset_pos, limit_offset_pos=token.limit_offset_pos, file=self.lexer.file,
                           type_hint=type_hint)
            else:
                self.eat(INLINE_VAR)
                if self.current_token.equals(COLON) and var_types:
                    self.eat(COLON)
                    type_hint = self.current_token.value
                    self.eat(VAR)
                else:
                    type_hint = None
                return var(token.value, var_type="INLINE", start_line=token.start_line, end_line=token.end_line,
                           offset_pos=token.offset_pos, limit_offset_pos=token.limit_offset_pos, file=self.lexer.file,
                           type_hint=type_hint)
        elif token.type == ITEM:
            self.eat(ITEM)
            if self.current_token.equals(LPAREN):
                start_line = token.start_line
                offset_pos = token.offset_pos
                self.eat(LPAREN)
                unpositional = []
                positional = []
                while self.current_token.type != EOF and self.current_token.type != RPAREN:
                    a = self.expr(assigning=True)
                    if isinstance(a, assign):
                        unpositional.append(a)
                    else:
                        positional.append(a)
                    if self.current_token.type == COMMA:
                        self.eat(COMMA)
                end_line = self.current_token.end_line
                limit_offset_pos = self.current_token.limit_offset_pos
                self.eat(RPAREN)
                return item(
                    arg=args(positional=positional, unpositional=unpositional, start_line=start_line, end_line=end_line,
                             offset_pos=offset_pos,
                             limit_offset_pos=limit_offset_pos, file=self.lexer.file), start_line=start_line,
                    end_line=end_line, offset_pos=offset_pos, limit_offset_pos=limit_offset_pos,
                    file=self.lexer.file)
            if self.current_token.equals(COLON) and var_types:
                self.eat(COLON)
                type_hint = self.current_token.value
                self.eat(VAR)
            else:
                type_hint = None
            return var("item", start_line=token.start_line, end_line=token.end_line, offset_pos=token.offset_pos,
                       limit_offset_pos=token.limit_offset_pos, file=self.lexer.file, type_hint=type_hint)
        elif token.type == LOCATION:
            self.eat(LOCATION)
            if self.current_token.equals(LPAREN):
                start_line = token.start_line
                offset_pos = token.offset_pos
                self.eat(LPAREN)
                unpositional = []
                positional = []
                while self.current_token.type != EOF and self.current_token.type != RPAREN:
                    a = self.expr(assigning=True)
                    if isinstance(a, assign):
                        unpositional.append(a)
                    else:
                        positional.append(a)
                    if self.current_token.type == COMMA:
                        self.eat(COMMA)
                end_line = self.current_token.end_line
                limit_offset_pos = self.current_token.limit_offset_pos
                self.eat(RPAREN)
                return location(
                    arg=args(positional=positional, unpositional=unpositional, start_line=start_line, end_line=end_line,
                             offset_pos=offset_pos,
                             limit_offset_pos=limit_offset_pos, file=self.lexer.file), start_line=start_line,
                    end_line=end_line, offset_pos=offset_pos, limit_offset_pos=limit_offset_pos,
                    file=self.lexer.file)
            if self.current_token.equals(COLON) and var_types:
                self.eat(COLON)
                type_hint = self.current_token.value
                self.eat(VAR)
            else:
                type_hint = None
            return var("location", end_line=token.end_line, offset_pos=token.offset_pos,
                       limit_offset_pos=token.limit_offset_pos, file=self.lexer.file, type_hint=type_hint)
        elif token.type == VECTOR:
            self.eat(VECTOR)
            if self.current_token.equals(LPAREN):
                start_line = token.start_line
                offset_pos = token.offset_pos
                self.eat(LPAREN)
                unpositional = []
                positional = []
                while self.current_token.type != EOF and self.current_token.type != RPAREN:
                    a = self.expr(assigning=True)
                    if isinstance(a, assign):
                        unpositional.append(a)
                    else:
                        positional.append(a)
                    if self.current_token.type == COMMA:
                        self.eat(COMMA)
                end_line = self.current_token.end_line
                limit_offset_pos = self.current_token.limit_offset_pos
                self.eat(RPAREN)
                return vector(
                    arg=args(positional=positional, unpositional=unpositional, start_line=start_line, end_line=end_line,
                             offset_pos=offset_pos,
                             limit_offset_pos=limit_offset_pos, file=self.lexer.file), start_line=start_line,
                    end_line=end_line, offset_pos=offset_pos, limit_offset_pos=limit_offset_pos,
                    file=self.lexer.file)
            if self.current_token.equals(COLON) and var_types:
                self.eat(COLON)
                type_hint = self.current_token.value
                self.eat(VAR)
            else:
                type_hint = None
            return var("vector", end_line=token.end_line, offset_pos=token.offset_pos,
                       limit_offset_pos=token.limit_offset_pos, file=self.lexer.file, type_hint=type_hint)
        elif token.type == POTION:
            start_line = token.start_line
            offset_pos = token.offset_pos
            self.eat(POTION)
            if self.current_token.equals(LPAREN):
                self.eat(LPAREN)
                unpositional = []
                positional = []
                while self.current_token.type != EOF and self.current_token.type != RPAREN:
                    a = self.expr(assigning=True)
                    if isinstance(a, assign):
                        unpositional.append(a)
                    else:
                        positional.append(a)
                    if self.current_token.type == COMMA:
                        self.eat(COMMA)
                end_line = self.current_token.end_line
                limit_offset_pos = self.current_token.limit_offset_pos
                self.eat(RPAREN)
                return potion(
                    arg=args(positional=positional, unpositional=unpositional, start_line=start_line, end_line=end_line,
                             offset_pos=offset_pos,
                             limit_offset_pos=limit_offset_pos, file=self.lexer.file), start_line=start_line,
                    end_line=end_line, offset_pos=offset_pos, limit_offset_pos=limit_offset_pos,
                    file=self.lexer.file)
            if self.current_token.equals(COLON) and var_types:
                self.eat(COLON)
                type_hint = self.current_token.value
                self.eat(VAR)
            else:
                type_hint = None
            return var("potion", end_line=token.end_line, offset_pos=token.offset_pos,
                       limit_offset_pos=token.limit_offset_pos, file=self.lexer.file, type_hint=type_hint)
        elif token.type == SOUND:
            start_line = token.start_line
            offset_pos = token.offset_pos
            self.eat(SOUND)
            if self.current_token.equals(LPAREN):
                self.eat(LPAREN)
                unpositional = []
                positional = []
                while self.current_token.type != EOF and self.current_token.type != RPAREN:
                    a = self.expr(assigning=True)
                    if isinstance(a, assign):
                        unpositional.append(a)
                    else:
                        positional.append(a)
                    if self.current_token.type == COMMA:
                        self.eat(COMMA)
                end_line = self.current_token.end_line
                limit_offset_pos = self.current_token.limit_offset_pos
                self.eat(RPAREN)
                return sound(
                    arg=args(positional=positional, unpositional=unpositional, start_line=start_line, end_line=end_line,
                             offset_pos=offset_pos,
                             limit_offset_pos=limit_offset_pos, file=self.lexer.file), start_line=start_line,
                    end_line=end_line, offset_pos=offset_pos, limit_offset_pos=limit_offset_pos,
                    file=self.lexer.file)
            if self.current_token.equals(COLON) and var_types:
                self.eat(COLON)
                type_hint = self.current_token.value
                self.eat(VAR)
            else:
                type_hint = None
            return var("sound", end_line=token.end_line, offset_pos=token.offset_pos,
                       limit_offset_pos=token.limit_offset_pos, file=self.lexer.file, type_hint=type_hint)
        elif token.type == PARTICLE:
            start_line = token.start_line
            offset_pos = token.offset_pos
            self.eat(PARTICLE)
            if self.current_token.equals(LPAREN):
                self.eat(LPAREN)
                unpositional = []
                positional = []
                while self.current_token.type != EOF and self.current_token.type != RPAREN:
                    a = self.expr(assigning=True)
                    if isinstance(a, assign):
                        unpositional.append(a)
                    else:
                        positional.append(a)
                    if self.current_token.type == COMMA:
                        self.eat(COMMA)
                end_line = self.current_token.end_line
                limit_offset_pos = self.current_token.limit_offset_pos
                self.eat(RPAREN)
                return particle(
                    arg=args(positional=positional, unpositional=unpositional, start_line=start_line, end_line=end_line,
                             offset_pos=offset_pos,
                             limit_offset_pos=limit_offset_pos, file=self.lexer.file), start_line=start_line,
                    end_line=end_line, offset_pos=offset_pos, limit_offset_pos=limit_offset_pos,
                    file=self.lexer.file)
            if self.current_token.equals(COLON) and var_types:
                self.eat(COLON)
                type_hint = self.current_token.value
                self.eat(VAR)
            else:
                type_hint = None
            return var("particle", end_line=token.end_line, offset_pos=token.offset_pos,
                       limit_offset_pos=token.limit_offset_pos, file=self.lexer.file, type_hint=type_hint)
        elif token.type == LPAREN:
            self.eat(LPAREN)
            result = self.expr()
            self.eat(RPAREN)
            return result
        elif token.type == LSPAREN:
            start_line = token.start_line
            offset_pos = token.offset_pos
            self.eat(LSPAREN)
            vals = []
            while self.current_token.type != EOF and self.current_token.type != RSPAREN:
                vals.append(self.expr())
                if self.current_token.type == COMMA:
                    self.eat(COMMA)
            end_line = self.current_token.end_line
            limit_offset_pos = self.current_token.limit_offset_pos
            self.eat(RSPAREN)
            return lst(vals, start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                       limit_offset_pos=limit_offset_pos, file=self.lexer.file)
        elif token.type == LCPAREN:
            start_line = token.start_line
            offset_pos = token.offset_pos
            self.eat(LCPAREN)
            keys = []
            vals = []
            while self.current_token.type != EOF and self.current_token.type != RCPAREN:
                keys.append(self.expr())
                self.eat(COLON)
                vals.append(self.expr())
                if self.current_token.type == COMMA:
                    self.eat(COMMA)
            end_line = self.current_token.end_line
            limit_offset_pos = self.current_token.limit_offset_pos
            self.eat(RCPAREN)
            return dct(keys, vals, start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                       limit_offset_pos=limit_offset_pos, file=self.lexer.file)
        elif token.type == VALUE:
            start_line = token.start_line
            offset_pos = token.offset_pos
            self.eat(VALUE)
            if self.current_token.equals(SELECTOR):
                end_line = self.current_token.end_line
                limit_offset_pos = self.current_token.limit_offset_pos
                selector = self.current_token.value
                self.eat(SELECTOR)
                return value(token.value, selector, start_line=start_line, end_line=end_line,
                             offset_pos=offset_pos, limit_offset_pos=limit_offset_pos, file=self.lexer.file)
            return value(token.value, start_line=start_line, end_line=token.end_line, offset_pos=offset_pos,
                         limit_offset_pos=token.limit_offset_pos, file=self.lexer.file)
        elif token.equals(WORLD, VARIABLE, ENTITY, CODE, PLAYER, SELECT, CONTROLLER):
            sub_action = self.current_token
            start_line = token.start_line
            offset_pos = token.offset_pos
            self.eat(self.current_token.type)
            if self.current_token.equals(SELECTOR):
                selector = self.current_token.value
                self.eat(SELECTOR)
            else:
                selector = None
            self.eat(LPAREN)
            unpositional = []
            positional = []
            while self.current_token.type != EOF and self.current_token.type != RPAREN:
                a = self.expr(assigning=True)
                if isinstance(a, assign):
                    unpositional.append(a)
                else:
                    positional.append(a)
                if self.current_token.type == COMMA:
                    self.eat(COMMA)
            end_line = self.current_token.end_line
            limit_offset_pos = self.current_token.limit_offset_pos
            self.eat(RPAREN)
            return action(sub_action.type.lower(), sub_action.value,
                          arg=args(positional=positional, unpositional=unpositional, start_line=start_line,
                                   end_line=end_line, offset_pos=offset_pos,
                                   limit_offset_pos=limit_offset_pos, file=self.lexer.file),
                          selector=selector,
                          start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                          limit_offset_pos=limit_offset_pos, file=self.lexer.file)
        else:
            error("SyntaxError", f"Неожиданный токен {self.current_token.type}",
                  start_line=self.current_token.start_line, end_line=self.current_token.end_line,
                  offset_pos=self.current_token.offset_pos, limit_offset_pos=self.current_token.limit_offset_pos,
                  file=self.lexer.file)

    def expr(self, assigning=False, work_with=None, pr=1, var_types=False):
        if self.current_token.equals(OEL):
            self.eat(OEL)
        if work_with is None:
            result = self.up_factor(assigning=assigning, work_with=work_with, var_types=var_types)
        else:
            result = work_with
        if pr == 1:
            result = self.expr(assigning=False, work_with=result, pr=2)
        if self.current_token.equals(PLUS, MINUS, MINUS_NUMBER, PLUS_NUMBER) and (pr == 0 or pr == 1):
            first = result
            while self.current_token.equals(PLUS, MINUS, MINUS_NUMBER, PLUS_NUMBER):
                start_line = result.start_line
                offset_pos = result.offset_pos
                if self.current_token.equals(MINUS_NUMBER):
                    operation = "-"
                    second = number(abs(self.current_token.value), start_line=self.current_token.start_line,
                                    end_line=self.current_token.end_line, offset_pos=self.current_token.offset_pos + 1,
                                    limit_offset_pos=self.current_token.limit_offset_pos, file=self.lexer.file)
                    self.eat(self.current_token.type)
                    if self.current_token.equals(MULTIPLY, DIVIDE, PR, DEG, INT_DIVIDE):
                        second = self.expr(work_with=second, pr=2)
                elif self.current_token.equals(PLUS_NUMBER):
                    operation = "+"
                    second = number(self.current_token.value, start_line=self.current_token.start_line,
                                    end_line=self.current_token.end_line, offset_pos=self.current_token.offset_pos + 1,
                                    limit_offset_pos=self.current_token.limit_offset_pos, file=self.lexer.file)
                    self.eat(self.current_token.type)
                    if self.current_token.equals(MULTIPLY, DIVIDE, PR, DEG, INT_DIVIDE):
                        second = self.expr(work_with=second, pr=2)
                else:
                    operation = self.current_token.value
                    self.eat(self.current_token.type)
                    second = self.expr(pr=1)
                end_line = second.end_line
                limit_offset_pos = second.limit_offset_pos
                first = math(operation=operation, first=first, second=second, start_line=start_line, end_line=end_line,
                             offset_pos=offset_pos, limit_offset_pos=limit_offset_pos, file=self.lexer.file)
            return first
        elif self.current_token.equals(MULTIPLY, DIVIDE, PR, DEG, INT_DIVIDE) and (pr == 0 or pr == 2):
            first = result
            while self.current_token.equals(MULTIPLY, DIVIDE, PR, DEG, INT_DIVIDE):
                start_line = result.start_line
                offset_pos = result.offset_pos
                operation = self.current_token.value
                self.eat(self.current_token.type)
                second = self.up_factor()
                end_line = second.end_line
                limit_offset_pos = second.limit_offset_pos
                first = math(operation=operation, first=first, second=second, start_line=start_line, end_line=end_line,
                             offset_pos=offset_pos, limit_offset_pos=limit_offset_pos, file=self.lexer.file)
            return first
        return result

    def up_factor(self, assigning=False, work_with=None, var_types=False):
        if work_with is None:
            result = self.factor(var_types=var_types)
        else:
            result = work_with
        if self.current_token.equals(LSPAREN):
            start_line = result.start_line
            offset_pos = result.offset_pos
            self.eat(LSPAREN)
            vals = []
            while self.current_token.type != EOF and self.current_token.type != RSPAREN:
                vals.append(self.expr())
                if self.current_token.type == COLON:
                    self.eat(COLON)
            end_line = self.current_token.end_line
            limit_offset_pos = self.current_token.limit_offset_pos
            self.eat(RSPAREN)
            return self.up_factor(work_with=slice(result,
                                                  arg=args(positional=vals, start_line=start_line, end_line=end_line,
                                                           offset_pos=offset_pos,
                                                           limit_offset_pos=limit_offset_pos, file=self.lexer.file),
                                                  start_line=start_line,
                                                  end_line=end_line,
                                                  offset_pos=offset_pos, limit_offset_pos=limit_offset_pos,
                                                  file=self.lexer.file))
        elif self.current_token.equals(DOT):
            start_line = result.start_line
            offset_pos = result.offset_pos
            self.eat(DOT)
            act = self.current_token.value
            end_line = self.current_token.end_line
            limit_offset_pos = self.current_token.limit_offset_pos
            self.eat(VAR)
            if self.current_token.type == LPAREN:
                self.eat(LPAREN)
                unpositional = [assign("origin", result)]
                positional = []
                while self.current_token.type != EOF and self.current_token.type != RPAREN:
                    a = self.expr(assigning=True)
                    if isinstance(a, assign):
                        unpositional.append(a)
                    else:
                        positional.append(a)
                    if self.current_token.type == COMMA:
                        self.eat(COMMA)
                end_line = self.current_token.end_line
                limit_offset_pos = self.current_token.limit_offset_pos
                self.eat(RPAREN)
                return self.up_factor(work_with=action("special", act,
                                                       arg=args(positional=positional, unpositional=unpositional,
                                                                start_line=start_line,
                                                                end_line=end_line, offset_pos=offset_pos,
                                                                limit_offset_pos=limit_offset_pos,
                                                                file=self.lexer.file),
                                                       start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                                       limit_offset_pos=limit_offset_pos, file=self.lexer.file))
            else:
                return self.up_factor(
                    work_with=atribute(result, act, start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                       limit_offset_pos=limit_offset_pos, file=self.lexer.file))
        if self.current_token.equals(ASSIGN) and assigning is True:
            start_line = result.start_line
            offset_pos = result.offset_pos
            self.eat(ASSIGN)
            second = self.expr()
            end_line = second.end_line
            limit_offset_pos = second.limit_offset_pos
            if isinstance(result, var):
                result = result.name
            elif isinstance(result, text):
                result = result.text
            elif isinstance(result, number):
                result = str(result.value)
            else:
                error("Impossible", f"значение типа {result.type} не может быть установлено как ключ",
                      result.start_line, result.end_line, result.offset_pos, result.limit_offset_pos, result.file)
            return assign(result, second, start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                          limit_offset_pos=limit_offset_pos, file=self.lexer.file)
        return result

    def statement(self, start=False):
        global symbol_table
        if self.current_token.equals(VAR, LOCAL_VAR, GAME_VAR, SAVE_VAR, INLINE_VAR, VAR_DEFINE, SAVE_DEFINE,
                                     GAME_DEFINE, LOCAL_DEFINE, INLINE_DEFINE, LOCATION, SOUND, ITEM, PARTICLE, VECTOR,
                                     POTION):
            variables = []
            start_line = self.current_token.start_line
            offset_pos = self.current_token.offset_pos
            while not self.current_token.equals(ASSIGN, PR_WITH_ASSIGN, DEG_WITH_ASSIGN, PLUS_WITH_ASSIGN,
                                                DIVIDE_WITH_ASSIGN,
                                                MINUS_WITH_ASSIGN, MULTIPLY_WITH_ASSIGN, INT_DIVIDE_WITH_ASSIGN, RPAREN,
                                                EOF, OEL, DOT):
                eat = True
                start_line = self.current_token.start_line
                offset_pos = self.current_token.offset_pos
                if self.current_token.equals(VAR_DEFINE):
                    self.eat(VAR_DEFINE)
                    var_name = self.current_token.value
                    symbol_table["variables"][var_name] = ["LOCAL", "any"]
                    var_type = "LOCAL"
                elif self.current_token.equals(SAVE_DEFINE):
                    self.eat(SAVE_DEFINE)
                    self.eat(VAR_DEFINE)
                    var_name = self.current_token.value
                    symbol_table["variables"][var_name] = ["SAVE", "any"]
                    var_type = "SAVE"
                elif self.current_token.equals(GAME_DEFINE):
                    self.eat(GAME_DEFINE)
                    self.eat(VAR_DEFINE)
                    var_name = self.current_token.value
                    symbol_table["variables"][var_name] = ["GAME", "any"]
                    var_type = "GAME"
                elif self.current_token.equals(LOCAL_DEFINE):
                    self.eat(LOCAL_DEFINE)
                    self.eat(VAR_DEFINE)
                    var_name = self.current_token.value
                    symbol_table["variables"][var_name] = ["LOCAL", "any"]
                    var_type = "LOCAL"
                elif self.current_token.equals(INLINE_DEFINE):
                    self.eat(INLINE_DEFINE)
                    self.eat(VAR_DEFINE)
                    var_name = self.current_token.value
                    symbol_table["variables"][var_name] = ["INLINE", "any"]
                    var_type = "INLINE"
                elif self.current_token.equals(VAR):
                    var_name = self.current_token.value
                    self.eat(VAR)
                    if self.current_token.equals(LPAREN):
                        self.eat(LPAREN)
                        unpositional = []
                        positional = []
                        while self.current_token.type != EOF and self.current_token.type != RPAREN:
                            a = self.expr(assigning=True)
                            if isinstance(a, assign):
                                unpositional.append(a)
                            else:
                                positional.append(a)
                            if self.current_token.type == COMMA:
                                self.eat(COMMA)
                        end_line = self.current_token.end_line
                        limit_offset_pos = self.current_token.limit_offset_pos
                        self.eat(RPAREN)
                        thing1, thing2, thing3 = try_action(
                            call_function(var_name, arg=args(positional=positional, unpositional=unpositional,
                                                             start_line=start_line, end_line=end_line,
                                                             offset_pos=offset_pos,
                                                             limit_offset_pos=limit_offset_pos,
                                                             file=self.lexer.file),
                                          start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                          limit_offset_pos=limit_offset_pos, file=self.lexer.file))
                        thing2.append(thing1)
                        thing2.extend(thing3)
                        return thing2
                    if not var_name in symbol_table["variables"].keys():
                        symbol_table["variables"][var_name] = ["LOCAL", "any"]
                    var_type = symbol_table["variables"][var_name][0]
                    eat = False
                elif self.current_token.equals(LOCAL_VAR):
                    var_name = self.current_token.value
                    if not var_name in symbol_table.keys():
                        symbol_table["variables"][var_name] = ["LOCAL", "any"]
                    var_type = "LOCAL"
                elif self.current_token.equals(GAME_VAR):
                    var_name = self.current_token.value
                    if not var_name in symbol_table.keys():
                        symbol_table["variables"][var_name] = ["GAME", "any"]
                    var_type = "GAME"
                elif self.current_token.equals(SAVE_VAR):
                    var_name = self.current_token.value
                    if not var_name in symbol_table.keys():
                        symbol_table["variables"][var_name] = ["SAVE", "any"]
                    var_type = "SAVE"
                elif self.current_token.equals(INLINE_VAR):
                    var_name = self.current_token.value
                    symbol_table["variables"][var_name] = ["INLINE", None]
                    var_type = "INLINE"
                else:
                    var_name = self.current_token.value
                    if not var_name in symbol_table.keys():
                        symbol_table["variables"][var_name] = ["LOCAL", "any"]
                    var_type = symbol_table["variables"][var_name][0]
                end_line = self.current_token.end_line
                limit_offset_pos = self.current_token.limit_offset_pos
                if self.current_token.equals(LOCATION, SOUND, ITEM, PARTICLE, VECTOR, POTION, LOCAL_VAR, GAME_VAR,
                                             INLINE_VAR, SAVE_VAR):
                    self.eat(self.current_token.type)
                elif eat:
                    self.eat(VAR)
                if self.current_token.equals(COLON):
                    self.eat(COLON)
                    type_hint = self.current_token.value
                    symbol_table["variables"][var_name][1] = type_hint
                    self.eat(VAR)
                else:
                    type_hint = None
                result = var(var_name, var_type, start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                             limit_offset_pos=limit_offset_pos, file=self.lexer.file, type_hint=type_hint)
                if self.current_token.equals(LSPAREN):
                    self.eat(LSPAREN)
                    unpositional = []
                    positional = []
                    while self.current_token.type != EOF and self.current_token.type != RSPAREN:
                        a = self.expr(assigning=True)
                        if isinstance(a, assign):
                            unpositional.append(a)
                        else:
                            positional.append(a)
                        if self.current_token.type == COLON:
                            self.eat(COLON)
                    end_line = self.current_token.end_line
                    limit_offset_pos = self.current_token.limit_offset_pos
                    self.eat(RSPAREN)
                    result = slice(result,
                                   arg=args(positional=positional, unpositional=unpositional, start_line=start_line,
                                            end_line=end_line, offset_pos=offset_pos,
                                            limit_offset_pos=limit_offset_pos, file=self.lexer.file),
                                   start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                   limit_offset_pos=limit_offset_pos, file=self.lexer.file)
                elif self.current_token.equals(DOT):
                    self.eat(DOT)
                    act = self.current_token.value
                    self.eat(VAR)
                    if self.current_token.equals(LPAREN):
                        self.eat(LPAREN)
                        unpositional = [
                            assign("origin", result, start_line=start_line, end_line=end_line,
                                   offset_pos=offset_pos,
                                   limit_offset_pos=limit_offset_pos, file=self.lexer.file)]
                        positional = []
                        while self.current_token.type != EOF and self.current_token.type != RPAREN:
                            a = self.expr(assigning=True)
                            if isinstance(a, assign):
                                unpositional.append(a)
                            else:
                                positional.append(a)
                            if self.current_token.type == COMMA:
                                self.eat(COMMA)
                        end_line = self.current_token.end_line
                        limit_offset_pos = self.current_token.limit_offset_pos
                        self.eat(RPAREN)
                        thing1, thing2, thing3 = try_action(
                            action("special", act, arg=args(positional=positional, unpositional=unpositional,
                                                            start_line=start_line, end_line=end_line,
                                                            offset_pos=offset_pos,
                                                            limit_offset_pos=limit_offset_pos,
                                                            file=self.lexer.file),
                                   start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                   limit_offset_pos=limit_offset_pos, file=self.lexer.file))
                        thing2.append(thing1)
                        thing2.extend(thing3)
                        return thing2
                    else:
                        result = atribute(result, act, start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                          limit_offset_pos=limit_offset_pos, file=self.lexer.file)
                variables.append(result)
                if self.current_token.equals(COMMA):
                    self.eat(COMMA)
            if self.current_token.equals(ASSIGN, PR_WITH_ASSIGN, DEG_WITH_ASSIGN, PLUS_WITH_ASSIGN, DIVIDE_WITH_ASSIGN,
                                         MINUS_WITH_ASSIGN, MULTIPLY_WITH_ASSIGN, INT_DIVIDE_WITH_ASSIGN):
                thing = self.current_token.value
                self.eat(self.current_token.type)
                second = self.expr()
                if second is not None:
                    end_line = second.end_line
                    limit_offset_pos = second.limit_offset_pos
                    thing1, thing2, thing3 = try_action(true_assign(thing, arg=args(positional=[second], unpositional=[
                        assign("first", variables, start_line=start_line,
                               end_line=end_line,
                               offset_pos=offset_pos,
                               limit_offset_pos=limit_offset_pos, file=self.lexer.file)],
                                                                                    start_line=start_line,
                                                                                    end_line=end_line,
                                                                                    offset_pos=offset_pos,
                                                                                    limit_offset_pos=limit_offset_pos,
                                                                                    file=self.lexer.file),
                                                                    start_line=start_line, end_line=end_line,
                                                                    offset_pos=offset_pos,
                                                                    limit_offset_pos=limit_offset_pos,
                                                                    file=self.lexer.file))
                    thing2.append(thing1)
                    thing2.extend(thing3)
                    return thing2
            if not isinstance(variables[0], var):
                if self.current_token.equals(DOT):
                    self.eat(DOT)
                    act = self.current_token
                    self.eat(VAR)
                    self.eat(LPAREN)
                    unpositional = [assign("origin", variables[0], start_line=variables[0].start_line,
                                           end_line=variables[0].end_line,
                                           offset_pos=variables[0].offset_pos,
                                           limit_offset_pos=variables[0].limit_offset_pos, file=self.lexer.file)]
                    positional = []
                    while self.current_token.type != EOF and self.current_token.type != RPAREN:
                        a = self.expr(assigning=True)
                        if isinstance(a, assign):
                            unpositional.append(a)
                        else:
                            positional.append(a)
                        if self.current_token.type == COMMA:
                            self.eat(COMMA)
                    end_line = self.current_token.end_line
                    limit_offset_pos = self.current_token.limit_offset_pos
                    self.eat(RPAREN)
                    thing1, thing2, thing3 = try_action(
                        action("special", act.value, arg=args(positional=positional, unpositional=unpositional,
                                                              start_line=act.start_line, end_line=end_line,
                                                              offset_pos=act.offset_pos,
                                                              limit_offset_pos=limit_offset_pos,
                                                              file=self.lexer.file),
                               start_line=act.start_line, end_line=end_line, offset_pos=act.offset_pos,
                               limit_offset_pos=limit_offset_pos, file=self.lexer.file))
                    thing2.append(thing1)
                    thing2.extend(thing3)
                    return thing2
                return [variables[0]]

        elif self.current_token.equals(IMPORT) and start == True:
            self.eat(IMPORT)
            thing = self.current_token.value
            self.eat(STRING)
            an_thing = create_path(self.lexer.work_dir, thing)
            if an_thing is None:
                error("UnexistsFile", f"Файл {thing} не найден.", thing.start_line, thing.end_line, thing.offset_pos,
                      thing.limit_offset_pos, thing.file)
            path, full_path = an_thing
            if not full_path in open_files:
                another_thing = Parser(Lexer(full_path, work_dir=path), self.tree)
                another_thing.parse()
            else:
                print(minecraft_based_text("&6", ignore_last_symbol=True) +
                      f"файл {full_path} уже был однажды импортирован, пропускаем" + minecraft_based_text(""))
        elif self.current_token.equals(WORLD, VARIABLE, ENTITY, REPEAT, CODE, PLAYER, SELECT, CONTROLLER):
            start_line = self.current_token.start_line
            offset_pos = self.current_token.offset_pos
            sub_action = self.current_token
            self.eat(self.current_token.type)
            if self.current_token.equals(SELECTOR):
                selector = self.current_token.value
                self.eat(SELECTOR)
            else:
                selector = None
            self.eat(LPAREN)
            unpositional = []
            positional = []
            no = None
            if self.current_token.equals(NOT):
                self.eat(NOT)
                no = True
            conditional = "conditional" in actions.setdefault(sub_action.type.lower() + "::" + sub_action.value,
                                                              {}).setdefault("type", "basic")
            while self.current_token.type != RPAREN:
                a = self.expr(assigning=True)
                if isinstance(a, assign):
                    unpositional.append(a)
                elif isinstance(a, action) and conditional == True:
                    conditional = a
                else:
                    positional.append(a)
                if self.current_token.type != RPAREN:
                    self.eat(COMMA)
            end_line = self.current_token.end_line
            limit_offset_pos = self.current_token.limit_offset_pos
            self.eat(RPAREN)
            if sub_action.equals(REPEAT):
                self.eat(LCPAREN)
                variables = []
                while (self.current_token.type != EOF and self.current_token.type != CYCLE_THING and
                       self.current_token.type != OEL):
                    variables.append(self.expr())
                    if self.current_token.type != CYCLE_THING and self.current_token.type != OEL:
                        self.eat(COMMA)
                if len(variables) > 0:
                    unpositional.append(
                        assign(f"lambda", variables, start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                               limit_offset_pos=limit_offset_pos, file=self.lexer.file))
                if self.current_token.equals(CYCLE_THING):
                    self.eat(CYCLE_THING)
                acts = []
                while self.current_token.type != EOF and self.current_token.type != RCPAREN:
                    a = self.statement()
                    if a is not None:
                        acts.extend(a)
                operations = lst(acts, start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                 limit_offset_pos=limit_offset_pos, file=self.lexer.file)
                end_line = self.current_token.end_line
                limit_offset_pos = self.current_token.limit_offset_pos
                self.eat(RCPAREN)
            elif sub_action.equals(CONTROLLER):
                self.eat(LCPAREN)
                unpositional = []
                acts = []
                while self.current_token.type != EOF and self.current_token.type != RCPAREN:
                    a = self.statement()
                    if a is not None:
                        acts.extend(a)
                operations = lst(acts, start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                 limit_offset_pos=limit_offset_pos, file=self.lexer.file)
                end_line = self.current_token.end_line
                limit_offset_pos = self.current_token.limit_offset_pos
                self.eat(RCPAREN)
            else:
                operations = None
            thing1, thing2, thing3 = try_action(action(sub_action.type.lower(), sub_action.value,
                                                       arg=args(positional=positional, unpositional=unpositional,
                                                                start_line=start_line,
                                                                end_line=end_line, offset_pos=offset_pos,
                                                                limit_offset_pos=limit_offset_pos,
                                                                file=self.lexer.file),
                                                       selector=selector,
                                                       no=no,
                                                       start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                                       limit_offset_pos=limit_offset_pos, file=self.lexer.file,
                                                       operations=operations,
                                                       conditional=conditional if isinstance(conditional,
                                                                                             action) else None))
            thing2.append(thing1)
            thing2.extend(thing3)
            return thing2
        elif self.current_token.equals(FUNCTION) and start == True:
            start_line = self.current_token.start_line
            offset_pos = self.current_token.offset_pos
            self.eat(FUNCTION)
            function_name = self.current_token.value
            self.eat(VAR)
            self.eat(LPAREN)
            positional = []
            while self.current_token.type != RPAREN:
                positional.append(self.expr(var_types=True))
                if self.current_token.type != RPAREN:
                    self.eat(COMMA)
            self.eat(RPAREN)
            self.eat(LCPAREN)
            vals = []
            while self.current_token.type != EOF and self.current_token.type != RCPAREN:
                a = self.statement()
                if a is not None:
                    vals.extend(a)
            end_line = self.current_token.end_line
            limit_offset_pos = self.current_token.limit_offset_pos
            self.eat(RCPAREN)
            return [function(function_name, lst(vals, start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                                limit_offset_pos=limit_offset_pos, file=self.lexer.file),
                             arg=positional,
                             start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                             limit_offset_pos=limit_offset_pos, file=self.lexer.file)]
        elif self.current_token.equals(PROCESS) and start == True:
            start_line = self.current_token.start_line
            offset_pos = self.current_token.offset_pos
            self.eat(PROCESS)
            process_name = self.current_token.value
            self.eat(VAR)
            self.eat(LPAREN)
            self.eat(RPAREN)
            self.eat(LCPAREN)
            vals = []
            while self.current_token.type != EOF and self.current_token.type != RCPAREN:
                a = self.statement()
                if a is not None:
                    vals.extend(a)
            end_line = self.current_token.end_line
            limit_offset_pos = self.current_token.limit_offset_pos
            self.eat(RCPAREN)
            return [process(process_name, lst(vals, start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                              limit_offset_pos=limit_offset_pos, file=self.lexer.file),
                            start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                            limit_offset_pos=limit_offset_pos, file=self.lexer.file)]
        elif self.current_token.equals(EVENT) and start == True:
            start_line = self.current_token.start_line
            offset_pos = self.current_token.offset_pos
            event_name = self.current_token.value
            self.eat(EVENT)
            self.eat(LCPAREN)
            vals = []
            while self.current_token.type != EOF and self.current_token.type != RCPAREN:
                a = self.statement()
                if a is not None:
                    vals.extend(a)
            end_line = self.current_token.end_line
            limit_offset_pos = self.current_token.limit_offset_pos
            self.eat(RCPAREN)
            return [event(event_name, lst(vals), start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                          limit_offset_pos=limit_offset_pos, file=self.lexer.file)]
        elif self.current_token.equals(IF, ELSE):
            start_line = self.current_token.start_line
            offset_pos = self.current_token.offset_pos
            act1 = self.current_token
            self.eat(self.current_token.type)
            act = None
            if act1.equals(IF):
                no = False
                if self.current_token.equals(NOT):
                    self.eat(NOT)
                    no = not no
                self.eat(LPAREN)
                if self.current_token.equals(NOT):
                    self.eat(NOT)
                    no = not no
                act = self.expr()
                act.no = no
                self.eat(RPAREN)
            self.eat(LCPAREN)
            vals = []
            while self.current_token.type != EOF and self.current_token.type != RCPAREN:
                a = self.statement()
                if a is not None:
                    vals.extend(a)
            end_line = self.current_token.end_line
            limit_offset_pos = self.current_token.limit_offset_pos
            self.eat(RCPAREN)
            if act1.equals(IF):
                return [if_(act, lst(vals), start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                            limit_offset_pos=limit_offset_pos, file=self.lexer.file)]
            else:
                return [else_(lst(vals), start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                              limit_offset_pos=limit_offset_pos, file=self.lexer.file)]
        elif self.current_token.equals(OEL):
            self.eat(OEL)
        elif self.current_token.equals(EL):
            self.eat(EL)
        else:
            error("SyntaxError", f"Неожиданный токен {self.current_token.type}",
                  start_line=self.current_token.start_line, end_line=self.current_token.end_line,
                  offset_pos=self.current_token.offset_pos, limit_offset_pos=self.current_token.limit_offset_pos,
                  file=self.lexer.file)

    def parse(self):
        while self.current_token.type != EOF:
            a = self.statement(start=True)
            if a is not None:
                self.tree.extend(a)

    def compile(self):
        self.parse()
        acts = []
        default = []
        for i in self.tree:
            if not type(i) in (function, process, event):
                acts.append(i)
            else:
                default.append(i)
        self.tree = default
        if len(acts) != 0:
            self.tree.insert(0, event("world_start", lst(acts)))
        eventes, additional_events = lst(self.tree).json(normal=True, with_ret=True)
        eventes.extend(additional_events)
        return json.dumps({"handlers": eventes}, indent=2)


def compile_file(file, upload=False, compress=False):
    global open_files, symbol_table, global_count, global_func_count, actions, origin_actions, events, values
    open_files = {}
    symbol_table = {"variables": {}, "functions": {}}
    tree = []
    global_count = -1
    global_func_count = 0
    thing = create_path(os.getcwd(), file)
    if thing is None:
        print(minecraft_based_text(f"&cUnexistsFile : Файл {file} не найден."))
        sys.exit()
    dir_path, full_path = thing
    for i in json.load(open("data/actions.json")):
        actions[i["object"] + "::" + i["name"]] = i
        if "origin" in i:
            origin_actions[i["name"]] = i["object"] + "::" + i["name"]
        else:
            non_origin_actions[i["name"]] = i["object"] + "::" + i["name"]
    for i in json.load(open("data/events.json")):
        events[i["id"]] = i
    for i in json.load(open("data/values.json")):
        values[i["id"]] = i
    lexer = Lexer(full_path, work_dir=dir_path)
    thing = Parser(lexer, tree)
    code = thing.compile()
    if not upload:
        file_name = full_path.replace(dir_path, "", 1)
        i2 = file_name.rfind(".")
        new_file_name = file_name[:i2] + ".json"
        if compress:
            open(dir_path + "/" + new_file_name, "wb").write(gzip.compress(code.encode('utf-8')))
        else:
            open(dir_path + "/" + new_file_name, "w").write(code)
    else:
        response = requests.post('https://m.justmc.ru/api/upload', data=code).json()["id"]
        print(minecraft_based_text(f"&aФайл успешно загружен\n\n&7Используйте данную команду на сервере для загрузки "
                                   f"модуля:\n&9/module loadUrl force https://m.justmc.ru/api/{response}\n"
                                   f"\n&eВажно &fМодуль по ссылке удалится через &c3 минуты!"
                                   f"\n      &fУспейте использовать команду на сервере за данное время"))
    exit()


global_func_count = 0
global_count = 0
var_count = -1
symbol_table = dict()
actions = dict()
origin_actions = dict()
non_origin_actions = dict()
allowed_actions = ["=", "+=", "-=", "%=", "^=", "//=", "/=", "*=", "subscript"]
math_functions = {"round": ["first", "second"], "floor": ["first"], "ceil": ["first"], "abs": ["first"],
                  "sqrt": ["first"], "cbrt:": ["first"], "pow": ["first"], "min": ["first", "second"],
                  "max": ["first", "second"],
                  "sign": ["first"]}
events = dict()
values = dict()
#compile_file("a.jc", upload=False)
