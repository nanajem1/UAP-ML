from flask import Flask, render_template, request, redirect, url_for
from src.citra import predict
import os

app = Flask(__name__)

# Folder untuk menyimpan gambar upload
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Model paths
MODEL_PATHS = {
    "mobilenet_model": "model/mobilenet_model.h5",
    "vgg_model": "model/modell_vgg.h5"
}

# Pastikan folder upload ada
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict_page():
    if request.method == "POST":
        if "file" not in request.files:
            return render_template("predict.html", error="No file selected")

        file = request.files["file"]
        if file.filename == "":
            return render_template("predict.html", error="No file selected")

        # Simpan file di folder static/uploads
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)

        # Ambil pilihan model
        model_choice = request.form.get("model_choice")
        if model_choice not in MODEL_PATHS:
            return render_template("predict.html", error="Invalid model selected")

        try:
            # Muat model sesuai pilihan
            model_path = MODEL_PATHS[model_choice]
            class_name, category, confidence = predict(file_path, model_path)

            # Hanya simpan nama file, bukan path lengkap
            return render_template(
                "predict.html",
                uploaded_image=f"uploads/{file.filename}",
                class_name=class_name,
                category=category,
                confidence=confidence,
            )
        except Exception as e:
            return render_template("predict.html", error=f"Prediction error: {str(e)}")

    return render_template("predict.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
