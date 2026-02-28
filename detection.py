import cv2
import os
import imutils
import time

def operate_camera(index):
	cam = cv2.VideoCapture(index)
	firstframe = None
	os.makedirs("camera0", exist_ok = True)
	n = 0
	photo = 0
	while cam.isOpened():
		ret, frame = cam.read()

		frame = imutils.resize(frame, width=500)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		gray = cv2.GaussianBlur(gray, (21, 21),  0)
		if firstframe is None:
			firstframe = gray
			continue
		
		framedif = cv2.absdiff(firstframe, gray)
		thresh = cv2.threshold(framedif, 25, 255, cv2.THRESH_BINARY)[1]
		thresh = cv2.dilate(thresh, None, iterations=2)
		cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)
		motion = False
		for c in cnts:
			if cv2.contourArea(c) < 800:
				continue
			motion = True
			(x, y, w, h) = cv2.boundingRect(c)
			cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
		curtime = time.time()
		if motion and (curtime - photo > 3):
			n += 1
			cv2.imwrite(f"camera0\\img{n}.png", frame)
			photo = curtime
		if cv2.waitKey(1) == ord('q') or ret == 0:
			break
		cv2.imshow("Camera", frame)
		if cv2.waitKey(1) == ord('s'):
			n += 1
			cv2.imwrite(f"camera0\\img{n}.png", frame)
	cam.release()
	cv2.destroyAllWindows()
if __name__ == "__main__":
	operate_camera(0)
