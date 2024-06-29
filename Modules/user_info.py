#!/usr/bin/env python3

# Libraries
##############################################################################
import pwd
import logging
##############################################################################

# Functions
##############################################################################
def get_user_info():
    try:
        # Initialize an empty list to store user information
        users = []

        # Iterate through the user entries in the /etc/passwd file
        for entry in pwd.getpwall():
            user_info = {
                "username": str(entry.pw_name),
                "user_id": str(entry.pw_uid),
                "group_id": str(entry.pw_gid),
                "home_directory": str(entry.pw_dir),
                "shell": str(entry.pw_shell),
            }
            users.append(user_info)
            
        return users
    except Exception as e:
        # Log the error
        logging.error(e)
        return []
##############################################################################
