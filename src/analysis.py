import numpy as np
import pandas as pd
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score, adjusted_rand_score, accuracy_score, classification_report, confusion_matrix, normalized_mutual_info_score, silhouette_samples
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import geopandas as gpd
import seaborn as sns
import pprint
import matplotlib as mpl
import matplotlib.lines as mlines
from scipy.spatial import ConvexHull
from sklearn.neighbors import NearestNeighbors
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from scipy.spatial.distance import jensenshannon

def shannon_entroy(probs) -> float:
    probs = np.asarray(probs, dtype = float)
    probs = probs[probs > 0]
    return -np.sum(probs * np.log(probs))

def gini_coefficient(values) -> float:
    values = np.asarray(values, dtype = float)
    if np.amin(values) < 0:
        values = values - np.amin(values)
    if np.sum(values) == 0:
        return 0.0
    values = np.sort(values)
    n = len(values)
    index = np.arange(1, n+ 1)
    return np.sum((2 * index - 1) * values) / (n * np.sum(values))

def compute_region_js_matrix(df_rel: pd.DataFrame, df_locations: pd.DataFrame):
    df_tmp = df_rel.copy()
    df_tmp["Ort"] = df_tmp.index

    df_tmp = df_tmp.merge(
        df_locations[["Ort", "Region"]],
        on = "Ort",
        how = "left"
    )

    name_cols = [c for c in df_tmp.columns if c not in ["Ort", "Regiom"]]

    df_region = (
        df_tmp.groupby("Region")[name_cols]
        .mean()
    )

    region_names = list(df_region.index)
    n = len(region_names)
    js_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            js_matrix[i, j] = jensenshannon(
                df_region.iloc[i].values,
                df_region.iloc[j].values
            )
    return js_matrix, region_names

def compute_mean_js(df_rel: pd.DataFrame, df_locations: pd.DataFrame) -> float:
    js_matrix, _ = compute_region_js_matrix(df_rel, df_locations)
    upper = js_matrix[np.triu_indices(len(js_matrix), 1)]
    return upper.mean()

def run_kmeans(df_rel: pd.Dataframe, k_values, seed: int = 42) -> pd.DataFrame:
    rows = []
    for k in k_values:
        model = KMeans(n_clusters = k, n_init = 50, random_state = seed)
        labels = model.fit_predict(df_rel)
        sil = silhouette_score(df_rel, labels)
        rows.append({"k": k, "Silhouette": sil})
    return pd.DataFrame(rows)

def run_svm(df_rel: pd.DataFrame, df_locations: pd.DataFrame, seed: int = 42):
    X = df_rel.copy()
    y = df_locations.set_index("Ort").loc[df_rel.index]["Region"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size = 0.3,
        random_state=seed, 
        stratify=y
    )

    svm = SVC(kernel="rbf", gamma="scale")
    svm.fit(X_train, y_train)
    pred = svm.predict(X_test)

    return {
        "model": svm, 
        "X_train": X_train,
        "X_test": X_test,
        "y_train": y_train,
        "y_test": y_test,
        "pred": pred, 
        "accuracy": accuracy_score(y_test, pred),
        "report": classification_report(y_test, pred),
        "cm": confusion_matrix(y_test, pred)
    }