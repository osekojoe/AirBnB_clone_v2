#!/usr/bin/python3
""" Generates a .tgz archive from the contents of the web_static folder
"""


from datetime import datetime
from os.path import isdir
from fabric.api import local


def do_pack():
	"""generates a .tgz archive from folder contents
	"""
	try:
		date = datetime.now().strftime("%Y%m%d%H%M%S")
		if isdir('versions') is False:
			local("mkdir versions")
		filename = "versions/web_static_{}.tgz".format(date)
		local("tar -cvzf {} web_static".format(filename))

		return filename
	except:
		return None
