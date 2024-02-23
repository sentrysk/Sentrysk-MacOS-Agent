#!/usr/bin/env python3

# Libraries
##############################################################################
import importlib.metadata as metadata
import logging
##############################################################################

# Functions
##############################################################################
def get_pip_packages():
    try:
        # Get a list of all installed packages
        installed_packages = []
        for package in metadata.distributions():
            installed_packages.append({
                "name":package.metadata['Name'],
                "version":package.metadata['Version']
            })
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
