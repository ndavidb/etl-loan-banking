import requests
from pathlib import Path

def download_file(url: str, path: Path):
    filename = url.split('/')[-1]
    zip_file_path = path / filename

    try:
        print("Downloading", filename)
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(zip_file_path, "wb") as zip_file:
                zip_file.write(response.content)
                print("Successfully downloaded data to data/raw/")
        elif response.status_code == 404:
            raise FileNotFoundError
        else:
            raise Exception("Error Downloading File")
    except requests.exceptions.RequestException as e:
        print(e)

    return zip_file_path
