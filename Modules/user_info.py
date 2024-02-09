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
                "username": entry.pw_name,
                "user_id": entry.pw_uid,
                "group_id": entry.pw_gid,
                "home_directory": entry.pw_dir,
                "shell": entry.pw_shell,
            }
            users.append(user_info)
            
        return users
    except Exception as e:
        # Log the error
        logging.error(e)
        return []
##############################################################################
