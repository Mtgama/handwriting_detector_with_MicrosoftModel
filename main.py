from flask import Flask, request, jsonify, render_template
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import openai
import os


process = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
load_model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten')

#openai api_key
openai.api_key = "ENTER_API_KEY"

#flask app create
flask_app = Flask(__name__)


@flask_app.route("/")
def home_page():
    return render_template('upload.html')

@flask_app.route("/process",methods=['POST'])
def process_img():
    if 'file' not in request.files:
        return  jsonify({'error': "NO file uploaded!"}), 400
    
    file = request.files['file']
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400
    
    custom_prompt = request.form.get("prompt", "").strip()
    prompt = request.form.get("use_prompt", "no") == "yes"
    try:
        img = Image.open(file).convert("RGB")
        pixel_values = process(images=img, return_tensors="pt").pixel_values
        generated_ids = load_model.generate(pixel_values)
        recon_text = process.batch_decode(generated_ids, skip_special_tokens=True)[0]

        if prompt:
          
            prompt = custom_prompt if custom_prompt else f"Provide a detailed description of this text: '{recon_text}'"
            gpt_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant"},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=100
            )
            gpt_text = gpt_response["choices"][0]["message"]["content"].strip()

            return jsonify({
                "recognized_text": recon_text,
                "gpt_description": gpt_text
            })
        else:
            return jsonify({
                "recognized_text": recon_text
            })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    flask_app.run(debug=True)
