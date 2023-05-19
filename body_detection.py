import cv2
import mediapipe as mp

model = mp.solutions.pose.Pose(static_image_mode=False, min_detection_confidence=0.5,
	min_tracking_confidence=0.5)

cap = cv2.VideoCapture("files/Cristiano.mp4")

while True:
	ret, frame = cap.read()

	if ret:
		width, height = frame.shape[1], frame.shape[0]
		frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

		lm = model.process(frame_rgb).pose_landmarks
		
		if lm: # if lm was not NAN
			# print(lent(lm))
			# print(len(lm.landmark)) # 33
			for point in lm.landmark:
				lm0 = point.x, point.y
				cv2.circle(frame, (int(lm0[0]*width), int(lm0[1]*height)), 3, (255, 255, 255), cv2.FILLED) 

		cv2.imshow("Cristiano", frame)
		q = cv2.waitKey(1) # frame rate

		if q == ord('q'):
			break
	else:
		break

cap.release()
cv2.destroyWindow("Cristiano")
