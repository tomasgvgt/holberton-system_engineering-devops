#change limit on nginx
exec { 'increase-limit':
  command => "sudo sed -i '$ d' /etc/default/nginx;
              sudo service nginx restart",
  path    => ['/usr/bin', '/usr/local/bin', '/usr/sbin', '/usr/local/sbin'],
}
