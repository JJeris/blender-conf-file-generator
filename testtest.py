from pathlib import Path
path = Path("C:\\Users\\J\\AppData\\Roaming\\Blender Foundation\\Blender\\3.6\\scripts\\addons")
print(path)
subdirectory_path = path / "disabled_addon_dir"
if not subdirectory_path.exists():
    subdirectory_path.mkdir()
    print("OK")