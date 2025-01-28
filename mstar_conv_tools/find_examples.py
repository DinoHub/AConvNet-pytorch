import os
import json

# Folder containing the JSON files
folder_path = '/workspace/dataset/soc/test/ZSU234'

# Iterate through each file in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.json'):  # Check if it's a JSON file
        file_path = os.path.join(folder_path, file_name)
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                # Check if azimuth_angle is 90
                if data.get('azimuth_angle') == 90:
                    print(file_name)
        except (json.JSONDecodeError, KeyError):
            print(f"Skipping invalid or unreadable file: {file_name}")
