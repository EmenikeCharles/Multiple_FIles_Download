import wget
import os
import re


UPLOAD_FOLDER = 'data'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

URLS_FILENAME = 'urls.txt'

pattern = r'%20'

print('Downloading files...')

with open(URLS_FILENAME) as file:

    for url in file:
        stripped_url = url.strip()
        cleaned_url = re.sub(pattern, " ", stripped_url)
        _, name = os.path.split(cleaned_url)

        destination = os.path.join(UPLOAD_FOLDER, name)
        print(destination)

        wget.download(cleaned_url, destination)

print('Download completed!')
        
