import os
import urllib.parse
import json

base_dir = 'nintendo/switch/savegames'
base_url = 'https://github.com/laleeroy/NX-Saves/raw/main/nintendo/switch/savegames/'

# Get all filenames and sort them alphabetically
filenames = sorted(os.listdir(base_dir))

# Create the file URLs
file_urls = []
for filename in filenames:
    encoded_filename = urllib.parse.quote(filename)
    download_url = base_url + encoded_filename
    file_urls.append(download_url)

# Create the JSON structure
json_data = {
    "files": file_urls
}

# Write to JSON file
with open('docs/index.html', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2, ensure_ascii=False)
