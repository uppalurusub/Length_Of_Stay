import streamlit as st
from datetime import datetime


def show_response(response: dict):

    if not response:
        st.error("No response received from API.")
        return

    st.success("Prediction generated successfully.")

    st.divider()

    prediction = response.get("predicted_length_of_stay_days", 0)
    model = response.get("model_name", "-")
    success = response.get("success", False)
    timestamp = response.get("prediction_timestamp", "")
    message = response.get("message", "")

    if timestamp:
        try:
            timestamp = datetime.fromisoformat(timestamp).strftime(
                "%d-%b-%Y %I:%M:%S %p"
            )
        except Exception:
            pass

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="🏥 Predicted Length of Stay",
            value=f"{prediction:.2f} Days"
        )

    with col2:
        st.metric(
            label="🤖 Model",
            value=model
        )

    with col3:
        st.metric(
            label="✅ Status",
            value="Success" if success else "Failed"
        )

    st.divider()

    st.subheader("Prediction Summary")

    st.markdown(
        f"""
**Prediction:** **{prediction:.2f} Days**

**Model Used:** `{model}`

**Prediction Time:** `{timestamp}`

**Message:** {message}
"""
    )

    st.divider()

    if prediction <= 3:
        st.success("🟢 Expected Short Hospital Stay")

    elif prediction <= 7:
        st.warning("🟡 Expected Moderate Hospital Stay")

    else:
        st.error("🔴 Expected Long Hospital Stay")

    st.divider()

    with st.expander("📄 View Complete API Response"):

        st.json(response)