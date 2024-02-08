def iou(a,b):
    x=max(0,min(a[2],b[2])-max(a[0],b[0]));y=max(0,min(a[3],b[3])-max(a[1],b[1]))
    intersection=x*y;area=(a[2]-a[0])*(a[3]-a[1])+(b[2]-b[0])*(b[3]-b[1])-intersection
    return intersection/area if area>0 else 0
class Tracker:
    def __init__(self,threshold=.2,max_age=3):self.threshold=threshold;self.max_age=max_age;self.tracks={};self.next_id=1
    def update(self,boxes,tick):
        self.tracks={k:v for k,v in self.tracks.items() if tick-v['tick']<=self.max_age};available=set(self.tracks);output=[]
        for box in boxes:
            ranked=sorted(((iou(box,self.tracks[k]['box']),k) for k in available),reverse=True)
            if ranked and ranked[0][0]>=self.threshold:identity=ranked[0][1];available.remove(identity)
            else:identity=self.next_id;self.next_id+=1
            self.tracks[identity]={'box':box,'tick':tick};output.append({'id':identity,'box':box})
        return output
