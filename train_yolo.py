from ultralytics import YOLO


model = YOLO('yolo11s-seg.pt')

results = model.train(data='YOLO_dataset/data.yaml', epochs=2, imgsz=640, batch=16)