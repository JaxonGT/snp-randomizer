import os, sys
import random

path = "."
maxNum = 60

for file in os.listdir(path):
    if file.endswith(".txt"):

        lines = []
        headers = []
        chars = []

        f = open(file, "r")
        for line in f:
            if line.startswith(">"):
                headers.append(line)
            else:
                lines.append(line)

        f.close()

        if len(lines) < maxNum:
            maxNum = len(lines)

        for i in range(maxNum):
            chars = []
            for j in range(len(lines)):
                chars.append("")
                for k in range(i+1):
                    rand = random.randrange(0,len(lines[0])-1,1)
                    chars[j] = chars[j] + lines[j][rand]
                chars[j] = chars[j] + "\n"

            f = open(file.replace(".txt", "_" + str(i+1) + ".txt"), "w")

            for k in range(len(headers)):
                f.write(headers[k])
                f.write(chars[k])

            f.close()