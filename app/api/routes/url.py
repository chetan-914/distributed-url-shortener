from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.schemas.url import UrlCreateRequest, UrlCreateResponse
from app.core.database import get_db
from app.services.url_service import create_short_url, get_long_url

router = APIRouter()

@router.post("/urls", response_model=UrlCreateResponse)
def create_url(
    payload: UrlCreateRequest,
    db: Session = Depends(get_db)
):
    short_url = create_short_url(db, str(payload.long_url))
    return UrlCreateResponse(short_url=short_url)

@router.get("/{short_code}")
def redirect_url(
    short_code: str,
    db: Session = Depends(get_db)
):
    long_url = get_long_url(db, short_code)

    if not long_url:
        raise HTTPException(status_code=404, detail="URL not found")
    
    return RedirectResponse(long_url)