from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Разрешаем запросы с фронта (GitHub Pages)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # потом можно ограничить https://portgas1996.github.io
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Score(BaseModel):
    name: str
    score: int
    total: int

LEADERS: List[Score] = []

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/leaders")
def get_leaders():
    sorted_list = sorted(LEADERS, key=lambda x: x.score, reverse=True)[:10]
    return [l.dict() for l in sorted_list]

@app.post("/score")
def add_score(score: Score):
    LEADERS.append(score)
    return {"status": "ok"}
