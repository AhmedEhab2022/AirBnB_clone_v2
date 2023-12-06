#!/usr/bin/python3
"""
Module contain fabric script with do_pack function
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static
    """
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(date)
    local("tar -cvzf {} web_static".format(path))
    if os.path.exists(path):
        return path
    else:
        return None
