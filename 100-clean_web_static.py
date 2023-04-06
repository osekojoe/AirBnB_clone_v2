#!/usr/bin/python3
"""
1. Generates a .tgz archive from the contents of the web_static folder
2. Deploy archive to web server
3. Full deploy
"""


from datetime import datetime
from os.path import exists, isdir
from fabric.api import local, put, run, env


env.hosts = ['54.236.26.66', '54.159.23.136']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa.pub'


def do_pack():
    """generates a .tgz archive from folder contents"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir('versions') is False:
            local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except Exception:
        return None


def do_deploy(archive_path):
    """Deploy archive to web server"""
    if exists(archive_path) is False:
        return False
    try:
        path_split = archive_path.replace('/', ' ').replace('.', ' ').split()
        archive_parent_dir = path_split[0]
        archivename_no_gz = path_split[1]
        archivename_gz = path_split[1] + '.' + path_split[2]
        dest_folder = '/data/web_static/releases/{}/'.format(archivename_no_gz)
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(dest_folder))
        run('tar -xzf /tmp/{} -C {}/'.format(archivename_gz, dest_folder))
        run('rm /tmp/{}'.format(archivename_gz))
        run('mv {}/web_static/* {}'.format(dest_folder, dest_folder))
        run('rm -rf {}/web_static'.format(dest_folder))
        current = '/data/web_static/current'
        run('rm -rf {}'.format(current))
        run('ln -s {}/ {}'.format(dest_folder, current))
        return True
    except Exception:
        return False


def deploy():
    """Full deploy web content"""
    archive_path = do_pack()
    if archive is None:
        return False
    return do_deploy(archive_path)


def do_clean(number=0):
    """deletes out-of-date archives"""
    number = int(number)

    if number in (0, 1):
        number = 1
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
