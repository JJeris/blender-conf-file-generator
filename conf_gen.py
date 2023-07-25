"""
This code assumes that the addon files are located in the already 
specified path Blender addon installation path.

"""

import time
from datetime import datetime
from pathlib import Path

import platform
import json
import appdirs


ADDON_SOURCE_PATH = None
OS_NAME = platform.system()
# USERNAME = getpass.getuser()
CONFIG_JSON_FILE_NAME = "config.json"
config_json = {
    "date_when_last_generated": None,
    "os_on_which_generated": None,
    "blender_foundation_path": None,
    "installed_blender_versions": {}
}
SCRIPT_NAME = "__init__"




def comp_fn_locate_addon_paths():
    start_time = time.time()
    config_json["date_when_last_generated"] = str(datetime.now())

    if OS_NAME == "Windows":
        config_json["os_on_which_generated"] = OS_NAME
        # Check if path exists
        ADDON_SOURCE_PATH = Path.home() / "AppData" / "Roaming" / "Blender Foundation" / "Blender"
    # print("MSG: ", ADDON_SOURCE_PATH)


    config_json["blender_foundation_path"] = str(ADDON_SOURCE_PATH) 
    # Get a list of the dirs inside addon_source_path
    for path_0 in ADDON_SOURCE_PATH.iterdir():
        
        cleaned_item = str(path_0.name.replace(".", "", 1))
        if cleaned_item.isdigit() or cleaned_item.replace("-", "", 1).isdigit():

            # Need an insertSort algo here
            config_json["installed_blender_versions"][str(path_0.name)] = {}
            config_json["installed_blender_versions"][str(path_0.name)]["blender_exe_path"] = None
            
            SCRIPTS_SOURCE_PATH = ADDON_SOURCE_PATH / path_0.name / "scripts" / "addons"
            # print(SCRIPTS_SOURCE_PATH)
            config_json["installed_blender_versions"][str(path_0.name)]["scripts_path"] = str(SCRIPTS_SOURCE_PATH)
            config_json["installed_blender_versions"][str(path_0.name)]["addons"] = {}

            for path_1 in SCRIPTS_SOURCE_PATH.iterdir():
                # print(path_1)
                if path_1.name != "__pycache__" and path_1.is_dir() == True:
                    # print(path_1)

                    config_json["installed_blender_versions"][path_0.name]["addons"][path_1.name] = {}
                    config_json["installed_blender_versions"][path_0.name]["addons"][path_1.name]["bl_info"] = {}

                    init_file_path = path_1 / "__init__.py"
                    print(init_file_path)



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
    # return json.dumps(config_json, indent=2)


def main():
    """
    Main function
    """
    comp_fn_locate_addon_paths()
main()



                    # # Read the addon file and extract bl_info
                    # addon_file = path_1 / f"{SCRIPT_NAME}.py"
                    # if addon_file.exists():
                    #     with open(addon_file, 'r') as f:
                    #         try:
                    #             parsed_code = ast.parse(f.read())
                    #             for node in ast.walk(parsed_code):
                    #                 if isinstance(node, ast.Assign) and len(node.targets) == 1 and \
                    #                         isinstance(node.targets[0], ast.Name) and node.targets[0].id == "bl_info":
                    #                     bl_info_dict = ast.literal_eval(node.value)
                    #                     # Now bl_info_dict contains the contents of bl_info from the addon file.
                    #                     # You can access and process the required information here.
                    #                     print(bl_info_dict)
                    #                     # For example, to access the 'name' and 'author' values:
                    #                     addon_name = bl_info_dict.get("name")
                    #                     addon_author = bl_info_dict.get("author")
                    #                     # Add the information to your config_json or do any other processing as needed.
                    #                     # config_json["installed_blender_versions"][path_0.name]["addons"][path_1.name]["author"] = addon_author
                    #                     # config_json["installed_blender_versions"][path_0.name]["addons"][path_1.name]["version"] = bl_info_dict.get("version")
                    #                     # config_json["installed_blender_versions"][path_0.name]["addons"][path_1.name]["enabled"] = True
                    #                     # config_json["installed_blender_versions"][path_0.name]["addons"][path_1.name]["version_latest"] = False
                    #         except SyntaxError:
                    #             # Handle any syntax errors in the addon file if needed.
                    #             pass
                    # config_json["installed_blender_versions"][path_0.name]["addons"][path_1.name]["author"] = "N/A"
                    # config_json["installed_blender_versions"][path_0.name]["addons"][path_1.name]["version"] = None
                    # config_json["installed_blender_versions"][path_0.name]["addons"][path_1.name]["enabled"] = True
                    # config_json["installed_blender_versions"][path_0.name]["addons"][path_1.name]["version_latest"] = False
                    # config_json["installed_blender_versions"][path_0.name]["addons"].append(path_1.name)
