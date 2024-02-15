import asyncio
from .common import validate_case
from .tracker import Tracker
from .ingestion import ingest
from .detection import detections
FAMILIES=('steady','crossing','overload','missing','bursty','occlusion')
async def execute(case):
    streams=case['size'];family=case['family'];frames=[]
    for tick in range(12):
        for stream in range(streams):
            x=5+tick*2;boxes=[[x,5,x+12,17]]
            if family=='crossing':boxes.append([50-tick*2,30,62-tick*2,42])
            if family in ('missing','occlusion') and tick%4==0:boxes=[]
            frames.append({'stream':stream,'tick':tick,'boxes':boxes})
    queue=asyncio.Queue(maxsize=4);trackers={i:Tracker() for i in range(streams)};events=[];processed=0;boxes_total=0
    producer=asyncio.create_task(ingest(queue,frames,drop=family=='overload',pace=family not in ('bursty','overload')))
    while True:
        frame=await queue.get()
        if frame is None:break
        processed+=1;boxes=detections(frame);boxes_total+=len(boxes);tracks=trackers[frame['stream']].update(boxes,frame['tick'])
        for track in tracks:
            center=(track['box'][0]+track['box'][2])/2
            if 24<=center<=26:events.append({'stream':frame['stream'],'tick':frame['tick'],'track':track['id'],'event':'line-region'})
        await asyncio.sleep(0)
    dropped=await producer
    return {'metrics':{'produced':len(frames),'processed':processed,'dropped':dropped,'accounted':processed+dropped==len(frames),'detections':boxes_total,'alerts':len(events),'queue_capacity':4},'output':events[:12]}
def run_case(case):
    validate_case(case)
    if case['family'] not in FAMILIES:raise ValueError('unknown video family')
    return asyncio.run(execute(case))
