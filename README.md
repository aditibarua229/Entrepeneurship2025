This is our app demo for the 2025 Entrepeneurship Project.

Setup Instructions:

1. Run the backend server by executing `python app.py` in your terminal (make sure you have all required Python packages installed).

2. In the WriteStory screen in MIT App Inventor, go to the Blocks view and set the Web1 URL to `http://your-computer-IP:5000/get_story`. Replace `your-computer-IP` with your local IP address (you can find this by running `ipconfig` on Windows or `ifconfig` on Mac/Linux).

3. Make sure your computer’s firewall is not blocking Python — allow access on both public and private networks when prompted, or manually enable it in your system settings.

4. Use the MIT AI2 Companion app to connect to the interface on your device. You can either scan the QR code from MIT App Inventor or build and install the `.apk` file on your phone.

Once connected, you can input your age and write a short story. The backend will return three relevant stories from the opposite age group using FAISS and SentenceTransformer.
