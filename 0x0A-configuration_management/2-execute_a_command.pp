#create a manifest that kills a process named killmenow.
#Must use the exec Puppet resource
#Must use pkill

exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin/'
}
