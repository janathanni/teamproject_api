from typing import List

from fastapi import Depends, FastAPI, File, UploadFile
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

#pip install fastapi
#pip install uvicorn
#pip install sqlalchemy

models.Base.metadata.create_all(bind=engine)
#Android에서 retrofit 설치하기 ^^..

#uvicorn main:app --reload

#AI_input for get by model

# Dependency
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/face-image/", response_model = schemas.FaceImageCreate)
async def create_image(faceimage: str, db:Session=Depends(get_db)):
    rps = crud.create_faceimage(db=db, faceimage=faceimage)
    return rps

@app.post("/info/", response_model = schemas.InfoCreate)
async def create_info(user_id : int, user_gender: str, user_age : int, db: Session = Depends(get_db)):
    return crud.create_info(db = db, user_id=user_id, user_gender=user_gender, user_age=user_age)

@app.post("/recommendation/", response_model = schemas.AI_OutPut)
async def create_aioutput(output : Ai_Output):
    pass

@app.post("/ad/", response_model = schemas.AI_OutPut)
async def create_aioutput(output : Ai_Output):
    return output

