# data_list = ["10", "4.0", "3.6", "3.5", "3.4", "Data"]

# # Loop through the list and print out only the numbers (integers and floats)
# for item in data_list:
#     cleaned_item = item.replace(".", "", 1)
#     if cleaned_item.isdigit() or cleaned_item.replace("-", "", 1).isdigit():
#         print(item)



import json

# Assuming you have the config_json dictionary
config_json = {
    "blender_foundation_path": "C:\\Users\\J\\AppData\\Roaming\\Blender Foundation\\Blender",
    "installed_blender_versions": {}
}

# Specify the file path where you want to save the JSON data
output_file_path = "config.json"

# Write the config_json dictionary into a JSON file
with open(output_file_path, 'w') as json_file:
    json.dump(config_json, json_file, indent=2)
