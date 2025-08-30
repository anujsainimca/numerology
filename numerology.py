import streamlit as st
import requests

st.title("Numerology Traits Generator 🔮")

# Inputs
name = st.text_input("Enter your Name")
dob = st.date_input("Enter your Date of Birth")

if st.button("Generate Traits"):
    payload = {"name": name, "dob": str(dob)}
    response = requests.post("https://asaini.app.n8n.cloud/webhook-test/81ba8d0a-aef1-4d23-99f9-f41da180e377", json=payload)

    if response.status_code == 200:
        st.subheader("Your Numerology Traits")
        st.write(response)
    else:
        st.error("Something went wrong!")
