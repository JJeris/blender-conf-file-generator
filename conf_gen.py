"""
This code assumes that the addon files are located in the already 
specified path - Blender addon installation path.

Author: @JJeris

"""

import time
from datetime import datetime
from pathlib import Path
import platform
import json
# import importlib.util
# import appdirs
# import sys
# import re

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




def comp_fn_generate_config():
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
            config_json["installed_blender_versions"][str(path_0.name)]["blender_launcher_exe_path"] = None
            
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
                    # print(init_file_path)
                    config_json["installed_blender_versions"][path_0.name]["addons"][path_1.name]["bl_info"]["init_path"] = str(init_file_path)
                    config_json["installed_blender_versions"][path_0.name]["addons"][path_1.name]["statuss"] = {}
                    config_json["installed_blender_versions"][path_0.name]["addons"][path_1.name]["statuss"]["installed"] = True
                    config_json["installed_blender_versions"][path_0.name]["addons"][path_1.name]["statuss"]["enabled"] = True
        else:
            pass

    BLENDER_SOURCE_PATH = Path("C:\\") / "Program Files" / "Blender Foundation"
    for path_2 in BLENDER_SOURCE_PATH.iterdir():
        # print(path_2.name[-3:])
        for path_3 in path_2.iterdir():
            
            if (path_3.name == "blender-launcher.exe"):
                # print(path_3.name)
                config_json["installed_blender_versions"][path_2.name[-3:]]["blender_launcher_exe_path"] = str(path_3)


    
    with open(CONFIG_JSON_FILE_NAME, 'w') as json_f:
        json.dump(config_json, json_f, indent=2)
    end_time = time.time()
    print(end_time - start_time)
    # return json.dumps(config_json, indent=2)


def main():
    """
    Main function
    """
    comp_fn_generate_config()


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

                    # with open(file_path, "r") as file:
                    #     code = compile(file.read(), file_path, "exec")
                    #     globals_dict = {}
                    #     exec(code, globals_dict)
                    #     bl_info_json = globals_dict.get("bl_info")
                    #     config_json["installed_blender_versions"][path_0.name]["addons"][path_1.name]["bl_info"] = bl_info_json
                    # try:
                    #     # Open the file in read mode
                    #     with open(file_path, "r", encoding="utf-8") as file:
                    #         # Read the entire contents of the file
                    #         file_contents = file.read()

                    #         # Use regular expressions to find the bl_info dictionary
                    #         pattern = r"bl_info\s*=\s*{[^}]*}"
                    #         match = re.search(pattern, file_contents)

                    #         if match:
                    #             # Extract the matched content and convert it to a dictionary
                    #             bl_info_str = match.group()
                    #             bl_info_dict = eval(bl_info_str)

                    #             print(bl_info_dict)
                    #             config_json["installed_blender_versions"][path_0.name]["addons"][path_1.name]["bl_info"] = bl_info_dict
                    #         else:
                    #             print("bl_info not found in the file.")
                    # except FileNotFoundError:
                    #     print(f"File not found: {file_path}")
                    # except UnicodeDecodeError:
                    #     print(f"Error decoding file: {file_path}")
                    # except SyntaxError:
                    #     print("Syntax error: Could not parse bl_info dictionary.")


                    # try:
                    #     # Open the file in read mode with explicit encoding specification
                    #     with open(init_file_path, "r", encoding="utf-8") as file:
                    #         # Read the entire contents of the file
                    #         file_contents = file.read()
                    #         print(file_contents)
                    # except FileNotFoundError:
                    #     print(f"File not found: {init_file_path}")
                    # except UnicodeDecodeError:
                    #     print(f"Error decoding file: {init_file_path}")


                    # init_file_path = path_1 / "__init__.py"
                    # print(init_file_path)
                    
                    # # Convert the file path to a package name
                    # package_name = "custom_module"

                    # # Load the script as a module
                    # spec = importlib.util.spec_from_file_location(package_name, init_file_path)
                    # module = importlib.util.module_from_spec(spec)
                    # spec.loader.exec_module(module)

                    # bl_info = module.bl_info
                    # config_json["installed_blender_versions"][path_0.name]["addons"][path_1.name]["bl_info"] = bl_info
