import cv2
import os

##Get FPS from Video

# Declar variabel for file name
video = 'video name'

# Get Video with opencv
cam = cv2.VideoCapture(video)

# Get FPS from video
fps = cam.get(cv2.CAP_PROP_FPS)

print(f"FPS from video is = {fps}")

##Convert Video to Image

# Count the Image
frame_count = 0

# Get Video Name
video_name = os.path.splitext(os.path.basename(video))[0]

# Create an output folder with a name corresponding to the video
output_directory = f"../../hasil_video/{video_name}_frames"
os.makedirs(output_directory, exist_ok=True)

while True:
    ret, frame = cam.read()
        
    if not ret:
        break
        
    frame_count += 1
        
    # Only extract frames at the desired frame rate
    if frame_count % int(cam.get(5) / fps) == 0:
        output_file = f"{output_directory}/frame_{frame_count}.jpg"
        cv2.imwrite(output_file, frame)
        print(f"Frame {frame_count} has been extracted and saved as {output_file}")
    
cam.release()
cv2.destroyAllWindows()