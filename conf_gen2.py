import time
from datetime import datetime
from pathlib import Path
import platform
import json
import ast  # Import the ast module for safe evaluation

ADDON_SOURCE_PATH = None
OS_NAME = platform.system()
CONFIG_JSON_FILE_NAME = "config.json"
config_json = {
    "date_when_last_generated": None,
    "generated_os": None,
    "blender_foundation_path": None,
    "installed_blender_versions": {}
}

def comp_fn_locate_addon_paths():
    start_time = time.time()
    config_json["date_when_last_generated"] = str(datetime.now())

    if OS_NAME == "Windows":
        # Check if path exists
        ADDON_SOURCE_PATH = Path.home() / "AppData" / "Roaming" / "Blender Foundation" / "Blender"

    config_json["blender_foundation_path"] = str(ADDON_SOURCE_PATH) 
    # Get a list of the dirs inside addon_source_path
    for path_0 in ADDON_SOURCE_PATH.iterdir():
        cleaned_item = str(path_0.name.replace(".", "", 1))
        if cleaned_item.isdigit() or cleaned_item.replace("-", "", 1).isdigit():
            config_json["installed_blender_versions"][str(path_0.name)] = {}
            config_json["installed_blender_versions"][str(path_0.name)]["blender_exe_path"] = None
            
            SCRIPTS_SOURCE_PATH = ADDON_SOURCE_PATH / path_0.name / "scripts" / "addons"
            config_json["installed_blender_versions"][str(path_0.name)]["scripts_path"] = str(SCRIPTS_SOURCE_PATH)
            config_json["installed_blender_versions"][str(path_0.name)]["addons"] = {}

            for path_1 in SCRIPTS_SOURCE_PATH.iterdir():
                if path_1.name != "__pycache__" and path_1.is_dir():
                    config_json["installed_blender_versions"][path_0.name]["addons"][path_1.name] = {}
                    config_json["installed_blender_versions"][path_0.name]["addons"][path_1.name]["bl_info"] = {}

                    init_file_path = path_1 / "__init__.py"

                    # Read the content of __init__.py
                    with open(init_file_path, 'r') as init_file:
                        init_content = init_file.read()

                    # Extract bl_info using ast.literal_eval()
                    import ast
                    try:
                        # Safely evaluate the dictionary literal
                        bl_info = ast.literal_eval(init_content)
                        if isinstance(bl_info, dict):
                            config_json["installed_blender_versions"][path_0.name]["addons"][path_1.name]["bl_info"] = bl_info
                    except ValueError:
                        # If the literal evaluation fails (invalid syntax), skip this addon
                        pass

        else:
            pass

    BLENDER_SOURCE_PATH = Path("C:\\") / "Program Files" / "Blender Foundation"
    for path_2 in BLENDER_SOURCE_PATH.iterdir():
        for path_3 in path_2.iterdir():
            if (path_3.name == "blender.exe"):
                config_json["installed_blender_versions"]["3.4"]["blender_exe_path"] = str(path_3)

    with open(CONFIG_JSON_FILE_NAME, 'w') as json_f:
        json.dump(config_json, json_f, indent=2)
    end_time = time.time()
    print(end_time - start_time)

# Call the function
comp_fn_locate_addon_paths()
