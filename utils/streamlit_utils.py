# utils/streamlit_utils.py
import streamlit as st


def create_sidebar():
    st.sidebar.image("assets/logo.png", use_column_width=True)
    st.sidebar.title("AI-Powered Threat Detection")
    st.sidebar.markdown(
        "Upload a video file or use live stream (coming soon) to detect weapons and anomalies in real-time.")


def display_video_player(video_file):
    if video_file is not None:
        return video_file
    else:
        st.error("Please upload a video file.")
        return None
