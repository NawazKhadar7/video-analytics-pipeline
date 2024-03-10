import asyncio
async def ingest(queue,frames,drop=False,pace=False):
    discarded=0
    for frame in frames:
        if drop:
            try:queue.put_nowait(frame)
            except asyncio.QueueFull:discarded+=1
        else:await queue.put(frame)
        if pace:await asyncio.sleep(0)
    await queue.put(None);return discarded
