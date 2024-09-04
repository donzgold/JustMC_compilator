

class SnbtReader:

    def __init__(self, t: str):
        self.text = t
        self.index = -1
        self.current_char = ''
        self.advance()
        self.current_token = self.next_token

    def advance(self):
        self.index += 1
        if self.index >= len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.index]

    @property
    def next_token(self):
        if self.current_char is None:
            return None
        elif self.current_char == "[":
            list_type = "List_begin"
            self.advance()
            if self.current_char == "B":
                list_type = "ByteArray_begin"
                self.advance()
            elif self.current_char == "I":
                list_type = "IntArray_begin"
                self.advance()
            elif self.current_char == "L":
                list_type = "LongArray_begin"
                self.advance()
            if list_type != "List_begin":
                if not self.current_char == ";":
                    raise SyntaxError("Ожидался символ ;")
                else:
                    self.advance()

            return Token(list_type, "[")
        elif self.current_char == "]":
            self.advance()
            return Token("List_end", "]")
        elif self.current_char == ",":
            self.advance()
            return Token("comma", ",")
        elif self.current_char == "{":
            self.advance()
            return Token("Compound_begin", "{")
        elif self.current_char == "}":
            self.advance()
            return Token("Compound_end", "}")
        elif self.current_char == ":":
            self.advance()
            return Token("colon", ":")
        elif self.current_char.isdigit() or self.current_char == "-" or self.current_char == "+" or self.current_char == ".":
            token_value = ""
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
            while self.current_char is not None and self.current_char.isdigit() or (
                    es is False and self.current_char == "e") or (plus is True and self.current_char == "+") or (
                    minus is True and self.current_char == "-") or (
                    dot is False and self.current_char == "." and es is False):
                if es is False and self.current_char == "e":
                    es = True
                if dot is False and self.current_char == "." and es is False:
                    dot = True
                token_value += self.current_char
                self.advance()
            if self.current_char == "b":
                self.advance()
                return Token("Byte", int(token_value))
            if self.current_char == "s":
                self.advance()
                return Token("Short", int(token_value))
            if self.current_char == "L":
                self.advance()
                return Token("Long", int(token_value))
            if self.current_char == "f":
                self.advance()
                return Token("Float", float(token_value))
            if self.current_char == "d":
                self.advance()
                return Token("Double", float(token_value))
            return Token("Int", int(token_value))
        elif self.current_char in ("\"", '\''):
            mode = self.current_char
            self.advance()
            token_value = ""
            block_next_symbol = False
            while self.current_char is not None and (self.current_char != mode or block_next_symbol is True):
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
                return Token("String", token_value)
            else:
                raise SyntaxError("Строка не была закрыта")
        elif self.current_char.isalpha() or self.current_char == "_":
            token_value = ""
            while self.current_char is not None and (
                    self.current_char.isalpha() or self.current_char.isdigit() or self.current_char == "_"):
                token_value += self.current_char
                self.advance()
            return Token("Compound_entry", token_value)

    def eat(self, token):
        if self.current_token.type == token:
            self.current_token = self.next_token
        else:
            raise SyntaxError(f"Ожидался токен {token}, но был получен {self.current_token.type}")

    def get_value(self):
        if self.current_token.type in ("Byte", "Short", "Int", "Long", "Float", "Double"):
            a = self.current_token
            self.eat(self.current_token.type)
            if a.type == "Byte":
                return Byte(a.value)
            elif a.type == "Short":
                return Short(a.value)
            elif a.type == "Int":
                return Int(a.value)
            elif a.type == "Long":
                return Long(a.value)
            elif a.type == "Float":
                return Float(a.value)
            elif a.type == "Double":
                return Double(a.value)
        elif self.current_token.type in ("List_begin", "ByteArray_begin", "IntArray_begin", "LongArray_begin"):
            a = self.current_token
            self.eat(self.current_token.type)
            values = []
            while self.current_token.type != "List_end":
                values.append(self.get_value())
                if self.current_token.type != "List_end":
                    self.eat("comma")
            self.eat("List_end")
            if a.type == "List_begin":
                return List(*values)
            elif a.type == "ByteArray_begin":
                return ByteArray(*values)
            elif a.type == "IntArray_begin":
                return IntArray(*values)
            elif a.type == "LongArray_begin":
                return LongArray(*values)
        elif self.current_token.type == "Compound_begin":
            self.eat(self.current_token.type)
            values = {}
            while self.current_token.type != "Compound_end":
                a = self.current_token
                if a.type == "String":
                    self.eat("String")
                else:
                    self.eat("Compound_entry")
                self.eat("colon")
                value = self.get_value()
                values[a.value] = value
                if self.current_token.type != "Compound_end":
                    self.eat("comma")
            self.eat("Compound_end")
            return Compound(**values)
        elif self.current_token.type == "String":
            a = self.current_token
            self.eat("String")
            return String(a.value)


class Token:
    def __init__(self, typ, value):
        self.type = typ
        self.value = value


def check_compound_entry(compound_entry):
    for i in compound_entry:
        if not (i.isalpha() or i == "_"):
            return False
    return True


class Compound:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if not type(v) in (
                    Compound, Byte, Short, Int, Long, Float, Double, ByteArray, String, List, IntArray, LongArray):
                raise Exception(f"Недопустимый элемент: {v.__class__.__name__}")
        self.values = kwargs

    def __str__(self):
        if sum(map(check_compound_entry, self.values)) == len(self.values):
            return "{" + ','.join([f"{k}:{str(v)}" for k, v in self.values.items()]) + "}"
        return "{" + ','.join(
            ["\"{0}\":{1}".format(k.replace("\"", "\\\""), str(v)) for k, v in self.values.items()]) + "}"

    def __repr__(self):
        return self.__str__

    def __setitem__(self, key, value):
        if not type(value) in (
                Compound, Byte, Short, Int, Long, Float, Double, ByteArray, String, List, IntArray, LongArray):
            raise Exception(f"Недопустимый элемент: {value.__class__.__name__}")
        self.values[key] = value

    def __contains__(self, item):
        return item in self.values

    def __getitem__(self, item):
        return self.values[item]

    def __len__(self):
        return len(self.values)


class Byte:
    def __init__(self, integer: int):
        if not isinstance(integer, int):
            raise Exception(f"Ожидалось число, но было получено {integer.__class__.__name__}")
        if not (-128 <= integer <= 127):
            raise Exception("Число находится вне допустимого диапазона [-128;127]")
        self.value = integer

    def __str__(self):
        return str(self.value) + "b"

    def __repr__(self):
        return self.__str__()


class Short:
    def __init__(self, integer: int):
        if not isinstance(integer, int):
            raise Exception(f"Ожидалось число, но было получено {integer.__class__.__name__}")
        if not (-32768 <= integer <= 32767):
            raise Exception("Число находится вне допустимого диапазона [-32768;32767]")
        self.value = integer

    def __str__(self):
        return str(self.value) + "s"

    def __repr__(self):
        return self.__str__()


class Int:
    def __init__(self, integer: int):
        if not isinstance(integer, int):
            raise Exception(f"Ожидалось число, но было получено {integer.__class__.__name__}")
        if not (-2_147_483_648 <= integer <= 2_147_483_647):
            raise Exception("Число находится вне допустимого диапазона [-2147483648;2147483647]")
        self.value = integer

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()


class Long:
    def __init__(self, integer: int):
        if not isinstance(integer, int):
            raise Exception(f"Ожидалось число, но было получено {integer.__class__.__name__}")
        if not (-9_223_372_036_854_707_808 <= integer <= 9_223_372_036_854_707_807):
            raise Exception("Число находится вне допустимого диапазона [-9223372036854707808;9223372036854707807]")
        self.value = integer

    def __str__(self):
        return str(self.value) + "L"

    def __repr__(self):
        return self.__str__()


class Float:
    def __init__(self, floating: float):
        if not isinstance(floating, (int, float)):
            raise Exception(f"Ожидалось число, но было получено {floating.__class__.__name__}")
        self.value = floating

    def __str__(self):
        return str(self.value) + "f"

    def __repr__(self):
        return self.__str__()


class Double:
    def __init__(self, floating):
        if not isinstance(floating, (int, float)):
            raise Exception(f"Ожидалось число, но было получено {floating.__class__.__name__}")
        self.value = floating

    def __str__(self):
        return str(self.value) + "d"

    def __repr__(self):
        return self.__str__()


class ByteArray:
    def __init__(self, *array):
        for i in array:
            if not isinstance(i, Byte):
                raise Exception(f"Недопустимый элемент: {i.__class__.__name__}")
        self.values = array

    def __str__(self):
        return f"[B;{','.join(list(map(str, self.values)))}]"

    def __repr__(self):
        return self.__str__()


class String:
    def __init__(self, text):
        self.value = text

    def __str__(self):
        if ("\"" in self.value) and (not "'" in self.value):
            return "'" + self.value + "'"
        return "\"" + self.value.replace("\"", "\\\"") + "\""

    def __repr__(self):
        return self.__str__()


class List:
    def __init__(self, *array):
        for i in array:
            if not type(i) in (
                    Compound, Byte, Short, Int, Long, Float, Double, ByteArray, String, List, IntArray, LongArray):
                raise Exception(f"Недопустимый элмент: {i.__class__.__name__}")
        self.values = list(array)

    def __str__(self):
        return f"[{','.join(list(map(str, self.values)))}]"

    def __repr__(self):
        return self.__str__()

    def append(self, value):
        if not type(value) in (
                Compound, Byte, Short, Int, Long, Float, Double, ByteArray, String, List, IntArray, LongArray):
            raise Exception(f"Недопустимый элемент: {value.__class__.__name__}")
        self.values.append(value)

    def extend(self, values):
        if not type(values) in (List, IntArray, LongArray, ByteArray):
            raise Exception(f"Недопустимый элемент: {values.__class__.__name__}")
        for i in values.values:
            if not type(i) in (
                    Compound, Byte, Short, Int, Long, Float, Double, ByteArray, String, List, IntArray, LongArray):
                raise Exception(f"Недопустимый элемент: {i.__class__.__name__}")
        self.values.extend(values.values)

    def __getitem__(self, item):
        return self.values[item]

    def __setitem__(self, key, value):
        if not type(value) in (
                Compound, Byte, Short, Int, Long, Float, Double, ByteArray, String, List, IntArray, LongArray):
            raise Exception(f"Недопустимый элемент: {value.__class__.__name__}")
        self.values[key] = value


class IntArray:
    def __init__(self, *array):
        for i in array:
            if not isinstance(i, Int):
                raise Exception(f"Недопустимый элемент: {i.__class__.__name__}")
        self.values = list(array)

    def __str__(self):
        return f"[I;{','.join(list(map(str, self.values)))}]"

    def __repr__(self):
        return self.__str__()

    def append(self, value):
        if not isinstance(value, Int):
            raise Exception(f"Недопустимый элемент: {value.__class__.__name__}")
        self.values.append(value)

    def extend(self, values):
        if not type(values) in (List, IntArray, LongArray, ByteArray):
            raise Exception(f"Недопустимый элемент: {values.__class__.__name__}")
        for i in values.values:
            if not isinstance(i, Int):
                raise Exception(f"Недопустимый элемент: {i.__class__.__name__}")
        self.values.extend(values.values)

    def __getitem__(self, item):
        return self.values[item]

    def __setitem__(self, key, value):
        if not isinstance(value, Int):
            raise Exception(f"Недопустимый элемент: {value.__class__.__name__}")
        self.values[key] = value


class LongArray:
    def __init__(self, *array):
        for i in array:
            if not isinstance(i, Long):
                raise Exception(f"Недопустимый элемент: {i.__class__.__name__}")
        self.values = list(array)

    def __str__(self):
        return f"[L;{','.join(list(map(str, self.values)))}]"

    def __repr__(self):
        return self.__str__()

    def append(self, value):
        if not isinstance(value, Long):
            raise Exception(f"Недопустимый элемент: {value.__class__.__name__}")
        self.values.append(value)

    def extend(self, values):
        if not type(values) in (List, IntArray, LongArray, ByteArray):
            raise Exception(f"Недопустимый элемент: {values.__class__.__name__}")
        for i in values.values:
            if not isinstance(i, Long):
                raise Exception(f"Недопустимый элемент: {i.__class__.__name__}")
        self.values.extend(values.values)

    def __getitem__(self, item):
        return self.values[item]

    def __setitem__(self, key, value):
        if not isinstance(value, Long):
            raise Exception(f"Недопустимый элемент: {value.__class__.__name__}")
        self.values[key] = value


def load(string):
    reader = SnbtReader(string)
    return reader.get_value()