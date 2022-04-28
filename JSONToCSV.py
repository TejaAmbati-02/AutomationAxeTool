import pandas as pd
import os


path =""
for filename in os.listdir(path):
    root, ext = os.path.splitext(filename)
    if ext == '.json':
        frame = pd.read_json(filename)
        frame.to_csv(root + '.csv', index=False)