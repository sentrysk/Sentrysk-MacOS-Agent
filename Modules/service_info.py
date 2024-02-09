#!/usr/bin/env python3

# Libraries
##############################################################################
import subprocess
import logging
##############################################################################

# Functions
##############################################################################
def get_macos_services():
    try:
        result = subprocess.run(["sudo", "launchctl", "list"], capture_output=True, text=True, check=True)
        return result.stdout.strip().split('\n')
    except subprocess.CalledProcessError as e:
        logging.error(e)
        return []

def get_macos_service_status(service_name):
    try:
        result = subprocess.run(["sudo", "launchctl", "list", service_name], capture_output=True, text=True, check=True)
        status_line = result.stdout.strip().split('\n')[-1]
        status = status_line.split()[0]
        return status
    except subprocess.CalledProcessError as e:
        logging.error(e)
        return "-"

def get_macos_service_description(service_name):
    try:
        result = subprocess.run(["sudo", "launchctl", "list", service_name], capture_output=True, text=True, check=True)
        description_line = result.stdout.strip().split('\n')[1]
        description = description_line.split('\t')[1].strip()
        return description
    except subprocess.CalledProcessError as e:
        logging.error(e)
        return "-"

def parse_macos_service(line):
    service_name = line.split()[0]
    return {
        "display_name": line.split()[2],
        "service_name": service_name,
        "status": get_macos_service_status(service_name), 
        "description": get_macos_service_description(service_name)
    }

def get_service_info():
    services = get_macos_services()
    services_info = [parse_macos_service(line) for line in services]
    services_json = {"services": services_info}
    return services_json
##############################################################################