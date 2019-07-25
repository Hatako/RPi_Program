import cv2

def camera_capture():
	cap = cv2.VideoCapture(0)

	while True:
		ret, frame = cap.read()
		cv2.imshow('camera capture', frame)
		key = cv2.waitKey(1)
		if key == 27:
			break

	cap.release()
	cv2.destroyAllWindows()

if __name__=='__main__':
	camera_capture()
