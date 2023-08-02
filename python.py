import subprocess

# Path to the Blender executable
blender_executable = "C:\\Users\\usr\\Desktop\\blender-3.3.4-windows-x64\\blender-launcher.exe"

# Path to the script you want to execute
script_path = "C:\\Users\\usr\\Desktop\\Physical addons\\code\\test_BVM\\manage_addon.py"

# Run Blender with the specified script
subprocess.run([blender_executable, "--python", script_path])