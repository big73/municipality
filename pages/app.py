import streamlit as st
from utils.downloader import download_csv

download_csv()

st.write("done")