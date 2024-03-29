# Setup New Ubuntu server with nginx


package { 'nginx':
provider => 'apt',
}

exec {'hlbtn_page':
command => '/usr/bin/sudo /bin/echo Holberton School > /var/www/html/index.nginx-debian.html',
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

exec {'start_server':

command => '/usr/bin/sudo /usr/sbin/service nginx start',
}
