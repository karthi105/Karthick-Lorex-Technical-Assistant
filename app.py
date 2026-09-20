import streamlit as st

st.set_page_config(
    page_title="Karthick's Lorex Assistant for Agents",
    page_icon="📹"
)

st.title("📹 Karthick's Lorex Assistant for Agents")
st.write("Enter a customer issue to view the troubleshooting steps.")

# Troubleshooting database
troubleshooting = {

    "IP Camera Offline": [
        "Check whether the camera has power.",
        "Check the Ethernet cable connection at the camera.",
        "Check the Ethernet cable connection at the NVR/router/PoE switch.",
        "Check whether the camera appears in the NVR camera list.",
        "Check the camera's network status.",
        "Restart the camera and network device.",
        "Check whether the camera comes back online."
    ],

    "Analog Camera Offline": [
        "Check whether the camera has power.",
        "Check the BNC/coaxial cable connection at the camera.",
        "Check the BNC/coaxial cable connection at the DVR.",
        "Check the camera channel connection.",
        "Check the camera power adapter or power supply.",
        "Restart the camera and DVR.",
        "Check whether video returns."
    ],

    "Camera No Video": [
        "Check whether the camera has power.",
        "Check the camera cable connection.",
        "Check the connection at the NVR/DVR.",
        "Check whether another camera works on the same channel.",
        "Check whether the camera appears in the device list.",
        "Restart the camera and recorder.",
        "Check whether video returns."
    ],

    "Camera Black Screen": [
        "Check whether the camera has power.",
        "Check the camera cable connection.",
        "Check the NVR/DVR video connection.",
        "Check whether the issue occurs during daytime and nighttime.",
        "Restart the camera.",
        "Check whether the camera image returns."
    ],

    "Camera Image Blurry": [
        "Check whether the camera lens is clean.",
        "Check whether the protective film has been removed from the lens.",
        "Check the camera focus.",
        "Check whether the issue occurs during daytime and nighttime.",
        "Restart the camera.",
        "Check whether the image quality improves."
    ],

    "Camera Image Flickering": [
        "Check the camera power connection.",
        "Check the camera cable connection.",
        "Check whether the cable is damaged.",
        "Check whether the flickering occurs during daytime, nighttime, or both.",
        "Restart the camera.",
        "Check whether the flickering continues."
    ],

    "Night Vision Not Working": [
        "Check whether the camera has power.",
        "Check whether the issue occurs only at night.",
        "Check whether the camera IR LEDs are functioning.",
        "Check whether anything is blocking the camera lens.",
        "Check the camera's night vision settings.",
        "Restart the camera.",
        "Check whether night vision is working."
    ],

    "Camera Audio Not Working": [
        "Check whether the camera supports audio.",
        "Check whether the microphone is enabled.",
        "Check the camera audio settings.",
        "Check the recorder audio settings.",
        "Check the device volume.",
        "Restart the camera and recorder.",
        "Check whether audio is working."
    ],

    "PTZ Camera Not Moving": [
        "Check whether the PTZ camera has power.",
        "Check the camera connection.",
        "Check the PTZ control settings.",
        "Check the PTZ address or configuration.",
        "Restart the camera and recorder.",
        "Test the pan, tilt, and zoom controls.",
        "Check whether PTZ movement is working."
    ],

    "Camera Not Recording": [
        "Check whether the camera is online.",
        "Check whether the HDD is detected.",
        "Check the recording schedule.",
        "Check the recording mode.",
        "Check available HDD storage.",
        "Restart the recorder.",
        "Check whether new recordings are being created."
    ],

    "NVR/DVR Not Recording": [
        "Check whether the NVR/DVR is powered on.",
        "Check whether the cameras are online.",
        "Check whether the HDD is detected.",
        "Check the recording schedule.",
        "Check the recording settings.",
        "Check available storage.",
        "Check whether recording has resumed."
    ],

    "Playback Not Working": [
        "Check whether the system is currently recording.",
        "Check the selected date and time.",
        "Check whether recordings exist for the selected period.",
        "Check the HDD status.",
        "Restart the NVR/DVR.",
        "Try playback again."
    ],

    "HDD Not Detected": [
        "Check whether the NVR/DVR is powered on.",
        "Check the HDD status in the recorder settings.",
        "Power off the recorder.",
        "Check the HDD connections.",
        "Reconnect the HDD if required.",
        "Power the recorder back on.",
        "Check whether the HDD is detected."
    ],

    "Remote Viewing Not Working": [
        "Check whether the NVR/DVR is connected to the internet.",
        "Check the network cable connection.",
        "Check the recorder network status.",
        "Check whether the device is online in the app.",
        "Restart the router and recorder.",
        "Check remote viewing again."
    ],

    "Camera Not Connecting to Wi-Fi": [
        "Check whether the camera has power.",
        "Check whether the Wi-Fi network is available.",
        "Check the Wi-Fi signal strength.",
        "Verify the Wi-Fi password.",
        "Restart the camera and router.",
        "Try connecting the camera again.",
        "Check whether the camera comes online."
    ],

    "Device Offline in Lorex App": [
        "Check whether the recorder or camera has power.",
        "Check the internet connection.",
        "Check the network connection.",
        "Check the device status on the recorder.",
        "Restart the network device.",
        "Restart the recorder or camera.",
        "Check whether the device becomes online in the app."
    ],

    "Push Notifications Not Working": [
        "Check whether notifications are enabled in the app.",
        "Check whether notifications are enabled on the phone.",
        "Check motion detection settings.",
        "Check the notification schedule.",
        "Check the camera's motion detection settings.",
        "Restart the app.",
        "Test notifications again."
    ],

    "Login/Password Issue": [
        "Confirm the username or email address.",
        "Confirm the password being entered.",
        "Check whether the account is locked.",
        "Try the password recovery option.",
        "Reset the password if required.",
        "Try logging in again."
    ],

    "NVR/DVR Not Powering On": [
        "Check the power adapter connection.",
        "Check the power outlet.",
        "Check whether the power adapter is damaged.",
        "Check the power connection at the recorder.",
        "Try another compatible power outlet.",
        "Power cycle the recorder.",
        "Check whether the recorder powers on."
    ],

    "HDMI/VGA Display Issue": [
        "Check whether the NVR/DVR is powered on.",
        "Check the HDMI/VGA cable connection.",
        "Check whether the monitor is powered on.",
        "Select the correct monitor input source.",
        "Try another compatible display cable.",
        "Restart the recorder and monitor.",
        "Check whether the display appears."
    ],

    "Date/Time Issue": [
        "Check the current date and time.",
        "Check the time zone.",
        "Check whether automatic time synchronization is enabled.",
        "Check the internet connection if network time is being used.",
        "Correct the date and time settings.",
        "Restart the recorder if required.",
        "Check whether the correct time is displayed."
    ]
}


# Issue input
issue = st.text_input(
    "Enter the customer issue:",
    placeholder="Example: IP Camera Offline"
)

# Show troubleshooting steps
if issue:

    matched_issue = None

    for item in troubleshooting:
        if issue.lower() == item.lower():
            matched_issue = item
            break

    if matched_issue:

        st.subheader("Troubleshooting Steps")

        for number, step in enumerate(
            troubleshooting[matched_issue], start=1
        ):
            st.write(f"**{number}.** {step}")

    else:

        st.warning(
            "Issue not found. Please enter an issue from the troubleshooting list."
        )
