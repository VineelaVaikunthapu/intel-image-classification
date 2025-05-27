from PIL import Image
import matplotlib.pyplot as plt

def preprocess_image(image_path):
    return Image.open(image_path).convert("RGB")

def get_prediction(model, image_path):
    image = preprocess_image(image_path)

    # Run prediction
    results = model.predict(image, imgsz=224)
    probs = results[0].probs  # classification probabilities

    # top label and all confidences
    top1 = probs.top1
    label = results[0].names[top1]
    confidences = {results[0].names[i]: float(prob) for i, prob in enumerate(probs.data)}

    return label, confidences
