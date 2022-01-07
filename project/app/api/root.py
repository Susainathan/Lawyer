from fastapi import APIRouter, Depends

from app.config import get_settings, Settings

router = APIRouter()



@router.get('/')
def root():
    return {"message":"lawyerapi message"}