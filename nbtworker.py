import base64
import gzip
import struct


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
        while self.current_char in {" ", "\n"}:
            self.advance()
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
        elif (self.current_char.isdigit() or self.current_char == "-" or
              self.current_char == "+" or self.current_char == "."):
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
                    es is False and self.current_char in ("e", "E") and token_value[-1] != ".") or (
                    plus is True and self.current_char == "+") or (
                    minus is True and self.current_char == "-") or (
                    dot is False and self.current_char == "." and es is False):
                if es is False and self.current_char in ("e", "E") and token_value[-1] != ".":
                    es = True
                if dot is False and self.current_char == "." and es is False:
                    dot = True
                token_value += self.current_char
                self.advance()
            if token_value[-1] == ".":
                token_value = token_value[:-1]
                self.index -= 1
                self.current_char = self.text[self.index]
            if self.current_char in ("b", "B"):
                self.advance()
                return Token("Byte", int(token_value))
            if self.current_char in ("s", "S"):
                self.advance()
                return Token("Short", int(token_value))
            if self.current_char in ("l", "L"):
                self.advance()
                return Token("Long", int(token_value))
            if self.current_char in ("f", "F"):
                self.advance()
                return Token("Float", float(token_value))
            if self.current_char in ("d", "D"):
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
            if token_value == "true":
                return Token("Byte", 1)
            elif token_value == "false":
                return Token("Byte", 0)
            return Token("Compound_entry", token_value)
        else:
            raise Exception("error", self.index, self.text)

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
            self.eat("Compound_begin")
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
        else:
            raise Exception(-1)


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

    def keys(self):
        return self.values.keys()

    def __contains__(self, item):
        return item in self.values

    def __getitem__(self, item):
        return self.values[item]

    def __len__(self):
        return len(self.values)

    def to_bytes(self, name: str):
        name_bytes = name.encode("UTF-8")
        bytes_ = [10, *struct.pack("!h", len(name_bytes)), *name_bytes]
        for key in self.values:
            bytes_.extend(self.values[key].to_bytes(key))
        bytes_.append(0)
        return bytes_


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

    def to_bytes(self, name):
        name_bytes = name.encode("UTF-8")
        return [1, *struct.pack("!h", len(name_bytes)), *name_bytes, *struct.pack("!b", self.value)]


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

    def to_bytes(self, name):
        name_bytes = name.encode("UTF-8")
        return [2, *struct.pack("!h", len(name_bytes)), *name_bytes, *struct.pack("!h", self.value)]


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

    def to_bytes(self, name):
        name_bytes = name.encode("UTF-8")
        return [3, *struct.pack("!h", len(name_bytes)), *name_bytes, *struct.pack("!i", self.value)]


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

    def to_bytes(self, name):
        name_bytes = name.encode("UTF-8")
        return [4, *struct.pack("!h", len(name_bytes)), *name_bytes, *struct.pack("!q", self.value)]


class Float:
    def __init__(self, floating: float):
        if not isinstance(floating, (int, float)):
            raise Exception(f"Ожидалось число, но было получено {floating.__class__.__name__}")
        self.value = floating

    def __str__(self):
        return str(self.value) + "f"

    def __repr__(self):
        return self.__str__()

    def to_bytes(self, name):
        name_bytes = name.encode("UTF-8")
        return [5, *struct.pack("!h", len(name_bytes)), *name_bytes, *struct.pack("!f", self.value)]


class Double:
    def __init__(self, floating):
        if not isinstance(floating, (int, float)):
            raise Exception(f"Ожидалось число, но было получено {floating.__class__.__name__}")
        self.value = floating

    def __str__(self):
        return str(self.value) + "d"

    def __repr__(self):
        return self.__str__()

    def to_bytes(self, name):
        name_bytes = name.encode("UTF-8")
        return [6, *struct.pack("!h", len(name_bytes)), *name_bytes, *struct.pack("!d", self.value)]


class ByteArray:
    def __init__(self, *array):
        for i in array:
            if not isinstance(i, Byte):
                raise Exception(f"Недопустимый элемент: {i.__class__.__name__}")
        self.values = array

    def __str__(self):
        return f"[B;{','.join(list(map(lambda x: str(x.value), self.values)))}]"

    def __repr__(self):
        return self.__str__()

    def to_bytes(self, name):
        name_bytes = name.encode("UTF-8")
        return [7, *struct.pack("!h", len(name_bytes)), *name_bytes, *struct.pack("!h", len(self.values)),
                  *[struct.pack("!b", i.value) for i in self.values]]


class String:
    def __init__(self, text):
        self.value = text

    def __str__(self):
        if ("\"" in self.value) and ("'" not in self.value):
            return "'" + self.value + "'"
        return "\"" + self.value.replace("\"", "\\\"") + "\""

    def __repr__(self):
        return self.__str__()

    def to_bytes(self, name):
        name_bytes = name.encode("UTF-8")
        str_bytes = self.value.encode("UTF-8")
        return [8, *struct.pack("!h", len(name_bytes)), *name_bytes, *struct.pack("!h", len(str_bytes)), *str_bytes]


class List:
    def __init__(self, *array):
        self.type = None
        for i in array:
            if not type(i) in (
                    Compound, Byte, Short, Int, Long, Float, Double, ByteArray, String, List, IntArray, LongArray):
                raise Exception(f"Недопустимый элмент: {i.__class__.__name__}")
            if self.type is None:
                self.type = type(i)
            if i != self.type:
                raise Exception(f"Недопустимый элмент: {i.__class__.__name__}")
        self.values = list(array)

    def __str__(self):
        return f"[{','.join(list(map(str, self.values)))}]"

    def __repr__(self):
        return self.__str__()

    def append(self, value):
        if not type(value) in (
                Compound, Byte, Short, Int, Long, Float, Double, ByteArray, String, List, IntArray, LongArray,
                self.type):
            raise Exception(f"Недопустимый элемент: {value.__class__.__name__}")
        if self.type is None:
            self.type = type(value)
        self.values.append(value)

    def extend(self, values):
        if not type(values) in (List, IntArray, LongArray, ByteArray):
            raise Exception(f"Недопустимый элемент: {values.__class__.__name__}")
        if isinstance(values, List) and self.type != values.type:
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

    def to_bytes(self, name):
        name_bytes = name.encode("UTF-8")
        bytes_ = [9, *struct.pack("!h", len(name_bytes)), *name_bytes]
        type1 = None
        for i1 in self.values:
            a = i1.to_bytes("")
            if type1 is None:
                type1 = a[0]
                bytes_.append(type1)
                bytes_.extend(struct.pack("!i", len(self.values)))
            bytes_.extend(a[3:])
        return bytes_


class IntArray:
    def __init__(self, *array):
        for i in array:
            if not isinstance(i, Int):
                raise Exception(f"Недопустимый элемент: {i.__class__.__name__}")
        self.values = list(array)

    def __str__(self):
        return f"[I;{','.join(list(map(lambda x: str(x.value), self.values)))}]"

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

    def to_bytes(self, name):
        name_bytes = name.encode("UTF-8")
        return [11, *struct.pack("!h", len(name_bytes)), *name_bytes, *struct.pack("!h", len(self.values)),
                  *[struct.pack("!i", i.value) for i in self.values]]


class LongArray:
    def __init__(self, *array):
        for i in array:
            if not isinstance(i, Long):
                raise Exception(f"Недопустимый элемент: {i.__class__.__name__}")
        self.values = list(array)

    def __str__(self):
        return f"[L;{','.join(list(map(lambda x: str(x.value), self.values)))}]"

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

    def to_bytes(self, name):
        name_bytes = name.encode("UTF-8")
        return [12, *struct.pack("!h", len(name_bytes)), *name_bytes, *struct.pack("!h", len(self.values)),
                  *[struct.pack("!q", i.value) for i in self.values]]


def load(string):
    reader = SnbtReader(string)
    return reader.get_value()


def read_base64(base64_text):
    def eat(a, number):
        if a[0] == number:
            del a[0]
        else:
            raise Exception()

    def read(a, amount):
        b = a[:amount]
        del a[:amount]
        return b

    def text_from_bytes(lst):
        return bytes(lst).decode("UTF-8")

    def int_from_bytes(inbytes):
        if len(inbytes) == 1:  # byte
            return struct.unpack("!b", bytes(inbytes))[0]
        if len(inbytes) == 2:  # short
            return struct.unpack("!h", bytes(inbytes))[0]
        if len(inbytes) == 4:  # int
            return struct.unpack("!i", bytes(inbytes))[0]
        if len(inbytes) == 8:  # long
            return struct.unpack("!q", bytes(inbytes))[0]
        raise Exception(-2)

    def float_from_bytes(inbytes):
        if len(inbytes) == 4:  # float
            return struct.unpack("!f", bytes(inbytes))[0]
        if len(inbytes) == 8:  # double
            return struct.unpack("!d", bytes(inbytes))[0]
        raise Exception(-3)

    def full_read(a):
        if a[0] == 12:  # longArray
            eat(a, 7)
            b = read(a, 2)
            name = text_from_bytes(read(a, int_from_bytes(b)))
            amount = int_from_bytes(read(a, 4))
            it = LongArray(*[Long(int_from_bytes(read(a, 8))) for _ in range(amount)])
            return name, it
        elif a[0] == 11:  # intArray
            eat(a, 7)
            b = read(a, 2)
            name = text_from_bytes(read(a, int_from_bytes(b)))
            amount = int_from_bytes(read(a, 4))
            it = IntArray(*[Int(int_from_bytes(read(a, 4))) for _ in range(amount)])
            return name, it
        elif a[0] == 10:  # dict
            it = Compound()
            eat(a, 10)
            b = read(a, 2)
            name = text_from_bytes(read(a, int_from_bytes(b)))
            while a[0] != 0:
                key, value = full_read(a)
                it[key] = value
            eat(a, 0)
            return name, it
        elif a[0] == 9:  # list
            it = List()
            eat(a, 9)
            b = read(a, 2)
            name = text_from_bytes(read(a, int_from_bytes(b)))
            list_of = read(a, 1)[0]
            amount = int_from_bytes(read(a, 4))
            for i1 in range(amount):
                a.insert(0, list_of)
                a.insert(1, 0)
                a.insert(2, 0)
                key, value = full_read(a)
                it.append(value)
            return name, it
        elif a[0] == 8:  # string
            eat(a, 8)
            b = read(a, 2)
            name = text_from_bytes(read(a, int_from_bytes(b)))
            b = read(a, 2)
            value = text_from_bytes(read(a, int_from_bytes(b)))
            return name, String(value)
        elif a[0] == 7:  # byteArray
            eat(a, 7)
            b = read(a, 2)
            name = text_from_bytes(read(a, int_from_bytes(b)))
            amount = int_from_bytes(read(a, 4))
            it = ByteArray(*[Byte(int_from_bytes(read(a, 1))) for _ in range(amount)])
            return name, it
        elif a[0] == 6:  # double
            eat(a, 5)
            b = read(a, 2)
            name = text_from_bytes(read(a, int_from_bytes(b)))
            return name, Float(float_from_bytes(read(a, 8)))
        elif a[0] == 5:  # float
            eat(a, 5)
            b = read(a, 2)
            name = text_from_bytes(read(a, int_from_bytes(b)))
            return name, Float(float_from_bytes(read(a, 4)))
        elif a[0] == 4:  # long
            eat(a, 4)
            b = read(a, 2)
            name = text_from_bytes(read(a, int_from_bytes(b)))
            return name, Long(int_from_bytes(read(a, 8)))
        elif a[0] == 3:  # int
            eat(a, 3)
            b = read(a, 2)
            name = text_from_bytes(read(a, int_from_bytes(b)))
            return name, Int(int_from_bytes(read(a, 4)))
        elif a[0] == 2:  # short
            eat(a, 2)
            b = read(a, 2)
            name = text_from_bytes(read(a, int_from_bytes(b)))
            return name, Short(int_from_bytes(read(a, 2)))
        elif a[0] == 1:  # byte
            eat(a, 1)
            b = read(a, 2)
            name = text_from_bytes(read(a, int_from_bytes(b)))
            return name, Byte(int_from_bytes(read(a, 1)))
        else:
            raise Exception(1)

    return full_read(list(gzip.decompress(base64.b64decode(base64_text))))[1]


def convert_to_base64(it):
    return base64.b64encode(gzip.compress(bytes(it.to_bytes(name="")), mtime=1337)).decode("UTF-8")
