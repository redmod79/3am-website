#!/usr/bin/env python3
"""Build research.json from raw data files."""

import json
import os
import re

BASE = "D:/bible/bible-studies/3am-07-hour-of-judgment"
RAW = os.path.join(BASE, "raw-data")
WS = "D:/bible/bible-studies/word-studies"
GR = "D:/bible/bible-studies/grammar-reference"

def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return ''

# Read all raw KJV verses
kjv_all = {}
with open(os.path.join(RAW, "kjv-verses-all.txt"), 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if '\t' in line:
            ref, text = line.split('\t', 1)
            kjv_all[ref] = text

# Also read full KJV
kjv_full = {}
with open("D:/bible/tools/data/kjv.txt", 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if '\t' in line:
            ref, text = line.split('\t', 1)
            kjv_full[ref] = text

# Supplement
for ref in ["Psalm 9:7", "Psalm 9:8", "Psalm 50:3", "Psalm 50:4", "Psalm 50:5", "Psalm 50:6",
            "Psalm 69:28", "Psalm 96:13", "Psalm 139:16",
            "Revelation 14:6", "Revelation 14:7", "Revelation 14:8",
            "Daniel 7:9", "Daniel 7:10", "Daniel 7:13", "Daniel 7:14",
            "Daniel 7:22", "Daniel 7:26", "Daniel 7:27",
            "Revelation 11:15", "Revelation 11:17"]:
    if ref in kjv_full:
        kjv_all[ref] = kjv_full[ref]

# Read parsing outputs
greek1 = read_file(os.path.join(RAW, "greek-parsing-batch1.txt"))
greek2 = read_file(os.path.join(RAW, "greek-parsing-batch2.txt"))
greek3 = read_file(os.path.join(RAW, "greek-parsing-batch3.txt"))
hebrew1 = read_file(os.path.join(RAW, "hebrew-parsing-batch1.txt"))
hebrew_dan726 = read_file(os.path.join(RAW, "hebrew-parsing-dan7-26.txt"))

def split_parsing(text):
    result = {}
    sections = text.split("===SEPARATOR===")
    for sec in sections:
        sec = sec.strip()
        if not sec:
            continue
        m = re.search(r'^\s+(.+?) - GRAMMATICAL ANALYSIS', sec, re.MULTILINE)
        if m:
            ref = m.group(1).strip()
            result[ref] = sec
        else:
            for line in sec.split('\n'):
                line = line.strip()
                if line and not line.startswith('=') and not line.startswith('-') and not line.startswith('Hebrew') and not line.startswith('Lemma') and not line.startswith('Greek'):
                    if any(line.startswith(b) for b in ['Daniel', 'Zechariah', 'Genesis', 'Exodus']):
                        result[line] = sec
                        break
    return result

all_greek = {}
for t in [greek1, greek2, greek3]:
    all_greek.update(split_parsing(t))

all_hebrew = {}
all_hebrew.update(split_parsing(hebrew1))
dan726_text = hebrew_dan726.strip()
if dan726_text:
    all_hebrew["Daniel 7:26"] = dan726_text

def kjv(ref):
    return kjv_all.get(ref, kjv_full.get(ref, ""))

print(f"Greek sections: {list(all_greek.keys())}")
print(f"Hebrew sections: {list(all_hebrew.keys())}")
print(f"KJV verses loaded: {len(kjv_all)}")
