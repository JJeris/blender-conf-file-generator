"""
This code launches a specified Blender version, 
retrieving its .exe path from a config file.

Author: @JJeris

"""


import json
from pathlib import Path
import subprocess




def comp_fn_run_blender_version():
    with open("config.json", "r") as config_json_file:
        config_json_data = json.load(config_json_file)

    VERSIONS = [version for version in config_json_data["installed_blender_versions"]]
    blender_version = str(input(f"Choose a valid Blender version from the list {VERSIONS}:"))
    while(blender_version not in VERSIONS):
        print("ERR: No such version was found.")
        blender_version = float(input(f"Choose a valid Blender version from the list {VERSIONS}:"))
        
    # print(blender_version)
    # print out a list from config file.
    # search the specified Blender version .exe and print it out and launch it.
    blender_exe_path = Path(config_json_data["installed_blender_versions"][blender_version]["blender_exe_path"])

    # print(blender_exe_path)

    addon_list = [addon for addon in config_json_data["installed_blender_versions"][blender_version]["addons"]]
    print(f"Installed addons: {addon_list}")
    # ok = 0   
    # while(ok == 0):
        
    #     count = 0
    #     print("Addons: ")
    #     for i in addon_list:
    #         print(f"{count}. {i}, enabled statuss: {config_json_data['installed_blender_versions'][blender_version]['addons'][i]['statuss']['enabled']}")
    #         count += 1

    #     ok = int(input("Continue launch config? 0/1"))
    #     enabled_or_disable = int(input("Enable or disable an addon? (True/False)"))
    #     if enabled_or_disable == 1:
    #         pass
    #         # enable
    #     elif enabled_or_disable == 0:
    #         ans = int(input(f"Which of these addons do you wish to disable? (0, 1, 2,...)"))
    #         while (addon_list[ans] not in addon_list):
    #             print("ERR: no such addon exists.")
    #             ans = int(input(f"Which of these addons do you wish to disable? (0, 1, 2,...)"))

            
    #         subdirectory_path = Path(config_json_data["installed_blender_versions"][blender_version]["scripts_path"] / "disabled_addon_dir")
    #         if not subdirectory_path.exists():
    #             subdirectory_path.mkdir()
            
    #         addon_path = Path(config_json_data["installed_blender_versions"][blender_version]["scripts_path"] / str(addon_list(ans)))
    #         addon_path.rename(subdirectory_path / addon_path)
    #         # find the addon dir,
    #         # move it into disabled_addon_dir

    #     ok = int(input("Continue launch config? 0/1"))
    #     exit()

    try:
        # Convert the Path object to a string using .resolve() to get the absolute path.
        exe_absolute_path = blender_exe_path.resolve()
        
        subprocess.run([exe_absolute_path], shell=True)

    except FileNotFoundError:
        print(f"Error: The specified .exe file '{blender_exe_path}' was not found.")
    except subprocess.CalledProcessError:
        print(f"Error: Failed to execute the .exe file '{blender_exe_path}'.")


def main():
    comp_fn_run_blender_version()

main()