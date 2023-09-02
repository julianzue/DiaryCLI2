from colorama import Fore, Style, init
import time
import os


init()


# colors
c = Fore.LIGHTBLUE_EX # blue
g = Fore.LIGHTGREEN_EX
r = Fore.LIGHTRED_EX
y = Fore.LIGHTYELLOW_EX
re = Fore.RESET


# styles
dim = Style.DIM
res = Style.RESET_ALL


def output(type, symbol, text):

    out = ""

    if type == "info":
        out = c + "[" + symbol + "] " + re + text

    elif type == "input":
        out = y + "[" + symbol + "] " + text + re

    elif type == "error":
        out = r + "[" + symbol + "] " + re + text

    return out


# create diary.txt file
if not os.path.isfile("diary.txt"):
    os.system("touch diary.txt")

    text = "File " + c + "diary.txt" + re + " successfully created!"
    print(output("info", "*", text))


class Diary():
    def __init__(self):
        self.prompt()


    def prompt(self):
        print("")
        x = input(output("input", "+", ""))
        print("")

        self.cmds = [
            {"name": "add", "cmd": self.add, "description": "Adds an event to diary"},
            {"name": "list", "cmd": self.list, "description": "Lists the events of the diary"},
            {"name": "search", "cmd": self.search, "description": "Search in the list"},
            {"name": "help", "cmd": self.help, "description": "Shows the help page"},
            {"name": "quit", "cmd": quit, "description": "Closes the diary program"}
        ]

        for c in self.cmds:
            if c["name"] == x:
                c["cmd"]()
            #else:
            #    text = "No action with keyword " + r + x + re + "!"
            #    print(output("error", "!", text))
            #    self.prompt()

        self.prompt()


    def add(self):

        event = input(output("input", "+", "Event: "))
        
        print("")

        with open("diary.txt", "a") as fa:
            fa.write(time.strftime("%A")[:3].upper() + " " + time.strftime("%Y-%m-%d %H:%M:%S") + " | " + event + "\n")

            text = "Event: " + c + event + re + " sucessfully added to " + c + "diary.txt" + re + "!"
            print(output("info", "*", text))

        self.prompt()


    def list(self):

        with open("diary.txt", "r") as fr:
            for index, line in enumerate(fr.readlines(), 1):
                print(c + "[*] " + re + "{:03d}".format(index) + " " + c + line.strip("\n").split(" | ")[0] + re + " " + line.strip("\n").split(" | ")[1])

        self.prompt()


    def help(self):
        for cmd in self.cmds:
            print(c + "[*] " + re + cmd["name"] + dim + " " + cmd["description"] + res)

        self.prompt()


    def search(self):
        search = input(output("input", "+", "Search: "))

        print("")

        with open("diary.txt", "r") as fr:
            for index, line in enumerate(fr.readlines(), 1):

                if search == "today":
                    today = time.strftime("%Y-%m-%d")
                    
                    if today in line:
                        print(c + "[*] " + re + "{:03d}".format(index) + " " + c + line.strip("\n").split(" | ")[0] + re + " " + line.strip("\n").split(" | ")[1])

                elif search in line:
                    print(c + "[*] " + re + "{:03d}".format(index) + " " + c + line.strip("\n").split(" | ")[0] + re + " " + line.strip("\n").split(" | ")[1])


Diary()
