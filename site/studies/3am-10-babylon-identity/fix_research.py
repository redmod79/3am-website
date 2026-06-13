import json

f = open('D:/bible/bible-studies/3am-10-babylon-identity/research.json', 'r', encoding='utf-8')
data = json.load(f)
f.close()

ws = data['word_studies']

# FIX 1: Occurrence count fixes (10 fixes)
ws[0]['occurrence_count'] = 107    # H2181
ws[6]['occurrence_count'] = 264    # H894
ws[7]['occurrence_count'] = 45     # H1101
ws[11]['occurrence_count'] = 127   # H8441
ws[15]['occurrence_count'] = 93    # G4098
ws[16]['occurrence_count'] = 133   # H2534
ws[17]['occurrence_count'] = 33    # G3631
ws[18]['occurrence_count'] = 151   # H3196
ws[19]['occurrence_count'] = 65    # G4352
ws[20]['occurrence_count'] = 194   # H7812

# FIX 2: PMI fix
ws[16]['relevance'] = ws[16]['relevance'].replace('PMI 27.69', 'PMI 6.18')

# FIX 3: Add 28 missing supporting verses
supporting = [
    {
        "reference": "Rev 14:8",
        "heading": "Second Angel -- Babylon Is Fallen (standalone supporting)",
        "kjv_text": "And there followed another angel, saying, Babylon is fallen, is fallen, that great city, because she made all nations drink of the wine of the wrath of her fornication.",
        "context": "The second angel's announcement within the three angels' messages sequence. Already covered as part of Rev 14:6-12 primary entry; listed here as standalone supporting reference.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. Crux text for this study; full analysis in the Rev 14:6-12 primary entry.",
        "tier": "supporting",
        "focus_areas": [1, 8, 10]
    },
    {
        "reference": "Rev 17:1-3",
        "heading": "Harlot-Bride Bracket -- Harlot Introduction Formula (standalone supporting)",
        "kjv_text": "And there came one of the seven angels which had the seven vials, and talked with me, saying unto me, Come hither; I will shew unto thee the judgment of the great whore that sitteth upon many waters: With whom the kings of the earth have committed fornication, and the inhabitants of the earth have been made drunk with the wine of her fornication. So he carried me away in the spirit into the wilderness: and I saw a woman sit upon a scarlet coloured beast, full of names of blasphemy, having seven heads and ten horns.",
        "context": "The angel-introduction formula that is word-for-word parallel to Rev 21:9-10. Already part of the Rev 17:1-6 primary entry; listed here for the bracket comparison.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. The bracket formula shared with Rev 21:9-10 is the key structural argument.",
        "tier": "supporting",
        "focus_areas": [2]
    },
    {
        "reference": "Rev 18:8-10",
        "heading": "Sudden Destruction of Babylon -- Parallels Jer 51:8",
        "kjv_text": "Therefore shall her plagues come in one day, death, and mourning, and famine; and she shall be utterly burned with fire: for strong [is] the Lord God who judgeth her. And the kings of the earth, who have committed fornication and lived deliciously with her, shall bewail her, and lament for her, when they shall see the smoke of her burning, Standing afar off for the fear of her torment, saying, Alas, alas, that great city Babylon, that mighty city! for in one hour is thy judgment come.",
        "context": "The sudden destruction of Babylon in one day/hour. Parallels Jer 51:8.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. The 'one hour' judgment emphasizes suddenness, echoing Jer 51:8.",
        "tier": "supporting",
        "focus_areas": [7, 10]
    },
    {
        "reference": "Rev 18:20-21",
        "heading": "Heaven Rejoices, Millstone Cast -- Parallels Jer 51:48, 63-64",
        "kjv_text": "Rejoice over her, [thou] heaven, and [ye] holy apostles and prophets; for God hath avenged you on her. And a mighty angel took up a stone like a great millstone, and cast [it] into the sea, saying, Thus with violence shall that great city Babylon be thrown down, and shall be found no more at all.",
        "context": "Heaven commanded to rejoice over Babylon's fall (cf. Jer 51:48). The millstone symbolic act directly echoes Jer 51:63-64.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. Two direct Jer 51 parallels: heaven rejoices (51:48) and millstone sinking (51:63-64).",
        "tier": "supporting",
        "focus_areas": [7]
    },
    {
        "reference": "Rev 19:1-2",
        "heading": "Judgment of the Great Whore -- Vindication of Martyrs",
        "kjv_text": "And after these things I heard a great voice of much people in heaven, saying, Alleluia; Salvation, and glory, and honour, and power, unto the Lord our God: For true and righteous [are] his judgments: for he hath judged the great whore, which did corrupt the earth with her fornication, and hath avenged the blood of his servants at her hand.",
        "context": "Heavenly doxology after Babylon's fall. Double charge: corrupting the earth with fornication and shedding blood of God's servants.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. Resolves the altar-vindication arc (Rev 6:10 answered here).",
        "tier": "supporting",
        "focus_areas": [10]
    },
    {
        "reference": "Jer 50:1-3",
        "heading": "Prophecy Against Babylon and Its Idols -- OT Judgment Template",
        "kjv_text": "The word that the LORD spake against Babylon [and] against the land of the Chaldeans by Jeremiah the prophet. Declare ye among the nations, and publish, and set up a standard; publish, [and] conceal not: say, Babylon is taken, Bel is confounded, Merodach is broken in pieces; her idols are confounded, her images are broken in pieces. For out of the north there cometh up a nation against her, which shall make her land desolate, and none shall dwell therein: they shall remove, they shall depart, both man and beast.",
        "context": "Opening of Jeremiah's Babylon oracle (chs. 50-51). Babylon's gods confounded -- idolatry central to identity.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. Part of the Jer 50-51 / Rev 17-18 literary typology.",
        "tier": "supporting",
        "focus_areas": [7]
    },
    {
        "reference": "Jer 50:8",
        "heading": "Flee from Babylon -- OT Come-Out Call",
        "kjv_text": "Remove out of the midst of Babylon, and go forth out of the land of the Chaldeans, and be as the he goats before the flocks.",
        "context": "One of several flee/come-out commands in Jer 50-51. Direct OT source for Rev 18:4.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. Part of the come-out command chain: Jer 50:8, 51:6, 51:45 -> Rev 18:4.",
        "tier": "supporting",
        "focus_areas": [7]
    },
    {
        "reference": "Jer 50:39-40",
        "heading": "Permanent Desolation of Babylon -- Fulfillment Question",
        "kjv_text": "Therefore the wild beasts of the desert with the wild beasts of the islands shall dwell [there], and the owls shall dwell therein: and it shall be no more inhabited for ever; neither shall it be dwelt in from generation to generation. As God overthrew Sodom and Gomorrah and the neighbour [cities] thereof, saith the LORD; [so] shall no man abide there, neither shall any son of man dwell therein.",
        "context": "Prophecy of Babylon's permanent Sodom-like desolation. Futurists argue these were never literally fulfilled.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. Key evidence for futurist position. Historicist response: Revelation applies typologically.",
        "tier": "supporting",
        "focus_areas": [7, 10]
    },
    {
        "reference": "Jer 51:44",
        "heading": "Bel Punished in Babylon -- Nations No Longer Flow",
        "kjv_text": "And I will punish Bel in Babylon, and I will bring forth out of his mouth that which he hath swallowed up: and the nations shall not flow together any more unto him: yea, the wall of Babylon shall fall.",
        "context": "God punishes Bel (chief Babylonian deity). Nations cease flowing to Babylon.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. Part of the Jer 50-51 / Rev 17-18 typology.",
        "tier": "supporting",
        "focus_areas": [7]
    },
    {
        "reference": "Jer 51:63-64",
        "heading": "Millstone Sinking -- Jeremiah's Symbolic Act, Rev 18:21 Parallel",
        "kjv_text": "And it shall be, when thou hast made an end of reading this book, [that] thou shalt bind a stone to it, and cast it into the midst of Euphrates: And thou shalt say, Thus shall Babylon sink, and shall not rise from the evil that I will bring upon her: and they shall be weary. Thus far [are] the words of Jeremiah.",
        "context": "Seraiah's symbolic act. Direct source for Rev 18:21.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. One of the 13 thematic connections between Jer 50-51 and Rev 17-18.",
        "tier": "supporting",
        "focus_areas": [7]
    },
    {
        "reference": "Isa 13:1-6",
        "heading": "Burden of Babylon -- Day of the LORD Judgment Language",
        "kjv_text": "The burden of Babylon, which Isaiah the son of Amoz did see. Lift ye up a banner upon the high mountain, exalt the voice unto them, shake the hand, that they may go into the gates of the nobles. I have commanded my sanctified ones, I have also called my mighty ones for mine anger, [even] them that rejoice in my highness. The noise of a multitude in the mountains, like as of a great people; a tumultuous noise of the kingdoms of nations gathered together: the LORD of hosts mustereth the host of the battle. They come from a far country, from the end of heaven, [even] the LORD, and the weapons of his indignation, to destroy the whole land. Howl ye; for the day of the LORD [is] at hand; it shall come as a destruction from the Almighty.",
        "context": "Isaiah's burden against Babylon uses Day of the LORD language -- connecting Babylon's judgment to eschatological judgment.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. Day of the LORD framework supports reading Revelation's Babylon as eschatological.",
        "tier": "supporting",
        "focus_areas": [7, 10]
    },
    {
        "reference": "Isa 47:1-9",
        "heading": "Virgin Daughter of Babylon -- Sorceries and Self-Exaltation",
        "kjv_text": "Come down, and sit in the dust, O virgin daughter of Babylon, sit on the ground: [there is] no throne, O daughter of the Chaldeans: for thou shalt no more be called tender and delicate. Take the millstones, and grind meal: uncover thy locks, make bare the leg, uncover the thigh, pass over the rivers. Thy nakedness shall be uncovered, yea, thy shame shall be seen: I will take vengeance, and I will not meet [thee as] a man. [As for] our redeemer, the LORD of hosts [is] his name, the Holy One of Israel. Sit thou silent, and get thee into darkness, O daughter of the Chaldeans: for thou shalt no more be called, The lady of kingdoms. I was wroth with my people, I have polluted mine inheritance, and given them into thine hand: thou didst shew them no mercy; upon the ancient hast thou very heavily laid thy yoke. And thou saidst, I shall be a lady for ever: [so] that thou didst not lay these [things] to thy heart, neither didst remember the latter end of it. Therefore hear now this, [thou that art] given to pleasures, that dwellest carelessly, that sayest in thine heart, I [am], and none else beside me; I shall not sit [as] a widow, neither shall I know the loss of children: But these two [things] shall come to thee in a moment in one day, the loss of children, and widowhood: they shall come upon thee in their perfection for the multitude of thy sorceries, [and] for the great abundance of thine enchantments.",
        "context": "Isaiah's taunt against Babylon personified as a woman. Key parallels: self-exaltation (cf. Rev 18:7), sorceries (cf. Rev 18:23), sudden one-day destruction (cf. Rev 18:8).",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. Multiple verbal parallels to Revelation's Babylon. Sorceries (kesheph) become pharmakeia in Rev 18:23.",
        "tier": "supporting",
        "focus_areas": [7, 10]
    },
    {
        "reference": "Ezek 16:8-14",
        "heading": "God's Covenant with Jerusalem -- The Marriage Metaphor Foundation",
        "kjv_text": "Now when I passed by thee, and looked upon thee, behold, thy time [was] the time of love; and I spread my skirt over thee, and covered thy nakedness: yea, I sware unto thee, and entered into a covenant with thee, saith the Lord GOD, and thou becamest mine. Then washed I thee with water; yea, I throughly washed away thy blood from thee, and I anointed thee with oil. I clothed thee also with broidered work, and shod thee with badgers' skin, and I girded thee about with fine linen, and I covered thee with silk. I decked thee also with ornaments, and I put bracelets upon thy hands, and a chain on thy neck. And I put a jewel on thy forehead, and earrings in thine ears, and a beautiful crown upon thine head. Thus wast thou decked with gold and silver; and thy raiment [was of] fine linen, and silk, and broidered work; thou didst eat fine flour, and honey, and oil: and thou wast exceeding beautiful, and thou didst prosper into a kingdom. And thy renown went forth among the heathen for thy beauty: for it [was] perfect through my comeliness, which I had put upon thee, saith the Lord GOD.",
        "context": "God's marriage covenant with Jerusalem -- the foundation for the harlotry metaphor in vv.15ff.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. Essential context for the Ezek 16:15-22 primary entry. The garments God gives are later used for harlotry.",
        "tier": "supporting",
        "focus_areas": [1]
    },
    {
        "reference": "Hos 4:11-12",
        "heading": "Whoredom and Wine Take Away the Heart",
        "kjv_text": "Whoredom and wine and new wine take away the heart. My people ask counsel at their stocks, and their staff declareth unto them: for the spirit of whoredoms hath caused [them] to err, and they have gone a whoring from under their God.",
        "context": "Hosea links whoredom (zanah) with wine as agents that remove understanding. Parallel to Babylon's intoxicating wine (Rev 14:8).",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. The zanah-wine connection is critical for understanding Rev 14:8.",
        "tier": "supporting",
        "focus_areas": [1, 8]
    },
    {
        "reference": "Jer 2:20",
        "heading": "Israel Broke Yoke and Played the Harlot",
        "kjv_text": "For of old time I have broken thy yoke, [and] burst thy bands; and thou saidst, I will not transgress; when upon every high hill and under every green tree thou wanderest, playing the harlot.",
        "context": "Another Jeremiah passage using zanah for Israel's covenant unfaithfulness.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. Part of the comprehensive zanah word chain in the prophets.",
        "tier": "supporting",
        "focus_areas": [1]
    },
    {
        "reference": "Rev 12:17",
        "heading": "Remnant Who Keep Commandments -- Faithful Counterpart to Babylon",
        "kjv_text": "And the dragon was wroth with the woman, and went to make war with the remnant of her seed, which keep the commandments of God, and have the testimony of Jesus Christ.",
        "context": "The remnant -- the faithful counterpart to Babylon's apostasy. Part of the commandment inclusio (Rev 12:17 -> 14:12).",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. Establishes the worship/obedience binary.",
        "tier": "supporting",
        "focus_areas": [10]
    },
    {
        "reference": "Rev 13:11-14",
        "heading": "Second Beast -- Lamblike Horns, Possible Daughter Connection",
        "kjv_text": "And I beheld another beast coming up out of the earth; and he had two horns like a lamb, and he spake as a dragon. And he exerciseth all the power of the first beast before him, and causeth the earth and them which dwell therein to worship the first beast, whose deadly wound was healed. And he doeth great wonders, so that he maketh fire come down from heaven on the earth in the sight of men, And deceiveth them that dwell on the earth by [the means of] those miracles which he had power to do in the sight of the beast; saying to them that dwell on the earth, that they should make an image to the beast, which had the wound by a sword, and did live.",
        "context": "The second beast with lamblike horns. Bohr identifies as 'daughters of the harlot.' The text itself does not use harlot language.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. Verify whether the text identifies the second beast as a daughter of the harlot.",
        "tier": "supporting",
        "focus_areas": [3, 10]
    },
    {
        "reference": "Rev 14:9-11",
        "heading": "Third Angel's Warning -- Consequence of Following Babylon",
        "kjv_text": "And the third angel followed them, saying with a loud voice, If any man worship the beast and his image, and receive [his] mark in his forehead, or in his hand, The same shall drink of the wine of the wrath of God, which is poured out without mixture into the cup of his indignation; and he shall be tormented with fire and brimstone in the presence of the holy angels, and in the presence of the Lamb: And the smoke of their torment ascendeth up for ever and ever: and they have no rest day nor night, who worship the beast and his image, and whosoever receiveth the mark of his name.",
        "context": "The third angel warns of consequence for following Babylon/beast. Polarity flip completed.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. Thumos polarity flip: Babylon's thumos (14:8) answered by God's thumos+orge (14:10).",
        "tier": "supporting",
        "focus_areas": [8, 10]
    },
    {
        "reference": "Rev 14:12",
        "heading": "Saints Who Keep Commandments and Faith of Jesus",
        "kjv_text": "Here is the patience of the saints: here [are] they that keep the commandments of God, and the faith of Jesus.",
        "context": "The alternative to Babylon. Completes the commandment inclusio with Rev 12:17.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. Positive counterpart to Babylon's corruption.",
        "tier": "supporting",
        "focus_areas": [10]
    },
    {
        "reference": "Rev 2:20-22",
        "heading": "Jezebel Teaching Fornication in the Church",
        "kjv_text": "Notwithstanding I have a few things against thee, because thou sufferest that woman Jezebel, which calleth herself a prophetess, to teach and to seduce my servants to commit fornication, and to eat things sacrificed unto idols. And I gave her space to repent of her fornication; and she repented not. Behold, I will cast her into a bed, and them that commit adultery with her into great tribulation, except they repent of their deeds.",
        "context": "Jezebel operates WITHIN the church, teaching fornication and idolatry. Harlotry from within.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. Internal corruption using porneia vocabulary -- a Babylon-type figure within the church.",
        "tier": "supporting",
        "focus_areas": [1, 10]
    },
    {
        "reference": "Dan 4:30",
        "heading": "Nebuchadnezzar's Babylon -- Is Not This Great Babylon?",
        "kjv_text": "The king spake, and said, Is not this great Babylon, that I have built for the house of the kingdom by the might of my power, and for the honour of my majesty?",
        "context": "Nebuchadnezzar's boast -- pride preceding fall. Self-exaltation parallels Rev 18:7.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. The 'great Babylon' designation echoes through Rev 14:8, 17:5, 18:2.",
        "tier": "supporting",
        "focus_areas": [4, 10]
    },
    {
        "reference": "Gen 10:8-10",
        "heading": "Nimrod Built Babel -- Origins of Babylon",
        "kjv_text": "And Cush begat Nimrod: he began to be a mighty one in the earth. He was a mighty hunter before the LORD: wherefore it is said, Even as Nimrod the mighty hunter before the LORD. And the beginning of his kingdom was Babel, and Erech, and Accad, and Calneh, in the land of Shinar.",
        "context": "The origin of Babel/Babylon as Nimrod's first kingdom.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. Babel as the beginning of human kingdom-building.",
        "tier": "supporting",
        "focus_areas": [4]
    },
    {
        "reference": "Lev 19:29",
        "heading": "Prohibition Against Harlotry",
        "kjv_text": "Do not prostitute thy daughter, to cause her to be a whore; lest the land fall to whoredom, and the land become full of wickedness.",
        "context": "Legal prohibition. Harlotry spreads -- 'the land fall to whoredom.'",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. Harlotry portrayed as spreading/reproductive.",
        "tier": "supporting",
        "focus_areas": [1, 3]
    },
    {
        "reference": "Deut 23:17",
        "heading": "No Temple Prostitution -- Zanah in Worship Context",
        "kjv_text": "There shall be no whore of the daughters of Israel, nor a sodomite of the sons of Israel.",
        "context": "Prohibition of cultic/temple prostitution. Links zanah to worship context.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. Links harlotry to worship context.",
        "tier": "supporting",
        "focus_areas": [1]
    },
    {
        "reference": "Rev 17:14",
        "heading": "Lamb Overcomes Beast -- Final Resolution",
        "kjv_text": "These shall make war with the Lamb, and the Lamb shall overcome them: for he is Lord of lords, and King of kings: and they that are with him [are] called, and chosen, and faithful.",
        "context": "The Lamb's victory resolves the Babylon conflict.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. Resolution: those with the Lamb overcome those allied with Babylon.",
        "tier": "supporting",
        "focus_areas": [10]
    },
    {
        "reference": "Matt 23:35-37",
        "heading": "Blood-Guilt Principle -- One Continuous Phenomenon",
        "kjv_text": "That upon you may come all the righteous blood shed upon the earth, from the blood of righteous Abel unto the blood of Zacharias son of Barachias, whom ye slew between the temple and the altar. Verily I say unto you, All these things shall come upon this generation. O Jerusalem, Jerusalem, [thou] that killest the prophets, and stonest them which are sent unto thee, how often would I have gathered thy children together, even as a hen gathereth her chickens under [her] wings, and ye would not!",
        "context": "Jesus charges Jerusalem with cumulative blood-guilt. Rev 18:24 applies the same principle to Babylon.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. Comprehensive blood-guilt principle: the Babylon spirit is one continuous phenomenon.",
        "tier": "supporting",
        "focus_areas": [10, 12]
    },
    {
        "reference": "Psa 137:8-9",
        "heading": "Prophecy Against Babylon -- Exiles' Response",
        "kjv_text": "O daughter of Babylon, who art to be destroyed; happy [shall he be], that rewardeth thee as thou hast served us. Happy [shall he be], that taketh and dasheth thy little ones against the stones.",
        "context": "The exiles' cry against Babylon. 'Daughter of Babylon' uses family/reproduction language.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. 'Daughter of Babylon' connects to mother-daughter vocabulary in Rev 17:5.",
        "tier": "supporting",
        "focus_areas": [3, 7]
    },
    {
        "reference": "Isa 21:9",
        "heading": "Babylon Is Fallen, Is Fallen -- OT Source of Doubled Formula",
        "kjv_text": "And, behold, here cometh a chariot of men, [with] a couple of horsemen. And he answered and said, Babylon is fallen, is fallen; and all the graven images of her gods he hath broken unto the ground.",
        "context": "Direct OT source for the doubled 'is fallen, is fallen' formula in Rev 14:8 and 18:2.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. The doubled fall-formula reused verbatim in Revelation.",
        "tier": "supporting",
        "focus_areas": [7, 8, 10]
    },
    {
        "reference": "1 Ki 12:28-33",
        "heading": "Jeroboam's State-Sponsored Apostasy -- Archetype of Institutional False Worship",
        "kjv_text": "Whereupon the king took counsel, and made two calves [of] gold, and said unto them, It is too much for you to go up to Jerusalem: behold thy gods, O Israel, which brought thee up out of the land of Egypt. And he set the one in Bethel, and the other put he in Dan. And this thing became a sin: for the people went [to worship] before the one, [even] unto Dan. And he made an house of high places, and made priests of the lowest of the people, which were not of the sons of Levi. And Jeroboam ordained a feast in the eighth month, on the fifteenth day of the month, like unto the feast that [is] in Judah, and he offered upon the altar. So did he in Bethel, sacrificing unto the calves that he had made: and he placed in Bethel the priests of the high places which he had made. So he offered upon the altar which he had made in Bethel the fifteenth day of the eighth month, [even] in the month which he had devised of his own heart; and ordained a feast unto the children of Israel: and he offered upon the altar, and burnt incense.",
        "context": "Jeroboam creates a counterfeit worship system. OT archetype of institutional apostasy.",
        "greek_parsing": [],
        "hebrew_parsing": [],
        "notes": "Supporting tier. The archetype of the Babylon principle: state-sponsored false worship imitating the true.",
        "tier": "supporting",
        "focus_areas": [10]
    }
]

data['verses'].extend(supporting)

with open('D:/bible/bible-studies/3am-10-babylon-identity/research.json', 'w', encoding='utf-8') as out:
    json.dump(data, out, ensure_ascii=False, indent=2)

print(f"Done. Verses: {len(data['verses'])}, WordStudies: {len(data['word_studies'])}")
print(f"Occurrence checks:")
for i, s in enumerate(ws):
    print(f"  [{i}] {s['strongs']} = {s['occurrence_count']}")
print(f"PMI check: {'PMI 6.18' in ws[16]['relevance']}")
