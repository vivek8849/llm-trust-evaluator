import streamlit as st
import requests

API_URL = "http://api:8000/evaluate"  # Docker service name

st.title("🧠 LLM Trust Evaluation Framework")

prompt = st.text_input("Enter your question:")

if st.button("Evaluate Trust"):

    if not prompt:
        st.warning("Please enter a prompt.")
    else:
        try:
            response = requests.post(API_URL, json={"prompt": prompt})
            result = response.json()

            st.subheader("Results")

            st.write("Consistency:", result["consistency"])
            st.write("Vulnerability:", result["vulnerability"])
            st.write("Trust Score:", result["trust_score"])
            st.write("Risk Level:", result["risk_level"])
            st.write("Decision:", result["decision"])

            st.subheader("Model Responses")
            for r in result["responses"]:
                st.write("-", r)

            st.subheader("Self-Critique")
            st.write(result["critique"])

        except Exception as e:
            st.error(f"Connection error: {e}")