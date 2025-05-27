
Intel Image Classification Web App
==================================

This project is a web-based image classification system using a YOLOv8 model trained on the Intel Image Classification dataset. The program allows users to upload an image and receive real-time predictions along with confidence probabilities via a modern web interface.

Features
--------
- YOLOv8-based Image Classification
- Upload any image (.jpg, .jpeg, .png, .bmp, .gif, .webp)
- Horizontal bar chart visualization of prediction probabilities (Chart.js)
- Human-readable prediction sentence
- Live preview before upload
- Clean UI using Bootstrap 5
- Frontend validation for file types

Project Structure
-----------------
intel-image-classification/
├── backend/
│   └── app.py                     # Flask backend
│   └── utils.py                   # Preprocessing and prediction logic
├── model/
│   └── yolov8_class_model.pt  # YOLOv8 trained weights
├── static/                    #save in backend too for less complications
|   └── logo.jpg               # Logo image
|   └── test.jpg               # Testing image(mountain)
├── templates/
│   ├── upload.html            # Upload form (UI)
│   └── result.html            # Output & graph
└── README.txt

Note: There is another folder DL_models that has our classification models done in google colab.
Setup Instructions
------------------

1. Create a Virtual Environment:
   python -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate

2. Install Requirements:
   pip install -r requirements.txt

3. Add YOLOv8 Model Weights:

Run the App
-----------
python app.py

Then open: http://localhost:5000

Dataset Reference
-----------------
Intel Image Classification on Kaggle:
https://www.kaggle.com/datasets/puneet6060/intel-image-classification

Classes:
- Building
- Forest
- Glacier
- Mountain
- Sea
- Street

TODO / Future Enhancements
--------------------------
- Add drag-and-drop upload support
- Store prediction history
- Deploy on Render / Heroku
- Mobile app
- Add complex error handling

Contributors
------------
- Satish Vepuri
- Triveni Kata
- Vineela Vaikunthapu
- Vinith Kumar Gaduputi
- Dilip Pushadapu

