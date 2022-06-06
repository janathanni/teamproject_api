from typing import List

from fastapi import Depends, FastAPI, File, UploadFile
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

import base64

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

# @app.post("/face-image/", response_model = schemas.FaceImageCreate)
# async def create_image(faceimage: str, db:Session=Depends(get_db)):
#     rps = crud.create_faceimage(db=db, faceimage=faceimage)
#     return rps

# @app.get("/face-image/{id}", response_model = schemas.FaceImageCreate)
# async def read_image(id: int, db: Session = Depends(get_db)):
#     db_image = crud.get_faceimage(db = db, user_id = id)
#     return db_image

@app.post("/face-image/", response_model = schemas.FaceImageCreate)
async def create_image(faceimage: str, db:Session=Depends(get_db)):
    
    rps = crud.create_faceimage(db=db, faceimage=faceimage)
    return rps

@app.get("/face-image/{id}", response_model = schemas.FaceImageCreate)
async def read_image(id: int, db: Session = Depends(get_db)):
    db_image = crud.get_faceimage(db = db, user_id = id)
    return db_image

@app.post("/info/", response_model = schemas.InfoCreate)
async def create_info(user_id : int, user_gender: str, user_age : int, db: Session = Depends(get_db)):
    return crud.create_info(db = db, user_id=user_id, user_gender=user_gender, user_age=user_age)

@app.get("/info/{user_id}", response_model = schemas.InfoCreate)
async def get_info(user_id : int, db: Session = Depends(get_db)):
    return crud.get_info(db=db, user_id = user_id)


# @app.post("/recommendation/", response_model = schemas.AI_OutPut)
# async def create_aioutput(output : Ai_Output):
#     pass

# @app.get("/recmmenddation/{user_id}", response_model = schemas.AI_input_Create)
# async def read_image(user_id: int, db: Session = Depends(get_db)):
#     # db_image = crud.get_image_by_id(db, user_id = user_id)
#     pass

# @app.post("/ad/", response_model = schemas.AI_OutPut)
# async def create_aioutput(output : Ai_Output):
#     return output

# @app.get("/ad/{user_id}", response_model = schemas.AI_input_Create)
# async def read_image(user_id: int, db: Session = Depends(get_db)):
#     db_image = crud.get_image_by_id(db, user_id = user_id)

#     return db_image