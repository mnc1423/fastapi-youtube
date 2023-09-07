
from pydantic import BaseModel, Field, NonNegativeInt
from datetime import datetime as dt
from pytz import timezone as tz

class YTSchema(BaseModel):
    url_list: str = Field(..., min_length=3, max_length=50) #additional validation for the inputs 
    vid_title: str = Field(...,min_length=3, max_length=50)
    videoID: str = Field(...,min_length=3, max_length=50)
    timestamp: str = Field(...,min_length=3, max_length=50)

class YTDB(YTSchema):
    id: int 