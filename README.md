🌿 Plant Disease Analyzer
This is a simple and effective web application that allows users to upload plant images (leaf, stem, fruit, etc.) and get an AI-powered analysis of the plant's health. The app leverages NVIDIA’s GenAI API to detect plant parts, health condition, diseases, scientific names, and provides both organic and chemical treatment recommendations.

✨ Features
📷 Upload plant images (leaf, fruit, stem, etc.)
🧠 Analyze plant health using NVIDIA’s LLM (google/gemma-3-27b-it)
🦠 Detect disease name (if unhealthy)
🔬 Show scientific name of the plant
💊 Recommend organic and chemical treatments
🧪 Uses image compression to stay within LLM API limits (under 180 KB base64)
🎨 Clean and interactive Streamlit UI

🚀 How It Works
User uploads an image
The image is resized and compressed to fit within API limits
An analysis prompt is constructed and sent to the NVIDIA LLM API
The AI model returns a formatted plant disease diagnosis
The diagnosis is displayed in the Streamlit app

🛠️ Technologies Used
Component	Description
Streamlit	Web framework for building interactive apps
PIL (Pillow)	Python Imaging Library for image compression
Requests	Handles communication with NVIDIA API
NVIDIA GenAI API	Powers the diagnosis using google/gemma-3-27b-it model

📦 Installation
Clone the repository:
git clone https://github.com/your-username/plant-disease-analyzer.git
cd plant-disease-analyzer
Install dependencies:
pip install streamlit pillow requests
Run the app:
streamlit run app.py
🔐 NVIDIA API Key
Replace the placeholder API key in the code with your actual key:
api_key = "your-nvidia-api-key"
You can get one from the NVIDIA AI Foundation Model APIs.

🧪 Sample Output
📋 Diagnosis

**Plant:** Tomato  
**Part:** Leaf  
**Health:** Unhealthy  
**Disease:** Early blight  
**Scientific:** Solanum lycopersicum  
**Treatment:**  
- *Organic:* Neem oil spray, compost tea  
- *Chemical:* Mancozeb, Chlorothalonil

📌 Note
Image must be under ~180 KB after base64 encoding. The app automatically compresses the image.

📄 License
This project is open-source and available under the MIT License.
