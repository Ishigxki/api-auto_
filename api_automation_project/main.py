import requests
import json
import logging
import os

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s -%(levelname)s - %(message)s"
)

API_KEY = os.getenv("API_KEY")

def fetch_data():

    logging.info("Starting API fetch process")
    url = "https://jsonplaceholder.typicode.com/posts"
    headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "application/json"
}

    try:
        
        response =requests.get(url,timeout=10,headers=headers)
        response.raise_for_status()
        data =response.json()

        with open("output.json","w") as file:
            json.dump(data,file, indent=4)
        logging.info("Data written to output.json successfully")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error occurred: {e}")


if __name__ == "__main__": fetch_data()