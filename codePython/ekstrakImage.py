import cv2
cam = cv2.VideoCapture('/home/apriyanto/Documents/video/video/archive/J-EDI20240607105034/2K0570OUTSV1019.mp4')
fps = cam.get(cv2.CAP_PROP_FPS)
print(fps)