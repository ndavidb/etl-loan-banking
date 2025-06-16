import requests

def download_file(url, path):
    filename = url.split('/')[-1]

    try:
        print("Downloading", filename)
        response = requests.get(url)
        if response.status_code == 200:
            print("Successfully downloaded data to data/raw/")
            zip_file_path = path / filename

            with open(zip_file_path, "wb") as zip_file:
                zip_file.write(response.content)
        elif response.status_code == 404:
            raise FileNotFoundError
        else:
            raise Exception("Error Downloading File")
    except requests.exceptions.RequestException as e:
        print(e)

