def draw_text(frame, text, x, y):
    import cv2
    cv2.putText(frame, text, (x, y),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)