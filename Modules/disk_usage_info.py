#!/usr/bin/env python3

# Libraries
##############################################################################
import psutil
import logging
##############################################################################

# Functions
##############################################################################
def get_disk_usage_info():
 # Disk Information
    partitions = psutil.disk_partitions()
    disk_info_list = []
    for partition in partitions:
        try:
            disk_usage = psutil.disk_usage(partition.mountpoint)
            disk_info_list.append({
                'device': partition.device,
                'total_size': disk_usage.total,
                'used_size': disk_usage.used,
                'free_size': disk_usage.free
            })
        except PermissionError as e:
            # Log the error
            logging.error(e)
            # Ignore disks that we don't have permission to access
            continue

    return disk_info_list
##############################################################################