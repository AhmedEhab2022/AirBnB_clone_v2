#!/usr/bin/python3
"""
Module contain fabric script with do_deploy function
"""
from fabric.api import env, put, run
import os


env.hosts = ['35.174.185.16', '34.229.72.168']
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"


def do_deploy(archive_path):
    """
    Fabric script (based on the file 1-pack_web_static.py)
    that distributes an archive to your web servers,
    using the function do_deploy
    """

    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        archive_name = archive_path.split("/")[-1]
        no_ext = archive_name.split(".")[0]
        unCompPath = "/data/web_static/releases"
        run("mkdir -p {}/{}".format(unCompPath, no_ext))
        run("tar -xzf /tmp/{} -C {}/{}/".format(archive_name,
                                                unCompPath, no_ext))
        run("rm /tmp/{}".format(archive_name))
        run("mv {}/{}/web_static/* {}/{}/".format(unCompPath, no_ext,
                                                  unCompPath, no_ext))

        run("rm -rf {}/{}/web_static".format(unCompPath, no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/{}/ /data/web_static/current".format(unCompPath,
                                                           no_ext))
        return True
    except:
        return False
