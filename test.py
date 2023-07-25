import importlib
from pathlib import Path
import sys

# Specify the name of the script without the '.py' extension
script_name = "node2json"

# Add the path to the directory containing the 'Node-2-JSON' addon
addon_path = Path("C:/Users/J/AppData/Roaming/Blender Foundation/Blender/3.6/scripts/addons")
addon_path_str = str(addon_path)
if addon_path_str not in map(str, Path(sys.path)):
    sys.path.append(addon_path_str)

# Load the script as a module
module = importlib.import_module(f"Node-2-JSON.{script_name}")

# Access the bl_info dictionary
bl_info = module.bl_info

# Access and call functions from the module
node_tree = ...  # Replace this with the node_tree object you want to pass as an argument
node_groups = ...  # Replace this with the node_groups dictionary you want to pass as an argument

result = module.generate_dict_from_node_tree(node_tree, node_groups)
# Replace `node_tree` and `node_groups` with appropriate values that you want to pass as arguments to the function.

# You can access and call other functions in the same way.
# For example:
# result2 = module.some_other_function(arg1, arg2)

# Remember to remove the added path from sys.path if you no longer need it.
if addon_path_str in map(str, Path(sys.path)):
    sys.path.remove(addon_path_str)

print(bl_info)