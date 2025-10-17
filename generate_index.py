import os
import urllib.parse
import json

base_dir = 'nintendo/switch/savegames'
base_url = 'https://github.com/laleeroy/NX-Saves/raw/main/nintendo/switch/savegames/'

# --- Add your directory links here ---
directories = [
    "https://github.com/laleeroy/nxlinks/raw/refs/heads/master/motd.json"
]

# --- Get all filenames and sort them alphabetically ---
filenames = sorted(os.listdir(base_dir))

# --- Create file URLs ---
file_urls = []
for filename in filenames:
    encoded_filename = urllib.parse.quote(filename)
    download_url = base_url + encoded_filename
    file_urls.append(download_url)

# --- Create JSON structure with directories first ---
json_data = {
    "directories": directories,
    "files": file_urls
}

# --- Write to docs/index.html ---
os.makedirs('docs', exist_ok=True)
with open('docs/index.html', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2, ensure_ascii=False)

print("docs/index.html generated successfully!")
