#Kill a process named killmenow, using puppet
exec { 'kill a process':
  path    => '/usr/bin/',
  command => 'pkill killmenow'
}
