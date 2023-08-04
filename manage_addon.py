import bpy
from pathlib import Path
import time

# Get the directory where the script is located
script_directory = Path(__file__).resolve().parent

# Construct the file path based on the script directory
file_path = script_directory / "example.txt"

start = time.time()

try:
    # Open the file in write mode ('w')
    with file_path.open('w') as file:
        
        # Write the content to the file
        for addon in bpy.context.preferences.addons:
            addon_module = addon.module
            file.write(f"{addon_module} \n")
    
        end = time.time()
        file.write(str(end - start))        
except Exception as e:
    print(f"An error occurred: {e}")


# import bpy
# import os
# import time

# # Get the directory where the script is located
# script_directory = os.path.dirname(os.path.realpath(__file__))

# # Construct the file path based on the script directory
# file_path = os.path.join(script_directory, "example.txt")

# start = time.time()

# try:
#     # Open the file in write mode ('w')
#     with open(file_path, 'w') as file:
        
#         # Write the content to the file
#         for i in range(len(bpy.context.preferences.addons)):
#             addon_module = bpy.context.preferences.addons[i].module
#             file.write(f"{addon_module} \n")
    
#         end = time.time()
#         file.write(str(end - start))        
# except Exception as e:
#     print(f"An error occurred: {e}")


# import bpy
# import time

# file_path = "C:\\Users\\J\\Desktop\\PA\\code\\blender-conf-file-generator\\example.txt"
# # import addon_utils

# start = time.time()

# try:
#     # Open the file in write mode ('w')
#     with open(file_path, 'w') as file:
        
#         # Write the content to the file
#         for i in  range(0, len(bpy.context.preferences.addons)):
#             # print(bpy.context.preferences.addons[i].module)
#             file.write(f"{bpy.context.preferences.addons[i].module} \n")
    
#         end = time.time()
#         # print(end-start)
#         file.write(str(end-start))        
#     # print(f"Content written to '{file_path}' successfully.")
    
# except Exception as e:
#     print(f"An error occurred: {e}")

# import addon_utils
# import bpy

# all_addons = addon_utils.modules()
# for addon in all_addons:
#     print(addon.__name__)


# import bpy
# import time

# file_path = "C:\\Users\\J\\Desktop\\PA\\code\\blender-conf-file-generator\\example.txt"
# # import addon_utils

# start = time.time()

# try:
#     # Open the file in write mode ('w')
#     with open(file_path, 'w') as file:
        
#         # Write the content to the file
#         for i in  range(0, len(bpy.context.preferences.addons)):
#             # print(bpy.context.preferences.addons[i].module)
#             file.write(f"{bpy.context.preferences.addons[i].module} \n")
    
#         end = time.time()
#         # print(end-start)
#         file.write(str(end-start))        
#     # print(f"Content written to '{file_path}' successfully.")
    
# except Exception as e:
#     print(f"An error occurred: {e}")



# import bpy
# # import addon_utils

# for i in  range(0, len(bpy.context.preferences.addons)):
#     print(bpy.context.preferences.addons[i].module)
    
# import addon_utils


# all_addons = addon_utils.modules()
# for addon in all_addons:
#     print(addon.__name__)
    
# import addon_utils

# all_addons = addon_utils.modules()
# count = 0
# for addon in all_addons:
#     count+=1
#     print(count, " ", addon.__name__)


# import bpy
# import time
# def get_addon_module(addon_name):
#     for mod in bpy.context.preferences.addons:
#         if mod.module == addon_name:
#             return mod.module
#     return None

# def import_addon_module(addon_name):
#     addon_module = get_addon_module(addon_name)
#     if addon_module:
#         try:
#             return __import__(addon_module)
#         except ImportError:
#             return None
#     return None

# def print_addon_info(addon_name):
#     addon_module = import_addon_module(addon_name)
#     if addon_module:
#         bl_info = getattr(addon_module, "bl_info", {})
#         print(f"Addon Name: {bl_info.get('name', 'N/A')}")
#         print(f"Version: {bl_info.get('version', 'N/A')}")
#         print(f"Author: {bl_info.get('author', 'N/A')}")
#         print(f"Description: {bl_info.get('description', 'N/A')}")
#         print(f"Category: {bl_info.get('category', 'N/A')}")
#     else:
#         print(f"Addon '{addon_name}' not found.")
# #
# def disable_addon(addon_name):
#     bpy.ops.preferences.addon_disable(module=addon_name)
#     print(f"Addon '{addon_name}' disabled.")
#     print_addon_info(addon_name)

# def enable_addon(addon_name):
#     bpy.ops.preferences.addon_enable(module=addon_name)
#     print(f"Addon '{addon_name}' enabled.")
#     print_addon_info(addon_name)

# # Replace 'addon_name_here' with the actual name of the addon you want to disable or enable.
# addon_name_to_manage = 'physical-starlight-atmosphere'

# # time.sleep(10)

# # Check if the addon is currently enabled.
# if addon_name_to_manage in bpy.context.preferences.addons.keys():
#     # If the addon is enabled, disable it.
#     disable_addon(addon_name_to_manage)
# else:
#     # If the addon is disabled, enable it.
#     enable_addon(addon_name_to_manage)
