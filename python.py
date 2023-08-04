import subprocess

# Path to the Blender executable
blender_executable = "C:\\Program Files\\Blender Foundation\\Blender 3.6\\blender-launcher.exe"

# Path to the script you want to execute
script_path = "C:\\Users\\J\\Desktop\\PA\\code\\blender-conf-file-generator\\manage_addon.py"

# Run Blender with the specified script
subprocess.run([blender_executable, "--python", script_path]) 