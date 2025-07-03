from ultralytics import YOLO
import matplotlib.pyplot as plt
import cv2
import numpy as np

model = YOLO("runs/segment/train/weights/best.pt")

img = cv2.imread("dataset/3_2/image-0045.png")
results = model(img, imgsz=640, iou=0.4, conf=0.7, save=True, device='cpu')

print(results)

def yolo_test_video_detect(model, input_video):
    cap = cv2.VideoCapture(input_video)

    if not cap.isOpened():
        raise Exception('Error: Could not oprn video!')
    
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    while cap.isOpened():
        success, frame = cap.read()

        if success:
            results = model.track(frame, persist=True, iou=0.65, conf=0.70, device='cpu',
                                  tracker='botsort.yaml', imgsz=640, verbose=False)
            annotated_frame = results[0].plot()

            annotated_frame = cv2.resize(annotated_frame, (annotated_frame.shape[1]//2, annotated_frame.shape[0]//2))
            cv2.imshow('YOLOv11 Tracking', annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyWindow()
                break
        else:
            break

    cap.release()

    cv2.destroyWindow()

yolo_test_video_detect(
    model=model,
    input_video='dataset/3_1.MOV'
)
