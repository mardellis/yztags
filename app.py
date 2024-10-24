# app.py
import streamlit as st
import cv2
from PIL import Image
from models.weapon_detection import detect_weapons
from utils.draw_utils import draw_bounding_boxes
from utils.streamlit_utils import create_sidebar, display_video_player

# Set page configuration
st.set_page_config(page_title="AI-Powered Threat Detection", layout="wide")


def main():
    create_sidebar()

    st.title("AI-Powered Threat Detection System")
    st.markdown("Upload your video feed to detect weapons (guns, knives) and analyze anomalies in real-time.")

    # Upload video file
    video_file = st.file_uploader("Upload a video", type=["mp4", "avi"])

    # Video player logic
    video = display_video_player(video_file)
    if video is not None:
        # Read video and process frames
        video_cap = cv2.VideoCapture(video_file.name)
        stframe = st.empty()  # Placeholder for displaying video frames

        while True:
            ret, frame = video_cap.read()
            if not ret:
                break

            # Weapon detection
            weapons_detected = detect_weapons(frame)
            frame = draw_bounding_boxes(frame, weapons_detected)

            # Display frame
            stframe.image(frame, channels="BGR")

            # Count detected weapons
            gun_count = len([weapon for weapon, box in weapons_detected if weapon == 'gun'])
            knife_count = len([weapon for weapon, box in weapons_detected if weapon == 'knife'])

            st.sidebar.write(f"Guns detected: {gun_count}")
            st.sidebar.write(f"Knives detected: {knife_count}")


if __name__ == "__main__":
    main()
