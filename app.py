from flask import Flask, render_template, request
from ultralytics import YOLO
from utils import preprocess_image, get_prediction
import os

app = Flask(__name__)
base_dir = os.path.dirname(os.path.abspath(__file__))  
model_path = os.path.abspath(os.path.join(base_dir, "..", "model", "yolov8_class_model.pt")) 

print(f"Loading model from: {model_path}")  # Debug print

model = YOLO(model_path)
 # Load CPU-compatible weights

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        image = request.files['image']
        os.makedirs('static', exist_ok=True)
        filepath = os.path.join('static', image.filename)
        image.save(filepath)

        label, confidences = get_prediction(model, filepath)

        #result sentence
        max_conf = max(confidences.values())
        if max_conf < 0.5:
            result_sentence = "The uploaded image does not appear to match any known class."
            label = "Unknown"
        else:
            result_sentence = f"The uploaded image is {max_conf*100:.1f}% likely to be a {label}."

        return render_template(
            'result.html',
            label=label,
            image=filepath,
            confidences=confidences,
            result_sentence=result_sentence
        )

    return render_template('upload.html')

if __name__ == "__main__":
    app.run(debug=True)