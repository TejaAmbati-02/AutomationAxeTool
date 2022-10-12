import pandas as pd
df_json = pd.read_json("C:\\Users\\teja.sai.k.ambati\\PycharmProjects\\Automation\\axeIntegration.json")
df_json.to_excel('DATAFILE.xlsx')
