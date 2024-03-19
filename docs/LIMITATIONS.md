# Limitations

Default frames contain synthetic boxes, not images, audio or pretrained detections. There is no YOLO, INT8 inference, Kafka, WebSocket transport or GPU validation. Steady producers yield between frames; burst producers push until backpressure blocks them. IoU matching is greedy and cannot reliably resolve severe occlusion. A finite queue must backpressure or drop under overload.
