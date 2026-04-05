import numpy as np
import pandas as pd

from src.config import SEED, regions, cities, city_to_state, names

def build_locations_df(seed: int = SEED) -> pd.DataFrame:
    np.random.seed(seed)

rows = []
for region,city_list in cities.items():
    for city,lat,lon in city_list:
        rows.append({
            "Region": region,
            "Ort": city,
            "lat": lat,
            "lon": lon
        })
        
df_locations = pd.DataFrame(rows)
df_locations["Bundesland"] = df_locations["Ort"].map(city_to_state)

# Nun Einwohnerzahl anhand lognormal-Verteilung generieren
df_locations["Einwohner"] = np.random.lognormal(
    mean = 9,
    sigma = 0.5,
    size = len(df_locations)
).astype(int)
df_locations["Einwohner"] = df_locations["Einwohner"].clip(5000,15000)

# Alpha-Werte für Makroregionen bestimmen 
alpha_base = np.ones(K)
region_alphas = {}
def build_region_alphas(names, dominance = 5.0, moderate = 3.0):
    freq = np.array([
        256003,
        190854,
        115749,
        97658,
        83586,
        86061,
        73736,
        79732,
        74009,
        42872,
        61591,
        59927,
        50648,
        59950,
        58903
    ])
    alpha_base = freq / freq.max()
    alpha_national = alpha_base * 50 
    
    region_alphas = {}
    
    
    for r in regions:
        alpha = alpha_national.copy()
        if r == "Nord":
            alpha[names.index("Schröder")] *= dominance
            alpha[names.index("Schmidt")] *= moderate
            
        elif r == "Bayern":
            alpha[names.index("Bauer")] *= dominance
            alpha[names.index("Meyer")] *= moderate
            
        elif r == "Ost":
            alpha[names.index("Richter")] *= dominance
            alpha[names.index("Schulz")] *= moderate
            
        elif r == "Rheinland":
            alpha[names.index("Becker")] *= dominance
            alpha[names.index("Schäfer")] *= moderate
            
        elif r == "Schwaben":
            alpha[names.index("Zimmermann")] *= dominance
            alpha[names.index("Becker")] *= moderate
            
        elif r == "West":
            alpha[names.index("Schneider")] *= dominance
            alpha[names.index("Weber")] *= moderate   
        region_alphas[r] = alpha 
    return region_alphas
region_alphas = build_region_alphas(names)

def simulate_micro_data(df_locations, names_current, beta_value: float, seed: int = SEED):
    np.random.seed(seed)
    region_alphas = build_region_alphas(names_current)

rows = []
for i,row in df_locations.iterrows():
    
    region = row["Region"]
    city = row["Ort"]
    state = row["Bundesland"]
    pop = row["Einwohner"]
    theta_regions = {
        r: np.random.dirichlet(region_alphas[r])
        for r in regions
    } 
    theta_region = theta_regions[region]
    theta_city = np.random.dirichlet(beta * theta_region)

    persons = np.random.choice(
        names,
        size = pop,
        p = theta_city
    )
    for name in persons:
        rows.append([
            region,
            city,
            state,
            row["lat"],
            row["lon"],
            name
        ])

return pd.DataFrame(
        rows,
        columns = ["Region", "Ort", "Bundesland", "lat", "lon", "Nachname"]
    )

def micro_to_relative(df_micro: pd.DataFrame) -> pd.DataFrame:
    df_agg = (
        df_micro
        .groupby(["Ort", "Nachname"])
        .size()
        .unstack(fill_value = 0)
    )
    return df_agg.div(df_agg.sum(axis = 1), axis = 0)