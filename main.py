# Simple Script
# Author : JTech Software Foundation

import os

__version__ = "0.1.0 ATB"
__author__ = "JTech Software Foundation"
var = {}
const = {}
lib = {}
temp = None


def data_chg(data):
    if data:
        raw = data.split("|")
        if raw[0] == "STRING":
            return str(raw[1])
        elif raw[0] == "INTEGER":
            return int(raw[1])
        elif raw[0] == "FLOAT":
            return float(raw[1])
        elif raw[0] == "BOOLEAN":
            if raw[1] == "False" or raw[1] == "0":
                return False
            return True
        elif raw[0] == "NONE":
            return None


def code_run(input):
    global temp
    raw = input().split(" ")
    if raw[0] == "variable":
        if raw[1] == "set":
            var[raw[2]] = data_chg(raw[3])
        elif raw[1] == "get":
            temp = var.get(raw[2])
    elif raw[0] == "constant":
        if raw[1] == "create":
            if not raw[2] in const.keys():
                const[raw[2]] = data_chg(raw[3])
        elif raw[1] == "get":
            temp = const.get(raw[2])
    elif raw[0] == "temp":
        if raw[1] == "set":
            temp = data_chg(raw[2])
        elif raw[1] == "get":
            temp = temp
    elif raw[0] == "lib":
        lib[raw[2]] = raw[1]
    else:
        os.system("python ./libs/" + lib[raw[0]] + " " + raw[1:].join(" "))

