# Prepare servers for web deployment

exec {'update ubuntu system':
	provider => shell,
	command => 'sudo apt-get -y update',
}

exec {'install nginx':
	provider => shell,
	command => 'sudo apt-get -y install nginx',
}

exec {'create dir /data/web_static/releases/test/':
	provider => shell,
	command => 'sudo mkdir -p /data/web_static/releases/test/',
}

exec {'create dir /data/web_static/shared/':
	provider => shell,
	command => 'sudo mkdir -p /data/web_static/shared/',
}

exec {'create fake html file':
	provider => shell,
	command => 'echo "Test page!" | sudo tee /data/web_static/releases/test/index.html',
}

exec {'creake symlink':
	provider => shell,
	command => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
}

file {'/data/':
	ensure => directory,
	owner => 'ubuntu',
	group => 'ubuntu',
	recurse => true,
}

exec {'update nginx config':
	provider => shell,
	command => 'sudo sed -i "/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
}

exec {'restart nginx':
	provider => shell,
	command => 'sudo service nginx restart'
}
