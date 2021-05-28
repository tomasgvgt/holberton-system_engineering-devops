#change limit on nginx
exec { 'increase-limit':
  command => "sed -i 's/15/10000/' /etc/default/nginx;
              service nginx restart",
  path    => '/bin/',
}
