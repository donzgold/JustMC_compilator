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

item_list = set()
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
    if thing is None:
        return None
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
        ret = f"process {fix_var_name(thing['name'])}" + "{" + (
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
            return thing['scope'][0] + "`"+thing['variable']+"`"
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
        return f"[{', '.join(arr)}]"
    elif typ == "item":
        if thing["item"] == "AAAAAAAAAAA=":
            return None
        try:
            it = nbtworker.load(thing["item"])
            if len(it) == 0:
                return None
            return f"item({it['id']}"+(f", count={it['count'].value}" if it['count'].value != 1 else "")  + (f", nbt=m{it['components']})" if "components" in it else "")+")"
        except Exception:
            item_list.add(thing["item"])
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
        selector = f"<{thing['selection']['type']}>" if "selection" in thing and thing["selection"] not in ("null",None) else ""
        selector = f"<{thing['conditional']['selection']['type']}>" if "conditional" in thing and "selection" in thing['conditional'] and thing['conditional']["selection"] not in ("null",None) else selector
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
                    (ori + ".") if (ori != "") else (act["object"] + "::")) + act["name"] + selector +"(" + ", ".join(
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
                (ori + ".") if ori != "" else (new_act["object"] + "::")) + new_act["name"] + selector + "(" + ", ".join(
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
                ret = ((ori + ".") if ori != "" else (act["object"] + "::")) + act["name"] + selector + "(" + ", ".join(
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
                (ori + ".") if ori != "" else (new_act["object"] + "::")) + new_act["name"] + selector + "(" + ", ".join(
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
        res = decompile(i)
        if res is not None:
            writing.write(res + "\n")
    if len(item_list) > 0:
        print(minecraft_based_text("&fВ коде обнаружены предметы, невозможные расшифровать обычным способом.\nПрограмма выполнит компиляцию кода необходимого для исправления предметов."))
        print(minecraft_based_text(translate("compilator.code_uploading_message")))
        from time import time
        from compilator import dct, text, assign, var, Vars
        import requests
        start_time1 = time()
        keys = [text(i, 0, -1, -1, "") for i in item_list]
        class fake_item:
            def __init__(self, base64, start_pos, end_pos, source):
                self.item = base64

            def json(self):
                return {"type": "item", "item": str(self.item)}
            def is_simple(self):
                return True
        vals = [fake_item(i, -1, -1, "") for i in item_list]
        add_actions = assign([var("a",Vars.LOCAL,-1,-1,"")],None,dct(keys, vals, -1, -1, ""),-1,-1,"").simplify()[0]
        add_actions = [i.json() for i in add_actions]
        code = {"handlers":[{"type":"event","event":"player_join","position":0,"operations":[{"action":"repeat_for_each_map_entry","values":[{"name":"key_variable","value":{"type":"variable","variable":"k","scope":"local"}},{"name":"value_variable","value":{"type":"variable","variable":"v","scope":"local"}},{"name":"map","value":{"type":"variable","variable":"a","scope":"local"}}],"operations":[{"action":"set_variable_replace_text","values":[{"name":"variable","value":{"type":"variable","variable":"v","scope":"local"}},{"name":"text","value":{"type":"variable","variable":"v","scope":"local"}},{"name":"replace","value":{"type":"text","text":"\"","parsing":"legacy"}},{"name":"replacement","value":{"type":"text","text":"\\\"","parsing":"legacy"}},{"name":"first","value":{"type":"enum","enum":"ANY"}}]},{"action":"if_variable_equals","values":[{"name":"value","value":{"type":"variable","variable":"i","scope":"local"}},{"name":"compare","value":{"type":"number","number":0}}],"operations":[{"action":"set_variable_value","values":[{"name":"variable","value":{"type":"variable","variable":"i","scope":"local"}},{"name":"value","value":{"type":"number","number":1}}]},{"action":"set_variable_text","values":[{"name":"variable","value":{"type":"variable","variable":"b","scope":"local"}},{"name":"text","value":{"type":"array","values":[{"type":"text","text":"{\"","parsing":"legacy"},{"type":"variable","variable":"k","scope":"local"},{"type":"text","text":"\":\"","parsing":"legacy"},{"type":"variable","variable":"v","scope":"local"},{"type":"text","text":"\"","parsing":"legacy"}]}},{"name":"merging","value":{"type":"enum","enum":"CONCATENATION"}}]}]},{"action":"else","values":[],"operations":[{"action":"set_variable_text","values":[{"name":"variable","value":{"type":"variable","variable":"b","scope":"local"}},{"name":"text","value":{"type":"array","values":[{"type":"variable","variable":"b","scope":"local"},{"type":"text","text":",\"","parsing":"legacy"},{"type":"variable","variable":"k","scope":"local"},{"type":"text","text":"\":\"","parsing":"legacy"},{"type":"variable","variable":"v","scope":"local"},{"type":"text","text":"\"","parsing":"legacy"}]}},{"name":"merging","value":{"type":"enum","enum":"CONCATENATION"}}]}]}]},{"action":"set_variable_text","values":[{"name":"variable","value":{"type":"variable","variable":"b","scope":"local"}},{"name":"text","value":{"type":"array","values":[{"type":"variable","variable":"b","scope":"local"},{"type":"text","text":"}","parsing":"legacy"}]}},{"name":"merging","value":{"type":"enum","enum":"CONCATENATION"}}]},{"action":"set_variable_set_component_click","values":[{"name":"variable","value":{"type":"variable","variable":"c","scope":"local"}},{"name":"component","value":{"type":"text","text":"&e\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043d\u0430 \u044d\u0442\u043e\u0442 \u0442\u0435\u043a\u0441\u0442, \u044d\u0442\u043e \u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0432 \u0432\u0430\u0448 \u0431\u0443\u0444\u0435\u0440 \u043e\u0431\u043c\u0435\u043d\u0430.\\n\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u0435 \u043a\u043e\u043c\u0430\u043d\u0434\u0443 `py jmcc.py fix_items \u043f\u0443\u0442\u044c_\u043a_\u0444\u0430\u0439\u043b\u0443_jc`\\n\u041a\u043e\u043c\u0430\u043d\u0434\u0430 \u0432\u043e\u0437\u044c\u043c\u0451\u0442 \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 \u0432\u0430\u0448\u0435\u0433\u043e \u0431\u0443\u0444\u0435\u0440\u0430 \u043e\u0431\u043c\u0435\u043d\u0430 \u0438 \u0438\u0441\u043f\u0440\u0430\u0432\u0438\u0442 \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u044b.","parsing":"legacy"}},{"name":"value","value":{"type":"variable","variable":"b","scope":"local"}},{"name":"click_action","value":{"type":"enum","enum":"COPY_TO_CLIPBOARD"}}]},{"action":"player_send_message","values":[{"name":"messages","value":{"type":"variable","variable":"c","scope":"local"}}]}]}]}
        add_actions.extend(code["handlers"][0]["operations"])
        code["handlers"][0]["operations"]=add_actions
        response = requests.post('https://m.justmc.ru/api/upload', json=code).json()
        end_time1 = time()
        print(minecraft_based_text(translate("compilator.code_uploading_time", {0: round(end_time1 - start_time1, 3)})))
        print(minecraft_based_text("&fДля исправления, необходимо прописать команду в свободном мире.\n"
                                   f"&9/module loadUrl force https://m.justmc.ru/api/{response['id']}\n"
                                   "&fДанная команда запустит код для создания словаря замен предметов."
                                   "&fПосле выполнения кода, проследовать инструкциям на стороне джаста."))
def fix_items(file, properties=None):
    from tkinter import Tk
    r = Tk()
    s = json.loads(r.clipboard_get())
    r.destroy()
    reading = open(file, "r+", encoding="UTF-8").read()
    for k, v in s.items():
        reading = reading.replace("\""+k+"\"", decompile({"type": "item", "item": v}))
    filename = file[:file.rfind(".")] + "(fixed).jc"
    open(filename, "w+", encoding="UTF-8").write(reading)
    print(minecraft_based_text(f"&fПредметы исправлены. Исправление находится в файле `{filename}`"))
