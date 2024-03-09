import shutil
import sys
import zipfile

import requests
import os
import socket


def is_connected():
    try:
        socket.create_connection(("1.1.1.1", 53))
        return True
    except:
        pass
    return False


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


def fix_type(thing):
    try:
        thing = int(thing)
    except:
        try:
            thing = float(thing)
        except:
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
    with open("release.zip", "wb") as receive:
        shutil.copyfileobj(filereq.raw, receive)
    receive.close()
    if os.path.isfile("jmcc.properties"):
        with zipfile.ZipFile(f"release.zip", "a") as z:
            for zip_info in z.infolist():
                if zip_info.filename != 'jmcc.properties':
                    z.extract(zip_info)
                else:
                    zip_info.filename = "jmcc2.properties"
        an_data = {i[:i.find("=")].strip(): fix_type(
            i[i.find("=") + 1:].encode('raw_unicode_escape').decode('unicode_escape').strip()) for i in
            open("jmcc2.properties", "r+")}
        data["release_version"] = an_data["release_version"]
        data["data_version"] = an_data["data_version"]
        data["current_version"] = an_data["current_version"]
        open("jmcc.properties", "w+").write(f"{k}={v}" for k, v in data.items())
        os.remove("jmcc2.properties")
    else:
        shutil.unpack_archive("release.zip")
    os.remove("release.zip")
    del filereq
    print(minecraft_based_text("&fУстановлен последний релиз jmcc"))
    if reload:
        print(minecraft_based_text("&cК сожалению запуск прервался из-за обновления."))
    exit()


def download_latest_version(reload=False):
    global data, an_data
    filereq = requests.get('https://raw.githubusercontent.com/donzgold/JustMC_compilator/master/release.zip')
    with open("release.zip", "wb") as receive:
        shutil.copyfileobj(filereq.raw, receive)
    receive.close()
    if os.path.isfile("jmcc.properties"):
        with zipfile.ZipFile(f"release.zip", "a") as z:
            for zip_info in z.infolist():
                if zip_info.filename != 'jmcc.properties':
                    z.extract(zip_info)
                else:
                    zip_info.filename = "jmcc2.properties"
        an_data = {i[:i.find("=")].strip(): fix_type(
            i[i.find("=") + 1:].encode('raw_unicode_escape').decode('unicode_escape').strip()) for i in open("jmcc2.properties", "r+")}
        data["release_version"] = an_data["release_version"]
        data["data_version"] = an_data["data_version"]
        data["current_version"] = an_data["current_version"]
        open("jmcc.properties", "w+").write(f"{k}={v}" for k, v in data.items())
        os.remove("jmcc2.properties")
    else:
        shutil.unpack_archive("release.zip")
    os.remove("release.zip")
    del filereq
    print(minecraft_based_text("&fУстановлена последняя версия jmcc"))
    if reload:
        print(minecraft_based_text("&cК сожалению запуск прервался из-за обновления."))
    exit()


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
    open("jmcc.properties").write(f"{k}={v}" for k, v in data.items())
    print(minecraft_based_text("&fУстановлена последняя версия базы"))


def check_updates():
    global an_data
    an_data = {i[:i.find("=")].strip(): fix_type(
        i[i.find("=") + 1:].encode('raw_unicode_escape').decode('unicode_escape').strip()) for i in requests.get(
        'https://raw.githubusercontent.com/donzgold/JustMC_compilator/master/jmcc.properties').text.split("\n")}
    if data["check_beta_versions"] and data["release_version"] < an_data["release_version"]:
        print(minecraft_based_text(
            f"&6Релизная версия jmcc отстаёт от последней на {an_data['release_version'] - data['release_version']}"))
        if data["auto_update"]:
            print(minecraft_based_text("&fИсправляем..."))
            download_latest_release()
            return

    elif not data["check_beta_versions"] and data["current_version"] < an_data["current_version"]:
        print(minecraft_based_text(
            f"&6Бета версия jmcc отстаёт от последней на {an_data['current_version'] - data['current_version']}"))
        if data["auto_update"]:
            print(minecraft_based_text("&fИсправляем..."))
            download_latest_version()
            return
    if data["data_version"] < an_data["data_version"]:
        print(minecraft_based_text(
            f"&6База кода jmcc отстаёт от последней на {an_data['data_version'] - data['data_version']}"))
        print(minecraft_based_text("&fИсправляем..."))
        download_latest_data()


path = os.path.realpath(__file__)
path = path[:path.rfind("\\")]
os.chdir(path)
an_data = {}
if not os.path.isfile("jmcc.properties"):
    download_latest_release()
    exit()
else:
    data = {i[:i.find("=")].strip(): fix_type(
        i[i.find("=") + 1:].encode('raw_unicode_escape').decode('unicode_escape').strip()) for i in
        open("jmcc.properties", "r").readlines()}
a = is_connected()
if a:
    check_updates()
if __name__ == "__main__":
    additional = sys.orig_argv[2:]
    if len(additional) == 0:
        additional = ["about"]
    if len(additional) >= 1:
        if additional[0] == "compile" and len(additional) > 1:
            from compilator import compile_file

            compile_file(additional[1], upload=additional[-1] == "-u")
        elif additional[0] == "decompile" and len(additional) > 1:
            from decompilator import decompile_file

            decompile_file(additional[1])
        elif additional[0] == "update" and len(additional) > 1:
            if additional[1] == "data":
                download_latest_data()
            elif additional[1] == "to_release":
                download_latest_release(reload=False)
            elif additional[1] == "to_version":
                download_latest_version(reload=False)
            else:
                print(minecraft_based_text("&cНеизвестная команда, попробуйте команду &4help"))
        elif additional[0] == "help":
            print(minecraft_based_text("&fПомощь по &eJMCC &fdonzgold edition:\n"
                                       "Команды:\n"
                                       " about - выести сведения о программе\n"
                                       " help - вывести это сообщение\n"
                                       " compile <file_path> [-u] &7- &fскомпилировать файл, -u для загрузки на сервер.\n"
                                       " decompile <file_path> &7- &fдекомпилировать json в код\n"
                                       " update data &7- &fобновить базу кода\n"
                                       " update to_release &7- &fобновиться до последнего релиза\n"
                                       " update to_version &7- &fобновиться до последней версии"))
        elif additional[0] == "about":
            print(minecraft_based_text(
                "&eJMCC &fdonzgold edition:\nЭто джей эм си си, он компилирует код в json, который используется на сервере justmc.ru\nПомощь по командам доступна с помощью команды &ehelp"))
        else:
            print(minecraft_based_text("&cНеизвестная команда, попробуйте команду &4help"))
