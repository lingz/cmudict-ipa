#! /usr/bin/env python3

import sys
import re

if sys.version_info <= (3, 0):
    print("This program only runs in python3", file=sys.stderr)
    exit(1)

mappings = {}
with open("arpa-ipa.map") as f:
    for line in f:
        arpa, ipa = line.strip().split("\t")
        mappings[arpa] = ipa

brackets = re.compile('\(\d+\)')
numbers = re.compile('[012]')
comments = re.compile(' #.+$')
with open("cmudict.dict") as f:
    for line in f:
        line = line.strip()
        line = comments.sub("", line)

        word, arpa = line.split(" ", 1)
        word = brackets.sub("", word)
        arpa = numbers.sub("", arpa).split(" ")
        mapped = []
        for part in arpa:
            ipa = mappings.get(part)
            if ipa:
                mapped.append(ipa)
            else:
                print("Could not map symbol %s in phrase: %s" % (part, word),
                      file=sys.stderr)
                continue
        print("%s\t%s" % (word, " ".join(mapped)))
