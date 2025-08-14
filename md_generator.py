import json
import os
import shutil
from copy import deepcopy

from jmcc import Properties

color_codes = {"0": "#000000", "1": "#0000AA", "2": "#00AA00", "3": "#00AAAA", "4": "#AA0000", "5": "#AA00AA",
               "6": "#FFAA00", "7": "#AAAAAA", "8": "#555555", "9": "#5555FF", "a": "#55FF55", "b": "#55FFFF",
               "c": "#FF5555", "d": "#FF55FF", "e": "#FFFF55", "f": "#FFFFFF"}
codes = {"r": "\x1b[0m", "l": "\x1b[1m", "o": "\x1b[3m", "n": "\x1b[4m", "k": "\x1b[40m"}
for k, v in color_codes.items():
    r, g, b = [int(v[i:i + 2], 16) for i in range(1, len(v), 2)]
    codes[k] = f"\x1b[38;2;{r};{g};{b}m"
allowed_symbols = "0123456789abcdefABCDEF"

import re


def convert_markdown_table_with_br_to_oneline(text):
    lines = text.strip().split('\n')
    header = []
    raw_rows = []

    for line in lines:
        stripped = line.strip()
        if '|' not in stripped:
            continue
        cells = [cell.strip() for cell in stripped.split('|')[1:-1]]
        if len(cells) < 2:
            continue

        if not header:
            header = cells
            continue

        # Пропускаем разделитель
        if all(re.fullmatch(r'\s*:?-+\s*:?$', cell) for cell in cells if cell.strip()):
            continue

        raw_rows.append(cells)
    result_rows = []

    for row in raw_rows:
        br_cells = [cell.split('<br/>') for cell in row]
        max_lines = max(len(cell_list) for cell_list in br_cells)
        for cell_list in br_cells:
            while len(cell_list) < max_lines:
                cell_list.append(cell_list[-1])
        name_col = 0
        desc_col = 2

        for i in range(max_lines):
            new_row = [br_cells[col][i] for col in range(len(br_cells))]
            if i > 0:
                new_row[name_col] = ""
                new_row[desc_col] = ""
            result_rows.append(new_row)

    if not result_rows:
        return ""

    all_rows = [header] + result_rows
    padding = 5
    col_widths = [
        max(len(row[i]) for row in all_rows) + padding
        for i in range(len(header))
    ]

    def format_row(cells):
        padded = [cell.ljust(col_widths[i]) for i, cell in enumerate(cells)]
        return '| ' + ' | '.join(padded) + ' |'

    lines_out = []
    lines_out.append(format_row(header))
    sep_parts = [f":{'-' * (w - padding - 1)}" for w in col_widths]
    lines_out.append('| ' + ' | '.join(sep_parts) + ' |')

    for row in result_rows:
        lines_out.append(format_row(row))

    return '\n'.join(lines_out)


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


ignored_lines = set([i.strip() for i in open("new_data/langs/ignored_lines.txt", "r", encoding="UTF-8").readlines()])
filt = lambda x: x not in ignored_lines
properties = {
    "ru_RU": {i[:i.find("=")].strip(): i[i.find("=") + 1:].strip()
              for i in open("new_data/langs/ru_RU.properties", "r", encoding="UTF-8").readlines()},
    "en_US": {i[:i.find("=")].strip(): i[i.find("=") + 1:].strip()
              for i in open("new_data/langs/en_US.properties", "r", encoding="UTF-8").readlines()}}
another_blocks = json.load(open("new_data/minecraft-data/blocks.json", "r", encoding="UTF-8"))
another_items = json.load(open("new_data/minecraft-data/items.json", "r", encoding="UTF-8"))
another_enchants = json.load(open("new_data/minecraft-data/enchantments.json", "r", encoding="UTF-8"))
st = open("localize.txt", "w+", encoding="UTF-8")
new_properties = {}
for k in properties:
    new_k = {}
    for v in properties[k]:
        if v not in ignored_lines:
            new_k[v] = properties[k][v]
    new_properties[k] = new_k
properties = new_properties
for k, v in properties["ru_RU"].items():
    if k not in properties["en_US"]:
        print(f"Ключ {k} отсутствует в en_US: {v}", file=st)
for k, v in properties["en_US"].items():
    if k not in properties["ru_RU"]:
        print(f"Ключ {k} отсутствует в ru_RU: {v}", file=st)
another_events = {}
another_game_values = {}
another_actions = {}
another_particles = {}
another_potions = {}
for k, v in properties["ru_RU"].items():
    if k.startswith("creative_plus.trigger.") and "." in k[22:]:
        event_data = k[22:].split(".")
        if event_data[0] == "process":
            continue
        if event_data[0] == "function":
            continue
        if event_data[0] not in another_events:
            another_events[event_data[0]] = {"id": event_data[0]}
        if event_data[1] == "work_with":
            if "worksWith" not in another_events[event_data[0]]:
                another_events[event_data[0]]["worksWith"] = []
            if event_data[2] not in another_events[event_data[0]]["worksWith"]:
                another_events[event_data[0]]["worksWith"].append(event_data[2])
        if event_data[1] == "additional_information":
            if "additionalInfo" not in another_events[event_data[0]]:
                another_events[event_data[0]]["additionalInfo"] = []
            if event_data[2] not in another_events[event_data[0]]["additionalInfo"]:
                another_events[event_data[0]]["additionalInfo"].append(event_data[2])
    elif k.startswith("creative_plus.game_value.") and "." in k[25:]:
        game_value_data = k[25:].split(".")
        if game_value_data[0] == "target":
            continue
        if game_value_data[0] == "exit":
            continue
        if game_value_data[0] == "selection":
            continue
        if game_value_data[0] == "next_page":
            continue
        if game_value_data[0] == "previous_page":
            continue
        if game_value_data[0] not in another_game_values:
            another_game_values[game_value_data[0]] = {"id": game_value_data[0]}
        if game_value_data[1] == "argument" and "type" in another_game_values[game_value_data[0]] and \
                another_game_values[game_value_data[0]]["type"] != game_value_data[2]:
            print(
                f"конфликт между {another_game_values[game_value_data[0]]['type']} и {game_value_data[2]} у {game_value_data[0]}")
            exit()
        if game_value_data[1] == "argument":
            another_game_values[game_value_data[0]]["type"] = game_value_data[2]
        if game_value_data[1] == "work_with":
            if "worksWith" not in another_game_values[game_value_data[0]]:
                another_game_values[game_value_data[0]]["worksWith"] = []
            if game_value_data[2] not in another_game_values[game_value_data[0]]["worksWith"]:
                another_game_values[game_value_data[0]]["worksWith"].append(game_value_data[2])
    elif k.startswith("creative_plus.action.") and "." in k[21:]:
        action_data = k[21:].split(".")
        if action_data[0] not in another_actions:
            another_actions[action_data[0]] = {"id": action_data[0]}
        if action_data[1] == "work_with":
            if "worksWith" not in another_actions[action_data[0]]:
                another_actions[action_data[0]]["worksWith"] = []
            if action_data[2] not in another_actions[action_data[0]]["worksWith"]:
                another_actions[action_data[0]]["worksWith"].append(action_data[2])
        if action_data[1] == "additional_information":
            if "additionalInfo" not in another_actions[action_data[0]]:
                another_actions[action_data[0]]["additionalInfo"] = []
            if action_data[2] not in another_actions[action_data[0]]["additionalInfo"]:
                another_actions[action_data[0]]["additionalInfo"].append(action_data[2])
        if action_data[1] == "argument":
            if "args" not in another_actions[action_data[0]]:
                another_actions[action_data[0]]["args"] = []
            a = False
            arg = -1
            for arg in range(len(another_actions[action_data[0]]["args"])):
                if action_data[2] == another_actions[action_data[0]]["args"][arg]["id"]:
                    a = True
                    break
            if not a:
                arg += 1
                another_actions[action_data[0]]["args"].append({"id": action_data[2]})
            if action_data[3] == "enum":
                if "values" not in another_actions[action_data[0]]["args"][arg]:
                    another_actions[action_data[0]]["args"][arg]["values"] = []
                if action_data[4].upper() not in another_actions[action_data[0]]["args"][arg]["values"]:
                    another_actions[action_data[0]]["args"][arg]["values"].append(action_data[4].upper())
    elif k.startswith("creative_plus.particle.") and "." in k[23:]:
        particle_data = k[23:].split(".")
        if particle_data[0] not in another_particles:
            another_particles[particle_data[0]] = {"id": particle_data[0]}
    elif k.startswith("creative_plus.potion.") and "." in k[21:]:
        potion_data = k[21:].split(".")
        if potion_data[0] not in another_potions:
            another_potions[potion_data[0]] = {"id": potion_data[0]}
ru_RU = Properties(text=open("data/lang/ru_RU.properties", "r+", encoding="UTF-8").read())
en_US = Properties(text=open("data/lang/en_US.properties", "r+", encoding="UTF-8").read())
target_dir = "documentation"
with os.scandir(target_dir) as entries:
    for entry in entries:
        if entry.is_dir() and not entry.is_symlink():
            shutil.rmtree(entry.path)
        else:
            os.remove(entry.path)
os.mkdir("documentation/ru_RU")
os.mkdir("documentation/ru_RU/actions")
os.mkdir("documentation/en_US")
os.mkdir("documentation/en_US/actions")
actions_docs = {"player": [], "entity": [], "select": [], "world": [], "variable": [], "repeat": [], "controller": [],
                "code": []}
events = []
doc_msgs = []
jmcc_completions = []
load_events_map = json.load(open("new_data/events_map.json"))
load_events = {i["id"]: i for i in json.load(open("new_data/events.json"))}
for i in load_events:
    if i not in another_events:
        print(f"Ивент {i} не найден в локализации")
        exit()
for i in another_events:
    if i not in load_events:
        if i not in load_events_map:
            print(f"Ивент {i} не найден в events_map")
            exit()
        another_events[i]["cancellable"] = load_events_map[i]["cancellable"]
    else:
        another_events[i]["cancellable"] = load_events[i]["cancellable"]
for i in sorted(another_events.values(), key=lambda x: x["id"]):
    event = {"id": i["id"],
             "cancellable": i["cancellable"]}
    doc_msg = {"id": "event<" + i["id"] + ">",
               "ru_localize_name": properties["ru_RU"].setdefault("creative_plus.trigger." + i["id"] + ".name", "None"),
               "ru_description": properties["ru_RU"].setdefault("creative_plus.trigger." + i["id"] + ".description",
                                                                "None"),
               "en_localize_name": properties["en_US"].setdefault("creative_plus.trigger." + i["id"] + ".name", "None"),
               "en_description": properties["en_US"].setdefault("creative_plus.trigger." + i["id"] + ".description",
                                                                "None")}
    if "additionalInfo" in i:
        doc_msg["ru_description"] = doc_msg[
                                        "ru_description"] + "<br/>**Дополнительная информация:**<br/>&nbsp;&nbsp;" + "<br/>".join(
            [
                properties["ru_RU"].setdefault("creative_plus.trigger." + i["id"] + ".additional_information." + i2,
                                               "None")
                for
                i2
                in i["additionalInfo"]])
        doc_msg["en_description"] = doc_msg[
                                        "en_description"] + "<br/>**Additional info:**<br/>&nbsp;&nbsp;" + "<br/>".join(
            [
                properties["en_US"].setdefault("creative_plus.trigger." + i["id"] + ".additional_information." + i2,
                                               "None")
                for
                i2
                in i["additionalInfo"]])
    if "worksWith" in i:
        doc_msg["ru_description"] = doc_msg["ru_description"] + "<br/>**Работает с:** " + ", ".join(
            [properties["ru_RU"].setdefault("creative_plus.trigger." + i["id"] + ".work_with." + i2, "None")
             for i2 in i["worksWith"]])
        doc_msg["en_description"] = doc_msg["en_description"] + "<br/>**Work with:** " + ", ".join(
            [properties["en_US"].setdefault("creative_plus.trigger." + i["id"] + ".work_with." + i2, "None")
             for i2 in i["worksWith"]])
    if i["cancellable"]:
        doc_msg["ru_description"] += "<br/>**ОТМЕНЯЕМОЕ**"
        doc_msg["en_description"] += "<br/>**CANCELLABLE**"
    doc_msgs.append(doc_msg)
    events.append(event)
    secret_tech = {
        "label": doc_msg["id"],
        "kind": 3,
        "insertText": doc_msg["id"],
        "insertTextFormat": 2,
        "detail": doc_msg["ru_localize_name"],
        "documentation": {
            "kind": "markdown",
            "value": "```justcode\n" + doc_msg["id"] + "\n```\n\n" + doc_msg['ru_description'].replace("<br/>", "\\\n")
        }
    }
    jmcc_completions.append(secret_tech)

json.dump(events, open("data/events.json", "w+"), indent=2)
x = max(max(map(lambda w: len(w) + 2, [i["id"] for i in doc_msgs])), 6)
y = max(max(map(len, [i["ru_localize_name"] for i in doc_msgs])), 12)
z = max(max(map(len, [i["ru_description"] for i in doc_msgs])), 12)
ru_true_doc_msg = "**События:**\n\n| " + "**Id**" + " " * (x - 6) + " | " + "**Название**" + " " * (
        y - 12) + " | " + "**Описание**" + " " * (
                          z - 12) + " |\n| " + "-" * x + " | " + "-" * y + " | " + "-" * z + " |\n"
for i in doc_msgs:
    ru_true_doc_msg += "| `" + i["id"] + "`" + " " * (x - 2 - len(i["id"])) + " | " + i["ru_localize_name"] + " " * (
            y - len(i["ru_localize_name"])) + " | " + i["ru_description"] + " " * (
                               z - len(i["ru_description"])) + " |\n"
y = max(max(map(len, [i["en_localize_name"] for i in doc_msgs])), 8)
z = max(max(map(len, [i["en_description"] for i in doc_msgs])), 15)
en_true_doc_msg = "**Events:**\n\n| " + "**Id**" + " " * (x - 6) + " | " + "**Name**" + " " * (
        y - 12) + " | " + "**Description**" + " " * (
                          z - 15) + " |\n| " + "-" * x + " | " + "-" * y + " | " + "-" * z + " |\n"
for i in doc_msgs:
    en_true_doc_msg += "| `" + i["id"] + "`" + " " * (x - 2 - len(i["id"])) + " | " + i["en_localize_name"] + " " * (
            y - len(i["en_localize_name"])) + " | " + i["en_description"] + " " * (
                               z - len(i["en_description"])) + " |\n"
open("documentation/ru_RU/events.md", "a+", encoding="UTF-8").write(ru_true_doc_msg)
open("documentation/en_US/events.md", "a+", encoding="UTF-8").write(en_true_doc_msg)
values = []
doc_msgs = []
for i in sorted(another_game_values.values(), key=lambda x: x["id"]):
    if i["type"] == "list":
        i["type"] = "array"
    value = {"id": i["id"], "type": i["type"]}
    doc_msg = {"id": "value::" + i["id"],
               "ru_localize_name": properties["ru_RU"].setdefault("creative_plus.game_value." + i["id"] + ".name",
                                                                  "None"),
               "en_localize_name": properties["ru_RU"].setdefault("creative_plus.game_value." + i["id"] + ".name",
                                                                  "None")}
    if "worksWith" in i:
        doc_msg["ru_localize_name"] = doc_msg["ru_localize_name"] + "<br/>**Работает с:** " + ", ".join(
            [properties["ru_RU"].setdefault("creative_plus.game_value." + i["id"] + ".work_with." + i2, "None")
             for i2 in i["worksWith"]])
        doc_msg["en_localize_name"] = doc_msg["en_localize_name"] + "<br/>**Work with:** " + ", ".join(
            [properties["ru_RU"].setdefault("creative_plus.game_value." + i["id"] + ".work_with." + i2, "None")
             for i2 in i["worksWith"]])
    if "type" in i:
        doc_msg["ru_localize_value"] = properties["ru_RU"]["creative_plus.argument." + i["type"] + ".name"] + "<br/>" + \
                                       properties["ru_RU"].setdefault(
                                           "creative_plus.game_value." + i["id"] + ".argument." + i["type"] + ".name",
                                           "None")
        doc_msg["en_localize_value"] = properties["en_US"]["creative_plus.argument." + i["type"] + ".name"] + "<br/>" + \
                                       properties["en_US"].setdefault(
                                           "creative_plus.game_value." + i["id"] + ".argument." + i["type"] + ".name",
                                           "None")
    doc_msgs.append(doc_msg)
    values.append(value)
    a = doc_msg["ru_localize_name"].split("<br/>")
    doc_msg["ru_localize_name"] = a[0]
    description = "<br/>".join(a[1:]) + "<br/>" + doc_msg["ru_localize_value"]
    secret_tech = {
        "label": doc_msg["id"],
        "kind": 3,
        "insertText": doc_msg["id"],
        "insertTextFormat": 2,
        "detail": doc_msg["ru_localize_name"],
        "documentation": {
            "kind": "markdown",
            "value": "```justcode\n" + doc_msg["id"] + "\n```\n\n" + description.replace("<br/>", "\\\n")
        }
    }
    jmcc_completions.append(secret_tech)
json.dump(values, open("data/values.json", "w+"), indent=2)
x = max(max(map(lambda w: len(w) + 2, [i["id"] for i in doc_msgs])), 6)
y = max(max(map(len, [i["ru_localize_name"] for i in doc_msgs])), 12)
z = max(max(map(len, [i["ru_localize_value"] for i in doc_msgs])), 16)
ru_true_doc_msg = "\
## Игровые значения\n\
\n\
Пример использования:\n\
```ts\n\
var a = value::location\n\
var b = value::current_health<default_entity>\n\
```\n\
\n\
### Доступные селекторы\n\
\n\
**Важно:** эти селекторы доступны только для игровых значений. Действия имеют свои собственные селекторы, которые вы должны смотреть на их страницах.\n\
\n\
| **Имя**            | **Описание**          |\n\
| ------------------ | --------------------- |\n\
| `<current>`        | Текущая цель          |\n\
| `<default>`        | По умолчанию          |\n\
| `<default_entity>` | Существо по умолчанию |\n\
| `<killer_entity>`  | Убийца                |\n\
| `<damager_entity>` | Атакующий             |\n\
| `<victim_entity>`  | Жертва                |\n\
| `<shooter_entity>` | Стрелок               |\n\
| `<projectile>`     | Снаряд                |\n\
| `<last_entity>`    | Последняя сущность    |"
en_true_doc_msg = "\
## Game values\n\
\n\
Usage example:\n\
```ts\n\
var a = value::location\n\
var b = value::health<default_entity>\n\
```\n\
\n\
### Selectors\n\
\n\
**Important:** These selectors are only available for game values. Actions have their own selectors that you should look at on their pages.\n\
\n\
| **Name**           | **Description**   |\n\
| ------------------ | ----------------- |\n\
| `<current>`        | Current           |\n\
| `<default>`        | Default           |\n\
| `<default_entity>` | Default entity    |\n\
| `<killer_entity>`  | Killer            |\n\
| `<damager_entity>` | Damager           |\n\
| `<victim_entity>`  | Victim            |\n\
| `<shooter_entity>` | Shooter           |\n\
| `<projectile>`     | Projectile        |\n\
| `<last_entity>`    | Last entity       |"
ru_true_doc_msg += "### Значения\n\n| " + "**Id**" + " " * (x - 6) + " | " + "**Название**" + " " * (
        y - 12) + " | " + "**Тип значения**" + " " * (
                           z - 16) + " |\n| " + "-" * x + " | " + "-" * y + " | " + "-" * z + " |\n"
for i in doc_msgs:
    ru_true_doc_msg += "| `" + i["id"] + "`" + " " * (x - 2 - len(i["id"])) + " | " + i["ru_localize_name"] + " " * (
            y - len(i["ru_localize_name"])) + " | " + i["ru_localize_value"] + " " * (
                               z - len(i["ru_localize_value"])) + " |\n"
y = max(max(map(len, [i["en_localize_name"] for i in doc_msgs])), 8)
z = max(max(map(len, [i["en_localize_value"] for i in doc_msgs])), 14)
en_true_doc_msg += "### Values\n\n| " + "**Id**" + " " * (x - 6) + " | " + "**Name**" + " " * (
        y - 8) + " | " + "**Value type**" + " " * (
                           z - 14) + " |\n| " + "-" * x + " | " + "-" * y + " |\n"
for i in doc_msgs:
    en_true_doc_msg += "| `" + i["id"] + "`" + " " * (x - 2 - len(i["id"])) + " | " + i["en_localize_name"] + " " * (
            y - len(i["en_localize_name"])) + " | " + i["en_localize_value"] + " " * (
                               y - len(i["en_localize_value"])) + " |\n"
open("documentation/ru_RU/properties.md", "a+", encoding="UTF-8").write(ru_true_doc_msg)
open("documentation/en_US/properties.md", "a+", encoding="UTF-8").write(en_true_doc_msg)
open("documentation/en_US/actions/player.md", "a+", encoding="UTF-8").write("\
<h2 id=player>\n\
  <code>player</code>\n\
  <a href=\"./actions.md\" style=\"font-size: 14px; margin-left:\">↩️</a>\n\
</h2>\n\
\n\
### Selectors\n\
\n\
| **Name**           | **Description** |\n\
|--------------------|-----------------|\n\
| `<current>`        | Current player  |\n\
| `<default_player>` | Default player  |\n\
| `<killer_player>`  | Killer          |\n\
| `<damager_player>` | Damager         |\n\
| `<shooter_player>` | Shooter         |\n\
| `<victim_player>`  | Victim          |\n\
| `<random_player>`  | Random player   |\n\
| `<all_players>`    | All players     |\n\n")

open("documentation/ru_RU/actions/player.md", "a+", encoding="UTF-8").write("\
<h2 id=player>\n\
  <code>player</code>\n\
  <a href=\"./actions.md\" style=\"font-size: 14px; margin-left:\">↩️</a>\n\
</h2>\n\
\n\
### Селекторы\n\
\n\
| **Имя**            | **Описание**       |\n\
|--------------------| -------------------|\n\
| `<current>`        | Текущая цель       |\n\
| `<default_player>` | Игрок по умолчанию |\n\
| `<killer_player>`  | Убийца             |\n\
| `<damager_player>` | Атакующий          |\n\
| `<shooter_player>` | Стрелок            |\n\
| `<victim_player>`  | Жертва             |\n\
| `<random_player>`  | Случайный игрок    |\n\
| `<all_players>`    | Все игроки         |\n\n")

open("documentation/en_US/actions/entity.md", "a+", encoding="UTF-8").write("\
<h2 id=entity>\n\
  <code>entity</code>\n\
  <a href=\"./actions.md\" style=\"font-size: 14px; margin-left:\">↩️</a>\n\
</h2>\n\
\n\
### Селекторы\n\
\n\
| **Name**           | **Description**           |\n\
|--------------------|---------------------------|\n\
| `<current>`        | Current entity            |\n\
| `<default_entity>` | Default entity            |\n\
| `<killer_entity>`  | Killer                    |\n\
| `<shooter_entity>` | Shooter                   |\n\
| `<projectile>`     | projectile of the shooter |\n\
| `<victim_entity>`  | Victim                    |\n\
| `<random_entity>`  | Random entity             |\n\
| `<all_mobs>`       | All mobs                  |\n\
| `<all_entities>`   | All entities              |\n\
| `<last_entity>`    | Last entity               |\n\n")

open("documentation/ru_RU/actions/entity.md", "a+", encoding="UTF-8").write("\
<h2 id=entity>\n\
  <code>entity</code>\n\
  <a href=\"./actions.md\" style=\"font-size: 14px; margin-left:\">↩️</a>\n\
</h2>\n\
\n\
### Селекторы\n\
\n\
| **Имя**            | **Описание**          |\n\
| ------------------ | --------------------- |\n\
| `<current>`        | Текущая цель          |\n\
| `<default_entity>` | Сущность по умолчанию |\n\
| `<killer_entity>`  | Убийца                |\n\
| `<shooter_entity>` | Стрелок               |\n\
| `<projectile>`     | Снаряд стрелка        |\n\
| `<victim_entity>`  | Жертва                |\n\
| `<random_entity>`  | Случайная сущность    |\n\
| `<all_mobs>`       | Все мобы              |\n\
| `<all_entities>`   | Все сущности          |\n\
| `<last_entity>`    | Последняя сущность    |\n\n")
load_actions = {i["id"]: i for i in json.load(open("new_data/actions.json"))}
actions_map = json.load(open("new_data/actions.map.json"))
load_actions_map = json.load(open("new_data/actions.map2.json"))
actions_data = []
for i in load_actions:
    if i not in another_actions:
        another_actions[i] = {"id": i, "type": load_actions[i]["type"], "args": load_actions[i]["args"]}
        if "worksWith" in load_actions[i]:
            another_actions[i]["worksWith"] = load_actions[i]["worksWith"]
        if "additionalInfo" in load_actions[i]:
            another_actions[i]["additionalInfo"] = load_actions[i]["additionalInfo"]
for i in another_actions:
    if "args" not in another_actions[i]:
        another_actions[i]["args"] = []
    if i not in load_actions:
        if i not in load_actions_map:
            print("Действие", json.dumps(another_actions[i]), "не найдено в actions.map2")
            exit()
        else:
            another_actions[i]["type"] = load_actions_map[i]["type"]
            arges = {i1["id"]: i1 for i1 in load_actions_map[i]["args"]}
            for i1 in another_actions[i]["args"]:
                i1["plural"] = arges[i1["id"]]["plural"]
                i1["type"] = arges[i1["id"]]["type"]
                i1["valueSlots"] = arges[i1["id"]]["valueSlots"]
                if "values" in arges[i1["id"]]:
                    if "values" not in i1:
                        i1["values"] = []
                    for i2 in arges[i1["id"]]["values"]:
                        if i2 not in i1["values"]:
                            i1["values"].append(i2)
    else:
        if i in load_actions_map:
            true_arges = 1
            another_actions[i]["type"] = load_actions_map[i]["type"]
            arges = {i1["id"]: i1 for i1 in load_actions_map[i]["args"]}
        else:
            true_arges = None
            another_actions[i]["type"] = load_actions[i]["type"]
            arges = {i1["id"]: i1 for i1 in load_actions[i]["args"]}
        for i1 in another_actions[i]["args"]:
            if not i1["id"] in arges:
                if i not in load_actions_map:
                    print("Не существующий аргумент:", json.dumps(i1))
                    print("Действие", json.dumps(another_actions[i]), "не найдено в actions.map2")
                    exit()
                else:
                    if true_arges is None:
                        true_arges = 1
                        arges = {i2["id"]: i2 for i2 in load_actions_map[i]["args"]}
                    if i1["id"] not in arges:
                        print("Не существующий аргумент:", json.dumps(i1))
                        print("Действие", json.dumps(another_actions[i]), "необходимо обновить в actions.map2")
                        exit()
            i1["plural"] = arges[i1["id"]]["plural"]
            i1["type"] = arges[i1["id"]]["type"]
            i1["valueSlots"] = arges[i1["id"]]["valueSlots"]
            if "values" in arges[i1["id"]]:
                if "values" not in i1:
                    i1["values"] = []
                for i2 in arges[i1["id"]]["values"]:
                    if i2.upper() not in i1["values"]:
                        i1["values"].append(i2.upper())
                i1["values"].sort()
        another_actions[i]["args"].sort(key=lambda x: (1000 * (min(x["valueSlots"]) % 9) + min(x["valueSlots"]) // 9))
        cringe1 = []
        cringe2 = []
        cringe3 = []
        for i1 in another_actions[i]["args"]:
            if i1["type"] == "variable":
                cringe1.append(i1)
            elif i1["type"] == "enum":
                cringe3.append(i1)
            else:
                cringe2.append(i1)
        cringe3.sort(key=lambda x: min(x["valueSlots"]))
        another_actions[i]["args"] = cringe1
        another_actions[i]["args"].extend(cringe2)
        another_actions[i]["args"].extend(cringe3)
for i in sorted(another_actions.values(), key=lambda x: x["id"]):
    if not i["id"] in actions_map:
        print(minecraft_based_text("&cНеизвестное действие: " + i["id"] + "(" + properties["ru_RU"].setdefault(
            "creative_plus.action." + i["id"] + ".name", "None") + "), аргументы: " +
                                   ", ".join([i1["id"] + "(" + properties["ru_RU"].setdefault(
                                       "creative_plus.action." + i["id"] + ".argument." + i1["id"] + ".name",
                                       "None") + ")[" +
                                              properties["ru_RU"]["creative_plus.argument." +
                                                                  i1["type"] + ".name"] + "]" for i1 in i["args"]])))
        exit()
    else:
        action = actions_map[i["id"]]
        obj = action["object"]
        if obj != "none":
            name = action["name"]
            ru_localized_name = properties["ru_RU"].setdefault("creative_plus.action." + i["id"] + ".name", "None")
            en_localized_name = properties["en_US"].setdefault("creative_plus.action." + i["id"] + ".name", "None")
            args = i["args"]
            new_args = []
            doc_msg = dict()
            for i1 in args:
                ru_arg_localized_name = properties["ru_RU"].setdefault(
                    "creative_plus.action." + i["id"] + ".argument." + i1["id"] + ".name", "None")
                en_arg_localized_name = properties["ru_RU"].setdefault(
                    "creative_plus.action." + i["id"] + ".argument." + i1["id"] + ".name", "None")
                new_arg = {"id": i1["id"], "type": i1["type"]}
                if i1["type"] == "enum":
                    new_arg_values = []
                    for i2 in i1["values"]:
                        ru_value_localized_name = properties["ru_RU"].setdefault(
                            "creative_plus.action." + i["id"] + ".argument." + i1["id"] + ".enum." +
                            i2.lower() + ".name", "None")
                        en_value_localized_name = properties["en_US"].setdefault(
                            "creative_plus.action." + i["id"] + ".argument." + i1["id"] + ".enum." +
                            i2.lower() + ".name", "None")
                        new_arg_values.append(i2)
                    new_arg["values"] = new_arg_values
                if i1["plural"]:
                    new_arg["array"] = len(i1["valueSlots"])
                elif len(i1["valueSlots"]) > 1:
                    new_arg["array"] = len(i1["valueSlots"])
                new_args.append(new_arg)
            new_action = {"id": i["id"], "name": name, "object": obj,
                          "args": new_args}
            ru_type = "Действие без значения"
            en_type = "Action without value"
            if "assign" in action:
                smth = [list(i1.items())[0] for i1 in action["assign"]]
                new_action["assign"] = [{"id": i2[0], "type": i2[1]} for i2 in smth]
                ru_type = "Действие, возращающее значение"
                en_type = "An action that returns a value"
            if "origin" in action:
                new_action["origin"] = action["origin"]
            if "boolean" in action:
                new_action["boolean"] = action["boolean"]
                ru_type = "Действие, проверяющее условие"
                en_type = "Action that checks the conditions"
            if "lambda" in action:
                smth = [list(i1.items())[0] for i1 in action["lambda"]]
                new_action["lambda"] = [{"id": i2[0], "type": i2[1]} for i2 in smth]
            new_action["type"] = i["type"]
            doc_msg["id"] = obj + "::" + name
            doc_msg["ru_name"] = ru_localized_name
            doc_msg["en_name"] = en_localized_name
            doc_msg["ru_type"] = ru_type
            doc_msg["en_type"] = en_type
            doc_msg["ru_description"] = properties["ru_RU"].setdefault(
                "creative_plus.action." + i["id"] + ".description",
                "None")
            doc_msg["en_description"] = properties["en_US"].setdefault(
                "creative_plus.action." + i["id"] + ".description",
                "None")
            if "additionalInfo" in i:
                doc_msg["ru_additional_info"] = [
                    properties["ru_RU"].setdefault("creative_plus.action." + i["id"] + ".additional_information." + i2,
                                                   "None")
                    for i2 in i["additionalInfo"]]
                doc_msg["en_additional_info"] = [
                    properties["en_US"].setdefault("creative_plus.action." + i["id"] + ".additional_information." + i2,
                                                   "None")
                    for i2 in i["additionalInfo"]]
            if "worksWith" in i:
                doc_msg["ru_work_with"] = [
                    properties["ru_RU"].setdefault("creative_plus.action." + i["id"] + ".work_with." + i2, "None") for
                    i2 in
                    i["worksWith"]]
                doc_msg["en_work_with"] = [
                    properties["en_US"].setdefault("creative_plus.action." + i["id"] + ".work_with." + i2, "None") for
                    i2 in
                    i["worksWith"]]
            if len(new_args) != 0:
                ids = []
                ru_types = []
                ru_names = []
                en_types = []
                en_names = []
                for i2 in new_args:
                    if "array" in i2:
                        ru_pref = "список["
                        en_pref = "list["
                        suff = "]"
                    else:
                        ru_pref = ""
                        en_pref = ""
                        suff = ""
                    ids.append(i2["id"])
                    if i2["type"] == "enum":
                        ru_types.append(ru_pref +
                                        properties["ru_RU"][
                                            "creative_plus.argument." + i2["type"] + ".name"] + "<br/>" + "<br/>".join(
                            ["**" + i3 + "** - " + properties["ru_RU"].setdefault(
                                "creative_plus.action." + i["id"] + ".argument." + i2["id"] + ".enum." +
                                i3.lower() + ".name", "None") for i3 in i2["values"]]) + suff)
                        en_types.append(en_pref +
                                        properties["en_US"][
                                            "creative_plus.argument." + i2["type"] + ".name"] + "<br/>" + "<br/>".join(
                            ["**" + i3 + "** - " + properties["en_US"].setdefault(
                                "creative_plus.action." + i["id"] + ".argument." + i2["id"] + ".enum." +
                                i3.lower() + ".name", "None") for i3 in i2["values"]]) + suff)
                    else:
                        if i2["type"] == "list":
                            i2["type"] = "array"
                        elif i2["type"] == "dictionary":
                            i2["type"] = "map"
                        ru_types.append(
                            ru_pref + properties["ru_RU"]["creative_plus.argument." + i2["type"] + ".name"] + suff)
                        en_types.append(
                            en_pref + properties["en_US"]["creative_plus.argument." + i2["type"] + ".name"] + suff)
                    ru_names.append(
                        properties["ru_RU"].setdefault(
                            "creative_plus.action." + i["id"] + ".argument." + i2["id"] + ".name",
                            "None"))
                    en_names.append(
                        properties["en_US"].setdefault(
                            "creative_plus.action." + i["id"] + ".argument." + i2["id"] + ".name",
                            "None"))
                doc_msg["ru_args"] = [ids, ru_types, ru_names]
                doc_msg["en_args"] = [ids, en_types, en_names]
            doc_msg["true_id"] = i["id"]
            ru_true_doc_msg = f"<h3 id={doc_msg['true_id']}>\n  <code>{doc_msg['id']}</code>\n  <a href=\"#\" style=\"font-size: 12px; margin-left:\">⬆️</a>\n</h3>\n\n"
            start = f"<h3 id={doc_msg['true_id']}>\n  <code>{doc_msg['id']}</code>\n  <a href=\"#\" style=\"font-size: 12px; margin-left:\">⬆️</a>\n</h3>\n\n"
            en_true_doc_msg = f"<h3 id={doc_msg['true_id']}>\n  <code>{doc_msg['id']}</code>\n  <a href=\"#\" style=\"font-size: 12px; margin-left:\">⬆️</a>\n</h3>\n\n"
            ru_true_doc_msg += "**Имя:** " + doc_msg["ru_name"] + "\\\n" + "**Тип:** " + doc_msg[
                "ru_type"] + "\\\n" + "**Описание:** " + doc_msg["ru_description"] + (
                                       "\\" * ("ru_additional_info" in doc_msg)) + "\n"
            en_true_doc_msg += "**Name:** " + doc_msg["en_name"] + "\\\n" + "**Type:** " + doc_msg[
                "en_type"] + "\\\n" + "**Description:** " + doc_msg["en_description"] + (
                                       "\\" * ("en_additional_info" in doc_msg)) + "\n"
            if "ru_additional_info" in doc_msg:
                ru_true_doc_msg += "**Дополнительная информация:**\\\n&nbsp;&nbsp;" + "\\\n&nbsp;&nbsp;".join(
                    doc_msg["ru_additional_info"]) + ("\\" * ("ru_work_with" in doc_msg)) + "\n"
            if "en_additional_info" in doc_msg:
                en_true_doc_msg += "**Additional info:**\\\n&nbsp;&nbsp;" + "\\\n&nbsp;&nbsp;".join(
                    doc_msg["en_additional_info"]) + ("\\" * ("en_work_with" in doc_msg)) + "\n"

            if "ru_work_with" in doc_msg:
                ru_true_doc_msg += "**Работает с:**\\\n&nbsp;&nbsp;" + "\\\n&nbsp;&nbsp;".join(
                    doc_msg["ru_work_with"]) + "\n"
            if "en_work_with" in doc_msg:
                en_true_doc_msg += "**Work_with:**\\\n&nbsp;&nbsp;" + "\\\n&nbsp;&nbsp;".join(
                    doc_msg["en_work_with"]) + "\n"
            ru_true_doc_msg += "\n**Пример использования:** \n"
            en_true_doc_msg += "\n**Usage example:** \n"
            ru_code_example = "```ts\n"
            en_code_example = "```ts\n"
            current_number = 0


            def base_arg(arg, ignore=False):
                global current_number, current_var
                if "array" in arg and not ignore:
                    return "[" + base_arg(arg, ignore=True) + ", " + base_arg(arg, ignore=True) + "]"
                if arg["type"] == "text":
                    return "\"" + arg['id'] + "\""
                elif arg["type"] == "number":
                    return str(current_number := current_number + 1)
                elif arg["type"] == "enum":
                    return "\"" + arg["values"][0] + "\""
                elif arg["type"] == "variable":
                    return f"`{arg['id']}`"
                elif arg["type"] == "location":
                    return "location(0,0,0,0,0)"
                elif arg["type"] == "block":
                    return "item(\"stone\")"
                elif arg["type"] == "item":
                    return "item(\"stick\")"
                elif arg["type"] == "any":
                    return "\"any value\""
                elif arg["type"] == "potion":
                    return "potion(\"slow_falling\")"
                elif arg["type"] == "particle":
                    return "particle(\"fire\")"
                elif arg["type"] == "vector":
                    return "vector(0,0,0)"
                elif arg["type"] == "sound":
                    return "sound(\"entity.zombie.hurt\")"
                elif arg["type"] == "array":
                    return f"`{arg['id']}`"
                elif arg["type"] == "map":
                    return f"`{arg['id']}`"


            base_args = {i2["id"]: base_arg(i2) for i2 in new_args}
            an_args = {i2["id"]: i2 for i2 in new_args}
            base_a = base_args.copy()
            if "assign" in action:
                code_thing = []
                for i2 in action["assign"]:
                    code_thing.append(base_a.pop(list(i2.keys())[0]))
                ru_code_example += ", ".join(code_thing) + " = " + doc_msg["id"] + "(" + ", ".join(
                    list(base_a.values())) + ");\n"
                en_code_example += ", ".join(code_thing) + " = " + doc_msg["id"] + "(" + ", ".join(
                    list(base_a.values())) + ");\n"
                if "origin" in action:
                    if an_args[action["origin"]]["type"] == "number":
                        base_a[action["origin"]] = "(" + base_a[action["origin"]] + ")"
                    try:
                        thing = base_a.pop(action["origin"])
                    except:
                        thing = base_args[action["origin"]]
                        code_thing = []
                    if len(code_thing) > 0:
                        ru_code_example += "\n//Или от объекта\n\n" + ", ".join(code_thing) + " = " + thing + "." + \
                                           action[
                                               "name"] + "(" + ", ".join(list(base_a.values())) + ");\n"
                        en_code_example += "\n//Or from the object\n\n" + ", ".join(code_thing) + " = " + thing + "." + \
                                           action["name"] + "(" + ", ".join(list(base_a.values())) + ");\n"
                    else:
                        ru_code_example += "\n//Или от объекта\n\n" + thing + "." + \
                                           action[
                                               "name"] + "(" + ", ".join(list(base_a.values())) + ");\n"
                        en_code_example += "\n//Or from the object\n\n" + thing + "." + \
                                           action["name"] + "(" + ", ".join(list(base_a.values())) + ");\n"
                ru_code_example += "\n//Или в сухую позиционно\n\n" + doc_msg["id"] + "(" + ", ".join(
                    list(base_args.values())) + ");\n"
                en_code_example += "\n//Or dry by positionals\n\n" + doc_msg["id"] + "(" + ", ".join(
                    list(base_args.values())) + ");\n"
                if len(base_args) > 0:
                    ru_code_example += "\n//Или в сухую по ключам\n\n" + doc_msg["id"] + "(" + ", ".join(
                        [f"{k1}={v1}" for k1, v1 in base_args.items()]) + ");\n"
                    en_code_example += "\n//Or dry by keywords\n\n" + doc_msg["id"] + "(" + ", ".join(
                        [f"{k1}={v1}" for k1, v1 in base_args.items()]) + ");\n"
            elif "lambda" in action:
                code_thing = []
                for i2 in action["lambda"]:
                    code_thing.append(base_a.pop(list(i2.keys())[0]))
                ru_code_example += doc_msg["id"] + "(" + ", ".join(list(base_a.values())) + "){" + ", ".join(
                    code_thing) + "->\n    player::message(\"Код в цикле\");\n}\n"
                en_code_example += doc_msg["id"] + "(" + ", ".join(list(base_a.values())) + "){" + ", ".join(
                    code_thing) + "->\n    player::message(\"Code in cycle\");\n}\n"
                if len(base_args) > 0:
                    ru_code_example += "\n//Или в сухую по ключам\n\n" + doc_msg["id"] + "(" + ", ".join(
                        [f"{k1}={v1}" for k1, v1 in
                         base_args.items()]) + "){\n    player::message(\"Код в цикле\");\n}\n"
                    en_code_example += "\n//Or dry by keywords\n\n" + doc_msg["id"] + "(" + ", ".join(
                        [f"{k1}={v1}" for k1, v1 in
                         base_args.items()]) + "){\n    player::message(\"Code in cycle\");\n}\n"
            elif "boolean" in action:
                ru_code_example += "if(" + doc_msg["id"] + "(" + ", ".join(
                    list(base_a.values())) + ")){\n    player::message(\"Условие верно\");\n}\n"
                en_code_example += "if(" + doc_msg["id"] + "(" + ", ".join(
                    list(base_a.values())) + ")){\n    player::message(\"Condition is true\");\n}\n"
                if "origin" in action:
                    if an_args[action["origin"]]["type"] == "number":
                        base_a[action["origin"]] = "(" + base_a[action["origin"]] + ")"
                    thing = base_a.pop(action["origin"])
                    ru_code_example += "\n//Или от объекта\n\n" + "if(" + thing + "." + action[
                        "name"] + "(" + ", ".join(
                        list(base_a.values())) + ")){\n    player::message(\"Условие верно\");\n}\n"
                    en_code_example += "\n//Or from the object\n\n" + "if(" + thing + "." + action[
                        "name"] + "(" + ", ".join(
                        list(base_a.values())) + ")){\n    player::message(\"Condition is true\");\n}\n"
                if len(base_args) > 0:
                    ru_code_example += "\n//Или в сухую по ключам\n\n" + doc_msg["id"] + "(" + ", ".join(
                        [f"{k1}={v1}" for k1, v1 in
                         base_args.items()]) + "){\n    player::message(\"Условие верно\");\n}\n"
                    en_code_example += "\n//Or dry by keywords\n\n" + doc_msg["id"] + "(" + ", ".join(
                        [f"{k1}={v1}" for k1, v1 in
                         base_args.items()]) + "){\n    player::message(\"Condition is true\");\n}\n"
            else:
                if new_action["type"] == "basic":
                    ru_code_example += doc_msg["id"] + "(" + ", ".join(list(base_a.values())) + ");\n"
                    en_code_example += doc_msg["id"] + "(" + ", ".join(list(base_a.values())) + ");\n"
                    if "origin" in action:
                        if an_args[action["origin"]]["type"] == "number":
                            base_a[action["origin"]] = "(" + base_a[action["origin"]] + ")"
                        thing = base_a.pop(action["origin"])
                        ru_code_example += "\n//Или от объекта\n\n" + thing + "." + action[
                            "name"] + "(" + ", ".join(list(base_a.values())) + ");\n"
                        en_code_example += "\n//Or from the object\n\n" + thing + "." + action[
                            "name"] + "(" + ", ".join(list(base_a.values())) + ");\n"
                    if len(base_args) > 0:
                        ru_code_example += "\n//Или в сухую по ключам\n\n" + doc_msg["id"] + "(" + ", ".join(
                            [f"{k1}={v1}" for k1, v1 in base_args.items()]) + ");\n"
                        en_code_example += "\n//Or dry by keywords\n\n" + doc_msg["id"] + "(" + ", ".join(
                            [f"{k1}={v1}" for k1, v1 in base_args.items()]) + ");\n"
                elif new_action["type"] == "container":
                    ru_code_example += doc_msg["id"] + "(" + ", ".join(
                        list(base_a.values())) + "){\n    player::message(\"Всё работает\");\n}\n"
                    en_code_example += doc_msg["id"] + "(" + ", ".join(
                        list(base_a.values())) + "){\n    player::message(\"Everything work\");\n}\n"
                    if len(base_args) > 0:
                        ru_code_example += "\n//Или в сухую по ключам\n\n" + doc_msg["id"] + "(" + ", ".join(
                            [f"{k1}={v1}" for k1, v1 in
                             base_args.items()]) + "){\n    player::message(\"Всё работает\");\n}\n"
                        en_code_example += "\n//Or dry by keywords\n\n" + doc_msg["id"] + "(" + ", ".join(
                            [f"{k1}={v1}" for k1, v1 in
                             base_args.items()]) + "){\n    player::message(\"Everything work\");\n}\n"
                elif new_action["type"] == "container_with_conditional":
                    ru_code_example += doc_msg["id"] + "(a1.exists()){\n    player::message(\"Всё работает\");\n}\n"
                    en_code_example += doc_msg["id"] + "(a1.exists()){\n    player::message(\"Everything work\");\n}\n"
                elif new_action["type"] == "basic_with_conditional":
                    ru_code_example += doc_msg["id"] + "(a1.exists());\n"
                    en_code_example += doc_msg["id"] + "(a1.exists());\n"
            ru_code_example += "```\n\n"
            en_code_example += "```\n\n"
            ru_true_doc_msg += ru_code_example
            en_true_doc_msg += en_code_example
            if "ru_args" in doc_msg:
                def th(x1):
                    return len(x1) + 2


                x = max(max(list(map(th, doc_msg["ru_args"][0]))), 7)
                y = max(max(list(map(len, doc_msg["ru_args"][1]))), 7)
                z = max(max(list(map(len, doc_msg["ru_args"][2]))), 12)
                ru_true_doc_msg +="**Аргументы:**\n\n"
                ru_args = "| " + "**Имя**" + " " * (x - 7) + " | " + "**Тип**" + " " * (
                        y - 7) + " | " + "**Описание**" + " " * (
                                  z - 12) + " |\n| " + "-" * x + " | " + "-" * y + " | " + "-" * z + " |\n"
                for i2 in range(0, len(doc_msg["ru_args"][0])):
                    ru_args += "| `" + doc_msg["ru_args"][0][i2] + "`" + " " * (
                            x - 2 - len(doc_msg["ru_args"][0][i2])) + " | " + doc_msg["ru_args"][1][i2] + " " * (
                                       y - len(doc_msg["ru_args"][1][i2])) + " | " + doc_msg["ru_args"][2][
                                   i2] + " " * (z - len(doc_msg["ru_args"][2][i2])) + " |\n"
                ru_true_doc_msg += ru_args
                if "en_args" in doc_msg:
                    x = max(max(list(map(th, doc_msg["en_args"][0]))), 8)
                    y = max(max(list(map(len, doc_msg["en_args"][1]))), 8)
                    z = max(max(list(map(len, doc_msg["en_args"][2]))), 15)
                    en_true_doc_msg += "**Arguments:**\n\n| " + "**Name**" + " " * (
                            x - 8) + " | " + "**Type**" + " " * (
                                               y - 8) + " | " + "**Description**" + " " * (
                                               z - 15) + " |\n| " + "-" * x + " | " + "-" * y + " | " + "-" * z + " |\n"
                    for i2 in range(0, len(doc_msg["en_args"][0])):
                        en_true_doc_msg += "| `" + doc_msg["en_args"][0][i2] + "`" + " " * (
                                x - 2 - len(doc_msg["en_args"][0][i2])) + " | " + doc_msg["en_args"][1][i2] + " " * (
                                                   y - len(doc_msg["en_args"][1][i2])) + " | " + doc_msg["en_args"][2][
                                               i2] + " " * (z - len(doc_msg["en_args"][2][i2])) + " |\n"
            open("documentation/ru_RU/actions/" + obj + ".md", "a+", encoding="UTF-8").write(ru_true_doc_msg)
            open("documentation/en_US/actions/" + obj + ".md", "a+", encoding="UTF-8").write(en_true_doc_msg)
            actions_docs[obj].append(doc_msg)
            actions_data.append(new_action)
            secret_tech = {
                "label": doc_msg["id"],
                "kind": 3,
                "insertText": doc_msg["id"],
                "insertTextFormat": 2,
                "detail": doc_msg["ru_name"],
                "documentation": {
                  "kind": "markdown",
                  "value": "```justcode\n" + doc_msg["id"] + "\n```\n\n" + ru_true_doc_msg.replace(start, "").replace(ru_args,convert_markdown_table_with_br_to_oneline(ru_args)).replace(
                        "```ts\n", "```justcode\n")
                }
              }
            if "ru_args" in doc_msg:
                secret_tech["signature"] = {
                  "label": ", ".join([f"{doc_msg['ru_args'][0][i1]}: {doc_msg['ru_args'][1][i1].split('<br/>')[0]}" for i1 in range(len(doc_msg["ru_args"][0]))]),
                  "parameters": [{ "label": i1 } for i1 in doc_msg["ru_args"][0]]
                }
            jmcc_completions.append(secret_tech)
            if "origin" in action:
                secret_tech = deepcopy(secret_tech)
                secret_tech["label"] = f".{action['name']}"
                secret_tech["insertText"] = action['name']+"(${0})"
                if "ru_args" in doc_msg:
                    secret_text = lambda x1: x1 != action["origin"]
                    secret_id = doc_msg["ru_args"][0].index(action["origin"])
                    secret_text2 = lambda x1: x1 != secret_id
                    secret_tech["signature"] = {
                        "label": ", ".join(
                            [f"{doc_msg['ru_args'][0][i1]}: {doc_msg['ru_args'][1][i1].split('<br/>')[0]}" for i1 in
                             filter(secret_text2, range(len(doc_msg["ru_args"][0])))]),
                        "parameters": [{"label": i1} for i1 in filter(secret_text, doc_msg["ru_args"][0])]
                    }
                jmcc_completions.append(secret_tech)
ru_true_doc_msg = "**Список действий:**\n\n"
en_true_doc_msg = "**Actions list:**\n\n"
for k, v in actions_docs.items():
    ru_true_doc_msg += "- **[" + k + "](./" + k + ".md)**\n"
    en_true_doc_msg += "- **[" + k + "](./" + k + ".md)**\n"
    for i in v:
        ru_true_doc_msg += "  - [*" + i["id"] + " [ " + i["ru_name"] + " ]*](./" + k + ".md#" + i["true_id"] + ")\n"
        en_true_doc_msg += "  - [*" + i["id"] + " [ " + i["en_name"] + " ]*](./" + k + ".md#" + i["true_id"] + ")\n"
open("documentation/ru_RU/actions/actions.md", "a+", encoding="UTF-8").write(ru_true_doc_msg)
open("documentation/en_US/actions/actions.md", "a+", encoding="UTF-8").write(en_true_doc_msg)
json.dump(actions_data, open("data/actions.json", "w+"), indent=2)
open("documentation/ru_RU/factories.md", "a+", encoding="UTF-8").write("\
## Фабрики\n\
\n\
Пример использования:\n\
```ts\n\
var a = location(1, 2, 3);\n\
var b = vector(1, 2, 3);\n\
var c = item(\"stone\");\n\
```\n\
\n\
### Типы фабрик\n\
\n\
Аргументы показывают на типы значений, которые вы должны передать фабрике для получения значения.\n\
\n\
Те аргументы, которые заканчиваются на `*` указывать обязательно.\n\
\n\
| **Имя**      | **Название**   | **Аргументы**                                                                                                                                                                                                     |\n\
| ------------ | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |\n\
| `location()` | Местоположение | (`x`: число*, `y`: число*, `z`: число*, `yaw`: число, `pitch`: число)                                                                                                                                             |\n\
| `item()`     | Предмет        | (`id`: текст*, `name`: текст, `count`: число, `lore`: список[текст], `nbt`: майнкрафт_нбт(данные components), `custom_tags`: словарь)                                                                             |\n\
| `sound()`    | Звук           | (`sound`: текст*, `volume`: число, `pitch`: число, `variation`: текст, `source`: маркер(**RECORD**, **BLOCK**, **MASTER**, **VOICE**, **WEATHER**, **AMBIENT**, **NEUTRAL**, **HOSTILE**, **PLAYER**, **MUSIC**)) |\n\
| `vector()`   | Вектор         | (`x`: число*, `y`: число*, `z`: число*)                                                                                                                                                                           |\n\
| `particle()` | Эффект частиц  | (`particle`: текст*, `count`: число, `spread_x`: число, `spread_y`: число, `motion_x`: число, `motion_y`: число, `motion_z`: число, `material`: текст, `color`: число, `size`: число, `to_color`: число)          |\n\
| `potion()`   | Зелье          | (`potion`: текст*, `amplifier`: число, `duration`: число)                                                                                                                                                         |")
open("documentation/en_US/factories.md", "a+", encoding="UTF-8").write("\
## Factories\n\
\n\
Usage example:\n\
```ts\n\
var a = location(1, 2, 3);\n\
var b = vector(1, 2, 3);\n\
var c = item(\"stone\");\n\
```\n\
\n\
### Types of factories\n\
\n\
The arguments indicate the types of values that you must pass to the factory to get the value.\n\
\n\
Those arguments ending in `*` must be specified.\n\
\n\
| **Name**     | **Description**   | **Arguments**                                                                                                                                                                                                     |\n\
| ------------ | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |\n\
| `location()` | Location          | (`x`: number*, `y`: number*, `z`: number*, `yaw`: number, `pitch`: number)                                                                                                                                        |\n\
| `item()`     | Item              | (`id`: text*, `name`: text, `count`: number, `lore`: list[text], `nbt`: minecraft_nbt(components data), `custom_tags`: dictionary)                                                                                |\n\
| `sound()`    | Sound             | (`sound`: text*, `volume`: number, `pitch`: number, `variation`: text, `source`: marker(**RECORD**, **BLOCK**, **MASTER**, **VOICE**, **WEATHER**, **AMBIENT**, **NEUTRAL**, **HOSTILE**, **PLAYER**, **MUSIC**)) |\n\
| `vector()`   | Vector            | (`x`: number*, `y`: number*, `z`: number*)                                                                                                                                                                        |\n\
| `particle()` | Particle effect   | (`particle`: text*, `count`: number, `spread_x`: number, `spread_y`: number, `motion_x`: number, `motion_y`: number, `motion_z`: number, `material`: текст, `color`: number, `size`: number, `to_color`: number)  |\n\
| `potion()`   | Potion            | (`potion`: text*, `amplifier`: number, `duration`: number)                                                                                                                                                        |")

particles_data = []
for i in sorted(another_particles):
    particles_data.append(i)
json.dump(particles_data, open("data/particles.json", "w+"), indent=2)
potions_data = []
for i in sorted(another_potions):
    potions_data.append(i)
json.dump(potions_data, open("data/potions.json", "w+"), indent=2)
enchants_data = []
for i in sorted(another_enchants, key=lambda x: x["name"]):
    enchants_data.append(i["name"])
json.dump(enchants_data, open("data/enchants.json", "w+"), indent=2)
blocks_data = {}
for i in sorted(another_blocks, key=lambda x: x["name"]):
    block_data = {}
    for i1 in i["states"]:
        if i1["type"] == "enum":
            block_data[i1["name"]] = i1["values"]
        elif i1["type"] == "bool":
            block_data[i1["name"]] = ['false', 'true']
        elif i1["type"] == "int":
            block_data[i1["name"]] = i1["values"]
        else:
            print(i1)
            exit(-1)
    blocks_data[i["name"]] = block_data
json.dump(blocks_data, open("data/blocks.json", "w+"), indent=2)
json.dump(jmcc_completions, open("assets/completions.json", "w+", encoding="UTF-8"), separators=(",", ":"), ensure_ascii=False)
items_data = []
for i in sorted(another_items, key=lambda x: x["name"]):
    items_data.append(i["name"])
json.dump(items_data, open("data/items.json", "w+"), indent=2)

import os, shutil


def copy_tree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


# ru_RU.save_properties(open("data/lang/ru_RU.properties", "w+", encoding="UTF-8"))
# en_US.save_properties(open("data/lang/en_US.properties", "w+", encoding="UTF-8"))
with os.scandir("release") as entries:
    for entry in entries:
        if entry.is_dir() and not entry.is_symlink():
            shutil.rmtree(entry.path)
        else:
            os.remove(entry.path)
os.mkdir("release/data")
copy_tree("data", "release/data")
open("release/jmcc.py", "w+", encoding="UTF-8").write(open("jmcc.py", "r+", encoding="UTF-8").read())
open("release/compilator.py", "w+", encoding="UTF-8").write(open("compilator.py", "r+", encoding="UTF-8").read())
open("release/decompilator.py", "w+", encoding="UTF-8").write(open("decompilator.py", "r+", encoding="UTF-8").read())
open("release/nbtworker.py", "w+", encoding="UTF-8").write(open("nbtworker.py", "r+", encoding="UTF-8").read())
open("release/jmcc.properties", "w+", encoding="UTF-8").write(open("jmcc.properties", "r+", encoding="UTF-8").read())
shutil.make_archive("release", 'zip', "release")
