from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Score(BaseModel):
    name: str
    score: int
    total: int

LEADERS: List[Score] = []

@app.get("/leaders")
def get_leaders():
    sorted_list = sorted(LEADERS, key=lambda x: x.score, reverse=True)[:10]
    return [l.dict() for l in sorted_list]

@app.post("/score")
def add_score(score: Score):
    LEADERS.append(score)
    return {"status": "ok"}
