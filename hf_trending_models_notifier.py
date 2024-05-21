import requests
from bs4 import BeautifulSoup
from winotify import Notification, audio
import time
import logging
import os

# Set up logging
script_dir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(script_dir, 'notifier.log')
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_trending_models():
    logging.info('Fetching trending models')
    url = "https://huggingface.co/models?sort=trending"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return []
    
    soup = BeautifulSoup(response.content, "html.parser")
    models = soup.find_all("header", class_="flex items-center mb-0.5")

    trending_models = []
    for model in models:
        try:
            model_name = model.find("h4", class_="text-md truncate font-mono text-black dark:group-hover/repo:text-yellow-500 group-hover/repo:text-indigo-600 text-smd").text.strip()
            author_name = model.get('title', '')  # Assuming the author name is in the title attribute
            trending_models.append({
                "model_name": model_name,
                "author_name": author_name
            })
        except AttributeError as e:
            logging.error(f"Error parsing model information: {e}")
    
    return trending_models

def send_notification(models):
    logging.info('Sending notifications')
    top_3_models = models[:3]  # Get only the top 3 models
    message = ""
    for model in top_3_models:
        message += f"Model: {model['model_name']}\n"
    
    toast = Notification(
        app_id="Hugging Face Notifier",
        title="Top 3 Trending Models on Hugging Face",
        msg=message.strip(),
        duration="long"
    )
    toast.set_audio(audio.Default, loop=False)
    toast.show()
    logging.info('Sent consolidated notification for top 3 models')

# Periodic Task
if __name__ == "__main__":
    logging.info('Script started')
    while True:
        try:
            trending_models = get_trending_models()
            if trending_models:
                send_notification(trending_models)
            else:
                logging.warning("No models found")
        except Exception as e:
            logging.error(f"Error occurred: {e}")
        time.sleep(3600)  # Wait for an hour before checking again
