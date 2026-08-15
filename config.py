# config.py

# Eye Aspect Ratio threshold (below this = eyes closed)
EAR_THRESHOLD = 0.25

# Number of consecutive frames to trigger alert
FRAME_LIMIT = 20

# Path to model files
SHAPE_PREDICTOR_PATH = "data/shape_predictor_68_face_landmarks.dat"

# Alarm sound file (optional)
ALARM_SOUND_PATH = "data/alarm.wav"