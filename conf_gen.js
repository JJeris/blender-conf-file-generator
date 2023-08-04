const fs = require('fs');
const path = require('path');

const OS_NAME = process.platform;
const CONFIG_JSON_FILE_NAME = 'config.json';
const config_json = {
  date_when_last_generated: null,
  os_on_which_generated: null,
  blender_foundation_path: null,
  installed_blender_versions: {}
};
const SCRIPT_NAME = '__init__';

function comp_fn_generate_config() {
  const start_time = Date.now();
  config_json.date_when_last_generated = new Date().toISOString();

  if (OS_NAME === 'win32') {
    config_json.os_on_which_generated = OS_NAME;
    const ADDON_SOURCE_PATH = path.join(
      process.env.APPDATA,
      'Blender Foundation',
      'Blender'
    );
    config_json.blender_foundation_path = ADDON_SOURCE_PATH;

    fs.readdirSync(ADDON_SOURCE_PATH).forEach((versionDir) => {
      const cleanedItem = versionDir.replace('.', '').replace('-', '');
      if (!isNaN(cleanedItem)) {
        config_json.installed_blender_versions[versionDir] = {
          blender_exe_path: null,
          scripts_path: path.join(
            ADDON_SOURCE_PATH,
            versionDir,
            'scripts',
            'addons'
          ),
          addons: {}
        };

        const SCRIPTS_SOURCE_PATH =
          config_json.installed_blender_versions[versionDir].scripts_path;

        fs.readdirSync(SCRIPTS_SOURCE_PATH).forEach((addonDir) => {
          const addonPath = path.join(
            SCRIPTS_SOURCE_PATH,
            addonDir,
            SCRIPT_NAME + '.py'
          );
          if (
            addonDir !== '__pycache__' &&
            fs.statSync(path.join(SCRIPTS_SOURCE_PATH, addonDir)).isDirectory()
          ) {
            config_json.installed_blender_versions[versionDir].addons[
              addonDir
            ] = {
              bl_info: { init_path: addonPath },
              statuss: {
                installed: true,
                enabled: true
              }
            };
          }
        });
      }
    });

    const BLENDER_SOURCE_PATH = path.join('C:\\', 'Program Files', 'Blender Foundation');
    fs.readdirSync(BLENDER_SOURCE_PATH).forEach((versionDir) => {
      config_json.installed_blender_versions[versionDir] = config_json.installed_blender_versions[versionDir] || {};
      fs.readdirSync(path.join(BLENDER_SOURCE_PATH, versionDir)).forEach((subDir) => {
        if (subDir === 'blender.exe') {
          config_json.installed_blender_versions[versionDir].blender_exe_path = path.join(
            BLENDER_SOURCE_PATH,
            versionDir,
            subDir
          );
        }
      });
    });

    fs.writeFileSync(CONFIG_JSON_FILE_NAME, JSON.stringify(config_json, null, 2));
    const end_time = Date.now();
    console.log(end_time - start_time);
  }
}

function main() {
  comp_fn_generate_config();
}

main();
