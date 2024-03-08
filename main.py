from typing import Optional, List, Dict

from fastapi import FastAPI
import pandas as pd

app = FastAPI()

pb = pd.read_csv('publishers.csv' )  
print(type(pb.to_dict()))



@app.get("/")
<<<<<<< HEAD
async def root() -> List[Dict]:
    pb = pd.read_csv('publishers.csv')    
    # list(pb.to_dict())
    return pb.iloc[:10,:].to_dict(orient='records')
    # return {"message": "Hola Mundo!!!"}
=======
async def root():
    return {"message": "Hola Grupo"}
>>>>>>> 08127174765c0615cc103ad061bde0d58ece83f3

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
