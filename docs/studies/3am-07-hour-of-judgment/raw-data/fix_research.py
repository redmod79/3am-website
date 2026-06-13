#!/usr/bin/env python3
"""Fix all 53 validation errors in research.json."""
import json, os

BASE = "D:/bible/bible-studies/3am-07-hour-of-judgment"

with open(os.path.join(BASE, "research.json"), 'r', encoding='utf-8') as f:
    R = json.load(f)

# ========== 1. FIX OCCURRENCE COUNTS (23 errors) ==========
oc_fixes = {
    "G2919": 132,
    "G2632": 22,
    "G350": 18,
    "G4793": 5,
    "H1779": 21,
    "H1777": 27,
    "H4941": 448,
    "H8199": 223,
    "H7378": 79,
    "G2064": 664,
    "G5401": 47,
    "G5399": 110,
    "G2098": 77,
    "G2097": 61,
    "G975": 32,
    "H5612": 194,
    "G1391": 168,
    "G2041": 176,
    "G1492": 334,
    "G2250": 388,
    "G1342": 81,
    "G1343": 92,
    "G1344": 48,
}

for ws in R["word_studies"]:
    if ws["strongs"] in oc_fixes:
        old = ws["occurrence_count"]
        ws["occurrence_count"] = oc_fixes[ws["strongs"]]
        print(f"  OC fix: {ws['strongs']} {old} -> {ws['occurrence_count']}")

# Also fix the summary text that references old counts
for ws in R["word_studies"]:
    s = ws["strongs"]
    if s == "G2919" and "98 NT" in ws["summary"]:
        ws["summary"] = ws["summary"].replace("98 NT verses", "132 tokens across NT")
    elif s == "H4941" and "406 verses" in ws["summary"]:
        ws["summary"] = ws["summary"].replace("406 verses", "448 tokens")
    elif s == "H8199" and "182 verses" in ws["summary"]:
        ws["summary"] = ws["summary"].replace("182 verses", "223 tokens")
    elif s == "H7378" and "59 verses" in ws["summary"]:
        ws["summary"] = ws["summary"].replace("59 verses", "79 tokens")
    elif s == "G2064" and "604 NT verses" in ws["summary"]:
        ws["summary"] = ws["summary"].replace("604 NT verses", "664 tokens")
    elif s == "G5399" and "90 NT verses" in ws["summary"]:
        ws["summary"] = ws["summary"].replace("90 NT verses", "110 tokens")
    elif s == "G2097" and "52 NT verses" in ws["summary"]:
        ws["summary"] = ws["summary"].replace("52 NT verses", "61 tokens")
    elif s == "G1391" and "151 NT verses" in ws["summary"]:
        ws["summary"] = ws["summary"].replace("151 NT verses", "168 tokens")
    elif s == "G2041" and "161 NT verses" in ws["summary"]:
        ws["summary"] = ws["summary"].replace("161 NT verses", "176 tokens")
    elif s == "G1492" and "297 NT verses" in ws["summary"]:
        ws["summary"] = ws["summary"].replace("297 NT verses", "334 tokens")
    elif s == "G2250" and "365 NT verses" in ws["summary"]:
        ws["summary"] = ws["summary"].replace("365 NT verses", "388 tokens")
    elif s == "G1342" and "76 NT verses" in ws["summary"]:
        ws["summary"] = ws["summary"].replace("76 NT verses", "81 tokens")
    elif s == "G1343" and "85 NT verses" in ws["summary"]:
        ws["summary"] = ws["summary"].replace("85 NT verses", "92 tokens")
    elif s == "G1344" and "36 NT verses" in ws["summary"]:
        ws["summary"] = ws["summary"].replace("36 NT verses", "48 tokens")

print(f"Fixed {len(oc_fixes)} occurrence counts")

# ========== 2. FIX PMI VALUE (1 error) ==========
for ws in R["word_studies"]:
    if ws["strongs"] == "H7379":
        ws["summary"] = ws["summary"].replace("PMI 20.28", "PMI 5.96")
        print("Fixed H7379 PMI: 20.28 -> 5.96")
        break

# ========== 3. ADD MISSING VERSES (19 errors) ==========
missing_verses = [
    {
        "reference": "Rom 14:10-12",
        "heading": "We shall all stand before the bema of God -- universal accountability",
        "kjv_text": "But why dost thou judge thy brother? or why dost thou set at nought thy brother? for we shall all stand before the judgment seat of Christ. For it is written, [As] I live, saith the Lord, every knee shall bow to me, and every tongue shall confess to God. So then every one of us shall give account of himself to God.",
        "context": "Paul addresses mutual judgment among believers. Every person will stand before God's judgment seat and give personal account.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "bema tou Christou (judgment seat of Christ). Universal: every knee, every tongue, every one of us. Confirms believers face evaluative accounting."
    },
    {
        "reference": "Heb 9:27",
        "heading": "Appointed unto men once to die, then judgment -- universal appointment",
        "kjv_text": "And as it is appointed unto men once to die, but after this the judgment:",
        "context": "Within Hebrews argument about Christ's once-for-all sacrifice. Judgment follows death as a universal human appointment.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "apokeitai (G606) 'it is appointed/laid up.' krisis (G2920) — same word as Rev 14:7. Death and judgment are parallel appointments."
    },
    {
        "reference": "Heb 10:26-30",
        "heading": "Fearful expectation of judgment for willful sin -- the serious side",
        "kjv_text": "For if we sin wilfully after that we have received the knowledge of the truth, there remaineth no more sacrifice for sins, But a certain fearful looking for of judgment and fiery indignation, which shall devour the adversaries. He that despised Moses' law died without mercy under two or three witnesses: Of how much sorer punishment, suppose ye, shall he be thought worthy, who hath trodden under foot the Son of God, and hath counted the blood of the covenant, wherewith he was sanctified, an unholy thing, and hath done despite unto the Spirit of grace? For we know him that hath said, Vengeance [belongeth] unto me, I will recompense, saith the Lord. And again, The Lord shall judge his people.",
        "context": "Hebrews warning about willful apostasy after receiving truth. Judgment is fearful for those who trample the Son of God.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "phobera ekdoche kriseos — fearful expectation of judgment. The serious side: judgment threatens the apostate. But note v.30 'the Lord shall judge his people' — echoes Deut 32:36, judgment OF the covenant community."
    },
    {
        "reference": "Rev 6:15-17",
        "heading": "Great day of wrath -- those who hide from judgment contrast with 1 John 4:17 boldness",
        "kjv_text": "And the kings of the earth, and the great men, and the rich men, and the chief captains, and the mighty men, and every bondman, and every free man, hid themselves in the dens and in the rocks of the mountains; And said to the mountains and rocks, Fall on us, and hide us from the face of him that sitteth on the throne, and from the wrath of the Lamb: For the great day of his wrath is come; and who shall be able to stand?",
        "context": "Sixth seal. Universal terror before the Lamb's wrath. The wicked hide — contrasts sharply with 1 John 4:17's boldness in judgment.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "elthen he hemera he megale tes orges — 'the great day of his wrath IS COME' — same prophetic aorist construction as Rev 14:7 elthen he hora. The question 'who shall be able to stand?' is answered by those with parrhesia (1 John 4:17)."
    },
    {
        "reference": "Matt 12:36-37",
        "heading": "Every idle word -- by words justified or condemned; comprehensive judgment",
        "kjv_text": "But I say unto you, That every idle word that men shall speak, they shall give account thereof in the day of judgment. For by thy words thou shalt be justified, and by thy words thou shalt be condemned.",
        "context": "Jesus warns the Pharisees about accountability for speech. Every idle word enters the judgment record.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "en hemera kriseos — in the day of judgment (same krisis as Rev 14:7). pan rhema argon — every idle/careless word. Judgment is comprehensive — includes speech, not just deeds. dikaiothese / katadikasthese — justified or condemned — two possible outcomes."
    },
    {
        "reference": "Heb 7:25",
        "heading": "Christ ever lives to make intercession -- ongoing high priestly ministry",
        "kjv_text": "Wherefore he is able also to save them to the uttermost that come unto God by him, seeing he ever liveth to make intercession for them.",
        "context": "Christ's permanent, unchangeable priesthood. He saves completely because He always lives to intercede.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "entygchanein (G1793 infinitive) — to make intercession. panteles (G3838) — to the uttermost/completely. pantote zon (always living) — present participle, continuous. Christ's intercession is ONGOING, not past — active during any judgment period."
    },
    {
        "reference": "Rev 3:5",
        "heading": "Will not blot out name from book of life -- preservation promise during judgment",
        "kjv_text": "He that overcometh, the same shall be clothed in white raiment; and I will not blot out his name out of the book of life, but I will confess his name before my Father, and before his angels.",
        "context": "Promise to the overcomer in Sardis. Names preserved in the book of life + confessed before the Father.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "ou me exaleipso — emphatic double negative: 'I will absolutely NOT blot out.' biblos tes zoes — book of life. homologeso — I will confess/acknowledge. Preservation promise directly linked to the judgment book imagery."
    },
    {
        "reference": "Rev 13:8",
        "heading": "Book of life of the Lamb slain from foundation -- names written before judgment",
        "kjv_text": "And all that dwell upon the earth shall worship him, whose names are not written in the book of life of the Lamb slain from the foundation of the world.",
        "context": "The beast's universal worship. Those NOT written in the book of life worship the beast. Names inscribed from the foundation of the world.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "bibliō tēs zōēs tou arniou — book of life of the Lamb. apo katabolēs kosmou — from the foundation of the world. Names inscribed BEFORE judgment, not determined by it."
    },
    {
        "reference": "Phil 4:3",
        "heading": "Names are in the book of life -- present-tense assurance of inscription",
        "kjv_text": "And I intreat thee also, true yokefellow, help those women which laboured with me in the gospel, with Clement also, and [with] other my fellowlabourers, whose names [are] in the book of life.",
        "context": "Paul mentions fellow workers whose names ARE (present tense) in the book of life. Present assurance of inscription.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "hōn ta onomata en bibliō zōēs — whose names [are] in the book of life. Present-tense statement of current inscription. Assurance coexists with judgment awareness."
    },
    {
        "reference": "Psa 69:28",
        "heading": "Let them be blotted from the book of the living -- OT book-of-life background",
        "kjv_text": "Let them be blotted out of the book of the living, and not be written with the righteous.",
        "context": "David's imprecatory prayer. The 'book of the living' can have names blotted from it — OT background for Rev 3:5's preservation promise.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "sepher chayyim (H5612 + H2416) — book of the living. yimmachuw — let them be blotted out. Names CAN be removed — making the Rev 3:5 promise meaningful. The judgment confirms or removes names."
    },
    {
        "reference": "Psa 139:16",
        "heading": "In thy book all my members were written -- God's comprehensive knowledge recorded",
        "kjv_text": "Thine eyes did see my substance, yet being unperfect; and in thy book all [my members] were written, [which] in continuance were fashioned, when [as yet there was] none of them.",
        "context": "David on God's intimate, comprehensive knowledge. Everything written in God's book before it existed.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "siphreka (H5612 with suffix) — in your book. God's omniscient record-keeping. The books of judgment reflect this comprehensive divine knowledge."
    },
    {
        "reference": "Isa 26:9",
        "heading": "When thy judgments are in the earth, inhabitants learn righteousness",
        "kjv_text": "With my soul have I desired thee in the night; yea, with my spirit within me will I seek thee early: for when thy judgments [are] in the earth, the inhabitants of the world will learn righteousness.",
        "context": "Isaiah's song of trust. God's judgments in the earth produce a pedagogical/redemptive effect — the world learns righteousness.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "mishpat (H4941) — judgments. tsedeq (H6664) — righteousness. Judgment as pedagogical: inhabitants LEARN righteousness through God's judgments. Redemptive, not merely punitive."
    },
    {
        "reference": "Dan 9:24",
        "heading": "Seventy weeks -- atonement-to-righteousness progression linked to judgment timing",
        "kjv_text": "Seventy weeks are determined upon thy people and upon thy holy city, to finish the transgression, and to make an end of sins, and to make reconciliation for iniquity, and to bring in everlasting righteousness, and to seal up the vision and prophecy, and to anoint the most Holy.",
        "context": "Gabriel's seventy-weeks prophecy. Six purposes: finish transgression, end sins, reconcile iniquity, bring everlasting righteousness, seal vision, anoint Most Holy.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "kaphar (H3722) — make reconciliation/atonement. tsedeq olamim — everlasting righteousness. The kaphar-to-tsedeq progression links DOA atonement to judgment timing per the dan-7-judgment-antitypical-doa study."
    },
    {
        "reference": "Lev 16:30",
        "heading": "Day of Atonement -- on this day atonement made to cleanse; typological basis",
        "kjv_text": "For on that day shall [the priest] make an atonement for you, to cleanse you, [that] ye may be clean from all your sins before the LORD.",
        "context": "The Day of Atonement ritual. Atonement (kaphar) produces cleansing (taher) from all sins before the LORD.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "kaphar (H3722) — atone/cover. taher (H2891) — cleanse/purify. The DOA typology: ritual cleansing maps to Dan 7 forensic judgment per Lev 16:30 kaphar -> Dan 8:14 nitsdaq progression."
    },
    {
        "reference": "Eph 1:13-14",
        "heading": "Sealed with the Holy Spirit of promise -- arrabon guarantee through judgment",
        "kjv_text": "In whom ye also [trusted], after that ye heard the word of truth, the gospel of your salvation: in whom also after that ye believed, ye were sealed with that holy Spirit of promise, Which is the earnest of our inheritance until the redemption of the purchased possession, unto the praise of his glory.",
        "context": "Paul on the believer's security. The Holy Spirit is a seal (sphragis) and earnest (arrabon) — a deposit guaranteeing the inheritance through any judgment.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "esphragisthete (G4972 aorist passive) — you were sealed. arrabon (G728) — earnest/down payment/guarantee. The Spirit as guarantee extends THROUGH any judgment period — the seal is not removed by evaluation."
    },
    {
        "reference": "1 John 5:13",
        "heading": "That you may KNOW you have eternal life -- oida settled certainty alongside judgment",
        "kjv_text": "These things have I written unto you that believe on the name of the Son of God; that ye may know that ye have eternal life, and that ye may believe on the name of the Son of God.",
        "context": "John's stated purpose for writing. Believers can KNOW (oida, settled certainty) they have eternal life.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "eidete (G1492 perfect active subjunctive) — 'that you may know' with settled certainty. The same author who writes about boldness in judgment day (4:17) also writes about settled assurance of eternal life. These coexist."
    },
    {
        "reference": "2 Tim 4:7-8",
        "heading": "Crown of righteousness from the righteous judge -- judgment as reward",
        "kjv_text": "I have fought a good fight, I have finished [my] course, I have kept the faith: Henceforth there is laid up for me a crown of righteousness, which the Lord, the righteous judge, shall give me at that day: and not to me only, but unto all them also that love his appearing.",
        "context": "Paul's final testimony. The 'righteous judge' (dikaios krites) awards a crown — judgment as REWARD, not threat.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "ho dikaios krites (G1342 + G2923) — the righteous judge. stephanos tes dikaiosynes — crown of righteousness. apodosei (G591 future) — will give/award. Judgment produces REWARD for the faithful. The judge's character (dikaios) guarantees fair outcome."
    },
    {
        "reference": "Jude 14-15",
        "heading": "The Lord CAME (elthen) with ten thousands -- parallel prophetic aorist",
        "kjv_text": "And Enoch also, the seventh from Adam, prophesied of these, saying, Behold, the Lord cometh with ten thousands of his saints, To execute judgment upon all, and to convince all that are ungodly among them of all their ungodly deeds which they have ungodly committed, and of all their hard [speeches] which ungodly sinners have spoken against him.",
        "context": "Jude quotes Enochic tradition. The Lord 'came' (elthen, same prophetic aorist as Rev 14:7) with myriads to execute judgment.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "elthen kyrios (G2064 V-2AAI-3S) — same prophetic aorist form as Rev 14:7 elthen. poiesai krisin (G2920) — to execute judgment. Enochic tradition uses the same grammatical device: future judgment narrated as past."
    },
    {
        "reference": "Rev 11:15",
        "heading": "Kingdoms became our Lord's (egeneto) -- prophetic aorist parallel",
        "kjv_text": "And the seventh angel sounded; and there were great voices in heaven, saying, The kingdoms of this world are become [the kingdoms] of our Lord, and of his Christ; and he shall reign for ever and ever.",
        "context": "Seventh trumpet. The kingdom transfer announced as accomplished fact — egeneto (became/has become), prophetic aorist.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "egeneto (G1096 V-2ADI-3S) — aorist indicative 'became.' Same prophetic aorist pattern as elthen in Rev 14:7 and epesen in Rev 14:8. Kingdom transfer announced as fait accompli before the events of chs.12-20 unfold."
    },
]

# Add them
R["verses"].extend(missing_verses)
print(f"Added {len(missing_verses)} missing verses (total now: {len(R['verses'])})")

# ========== 4. FIX RAW PARSING KEYS (10 errors) ==========
# The validation expects abbreviated refs matching the verse entries.
# Current keys use full book names. We need to add entries with the expected keys.

RAW = os.path.join(BASE, "raw-data")

# Read all raw parsing files
def read_file(p):
    try:
        with open(p,'r',encoding='utf-8') as f: return f.read()
    except: return ''

greek1 = read_file(os.path.join(RAW, "greek-parsing-batch1.txt"))
greek2 = read_file(os.path.join(RAW, "greek-parsing-batch2.txt"))
greek3 = read_file(os.path.join(RAW, "greek-parsing-batch3.txt"))
hebrew1 = read_file(os.path.join(RAW, "hebrew-parsing-batch1.txt"))
hebrew_dan726 = read_file(os.path.join(RAW, "hebrew-parsing-dan7-26.txt"))

import re
def extract_sections(text):
    """Split parser output into sections by separator."""
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
for t in [greek1, greek2, greek3]:
    all_greek.update(extract_sections(t))

all_hebrew = {}
all_hebrew.update(extract_sections(hebrew1))
h = hebrew_dan726.strip()
if h:
    all_hebrew["Daniel 7:26"] = h

# Map full names to abbreviated refs expected by validator
greek_key_map = {
    "Rev 14:7": "Revelation 14:7",
    "Rom 8:1": "Romans 8:1",
    "Rom 5:16": "Romans 5:16",
    "Rom 5:18": "Romans 5:18",
    "Rom 2:16": "Romans 2:16",
    "Rev 14:8": "Revelation 14:8",
    "John 5:24": "John 5:24",
    "John 5:22": "John 5:22",
    "1 John 4:17": "1 John 4:17",
    "1 John 4:18": "1 John 4:18",
}

# For combined refs, concatenate the individual entries
greek_combined = {
    "Rom 8:33-34": ["Romans 8:33", "Romans 8:34"],
}

hebrew_key_map = {
    "Dan 7:22": "Daniel 7:22",
    "Dan 7:10": "Daniel 7:10",
    "Dan 7:26": "Daniel 7:26",
}

hebrew_combined = {
    "Zech 3:1-2": ["Zechariah 3:1", "Zechariah 3:2"],
}

# Rebuild raw_parsing with correct abbreviated keys
new_greek = {}
for abbr, full in greek_key_map.items():
    if full in all_greek:
        new_greek[abbr] = all_greek[full]
    else:
        print(f"  WARNING: Greek {full} not found in parsed data")

for abbr, fulls in greek_combined.items():
    parts = []
    for full in fulls:
        if full in all_greek:
            parts.append(all_greek[full])
        else:
            print(f"  WARNING: Greek {full} not found for combined key {abbr}")
    if parts:
        new_greek[abbr] = "\n\n".join(parts)

new_hebrew = {}
for abbr, full in hebrew_key_map.items():
    if full in all_hebrew:
        new_hebrew[abbr] = all_hebrew[full]
    else:
        print(f"  WARNING: Hebrew {full} not found in parsed data")

for abbr, fulls in hebrew_combined.items():
    parts = []
    for full in fulls:
        if full in all_hebrew:
            parts.append(all_hebrew[full])
        else:
            print(f"  WARNING: Hebrew {full} not found for combined key {abbr}")
    if parts:
        new_hebrew[abbr] = "\n\n".join(parts)

# Keep any existing entries that aren't being remapped, and add the new ones
R["raw_parsing"]["greek"] = new_greek
R["raw_parsing"]["hebrew"] = new_hebrew
print(f"Rebuilt raw_parsing: {len(new_greek)} Greek, {len(new_hebrew)} Hebrew entries")

# ========== 5. WRITE ==========
out = os.path.join(BASE, "research.json")
with open(out, 'w', encoding='utf-8') as f:
    json.dump(R, f, indent=2, ensure_ascii=False)

sz = os.path.getsize(out)
print(f"\nWritten: {sz} bytes ({sz/1024:.1f} KB)")
print(f"Topics: {len(R['topics'])}, Verses: {len(R['verses'])}, WordStudies: {len(R['word_studies'])}, Parallels: {len(R['parallels'])}")
print(f"Greek parsing keys: {list(R['raw_parsing']['greek'].keys())}")
print(f"Hebrew parsing keys: {list(R['raw_parsing']['hebrew'].keys())}")
