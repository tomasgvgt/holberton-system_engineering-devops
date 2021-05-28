#change limit on nginx
exec { 'increase-limit':
  command => "sudo sed -i 's/15/10000/' /etc/default/nginx;
              sudo service nginx restart",
  path    => '/bin/',
}
