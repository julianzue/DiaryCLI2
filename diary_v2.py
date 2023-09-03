from colorama import Fore, Style, init
import time
import os
from datetime import datetime

init()


# colors
b = Fore.LIGHTBLUE_EX
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
        out = b + "[" + symbol + "] " + re + text

    elif type == "input":
        out = y + "[" + symbol + "] " + text + re

    elif type == "error":
        out = r + "[" + symbol + "] " + re + text

    return out


# create diary.txt file
if not os.path.isfile("diary.txt"):
    os.system("touch diary.txt")

    text = "File " + b + "diary.txt" + re + " successfully created!"
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
            {"name": "list all", "cmd": self.list_all, "description": "Lists the whole diary list"},
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
        event_day = input(output("input", "+", "Today? [Y|n]: "))

        if event_day == "Y" or event_day == "y" or event_day == "":
            day = time.strftime("%Y-%m-%d")
        else:
            day = input(output("input", "+", "Date: "))

        event_time = input(output("input", "+", "Time: "))
        
        print("")

        # dates = []

        #with open("diary.txt", "r") as fr:
        #    for line in fr.readlines():
        #        dates.append(line.strip("\n").split(" | ")[1])

        #dates.sort(key=lambda date: datetime.strptime(date, ("%Y-%m-%d %H:%M")))

        #print("dates sorted: ", dates)

        with open("diary.txt", "a") as fa:
            fa.write(time.strftime("%Y-%m-%d %H:%M") + " | " + day + " " + event_time + " | " + event + "\n")

            text = "Event: " + b + event + re + " sucessfully added to " + c + "diary.txt" + re + "!"
            print(output("info", "*", text))

        self.prompt()


    def list(self):

        lines_sorted = []
        lines = []

        with open("diary.txt", "r") as fr:
            for index, line in enumerate(fr.readlines(), 1):
                lines_sorted.append(line.strip("\n").split(" | ")[1])
                lines.append(line.strip())

        lines_sorted.sort(key=lambda date: datetime.strptime(date, ("%Y-%m-%d %H:%M")))

        for index, line in enumerate(lines_sorted):
            for l in lines:
                if line in l:
                    print(b + "[*] " + re + "{:03d}".format(index) + " " + b + l.strip("\n").split(" | ")[1] + re + " " + l.strip("\n").split(" | ")[2])

        self.prompt()


    def help(self):
        for cmd in self.cmds:
            print(b + "[*] " + re + cmd["name"] + dim + " " + cmd["description"] + res)

        self.prompt()


    def search(self):
        search = input(output("input", "+", "Search: "))

        print("")

        lines_sorted = []
        lines = []

        with open("diary.txt", "r") as fr:
            for index, line in enumerate(fr.readlines(), 1):
                lines_sorted.append(line.strip("\n").split(" | ")[1])
                lines.append(line.strip())

        lines_sorted.sort(key=lambda date: datetime.strptime(date, ("%Y-%m-%d %H:%M")))

        for index, line in enumerate(lines_sorted):
            for l in lines:
                if line in l:
                    
                    if search == "today":
                        today = time.strftime("%Y-%m-%d")
                        
                        if today in l:
                            print(b + "[*] " + re + "{:03d}".format(index +1 ) + " " + b + l.strip("\n").split(" | ")[1] + re + " " + l.strip("\n").split(" | ")[2])

                    elif search in l:
                        print(b + "[*] " + re + "{:03d}".format(index + 1) + " " + b + l.strip("\n").split(" | ")[1] + re + " " + l.strip("\n").split(" | ")[2])


    def list_all(self):

        with open("diary.txt", "r") as fr:
            for index, line in enumerate(fr.readlines(), 1):
                print(b + "[*] " + re + "{:03d}".format(index) + " " + b + line.strip("\n").split(" | ")[0] + re  + " " + line.strip("\n").split(" | ")[1] + " " + b + line.strip("\n").split(" | ")[2])

        self.prompt()


Diary()
