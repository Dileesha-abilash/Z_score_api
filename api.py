
from fastapi import FastAPI
from Main import Main
from Main import stru_json
from Main import json_out
from guess import out_str
from guess import guess_es
app = FastAPI()

@app.get("/")
async def read_root(s1:str,s3:str,s2:str,distric:str,z:float,bais:float):
  return stru_json(Main(s1,s3,s2,distric,z,bais))


@app.get("/guess")
async def guess_the(z: float, syb1: str, syb2: str, syb3: str, math: bool):
    return  out_str(guess_es(z, syb1, syb2, syb3, math))

@app.get("/guess2")
async def read_root2():
  return "hellp"
