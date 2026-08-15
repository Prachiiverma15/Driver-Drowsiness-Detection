import cv2
from eye_aspect_ratio import calculate_ear
from alarm import sound_alarm
import dlib

class DrowsinessDetector:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("data/shape_predictor_68_face_landmarks.dat")
        self.counter = 0
        self.threshold = 0.25
        self.frames = 20

    def start(self):
        while True:
            ret, frame = self.cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = self.detector(gray)

            for face in faces:
                landmarks = self.predictor(gray, face)

                ear = calculate_ear(landmarks)

                if ear < self.threshold:
                    self.counter += 1

                    if self.counter >= self.frames:
                        sound_alarm()
                        cv2.putText(frame, "DROWSINESS ALERT!", (50, 50),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                else:
                    self.counter = 0

            cv2.imshow("Drowsiness Detection", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()