import sys
import re

if sys.version_info <= (3, 0):
    print("This program only runs in python3", file=sys.stderr)
    exit(1)

mappings = []
with open("arpa-ipa.map") as f:
    for line in f:
        mappings.append(line.strip().split("\t"))

brackets = re.compile('\(\d+\)')
numbers = re.compile('[012]')
capital = re.compile('[A-Z]')
with open("cmudict.dict") as f:
    for line in f:
        line = line.strip()
        word, arpa = line.split(" ", 1)
        word = brackets.sub("", word)
        arpa = numbers.sub("", arpa)
        for mapping in mappings:
            arpa = arpa.replace(mapping[0], mapping[1])
        if capital.match(arpa):
            print("Could not map phrase: %s %s" % (word, arpa),
                  file=sys.stderr)
        print("%s\t%s" % (word, arpa))
