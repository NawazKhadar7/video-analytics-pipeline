"""Optional local-file capture adapter; no pretrained object model."""
import argparse,json

def main():
    import cv2
    p=argparse.ArgumentParser();p.add_argument('video');p.add_argument('--limit',type=int,default=100);args=p.parse_args()
    if args.limit<1:raise ValueError('limit must be positive')
    cap=cv2.VideoCapture(args.video)
    if not cap.isOpened():raise OSError('cannot open local video')
    count=0
    try:
        while count<args.limit:
            ok,frame=cap.read()
            if not ok:break
            count+=1
        print(json.dumps({'decoded_frames':count,'detection_performed':False}))
    finally:cap.release()
if __name__=='__main__':main()
