#!/usr/bin/env python3

# Libraries
##############################################################################
import subprocess
import json
##############################################################################

# Functions
##############################################################################
def get_installed_programs():
    try:
        # Execute the shell command to list installed applications
        installed_apps_output = subprocess.check_output(
            ["system_profiler", "SPApplicationsDataType", "-json"],
            stderr=subprocess.STDOUT
        )
        # Load Output to JSON
        installed_apps_output = json.loads(installed_apps_output)
        # Get First Element Values
        installed_apps_output = installed_apps_output.get("SPApplicationsDataType")
        
        installed_apps = []
        for app in installed_apps_output:
            app_info = {}
            app_info["name"] = app.get("_name")
            app_info["version"] = app.get("version")
            app_info["installed_by"] = app.get("obtained_from")
            installed_apps.append(app_info)
        
        return installed_apps

    except subprocess.CalledProcessError as e:
        print("Error:", e.output.decode('utf-8'))

##############################################################################