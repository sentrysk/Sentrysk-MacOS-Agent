#!/usr/bin/env python3

# Libraries
##############################################################################
import json
from configparser import ConfigParser,ExtendedInterpolation
import logging

from Modules.system_info import get_system_info
from Modules.user_info import get_user_info
from Modules.installed_apps import get_installed_programs
from Modules.npm_info import get_npm_packages
from Modules.service_info import get_service_info
from Modules.pip_info import get_pip_packages
from Modules.docker_info import get_docker_info
from Modules.last_logon import get_last_logons
##############################################################################

# Configs
##############################################################################
CONFIG_FILE = 'config.ini'

config = ConfigParser(interpolation=ExtendedInterpolation())
config.read(CONFIG_FILE)

DASHBOARD_URL   = config.get('dashboard','url')
LOGFILE         = config.get('logging','logfile')


FORMAT = '%(asctime)s :: %(levelname)-6s :: %(name)s :: [%(filename)s:%(lineno)s - %(funcName)s()] :: %(message)s'
# Configure logging to write logs to a log file
logging.basicConfig(
    filename=LOGFILE, 
    level=logging.INFO,
    format=FORMAT,
    encoding='utf-8'
)
##############################################################################

# Functions
##############################################################################
"""
    Retrieve system information.
"""

system_info = {}

system_info['system']               = get_system_info()
system_info['users']                = get_user_info()
system_info['installed_programs']   = get_installed_programs()
system_info['npm_info']             = get_npm_packages()
system_info['services']             = get_service_info()
system_info['pip_info']             = get_pip_packages()
system_info['docker_info']          = get_docker_info()
system_info['last_logons']          = get_last_logons()
##############################################################################


# Usage
json_data = json.dumps(system_info, indent=4)
with open('result.json','w') as f:
    f.write(json_data)
print(json_data)
