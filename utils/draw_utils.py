# utils/draw_utils.py
import cv2

def draw_bounding_boxes(frame, weapons_detected):
    for weapon, box in weapons_detected:
        x1, y1, x2, y2 = map(int, box)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Green for detected weapons
        cv2.putText(frame, weapon, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    return frame
