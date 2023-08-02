import addon_utils

all_addons = addon_utils.modules()
for addon in all_addons:
    print(addon.__name__)
    
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
