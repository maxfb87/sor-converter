import pandas as pd

def get_hierarchy(id):
    return len(str(id).split("."))

def get_quantity(x):
    return 1

path = "./EPU_prezzario2013.ods"

map = {
    "Codice" : "Identification",
    "Descrizione" : "Name",
    "UMI" : "Unit",
    "Prezzo" : "Value",
}

df = pd.read_excel(path, engine="odf", dtype = {"Codice" : str})

df = df.rename(columns = map)

df = df.drop(["% Man."], axis = 1)

df["Hierarchy"] = df["Identification"].apply(get_hierarchy)

df["Quantity"] = df["Identification"].apply(get_quantity)

df = df.reindex(columns = ["Hierarchy", "Identification", "Name", "Quantity", "Unit", "Value"])

df = df.head(56)

print(df.columns)
print(df.head())
print(df.dtypes)

df.to_csv("./EPU_prezzario2013.csv", index = False)


