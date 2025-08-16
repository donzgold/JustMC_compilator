from time import time
import sys

sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")
start_time = time()
import shutil
import sys
import zipfile

import requests
import os
import socket


class Properties:
    def __init__(self, file=None, text=None):
        self.file = file
        self.text = text
        self.properties = {}
        self.positions = {}
        if text is not None:
            self.get_properties(text=text)
        else:
            self.get_properties()
        if len(self.positions) == 0:
            self.positions[-1] = "#properties"

    def __getitem__(self, item):
        return self.properties[item]

    def __setitem__(self, key, value):
        if key not in self.properties:
            self.positions[max(self.positions.keys()) + 1] = key
        self.properties[key] = value

    def __contains__(self, item):
        return item in self.properties

    def get_properties(self, file=None, text=None):
        if file is None:
            file = self.file
        c = 0
        if text is not None:
            for line in text.split("\n"):
                c += 1
                if line.startswith("#"):
                    self.positions[c] = line
                else:
                    key = line[:line.find("=")].strip()
                    value = fix_type(
                        line[line.find("=") + 1:].encode('raw_unicode_escape').decode('unicode_escape').strip())
                    self.positions[c] = key
                    self.properties[key] = value
            return
        while (line := file.readline()) != "":
            c += 1
            if line.startswith("#"):
                self.positions[c] = line
            else:
                key = line[:line.find("=")].strip()
                value = fix_type(
                    line[line.find("=") + 1:].encode('raw_unicode_escape').decode('unicode_escape').strip())
                self.positions[c] = key
                self.properties[key] = value

    def save_properties(self, file=None):
        if file is None:
            file = self.file
        a1 = sorted(self.positions.items(), key=lambda x: x[0])
        for i in range(len(a1) - 1):
            if isinstance(a1[i][1], str):
                if a1[i][1].startswith("#"):
                    file.write(str(a1[i][1]).replace("\n", "\\n") + "\n")
                    continue
            file.write(
                a1[i][1].replace("\n", "\\n") + " = " + str(self.properties[a1[i][1]]).replace("\n", "\\n") + "\n")
        if isinstance(a1[-1][1], str):
            if a1[-1][1].startswith("#"):
                file.write(str(a1[-1][1]).replace("\n", "\\n"))
                return
        file.write(a1[-1][1].replace("\n", "\\n") + " = " + str(self.properties[a1[-1][1]]).replace("\n", "\\n"))


def translate(message: str, insert: dict = None, fallback: str = None):
    global lang
    if lang is None or message not in lang:
        if fallback is None:
            return f"&fMessage '{message}' not found, inserts={insert}&r"
        else:
            message = fallback
    else:
        message = lang[message]
    if insert is not None:
        for k1, v1 in insert.items():
            message = message.replace("{" + str(k1) + "}", str(v1))
    return message


def is_connected():
    try:
        socket.create_connection(("1.1.1.1", 53))
        return True
    except Exception:
        pass
    return False


color_codes = {"0": "#000000", "1": "#0000AA", "2": "#00AA00", "3": "#00AAAA", "4": "#AA0000", "5": "#AA00AA",
               "6": "#FFAA00", "7": "#AAAAAA", "8": "#555555", "9": "#5555FF", "a": "#55FF55", "b": "#55FFFF",
               "c": "#FF5555", "d": "#FF55FF", "e": "#FFFF55", "f": "#FFFFFF"}
codes = {"r": "\x1b[0m", "l": "\x1b[1m", "o": "\x1b[3m", "n": "\x1b[4m", "k": "\x1b[40m"}
for k, v in color_codes.items():
    r, g, b = [int(v[i:i + 2], 16) for i in range(1, len(v), 2)]
    codes[k] = f"\x1b[38;2;{r};{g};{b}m"
allowed_symbols = set("0123456789abcdefABCDEF")


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
                a_as, gds, bdsa = [int(thing[i:i + 2], 16) for i in range(1, len(thing), 2)]
                msg += f"\x1b[38;2;{a_as};{gds};{bdsa}m"
                continue
            msg += "&" + symbol
            continue

        msg += symbol
        continue
    return msg


def fix_type(thing):
    try:
        thing = int(thing)
    except Exception:
        try:
            thing = float(thing)
        except Exception:
            if thing == "False":
                thing = False
            elif thing == "True":
                thing = True
    return thing


def download_latest_release(reload=False):
    global data, an_data
    url = requests.get("https://api.github.com/repos/donzgold/JustMC_compilator/releases/latest").json()["assets"][-1][
        "browser_download_url"]
    filereq = requests.get(url, stream=True)
    open("release.zip", "wb").write(filereq.content)
    if os.path.isfile("jmcc.properties"):
        with zipfile.ZipFile(f"release.zip", "a") as z:
            for zip_info in z.infolist():
                if zip_info.filename != 'jmcc.properties':
                    z.extract(zip_info)
                else:
                    z.getinfo(zip_info.filename).filename = "jmcc2.properties"
                    z.extract("jmcc.properties")
        an_data = Properties(text=open("jmcc2.properties", "r+", encoding="UTF-8").read())
        data["release_version"] = an_data["release_version"]
        data["data_version"] = an_data["data_version"]
        data["current_version"] = an_data["current_version"]
        data.save_properties(open("jmcc.properties", "w+", encoding="UTF-8"))
        os.remove("jmcc2.properties")
    else:
        shutil.unpack_archive("release.zip")
    os.remove("release.zip")
    del filereq
    print(minecraft_based_text("&f" + translate("jmcc.download.last_release")))
    if reload:
        print(minecraft_based_text("&c" + translate("error.load.because.update")))
    exit()


def download_latest_version(reload=False):
    global data, an_data
    filereq = requests.get('https://raw.githubusercontent.com/donzgold/JustMC_compilator/master/release.zip')
    open("release.zip", "wb").write(filereq.content)
    if os.path.isfile("jmcc.properties"):
        with zipfile.ZipFile(f"release.zip", "a") as z:
            for zip_info in z.infolist():
                if zip_info.filename != 'jmcc.properties':
                    z.extract(zip_info)
                else:
                    z.getinfo(zip_info.filename).filename = "jmcc2.properties"
                    z.extract("jmcc.properties")
        an_data = Properties(text=open("jmcc2.properties", "r+", encoding="UTF-8").read())
        data["release_version"] = an_data["release_version"]
        data["data_version"] = an_data["data_version"]
        data["current_version"] = an_data["current_version"]
        data.save_properties(open("jmcc.properties", "w+", encoding="UTF-8"))
        os.remove("jmcc2.properties")
    else:
        shutil.unpack_archive("release.zip")
    os.remove("release.zip")
    del filereq
    print(minecraft_based_text("&f" + translate("jmcc.download.last_version")))
    if reload:
        print(minecraft_based_text("&c" + translate("error.load.because.update")))


def download_latest_data():
    global data, an_data
    if not os.path.isdir("data"):
        os.mkdir("data")
    open("data/actions.json", "w+").write(
        requests.get('https://raw.githubusercontent.com/donzgold/JustMC_compilator/master/data/actions.json').text)
    open("data/events.json", "w+").write(
        requests.get('https://raw.githubusercontent.com/donzgold/JustMC_compilator/master/data/events.json').text)
    open("data/values.json", "w+").write(
        requests.get('https://raw.githubusercontent.com/donzgold/JustMC_compilator/master/data/values.json').text)
    data["data_version"] = an_data["data_version"]
    data.save_properties(open("jmcc.properties", "w+", encoding="UTF-8"))
    print(minecraft_based_text("&f" + translate("jmcc.download.last_data")))


def check_updates():
    global data, an_data
    an_data = Properties(text=requests.get(
        'https://raw.githubusercontent.com/donzgold/JustMC_compilator/master/jmcc.properties').text)
    if data["check_beta_versions"] and (data["release_version"] < an_data["release_version"]):
        print(minecraft_based_text("&6" + translate("warning.jmcc_release_version.is_not_last",
                                                    {0: an_data['release_version'] - data['release_version']})))
        if data["auto_update"]:
            print(minecraft_based_text("&f" + translate("jmcc.fixing")))
            download_latest_release()
            return

    elif data["check_beta_versions"] and (data["current_version"] < an_data["current_version"]):
        print(minecraft_based_text("&6" + translate("warning.jmcc_beta_version.is_not_last",
                                                    {0: an_data['current_version'] - data['current_version']})))
        if data["auto_update"]:
            print(minecraft_based_text("&f" + translate("jmcc.fixing")))
            download_latest_version()
            return
    if data["data_version"] < an_data["data_version"]:
        print(minecraft_based_text("&6" + translate("warning.jmcc_data_version.is_not_last",
                                                    {0: an_data['data_version'] - data['data_version']})))
        if data["auto_update"]:
            print(minecraft_based_text("&f" + translate("jmcc.fixing")))
            download_latest_data()


os.system('color')
path = os.path.realpath(__file__)
path = path[:path.rfind("\\")]
os.chdir(path)
an_data = Properties(text="")
if not os.path.isfile("jmcc.properties"):
    lang = None
    download_latest_release()
    exit()
else:
    data = Properties(text=open("jmcc.properties", "r", encoding="UTF-8").read())
    if "lang" in data and os.path.isfile("data/lang/" + data["lang"] + ".properties"):
        lang = Properties(text=open("data/lang/" + data["lang"] + ".properties", "r", encoding="UTF-8").read())
    else:
        lang = None
end_time = time()
print(minecraft_based_text(translate("jmcc.prepare_data_time", {0: round(end_time - start_time, 3)})))
if __name__ == "__main__":
    if data["check_updates"]:
        a = is_connected()
        if a:
            check_updates()
    additional = sys.argv[1:]
    if len(additional) == 0:
        additional = ["about"]
    if len(additional) >= 1:
        if len(additional) > 2:
            multi_known_dict = {"-o": "output"}
            small_known_dict = {"-u": "upload", "-c": "compact", "-s": "save", "-su": ("save", "upload"), "-us": ("save", "upload")}
            known_attr = data.properties.copy()
            i1 = 2
            while i1 < len(additional):
                if additional[i1] in multi_known_dict and i1 + 1 < len(additional):
                    known_attr[multi_known_dict[additional[i1]]] = fix_type(additional[i1 + 1])
                    i1 += 2
                elif additional[i1] in small_known_dict:
                    if isinstance(small_known_dict[additional[i1]], (tuple, list, set)):
                        for i2 in small_known_dict[additional[i1]]:
                            known_attr[i2] = True
                    else:
                        known_attr[small_known_dict[additional[i1]]] = True
                    i1 += 1
                else:
                    print(minecraft_based_text("&c" + translate("error.jmcc.unknown_arg", insert={0: additional[i1]})))
                    exit()
        else:
            known_attr = data.properties.copy()
        if additional[0] == "compile" and len(additional) > 1:
            from compilator import compile_file

            compile_file(additional[1], upload=known_attr.setdefault("upload", False), properties=known_attr)
        elif additional[0] == "decompile" and len(additional) > 1:
            from decompilator import decompile_file

            decompile_file(additional[1], properties=known_attr)
        elif additional[0] == "fix_items" and len(additional) > 1:
            from decompilator import fix_items

            fix_items(additional[1], properties=known_attr)
        elif additional[0] == "update" and len(additional) > 1:
            if additional[1] == "data":
                an_data = Properties(text=requests.get(
                    'https://raw.githubusercontent.com/donzgold/JustMC_compilator/master/jmcc.properties').text)
                download_latest_data()
            elif additional[1] == "to_release":
                download_latest_release(reload=False)
            elif additional[1] == "to_version":
                download_latest_version(reload=False)
            else:
                print(minecraft_based_text("&c" + translate("error.unknown_command", {0: "&4help"})))
        elif additional[0] == "help":
            command_list = ["help", "about", "compile", "decompile", "fix_items", "update.data", "update.to_release",
                            "update.to_version"]
            print(minecraft_based_text("&f" + translate("jmcc.command.help")))
            for command in command_list:
                print(minecraft_based_text("&f " + translate(f"jmcc.command.{command}.description")))
        elif additional[0] == "about":
            print(minecraft_based_text("&f" + translate("jmcc.command.about")))
        else:
            print(minecraft_based_text("&c" + translate("error.unknown_command", {0: "&4help"})))
