import streamlit as st
from PIL import Image
import requests, base64, io

# UI Title
st.title("🌿 Plant Disease Analyzer")

# Image Upload
uploaded_file = st.file_uploader("Upload a plant image (leaf/fruit/etc)", type=["jpg", "jpeg", "png"])

# Compress and Encode
def compress_image_to_fit(file, max_b64_len=180_000, resize_max=512):
    img = Image.open(file).convert("RGB")
    img.thumbnail((resize_max, resize_max))
    buffer = io.BytesIO()
    quality = 95

    while quality >= 10:
        buffer.seek(0)
        buffer.truncate()
        img.save(buffer, format="JPEG", quality=quality)
        b64 = base64.b64encode(buffer.getvalue()).decode()
        if len(b64) < max_b64_len:
            return b64
        quality -= 5

    raise ValueError("❌ Could not compress image within required size.")

# When an image is uploaded
if uploaded_file:
    try:
        image_b64 = compress_image_to_fit(uploaded_file)
        st.success("✅ Image successfully cooked!")

        # Prompt template
        prompt = f"""Analyze this plant image strictly in this format:
Plant: [common name]
Part: [leaf/stem/fruit/root/flower]
Health: [healthy/unhealthy]
Disease: [name if unhealthy]
Scientific: [latin name]
Treatment: [organic and chemical options]
<img src="data:image/jpeg;base64,{image_b64}" />
"""

        # API Info
        invoke_url = "https://integrate.api.nvidia.com/v1/chat/completions"
        api_key = "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"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json"
        }
        payload = {
            "model": "google/gemma-3-27b-it",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 512,
            "temperature": 0.2,
            "top_p": 0.7,
            "stream": False
        }

        # Analyze Button
        if st.button("🔍 Analyze Plant Image"):
            with st.spinner("Analyzing"):
                response = requests.post(invoke_url, headers=headers, json=payload)
                result = response.json()
                message = result["choices"][0]["message"]["content"]
                st.subheader("📋 Diagnosis")
                formatted_message = message.replace("Plant:", "\n\n**Plant:**") \
                    .replace("Part:", "\n**Part:**") \
                    .replace("Health:", "\n**Health:**") \
                    .replace("Disease:", "\n**Disease:**") \
                    .replace("Scientific:", "\n**Scientific:**") \
                    .replace("Treatment:", "\n**Treatment:**") \
                    .replace("Organic:", "\n- *Organic:*") \
                    .replace("Chemical:", "\n- *Chemical:*")
                st.markdown(formatted_message)

    except Exception as e:
        st.error(str(e))
