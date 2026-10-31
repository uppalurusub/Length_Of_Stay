import streamlit as st
from components.sidebar import render_sidebar
from components.request_form import render_form
from components.response_view import show_response
from api.los_api import predict
def render():
    st.title("Hospital Length of Stay Prediction")
    render_sidebar()
    submitted,payload=render_form()
    if submitted:
        try:
            show_response(predict(payload))
        except Exception as e:
            st.error(str(e))
