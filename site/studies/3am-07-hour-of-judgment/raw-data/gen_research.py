#!/usr/bin/env python3
"""Generate research.json by loading template + injecting raw parsing data."""
import json, os, re

BASE = "D:/bible/bible-studies/3am-07-hour-of-judgment"
RAW = os.path.join(BASE, "raw-data")

def read_file(p):
    try:
        with open(p,'r',encoding='utf-8') as f: return f.read()
    except: return ''

# Load KJV
kjv = {}
with open("D:/bible/tools/data/kjv.txt",'r',encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if '\t' in line:
            r,t = line.split('\t',1)
            kjv[r] = t

def k(ref): return kjv.get(ref,'')

def split_p(text):
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
                        result[line] = sec; break
    return result

ag = {}
for fn in ["greek-parsing-batch1.txt","greek-parsing-batch2.txt","greek-parsing-batch3.txt"]:
    ag.update(split_p(read_file(os.path.join(RAW,fn))))
ah = {}
ah.update(split_p(read_file(os.path.join(RAW,"hebrew-parsing-batch1.txt"))))
h = read_file(os.path.join(RAW,"hebrew-parsing-dan7-26.txt")).strip()
if h: ah["Daniel 7:26"] = h

WS = "D:/bible/bible-studies/word-studies"

# Build the full research dict
R = {
"question": "What does hoti elthen he hora tes kriseos autou (\"for the hour of his judgment is come\") mean? What is this judgment -- the cross, the second coming, the investigative/pre-advent judgment, or something else? Why does the aorist elthen present it as an accomplished fact? How does krisis (G2920) differ from katakrima (G2631)? Trace krisis through the LXX to Daniel 7's dina. How does Daniel 7:22 establish this judgment is FOR believers? How can judgment be \"good news\"? Does the pre-advent judgment undermine assurance? Address using Daniel 12:1, 1 John 4:17, Romans 8:1,33-34, John 5:24. How does Romans 2:16 prove judgment IS gospel content?",

"topics": [
{"name":"JUDGMENT","subtopic":"THE GENERAL","verse_refs":["Psa 9:7","Psa 50:3-6","Psa 96:13","Ecc 12:14","Dan 7:9-10","Mat 12:36-37","Mat 22:11-13","Jhn 5:22","Act 17:31","Rom 2:5-16","1Co 3:13","2Co 5:10","Heb 9:27","1Jn 4:17","Rev 11:18","Rev 20:11-15"],
"entry_text":"THE GENERAL 1CH 16:33; JOB 14:17; 21:30; PSA 9:7; 50:3-6; 96:13; ECC 3:17; 11:9; 12:14; DAN 7:9,10; MAT 12:36,37; 22:11-13; 25:1-46; JHN 5:22; ACT 17:31; ROM 2:5-16; 14:10-12; 1CO 3:13; 2CO 5:10; 2TI 4:1,8; HEB 9:27; 1PE 4:5,7; 1JN 4:17; Jude 1:14,15; REV 11:18; 20:11-15; 22:12"},
{"name":"JUDGMENT","subtopic":"ACCORDING TO OPPORTUNITY AND WORKS","verse_refs":["Mat 25:14-30","Rom 2:5-12","1Co 3:12-15","Rev 20:12-13"],
"entry_text":"ACCORDING TO OPPORTUNITY AND WORKS GEN 4:7; JOB 34:11; PSA 62:12; MAT 25:14-30; ROM 2:5-12; 1CO 3:8,12-15; JAS 2:12,13; REV 2:23; 20:12,13"},
{"name":"ASSURANCE","subtopic":"SAINTS PRIVILEGED TO HAVE","verse_refs":["1Jn 5:13","Rom 8:38-39","Rom 5:1","Php 1:6","2Ti 4:7-8"],
"entry_text":"SAINTS PRIVILEGED TO HAVE -- Eternal life 1JN 5:13. Unalienable love ROM 8:38,39. Peace ROM 5:1. Continuance PHP 1:6. Crown 2TI 4:7,8"},
{"name":"BOOK","subtopic":"OF LIFE","verse_refs":["Exo 32:32-33","Psa 69:28","Dan 12:1","Php 4:3","Rev 3:5","Rev 13:8","Rev 20:12,15"],
"entry_text":"OF LIFE EXO 32:32,33; PSA 69:28; DAN 12:1; PHP 4:3; REV 3:5; 13:8; 20:12,15; 21:27"},
{"name":"BOOK","subtopic":"OF REMEMBRANCE","verse_refs":["Psa 56:8","Psa 139:16","Mal 3:16"],
"entry_text":"OF REMEMBRANCE PSA 56:8; 139:16; MAL 3:16"},
{"name":"SATAN","subtopic":"ACCUSER","verse_refs":["Rev 12:10","Job 1:6-12","Zec 3:1-2"],
"entry_text":"The accuser REV 12:10. JOB 1:6-12; ZEC 3:1,2; REV 12:9-12"},
{"name":"GOSPEL","subtopic":"UNCLASSIFIED SCRIPTURES","verse_refs":["Rom 2:16","Rev 14:6-7","Luk 3:18","Act 17:30-31"],
"entry_text":"Gospel includes judgment: ROM 2:16; REV 14:6-7; LUK 3:18; ACT 17:30-31"},
{"name":"ATONEMENT","subtopic":"DAY OF","verse_refs":["Lev 16:1-34","Lev 23:27-32"],
"entry_text":"DAY OF LEV 16:1-34; 23:27-32; EXO 30:10"},
{"name":"JUDGMENT-SEAT","subtopic":"Of Christ","verse_refs":["Rom 14:10","2Co 5:10"],
"entry_text":"Of Christ ROM 14:10; 2CO 5:10"},
{"name":"MEDIATION","subtopic":"GENERAL","verse_refs":["1Ti 2:5","Heb 8:6","Heb 9:15"],
"entry_text":"GENERAL 1TI 2:5; HEB 8:6; 9:15; 12:24"}
],

"verses": [],
"word_studies": [],
"parallels": [],
"raw_parsing": {"greek":{},"hebrew":{}}
}

# --- VERSES ---
V = R["verses"]
def av(ref,hd,kj,ctx,notes):
    V.append({"reference":ref,"heading":hd,"kjv_text":kj,"context":ctx,"greek_parsing":[],"hebrew_parsing":[],"notes":notes})

av("Rev 14:6-7","The crux text: the hour of his judgment is come",
   k("Revelation 14:6")+" "+k("Revelation 14:7"),
   "First angel with everlasting gospel. Three imperatives + hoti clause declaring judgment arrival.",
   "krisis G2920 genitive singular. elthen V-2AAI-3S prophetic aorist. hoti G3754 causal. Three aorist imperatives.")
av("Rom 8:1","No katakrima -- condemnation negated, not judgment",k("Romans 8:1"),
   "Romans 8 after ch.7 struggle. katakrima G2631 NOT krisis G2920.",
   "katakrima G2631 Nom Sg N. ouden categorical negation. Only 3 NT uses all in Romans.")
av("Rom 5:16","Katakrima #1: from one sin to condemnation",k("Romans 5:16"),
   "Adam-Christ typology. krima from one to katakrima vs charisma to dikaioma.",
   "krima G2917 -> katakrima G2631 vs charisma -> dikaioma. Text distinguishes process from adverse outcome.")
av("Rom 5:18","Katakrima #2: one trespass, condemnation for all",k("Romans 5:18"),
   "Parallel: one paraptoma -> katakrima vs one dikaioma -> dikaiosis zoes.",
   "katakrima Acc Sg N. Parallel with dikaiosis G1347. Opposite judicial outcomes.")
av("John 5:22","All judgment (krisin) committed to the Son",k("John 5:22"),
   "Father-Son discourse. ALL krisin given to Son. dedoken perfect tense.",
   "krisin G2920 Acc Sg F. dedoken V-RAI-3S perfect. pasan=ALL judgment permanently delegated.")
av("John 5:24","Does not come into krisin -- condemnatory outcome",k("John 5:24"),
   "After v.22. Hearing+believing=no krisis+passed from death to life.",
   "krisin G2920 same word as v.22. metabebeken V-RAI-3S perfect permanent transition. krisin=condemnatory OUTCOME since crossed from death to life.")
av("John 5:27-29","Authority as Son of Man -- Dan 7:13 allusion",
   k("John 5:27")+" "+k("John 5:28")+" "+k("John 5:29"),
   "Authority grounded in Son of Man identity. Dan 7:13-14 allusion. Resurrection judgment.",
   "v.27 krisin anarthrous qualitative. Son of Man links Dan 7:13. v.29 resurrection of krisis vs life.")
av("1 John 4:17","Boldness (parrhesia) IN the day of krisis",k("1 John 4:17"),
   "Love perfected produces parrhesia in the day of krisis. Same word as Rev 14:7.",
   "parrhesian G3954 Acc Sg F. en te hemera tes kriseos locative dative. Confidence WITHIN judgment.")
av("1 John 4:18","Perfect love casts out fear -- kolasis fear",k("1 John 4:18"),
   "Fear cast out is kolasis-fear (punishment dread) not reverential awe.",
   "phobos G5401. kolasin G2851 punishment. Only 2 NT uses. NOT phobeo of Rev 14:7.")
av("Dan 7:9-10","OT source: heavenly court seated, books opened",
   k("Daniel 7:9")+" "+k("Daniel 7:10"),
   "Night vision. Thrones, Ancient of Days, fiery stream, multitude. Court opens.",
   "Aramaic: dina yetib A1780+A3488=court sat. siphrin pethichu=books opened. LXX: kriterion ekathisen G2922.")
av("Dan 7:13-14","Son of Man to Ancient of Days -- dominion AFTER judgment",
   k("Daniel 7:13")+" "+k("Daniel 7:14"),
   "After court scene. Son of Man TO Ancient of Days. Kingdom transfer after judgment.",
   "Direction TO God. OG LXX uses latreuo. Kingdom follows judgment=pre-advent concept.")
av("Dan 7:22","Judgment given TO/FOR the saints -- vindication",k("Daniel 7:22"),
   "Horn wars saints UNTIL Ancient of Days comes, judgment given TO saints, saints possess kingdom.",
   "Aramaic: dina yehib leqaddishe elyonin. le=benefactive. LXX: to krima edoken G2917. Three-phase: v.10 investigation, v.22 verdict, vv.26-27 execution.")
av("Dan 7:26-27","Third judgment: dominion transferred to saints",
   k("Daniel 7:26")+" "+k("Daniel 7:27"),
   "Court sits, horn dominion removed, kingdom given to saints permanently.",
   "dina yittib A1780+A3488 impf=court shall sit. LXX: to kriterion kathisei G2922.")
av("Rom 2:16","Judgment IS gospel -- kata to euangelion mou",k("Romans 2:16"),
   "God judges secrets through Christ according to my gospel.",
   "krinei G2919 V-PAI-3S present. kata G2596+euangelion G2098. Barnes/Meyer confirm kata modifies krinei.")
av("Acts 17:30-31","Repentance commanded BECAUSE judgment appointed",
   k("Acts 17:30")+" "+k("Acts 17:31"),
   "Mars Hill. Creator+command+judgment parallels Rev 14:7.",
   "estesen hemeran=appointed day. mellei krinein=about to judge. Bridges anticipation(mellei)/announcement(elthen).")
av("Luke 3:18","Judgment warnings AS gospel -- euengelizeto",k("Luke 3:18"),
   "Luke uses euengelizeto G2097 for judgment-inclusive preaching.",
   "euengelizeto V-INI-3S imperfect. Judgment warnings=gospel proclamation.")
av("Rom 8:33-34","Courtroom vindication: who charges? who condemns?",
   k("Romans 8:33")+" "+k("Romans 8:34"),
   "Triumphant courtroom rhetoric. Forensic: egkalesei, katakrinon, entygchanei.",
   "egkalesei G1458 V-FAI-3S. katakrinon G2632. entygchanei G1793 V-PAI-3S present=ongoing intercession NOW.")
av("Dan 12:1","Everyone FOUND WRITTEN delivered -- judgment as deliverance",k("Daniel 12:1"),
   "Michael stands for people. Deliverance for those found written in the book.",
   "Names already IN book. Judgment FINDS and confirms. Verification not determination.")
av("1 Cor 3:13-15","Fire tests works, person saved -- evaluative with safety net",
   k("1 Corinthians 3:13")+" "+k("1 Corinthians 3:14")+" "+k("1 Corinthians 3:15"),
   "Building metaphor. Fire tests erga. Even total work failure: person saved.",
   "Fire tests erga G2041=same as Rev 20:12. Person saved sothesetai divine passive. Evaluative not condemnatory.")
av("Gen 18:20-21","God investigates Sodom BEFORE judging",
   k("Genesis 18:20")+" "+k("Genesis 18:21"),
   "God uses investigation language despite omniscience. Transparent justice pattern.",
   "Investigation for transparent justice. Pattern: cry->investigation->execution.")
av("Matt 22:11-14","Wedding garment inspection -- pre-event examination",
   k("Matthew 22:11")+" "+k("Matthew 22:12")+" "+k("Matthew 22:13")+" "+k("Matthew 22:14"),
   "King inspects guests BEFORE feast. Three phases: invitation, inspection, removal.",
   "eiselthon to theasasthai=came in to examine. Three-phase mirrors Dan 7.")
av("Eccl 12:14","God brings every work into judgment",k("Ecclesiastes 12:14"),
   "After fear God (v.13). God brings EVERY work into mishpat.",
   "mishpat H4941. Parallels Rev 14:7: fear God+judgment. Every secret=Rom 2:16 ta krupta.")
av("Rev 14:8","Prophetic aorist parallel -- epesen epesen",k("Revelation 14:8"),
   "Second angel. Same prophetic aorist. Doubled echoing Isa 21:9.",
   "Epesen G4098 V-2AAI-3S doubled. Same grammar as elthen.")
av("Zech 3:1-5","Courtroom vindication -- Joshua accused, defended, restored",
   k("Zechariah 3:1")+" "+k("Zechariah 3:2")+" "+k("Zechariah 3:3")+" "+k("Zechariah 3:4")+" "+k("Zechariah 3:5"),
   "Heavenly court. Joshua filthy garments, Satan accuses, God rebukes, garments replaced.",
   "ha-satan H7854 formal accuser. Pattern: guilt->accusation->advocacy->cleansing->new status.")
av("Rev 20:11-15","Great white throne -- books + book of life",
   k("Revelation 20:11")+" "+k("Revelation 20:12")+" "+k("Revelation 20:13")+" "+k("Revelation 20:14")+" "+k("Revelation 20:15"),
   "Post-millennial. biblia (deeds) and biblos tes zoes. Judged kata ta erga.",
   "biblia G975 books of deeds. kata ta erga auton G2041. Two standards: works AND book of life.")
av("Mal 3:16-17","Book of remembrance preserves the faithful",
   k("Malachi 3:16")+" "+k("Malachi 3:17"),
   "Book of remembrance written FOR those who feared the LORD. segullah=special treasure.",
   "sepher zikkaron H5612+H2146 benefactive. Records faithful service not sins.")
av("Psa 50:3-6","God calls witnesses to judge His people",
   k("Psalm 50:3")+" "+k("Psalm 50:4")+" "+k("Psalm 50:5")+" "+k("Psalm 50:6"),
   "Theophany of judgment. God gathers covenant saints. Heavens declare righteousness.",
   "Judgment OF covenant community. Precedent for 1 Pet 4:17.")
av("Psa 96:13","He comes to judge with righteousness -- positive event",k("Psalm 96:13"),
   "Creation rejoices BECAUSE He comes to judge.",
   "shaphat H8199. Judgment=reason for rejoicing when judge righteous.")
av("Psa 9:7-8","LORD throne prepared for judgment -- righteous order",
   k("Psalm 9:7")+" "+k("Psalm 9:8"),
   "LORD endures forever, throne prepared for mishpat. Judges in righteousness.",
   "mishpat H4941. meysharim=uprightness. Permanent righteous order.")
av("1 Pet 4:17","Judgment begins at house of God",k("1 Peter 4:17"),
   "krima G2917 begins at God house. Believers first. Pre-advent concept.",
   "arx-=temporal priority. Believers evaluated FIRST.")
av("Rev 11:18-19","Judgment of dead + ark revealed -- DOA activation",
   k("Revelation 11:18")+" "+k("Revelation 11:19"),
   "Seventh trumpet. Dead judged, servants rewarded. Temple opened, ark seen.",
   "kibotos tes diathekes=ark of covenant DOA furniture. Three angels follow.")
av("2 Cor 5:10","Bema of Christ -- ALL must appear",k("2 Corinthians 5:10"),
   "ALL appear before bema for evaluation of deeds.",
   "bema G968. pantas G3956 ALL including believers.")
av("Dan 8:14","Sanctuary vindicated -- timing question",k("Daniel 8:14"),
   "2300 days. Sanctuary nitsdaq. Concept from Dan 7 independent of timing.",
   "nitsdaq niphal of tsadaq=vindicated. Pre-advent CONCEPT from Dan 7 sequence.")
av("Jas 2:12-13","Law of liberty -- mercy triumphs",
   k("James 2:12")+" "+k("James 2:13"),
   "Judged by law of liberty. Mercy triumphs over judgment.",
   "nomos eleutheiras. katakauchastai G2620 mercy triumphs.")
av("Rev 12:10","Accuser cast down",k("Revelation 12:10"),
   "Accuser (kategor) of brethren cast down. Overcome by blood of Lamb.",
   "kategor G2725 prosecutor disbarred. ebletke aorist passive.")
av("Gen 3:8-13","God questions before judgment -- investigation pattern",
   k("Genesis 3:8")+" "+k("Genesis 3:9")+" "+k("Genesis 3:10")+" "+k("Genesis 3:11")+" "+k("Genesis 3:12")+" "+k("Genesis 3:13"),
   "After fall. God calls, asks, investigates BEFORE pronouncing judgment.",
   "Questions for transparent process. Pattern: presence->inquiry->response->verdict.")
av("Rev 15:3-4","Just and true are thy ways -- vindication progression",
   k("Revelation 15:3")+" "+k("Revelation 15:4"),
   "Song of Moses/Lamb. Character affirmation. Fear+glorify echo 14:7.",
   "14:7 announcement->15:3-4 character->16:7 acts->19:1-2 completion.")
av("Rev 16:7","True and righteous are thy judgments",k("Revelation 16:7"),
   "During plagues. Altar affirms specific judgment acts.",
   "kriseis G2920 plural. Altar=martyrs (6:9-11) vindicated.")
av("Rev 19:1-2","Vindication complete -- he hath judged",
   k("Revelation 19:1")+" "+k("Revelation 19:2"),
   "After Babylon fall. Final vindication formula.",
   "ekrinen G2919 aorist completed. Full progression announcement to completion.")

# --- WORD STUDIES ---
W = R["word_studies"]
def aw(s,w,sf,oc,su,cats,kvs,rel):
    W.append({"strongs":s,"word":w,"source_file":sf,"occurrence_count":oc,"summary":su,"semantic_categories":cats,"key_verses":kvs,"relevance":rel})

aw("G2920","krisis",f"{WS}/G2920-krisis.md",47,"Judgment/evaluation PROCESS. 47 NT occ. From krino. Judicial process -- separating, trial, evaluation.",["day of judgment","judicial process","divine judicial act"],["Rev 14:7","John 5:22","John 5:24","1 John 4:17","Heb 9:27"],"THE word in Rev 14:7. Angel announces judgment PROCESS not condemnation.")
aw("G2631","katakrima",f"{WS}/G2631-katakrima.md",3,"Adverse verdict+execution. Only 3 NT occ (Rom 5:16,5:18,8:1). Uniformly condemnation.",["adverse verdict","condemnation from Adam","negated for believers"],["Rom 8:1","Rom 5:16","Rom 5:18"],"CONTRASTING word. Rom 8:1 no katakrima not no krisis. Exempt from condemnation not evaluation.")
aw("G2917","krima",f"{WS}/G2917-krima.md",27,"Judgment/decision RESULT. 27 NT occ. LXX for mishpat 175x. Dan 7:22 LXX term.",["divine verdict","judicial decision","lawsuit"],["Dan 7:22 LXX","1 Pet 4:17","Rev 20:4"],"LXX term in Dan 7:22 to krima edoken. Bridges PROCESS and OUTCOME.")
aw("G2919","krino",f"{WS}/G2919-krino.md",98,"Root verb to judge/separate/decide. 98 NT verses.",["judicial verdict","mental evaluation","divine judgment"],["Rom 2:16","John 5:22","Acts 17:31","Rev 19:11"],"ROOT VERB. Rom 2:16 God judges according to gospel.")
aw("G2922","kriterion",f"{WS}/G2922-kriterion.md",3,"Tribunal/court. 3 NT occ. LXX Dan 7:10,26.",["court of justice","tribunal"],["1 Cor 6:2","Dan 7:10 LXX","Dan 7:26 LXX"],"LXX for COURT in Dan 7:10 kriterion ekathisen and 7:26.")
aw("G2923","krites",f"{WS}/G2923-krites.md",17,"Judge -- the person. 17 NT occ.",["God/Christ as Judge","civil judge"],["Acts 10:42","2 Tim 4:8","Jas 4:12"],"Completes krin- family: judge, krisis, krima, kriterion.")
aw("G2632","katakrino",f"{WS}/G2632-katakrino.md",19,"To condemn. 19 NT verses. Always adverse.",["adverse judgment","condemnation"],["Rom 8:34","John 3:17"],"Rom 8:34 who condemns? Christ intercedes.")
aw("G2633","katakrisis",f"{WS}/G2633-katakrisis.md",2,"Act of condemning. Only 2 NT occ.",["condemnation act"],["2 Cor 3:9"],"Completes kata-krin- family.")
aw("G350","anakrino",f"{WS}/G350-anakrino.md",14,"Examine/investigate/scrutinize. 14 NT verses. INVESTIGATIVE member.",["judicial investigation","spiritual discernment"],["Luke 23:14","1 Cor 2:15","1 Cor 4:3"],"INVESTIGATIVE verb. Investigation built into krin- word group.")
aw("G4793","synkrino",f"{WS}/G4793-synkrino.md",2,"Compare/judge together. 2 NT verses.",["comparison"],["1 Cor 2:13"],"Completes krin- family mapping.")
aw("A1780","diyn (Aramaic)",f"{WS}/A1780-diyn.md",5,"Aramaic judgment/court. 5 OT occ. Dan 7 SOURCE WORD.",["heavenly court","judicial verdict","divine justice"],["Dan 7:10","Dan 7:22","Dan 7:26"],"SOURCE feeding entire krisis chain.")
aw("H1779","diyn (Hebrew noun)",f"{WS}/H1779-diyn.md",17,"Hebrew judgment/cause/plea. 17 verses.",["legal case","championing poor"],["Psa 9:4","Psa 140:12"],"Hebrew cognate of Aramaic A1780.")
aw("H1777","diyn (Hebrew verb)",f"{WS}/H1777-diyn.md",24,"To judge/rule/plead. 24 verses.",["divine judging","pleading cause"],["Gen 49:16","Psa 7:8"],"Verbal root behind A1780 and H1779.")
aw("H4941","mishpat",f"{WS}/H4941-mishpat.md",406,"Most common OT judgment term. 406 verses. LXX krima 175x + krisis 132x.",["divine verdict","justice","ordinance"],["Eccl 12:14","Mic 6:8","Psa 89:14"],"Primary OT bridge to NT krisis. Eccl 12:14 parallels Rev 14:7.")
aw("H8199","shaphat",f"{WS}/H8199-shaphat.md",182,"To judge/vindicate/govern. 182 verses. LXX krino 105x.",["divine judgment","vindication"],["Gen 18:25","Psa 96:13"],"OT verb bridge to NT krino.")
aw("H7378","riyb (verb)",f"{WS}/H7378-riyb.md",59,"Covenant lawsuit verb. 59 verses. LXX krisis 29x.",["covenant lawsuit","legal advocacy"],["Mic 6:1-2","Isa 1:18"],"riyb->krisis LXX bridge. Rev 14:7 carries covenant lawsuit weight.")
aw("H7379","riyb (noun)",f"{WS}/H7379-riyb.md",59,"Lawsuit/cause/controversy. 59 verses. LXX krisis 29x PMI 20.28.",["formal lawsuit","divine controversy"],["Mic 6:2","Psa 43:1"],"Noun form. LXX renders as krisis 29x.")
aw("G5610","hora",f"{WS}/G5610-hora.md",108,"Hour/appointed time. 108 occ. With article=THE appointed hour.",["appointed time","decisive moment"],["Rev 14:7","John 12:23","John 13:1","John 17:1"],"Rev 14:7 he hora. Parallels Jesus' hora language.")
aw("G2064","erchomai",f"{WS}/G2064-erchomai.md",604,"To come/arrive. 604 NT verses. elthen=aorist.",["physical arrival","eschatological coming"],["Rev 14:7","Jude 1:14","John 5:24"],"elthen V-2AAI-3S prophetic aorist. Compare Jude 14.")
aw("G3954","parrhesia",f"{WS}/G3954-parrhesia.md",31,"Boldness/confidence. 31 occ. pas+rhesis.",["confident access","bold speech","assurance"],["1 John 4:17","1 John 2:28","Eph 3:12"],"1 John 4:17 parrhesia IN day of krisis. Answer to assurance question.")
aw("G2851","kolasis",f"{WS}/G2851-kolasis.md",2,"Punishment/torment. Only 2 NT occ.",["eschatological punishment","fear of punishment"],["Matt 25:46","1 John 4:18"],"1 John 4:18 kolasis fear cast out, NOT reverential awe.")
aw("G5401","phobos",f"{WS}/G5401-phobos.md",44,"Fear -- alarm or reverence. 44 NT verses.",["visceral terror","reverential awe"],["1 John 4:18","Rom 8:15"],"1 John 4:18 phobos (dread) vs Rev 14:7 phobeo (reverence).")
aw("G5399","phobeo",f"{WS}/G5399-phobeo.md",90,"To fear/revere. 90 NT verses.",["divine command","fear of God"],["Rev 14:7","Matt 10:28"],"Rev 14:7 Phobethete decisive reverential command.")
aw("G3875","parakletos",f"{WS}/G3875-parakletos.md",5,"Advocate/helper. 5 NT occ Johannine.",["Christ Advocate","Spirit Helper"],["1 John 2:1","John 14:16"],"1 John 2:1 Christ as defense attorney in judgment.")
aw("G1793","entynchano",f"{WS}/G1793-entynchano.md",5,"To intercede. 5 NT verses.",["Christ intercession","Spirit intercession"],["Rom 8:34","Heb 7:25"],"Rom 8:34 present tense ONGOING intercession during judgment.")
aw("G5241","huperentugchano",f"{WS}/G5241-huperentugchano.md",1,"Intensified intercession. HAPAX Rom 8:26.",["Spirit intercession"],["Rom 8:26"],"Triple intercession Rom 8: Spirit v.26, Spirit v.27, Christ v.34.")
aw("G3316","mesites",f"{WS}/G3316-mesites.md",6,"Mediator. 6 NT occ. Christ new covenant mediator.",["covenant mediator"],["1 Tim 2:5","Heb 8:6","Heb 9:15"],"Christ stands between God and humanity during judgment.")
aw("G1341","dikaiokrisia",f"{WS}/G1341-dikaiokrisia.md",1,"Righteous judgment. HAPAX Rom 2:5.",["righteous divine judgment"],["Rom 2:5"],"Embeds righteousness into judgment concept.")
aw("G1349","dike",f"{WS}/G1349-dike.md",4,"Justice/right/penalty. 4 NT occ.",["personified justice","divine retribution"],["Acts 28:4","2 Thess 1:9"],"Root of dik- family.")
aw("G2098","euangelion",f"{WS}/G2098-euangelion.md",74,"Good news/gospel. 74 NT verses.",["gospel of Christ","gospel of kingdom"],["Rev 14:6","Rom 2:16","Rom 1:16"],"Rev 14:6 euangelion aionion. Rom 2:16 kata to euangelion mou.")
aw("G2097","euangelizo",f"{WS}/G2097-euangelizo.md",52,"To announce good news. 52 NT verses.",["gospel proclamation"],["Luke 3:18","Rev 14:6"],"Luke 3:18 euengelizeto with judgment content.")
aw("G975","biblion",f"{WS}/G975-biblion.md",28,"Book/scroll. 28 NT verses.",["heavenly record","book of life"],["Rev 20:12","Rev 5:1"],"Rev 20:12 biblia of deeds. Books contain erga broadly.")
aw("H5612","cepher",f"{WS}/H5612-cepher.md",174,"Book/writing. 174 OT verses.",["sacred text","divine record"],["Dan 12:1","Mal 3:16"],"Dan 12:1 found written. Mal 3:16 sepher zikkaron.")
aw("G1391","doxa",f"{WS}/G1391-doxa.md",151,"Glory. 151 NT verses.",["divine radiance","honor"],["Rev 14:7","John 17:1"],"Rev 14:7 give glory. Glory-judgment connection.")
aw("G2041","ergon",f"{WS}/G2041-ergon.md",161,"Work/deed. 161 NT verses.",["deeds judged","works of faith"],["Rev 20:12-13","Matt 5:16"],"Rev 20:12-13 judged according to erga. Includes faithful service.")
aw("G1492","oida",f"{WS}/G1492-oida.md",297,"Know with settled certainty. 297 NT verses.",["settled knowledge"],["1 John 5:13","Rom 8:28"],"1 John 5:13 oida coexists with judgment awareness.")
aw("G2250","hemera",f"{WS}/G2250-hemera.md",365,"Day. 365 NT verses.",["eschatological day","day of judgment"],["1 John 4:17","Rom 2:16"],"1 John 4:17 en te hemera tes kriseos. Rev 14:7 uses hora not hemera.")
aw("G2435","hilasterion",f"{WS}/G2435-hilasterion.md",2,"Mercy seat/propitiation. 2 NT occ.",["DOA furniture","propitiatory sacrifice"],["Rom 3:25","Heb 9:5"],"Connects DOA typology to judgment.")
aw("G1458","enkaleo","",None,"Bring charges/accuse. Formal legal prosecution.",["formal accusation"],["Rom 8:33","Acts 19:38"],"Rom 8:33 who shall charge? God justifies.")
aw("G2725","kategoros",f"{WS}/G2725-kategoros.md",7,"Accuser/prosecutor. 7 NT occ.",["Roman accusers","Satan cosmic accuser"],["Rev 12:10","Acts 23:30"],"Rev 12:10 Satan as prosecutor cast down.")
aw("H7854","satan",f"{WS}/H7854-satan.md",28,"Adversary/accuser. 28 OT occ.",["human adversary","divine council accuser"],["Zech 3:1-2","Job 1:6-12"],"Zech 3:1 ha-satan in courtroom.")
aw("A3488","ythib",f"{WS}/A3488-ythib.md",5,"Aramaic to sit. 5 OT occ.",["divine court session"],["Dan 7:9","Dan 7:10","Dan 7:26"],"dina yetib=court took seat.")
aw("G1342","dikaios",f"{WS}/G1342-dikaios.md",76,"Righteous/just. 76 NT verses.",["divine righteousness","legal standing"],["2 Tim 4:8","1 John 2:1","Rev 15:3"],"2 Tim 4:8 righteous judge.")
aw("G1343","dikaiosyne",f"{WS}/G1343-dikaiosyne.md",85,"Righteousness. 85 NT verses.",["divine attribute","imputed righteousness"],["Rom 3:21-26","Phil 3:9"],"Gods dikaiosyne guarantees fair krisis.")
aw("G1344","dikaioo",f"{WS}/G1344-dikaioo.md",36,"To justify/acquit. 36 NT verses.",["forensic acquittal","divine declaration"],["Rom 8:33","Rom 3:24","Gal 2:16"],"Rom 8:33 God who justifies. Present=ongoing.")
aw("G1347","dikaiosis",f"{WS}/G1347-dikaiosis.md",2,"Justification. Only 2 NT occ.",["acquittal"],["Rom 4:25","Rom 5:18"],"Rom 5:18 katakrima vs dikaiosis. Opposite outcomes.")

# --- PARALLELS ---
R["parallels"] = [
{"source_verse":"Rev 14:7","parallel_verse":"Eccl 12:13-14","direction":"ot","connection_type":"vocabulary+structural: fear God+judgment of all works"},
{"source_verse":"Rev 14:7","parallel_verse":"Psa 96:13","direction":"ot","connection_type":"vocabulary: coming to judge, judgment positive"},
{"source_verse":"Rev 14:7","parallel_verse":"Gen 28:17","direction":"ot","connection_type":"semantic: fear+heaven (hybrid 0.416)"},
{"source_verse":"Rev 14:7","parallel_verse":"Rev 19:1","direction":"nt","connection_type":"vocabulary+structural: glory,heaven,voice (hybrid 0.443)"},
{"source_verse":"Rev 14:7","parallel_verse":"Rev 12:10","direction":"nt","connection_type":"vocabulary: heaven,voice,accuser (hybrid 0.425)"},
{"source_verse":"Rev 14:7","parallel_verse":"Rev 15:4","direction":"nt","connection_type":"vocabulary: fear,worship,judgments (hybrid 0.404)"},
{"source_verse":"Rev 14:7","parallel_verse":"Rev 18:10","direction":"nt","connection_type":"vocabulary: fear,hour,judgment (hybrid 0.395)"},
{"source_verse":"Dan 7:22","parallel_verse":"Dan 7:18","direction":"ot","connection_type":"structural: saints possess kingdom (hybrid 0.547)"},
{"source_verse":"Dan 7:22","parallel_verse":"Dan 7:27","direction":"ot","connection_type":"structural: kingdom given to saints (hybrid 0.455)"},
{"source_verse":"Dan 7:22","parallel_verse":"1 Cor 4:5","direction":"nt","connection_type":"semantic: time/judgment (hybrid 0.424)"},
{"source_verse":"Rom 2:16","parallel_verse":"Rom 16:25","direction":"nt","connection_type":"vocabulary: Christ,gospel,Jesus,secret (hybrid 0.455)"},
{"source_verse":"Rom 2:16","parallel_verse":"2 Tim 4:1","direction":"nt","connection_type":"vocabulary: Christ,Jesus,judge (hybrid 0.432)"},
{"source_verse":"Zech 3:1-2","parallel_verse":"Rev 12:10","direction":"nt","connection_type":"structural: accuser in divine court rebuked/cast down"},
{"source_verse":"Zech 3:1-2","parallel_verse":"Rom 8:33-34","direction":"nt","connection_type":"structural: accusation answered by divine advocacy"},
{"source_verse":"Gen 18:20-21","parallel_verse":"Dan 7:9-10","direction":"ot","connection_type":"structural: divine investigation before execution"},
{"source_verse":"Gen 18:20-21","parallel_verse":"Matt 22:11-14","direction":"nt","connection_type":"structural: inspection before execution"},
{"source_verse":"1 John 4:17","parallel_verse":"Rev 14:7","direction":"nt","connection_type":"vocabulary: same krisis; boldness IN judgment day"},
{"source_verse":"Mal 3:16-17","parallel_verse":"Dan 12:1","direction":"ot","connection_type":"structural: book preserves/delivers faithful"},
{"source_verse":"Mal 3:16-17","parallel_verse":"Rev 20:12","direction":"nt","connection_type":"vocabulary+structural: books in judgment, faithful preserved"}
]

# --- RAW PARSING ---
R["raw_parsing"]["greek"] = {ref: text for ref, text in ag.items()}
R["raw_parsing"]["hebrew"] = {ref: text for ref, text in ah.items()}

# Write
out = os.path.join(BASE, "research.json")
with open(out, 'w', encoding='utf-8') as f:
    json.dump(R, f, indent=2, ensure_ascii=False)

sz = os.path.getsize(out)
print(f"Written: {sz} bytes ({sz/1024:.1f} KB)")
print(f"Topics: {len(R['topics'])}, Verses: {len(R['verses'])}, WordStudies: {len(R['word_studies'])}, Parallels: {len(R['parallels'])}")
print(f"Greek: {len(R['raw_parsing']['greek'])}, Hebrew: {len(R['raw_parsing']['hebrew'])}")
