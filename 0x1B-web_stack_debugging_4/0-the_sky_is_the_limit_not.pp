# increase the ULIMIT of the default/nginx

exec {'ULIMIT':
  provider => shell,
  command  => 'sed -i "s/15/4096/" /etc/default/nginx',
}

exec {'nginx restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
