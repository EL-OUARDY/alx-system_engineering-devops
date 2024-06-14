# Manuscript reconfigure Nginx 
# increase the amount of traffic that the server can handle

# increase ULIMIT
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# restart server
-> exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
