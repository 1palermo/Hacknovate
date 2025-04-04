import openai
import os
from dotenv import load_dotenv
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
from paddleocr import PaddleOCR
import json
import re

# Load environment variables
load_dotenv()
akash_api_key = os.getenv("AKASH_API_KEY")  # Set this in .env file

# Initialize Akash OpenAI Client
client = openai.OpenAI(
    api_key=akash_api_key,
    base_url="https://chatapi.akash.network/api/v1"
)

# Initialize OCR Model
ocr = PaddleOCR(use_angle_cls=False, lang='en')

# Function to generate product listing using Akash API
def generate_product_details(text):
    response = client.chat.completions.create(
        model="Meta-Llama-3-1-8B-Instruct-FP8",
        messages=[
            {
                "role": "system",
                "content": """Extract product details for e-commerce listing. 
Format a human-readable listing followed by a JSON block at the end.
Human Readable Format:
📦 [Product Name]  
💰 Price: ₹XX.XX  
✨ Key Features:  
• [Main Feature 1]  
• [Main Feature 2]  
• [Main Feature 3]  
🖼 [Product Image]  
🏷 Available Now on E-commerce Platform  
✈ Fast Shipping Available  
🛒 Shop Now: [Link]  
🔍 Search: [Main Keywords]  
[#RelevantHashtags]
(Optional if available)
🆔 License Number: [License No.]  
🏭 Manufacturing Date: [DD-MM-YYYY]  
⌛ Use By: [DD-MM-YYYY]  
🍽 Nutrition Information:  
• [Nutrient 1: Value]  
• [Nutrient 2: Value]  
• [Nutrient 3: Value]
JSON Format:
{
  "product_name": "...",
  "price": "...",
  "features": ["...", "...", "..."],
  "image": "...",
  "available": true,
  "shipping": "Fast",
  "shop_link": "...",
  "keywords": "...",
  "hashtags": ["#tag1", "#tag2"],
  "license_number": "...",
  "manufacture_date": "...",
  "use_by": "...",
  "nutrition_info": {
    "Nutrient 1": "...",
    "Nutrient 2": "...",
    "Nutrient 3": "..."
  }
}
"""
            },
            {"role": "user", "content": text}
        ],
    )
    return response.choices[0].message.content

# Streamlit UI
st.title("Hacknovate 6.0 - Automated Product Listing")
st.sidebar.title("Navigation")
app_mode = st.sidebar.selectbox("Choose the task", ["Welcome", "Project Details", "Task 1"])

if app_mode == "Task 1":
    st.write("## Task 1: Extract Product Details Using OCR")

    input_method = st.radio("Choose Input Method", ["Upload from Device", "Take Photo with Camera"])
    camera_images = []
    uploaded_files = []

    if input_method == "Upload from Device":
        uploaded_files = st.file_uploader("Upload product images", type=["jpeg", "png", "jpg"], accept_multiple_files=True)
    elif input_method == "Take Photo with Camera":
        camera_photo = st.camera_input("Take a picture")
        if camera_photo:
            camera_images = [camera_photo]

    if uploaded_files or camera_images:
        all_images = uploaded_files + camera_images

        if st.button("Start Analysis"):
            st.write("Processing... ⏳")
            product_data_list = []

            for uploaded_image in all_images:
                img = Image.open(uploaded_image)
                st.image(img, caption="Analyzing this image", use_column_width=True)
                img_array = np.array(img)
                result = ocr.ocr(img_array, cls=True)
                text = " ".join([box[1][0] for line in result for box in line])
                st.write(f"OCR Result: {text}")

                # Generate Product Listing with Akash AI
                product_details = generate_product_details(text)
                st.markdown(product_details)
                st.markdown("---")

                # Extract JSON part from the product_details
                try:
                    json_str = re.search(r'\{.*\}', product_details, re.DOTALL).group()
                    product_data = json.loads(json_str)
                    product_data_list.append(product_data)
                except Exception as e:
                    st.warning(f"⚠️ Could not extract JSON for this product. Error: {e}")

            # Offer download of all product listings as JSON
            if product_data_list:
                json_output = json.dumps(product_data_list, indent=2)
                st.download_button(
                    label="📥 Download Product Details as JSON",
                    data=json_output,
                    file_name="product_listings.json",
                    mime="application/json"
                )
    else:
        st.write("Please upload an image or take a photo to start analysis.")

st.sidebar.write("© 2024 Hacknovate 6.0")