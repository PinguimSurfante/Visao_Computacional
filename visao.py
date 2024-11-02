import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# O video
video = cv2.VideoCapture('video de sua preferencia')

# Leitura
ok, frame = video.read()


while True:
    ok, frame = video.read()
    if not ok:
        break

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = pose.process(image_rgb)

    if results.pose_landmarks:
        mp.solutions.drawing_utils.draw_landmarks(frame,results.pose_landmarks,mp_pose.POSE_CONNECTIONS)

    cv2.imshow('Pose Estimation', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break