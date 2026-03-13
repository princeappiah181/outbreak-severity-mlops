import streamlit as st
import requests

API_URL = "https://outbreak-severity-api.onrender.com/predict"

st.set_page_config(
    page_title="Outbreak Severity Predictor",
    page_icon="🦠",
    layout="centered"
)

st.title("🦠 Outbreak Severity Predictor")

# ---- ADD API STATUS CHECK HERE ----
health_url = "https://outbreak-severity-api.onrender.com/health"

try:
    r = requests.get(health_url, timeout=5)
    if r.status_code == 200:
        st.success("API Status: Online")
    else:
        st.warning("API Status: Waking up...")
except:
    st.warning("API Status: Connecting...")
# ----------------------------------

st.markdown(
    "Enter an outbreak report below to predict whether the outbreak is **severe** or **not severe**."
)

report_text = st.text_area(
    "Outbreak Report",
    height=180,
    placeholder="Example: Ebola outbreak reported with 350 deaths and rapid spread across multiple regions."
)




if st.button("Predict Severity", use_container_width=True):
    if not report_text.strip():
        st.warning("Please enter an outbreak report.")
    else:
        payload = {"report": report_text}

        try:
            with st.spinner("Generating prediction..."):
                response = requests.post(API_URL, json=payload, timeout=60)

            if response.status_code == 200:
                result = response.json()

                severity_prediction = result.get("severity_prediction")
                probability_severe = result.get("probability_severe")

                st.success("Prediction completed successfully.")

                if probability_severe is not None:
                    probability_percent = round(float(probability_severe) * 100, 2)
                else:
                    probability_percent = None

                st.subheader("Prediction Result")

                if severity_prediction == 1:
                    st.error("Severe Outbreak")
                elif severity_prediction == 0:
                    st.info("Not Severe Outbreak")
                else:
                    st.warning("Prediction label unavailable.")

                col1, col2 = st.columns(2)
                label_text = "Severe" if severity_prediction == 1 else "Not Severe"

                with col1:
                    st.metric("Prediction", label_text)

                with col2:
                    if probability_percent is not None:
                        st.metric("Probability Severe", f"{probability_percent}%")
                    else:
                        st.metric("Probability Severe", "N/A")

                if probability_percent is not None:
                    st.progress(min(max(probability_percent / 100, 0.0), 1.0))

                with st.expander("View raw API response"):
                    st.json(result)

            else:
                st.error(f"API request failed with status code {response.status_code}")
                try:
                    st.json(response.json())
                except Exception:
                    st.text(response.text)

        except requests.exceptions.RequestException as e:
            st.error("Could not connect to the API.")
            st.text(str(e))
            
            
            