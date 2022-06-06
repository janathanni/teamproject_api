from sqlalchemy import BLOB
from sqlalchemy.orm import Session 

from sqlalchemy.orm import Session

import models, schemas


#AI_Input

#RPi post 
def create_faceimage(db: Session, faceimage : str):
    db_image = models.FaceImage(image = faceimage)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image


#Ai Model get
def get_faceimage(db: Session, user_id: int):
    return db.query(models.FaceImage).filter(models.FaceImage.id == user_id).first()


#Ai Model post
def create_info(db: Session, user_gender:str, user_age:int, user_id:int):
    db_info = models.Info(user_id = user_id, gender=user_gender, age=user_age)
    db.add(db_info)
    db.commit()
    db.refresh(db_info)
    return db_info


#BigData Model get
def get_info(db: Session, user_id : int):
    return db.query(models.Info).filter(models.Info.user_id == user_id).first()