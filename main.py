import pandas as pd
import requests
import os
import json
from datetime import datetime

product_count = 0
image_download_count = 0


def get_current_datetime():
    # Get the current date and time
    current_datetime = datetime.now()

    # Formatting the datetime object to a string
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_datetime


def download_images(csv_file):
    global product_count
    global image_download_count

    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Ensure 'Images' column exists
    if 'Images' not in df.columns:
        raise ValueError("The CSV file does not contain an 'Images' column.")

    # Create a directory to save the images
    os.makedirs('downloaded_images', exist_ok=True)

    # Loop through each row in the DataFrame
    for index, row in df.iterrows():
        product_count += 1
        # Get the value in the 'Images' column
        images_value = row['Images']

        # Check if the value is NaN or an empty string
        if pd.isna(images_value) or images_value.strip() == '':
            print(f"{index} | No images found for row.")
            continue

        # Split the URLs by comma, or handle it as a single URL
        urls = [
            images_value] if ',' not in images_value else images_value.split(',')

        # Download each image
        for url in urls:
            url = url.strip()  # Remove any leading/trailing whitespace
            if url:
                # Extract the image name from the URL
                image_name = os.path.basename(url)
                image_path = os.path.join('downloaded_images', image_name)

                # Check if the image already exists
                image_download_count += 1
                if not os.path.exists(image_path):
                    try:
                        response = requests.get(url)
                        response.raise_for_status()  # Check if the request was successful

                        # Save the image
                        with open(image_path, 'wb') as file:
                            file.write(response.content)

                        print(f"{index} | Downloaded {image_name}")
                    except requests.exceptions.RequestException as e:
                        print(f"{index} | Failed to download {url}: {e}")
                else:
                    print(
                        f"{index} | {image_name} already exists. Skipping download.")

    # Write the count of downloaded images and processed products to a JSON file
    with open(get_current_datetime() + '.json', 'w') as f:
        json.dump({"image_download_count": image_download_count,
                   "product_count": product_count}, f)


# Usage example
download_images('input.csv')
