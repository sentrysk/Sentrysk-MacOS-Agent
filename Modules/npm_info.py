#!/usr/bin/env python3

# Libraries
##############################################################################
import json
import subprocess
import logging
##############################################################################


# Functions
##############################################################################
def get_npm_packages():
    try:
        # Check if npm is installed
        subprocess.run('npm -v', capture_output=True, check=True, shell=True)

        # NPM is installed, collect packages and versions
        completed_process = subprocess.run(
            'npm list -g --depth=0 --json', 
            capture_output=True, 
            check=True, 
            shell=True
        )
        package_list = json.loads(completed_process.stdout)['dependencies']
        
        installed_packages = []
        for package_name, package_info in package_list.items():
            package = {"name": package_name, "version": package_info['version']}
            installed_packages.append(package)

        return {
            "is_installed": True,
            "packages": installed_packages
        }
    except Exception as e:
        # Log the error
        logging.error(e)
        return {
            "is_installed": False,
            "packages": []
        }


##############################################################################