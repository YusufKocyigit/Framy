#pip install opencv-python
import cv2
import os

while True:
    # Prompt the user to input the video file path or link
    video_path = input("Enter the video file path or link (or type 'exit' to quit): ")
    
    if video_path.lower() == 'exit':
        break  # Exit the loop if the user enters 'exit'

    # Open the video file
    video_capture = cv2.VideoCapture(video_path)

    # Extract the video name without the extension
    video_name = os.path.splitext(os.path.basename(video_path))[0]

    # Create a directory to save the frames for this video
    video_frame_directory = os.path.join('extracted', video_name)
    if not os.path.exists(video_frame_directory):
        os.makedirs(video_frame_directory)

    frame_count = 0

    while True:
        # Read a frame from the video
        ret, frame = video_capture.read()

        # If there are no more frames to read, break the inner loop
        if not ret:
            break

        # Save the frame as an image (you can choose the format, e.g., 'frame{:04d}.jpg')
        frame_filename = os.path.join(video_frame_directory, f'{frame_count:04d}.jpg')
        cv2.imwrite(frame_filename, frame)

        frame_count += 1

    # Release the video capture object
    video_capture.release()

    print(f"Extracted {frame_count} frames from '{video_name}'.")

print("Exiting the program.")
