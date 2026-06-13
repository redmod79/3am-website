import json

with open('D:/bible/bible-studies/3am-06-give-glory/research.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Fix 1: PMI value for H3034 (word_studies[5])
for ws in data['word_studies']:
    if ws['strongs'] == 'H3034':
        ws['summary'] = ws['summary'].replace('PMI 33.14', 'PMI 7.58')
        break

# Fix 2: Add 35 missing verse entries
new_verses = [
    {
        "reference": "John 15:8",
        "heading": "Fruit-Bearing IS Glorification",
        "kjv_text": "Herein is my Father glorified, that ye bear much fruit; so shall ye be my disciples.",
        "context": "John 15:1-8 — the vine and branches discourse. V.8 is the glorification climax: the Father is glorified (edoxasthe, aorist passive) when believers bear much fruit.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "edoxasthe (V-API-3S of doxazo G1392) — divine passive. Fruit-bearing glorifies the Father. Listed in Nave's GLORIFYING GOD under Accomplished by: Bringing forth fruits of righteousness."
    },
    {
        "reference": "1 Chr 16:28-29",
        "heading": "Give Unto the LORD Glory: The Commanded Pattern",
        "kjv_text": "Give unto the LORD, ye kindreds of the people, give unto the LORD glory and strength. Give unto the LORD the glory [due] unto his name: bring an offering, and come before him: worship the LORD in the beauty of holiness.",
        "context": "1 Chronicles 16:8-36 — David's psalm of thanksgiving when the ark was brought to Zion. A call to all peoples to give (habuw) glory (kabod) to YHWH — the same vocabulary as Rev 14:7.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "habuw la-YHWH kabod — 'give unto the LORD glory.' Listed in Nave's GLORIFYING GOD as Commanded. The construction habuw + kabod + la-YHWH is the OT equivalent of dote + doxan + auto in Rev 14:7."
    },
    {
        "reference": "Psa 22:23",
        "heading": "Command to Glorify: Fear and Glorify Together",
        "kjv_text": "Ye that fear the LORD, praise him; all ye the seed of Jacob, glorify him; and fear him, all ye the seed of Israel.",
        "context": "Psalm 22:22-26 — the psalmist's vow of praise after deliverance. The fear-glorify pairing anticipates the Rev 14:7 triad.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "kabbeduhu (Piel imperative of kabad H3513) — 'glorify him.' Listed in Nave's GLORIFYING GOD as Commanded. Pairs fear (yare) with glorify (kabad) — the same two concepts as Rev 14:7."
    },
    {
        "reference": "Psa 50:23",
        "heading": "Praise as Glorification Mechanism",
        "kjv_text": "Whoso offereth praise glorifieth me: and to him that ordereth [his] conversation [aright] will I shew the salvation of God.",
        "context": "Psalm 50 — a judgment scene (vv.3-6) followed by God's indictment. V.23 defines the mechanism: offering praise (todah, from yadah) = glorifying God (kabad).",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "todah... yekabbedaniy — 'praise... glorifies me.' todah (from yadah H3034) and kabad (H3513) are equated. Listed in Nave's GLORIFYING GOD under Accomplished by: Praising him."
    },
    {
        "reference": "Psa 86:9",
        "heading": "Universal Glorification: All Nations Shall Glorify",
        "kjv_text": "All nations whom thou hast made shall come and worship before thee, O Lord; and shall glorify thy name.",
        "context": "Psalm 86:8-10 — a prayer acknowledging God's uniqueness among the gods. V.9 envisions universal glorification — all nations worshipping and glorifying.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "vikabbedu lishmeka — 'and shall glorify thy name.' Listed in Nave's GLORIFYING GOD: Shall be universal. Parallels Rev 14:6-7's universal scope ('every nation, kindred, tongue, people')."
    },
    {
        "reference": "Psa 86:12",
        "heading": "Personal Resolve to Glorify Forever",
        "kjv_text": "I will praise thee, O Lord my God, with all my heart: and I will glorify thy name for evermore.",
        "context": "Psalm 86:11-13 — a personal vow of praise and glorification. The psalmist resolves to glorify God's name perpetually.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "vaakabbedah shimka le-olam — 'I will glorify thy name forever.' Listed in Nave's GLORIFYING GOD: Saints should persevere in."
    },
    {
        "reference": "Psa 115:1",
        "heading": "Not Unto Us: Glory Belongs to God's Name",
        "kjv_text": "Not unto us, O LORD, not unto us, but unto thy name give glory, for thy mercy, [and] for thy truth's sake.",
        "context": "Psalm 115 — a psalm of trust. V.1 redirects all glory from human recipients to God's name, grounded in His mercy and truth (chesed and emeth, the same attributes as Exod 34:6).",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "ten kabod — 'give glory.' Same nathan + kabod construction as Josh 7:19 and Mal 2:2. Listed in Nave's GLORIFYING GOD for mercy and truth."
    },
    {
        "reference": "Isa 25:3",
        "heading": "Glorifying God for Judgments",
        "kjv_text": "Therefore shall the strong people glorify thee, the city of the terrible nations shall fear thee.",
        "context": "Isaiah 25:1-5 — a song of praise for God's judgments. V.3: even strong/terrible nations glorify God when they witness His judgments.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "yekabbeducha — 'shall glorify thee' (Piel imperfect of kabad H3513). Listed in Nave's GLORIFYING GOD for judgments. Connects glorification directly to the judgment motif — paralleling Rev 14:7 where glory-giving and judgment are paired."
    },
    {
        "reference": "Isa 60:1-2",
        "heading": "Rise and Shine: Glory of the LORD Risen Upon Thee",
        "kjv_text": "Arise, shine; for thy light is come, and the glory of the LORD is risen upon thee. For, behold, the darkness shall cover the earth, and gross darkness the people: but the LORD shall arise upon thee, and his glory shall be seen upon thee.",
        "context": "Isaiah 60 — eschatological vision of Zion's glory. God's glory (kabod) rises upon His people while darkness covers the earth — a light-darkness contrast paralleling Rev 18:1.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "ukebod YHWH alayik zarach — 'and the glory of the LORD is risen upon thee.' The glory illuminates God's people while darkness covers the nations. Connects to Rev 18:1 ('the earth was lightened with his glory')."
    },
    {
        "reference": "Isa 60:21",
        "heading": "All Blessings Designed to Lead to Glorification",
        "kjv_text": "Thy people also [shall be] all righteous: they shall inherit the land for ever, the branch of my planting, the work of my hands, that I may be glorified.",
        "context": "Isaiah 60:21 — God's purpose for His people: 'that I may be glorified.' All divine blessings aim at this end.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "lehithpa'er — 'that I may be glorified' (Hithpael infinitive of pa'ar H6286). Listed in Nave's GLORIFYING GOD: All the blessings of God are designed to lead to."
    },
    {
        "reference": "Rom 6:4",
        "heading": "Glory as Divine Power: Raised by the Glory of the Father",
        "kjv_text": "Therefore we are buried with him by baptism into death: that like as Christ was raised up from the dead by the glory of the Father, even so we also should walk in newness of life.",
        "context": "Romans 6:1-4 — baptism as death and resurrection with Christ. V.4: Christ was raised 'by the glory (doxa) of the Father' — glory here denotes omnipotence, a divine attribute.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "dia tes doxes tou patros — 'through the glory of the Father.' Doxa here = divine omnipotence (Running 1963: not flashing beams of light but God's attribute of Omnipotence). Glory as power/attribute, not merely radiance."
    },
    {
        "reference": "Rom 8:18",
        "heading": "Future Glory: Present Suffering vs. Coming Glory",
        "kjv_text": "For I reckon that the sufferings of this present time [are] not worthy [to be compared] with the glory which shall be revealed in us.",
        "context": "Romans 8:18-25 — the present suffering/future glory contrast. The glory 'revealed in us' is eschatological — the full transformation that 2 Cor 3:18 begins now.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "ten mellousan doxan apokalyphthenai eis hemas — 'the glory about to be revealed unto us.' The future glory is already determined (mellousan) — it awaits revelation, not creation."
    },
    {
        "reference": "Rom 8:29",
        "heading": "Conformed to the Image of the Son",
        "kjv_text": "For whom he did foreknow, he also did predestinate [to be] conformed to the image of his Son, that he might be the firstborn among many brethren.",
        "context": "Romans 8:28-30 — the golden chain (foreknew, predestinated, called, justified, glorified). V.29: the goal is conformity to Christ's image (eikon).",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "symmorphous tes eikonos tou huiou autou — 'conformed to the image of his Son.' symmorphos (G4832) = same form/nature. The image-transformation trajectory: 2 Cor 3:18 (progressive) to Rom 8:29 (predestined goal) to 1 John 3:2 (completed at appearing)."
    },
    {
        "reference": "Rom 9:23",
        "heading": "Vessels of Mercy Prepared Unto Glory",
        "kjv_text": "And that he might make known the riches of his glory on the vessels of mercy, which he had afore prepared unto glory,",
        "context": "Romans 9:22-23 — God's patience with vessels of wrath and His desire to make known glory on vessels of mercy, 'prepared unto glory.'",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "ton plouton tes doxes autou epi skeue eleous — 'the riches of his glory on vessels of mercy.' Believers are vessels designed to display God's glory — connecting to the purpose of glory-giving."
    },
    {
        "reference": "Rom 11:36",
        "heading": "Doxology: All Things to His Glory",
        "kjv_text": "For of him, and through him, and to him, [are] all things: to whom [be] glory for ever. Amen.",
        "context": "Romans 11:33-36 — Paul's concluding doxology after chapters 9-11. All things originate from, are sustained by, and return to God — therefore glory belongs to Him forever.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "auto he doxa eis tous aionas — 'to him be glory forever.' Listed in Nave's GLORIFYING GOD under EXEMPLIFIED: Paul. The doxological formula ascribes glory as the creature's proper response to God's sovereignty."
    },
    {
        "reference": "Rom 15:6",
        "heading": "United Glorification: One Mind and One Mouth",
        "kjv_text": "That ye may with one mind [and] one mouth glorify God, even the Father of our Lord Jesus Christ.",
        "context": "Romans 15:5-6 — Paul's prayer for unity in worship. The purpose: united glorification of God with one mind and one mouth.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "doxazete ton theon — 'glorify God.' Listed in Nave's GLORIFYING GOD: Saints should unite in. Corporate glory-giving requires doctrinal and relational unity."
    },
    {
        "reference": "2 Cor 3:9-10",
        "heading": "The Surpassing Glory of the Gospel Ministry",
        "kjv_text": "For if the ministration of condemnation [be] glory, much more doth the ministration of righteousness exceed in glory. For even that which was made glorious had no glory in this respect, by reason of the glory that excelleth.",
        "context": "2 Corinthians 3:7-11 — Paul compares the glory of the old covenant ministry (Moses) with the surpassing glory of the new. The new covenant's glory outshines the old.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "The a fortiori argument: if the ministry of condemnation had glory, how much MORE the ministry of righteousness. The doxa of the gospel exceeds the doxa of Sinai — progressive revelation of glory."
    },
    {
        "reference": "2 Cor 9:13",
        "heading": "Obedience to Gospel Producing Glorification",
        "kjv_text": "Whiles by the experiment of this ministration they glorify God for your professed subjection unto the gospel of Christ, and for [your] liberal distribution unto them, and unto all [men];",
        "context": "2 Corinthians 9:12-13 — generous giving causes others to glorify God. The Corinthians' obedience and generosity produce glorification in others.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "doxazontes ton theon — 'glorifying God.' Listed in Nave's GLORIFYING GOD under grace to others. Obedience to the gospel and practical generosity become occasions for others to glorify God."
    },
    {
        "reference": "Eph 1:12",
        "heading": "To the Praise of His Glory: The Purpose of Election",
        "kjv_text": "That we should be to the praise of his glory, who first trusted in Christ.",
        "context": "Ephesians 1:3-14 — Paul's extended blessing on God's redemptive plan. V.12: the purpose of election is that believers be 'to the praise of his glory.'",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "eis epainon tes doxes autou — 'to the praise of his glory.' This phrase appears three times in Eph 1 (vv.6, 12, 14), forming a refrain: all salvation history aims at God's glorification."
    },
    {
        "reference": "Phil 2:11",
        "heading": "Every Tongue Confess to the Glory of God",
        "kjv_text": "And [that] every tongue should confess that Jesus Christ [is] Lord, to the glory of God the Father.",
        "context": "Philippians 2:9-11 — the exaltation following Christ's humiliation. Universal confession that Jesus is Lord results in glory to God the Father.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "exomologesetai... eis doxan theou patros — 'confess... to the glory of God the Father.' Confession (exomologeo G1843) and glory (doxa G1391) are linked: confessing Christ's lordship IS giving glory to the Father. This connects to the confession-idiom chain (Josh 7:19, John 9:24, Rev 14:7)."
    },
    {
        "reference": "Col 1:15",
        "heading": "Christ as the Image of the Invisible God",
        "kjv_text": "Who is the image of the invisible God, the firstborn of every creature:",
        "context": "Colossians 1:15-20 — the Christological hymn. Christ is the eikon (image) of the invisible God — making the invisible visible.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "eikon tou theou tou aoratou — 'image of the invisible God.' Christ is the visible expression of divine glory (cf. John 1:14, Heb 1:3). The eikon vocabulary connects to the image-transformation theme of 2 Cor 3:18 and Rom 8:29."
    },
    {
        "reference": "2 Th 1:12",
        "heading": "Christ's Name Glorified In You",
        "kjv_text": "That the name of our Lord Jesus Christ may be glorified in you, and ye in him, according to the grace of our God and the Lord Jesus Christ.",
        "context": "2 Thessalonians 1:11-12 — Paul's prayer that Christ's name be glorified in the Thessalonians. Mutual glorification: Christ glorified in believers, believers glorified in Christ.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "endoxasthe to onoma tou kyriou hemon Iesou en hymin — 'the name of our Lord Jesus may be glorified in you.' endoxasthe (G1740 endoxazo, aorist passive) — intensified form of doxazo. Listed in Nave's GLORIFYING GOD under Accomplished by: Glorifying Christ."
    },
    {
        "reference": "Heb 2:10",
        "heading": "Bringing Many Sons Unto Glory",
        "kjv_text": "For it became him, for whom [are] all things, and by whom [are] all things, in bringing many sons unto glory, to make the captain of their salvation perfect through sufferings.",
        "context": "Hebrews 2:5-18 — Christ's identification with humanity. V.10: God's purpose is 'bringing many sons unto glory' — salvation's goal is glorification.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "pollous huious eis doxan agagonta — 'bringing many sons unto glory.' Glory (doxa) is the destination of salvation. The 'captain' (archegos) was perfected through suffering — the path to glory passes through suffering (cf. 1 Pet 4:14-16)."
    },
    {
        "reference": "1 Pet 1:8",
        "heading": "Joy Unspeakable and Full of Glory",
        "kjv_text": "Whom having not seen, ye love; in whom, though now ye see [him] not, yet believing, ye rejoice with joy unspeakable and full of glory:",
        "context": "1 Peter 1:3-9 — the living hope. V.8: faith in the unseen Christ produces joy 'full of glory' (dedoxasmene, perfect passive participle of doxazo — glorified joy).",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "chara aneklaleto kai dedoxasmene — 'joy unspeakable and glorified.' dedoxasmene (perfect passive participle of doxazo G1392) — the joy is already in a state of glory. Faith produces glory even before sight."
    },
    {
        "reference": "1 Pet 4:14-16",
        "heading": "Suffering as a Christian: The Spirit of Glory Rests on You",
        "kjv_text": "If ye be reproached for the name of Christ, happy [are ye]; for the spirit of glory and of God resteth upon you: on their part he is evil spoken of, but on your part he is glorified. But let none of you suffer as a murderer, or [as] a thief, or [as] an evildoer, or as a busybody in other men's matters. Yet if [any man suffer] as a Christian, let him not be ashamed; but let him glorify God on this behalf.",
        "context": "1 Peter 4:12-19 — suffering for Christ. The 'spirit of glory' rests on persecuted believers. Suffering as a Christian is an occasion to glorify God.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "to tes doxes kai to tou theou pneuma — 'the spirit of glory and of God.' doxazeto ton theon (v.16) — 'let him glorify God' (present imperative). Listed in Nave's GLORIFYING GOD under Accomplished by: Suffering for Christ."
    },
    {
        "reference": "2 Pet 1:3-4",
        "heading": "Called to Glory and Virtue: Partakers of Divine Nature",
        "kjv_text": "According as his divine power hath given unto us all things that [pertain] unto life and godliness, through the knowledge of him that hath called us to glory and virtue: Whereby are given unto us exceeding great and precious promises: that by these ye might be partakers of the divine nature, having escaped the corruption that is in the world through lust.",
        "context": "2 Peter 1:3-11 — the divine provision for godliness. God calls believers 'to glory and virtue' and grants participation in 'divine nature' — the ultimate fulfillment of the image-transformation trajectory.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "tou kalesantos hemas dia doxes kai aretes — 'him that called us by/to glory and virtue.' theias koinonoi physeos — 'partakers of divine nature.' This is the climax of the glory-transformation trajectory: not merely reflecting glory but participating in the divine nature itself."
    },
    {
        "reference": "Rev 14:11",
        "heading": "No Rest for Beast Worshippers: The Anti-Glory",
        "kjv_text": "And the smoke of their torment ascendeth up for ever and ever: and they have no rest day nor night, who worship the beast and his image, and whosoever receiveth the mark of his name.",
        "context": "Revelation 14:9-11 — the third angel's warning. Those who give glory to the beast (worship his image) instead of God receive the opposite of rest — ceaseless torment.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "The contrast: those who give glory to God receive blessing (Rev 14:13); those who give glory to the beast receive unrest (Rev 14:11). Worshipping the beast's image (eikon) inverts the image-transformation of 2 Cor 3:18."
    },
    {
        "reference": "Rev 21:11,23",
        "heading": "New Jerusalem: Glory Fully Realized",
        "kjv_text": "Having the glory of God: and her light [was] like unto a stone most precious, even like a jasper stone, clear as crystal; And the city had no need of the sun, neither of the moon, to shine in it: for the glory of God did lighten it, and the Lamb [is] the light thereof.",
        "context": "Revelation 21 — the New Jerusalem. The city has 'the glory of God' (v.11) and needs no sun because God's glory IS its light (v.23). The eschatological fulfillment of Hab 2:14 and Isa 6:3.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "he doxa tou theou ephotisen auten — 'the glory of God lightened it' (v.23). he polis... echousan ten doxan tou theou — 'the city having the glory of God' (v.11). In the New Jerusalem, glory is no longer commanded but fully realized — the creation-wide filling of glory that was always God's purpose."
    },
    {
        "reference": "Luke 17:15-18",
        "heading": "Only One Returned to Give Glory: Gratitude as Glorification",
        "kjv_text": "And one of them, when he saw that he was healed, turned back, and with a loud voice glorified God, And fell down on [his] face at his feet, giving him thanks: and he was a Samaritan. And Jesus answering said, Were there not ten cleansed? but where [are] the nine? There are not found that returned to give glory to God, save this stranger.",
        "context": "Luke 17:11-19 — the ten lepers cleansed, only one returns. Jesus frames the return as 'giving glory to God' (dounai doxan to theo) — gratitude expressed as glorification.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "dounai doxan to theo (v.18) — 'to give glory to God' — the same didomi + doxa construction as Rev 14:7. edoxazen ton theon (v.15) — 'glorified God' (imperfect of doxazo). Gratitude is a form of glory-giving; ingratitude is a form of the refusal described in Rom 1:21 ('neither were thankful')."
    },
    {
        "reference": "John 21:19",
        "heading": "Death as Glorification: Martyrdom as Glory-Giving",
        "kjv_text": "This spake he, signifying by what death he should glorify God. And when he had spoken this, he saith unto him, Follow me.",
        "context": "John 21:18-19 — Jesus prophesies Peter's martyrdom. Peter's death is described as glorifying God — physical death as an act of glory-giving.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "doxasei ton theon — 'he should glorify God' (future active of doxazo G1392). Listed in Nave's GLORIFYING GOD under Accomplished by: Dying for him. Martyrdom is a mode of glorification."
    },
    {
        "reference": "Acts 4:21",
        "heading": "People Glorified God for Healing",
        "kjv_text": "So when they had further threatened them, they let them go, finding nothing how they might punish them, because of the people: for all [men] glorified God for that which was done.",
        "context": "Acts 4:13-22 — the Sanhedrin releases Peter and John because the people glorify God for the healing miracle. Observers glorify God when they witness His works.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "pantes edoxazon ton theon — 'all glorified God' (imperfect of doxazo G1392). Listed in Nave's GLORIFYING GOD for wondrous works. Miracles/healing prompts spontaneous glorification — a response category."
    },
    {
        "reference": "Eph 4:24",
        "heading": "New Man Created After God in Righteousness",
        "kjv_text": "And that ye put on the new man, which after God is created in righteousness and true holiness.",
        "context": "Ephesians 4:22-24 — put off the old man, put on the new. The new man is 'created after God' (kata theon) in righteousness and holiness — image-restoration language.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "ton kata theon ktisthenta en dikaiosyne kai hosioteti — 'created after God in righteousness and holiness.' The new creation is kata theon — according to God's pattern/image. Parallels Col 3:10 (renewed after the image of the Creator)."
    },
    {
        "reference": "Jas 1:23-24",
        "heading": "Mirror Metaphor: Self-Examination Contrast with 2 Cor 3:18",
        "kjv_text": "For if any be a hearer of the word, and not a doer, he is like unto a man beholding his natural face in a glass: For he beholdeth himself, and goeth his way, and straightway forgetteth what manner of man he was.",
        "context": "James 1:22-25 — hearing vs. doing the word. The mirror (esoptron) metaphor here is a contrast with 2 Cor 3:18's katoptrizomai: James' mirror reveals the hearer's own face; Paul's mirror reveals the Lord's glory.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "katanoounti to prosopon... en esoptro — 'beholding his natural face in a mirror.' esoptron (G2072) is the standard word for mirror; Paul uses katoptrizomai (G2734) from katoptron. James' mirror shows self; Paul's mirror shows Christ's glory — the distinction matters for understanding the beholding-transformation mechanism."
    },
    {
        "reference": "Psa 19:1",
        "heading": "Creation Declares Glory: The Heavens as Testimony",
        "kjv_text": "The heavens declare the glory of God; and the firmament sheweth his handywork.",
        "context": "Psalm 19:1-6 — creation's testimony to God's glory. The heavens 'declare' (mesapperim) God's glory (kabod) without words — a non-verbal form of glory-giving that parallels Rom 1:19-20.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "hashamayim mesapperim kebod El — 'the heavens declare the glory of God.' Creation itself gives glory to God by displaying His attributes. This is the testimony that Rom 1:19-20 says leaves humanity 'without excuse' for failing to glorify."
    },
    {
        "reference": "Psa 99:9",
        "heading": "Worship at His Holy Hill: God Is Holy",
        "kjv_text": "Exalt the LORD our God, and worship at his holy hill; for the LORD our God [is] holy.",
        "context": "Psalm 99 — God's holiness. V.9: exaltation and worship grounded in holiness. Listed in Nave's GLORIFYING GOD for his holiness.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "romemu YHWH Eloheinu vehishtachavu lehar qodsho — 'exalt the LORD our God and worship at his holy hill.' Listed in Nave's GLORIFYING GOD for his holiness. Holiness is the ground of glorification — connecting to Isa 6:3 ('Holy, holy, holy... the whole earth is full of his glory')."
    }
]

data['verses'].extend(new_verses)

with open('D:/bible/bible-studies/3am-06-give-glory/research.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f'Done. Total verses now: {len(data["verses"])}')
# Verify H3034 fix
for ws in data['word_studies']:
    if ws['strongs'] == 'H3034':
        assert 'PMI 7.58' in ws['summary'], f"PMI fix failed: {ws['summary']}"
        assert 'PMI 33.14' not in ws['summary'], f"Old PMI still present"
        print('H3034 PMI fix verified: PMI 7.58')
        break
