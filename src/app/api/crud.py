from app.api.models import YTSchema
from app.database import yt, database
from datetime import datetime as dt


async def post(payload: YTSchema):
    timestamp = dt.now().strftime("%Y-%m-%d %H:%M")
    query = yt.insert().values(url_list=payload.url_list, 
    vid_title=payload.vid_title, videoID=payload.videoID, timestamp=timestamp)
    return await database.execute(query=query)

async def get(id: int):
    query = yt.select().where(id == yt.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = yt.select()
    return await database.fetch_all(query=query)


async def put(id:int, payload=YTSchema):
    timestamp = dt.now().strftime("%Y-%m-%d %H:%M")
    query = (
        yt.update().where(id == yt.c.id).values(url_list=payload.url_list, 
        vid_title=payload.vid_title, videoID=payload.videoID, timestamp=timestamp)
        .returning(yt.c.id)
    )
    return await database.execute(query=query)

async def delete(id:int):
    query = yt.delete().where(id == yt.c.id)
    return await database.execute(query=query)