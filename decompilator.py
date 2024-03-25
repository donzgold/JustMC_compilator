import json

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


current_indent = 0


def fix_var_name(var_name):
    for i in var_name:
        if not (i in allowed_symbols or i == "_"):
            return "`" + var_name.replace("\\", "\\\\").replace('`', '\\`') + "`"
    return var_name


def is_not_none(th):
    return th is not None


def decompile(thing):
    global current_indent
    typ = thing.setdefault("type", None)
    if len(thing) == 1 and typ is None:
        return None
    elif typ == "event":
        ret = f"event<{thing['event']}>" + "{" + ("\n" + " " * ((current_indent := current_indent + 1) * 4)) + (
                "\n" + " " * (current_indent * 4)).join(
            list(filter(is_not_none, map(decompile, thing["operations"])))) + (
                      "\n" + " " * ((current_indent := current_indent - 1) * 4)) + "}\n"
        return ret
    elif typ == "function":
        ret = f"function {fix_var_name(thing['name'])}()" + "{" + (
                "\n" + " " * ((current_indent := current_indent + 1) * 4)) + (
                      "\n" + " " * (current_indent * 4)).join(
            list(filter(is_not_none, map(decompile, thing["operations"])))) + (
                      "\n" + " " * ((current_indent := current_indent - 1) * 4)) + "}\n"
        return ret
    elif typ == "process":
        ret = f"process {fix_var_name(thing['name'])}()" + "{" + (
                "\n" + " " * ((current_indent := current_indent + 1) * 4)) + (
                      "\n" + " " * (current_indent * 4)).join(
            list(filter(is_not_none, map(decompile, thing["operations"])))) + (
                      "\n" + " " * ((current_indent := current_indent - 1) * 4)) + "}\n"
        return ret
    elif typ == "block":
        return "\"" + thing['block'].replace("\\","\\\\").replace("\"", "\\\"") + "\""
    elif typ == "text":
        return (thing['parsing'][0] if thing['parsing'] != 'legacy' else '') + "\"" + thing['text'].replace("\\",
                                                                                                            "\\\\").replace(
            "\"", "\\\"") + "\""
    elif typ == "variable":
        return thing['scope'][0] + "`" + thing['variable'].replace("\\", "\\\\").replace('`', '\\`') + "`"
    elif typ == "number":
        if isinstance(thing["number"], int) or isinstance(thing["number"], float):
            return str(thing["number"])
        return "\"" + str(thing["number"]).replace("\"", "\\\"") + "\""
    elif typ == "enum":
        if "variable" in thing:
            return thing['scope'][0] + "`" + thing['variable'].replace("\\", "\\\\").replace('`', '\\`') + "`"
        else:
            return "\"" + thing['enum'].replace("\\", "\\\\").replace("\"", "\\\"") + "\""
    elif typ == "array":
        return f"[{', '.join(list(filter(is_not_none, map(decompile, thing['values']))))}]"
    elif typ == "item":
        try:
            it = json.loads(thing["item"])
            if len(it) == 0:
                return None
            return f"item({it['id']}, {it['Count']}" + (f", nbt={json.dumps(it['tag'])})" if "tag" in it else ")")
        except:
            return ("\"" + thing["item"].replace("\"", "\\\"") + "\"").replace('\n', '\\n')
    elif typ == "game_value":
        return f"value::{thing['game_value']}" + (
            f"<{json.loads(thing['selection'])['type']}>" if thing["selection"] != "null" else "")
    elif typ == "sound":
        return f"sound(\"{thing['sound']}\", {thing['volume']}, {thing['pitch']}" + (
            f", \"{thing['variation']}\"" if thing['variation'] != "" else "") + (
            f", \"{thing['source']}\"" if thing['source'] != "" else "") + ")"
    elif typ == "potion":
        return f"potion(\"{thing['potion']}\", {thing['amplifier']}, {thing['duration']})"
    elif typ == "vector":
        return f"vector({thing['x']}, {thing['y']}, {thing['z']})"
    elif typ == "location":
        return f"location({thing['x']}, {thing['y']}, {thing['z']}, {thing['yaw']}, {thing['pitch']})"
    elif typ == "particle":
        material = thing.setdefault("material", None)
        color = thing.setdefault("color", None)
        size = thing.setdefault("size", None)
        to_color = thing.setdefault("to_color", None)
        a = f', material=\"{material}\"' if material is not None else '' + f', color={color}' if color is not None else '' + f', size={size}' if size is not None else '' + f', to_color={to_color}' if to_color is not None else ''
        return f"particle(\"{thing['particle_type']}\", {thing['count']}, {thing['first_spread']}, {thing['second_spread']}, {thing.setdefault('x_motion',0)}, {thing.setdefault('y_motion',0)}, {thing.setdefault('z_motion',0)}{a})"
    elif "action" in thing:
        if thing["action"] == "empty":
            return None
        elif thing["action"] == "else":
            ret = "else{" + ("\n" + " " * ((current_indent := current_indent + 1) * 4)) + (
                    "\n" + " " * (current_indent * 4)).join(
                list(filter(is_not_none, map(decompile, thing["operations"])))) + (
                          "\n" + " " * ((current_indent := current_indent - 1) * 4)) + "}\n"
            return ret
        act = actions[thing["action"]]
        if act["type"] == "basic":
            args = {arg["name"]: arg for arg in thing["values"]}
            arg_text = []
            pos = True
            if "assign" in act:
                ass = [list(arg.keys())[0] for arg in act["assign"]]
                ass_pos = True
            else:
                ass_pos = False
                ass = []
            ori = ""
            if "origin" in act:
                ori_pos = True
            else:
                ori_pos = False
            ass_text = []
            for arg in act["args"]:
                if arg["id"] in args:
                    arg_t = decompile(args[arg["id"]]["value"])
                    if is_not_none(arg_t):
                        if arg["id"] in ass:
                            if ass_pos:
                                ass_text.append(arg_t)
                                continue
                        elif ass_pos:
                            ass_pos = False
                        if ori_pos:
                            if arg["id"] == act["origin"]:
                                ori = arg_t
                                ori_pos = False
                                continue
                        if pos:
                            arg_text.append(arg_t)
                        else:
                            arg_text.append(arg["id"] + "=" + arg_t)
                    elif pos:
                        pos = False
                elif pos:
                    pos = False
            if act["id"] == "set_variable_value":
                ret = (f"{', '.join(ass_text)} = {', '.join(arg_text)}" if len(ass_text) != 0 else "")
            elif act["id"] == "set_variable_create_list":
                ret = (f"{', '.join(ass_text)} = {', '.join(arg_text)}" if len(ass_text) != 0 else "")
            else:
                ret = ""
            if ret == "":
                ret = (f"{', '.join(ass_text)} = " if len(ass_text) != 0 else "") + (
                    (ori + ".") if (ori != "") else (act["object"] + "::")) + act["name"] + "(" + ", ".join(
                    arg_text) + ")"
            return ret
        elif act["type"] == "basic_with_conditional":
            new_thing = thing["conditional"]
            new_act = actions[new_thing["action"]]
            args = {arg["name"]: arg for arg in thing["values"]}
            arg_text = []
            pos = True
            ori = ""
            if "origin" in new_act:
                ori_pos = True
            else:
                ori_pos = False
            for arg in new_act["args"]:
                if arg["id"] in args:
                    arg_t = decompile(args[arg["id"]]["value"])
                    if is_not_none(arg_t):
                        if ori_pos:
                            if arg["id"] == new_act["origin"]:
                                ori = decompile(args[arg["id"]]["value"])
                                ori_pos = False
                                continue
                        if pos:
                            arg_text.append(decompile(args[arg["id"]]["value"]))
                        else:
                            arg_text.append(arg["id"] + "=" + decompile(args[arg["id"]]["value"]))
                    else:
                        pos = False
                elif pos:
                    pos = False
            new_ret = ('not ' if new_thing.setdefault('is_inverted', False) else '') + ((ori + ".") if ori != "" else (new_act["object"] + "::")) + new_act["name"] + "(" + ", ".join(
                arg_text) + ")"
            return act["object"] + "::" + act["name"] + "(" + new_ret + ")"
        elif act["type"] == "container":
            args = {arg["name"]: arg for arg in thing["values"]}
            arg_text = []
            pos = True
            ori = ""
            if "origin" in act:
                ori_pos = True
            else:
                ori_pos = False
            for arg in act["args"]:
                if arg["id"] in args:
                    arg_t = decompile(args[arg["id"]]["value"])
                    if is_not_none(arg_t):
                        if ori_pos:
                            if arg["id"] == act["origin"]:
                                ori = arg_t
                                ori_pos = False
                                continue
                        if pos:
                            arg_text.append(arg_t)
                        else:
                            arg_text.append(arg["id"] + "=" + arg_t)
                    else:
                        pos = False
                elif pos:
                    pos = False
            if act["id"] == "else":
                ret = "else"
            else:
                ret = ""
            if ret == "":
                ret = ((ori + ".") if ori != "" else (act["object"] + "::")) + act["name"] + "(" + ", ".join(
                    arg_text) + ")"
                if "boolean" in act:
                    ret = f"if{' not ' if thing.setdefault('is_inverted', False) else ''}(" + ret + ")"
            ret = ret + "{" + ("\n" + " " * ((current_indent := current_indent + 1) * 4)) + (
                    "\n" + " " * (current_indent * 4)).join(
                list(filter(is_not_none, map(decompile, thing["operations"])))) + (
                          "\n" + " " * ((current_indent := current_indent - 1) * 4)) + "}\n"
            return ret
        elif act["type"] == "container_with_conditional":
            new_thing = thing["conditional"]
            new_act = actions[new_thing["action"]]
            args = {arg["name"]: arg for arg in thing["values"]}
            arg_text = []
            pos = True
            ori = ""
            if "origin" in new_act:
                ori_pos = True
            else:
                ori_pos = False
            for arg in new_act["args"]:
                if arg["id"] in args:
                    arg_t = decompile(args[arg["id"]]["value"])
                    if is_not_none(arg_t):
                        if ori_pos:
                            if arg["id"] == new_act["origin"]:
                                ori = arg_t
                                ori_pos = False
                                continue
                        if pos:
                            arg_text.append(arg_t)
                        else:
                            arg_text.append(arg["id"] + "=" + arg_t)
                    else:
                        pos = False
                elif pos:
                    pos = False
            new_ret = ('not ' if new_thing.setdefault('is_inverted', False) else '') + ((ori + ".") if ori != "" else (new_act["object"] + "::")) + new_act["name"] + "(" + ", ".join(
                arg_text) + ")"
            ret = act["object"] + "::" + act["name"] + "(" + new_ret + ")" + "{" + (
                    "\n" + " " * ((current_indent := current_indent + 1) * 4)) + (
                          "\n" + " " * (current_indent * 4)).join(
                list(filter(is_not_none, map(decompile, thing["operations"])))) + (
                          "\n" + " " * ((current_indent := current_indent - 1) * 4)) + "}\n"
            return ret
    print(thing)
    print(minecraft_based_text("&cНеизвестный тип"))
    exit()


def decompile_file(file):
    for i in json.load(open("data/actions.json")):
        actions[i["id"]] = i
    for i in json.load(open("data/events.json")):
        events[i["id"]] = i
    for i in json.load(open("data/values.json")):
        values[i["id"]] = i
    writing = open(file[:file.rfind(".")] + ".jc", "w+", encoding="UTF-8")
    for i in json.load(open(file, encoding="UTF-8"))["handlers"]:
        writing.write(decompile(i) + "\n")

#decompile_file("a.json")
