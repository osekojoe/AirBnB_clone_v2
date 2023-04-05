#!/usr/bin/python3
""" 
1. Generates a .tgz archive from the contents of the web_static folder
2. Deploy archive to web server
"""

from datetime import datetime
from os.path import isdir, isfile
from fabric.api import *


def do_pack():
	"""generates a .tgz archive from folder contents"""
	try:
		date = datetime.now().strftime("%Y%m%d%H%M%S")
		if isdir('versions') is False:
			local("mkdir versions")
		filename = "versions/web_static_{}.tgz".format(date)
		local("tar -cvzf {} web_static".format(filename))

		return filename
	except:
		return None

def do_deploy(archive_path):
	"""Deploy archive to web server"""
	if isfile(archive_path) is False:
		return False
	try:
		archive_path_split = archive_path.replace('/', ' ').replace('.', ' ')
		archive_parent_dir = archive_path_split[0]
		archivename_no_gz = archive_path_split[1]
		archivename_gz = archive_path_split[1] + '.' + archive_path_split[2]
		dest_folder = '/data/web_static/releases/{}/'.format(archivename_no_gz)
		put(archive_path, '/tmp/')
		run('mkdir -p {}'.format(foldername))
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
