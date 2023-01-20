from pymongo import MongoClient
import pandas as pd
import json
# f=open('./data/data.json','r')
client = MongoClient('mongodb+srv://shwetapatil:shweta19@cluster0.xxd0hpa.mongodb.net/?retryWrites=true&w=majority')
# json.load(f)
df = pd.read_csv('./data/data.csv').to_dict(orient='dict')
# db = client.get_database('myFirstDatabase')
# recipes = db.get_collection('recipes')
# recipes.insert_many([data for data in recipes])
print(df)