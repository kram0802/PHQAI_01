import streamlit as st
import cv2

def run_dashboard():
    st.title("Hybrid AI + Quantum Dashboard")
    st.write("OpenCV version:", cv2.__version__)
