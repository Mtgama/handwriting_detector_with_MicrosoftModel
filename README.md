# Image OCR and GPT-3 Description

This project is a web application that allows users to upload an image containing handwritten text, recognize the text using Microsoft's TrOCR model, and optionally generate a detailed description of the recognized text using OpenAI's GPT-3.

## Features
- **OCR (Optical Character Recognition):** Extract handwritten text from uploaded images using the [TrOCR model](https://huggingface.co/microsoft/trocr-base-handwritten).
- **Custom Prompt Support:** Users can provide a custom prompt for GPT-3 to generate detailed descriptions.
- **Toggle Description:** The user can choose to disable GPT-3 and only retrieve the recognized text.
- **Responsive Web Interface:** Simple and user-friendly interface for uploading images and managing prompts.

---

## Project Structure
- **`app.py`:** The main Flask application handling image uploads, text recognition, and communication with GPT-3.
- **`templates/upload.html`:** Frontend HTML template for the user interface.
- **`requirements.txt`:** List of Python dependencies for the project.

---

## Prerequisites
Before running the project, ensure you have the following:
- **Python 3.8 or newer.**
- **A valid OpenAI API key:** Can be obtained from [OpenAI](https://platform.openai.com/signup/).
- **Required Python libraries:** These are listed in `requirements.txt`.
- **Access to the TrOCR model:** Available on Hugging Face.

---

## Installation
Follow these steps to set up the project:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mtgama/handwriting_detector_with_MicrosoftModel.git
   cd handwriting_detector_with_MicrosoftModel
   ```

2. **Install required dependencies:**
- Run the following command to install the necessary Python libraries:
    ```bash
    pip install -r requirements.txt
    ```
3. **Setup your OpenAI key:**

- Create an API key by signing up at OpenAI.
- Open the app.py file and add your API key in the line


## Usage
Once the setup is complete, follow these steps to use the application:

1. **Run the Flask application:**
   Start the application by running:
   ```bash
   python main.py

2. **Open the application in your browser:**

- By default, the application runs at: http://127.0.0.1:5000/


## Example Workflow
Below is an example workflow demonstrating the application's functionality:

![Example Workflow](https://s8.uupload.ir/files/screen-recording-2024-12-02-124648_0rnf.gif)
