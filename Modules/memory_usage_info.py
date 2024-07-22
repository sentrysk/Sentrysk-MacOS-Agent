#!/usr/bin/env python3

# Libraries
##############################################################################
import psutil
import logging
##############################################################################

# Functions
##############################################################################
def get_memory_usage_info():
    try:
        # Memory Information
        memory = psutil.virtual_memory()
        return {
            'total_size': memory.total,
            'used_size': memory.used
        }
    except Exception as e:
        # Log the error
        logging.error(e)
##############################################################################