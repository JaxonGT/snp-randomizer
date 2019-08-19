import os, sys
import random

path = "."
maxNum = 60

for file in os.listdir(path):
    if file.endswith(".txt"):

        lines = []
        edit = []
        headers = []
        chars = []

        f = open(file, "r")
        for line in f:
            if line.startswith(">"):
                headers.append(line)
            else:
                lines.append(line)

        f.close()

        length = len(lines[0]) - 1

        if length < maxNum:
            maxNum = length

        for i in range(maxNum):
            chars = []
            for n in range(len(lines)):
                chars.append("")

            edit = lines.copy()
            for k in range(i+1):
                rand = random.randrange(0,len(edit[0])-1,1)
                for j in range(len(lines)):
                    chars[j] = chars[j] + edit[j][rand]
                    edit[j] = edit[j][:rand] + edit[j][rand+1:]

            for n in range(len(chars)):
                chars[n] = chars[n] + "\n"

            f = open(file.replace(".txt", "_" + str(i+1) + ".txt"), "w")

            for k in range(len(headers)):
                f.write(headers[k])
                f.write(chars[k])

            f.close()