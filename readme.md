
# 🌿 Plant Disease Analyzer

This Streamlit application lets you **diagnose plant health from leaf, flower, or fruit images instantly!**  
Simply **upload a photo of your plant**, and the app will:

✅ Compress and base64-encode the photo efficiently.  
✅ Send it to **Nvidia's Gemini-3-27B API** for analysis.  
✅ Display a clear, human-readable diagnosis — including disease, health, treatment options, and more.

---

## 🚀 Features

- **Plant Disease Identification:** Detects whether a leaf, flower, or fruit is healthy or sick.
- **Part Detection:** Recognises which part of the plant you’re investigating.
- **Comprehensive Report:** Shows the plant's health, disease, scientific name, and organic/chemical treatment options.
- **Efficient:** Compresses large images under 180KB without losing detail.
- **User-Friendly UI:** Built with Streamlit — lightweight, interactive, and fast.

---

## 🛠 Tech Stack

- **Python 3.7+**
- **Streamlit**
- **Pillow (Python Imaging Library)**
- **Base64**
- **Nvidia Gemini-3-27B API**
- **Requests**

---

## 📥 Installation

1️⃣ **Clone this repository:**

```bash
git clone https://github.com/your-username/plant-disease-analyzer.git
cd plant-disease-analyzer
````

2️⃣ **Install required packages:**

```bash
pip install streamlit Pillow requests
```

---

## 🔐 API Key

* Signup for NVIDIA API and get your API key from [https://developer.nvidia.com/](https://developer.nvidia.com/)
* Update the `api_key` in `app.py` with your own API key:

```python
api_key = "your_api_key_here"
```

---

## ⚙ Run the Application

Start Streamlit:

```bash
streamlit run app.py
```

Then view the application at:

```
http://localhost:8501
```

---

## 📝 How to Use

✅ **Step 1:** Upload a clear photo of your plant's leaf, flower, or fruit.
✅ **Step 2:** The app will compress and send it for analysis.
✅ **Step 3:** Once you click **Analyze**, it will return:

* The plant's health
* Disease (if any)
* Scientific name
* Possible organic and chemical treatments

---

## 🌟 Forward-Looking View

This pipeline can be integrated into:

✅ **Smart agriculture platforms**
✅ **Farmer's mobile apps**
✅ **Automated disease surveillance systems**
✅ **AI-assisted agricultural diagnostics**

---

## 📝 Notes

* The photo should be clear, well-lighted, and show the affected area in detail.
* Large images are compressed under 180KB for faster processing.

---

## 🕹 License

This project is licensed under the **MIT License** — see `LICENSE` for details.


