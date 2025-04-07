# 📸 SnapTrack – AI-Powered Product Listing Tool

SnapTrack is a smart and accessible tool designed to help small shopkeepers, ONDC sellers, and inventory managers digitize their products instantly using just a camera. By using a combination of OCR, object detection, and LLMs (via Akash Network), SnapTrack generates structured e-commerce listings from simple product images — no barcodes or manual entry required.

---

## 🚀 Features

- 🔍 **OCR-based Text Extraction** – Extracts printed information like product name, dates, and license numbers.
- 🧠 **AI-Powered Listing Generation** – Uses a LLM hosted on Akash to format data into detailed, human-readable and machine-readable listings.
- 🎯 **YOLO Object Detection** – Detects item count and package quantity automatically from the image.
- 🍎 **Freshness Classification** – (Optional) Detects freshness levels of perishable items.
- 📥 **JSON Output Download** – Easily download product listings in structured JSON format.
- ☁️ **Decentralized Compute** – Inference is powered by Akash Network, ensuring privacy, scalability, and lower costs.

---

## 💡 Use Case

SnapTrack is ideal for:
- **Local Kirana stores** that want to join digital marketplaces like ONDC.
- **Sellers without barcode tools**, needing a visual-based alternative.
- **Grocery vendors** who manage expiry-sensitive products.
- **Inventory handlers** looking to automate listing and record keeping.

---

## 🛠️ Tech Stack

- **Frontend/UI**: Streamlit (Python)
- **OCR**: PaddleOCR
- **Object Detection**: YOLOv8
- **LLM**: Meta-LLaMA 3 hosted on [Akash Network](https://akash.network/)
- **Image Handling**: PIL, NumPy
- **Cloud Config**: dotenv for environment variables

---

## 🧱 Architecture

1. 📷 **User uploads/takes product image**
2. 🔠 **PaddleOCR extracts textual details**
3. 📦 **YOLO counts quantity and packs**
4. 🤖 **Text passed to LLM via Akash API**
5. 🧾 **Returns formatted listing + JSON**
6. 📤 **User downloads or copies listing**

---

## 🔗 Akash Network Integration

- LLM inference (Meta-LLaMA 3) is done via OpenAI-compatible API hosted on Akash.
- This ensures low-cost, censorship-resistant, and decentralized AI access.
- All AI prompts/responses are securely processed using Akash's cloud infra.

---

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/snaptrack.git
cd snaptrack
2. Create a .env File
AKASH_API_KEY=your_akash_key_here
3. Install Requirements
pip install -r requirements.txt
4. Run the App
streamlit run app.py

```
Folder Structure
```bash
snaptrack/
│
├── app.py               # Main Streamlit application
├── utils/               # Utility scripts (if added)
├── models/              # YOLO model files
├── .env                 # Environment variables
├── requirements.txt     # Python dependencies
└── README.md            # Project Documentation
```

🤝 Acknowledgements
Akash Network for decentralized compute power.

Meta LLaMA 3 for language modeling.

PaddleOCR for text recognition.

Ultralytics YOLOv8 for object detection.


---

Let me know if you want to turn this into a GitHub page or need visuals like a system architecture diagram!

![image](https://github.com/user-attachments/assets/04fee203-6abf-466d-96c8-eb6dfda025fd)
![image](https://github.com/user-attachments/assets/7fb3248a-f62c-45a0-aab5-b8888f525e87)
![image](https://github.com/user-attachments/assets/4d268379-f585-4a0a-948a-9b1fd9b88b4f)
![image](https://github.com/user-attachments/assets/facbb469-74d1-45ea-ab41-4b5a2d0bfb8a)





