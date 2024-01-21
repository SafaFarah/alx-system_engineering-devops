#Puppet to make changes to our configuration file.
#SSH client configuration must be configured to use the private key ~/.ssh/school
#SSH client configuration must be configured to refuse to authenticate using a password

include stdlib
file_line { 'Disabling password ':
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  replace => true,
}

file_line { 'change Identity File':
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/school',
  replace => true,
}
