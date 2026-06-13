#!/usr/bin/env python3
"""Build the full research.json from raw data files."""

import json, os, re

BASE = "D:/bible/bible-studies/3am-07-hour-of-judgment"
RAW = os.path.join(BASE, "raw-data")
WS = "D:/bible/bible-studies/word-studies"

def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return ''

# Load KJV
kjv_all = {}
with open(os.path.join(RAW, "kjv-verses-all.txt"), 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if '\t' in line:
            ref, text = line.split('\t', 1)
            kjv_all[ref] = text

kjv_full = {}
with open("D:/bible/tools/data/kjv.txt", 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if '\t' in line:
            ref, text = line.split('\t', 1)
            kjv_full[ref] = text

# Supplement missing refs
for ref in ["Psalm 9:7","Psalm 9:8","Psalm 50:3","Psalm 50:4","Psalm 50:5","Psalm 50:6",
            "Psalm 69:28","Psalm 96:13","Psalm 139:16",
            "Revelation 14:6","Revelation 14:7","Revelation 14:8",
            "Daniel 7:9","Daniel 7:10","Daniel 7:13","Daniel 7:14",
            "Daniel 7:22","Daniel 7:26","Daniel 7:27",
            "Revelation 11:15","Revelation 11:17","Revelation 11:18","Revelation 11:19",
            "Genesis 11:5","Genesis 11:6","Genesis 11:7"]:
    if ref in kjv_full:
        kjv_all[ref] = kjv_full[ref]

def kjv(ref):
    return kjv_all.get(ref, kjv_full.get(ref, ""))

# Load parsing
def split_parsing(text):
    result = {}
    for sec in text.split("===SEPARATOR==="):
        sec = sec.strip()
        if not sec: continue
        m = re.search(r'^\s+(.+?) - GRAMMATICAL ANALYSIS', sec, re.MULTILINE)
        if m:
            result[m.group(1).strip()] = sec
        else:
            for line in sec.split('\n'):
                line = line.strip()
                if line and not line.startswith(('=','-','Hebrew','Lemma','Greek')):
                    if any(line.startswith(b) for b in ['Daniel','Zechariah','Genesis','Exodus']):
                        result[line] = sec
                        break
    return result

all_greek = {}
for fn in ["greek-parsing-batch1.txt","greek-parsing-batch2.txt","greek-parsing-batch3.txt"]:
    all_greek.update(split_parsing(read_file(os.path.join(RAW, fn))))

all_hebrew = {}
all_hebrew.update(split_parsing(read_file(os.path.join(RAW, "hebrew-parsing-batch1.txt"))))
h = read_file(os.path.join(RAW, "hebrew-parsing-dan7-26.txt")).strip()
if h:
    all_hebrew["Daniel 7:26"] = h

# Load the research template from the JSON file we'll write inline
research = json.loads(read_file(os.path.join(RAW, "research_template.json")))

# Inject raw parsing
research["raw_parsing"] = {"greek": {}, "hebrew": {}}
for ref, text in all_greek.items():
    research["raw_parsing"]["greek"][ref] = text
for ref, text in all_hebrew.items():
    research["raw_parsing"]["hebrew"][ref] = text

# Write
out = os.path.join(BASE, "research.json")
with open(out, 'w', encoding='utf-8') as f:
    json.dump(research, f, indent=2, ensure_ascii=False)

size = os.path.getsize(out)
print(f"Written research.json: {size} bytes ({size/1024:.1f} KB)")
print(f"Topics: {len(research['topics'])}")
print(f"Verses: {len(research['verses'])}")
print(f"Word studies: {len(research['word_studies'])}")
print(f"Parallels: {len(research['parallels'])}")
print(f"Greek parsing: {len(research['raw_parsing']['greek'])}")
print(f"Hebrew parsing: {len(research['raw_parsing']['hebrew'])}")
