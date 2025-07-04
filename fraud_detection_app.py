import streamlit as st
import pandas as pd
import joblib

model = joblib.load('fraud_detection_model.pkl')