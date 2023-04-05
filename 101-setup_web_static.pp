# Prepare servers for web deployment

exec {'update ubuntu system':
	provider => bash,
	command => 'sudo apt-get -y update',
}

exec {'install nginx':
	provider => bash,
	command => 'sudo apt-get -y install nginx',
}

exec {'create dir /data/web_static/releases/test/':
	provider => bash,
	command => 'sudo mkdir -p /data/web_static/releases/test/',
}

exec {'create dir /data/web_static/shared/':
	provider => bash,
	command => 'sudo mkdir -p /data/web_static/shared/',
}

exec {'create fake html file':
	provider => bash,
	command => 'echo "Test page!" | sudo tee /data/web_static/releases/test/index.html',
}

exec {'creake symlink':
	provider => bash,
	command => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
}

file {'/data/':
	ensure => directory,
	owner => 'ubuntu',
	group => 'ubuntu',
	recurse => true,
}

exec {'update nginx config':
	provider => bash,
	command => 'sudo sed -i "/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
}

exec {'restart nginx':
	provider => bash,
	command => 'sudo service nginx restart'
}
