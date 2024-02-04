def detections(frame):
    """Synthetic metadata detector; does not infer real video objects."""
    boxes=frame.get('boxes',[])
    for box in boxes:
        if len(box)!=4 or box[2]<=box[0] or box[3]<=box[1]:raise ValueError('invalid box')
    return boxes
