# Add a custom HTTP header
exec { 'update':
  command => '/usr/bin/env apt-get -y update',
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
