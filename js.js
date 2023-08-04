const { spawn } = require('child_process');

// Path to the Blender executable
const blenderExecutable = "C:\\Program Files\\Blender Foundation\\Blender 3.6\\blender-launcher.exe";

// Path to the script you want to execute
const scriptPath = "C:\\Users\\J\\Desktop\\PA\\code\\blender-conf-file-generator\\manage_addon.py";

// Run Blender with the specified script
const subprocess = spawn(blenderExecutable, ['--python', scriptPath]);

// Handle subprocess events
subprocess.on('close', (code) => {
  console.log(`Blender process exited with code ${code}`);
});

subprocess.on('error', (error) => {
  console.error(`Error occurred: ${error.message}`);
});