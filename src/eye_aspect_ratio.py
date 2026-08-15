from scipy.spatial import distance

def calculate_ear(landmarks):
    # Extract eye coordinates (example indices)
    left_eye = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(36, 42)]

    A = distance.euclidean(left_eye[1], left_eye[5])
    B = distance.euclidean(left_eye[2], left_eye[4])
    C = distance.euclidean(left_eye[0], left_eye[3])

    ear = (A + B) / (2.0 * C)
    return ear