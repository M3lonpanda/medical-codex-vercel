from fastapi import FastAPI
import pandas as pd 

df = pd.read_csv('./data/diagnoses2018.csv')
app = FastAPI() 

@app.get('/')
async def root():
    return {'this is a API service for MN ICD code details'}

@app.get('/preview')
async def preview():
    top10rows = df.head(1)
    result = top10rows.to_json(orient="records")
    return {result}

@app.get("/age_code/{value}")
async def age_code(value):
    print('value: ', value)
    filtered = df[df['age_group_code'] == value]
    if len(filtered) <= 0:
        return {'There is nothing here'}
    else: 
        return {filtered.to_json(orient="records")}

@app.get('/agecode/{value}/sex/{value2}')
async def agecode2(value, value2):
    filtered = df[df['age_group_code'] == value]
    filtered2 = filtered[filtered['sex'] == value2]
    if len(filtered2) <= 0:
        return {'There is nothing here'}
    else: 
        return {filtered2.to_json(orient="records")}    
    