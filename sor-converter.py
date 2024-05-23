import pandas as pd

def get_hierarchy(id):
    return len(str(id).split("."))

def get_quantity(x):
    return 1

def set_flat_hierarchy(x):
    return 1


path = "./EPU_prezzario2023.ods"

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

df = df[df.Value.notnull()]

df["Hierarchy"] = df["Identification"].apply(set_flat_hierarchy)

#df = df.head(5760)

df = df.replace("%", "perc")
df = df.replace("m³", "mc")
df = df.replace("m²", "mq")
df = df.replace("dm²", "dmq")
df = df.replace("dm³", "dmc")
df = df.replace("m²*cm", "mq*cm")
df = df.replace("m²/me", "mq/me")
df = df.replace("m²*h", "mq*h")
df = df.replace("m²*mm", "mq*mm")
df = df.replace("m²cm", "mqcm")
df = df.replace("m²x gg", "mq x gg")
df = df.replace("m²/mese", "mq/mese")
df = df.replace("m³ x km", "mc x km")
df = df.replace("m³vpp", "mc vpp")
df = df.replace("m³/me", "mc/me")
df = df.replace(r'^\s*$', "cad..", regex=True)

print(df.columns)
print(df.head())
print(df.dtypes)

df.to_csv("./EPU_prezzario2023.csv", index = False)


