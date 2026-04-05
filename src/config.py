SEED = 42

names = [
    "Müller", "Schmidt", "Schneider", "Fischer", "Meyer",
    "Weber", "Schulz", "Wagner", "Becker", "Zimmermann", 
    "Schäfer", "Koch", "Schröder", "Richter", "Bauer"
    
]

names2 = [
    "Hoffmann", "Krüger", "Keller", "Winkler", "Köhler",
    "Baumann", "Schuhmacher", "Schuster", "Jäger", "Kaufmann",
    "Schreiber", "Bergmann", "Krämer", "Ziegler", "Maurer"
]

names3 = [
    "Berger", "Pfeiffer", "Fiedler", "Förster", "Schütz",
    "Schindler", "Böttcher", "Gärtner", "Ackermann", "Geiger",
    "Fuhrmann", "Krieger", "Schreiner", "Fleischer", "Glaser"
]

name_sets = {
    15: names,
    30: names + names2,
    45: names + names2 + names3
}

# Regionen 

regions = [
    "Nord", "Rheinland", "Bayern",
    "West", "Schwaben", "Ost"
    
]

# Städte

cities ={

"Nord": [
    ("Hannover",52.37,9.72),
    ("Braunschweig",52.27,10.52),
    ("Bremen",53.08,8.80),
    ("Hamburg",53.55,10.00),
    ("Kiel",54.32,10.14),
    ("Lübeck",53.87,10.69),
    ("Rostock",54.09,12.14),
    ("Schwerin",53.63,11.41)    
],
    
"Ost":[
    ("Potsdam",52.39,13.06),
    ("Frankfurt (Oder)",52.35,14.55),
    ("Dresden",51.05,13.74),
    ("Leipzig",51.34,12.37),
    ("Magdeburg",52.13,11.63),
    ("Halle (Saale)",51.48,11.97),
    ("Erfurt",50.98,11.03),
    ("Berlin",52.52,13.40)
],
    
"West":[
    ("Köln",50.94,6.96),
    ("Münster", 51.96,7.63),
    ("Bonn",50.74,7.10),
    ("Gelsenkirchen",51.52,7.09),
    ("Frankfurt (Main)",50.11,8.68),
    ("Wiesbaden",50.08,8.24),
    ("Kassel",51.31,9.49),
    ("Marburg",50.81,8.77)
], 
    
"Rheinland":[
    ("Koblenz",50.36,7.60),
    ("Mainz",49.99,8.27),
    ("Trier",49.75,6.64),
    ("Cochem",50.15,7.17),
    ("Saarbrücken",49.23,7.00),
    ("Saarlouis",49.31,6.75),
    ("Weiskirchen",49.55,6.82),
    ("St. Ingbert",49.28,7.11)
],
    
"Bayern":[
    ("München",48.13,11.58),
    ("Nürnberg",49.45,11.08),
    ("Würzburg",49.79,9.95),
    ("Passau",48.57,13.46),
    ("Augsburg",48.37,10.90),
    ("Regensburg",49.02,12.10),
    ("Ingolstadt",48.76,11.42),
    ("Füssen",47.57,10.70),
],
    
"Schwaben":[
    ("Heidelberg",49.41,8.69),
    ("Mannheim",49.49,8.47),
    ("Stuttgart",48.78,9.18),
    ("Freiburg",47.99,7.85),
    ("Heilbronn",49.14,9.22),
    ("Tübingen",48.52,9.06),
    ("Konstanz",47.66,9.17),
    ("Ulm",48.40,10.00)
]

}

city_to_state = {
    "Hamburg": "Hamburg",
    "Kiel": "Schleswig-Holstein",
    "Lübeck": "Schleswig-Holstein",
    "Bremen": "Bremen",
    "Hannover": "Niedersachsen",
    "Braunschweig": "Niedersachsen",
    "Rostock": "Mecklenburg-Vorpommern",
    
    "Berlin": "Berlin",
    "Potsdam": "Brandenburg",
    "Frankfurt (Oder)": "Brandenburg",
    "Dresden": "Sachsen", 
    "Leipzig": "Sachsen",
    "Magdeburg": "Sachsen-Anhalt",
    "Halle (Saale)": "Sachsen-Anhalt",
    "Erfurt": "Thüringen",
    
    "Köln": "Nordrhein-Westfalen",
    "Münster": "Nordrhein-Westfalen", 
    "Bonn": "Nordrhein-Westfalen",
    "Gelsenkirchen": "Nordrhein-Westfalen",
    "Frankfurt (Main)": "Hessen",
    "Wiesbaden": "Hessen", 
    "Kassel": "Hessen",
    "Marburg": "Hessen",
    
    "Mainz": "Rheinland-Pfalz",
    "Trier": "Rheinland-Pfalz",
    "Koblenz": "Rheinland-Pfalz",
    "Cochem": "Rheinland-Pfalz",
    "Saarbrücken": "Saarland",
    "Saarlouis": "Saarland",
    "Weiskirchen": "Saarland",
    "St. Ingbert": "Saarland", 
    
    "München": "Bayern",
    "Nürnberg": "Bayern", 
    "Würzburg": "Bayern",
    "Passau": "Bayern",
    "Augsburg": "Bayern",
    "Regensburg": "Bayern",
    "Ingolstadt": "Bayern",
    "Füssen": "Bayern",
    
    "Stuttgart": "Baden-Württemberg",
    "Heidelberg": "Baden-Württemberg",
    "Mannheim": "Baden-Württemberg", 
    "Freiburg": "Baden-Württemberg", 
    "Heilbronn": "Baden-Württemberg",
    "Tübingen": "Baden-Württemberg", 
    "Konstanz": "Baden-Württemberg",
    "Ulm": "Baden-Württemberg"
}
