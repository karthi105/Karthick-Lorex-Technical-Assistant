import streamlit as st

st.set_page_config(
"Karthick's Lorex Assistant for Agents ",
    page_icon="📹"
)

st.title("📹 Karthick's Lorex Assistant for Agents")
st.write("Agent-only troubleshooting tool")

issue = st.selectbox(
    "Select the customer issue:",
    [
        "Select an issue",
        "IP Camera Offline",
        "Analog Camera Offline"
    ]
)

# -----------------------------
# IP CAMERA OFFLINE
# -----------------------------

if issue == "IP Camera Offline":

    st.header("IP Camera Offline")

    st.write("### Ask the customer:")

    answer1 = st.radio(
        "Is the camera receiving power?",
        ["Yes", "No", "Not sure"]
    )

    if answer1 == "Yes":

        st.info(
            "Next question to ask the customer: "
            "Is the Ethernet cable securely connected "
            "to the camera and network device?"
        )

    elif answer1 == "No":

        st.warning(
            "Ask the customer to check the camera power "
            "connection and PoE/power source."
        )

    else:

        st.info(
            "Ask the customer to check whether the camera "
            "has any power/status LED."
        )


# -----------------------------
# ANALOG CAMERA OFFLINE
# -----------------------------

elif issue == "Analog Camera Offline":

    st.header("Analog Camera Offline")

    st.write("### Ask the customer:")

    answer1 = st.radio(
        "Is the camera receiving power?",
        ["Yes", "No", "Not sure"]
    )

    if answer1 == "Yes":

        st.info(
            "Next question to ask the customer: "
            "Is the BNC/coaxial cable securely connected "
            "at both the camera and DVR?"
        )

    elif answer1 == "No":

        st.warning(
            "Ask the customer to check the camera "
            "power supply."
        )

    else:

        st.info(
            "Ask the customer to check whether the camera "
            "has any power/status indication."
        )
