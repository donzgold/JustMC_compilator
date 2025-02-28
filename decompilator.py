import json
import nbtworker
from jmcc import translate, minecraft_based_text

symbol_table = dict()
actions = dict()
origin_actions = dict()
non_origin_actions = dict()
events = dict()
values = dict()
color_codes = {"0": "#000000", "1": "#0000AA", "2": "#00AA00", "3": "#00AAAA", "4": "#AA0000", "5": "#AA00AA",
               "6": "#FFAA00", "7": "#AAAAAA", "8": "#555555", "9": "#5555FF", "a": "#55FF55", "b": "#55FFFF",
               "c": "#FF5555", "d": "#FF55FF", "e": "#FFFF55", "f": "#FFFFFF"}
allowed_symbols = "0123456789abcdefABCDEF"

current_indent = 0


def fix_var_name(var_name):
    if not is_normal(var_name):
            return "`" + var_name.replace("\\", "\\\\").replace('`', '\\`') + "`"
    return var_name


def is_not_none(th):
    return th is not None

def is_normal(th):
    for i in th:
        if not (i.isalpha() or i.isdigit() or i == "_"):
            return False
    return True

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
        ret = f"function {fix_var_name(thing['name'])}" + "{" + (
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
        return "\"" + thing['block'].replace("\\", "\\\\").replace("\"", "\\\"") + "\""
    elif typ == "text":
        return (thing['parsing'][0] if thing['parsing'] != 'legacy' else '') + "\"" + thing['text'].replace(
            "\\", "\\\\").replace("\"", "\\\"") + "\""
    elif typ == "variable":
        if is_normal(thing['variable']):
            if thing["scope"] == "local":
                return thing['variable']
            return thing['scope'][0] + "`"+fix_var_name(thing['variable'])+"`"
        return thing['scope'][0] + fix_var_name(thing['variable'])
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
        arr = list(filter(is_not_none, map(decompile, thing['values'])))
        if len(arr) == 1:
            return arr[0]
        return f"[{', '.join(arr)}]"
    elif typ == "item":
        try:
            it = nbtworker.load(thing["item"])
            if len(it) == 0:
                return None
            return f"item({it['id']}, {it['Count'].value}" + (f", nbt=m{it['tag']})" if "tag" in it else ")")
        except Exception:
            return "\"" + thing["item"] + "\""
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
        return f"particle(\"{thing['particle_type']}\", {thing['count']}, {thing['first_spread']}, {thing['second_spread']}, {thing.setdefault('x_motion', 0)}, {thing.setdefault('y_motion', 0)}, {thing.setdefault('z_motion', 0)}{a})"
    elif "action" in thing:
        if thing["action"] == "empty":
            return None
        elif thing["action"] == "else":
            ret = "else{" + ("\n" + " " * ((current_indent := current_indent + 1) * 4)) + (
                    "\n" + " " * (current_indent * 4)).join(
                list(filter(is_not_none, map(decompile, thing["operations"])))) + (
                          "\n" + " " * ((current_indent := current_indent - 1) * 4)) + "}"
            return ret
        act = actions[thing["action"]]
        if act["type"] == "basic":
            args = {arg["name"]: arg for arg in thing["values"]}
            arg_text = []
            pos = True
            if "assign" in act:
                ass = [arg["id"] for arg in act["assign"]]
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
                                ori = "(" + arg_t + ")" if "." in arg_t else arg_t
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
                ret = (f"{', '.join(ass_text)} = {', '.join(arg_text)};" if len(ass_text) != 0 else "")
            elif act["id"] == "set_variable_create_list":
                ret = (f"{', '.join(ass_text)} = {', '.join(arg_text)};" if len(ass_text) != 0 else "")
            else:
                ret = ""
            if ret == "":
                ret = (f"{', '.join(ass_text)} = " if len(ass_text) != 0 else "") + (
                    (ori + ".") if (ori != "") else (act["object"] + "::")) + act["name"] + "(" + ", ".join(
                    arg_text) + ");"
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
                                ori = "(" + arg_t + ")" if "." in arg_t else arg_t

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
            new_ret = ('not ' if new_thing.setdefault('is_inverted', False) else '') + (
                (ori + ".") if ori != "" else (new_act["object"] + "::")) + new_act["name"] + "(" + ", ".join(
                arg_text) + ")"
            return act["object"] + "::" + act["name"] + "(" + new_ret + ");"
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
                                ori = "(" + arg_t + ")" if "." in arg_t else arg_t
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
                          "\n" + " " * ((current_indent := current_indent - 1) * 4)) + "}"
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
                                ori = "(" + arg_t + ")" if "." in arg_t else arg_t
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
            new_ret = ('not ' if new_thing.setdefault('is_inverted', False) else '') + (
                (ori + ".") if ori != "" else (new_act["object"] + "::")) + new_act["name"] + "(" + ", ".join(
                arg_text) + ")"
            ret = act["object"] + "::" + act["name"] + "(" + new_ret + ")" + "{" + (
                    "\n" + " " * ((current_indent := current_indent + 1) * 4)) + (
                          "\n" + " " * (current_indent * 4)).join(
                list(filter(is_not_none, map(decompile, thing["operations"])))) + (
                          "\n" + " " * ((current_indent := current_indent - 1) * 4)) + "}\n"
            return ret
    print(thing)
    print(minecraft_based_text("&c" + translate("error.unknown_type")))
    exit()


def decompile_file(file, properties=None):
    for i in json.load(open("data/actions.json")):
        actions[i["id"]] = i
    for i in json.load(open("data/events.json")):
        events[i["id"]] = i
    for i in json.load(open("data/values.json")):
        values[i["id"]] = i
    writing = open(file[:file.rfind(".")] + ".jc", "w+", encoding="UTF-8")
    for i in json.load(open(file, encoding="UTF-8"))["handlers"]:
        writing.write(decompile(i) + "\n")
