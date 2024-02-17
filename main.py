import json
import os
import sys
import gzip

from math import floor, ceil
from codecs import open

import requests

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
color_codes = {"0": "#000000", "1": "#0000AA", "2": "#00AA00", "3": "#00AAAA", "4": "#AA0000", "5": "#AA00AA",
               "6": "#FFAA00", "7": "#AAAAAA", "8": "#555555", "9": "#5555FF", "a": "#55FF55", "b": "#55FFFF",
               "c": "#FF5555", "d": "#FF55FF", "e": "#FFFF55", "f": "#FFFFFF"}
codes = {"r": "\x1b[0m", "l": "\x1b[1m", "o": "\x1b[3m", "n": "\x1b[4m", "k": "\x1b[40m"}
for k, v in color_codes.items():
    r, g, b = [int(v[i:i + 2], 16) for i in range(1, len(v), 2)]
    codes[k] = f"\x1b[38;2;{r};{g};{b}m"
allowed_symbols = "0123456789abcdefABCDEF"


def minecraft_text(text):
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
    while (s := next_symbol(text, pos))[1] is not None:
        pos, symbol = s[0], s[1]
        if symbol == "&" and (s := next_symbol(text, pos))[1] is not None:
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
                if (s := next_symbol(text, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if not symbol in allowed_symbols:
                        msg += "&" + thing
                        continue
                if (s := next_symbol(text, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if not symbol in allowed_symbols:
                        msg += "&" + thing
                        continue
                if (s := next_symbol(text, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if not symbol in allowed_symbols:
                        msg += "&" + thing
                        continue
                if (s := next_symbol(text, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if not symbol in allowed_symbols:
                        msg += "&" + thing
                        continue
                if (s := next_symbol(text, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if not symbol in allowed_symbols:
                        msg += "&" + thing
                        continue
                if (s := next_symbol(text, pos))[1] is not None:
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
        msg = ""
    return full_msg


def minecraft_based_text(text, ignore_last_symbol=False):
    if ignore_last_symbol is False:
        text = text + "&r"

    def next_symbol(afsd, fdsa):
        if fdsa >= len(afsd):
            return fdsa + 1, None
        return fdsa + 1, afsd[fdsa]

    pos = 0
    msg = ""
    while (s := next_symbol(text, pos))[1] is not None:
        pos, symbol = s[0], s[1]
        if symbol == "&" and (s := next_symbol(text, pos))[1] is not None:
            pos, symbol = s[0], s[1]
            if symbol in codes:
                msg += codes[symbol]
                continue
            elif symbol == "#":
                thing = "#"
                if (s := next_symbol(text, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if not symbol in allowed_symbols:
                        msg += "&" + thing
                        continue
                if (s := next_symbol(text, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if not symbol in allowed_symbols:
                        msg += "&" + thing
                        continue
                if (s := next_symbol(text, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if not symbol in allowed_symbols:
                        msg += "&" + thing
                        continue
                if (s := next_symbol(text, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if not symbol in allowed_symbols:
                        msg += "&" + thing
                        continue
                if (s := next_symbol(text, pos))[1] is not None:
                    pos, symbol = s[0], s[1]
                    thing += symbol
                    if not symbol in allowed_symbols:
                        msg += "&" + thing
                        continue
                if (s := next_symbol(text, pos))[1] is not None:
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


def fix_operations_len(operations, limit=43):
    global global_func_count, global_count

    def get_operations_len(ops, coun=True):
        op_count = 0
        for i in ops:
            op_count += 1
            if "operations" in i.keys():
                op_count += get_operations_len(i["operations"]) + coun
        return op_count

    op_count = get_operations_len(operations)
    additional_events = []
    if op_count > limit:
        i = 0
        s_i = 0
        now_operations = [operations]
        now_i = [0]
        cur_i = [0]
        act_i = [0]
        op_count = get_operations_len(operations, coun=False)
        new_ops = []
        while i < op_count:
            if now_i[-1] >= len(now_operations[-1]):
                a = False
                while now_i[-1] >= len(now_operations[-1]):
                    if len(now_operations) == 1:
                        if s_i >= limit and now_i[-1] > 1:
                            while now_operations[-1][ceil(now_i[-1] / 2)]["action"] == "else":
                                now_i[-1]+=1
                            while s_i > limit:
                                new_ops.append(now_operations[-1][:ceil(now_i[-1] / 2)])
                                s_i -= ceil(now_i[-1] / 2)
                                now_i[-1] -= ceil(now_i[-1] / 2)
                                now_operations[-1] = now_operations[-1][ceil(now_i[-1] / 2):]
                            s_i = 0
                            now_i[-1] = 0
                            cur_i[-1] = 0
                        new_ops.append(now_operations[-1])
                        a = True
                        break
                    else:
                        if cur_i[-1] >= limit and now_i[-1] > 1:
                            an_ops = [[]]
                            first = limit
                            while cur_i[-1] >= limit - 1:
                                an_ops.append(now_operations[-1][:first])
                                now_operations[-1] = now_operations[-1][first:]
                                cur_i[-1] -= first
                                first = limit - 1
                            an_ops.append(now_operations[-1])
                            for i1 in range(1, len(an_ops)):
                                global_func_count += 1
                                global_count += 1
                                an_ops[i1 - 1].append({"action": "call_function", "values": [
                                    {"name": "function_name",
                                     "value": {"type": "text", "text": f"jmcc.{global_func_count}",
                                               "parsing": "legacy"}}]})
                                additional_events.append(
                                    {"type": "function", "position": global_count, "operations": an_ops[i1],
                                     "is_hidden": False, "name": f"jmcc.{global_func_count}"})
                            now_operations[-2][act_i[-1]]["operations"] = an_ops[0]
                            s_i-=cur_i[-1]
                            cur_i[-1] = 1
                        elif s_i > limit and cur_i[-1] > 1 and now_i[-1] > 1:
                            if cur_i[-1] + cur_i[-2] > limit:
                                global_func_count += 1
                                global_count += 1
                                now_operations[-2][act_i[-1]]["operations"] = [{"action": "call_function", "values": [
                                    {"name": "function_name",
                                     "value": {"type": "text", "text": f"jmcc.{global_func_count}",
                                               "parsing": "legacy"}}]}]
                                additional_events.append(
                                    {"type": "function", "position": global_count, "operations": now_operations[-1],
                                     "is_hidden": False, "name": f"jmcc.{global_func_count}"})
                                s_i -= cur_i[-1]+1
                                cur_i[-1] = 1
                    del now_operations[-1]
                    del now_i[-1]
                    if len(now_operations) > 0:
                        cur_i[-2] += cur_i[-1]
                    del cur_i[-1]
                    del act_i[-1]
                if a == True:
                    break
            if len(now_operations) == 1 and s_i >= limit - 1 and now_operations[-1][now_i[-1]]["action"] != "else":
                new_ops.append(now_operations[-1][:now_i[-1]])
                now_operations[-1] = now_operations[-1][now_i[-1]:]
                s_i = 0
                now_i[-1] = 0
                cur_i[-1] = 0
            if "operations" in now_operations[-1][now_i[-1]].keys():
                now_operations.append(now_operations[-1][now_i[-1]]["operations"])
                s_i += 1
                act_i.append(now_i[-1])
                now_i[-1] += 1
                cur_i.append(1)
                now_i.append(0)
            now_i[-1] += 1
            i += 1
            s_i += 1
            cur_i[-1] += 1
        for i in range(1, len(new_ops)):
            global_func_count += 1
            global_count += 1
            new_ops[i - 1].append({"action": "call_function", "values": [{"name": "function_name",
                                                                          "value": {"type": "text",
                                                                                    "text": f"jmcc.{global_func_count}",
                                                                                    "parsing": "legacy"}}]})
            additional_events.append(
                {"type": "function", "position": global_count, "operations": new_ops[i], "is_hidden": False,
                 "name": f"jmcc.{global_func_count}"})
        operations = new_ops[0]

    return operations, additional_events


def create_path(now_path, need_path):
    if os.path.isfile(need_path):
        full_path = os.path.abspath(need_path).replace("\\", "/").split("/")
        dir_path = full_path[:len(full_path) - 1]
        dir_path, full_path = "/".join(dir_path), "/".join(full_path)
        return dir_path, full_path
    else:
        a = now_path.replace("\\", "/").split("/")
        b = need_path.replace("\\", "/").split("/")
        if b[0].count(".") == len(b[0]):
            back = len(b[0]) - 1
            del b[0]
        else:
            back = 0

        full_path = a[:len(a) - back]
        full_path.extend(b)
        dir_path = full_path.copy()
        del dir_path[-1]
        dir_path, full_path = "/".join(dir_path), "/".join(full_path)
        if os.path.isfile(full_path):
            return dir_path, full_path
    return None


class Error:
    def __init__(self, error_type, arg="None", start_line=0, end_line=0, offset_pos=0, limit_offset_pos=0, file="None"):
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

    def __init__(self, token_type, value, start_line=0, end_line=0, offset_pos=0, limit_offset_pos=0, file=""):
        self.type = token_type
        self.value = value
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

    def equals(self, *args, need=False):
        for i in args:
            if self.type == i:
                return True
        if need == True:
            Error("SyntaxError", f"Ожидался один из токенов ({', '.join(args)}), но был получен {self.type}",
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
        open_files[self.file] = open(self.file, "r", "UTF-8").read()
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
                    if block_next_symbol == True:
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
                    Error("IncorrectSymbol", "Строка не была закрыта", start_line=start_line, end_line=self.line,
                          offset_pos=start_pos, limit_offset_pos=self.offset_pos + 1, file=self.file)
            if self.current_char == '"':
                start_pos = self.offset_pos
                start_line = self.line
                self.advance()
                string_value = ""
                block_next_symbol = False
                while self.current_char is not None and (self.current_char != '"' or block_next_symbol is True):
                    if block_next_symbol == True:
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
                    Error("IncorrectSymbol", "Строка не была закрыта", start_line=start_line, end_line=self.line,
                          offset_pos=start_pos, limit_offset_pos=self.offset_pos + 1, file=self.file)
            if self.current_char == '`':
                start_pos = self.offset_pos
                start_line = self.line
                self.advance()
                var_name = ""
                block_next_symbol = False
                while self.current_char is not None and (self.current_char != '`' or block_next_symbol is True):
                    if block_next_symbol == True:
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
                    Error("IncorrectSymbol", "Переменная не была закрыта", start_line=start_line, end_line=self.line,
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
                    Error("IncorrectSymbol", "Селектор не был закрыт", start_line=start_line, end_line=self.line,
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
                        if block_next_symbol == True:
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
                        Error("IncorrectSymbol", "Переменная не была закрыта", start_line=start_line,
                              end_line=self.line, offset_pos=start_pos, limit_offset_pos=self.offset_pos,
                              file=self.file)
                if self.current_char == "\"" and token_value in (
                        "p", "plain", "l", "legacy", "m", "minimessage", "j", "json"):
                    self.advance()
                    string_value = ""
                    block_next_symbol = False
                    while self.current_char is not None and (self.current_char != '"' or block_next_symbol is True):
                        if block_next_symbol == True:
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
                        Error("IncorrectSymbol", "Строка не была закрыта", start_line=start_line, end_line=self.line,
                              offset_pos=start_pos, limit_offset_pos=self.offset_pos, file=self.file)
                if self.current_char == "\'" and token_value in (
                        "p", "plain", "l", "legacy", "m", "minimessage", "j", "json"):
                    self.advance()
                    string_value = ""
                    block_next_symbol = False
                    while self.current_char is not None and (self.current_char != '\'' or block_next_symbol is True):
                        if block_next_symbol == True:
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
                        Error("IncorrectSymbol", "Строка не была закрыта", start_line=start_line, end_line=self.line,
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
                        Error("IncorrectSymbol", "Значение ивента не было закрыто", start_line=start_line,
                              end_line=self.line,
                              offset_pos=start_pos, limit_offset_pos=self.offset_pos, file=self.file)
                if self.current_char == ":" and token_value in (
                        "value", "player", "variable", "code", "repeat", "entity", "world", "select", "controller"):
                    action = token_value
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
                            self.last_token = Token(action.upper(), sub_action, start_line=start_line,
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

            Error("SyntaxError", f"Неизвестный символ &4&n{self.current_char}", start_line=self.line,
                  offset_pos=self.offset_pos, file=self.file)
        self.last_token = Token(EOF, None, start_line=self.line, offset_pos=self.offset_pos, file=self.file)
        return self.last_token


class assign:
    def __init__(self, key, value, start_line=None, end_line=None, offset_pos=None, limit_offset_pos=None, file=None):
        self.key = key
        self.value = value
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file

    def __str__(self):
        return f'a({self.key}={self.value})'

    def __repr__(self):
        return self.__str__()


class args:
    def __init__(self, arg_list=None, positional=None, unpositional=None, start_line=None, end_line=None,
                 offset_pos=None,
                 limit_offset_pos=None, file=None, assigning=None, origin=None, lamba=None):
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
        self.get_args()

    def get_args(self):
        self.args = dict()
        if self.arg_list is not None:
            dct = [None] * len(self.arg_list)
            for i in self.unpositional:
                if i.key == "assigning":
                    i.key = self.assigning[0]
                elif i.key == "origin":
                    i.key = self.origin
                elif i.key.startswith("lamba") and self.lamba is not None:
                    i.key = self.lamba[int(i.key[6:]) - 1]
                if type(i.key) != var:
                    if i.key in self.arg_list:
                        dct[self.arg_list.index(i.key)] = i.value
                    else:
                        Error("UnexistsArgument",f"Указан несуществующий аргумент : {i.key}",i.start_line,i.end_line,i.offset_pos,i.limit_offset_pos,i.file)
                else:
                    dct[self.arg_list.index(i.key.name)] = i.value
            i1 = 0
            if len(dct) != 0:
                for i in self.positional:
                    while dct[i1] != None:
                        i1 += 1
                    dct[i1] = i
                for i in range(len(dct)):
                    self.args[self.arg_list[i]] = dct[i]
        return self.args

    def __str__(self):
        return f'args(unpositional={self.unpositional},positional={self.positional})'

    def __repr__(self):
        return self.__str__()


class text:
    def __init__(self, text, text_type="legacy", start_line=None, end_line=None, offset_pos=None, limit_offset_pos=None,
                 file=None):
        self.text_type = text_type
        self.text = text
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
        if normal == False:
            return {"type": "text", "text": self.text, "parsing": self.text_type}, []
        return self.text, []


class number:
    def __init__(self, value, start_line=None, end_line=None, offset_pos=None, limit_offset_pos=None, file=None):
        self.type = "number"
        self.value = value
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
        if in_text == True:
            return str(self.value)
        if normal == False:
            return {"type": "number", "number": self.value}, []
        return self.value, []


class lst:
    def __init__(self, values, start_line=None, end_line=None, offset_pos=None, limit_offset_pos=None, file=None):
        self.type = "array"
        self.values = values
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file

    def __str__(self):
        return f'lst({', '.join(list(map(str, self.values)))})'

    def __repr__(self):
        return self.__str__()

    def json(self, normal=False):
        additional_actions = []
        values = []
        for i in self.values:
            if type(i) == var and i.var_type == "INLINE":
                a=symbol_table["inlines"][i.name]
                values.append(a)
            else:
                a, additional = i.json()
                values.append(a)
                additional_actions.extend(additional)
        if normal == False:
            return {"type": "array", "values": actions}, additional_actions
        return values, additional_actions


class dct:
    def __init__(self, keys, values, start_line=None, end_line=None, offset_pos=None, limit_offset_pos=None, file=None):
        self.type = "map"
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        self.keys = keys
        self.values = values

    def __str__(self):
        return "dct(" + f'{",".join([f'{self.keys[i]}:{self.values[i]}' for i in range(len(self.keys))])})' + ")"

    def __repr__(self):
        return self.__str__()

    def json(self, normal=True):
        additional_actions = []
        if normal == False:
            return None, additional_actions
        dct = dict()
        for i in range(len(self.keys)):
            a, additional = self.keys[i].json(normal=True)
            additional_actions.extend(additional)
            b, additional = self.values[i].json(normal=True)
            additional_actions.extend(additional)
            dct[a] = b
        return dct, additional_actions


def check(checking=None, *args):
    if checking is None:
        return checking
    for i in args:
        if checking.type == i:
            return checking
    Error("TypeError", f"Ожидался объект типа ({",".join(args)}), но был получен {checking.type}",
          start_line=checking.start_line, end_line=checking.end_line, offset_pos=checking.offset_pos,
          limit_offset_pos=checking.limit_offset_pos, file=checking.file)


class item:
    def __init__(self, id=None, name=None, count=None, lore=None, nbt=None, args=None, start_line=None, end_line=None,
                 offset_pos=None, limit_offset_pos=None, file=None):
        self.type = "item"
        if args != None:
            args.arg_list = ["id", "name", "count", "lore", "nbt"]
            args = args.get_args()
            id = args["id"]
            name = args["name"]
            count = args["count"]
            if count is None:
                count = number(1)
            lore = args["lore"]
            nbt = args["nbt"]
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        self.id = check(id, "text")
        self.name = check(name, "text")
        self.count = check(count, "text", "number")
        self.lore = check(lore, "text", "array")
        self.nbt = check(nbt, "map")

    def __str__(self):
        return f'item({self.id},{self.name},{self.lore},{self.nbt})'

    def __repr__(self):
        return self.__str__()

    def json(self):
        try:
            id = self.id.json(normal=True)
            if type(id) != str:
                raise Exception
            count = self.count.json(normal=True)
            if type(count) != int:
                raise Exception
            a = {"id": id, "Count": count}
            if self.nbt is not None:
                nbt = self.nbt.json(normal=True)
                if type(nbt) != dict:
                    raise Exception
                a["tag"] = nbt
            if self.name is not None or self.lore is not None:
                if not "tag" in a.keys():
                    a["tag"] = {}
                if not "display" in a.keys():
                    a["tag"]["display"] = {}
                if self.name is not None:
                    a["tag"]["display"]["Name"] = json.dumps(minecraft_text(self.name.json(normal=True)))
                if self.lore is not None:
                    if self.lore.type != "array":
                        lore = self.lore.json(normal=True).split("\\n")
                    else:
                        lore = self.lore.json(normal=True)
                    a["tag"]["display"]["Lore"] = list(map(json.dumps, map(minecraft_text, lore)))
            return {"type": "item", "item": json.dumps(a)}, []
        except Exception as e:
            Error("WrongItem", "Неправильно созданный предмет", self.start_line, self.end_line, self.offset_pos,
                  self.limit_offset_pos, self.file)


class location:
    def __init__(self, x=None, y=None, z=None, yaw=number(0), pitch=number(0), args=None, start_line=None,
                 end_line=None, offset_pos=None, limit_offset_pos=None, file=None):
        self.type = "location"
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        if args != None:
            args.arg_list = ["x", "y", "z", "yaw", "pitch"]
            args = args.get_args()
            x = args["x"]
            y = args["y"]
            z = args["z"]
            yaw = args["yaw"]
            if yaw is None:
                yaw = number(0)
            pitch = args["pitch"]
            if pitch is None:
                pitch = number(0)
        self.x = check(x, "variable", "number")
        self.y = check(y, "variable", "number")
        self.z = check(z, "variable", "number")
        self.yaw = check(yaw, "variable", "number")
        self.pitch = check(pitch, "variable", "number")

    def __str__(self):
        return f'location({self.x},{self.y},{self.z},{self.yaw},{self.pitch})'

    def __repr__(self):
        return self.__str__()

    def json(self):
        return {"type": "location", "x": self.x.json(normal=True), "y": self.y.json(normal=True),
                "z": self.z.json(normal=True), "yaw": self.yaw.json(normal=True),
                "pitch": self.pitch.json(normal=True)}, []


class vector:
    def __init__(self, x=None, y=None, z=None, args=None, start_line=None, end_line=None, offset_pos=None,
                 limit_offset_pos=None, file=None):
        self.type = "vector"
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        if args != None:
            args.arg_list = ["x", "y", "z"]
            args = args.get_args()
            x = args["x"]
            y = args["y"]
            z = args["z"]
        self.x = check(x, "variable", "number")
        self.y = check(y, "variable", "number")
        self.z = check(z, "variable", "number")

    def __str__(self):
        return f'vector({self.x},{self.y},{self.z})'

    def __repr__(self):
        return self.__str__()

    def json(self):
        return {"type": "vector", "x": self.x.json(normal=True), "y": self.y.json(normal=True),
                "z": self.z.json(normal=True)}, []


class potion:
    def __init__(self, potion=None, amplifier=number(0), duration=number(0), args=None, start_line=None, end_line=None,
                 offset_pos=None, limit_offset_pos=None, file=None):
        self.type = "potion"
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        if args is not None:
            args.arg_list = ["potion", "amplifier", "duration"]
            args = args.get_args()
            potion = args["potion"]
            amplifier = args["amplifier"]
            if amplifier is None:
                amplifier = number(0)
            duration = args["duration"]
            if duration is None:
                duration = number(0)
        self.potion = check(potion, "variable", "number")
        self.amplifier = check(amplifier, "variable", "number")
        self.duration = check(duration, "variable", "number")

    def __str__(self):
        return f'potion({self.potion},{self.amplifier},{self.duration})'

    def __repr__(self):
        return self.__str__()


class sound:
    def __init__(self, sound=None, volume=number(0), pitch=number(0), args=None, start_line=None, end_line=None,
                 offset_pos=None, limit_offset_pos=None, file=None):
        self.type = "sound"
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        if args is not None:
            args.arg_list = ["sound", "volume", "pitch"]
            args = args.get_args()
            sound = args["sound"]
            volume = args["volume"]
            if volume is None:
                volume = number(0)
            pitch = args["pitch"]
            if pitch is None:
                pitch = number(0)
        self.sound = check(sound, "text", "variable")
        self.volume = check(volume, "variable", "number")
        self.pitch = check(pitch, "variable", "number")

    def __str__(self):
        return f'sound({self.sound},{self.volume},{self.pitch})'

    def __repr__(self):
        return self.__str__()


class particle:
    def __init__(self, particle=None, count=number(0), spread_x=number(0), spread_y=number(0), motion_x=number(0),
                 motion_y=number(0), motion_z=number(0), material=None, color=None, args=None, start_line=None,
                 end_line=None,
                 offset_pos=None, limit_offset_pos=None, file=None):
        self.type = "sound"
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        if args is not None:
            args.arg_list = ["particle", "count", "spread_x", "spread_y", "motion_x", "motion_y", "motion_z",
                             "material", "color", "size"]
            args = args.get_args()
            particle = args["particle"]
            count = args["count"]
            if count is None:
                count = number(1)
            spread_x = args["spread_x"]
            if spread_x is None:
                spread_x = number(0)
            spread_y = args["spread_y"]
            if spread_y is None:
                spread_y = number(0)
            motion_x = args["motion_x"]
            if motion_x is None:
                motion_x = number(0)
            motion_y = args["motion_y"]
            if motion_y is None:
                motion_y = number(0)
            motion_z = args["motion_z"]
            if motion_z is None:
                motion_z = number(0)
            material = args["material"]
            color = args["color"]
            size = args["size"]
            if size is None:
                size = number(0)
        self.particle = check(particle, "variable", "text")
        self.count = check(count, "variable", "number")
        self.spread_x = check(spread_x, "variable", "number")
        self.spread_y = check(spread_y, "variable", "number")
        self.motion_x = check(motion_x, "variable", "number")
        self.motion_y = check(motion_y, "variable", "number")
        self.motion_z = check(motion_y, "variable", "number")
        self.material = check(material, "variable", "text")
        self.color = check(color, "variable", "text")
        self.size = check(color, "variable", "number")

    def __str__(self):
        return f'particle({self.particle},{self.count},{self.spread_x},{self.spread_y},{self.motion_x},{self.motion_y},{self.material},{self.color},{self.size})'

    def __repr__(self):
        return self.__str__()

    def json(self):
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
        return a, []


class value:
    def __init__(self, name, selector=None, start_line=None, end_line=None, offset_pos=None, limit_offset_pos=None,
                 file=None):
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        if not name in values.keys():
            Error("UnexistsValue", f"Указано несуществующее игровое значение {name}", start_line, end_line, offset_pos,
                  limit_offset_pos, file)
        self.name = name
        if selector is None:
            selector = "default"
        if not selector in (
                "current", "default", "default_entity", "killer_entity", "damager_entity", "victim_entity",
                "shooter_entity",
                "projectile", "last_entity"):
            Error("UnexistsSelector", f"Указан несуществующий селектор {selector}", start_line, end_line, offset_pos,
                  limit_offset_pos, file)
        self.selector = selector
        self.type = values[name]["type"]

    def __str__(self):
        return f'value({self.name},{self.selector})'

    def __repr__(self):
        return self.__str__()

    def json(self):
        return {"type": "game_value", "game_value": values[self.name]["id"],
                "selection": json.dumps({"type": self.selector})}, []


def try_action(act):
    if act.sub_action == "=":
        if type(act.args.unpositional[0].value) == var and act.args.unpositional[0].value.var_type == "INLINE":
            symbol_table["inlines"][act.args.unpositional[0].value.name] = act.args.positional[0]
            return
        if type(act.args.unpositional[0].value) == action:
            if act.args.unpositional[0].value.sub_action == "subscript":
                if type(act.args.positional[0]) in (
                        number, text, item, sound, particle, vector, location, potion, value, var):
                    return try_action(action("variable", "set_list_value", args(
                        unpositional=[act.args.unpositional[0].value.args.unpositional[0],
                                      assign("origin", act.args.unpositional[0].value.args.unpositional[0].value,act.args.unpositional[0].value.args.unpositional[0].start_line,act.args.unpositional[0].value.args.unpositional[0].end_line,act.args.unpositional[0].value.args.unpositional[0].offset_pos,act.args.unpositional[0].value.args.unpositional[0].limit_offset_pos,act.args.unpositional[0].value.args.unpositional[0].file)],
                        positional=[act.args.unpositional[0].value.args.positional[0], act.args.positional[0]]),None,None,act.start_line,act.end_line,act.offset_pos,act.limit_offset_pos,act.file))
                else:
                    Error("WrongAction",
                          f"Ожидался один из типов, но был получен {act.args.positional[0].__class__.__name__}",
                          act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos, act.file)
        if type(act.args.positional[0]) == action:
            if act.args.positional[0].sub_action == "subscript":
                if len(act.args.positional[0].args.positional) == 2:
                    act.args.unpositional.extend([assign("origin", act.args.positional[0].args.positional[0]),
                                                  assign("number", act.args.positional[0].args.positional[1])])
                    return try_action(action("variable", "get_list_value",
                                             args(unpositional=act.args.unpositional), act.args.positional[0].selector,
                                             act.args.positional[0].no, act.start_line, act.end_line, act.offset_pos,
                                             act.limit_offset_pos, act.file))
                # elif len(act.args.positional[0].args.values) == 3:
                #    pass
                # elif len(act.args.positional[0].args.values) == 4:
                #    pass
                else:
                    Error("WrongSlice", "Slice не может состоять из более чем 3 объектов",
                          act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos, act.file)
            if "assigning" in actions[act.args.positional[0].sub_action].keys():
                act.args.unpositional.extend(act.args.positional[0].args.unpositional)
                return try_action(action(act.args.positional[0].act_type, act.args.positional[0].sub_action,
                                         args(positional=act.args.positional[0].args.positional,
                                              unpositional=act.args.unpositional), act.args.positional[0].selector,
                                         act.args.positional[0].no, act.start_line, act.end_line, act.offset_pos,
                                         act.limit_offset_pos, act.file))
            else:
                Error("ActionWithoutResult", "Выражение не имеет значения и не может быть приравнено", act.start_line,
                      act.end_line, act.offset_pos, act.limit_offset_pos, act.file)
        elif type(act.args.positional[0]) == lst:
            act.args.unpositional.append(assign("values", act.args.positional[0]))
            return try_action(
                action("variable", "create_list", args(unpositional=act.args.unpositional,start_line=act.start_line,end_line=act.end_line,offset_pos=act.offset_pos,limit_offset_pos=act.limit_offset_pos,file=act.file), None, None, act.start_line,
                       act.end_line, act.offset_pos, act.limit_offset_pos, act.file))
        elif type(act.args.positional[0]) == dct:
            act.args.unpositional.extend([assign("values",
                                                 lst(act.args.positional[0].values, act.args.positional[0].start_line,
                                                     act.args.positional[0].end_line, act.args.positional[0].offset_pos,
                                                     act.args.positional[0].limit_offset_pos,
                                                     act.args.positional[0].file), act.args.positional[0].start_line,
                                                 act.args.positional[0].end_line, act.args.positional[0].offset_pos,
                                                 act.args.positional[0].limit_offset_pos, act.args.positional[0].file),
                                          assign("keys",
                                                 lst(act.args.positional[0].keys, act.args.positional[0].start_line,
                                                     act.args.positional[0].end_line, act.args.positional[0].offset_pos,
                                                     act.args.positional[0].limit_offset_pos,
                                                     act.args.positional[0].file), act.args.positional[0].start_line,
                                                 act.args.positional[0].end_line, act.args.positional[0].offset_pos,
                                                 act.args.positional[0].limit_offset_pos, act.args.positional[0].file)])
            return try_action(
                action("variable", "create_map", args(unpositional=act.args.unpositional,start_line=act.start_line,end_line=act.end_line,offset_pos=act.offset_pos,limit_offset_pos=act.limit_offset_pos,file=act.file), None, None, act.start_line,
                       act.end_line, act.offset_pos, act.limit_offset_pos, act.file))
        else:
            act.sub_action = "set_value"
            return try_action(act)
    elif act.sub_action == "+=":
        if act.args.unpositional[0].value.var_type == "INLINE":
            symbol_table["inlines"][act.args.unpositional[0].value.name] = try_math(
                math("+", symbol_table["inlines"][act.args.unpositional[0].value.name], None, act.start_line,
                     act.end_line, act.offset_pos, act.limit_offset_pos, act.file))
            return
        return try_action(action("variable", "increment", args(
            unpositional=[act.args.unpositional[0], assign("number", act.args.positional[0])]), None, None,
                                 act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos, act.file))
    elif act.sub_action == "*=":
        if act.args.unpositional[0].value.var_type == "INLINE":
            symbol_table["inlines"][act.args.unpositional[0].value.name] = try_math(
                math("*", symbol_table["inlines"][act.args.unpositional[0].value.name], None, act.start_line,
                     act.end_line, act.offset_pos, act.limit_offset_pos, act.file))
            return
        return try_action(action("variable", "multiply", args(
            unpositional=[act.args.unpositional[0],
                          assign("value", lst([act.args.unpositional[0].value, act.args.positional[0]],start_line=act.start_line,end_line=act.end_line,offset_pos=act.offset_pos,limit_offset_pos=act.limit_offset_pos,file=act.file),start_line=act.start_line,end_line=act.end_line,offset_pos=act.offset_pos,limit_offset_pos=act.limit_offset_pos,file=act.file)],start_line=act.start_line,end_line=act.end_line,offset_pos=act.offset_pos,limit_offset_pos=act.limit_offset_pos,file=act.file), None,
                                 False,
                                 act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos, act.file))
    elif act.sub_action == "-=":
        if act.args.unpositional[0].value.var_type == "INLINE":
            symbol_table["inlines"][act.args.unpositional[0].value.name] = try_math(
                math("-", symbol_table["inlines"][act.args.unpositional[0].value.name], act.args.positional[0],
                     act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos, act.file))
            return
        return try_action(action("variable", "decrement", args(
            unpositional=[act.args.unpositional[0], assign("number", act.args.positional[0],start_line=act.start_line,end_line=act.end_line,offset_pos=act.offset_pos,limit_offset_pos=act.limit_offset_pos,file=act.file)],start_line=act.start_line,end_line=act.end_line,offset_pos=act.offset_pos,limit_offset_pos=act.limit_offset_pos,file=act.file), None, False,
                                 act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos, act.file))
    elif act.sub_action == "/=":
        if act.args.unpositional[0].value.var_type == "INLINE":
            symbol_table["inlines"][act.args.unpositional[0].value.name] = try_math(
                math("/", symbol_table["inlines"][act.args.unpositional[0].value.name], act.args.positional[0],
                     act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos, act.file))
            return
        return try_action(action("variable", "divide", args(
            unpositional=[act.args.unpositional[0],
                          assign("value", lst([act.args.unpositional[0].value, act.args.positional[0]]))]), None,
                                 False,
                                 act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos, act.file))
    elif act.sub_action == "//=":
        if act.args.unpositional[0].value.var_type == "INLINE":
            symbol_table["inlines"][act.args.unpositional[0].value.name] = try_math(
                math("//", symbol_table["inlines"][act.args.unpositional[0].value.name], act.args.positional[0],
                     act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos, act.file))
            return
        return try_action(action("variable", "divide", args(
            unpositional=[act.args.unpositional[0],
                          assign("value", lst([act.args.unpositional[0].value, act.args.positional[0]])),
                          assign("division_mode", text("FLOOR"))]), None, False,
                                 act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos, act.file))
    elif act.sub_action == "%=":
        if act.args.unpositional[0].value.var_type == "INLINE":
            symbol_table["inlines"][act.args.unpositional[0].value.name] = try_math(
                math("%", symbol_table["inlines"][act.args.unpositional[0].value.name], act.args.positional[0],
                     act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos, act.file))
            return
        return try_action(action("variable", "remainder", args(
            unpositional=[act.args.unpositional[0], assign("dividend", act.args.unpositional[0].value),
                          assign("number", act.args.positional[0])]), None, False,
                                 act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos, act.file))
    elif act.sub_action == "^=":
        if act.args.unpositional[0].value.var_type == "INLINE":
            symbol_table["inlines"][act.args.unpositional[0].value.name] = try_math(
                math("^", symbol_table["inlines"][act.args.unpositional[0].value.name], act.args.positional[0],
                     act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos, act.file))
            return
        return try_action(action("variable", "remainder", args(
            unpositional=[act.args.unpositional[0], assign("base", act.args.unpositional[0].value),
                          assign("power", act.args.positional[0])]), None, False,
                                 act.start_line, act.end_line, act.offset_pos, act.limit_offset_pos, act.file))
    thing = act.args.unpositional.copy()
    for i in range(len(act.args.unpositional)):
        if type(act.args.unpositional[i].value) == var and act.args.unpositional[i].value.var_type == "INLINE":
            thing[i] = symbol_table["inlines"][act.args.unpositional[i].value.name]
    act.args.unpositional = thing
    thing = act.args.positional.copy()
    for i in range(len(act.args.positional)):
        if type(act.args.positional[i]) == var and act.args.positional[i].var_type == "INLINE":
            thing[i] = symbol_table["inlines"][act.args.positional[i].name]
    act.args.positional = thing

    return act


class action:
    def __init__(self, act_type, sub_action, args=None, selector=None, no=None, start_line=None, end_line=None,
                 offset_pos=None, limit_offset_pos=None, file=None, operations=None, conditional=None):
        self.type="action"
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        self.act_type = act_type
        if (not sub_action in actions.keys()) and (not sub_action in allowed_actions):
            Error("UnexistsAction", f"Указано несуществующее действие {sub_action}", start_line, end_line, offset_pos,
                  limit_offset_pos, file)
        self.sub_action = sub_action
        self.args = args
        if selector is not None:
            if act_type == "player" and not selector in (
                    "current", "default_player", "killer_player", "damager_player", "shooter_player", "victim_player",
                    "random_player", "all_players"):
                Error("UnexistsSelector", f"Указан несуществующий селектор {selector}", start_line, end_line,
                      offset_pos,
                      limit_offset_pos, file)
            if act_type == "entity" and not selector in (
                    "current", "default_entity", "killer_entity", "damager_entity", "shooter_entity", "projectile",
                    "victim_entity", "random_entity", "all_mobs", "all_entities", "last_entity"):
                Error("UnexistsSelector", f"Указан несуществующий селектор {selector}", start_line, end_line,
                      offset_pos,
                      limit_offset_pos, file)
        self.selector = selector
        self.operations = operations
        self.conditional = conditional
        self.no = no

    def __str__(self):
        return f'action({self.act_type},{self.sub_action},{self.args},{self.selector},{self.no})'

    def __repr__(self):
        return self.__str__()

    def json(self,in_text=None):
        if in_text != None:
            Error("UnexistsAction", f"Указано несуществующее действие {self.sub_action}", self.start_line,
                  self.end_line, self.offset_pos, self.limit_offset_pos, self.file)
        additional_actions = []

        def check_type(need_type, obj):
            if obj.type in ("text", "variable"):
                return True
            if need_type == "text":
                return True
            elif need_type == "variable":
                if obj.type == need_type or type(obj) == value:
                    return True
            elif need_type == "any":
                return True
            else:
                if obj.type in need_type:
                    return True
            return False

        if not self.sub_action in actions.keys():
            sub_action = None
            Error("UnexistsAction", f"Указано несуществующее действие {self.sub_action}", self.start_line,
                  self.end_line, self.offset_pos, self.limit_offset_pos, self.file)
        elif self.act_type != "special":
            sub_action = None
            for i in old_actions:
                if i["name"] == self.sub_action and i["object"] == self.act_type:
                    sub_action = i["id"]
                    break
            if sub_action == None:
                Error("UnexistsAction", f"Указано несуществующее действие {self.act_type}::{self.sub_action}",
                      self.start_line,
                      self.end_line, self.offset_pos, self.limit_offset_pos, self.file)
        else:
            self.act_type = actions[self.sub_action]["object"]
            sub_action = actions[self.sub_action]["id"]
        self.args.arg_list = [i["name"] for i in actions[self.sub_action]["args"]]
        self.args.assigning = [actions[self.sub_action].setdefault("assigning", None)]
        self.args.origin = actions[self.sub_action].setdefault("origin", None)
        self.args.lamba = actions[self.sub_action].setdefault("lambda", None)
        self.args.get_args()
        args = []
        types = {i["name"]: i for i in actions[self.sub_action]["args"]}
        for k, v in self.args.args.items():
            if v is not None:
                if types[k]["type"] in ("enum", "boolean"):
                    additional=[]
                    if type(v) == text:
                        if (types[k]["type"] == "enum" and not v.text in types[k]["enum"]) or (
                                types[k]["type"] == "boolean" and not v.text in ("TRUE", "FALSE")):
                            Error("UnknownArgument",
                                  f"Неизвестный тип перечисления {v.text}",
                                  v.start_line, v.end_line, v.offset_pos, v.limit_offset_pos, v.file)
                        a = {"type": "enum", "enum": v.text}
                    elif v.type == "variable":
                        if types[k]["type"] == "enum":
                            a = {"type": "enum", "enum": types[k]["enum"][0]}
                        else:
                            a = {"type": "enum", "enum": "FALSE"}
                        a["variable"] = v.name
                        a["scope"] = v.var_type.lower()
                    else:
                        a=None
                        Error("TypeError", f"Ожидался объект типа {types[k]["type"]}, но был получен {v.type}",
                              v.start_line, v.end_line, v.offset_pos, v.limit_offset_pos, v.file)
                elif types[k].setdefault("array", False) == True and v.type == "array":
                    if len(v.values) > types[k]["length"]:
                        Error("SizeError",
                              f"В объекте array[{types[k]["type"]}], максимальное количество элементов {types[k]["length"]}, но было указано {len(v.values)}",
                              v.start_line, v.end_line, v.offset_pos, v.limit_offset_pos, v.file)
                    for i in v.values:
                        if not check_type(types[k]["type"], i):
                            Error("TypeError", f"Ожидался объект типа {types[k]["type"]}, но был получен {i.type}",
                                  i.start_line, i.end_line, i.offset_pos, i.limit_offset_pos, i.file)
                    a, additional = v.json()
                elif check_type(types[k]["type"], v):
                    a, additional = v.json()
                else:
                    a, additional = None, []
                    Error("TypeError", f"Ожидался объект типа {types[k]["type"]}, но был получен {v.type}",
                          v.start_line, v.end_line, v.offset_pos, v.limit_offset_pos, v.file)
                additional_actions.extend(additional)
                args.append({"name": k, "value": a})
        a = {"action": sub_action, "values": args}
        if self.selector is not None:
            if self.act_type == "player" and not self.selector in (
                    "current", "default_player", "killer_player", "damager_player", "shooter_player", "victim_player",
                    "random_player", "all_players"):
                Error("UnexistsSelector", f"Указан несуществующий селектор {self.selector}", self.start_line,
                      self.end_line,
                      self.offset_pos,
                      self.limit_offset_pos, self.file)
            if self.act_type == "entity" and not self.selector in (
                    "current", "default_entity", "killer_entity", "damager_entity", "shooter_entity", "projectile",
                    "victim_entity", "random_entity", "all_mobs", "all_entities", "last_entity"):
                Error("UnexistsSelector", f"Указан несуществующий селектор {self.selector}", self.start_line,
                      self.end_line,
                      self.offset_pos,
                      self.limit_offset_pos, self.file)
            a["selection"] = {"type": self.selector}
        if self.no is not None:
            a["is_inverted"] = self.no
        if self.conditional is not None:
            self.conditional.operations = lst([])
            if self.conditional.no is not None:
                if self.no is None:
                    self.no = self.conditional.no
            else:
                self.conditional.no = False
            a["conditional"], additional = self.conditional.json()
            additional_actions.extend(additional)
            a["values"].extend(a["conditional"]["values"])
        if self.operations is not None:
            operations, additional = self.operations.json(normal=True)
            a["operations"] = operations
            additional_actions.extend(additional)

        return a, additional_actions


class var:
    def __init__(self, name, var_type=None, start_line=None, end_line=None, offset_pos=None, limit_offset_pos=None,
                 file=None):
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        self.type = "variable"
        self.name = name
        if var_type is None:
            if name in symbol_table["variables"].keys():
                var_type = symbol_table["variables"][name]
            else:
                var_type = "LOCAL"
        self.var_type = var_type

    def __str__(self):
        return f'var({self.name},{self.var_type})'

    def __repr__(self):
        return self.__str__()

    def json(self, in_text=False):
        if in_text:
            if self.var_type == "LOCAL":
                return f"%var_local({self.name})"
            elif self.var_type == "GAME":
                return f"%var({self.name})"
            elif self.var_type == "SAVE":
                return f"%var_save({self.name})"
        if self.var_type == "INLINE":
            Error("UnknownError", "Обнаружена переменная типа INLINE", self.start_line, self.end_line, self.offset_pos,
                  self.limit_offset_pos, self.file)
        return {"type": "variable", "variable": self.name, "scope": self.var_type.lower()}, []


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

    def json(self):
        additional_actions = []
        act, additional = self.act.json()
        additional_actions.extend(additional)
        operations, additional = self.operations.json(normal=True)
        additional_actions.extend(additional)
        act["operations"] = operations
        return act, additional_actions


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

    def json(self):
        additional_actions = []
        operations, additional = self.operations.json(normal=True)
        additional_actions.extend(additional)
        a = {"action": "else", "values": [], "operations": operations}
        return a, additional_actions


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
            Error("UnexistsEvent", f"Указан несуществующий ивент {self.name}", start_line=self.start_line,
                  end_line=self.end_line, offset_pos=self.offset_pos, limit_offset_pos=self.limit_offset_pos,
                  file=self.file)
        self.operations = operations

    def __str__(self):
        return f'event({self.name},{self.operations})'

    def __repr__(self):
        return self.__str__()

    def json(self):
        global global_count
        global_count += 1
        a = {"type": "event", "event": self.name, "position": global_count,
             "operations": []}
        additional_events = []
        operations, additional_actions = self.operations.json(normal=True)
        operations.extend(additional_actions)
        operations, additional = fix_operations_len(operations)
        additional_events.extend(additional)
        a["operations"] = operations
        return a, additional_events


def try_math(mat):
    if type(mat.first) == number and type(mat.second) == number:
        if mat.operation == "*":
            return number(mat.first.value * mat.second.value, mat.start_line, mat.end_line, mat.offset_pos,
                          mat.limit_offset_pos, mat.file)
        elif mat.operation == "+":
            return number(mat.first.value + mat.second.value, mat.start_line, mat.end_line, mat.offset_pos,
                          mat.limit_offset_pos, mat.file)
        elif mat.operation == "/":
            return number(mat.first.value / mat.second.value, mat.start_line, mat.end_line, mat.offset_pos,
                          mat.limit_offset_pos, mat.file)
        elif mat.operation == "//":
            return number(mat.first.value // mat.second.value, mat.start_line, mat.end_line, mat.offset_pos,
                          mat.limit_offset_pos, mat.file)
        elif mat.operation == "-":
            return number(mat.first.value - mat.second.value, mat.start_line, mat.end_line, mat.offset_pos,
                          mat.limit_offset_pos, mat.file)
        elif mat.operation == "%":
            return number(mat.first.value % mat.second.value, mat.start_line, mat.end_line, mat.offset_pos,
                          mat.limit_offset_pos, mat.file)
        elif mat.operation == "^":
            return number(mat.first.value ** mat.second.value, mat.start_line, mat.end_line, mat.offset_pos,
                          mat.limit_offset_pos, mat.file)
    elif type(mat.first) == text and type(mat.second) == number:
        if mat.operation == "*":
            return text(mat.first.text * mat.second.value, mat.first.text_type, mat.start_line, mat.end_line,
                        mat.offset_pos, mat.limit_offset_pos, mat.file)
    elif type(mat.first) == text and type(mat.second) == text:
        if mat.operation == "+":
            return text(mat.first.text + mat.second.text, mat.first.text_type, mat.start_line, mat.end_line,
                        mat.offset_pos, mat.limit_offset_pos, mat.file)
    else:
        return mat
    Error("UnsopportedOperand",
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
        if type(first) == var and first.var_type == "INLINE":
            first = symbol_table["inlines"][first.name]
        self.first = first
        if type(second) == var and second.var_type == "INLINE":
            second = symbol_table["inlines"][second.name]
        self.second = second
        self.type = "number"

    def __str__(self):
        return f'math({self.first}{self.operation}{self.second})'

    def __repr__(self):
        return self.__str__()

    def json(self, in_text=False):
        if in_text == True:
            return f"({self.first.json(in_text=True)}{self.operation}{self.second.json(in_text=True)})"

        return {"type": "number",
                "number": f"%math({self.first.json(in_text=True)}{self.operation}{self.second.json(in_text=True)})"}, []


class function:
    def __init__(self, name, actions=None, start_line=None, end_line=None, offset_pos=None,
                 limit_offset_pos=None, file=None):
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        self.name = name
        self.actions = actions

    def __str__(self):
        return f'function({self.name},{self.actions})'

    def __repr__(self):
        return self.__str__()

    def json(self):
        global global_count
        global_count += 1
        a = {"type": "function", "position": global_count, "operations": [],
             "is_hidden": False, "name": self.name}
        additional_events = []
        operations, additional_actions = self.actions.json(normal=True)
        operations.extend(additional_actions)
        operations, additional = fix_operations_len(operations)
        additional_events.extend(additional)
        a["operations"] = operations
        return a, additional_events


def try_function(call_func):
    if call_func.name in allowed_actions:
        if call_func.name == "round":
            if type(call_func.args.args["first"]) == number:
                if call_func.args.args["second"] is None:
                    call_func.args.args["second"] = number(0)
                if type(call_func.args.args["second"]) == number:
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

    def json(self, in_text=False):
        if in_text == True:
            arg = []
            for k, v in self.args.args.items():
                if v is not None:
                    arg.append(v.json(in_text=True))
            return f"{self.name}({"".join(arg)})"
        act,additional=action("code", "call_function", args(positional=[text(self.name)]), None, None, self.start_line,self.end_line, self.offset_pos, self.limit_offset_pos, self.file).json()
        return act,additional


class process:
    def __init__(self, name, actions, start_line=None, end_line=None, offset_pos=None, limit_offset_pos=None,
                 file=None):
        self.start_line = start_line
        self.end_line = end_line
        self.offset_pos = offset_pos
        self.limit_offset_pos = limit_offset_pos
        self.file = file
        self.name = name
        self.actions = actions

    def __str__(self):
        return f'process({self.name},{self.actions})'

    def __repr__(self):
        return self.__str__()

    def json(self):
        global global_count
        global_count += 1
        a = {"type": "process", "position": global_count, "operations": [],
             "name": self.name,
             "is_hidden": False}
        additional_events = []
        operations, additional_actions = self.actions.json(normal=True)
        operations.extend(additional_actions)
        operations, additional = fix_operations_len(operations)
        additional_events.extend(additional)
        a["operations"] = operations
        return a, additional_events


class Parser():
    global open_files

    def __init__(self, lexer, tree):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token
        self.tree = tree

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token
        else:
            Error("SyntaxError", f"Ожидался объект типа {token_type}, но был встречен {self.current_token.type}",
                  start_line=self.current_token.start_line, end_line=self.current_token.end_line,
                  offset_pos=self.current_token.offset_pos, limit_offset_pos=self.current_token.limit_offset_pos,
                  file=self.lexer.file)

    def factor(self):
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
                        if type(a) == assign:
                            unpositional.append(a)
                        else:
                            positional.append(a)
                        if self.current_token.type == COMMA:
                            self.eat(COMMA)
                    end_line = self.current_token.end_line
                    limit_offset_pos = self.current_token.limit_offset_pos
                    self.eat(RPAREN)
                    return try_function(
                        call_function(token.value, arg=args(positional=positional, unpositional=unpositional,start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                      limit_offset_pos=limit_offset_pos, file=self.lexer.file),
                                      start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                      limit_offset_pos=limit_offset_pos, file=self.lexer.file))
                return var(token.value, start_line=token.start_line, end_line=token.end_line,
                           offset_pos=token.offset_pos, limit_offset_pos=token.limit_offset_pos, file=self.lexer.file)
            elif token.type == LOCAL_VAR:
                self.eat(LOCAL_VAR)
                return var(token.value, var_type="LOCAL", start_line=token.start_line, end_line=token.end_line,
                           offset_pos=token.offset_pos, limit_offset_pos=token.limit_offset_pos, file=self.lexer.file)
            elif token.type == GAME_VAR:
                self.eat(GAME_VAR)
                return var(token.value, var_type="GAME", start_line=token.start_line, end_line=token.end_line,
                           offset_pos=token.offset_pos, limit_offset_pos=token.limit_offset_pos, file=self.lexer.file)
            elif token.type == SAVE_VAR:
                self.eat(SAVE_VAR)
                return var(token.value, var_type="SAVE", start_line=token.start_line, end_line=token.end_line,
                           offset_pos=token.offset_pos, limit_offset_pos=token.limit_offset_pos, file=self.lexer.file)
            else:
                self.eat(INLINE_VAR)
                return var(token.value, var_type="INLINE", start_line=token.start_line, end_line=token.end_line,
                           offset_pos=token.offset_pos, limit_offset_pos=token.limit_offset_pos, file=self.lexer.file)
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
                    if type(a) == assign:
                        unpositional.append(a)
                    else:
                        positional.append(a)
                    if self.current_token.type == COMMA:
                        self.eat(COMMA)
                end_line = self.current_token.end_line
                limit_offset_pos = self.current_token.limit_offset_pos
                self.eat(RPAREN)
                return item(args=args(positional=positional, unpositional=unpositional,start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                      limit_offset_pos=limit_offset_pos, file=self.lexer.file), start_line=start_line,
                            end_line=end_line, offset_pos=offset_pos, limit_offset_pos=limit_offset_pos,
                            file=self.lexer.file)
            return var("item", start_line=token.start_line, end_line=token.end_line, offset_pos=token.offset_pos,
                       limit_offset_pos=token.limit_offset_pos, file=self.lexer.file)
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
                    if type(a) == assign:
                        unpositional.append(a)
                    else:
                        positional.append(a)
                    if self.current_token.type == COMMA:
                        self.eat(COMMA)
                end_line = self.current_token.end_line
                limit_offset_pos = self.current_token.limit_offset_pos
                self.eat(RPAREN)
                return location(args=args(positional=positional, unpositional=unpositional,start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                      limit_offset_pos=limit_offset_pos, file=self.lexer.file), start_line=start_line,
                                end_line=end_line, offset_pos=offset_pos, limit_offset_pos=limit_offset_pos,
                                file=self.lexer.file)
            return var("location", end_line=token.end_line, offset_pos=token.offset_pos,
                       limit_offset_pos=token.limit_offset_pos, file=self.lexer.file)
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
                    if type(a) == assign:
                        unpositional.append(a)
                    else:
                        positional.append(a)
                    if self.current_token.type == COMMA:
                        self.eat(COMMA)
                end_line = self.current_token.end_line
                limit_offset_pos = self.current_token.limit_offset_pos
                self.eat(RPAREN)
                return vector(args=args(positional=positional, unpositional=unpositional,start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                      limit_offset_pos=limit_offset_pos, file=self.lexer.file), start_line=start_line,
                              end_line=end_line, offset_pos=offset_pos, limit_offset_pos=limit_offset_pos,
                              file=self.lexer.file)
            return var("vector", end_line=token.end_line, offset_pos=token.offset_pos,
                       limit_offset_pos=token.limit_offset_pos, file=self.lexer.file)
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
                    if type(a) == assign:
                        unpositional.append(a)
                    else:
                        positional.append(a)
                    if self.current_token.type == COMMA:
                        self.eat(COMMA)
                end_line = self.current_token.end_line
                limit_offset_pos = self.current_token.limit_offset_pos
                self.eat(RPAREN)
                return potion(args=args(positional=positional, unpositional=unpositional,start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                      limit_offset_pos=limit_offset_pos, file=self.lexer.file), start_line=start_line,
                              end_line=end_line, offset_pos=offset_pos, limit_offset_pos=limit_offset_pos,
                              file=self.lexer.file)
            return var("potion", end_line=token.end_line, offset_pos=token.offset_pos,
                       limit_offset_pos=token.limit_offset_pos, file=self.lexer.file)
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
                    if type(a) == assign:
                        unpositional.append(a)
                    else:
                        positional.append(a)
                    if self.current_token.type == COMMA:
                        self.eat(COMMA)
                end_line = self.current_token.end_line
                limit_offset_pos = self.current_token.limit_offset_pos
                self.eat(RPAREN)
                return sound(args=args(positional=positional, unpositional=unpositional,start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                      limit_offset_pos=limit_offset_pos, file=self.lexer.file), start_line=start_line,
                             end_line=end_line, offset_pos=offset_pos, limit_offset_pos=limit_offset_pos,
                             file=self.lexer.file)
            return var("sound", end_line=token.end_line, offset_pos=token.offset_pos,
                       limit_offset_pos=token.limit_offset_pos, file=self.lexer.file)
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
                    if type(a) == assign:
                        unpositional.append(a)
                    else:
                        positional.append(a)
                    if self.current_token.type == COMMA:
                        self.eat(COMMA)
                end_line = self.current_token.end_line
                limit_offset_pos = self.current_token.limit_offset_pos
                self.eat(RPAREN)
                return particle(args=args(positional=positional, unpositional=unpositional,start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                      limit_offset_pos=limit_offset_pos, file=self.lexer.file), start_line=start_line,
                                end_line=end_line, offset_pos=offset_pos, limit_offset_pos=limit_offset_pos,
                                file=self.lexer.file)
            return var("particle", end_line=token.end_line, offset_pos=token.offset_pos,
                       limit_offset_pos=token.limit_offset_pos, file=self.lexer.file)
        elif token.type == LPAREN:
            self.eat(LPAREN)
            result = self.expr()
            self.eat(RPAREN)
            return result
        elif token.type == LSPAREN:
            start_line = token.start_line
            offset_pos = token.offset_pos
            self.eat(LSPAREN)
            values = []
            while self.current_token.type != EOF and self.current_token.type != RSPAREN:
                values.append(self.expr())
                if self.current_token.type == COMMA:
                    self.eat(COMMA)
            end_line = self.current_token.end_line
            limit_offset_pos = self.current_token.limit_offset_pos
            self.eat(RSPAREN)
            return lst(values, start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                       limit_offset_pos=limit_offset_pos, file=self.lexer.file)
        elif token.type == LCPAREN:
            start_line = token.start_line
            offset_pos = token.offset_pos
            self.eat(LCPAREN)
            keys = []
            values = []
            while self.current_token.type != EOF and self.current_token.type != RCPAREN:
                keys.append(self.expr())
                self.eat(COLON)
                values.append(self.expr())
                if self.current_token.type == COMMA:
                    self.eat(COMMA)
            end_line = self.current_token.end_line
            limit_offset_pos = self.current_token.limit_offset_pos
            self.eat(RCPAREN)
            return dct(keys, values, start_line=start_line, end_line=end_line, offset_pos=offset_pos,
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
                if type(a) == assign:
                    unpositional.append(a)
                else:
                    positional.append(a)
                if self.current_token.type == COMMA:
                    self.eat(COMMA)
            end_line = self.current_token.end_line
            limit_offset_pos = self.current_token.limit_offset_pos
            self.eat(RPAREN)
            return try_action(action(sub_action.type.lower(), sub_action.value,
                                     args=args(positional=positional, unpositional=unpositional,start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                      limit_offset_pos=limit_offset_pos, file=self.lexer.file), selector=selector,
                                     start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                     limit_offset_pos=limit_offset_pos, file=self.lexer.file))
        else:
            Error("SyntaxError", f"Неожиданный токен {self.current_token.type}",
                  start_line=self.current_token.start_line, end_line=self.current_token.end_line,
                  offset_pos=self.current_token.offset_pos, limit_offset_pos=self.current_token.limit_offset_pos,
                  file=self.lexer.file)

    def expr(self, assigning=False, work_with=None, pr=1):
        if self.current_token.equals(OEL):
            self.eat(OEL)
        if work_with == None:
            result = self.up_factor(assigning=assigning, work_with=work_with)
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
                first = try_math(
                    math(operation=operation, first=first, second=second, start_line=start_line, end_line=end_line,
                         offset_pos=offset_pos, limit_offset_pos=limit_offset_pos, file=self.lexer.file))
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
                first = try_math(
                    math(operation=operation, first=first, second=second, start_line=start_line, end_line=end_line,
                         offset_pos=offset_pos, limit_offset_pos=limit_offset_pos, file=self.lexer.file))
            return first
        return result

    def up_factor(self, assigning=False, work_with=None):
        if work_with is None:
            result = self.factor()
        else:
            result = work_with
        if self.current_token.equals(DOT):
            start_line = result.start_line
            offset_pos = result.offset_pos
            self.eat(DOT)
            act = self.current_token.value
            self.eat(VAR)
            self.eat(LPAREN)
            unpositional = [assign("origin", result)]
            positional = []
            while self.current_token.type != EOF and self.current_token.type != RPAREN:
                a = self.expr(assigning=True)
                if type(a) == assign:
                    unpositional.append(a)
                else:
                    positional.append(a)
                if self.current_token.type == COMMA:
                    self.eat(COMMA)
            end_line = self.current_token.end_line
            limit_offset_pos = self.current_token.limit_offset_pos
            self.eat(RPAREN)
            return try_action(action("special", act, args=args(positional=positional, unpositional=unpositional,start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                      limit_offset_pos=limit_offset_pos, file=self.lexer.file),
                                     start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                     limit_offset_pos=limit_offset_pos, file=self.lexer.file))
        elif self.current_token.equals(LSPAREN):
            start_line = result.start_line
            offset_pos = result.offset_pos
            self.eat(LSPAREN)
            values = [result]
            while self.current_token.type != EOF and self.current_token.type != RSPAREN:
                values.append(self.expr())
                if self.current_token.type == COLON:
                    self.eat(COLON)
            end_line = self.current_token.end_line
            limit_offset_pos = self.current_token.limit_offset_pos
            self.eat(RSPAREN)
            return try_action(
                action("special", "subscript", args=args(positional=values,start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                      limit_offset_pos=limit_offset_pos, file=self.lexer.file), start_line=start_line, end_line=end_line,
                       offset_pos=offset_pos, limit_offset_pos=limit_offset_pos, file=self.lexer.file))
        if self.current_token.equals(ASSIGN) and assigning is True:
            start_line = result.start_line
            offset_pos = result.offset_pos
            self.eat(ASSIGN)
            second = self.expr()
            end_line = second.end_line
            limit_offset_pos = second.limit_offset_pos
            if type(result) == var:
                result = result.name
            elif type(result) == text:
                result = result.text
            elif type(result) == number:
                result = str(result.value)
            else:
                Error("Impossible", f"значение типа {result.type} не может быть установлено как ключ",
                      result.start_line, result.end_line, result.offset_pos, result.limit_offset_pos, result.file)
            return assign(result, second, start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                          limit_offset_pos=limit_offset_pos, file=self.lexer.file)
        return result

    def statement(self):
        if self.current_token.equals(VAR, LOCAL_VAR, GAME_VAR, SAVE_VAR, INLINE_VAR, VAR_DEFINE, SAVE_DEFINE,
                                     GAME_DEFINE, LOCAL_DEFINE, INLINE_DEFINE, LOCATION, SOUND, ITEM, PARTICLE, VECTOR,
                                     POTION):
            eat = True
            start_line = self.current_token.start_line
            offset_pos = self.current_token.offset_pos
            if self.current_token.equals(VAR_DEFINE):
                self.eat(VAR_DEFINE)
                var_name = self.current_token.value
                symbol_table["variables"][var_name] = "LOCAL"
                var_type = "LOCAL"
            elif self.current_token.equals(SAVE_DEFINE):
                self.eat(SAVE_DEFINE)
                self.eat(VAR_DEFINE)
                var_name = self.current_token.value
                symbol_table["variables"][var_name] = "SAVE"
                var_type = "SAVE"
            elif self.current_token.equals(GAME_DEFINE):
                self.eat(GAME_DEFINE)
                self.eat(VAR_DEFINE)
                var_name = self.current_token.value
                symbol_table["variables"][var_name] = "GAME"
                var_type = "GAME"
            elif self.current_token.equals(LOCAL_DEFINE):
                self.eat(LOCAL_DEFINE)
                self.eat(VAR_DEFINE)
                var_name = self.current_token.value
                symbol_table["variables"][var_name] = "LOCAL"
                var_type = "LOCAL"
            elif self.current_token.equals(INLINE_DEFINE):
                self.eat(INLINE_DEFINE)
                self.eat(VAR_DEFINE)
                var_name = self.current_token.value
                symbol_table["variables"][var_name] = "INLINE"
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
                        if type(a) == assign:
                            unpositional.append(a)
                        else:
                            positional.append(a)
                        if self.current_token.type == COMMA:
                            self.eat(COMMA)
                    end_line = self.current_token.end_line
                    limit_offset_pos = self.current_token.limit_offset_pos
                    self.eat(RPAREN)
                    return call_function(var_name, arg=args(positional=positional, unpositional=unpositional,start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                      limit_offset_pos=limit_offset_pos, file=self.lexer.file),
                                         start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                         limit_offset_pos=limit_offset_pos, file=self.lexer.file)
                if not var_name in symbol_table["variables"].keys():
                    symbol_table["variables"][var_name] = "LOCAL"
                var_type = symbol_table["variables"][var_name]
                eat = False
            elif self.current_token.equals(LOCAL_VAR):
                var_name = self.current_token.value
                if not var_name in symbol_table.keys():
                    symbol_table["variables"][var_name] = "LOCAL"
                var_type = "LOCAL"
            elif self.current_token.equals(GAME_VAR):
                var_name = self.current_token.value
                if not var_name in symbol_table.keys():
                    symbol_table["variables"][var_name] = "GAME"
                var_type = "GAME"
            elif self.current_token.equals(SAVE_VAR):
                var_name = self.current_token.value
                if not var_name in symbol_table.keys():
                    symbol_table["variables"][var_name] = "SAVE"
                var_type = "SAVE"
            elif self.current_token.equals(INLINE_VAR):
                var_name = self.current_token.value
                symbol_table["variables"][var_name] = "INLINE"
                var_type = "INLINE"
            else:
                var_name = self.current_token.value
                if not var_name in symbol_table.keys():
                    symbol_table["variables"][var_name] = "LOCAL"
                var_type = symbol_table["variables"][var_name]
            end_line = self.current_token.end_line
            limit_offset_pos = self.current_token.limit_offset_pos
            if self.current_token.equals(LOCATION, SOUND, ITEM, PARTICLE, VECTOR, POTION, LOCAL_VAR, GAME_VAR,
                                         INLINE_VAR, SAVE_VAR):
                self.eat(self.current_token.type)
            elif eat:
                self.eat(VAR)
            result = var(var_name, var_type, start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                         limit_offset_pos=limit_offset_pos, file=self.lexer.file)
            if self.current_token.equals(LSPAREN):
                self.eat(LSPAREN)
                unpositional = [assign("assigning", result)]
                positional = []
                while self.current_token.type != EOF and self.current_token.type != RSPAREN:
                    a = self.expr(assigning=True)
                    if type(a) == assign:
                        unpositional.append(a)
                    else:
                        positional.append(a)
                    if self.current_token.type == COLON:
                        self.eat(COLON)
                end_line = self.current_token.end_line
                limit_offset_pos = self.current_token.limit_offset_pos
                self.eat(RSPAREN)
                result = try_action(
                    action("special", "subscript", args=args(positional=positional, unpositional=unpositional,start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                      limit_offset_pos=limit_offset_pos, file=self.lexer.file),
                           start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                           limit_offset_pos=limit_offset_pos, file=self.lexer.file))
            if self.current_token.equals(ASSIGN, PR_WITH_ASSIGN, DEG_WITH_ASSIGN, PLUS_WITH_ASSIGN, DIVIDE_WITH_ASSIGN,
                                         MINUS_WITH_ASSIGN, MULTIPLY_WITH_ASSIGN, INT_DIVIDE_WITH_ASSIGN):
                thing = self.current_token.value
                self.eat(self.current_token.type)
                second = self.expr()
                if second is not None:
                    end_line = second.end_line
                    limit_offset_pos = second.limit_offset_pos
                    return try_action(action("special", thing,
                                             args=args(positional=[second], unpositional=[assign("assigning", result,start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                      limit_offset_pos=limit_offset_pos, file=self.lexer.file)],start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                      limit_offset_pos=limit_offset_pos, file=self.lexer.file),
                                             start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                             limit_offset_pos=limit_offset_pos, file=self.lexer.file))
            elif self.current_token.equals(DOT):
                self.eat(DOT)
                act = self.current_token.value
                self.eat(VAR)
                self.eat(LPAREN)
                unpositional = [assign("origin", result,start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                      limit_offset_pos=limit_offset_pos, file=self.lexer.file)]
                positional = []
                while self.current_token.type != EOF and self.current_token.type != RPAREN:
                    a = self.expr(assigning=True)
                    if type(a) == assign:
                        unpositional.append(a)
                    else:
                        positional.append(a)
                    if self.current_token.type == COMMA:
                        self.eat(COMMA)
                end_line = self.current_token.end_line
                limit_offset_pos = self.current_token.limit_offset_pos
                self.eat(RPAREN)
                return try_action(action("special", act, args=args(positional=positional, unpositional=unpositional,start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                      limit_offset_pos=limit_offset_pos, file=self.lexer.file),
                                         start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                         limit_offset_pos=limit_offset_pos, file=self.lexer.file))
            if type(result) != var:
                return result

        elif self.current_token.equals(IMPORT):
            self.eat(IMPORT)
            thing = self.current_token.value
            self.eat(STRING)
            an_thing = create_path(self.lexer.work_dir, thing)
            if an_thing is None:
                Error("UnexistsFile", f"Файл {thing} не найден.", thing.start_line, thing.end_line, thing.offset_pos,
                      thing.limit_offset_pos, thing.file)
            path, full_path = an_thing
            if not full_path in open_files:
                another_thing = Parser(Lexer(full_path, work_dir=path), self.tree)
                another_thing.parse()
            else:
                print(minecraft_based_text("&6",
                                           ignore_last_symbol=True) + f"файл {full_path} уже был однажды импортирован, пропускаем" + minecraft_based_text(
                    ""))
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
            conditional = None
            while self.current_token.type != EOF and self.current_token.type != RPAREN:
                a = self.expr(assigning=True)
                if type(a) == assign:
                    unpositional.append(a)
                elif type(a) == action and sub_action.value == "while":
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
                count = 0
                while self.current_token.type != EOF and self.current_token.type != CYCLE_THING and self.current_token.type != OEL:
                    a = self.expr()
                    count += 1
                    unpositional.append(assign(f"lamba_{count}", a,start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                      limit_offset_pos=limit_offset_pos, file=self.lexer.file))
                    if self.current_token.type != CYCLE_THING and self.current_token.type != OEL:
                        self.eat(COMMA)
                if self.current_token.equals(CYCLE_THING):
                    self.eat(CYCLE_THING)
                acts = []
                while self.current_token.type != EOF and self.current_token.type != RCPAREN:
                    a = self.statement()
                    if a is not None:
                        acts.append(a)
                operations = lst(acts,start_line=start_line, end_line=end_line, offset_pos=offset_pos,
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
                        acts.append(a)
                operations = lst(acts,start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                      limit_offset_pos=limit_offset_pos, file=self.lexer.file)
                end_line = self.current_token.end_line
                limit_offset_pos = self.current_token.limit_offset_pos
                self.eat(RCPAREN)
            else:
                operations = None
            return try_action(action(sub_action.type.lower(), sub_action.value,
                                     args=args(positional=positional, unpositional=unpositional,start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                      limit_offset_pos=limit_offset_pos, file=self.lexer.file), selector=selector,
                                     no=no,
                                     start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                     limit_offset_pos=limit_offset_pos, file=self.lexer.file, operations=operations,
                                     conditional=conditional))
        elif self.current_token.equals(FUNCTION):
            start_line = self.current_token.start_line
            offset_pos = self.current_token.offset_pos
            self.eat(FUNCTION)
            function_name = self.current_token.value
            self.eat(VAR)
            self.eat(LPAREN)
            self.eat(RPAREN)
            self.eat(LCPAREN)
            values = []
            while self.current_token.type != EOF and self.current_token.type != RCPAREN:
                a = self.statement()
                if a is not None:
                    values.append(a)
            end_line = self.current_token.end_line
            limit_offset_pos = self.current_token.limit_offset_pos
            self.eat(RCPAREN)
            return function(function_name, lst(values,start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                      limit_offset_pos=limit_offset_pos, file=self.lexer.file), start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                            limit_offset_pos=limit_offset_pos, file=self.lexer.file)
        elif self.current_token.equals(PROCESS):
            start_line = self.current_token.start_line
            offset_pos = self.current_token.offset_pos
            self.eat(PROCESS)
            process_name = self.current_token.value
            self.eat(VAR)
            self.eat(LPAREN)
            self.eat(RPAREN)
            self.eat(LCPAREN)
            values = []
            while self.current_token.type != EOF and self.current_token.type != RCPAREN:
                a = self.statement()
                if a is not None:
                    values.append(a)
            end_line = self.current_token.end_line
            limit_offset_pos = self.current_token.limit_offset_pos
            self.eat(RCPAREN)
            return process(process_name, lst(values,start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                                      limit_offset_pos=limit_offset_pos, file=self.lexer.file), start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                           limit_offset_pos=limit_offset_pos, file=self.lexer.file)
        elif self.current_token.equals(EVENT):
            start_line = self.current_token.start_line
            offset_pos = self.current_token.offset_pos
            event_name = self.current_token.value
            self.eat(EVENT)
            self.eat(LCPAREN)
            values = []
            while self.current_token.type != EOF and self.current_token.type != RCPAREN:
                a = self.statement()
                if a is not None:
                    values.append(a)
            end_line = self.current_token.end_line
            limit_offset_pos = self.current_token.limit_offset_pos
            self.eat(RCPAREN)
            return event(event_name, lst(values), start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                         limit_offset_pos=limit_offset_pos, file=self.lexer.file)
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
            values = []
            while self.current_token.type != EOF and self.current_token.type != RCPAREN:
                a = self.statement()
                if a is not None:
                    values.append(a)
            end_line = self.current_token.end_line
            limit_offset_pos = self.current_token.limit_offset_pos
            self.eat(RCPAREN)
            if act1.equals(IF):
                return if_(act, lst(values), start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                           limit_offset_pos=limit_offset_pos, file=self.lexer.file)
            else:
                return else_(lst(values), start_line=start_line, end_line=end_line, offset_pos=offset_pos,
                             limit_offset_pos=limit_offset_pos, file=self.lexer.file)
        elif self.current_token.equals(OEL):
            self.eat(OEL)
        elif self.current_token.equals(EL):
            self.eat(EL)
        else:
            Error("SyntaxError", f"Неожиданный токен {self.current_token.type}",
                  start_line=self.current_token.start_line, end_line=self.current_token.end_line,
                  offset_pos=self.current_token.offset_pos, limit_offset_pos=self.current_token.limit_offset_pos,
                  file=self.lexer.file)

    def parse(self):
        while self.current_token.type != EOF:
            a = self.statement()
            if a is not None:
                self.tree.append(a)

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
        eventes, additional_events = lst(self.tree).json(normal=True)
        eventes.extend(additional_events)
        return json.dumps({"handlers": eventes}, indent=2)


def compile(file, upload=False, compress=False):
    global open_files, symbol_table, global_count, global_func_count
    open_files = {}
    symbol_table = {"variables": {}, "inlines": {}}
    tree = []
    global_count = -1
    global_func_count = 0
    thing = create_path(os.getcwd(), file)
    if thing == None:
        print(minecraft_based_text(f"&cUnexistsFile : Файл {file} не найден."))
        sys.exit()
    dir_path, full_path = thing
    lexer = Lexer(full_path, work_dir=dir_path)
    thing = Parser(lexer, tree)
    code = thing.compile()
    if upload == False:
        file_name = full_path.replace(dir_path, "", 1)
        i = file_name.rfind(".")
        new_file_name = file_name[:i] + ".json"
        if compress == True:
            open(dir_path + "/" + new_file_name, "wb").write(gzip.compress(code.encode('utf-8')))
        else:
            open(dir_path + "/" + new_file_name, "w").write(code)
    else:
        response = requests.post('https://m.justmc.ru/api/upload', data=code).json()["id"]
        print(minecraft_based_text(f"&aФайл успешно загружен\n\n&7Используйте данную команду на сервере для загрузки "
                                   f"модуля:\n&9/module loadUrl force https://m.justmc.ru/api/{response}\n\n&eВажно &fМодуль "
                                   f"по ссылке удалится через &c3 минуты!\n      &fУспейте использовать команду на сервере "
                                   f"за данное время"))


old_actions = json.load(open("data/actions.json"))
actions = dict()
for i in old_actions:
    actions[i["name"]] = i
allowed_actions = ["=", "+=", "-=", "%=", "^=", "//=", "/=", "*=", "subscript"]
math_functions = {"round": ["first", "second"], "floor": ["first"], "ceil": ["first"],"abs":["first"],"sqrt":["first"],"cbrt:":["first"],"pow":["first"],"min":[],"max":[],"sign":["first"]}
events = json.load(open("data/events.json"))
values = dict()
for i in json.load(open("data/values.json")):
    values[i["name"]] = i
compile("a.jc", upload=True)
