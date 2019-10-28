from .features import Dictionary, RegexMatches, Stopwords

name = "latvian"

try:
    import enchant
    dictionary = enchant.Dict("lv")
except enchant.errors.DictNotFoundError:
    raise ImportError("No enchant-compatible dictionary found for 'lv'.  " +
                      "Consider installing 'myspell-lv'.")

dictionary = Dictionary(name + ".dictionary", dictionary.check)
"""
:class:`~revscoring.languages.features.Dictionary` features via
`enchant.Dict <https://github.com/rfk/pyenchant>`_ "lv".  Provided by `aspell-lv`
"""

stopwords = [
    r"aizmetnis",
    r"amerikas",
    r"and",
    r"angļu",
    r"apmēram",
    r"arī",
    r"asv",
    r"atdalīšana",
    r"atrodas",
    r"atsauce",
    r"atsauces",
    r"att",
    r"attēls",
    r"autoritatīvā",
    r"beigās",
    r"bet",
    r"bez",
    r"bieži",
    r"bija",
    r"būt",
    r"caption",
    r"centrs",
    r"cilvēki",
    r"cilvēks",
    r"citas",
    r"citi",
    r"citu",
    r"dat",
    r"datums",
    r"daudz",
    r"daļa",
    r"daļu",
    r"diena",
    r"dienas",
    r"divas",
    r"dzimis",
    r"dzimums",
    r"dzimušie",
    r"dzīves",
    r"dēļ",
    r"eiropas",
    r"flaga",
    r"gada",
    r"gadam",
    r"gados",
    r"gads",
    r"gadsimta",
    r"gadu",
    r"gadus",
    r"gadā",
    r"gan",
    r"gandrīz",
    r"garums",
    r"ieguva",
    r"iespējams",
    r"ikona",
    r"infokaste",
    r"izmērs",
    r"izveidots",
    r"janvārī",
    r"jau",
    r"jeb",
    r"jpg",
    r"jāuzlabo",
    r"kad",
    r"kara",
    r"karš",
    r"kas",
    r"kategorija",
    r"kategorijas",
    r"kopā",
    r"kopš",
    r"krievija",
    r"krievijas",
    r"kur",
    r"kura",
    r"kuras",
    r"kuru",
    r"kurā",
    r"kurš",
    r"kļuva",
    r"lai",
    r"laika",
    r"laiks",
    r"laiku",
    r"laikā",
    r"latns",
    r"latviešu",
    r"latvija",
    r"latvijas",
    r"latvijā",
    r"lielākā",
    r"līdz",
    r"mājaslapa",
    r"mūsdienās",
    r"nav",
    r"nbsp",
    r"nekā",
    r"news",
    r"nosaukums",
    r"notika",
    r"nozīmes",
    r"nozīmju",
    r"old",
    r"orig",
    r"otrā",
    r"padomju",
    r"par",
    r"paraksts",
    r"parasti",
    r"pasaules",
    r"pasaulē",
    r"pat",
    r"pašlaik",
    r"pie",
    r"piemēram",
    r"piezīmes",
    r"pilsēta",
    r"pilsētas",
    r"pirmais",
    r"pirmo",
    r"pirms",
    r"pirmā",
    r"platums",
    r"pret",
    r"psrs",
    r"publisher",
    r"pēc",
    r"raksts",
    r"ref",
    r"reizi",
    r"right",
    r"rīga",
    r"rīgas",
    r"saites",
    r"savas",
    r"savienotās",
    r"savienība",
    r"savu",
    r"savukārt",
    r"savā",
    r"skaits",
    r"skatīt",
    r"sporta",
    r"starp",
    r"sāka",
    r"sākumā",
    r"tad",
    r"tai",
    r"tajā",
    r"tam",
    r"tas",
    r"taču",
    r"text",
    r"tie",
    r"tiek",
    r"tiem",
    r"tika",
    r"tikai",
    r"title",
    r"tomēr",
    r"trīs",
    r"type",
    r"tāpat",
    r"tās",
    r"tīmekļa",
    r"url",
    r"vadība",
    r"vai",
    r"vairāk",
    r"vairākas",
    r"val",
    r"valoda",
    r"valodā",
    r"valstis",
    r"valsts",
    r"var",
    r"veido",
    r"viena",
    r"viens",
    r"vienu",
    r"vieta",
    r"vietas",
    r"vietu",
    r"vietā",
    r"visas",
    r"visu",
    r"viņa",
    r"viņu",
    r"viņš",
    r"vācija",
    r"vācu",
    r"vārds",
    r"vēl",
    r"vēlāk",
    r"vēsture",
    r"website",
    r"zemes",
    r"ārējās",
    r"ļoti",
    r"šajā",
    r"šis",
    r"šīs"
]

stopwords = Stopwords(name + ".stopwords", stopwords)
"""
:class:`~revscoring.languages.features.Stopwords` features copied from
"common words" in https://meta.wikimedia.org/w/index.php?diff=13836514
"""

badword_regexes = [
    r"bla",
    r"ble",
    r"bomzis",
    r"bļa",
    r"bļe",
    r"bļeģ",
    r"daunis",
    r"dauņi",
    r"dick",
    r"dildo",
    r"dirsa",
    r"dirsas",
    r"dirst",
    r"dirsu",
    r"dirsā",
    r"diseni",
    r"fuck",
    r"fucking",
    r"gay",
    r"homītis",
    r"huiņa",
    r"idioti",
    r"idiots",
    r"izpisa",
    r"jebal",
    r"jobans",
    r"kaka",
    r"kakas",
    r"kaku",
    r"kroplis",
    r"kuce",
    r"kuces",
    r"loh",
    r"lohi",
    r"lohs",
    r"lohu",
    r"lose",
    r"losene",
    r"losis",
    r"lox",
    r"loxi",
    r"loxs",
    r"mauka",
    r"maukas",
    r"mauku",
    r"nahuj",
    r"nais",
    r"nepiš",
    r"niga",
    r"nigga",
    r"pauti",
    r"pediņi",
    r"pediņš",
    r"peža",
    r"pidaras",
    r"pidarasi",
    r"pidari",
    r"pidars",
    r"pidaru",
    r"pimpi",
    r"pimpis",
    r"pimpja",
    r"pimpji",
    r"pipele",
    r"pirdiens",
    r"piš",
    r"pizda",
    r"pīzda",
    r"pohuj",
    r"porno",
    r"seks",
    r"sex",
    r"shit",
    r"smird",
    r"smirdi",
    r"stulba",
    r"stulbs",
    r"stūlbs",
    r"suck",
    r"suds",
    r"sukaja",
    r"suukaa",
    r"sūda",
    r"sūdi",
    r"sūdiem",
    r"sūds",
    r"sūdu",
    r"sūkā",
    r"sūkāja",
    r"sūkāt"
]

badwords = RegexMatches(name + ".badwords", badword_regexes)
"""
:class:`~revscoring.languages.features.RegexMatches` features via a list of
badword detecting regexes.
"""

informal_regexes = [
    r"arii",
    r"boldā",
    r"cau",
    r"caw",
    r"chau",
    r"dibens",
    r"diseni",
    r"ejat",
    r"ejiet",
    r"fail",
    r"garso",
    r"garšo",
    r"haha",
    r"hello",
    r"jaa",
    r"kko",
    r"kruts",
    r"lol",
    r"nais",
    r"naw",
    r"mēsls",
    r"paldies",
    r"rullē",
    r"stulbi",
    r"sveiki",
    r"swag",
    r"taa",
    r"urlas",
    r"urlu",
    r"vinjam",
    r"vinji",
    r"vinju",
    r"vinsh",
    r"wtf",
    r"yolo",
    r"čalis",
    r"čau"
]

informals = RegexMatches(name + ".informals", informal_regexes)
"""
:class:`~revscoring.languages.features.RegexMatches` features via a list of
informal word detecting regexes.
"""
