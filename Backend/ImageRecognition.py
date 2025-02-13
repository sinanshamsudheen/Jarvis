import os
import pyautogui
import requests
from dotenv import dotenv_values
# Set your Groq API key
env_vars=dotenv_values(".env")
GROQ_API_KEY = env_vars.get("GROQ_API_KEY") # Replace with your actual API key
 # Replace with your actual API key

# Groq API endpoints (adjust based on actual documentation)
TEXT_ANALYSIS_URL = "https://api.groq.com/v1/chat/completions"
OCR_URL = "https://api.groq.com/v1/vision"
IMAGE_CLASSIFICATION_URL = "https://api.groq.com/v1/vision/classify"


def capture_screenshot():
    """Captures a screenshot and saves it as an image file."""
    screenshot = pyautogui.screenshot()
    screenshot_path = r"Data\screenshot.png"
    screenshot.save(screenshot_path)
    return screenshot_path


def extract_text_groq(image_path):
    """Sends the image to Groq API for OCR-based text extraction."""
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
    
    with open(image_path, "rb") as img_file:
        files = {"file": img_file}
        response = requests.post(OCR_URL, headers=headers, files=files)

    if response.status_code == 200:
        return response.json().get("extracted_text", "")
    return "Error in OCR request"


def is_text_a_question(text):
    """Uses Groq API to classify whether the extracted text is a question."""
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    
    data = {
        "model": "llama-3-8b",  # Adjust model if needed
        "messages": [
            {"role": "system", "content": "Determine if the following text is a programming question. Reply 'yes' or 'no'."},
            {"role": "user", "content": text}
        ]
    }

    response = requests.post(TEXT_ANALYSIS_URL, headers=headers, json=data)

    if response.status_code == 200:
        return "yes" in response.json().get("choices", [{}])[0].get("message", {}).get("content", "").lower()
    return False


def classify_image_groq(image_path):
    """Uses Groq API to classify if the image looks like a question."""
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
    
    with open(image_path, "rb") as img_file:
        files = {"file": img_file}
        response = requests.post(IMAGE_CLASSIFICATION_URL, headers=headers, files=files)

    if response.status_code == 200:
        classification = response.json().get("classification", "")
        return "question" in classification.lower()
    return False


def answer_question(question_text):
    """Uses Groq AI to generate an answer if the screenshot contains a question."""
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    
    data = {
        "model": "llama-3-8b",  # Use an appropriate Groq model
        "messages": [
            {"role": "system", "content": "You are an AI assistant that answers programming and general questions."},
            {"role": "user", "content": question_text}
        ]
    }

    response = requests.post(TEXT_ANALYSIS_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "No answer generated.")
    return "Error in getting an answer."


def summarize_screen_content(text):
    """Summarizes the screen content if it's not a question."""
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    
    data = {
        "model": "llama-3-8b",  # Use an appropriate Groq model
        "messages": [
            {"role": "system", "content": "Summarize the following screen content in a few sentences."},
            {"role": "user", "content": text}
        ]
    }

    response = requests.post(TEXT_ANALYSIS_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "No summary generated.")
    return "Error in summarizing content."


def analyze_screenshot():
    """Main function to analyze the screenshot and determine if it's a question, then answer it or summarize it."""
    image_path = capture_screenshot()
    
    # Step 1: Extract text
    extracted_text = extract_text_groq(image_path)
    print(extracted_text)
    
    # Step 2: Check if extracted text is a question
    text_result = is_text_a_question(extracted_text)
    print(text_result)
    
    # Step 3: Use Groq API to classify the image
    image_result = classify_image_groq(image_path)
    print(image_result)

    # Step 4: Decision
    if text_result or image_result:
        answer = answer_question(extracted_text)
        return f"✅ The screenshot is a question.\n💡 **Answer:** {answer}"
    else:
        summary = summarize_screen_content(extracted_text)
        return f"🔍 The screenshot does not contain a question.\n📄 **Summary:** {summary}"


if __name__ == "__main__":
    result = analyze_screenshot()
    print(result)
