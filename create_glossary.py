from open_csv import open_csv
import pandas as pd



data = open_csv("/Users/carlostubbax-narato/IdeaProjects/reverse_engineering_relational_databases/Test/test1.csv")
df = pd.DataFrame.from_records(data)
print(df)

Tables = []
Primary_keys = []
Normal_datafields = []
Foreign_keys = []
n = len(df)

Tables = list(df["table_name"].unique())


for table in Tables:
    selection = df[df["table_name"]==table]


    n = len(selection)
    normal_datafields = list(selection[(selection["constraint_type"]!= "PRIMARY KEY") & (selection["constraint_type"]!= "FOREIGN KEY")]["column_name"].values)
    normal_datafields = str(normal_datafields)
    Normal_datafields.append(normal_datafields[1:-1].replace("'",""))

    primary_keys = list(selection[(selection["constraint_type"]== "PRIMARY KEY")]["column_name"].values)
    primary_keys = str(primary_keys)
    Primary_keys.append(primary_keys[1:-1].replace("'",""))

    foreign_keys = selection[(selection["constraint_type"]== "FOREIGN KEY")][["table_name-2","column_name-2"]].drop_duplicates()
    #print(foreign_keys)
    if not foreign_keys.empty:
        foreign_key = ''
        for o in list(foreign_keys.index):

            foreign_key += foreign_keys[foreign_keys.index==o]["table_name-2"].values[0] + '(' + foreign_keys[foreign_keys.index==o]["column_name-2"].values[0] + '), '
        foreign_key.replace("'","")
        foreign_key = foreign_key[:-2]
        Foreign_keys.append(foreign_key)
    else:
        Foreign_keys.append('')

glossary = pd.DataFrame([])
glossary['Table'] = Tables
glossary['Primary keys'] = Primary_keys
glossary['Foreign keys'] = Foreign_keys

glossary['Normal datafields'] = Normal_datafields

print(glossary)

#print(Normal_datafields)
#print(len(Normal_datafields))
#print(Primary_keys)
#print(len(Primary_keys))
#print(Foreign_keys)
#print(len(Foreign_keys))
#print(Tables)

#print(data)



