
from fastapi import FastAPI
from Main import Main
from Main import stru_json
from Main import json_out
app = FastAPI()

@app.get("/")
async def read_root(s1:str,s3:str,s2:str,distric:str,z:float,bais:float):
  return json_out(stru_json(Main(s1,s3,s2,distric,z,bais)))
   
    