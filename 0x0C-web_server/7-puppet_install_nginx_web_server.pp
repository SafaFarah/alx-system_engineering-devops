# Setup New Ubuntu server with nginx

exec { 'update system':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
	ensure => 'installed',
	require => Exec['update system']
}

file {'/var/www/html/index.html':
	content => 'Hello World!'
}

file {'/etc/nginx/sites-available/default':
	content => 'server {
    listen 80;
    listen [::]:80 default_server;
    root   /etc/nginx/html;
    index  index.html;
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}'
}


service {'nginx':
	ensure => running,
	require => Package['nginx']
}
