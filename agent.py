#!/usr/bin/env python3

# Libraries
##############################################################################
import json
import os
import logging
import schedule
import requests
import time

from Modules.system_info import get_system_info
from Modules.user_info import get_user_info
from Modules.installed_apps import get_installed_programs
from Modules.service_info import get_service_info
from Modules.last_logon import get_last_logons
from Modules.pip_info import get_pip_packages
from Modules.npm_info import get_npm_packages
from Modules.docker_info import get_docker_info
from Modules.disk_usage_info import get_disk_usage_info
from Modules.memory_usage_info import get_memory_usage_info
##############################################################################

# Configs
##############################################################################
def load_config(file_path):
    with open(file_path, 'r') as file:
        config_data = json.load(file)
    return config_data

# Specify the path to your JSON configuration file
config_file_path = 'config.json'

# Load configuration from the JSON file
config = load_config(config_file_path)

# Extract information from the configuration
base_url = config['api']['base_url']
endpoints = config['api']['endpoints']
agent_token = config['api']['agent_token']

home_dir = config['dirs']['home_dir']
logs_dir = os.path.join(home_dir,'logs')
logfile_relative_path = config['dirs']['logfile']
logfile_path = os.path.join(home_dir, logfile_relative_path)

# Check if path not exist, create new one
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

FORMAT = '%(asctime)s :: %(levelname)-6s :: %(name)s :: [%(filename)s:%(lineno)s - %(funcName)s()] :: %(message)s'
# Configure logging to write logs to a log file
logging.basicConfig(
    filename=logfile_path, 
    level=logging.INFO,
    format=FORMAT,
    encoding='utf-8'
)

# Get Scheduled Jobs from Config
scheduled_jobs = config['scheduled_jobs']
##############################################################################

# Functions
##############################################################################
# System Info Sender Function
def send_system_info():
    try:
        url = str(base_url) + endpoints["system_info"]

        payload = json.dumps(get_system_info(), indent=4)

        headers = {
            'Authorization': agent_token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
    except Exception as e:
        print(e)

# Users Info Sender Function
def send_user_info():
    try:
        url = str(base_url) + endpoints["user_info"]

        payload = json.dumps({"users":get_user_info()})

        headers = {
            'Authorization': agent_token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
    except Exception as e:
        print(e)

# Installed Apps Info Sender Function
def send_installed_programs():
    try:
        url = str(base_url) + endpoints["installed_programs"]

        payload = json.dumps({"apps":get_installed_programs()})

        headers = {
            'Authorization': agent_token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
    except Exception as e:
        print(e)

# Services Info Sender Function
def send_service_info():
    try:
        url = str(base_url) + endpoints["service_info"]

        payload = json.dumps({"services":get_service_info()})

        headers = {
            'Authorization': agent_token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
    except Exception as e:
        print(e)

# Last Logons Info Sender Function
def send_last_logons():
    try:
        url = str(base_url) + endpoints["last_logons"]

        payload = json.dumps({"last_logons":get_last_logons()})

        headers = {
            'Authorization': agent_token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
    except Exception as e:
        print(e)

# Pip Packages Info Sender Function
def send_pip_packages():
    try:
        url = str(base_url) + endpoints["pip_pkgs"]

        pip_info = get_pip_packages()

        payload = json.dumps({
            "is_installed": pip_info["is_installed"],
            "pip_packages": pip_info["packages"]
        })

        headers = {
            'Authorization': agent_token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
    except Exception as e:
        print(e)

# Npm Packages Info Sender Function
def send_npm_packages():
    try:
        url = str(base_url) + endpoints["npm_pkgs"]

        npm_pkgs_info = get_npm_packages()

        payload = json.dumps({
            "is_installed": npm_pkgs_info["is_installed"],
            "npm_packages": npm_pkgs_info["packages"]
        })

        headers = {
            'Authorization': agent_token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
    except Exception as e:
        print(e)

# Docker Info Sender Function
def send_docker_info():
    try:
        url = str(base_url) + endpoints["docker_info"]

        docker_info = get_docker_info()

        payload = json.dumps(docker_info)

        headers = {
            'Authorization': agent_token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
    except Exception as e:
        print(e)

# Agent Config Sender Function
def send_agent_config():
    try:
        url = str(base_url) + endpoints["agent_config"]

        payload = json.dumps(config)

        headers = {
            'Authorization': agent_token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
    except Exception as e:
        print(e)

# Disk Usage Sender Function
def send_disk_usage():
    try:
        url = str(base_url) + endpoints["disk_usage"]

        payload = json.dumps({
           "disk_usage": get_disk_usage_info()
        })
        print(payload)
        headers = {
            'Authorization': agent_token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
    except Exception as e:
        print(e)

# Memory Usage Sender Function
def send_memory_usage():
    try:
        url = str(base_url) + endpoints["memory_usage"]

        payload = json.dumps(get_memory_usage_info())
        print(payload)
        headers = {
            'Authorization': agent_token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
    except Exception as e:
        print(e)

##############################################################################

# Schedule jobs
for job_name, job_config in scheduled_jobs.items():
    if "interval" in job_config:
        interval = job_config["interval"]
        unit = job_config.get("unit", "minutes")
        getattr(schedule.every(interval), unit).do(eval(job_name))
    elif "time" in job_config:
        time_str = job_config["time"]
        schedule.every().day.at(time_str).do(eval(job_name))

# Run 
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every 60 seconds