
from ShahmMusic import Shahmdb


async def put(
    chat_id,
    title,
    duration,
    videoid,
    file_path,
    ruser,
    user_id,
):
    put_f = {
        "title": title,
        "duration": duration,
        "file_path": file_path,
        "videoid": videoid,
        "req": ruser,
        "user_id": user_id,
    }
    get = Shahmdb.get(chat_id)
    if get:
        Shahmdb[chat_id].append(put_f)
    else:
        Shahmdb[chat_id] = []
        Shahmdb[chat_id].append(put_f)
