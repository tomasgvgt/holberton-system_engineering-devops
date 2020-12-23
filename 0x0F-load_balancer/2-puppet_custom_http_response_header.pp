# Add a custom HTTP header
# The name of the custom HTTP header must be X-Served-By
# The value of the custom HTTP header must be the hostname of the server Nginx is running on

exec { 'update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure => 'installed',
  name   => 'nginx',
}

file_line { 'add header':
  path  => '/etc/nginx/sites-available/default',
  line  => "\tadd_header X-Served-By ${hostname};",
  after => 'server_name _;',
}
exec { 'restart':
  command => '/usr/sbin/service nginx restart',
}
