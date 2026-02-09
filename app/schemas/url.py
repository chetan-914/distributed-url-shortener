from pydantic import BaseModel, HttpUrl

class UrlCreateRequest(BaseModel):
    long_url: HttpUrl

class UrlCreateResponse(BaseModel):
    short_url: str