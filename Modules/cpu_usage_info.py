#!/usr/bin/env python3

# Libraries
##############################################################################
import psutil
import logging
##############################################################################

# Functions
##############################################################################
def get_cpu_usage_info():
    # CPU Information
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        return {
            "cpu_usage": cpu_usage
        }
    except Exception as e:
        # Log the error
        logging.error(e)
##############################################################################