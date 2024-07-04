
from fastapi import FastAPI
from Course import Main
from Course import stru_json
from Course import json_out
from Marks_Guess import out_str
from Marks_Guess import guess_es
app = FastAPI()

@app.get("/course")
async def read_root(s1:str,s3:str,s2:str,distric:str,z:float,bais:float):
  return stru_json(Main(s1,s3,s2,distric,z,bais))


@app.get("/guess")
async def guess_the(z: float, syb1: str, syb2: str, syb3: str, math: bool):
    return  out_str(guess_es(z, syb1, syb2, syb3, math))

