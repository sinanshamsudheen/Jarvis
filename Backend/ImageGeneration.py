import asyncio
from random import randint
from PIL import Image
import requests
from dotenv import get_key
import os
from time import sleep
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def open_images(prompt):
    folder_path = os.path.abspath(r"Data")  # Use absolute path
    prompt = prompt.replace(" ", "_")

    # Generate filenames
    files = [f"{prompt}{i}.jpg" for i in range(1, 5)]

    for jpg_file in files:
        image_path = os.path.join(folder_path, jpg_file)

        try:
            img = Image.open(image_path)
            logging.info(f"Opening image: {image_path}")
            img.show()
            sleep(1)
        except IOError:
            logging.error(f"Unable to open {image_path}")

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {get_key('.env', 'HuggingFaceAPIKey')}"}

async def query(payload):
    response = await asyncio.to_thread(requests.post, API_URL, headers=headers, json=payload)
    return response.content

async def generate_images(prompt: str):
    tasks = []
    for _ in range(4):
        payload = {
            "inputs": f"{prompt}, quality=4k, sharpness=maximum, Ultra High details, high resolution, seed = {randint(0, 1000000)}",
        }
        task = asyncio.create_task(query(payload))
        tasks.append(task)

    image_bytes_list = await asyncio.gather(*tasks)

    for i, image_bytes in enumerate(image_bytes_list):
        with open(os.path.abspath(fr"Data\{prompt.replace(' ', '_')}{i + 1}.jpg"), "wb") as f:
            f.write(image_bytes)

def GenerateImages(prompt: str):
    asyncio.run(generate_images(prompt))
    open_images(prompt)

def main():
    image_generation_file = os.path.abspath(r"Frontend\Files\ImageGeneration.data")

    while True:
        try:
            with open(image_generation_file, "r") as f:
                data: str = f.read()

            prompt, status = data.split(",")

            if status.strip() == "True":
                logging.info("Generating Images...")
                GenerateImages(prompt=prompt)

                with open(image_generation_file, "w") as f:
                    f.write("False,False")
                break
            else:
                sleep(1)  # Reduce CPU usage
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            sleep(1)  # Avoid spamming logs on repeated errors

if __name__ == "__main__":
    main()