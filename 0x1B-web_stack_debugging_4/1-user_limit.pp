#remove limit for holberton
exec { 'remove-limit':
  command => "sed -i '$ d' /etc/security/limits.conf;
              sed -i '$ d' /etc/security/limits.conf;
              sed -i '$ d' /etc/security/limits.conf",
  path    => '/bin/',
}
