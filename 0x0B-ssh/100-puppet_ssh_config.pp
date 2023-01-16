# setting up client config file
include stdlib

file_line { 'No authentication':
    ensure => present,
    path => '/etc/ssh/ssh_config',
    line => '  PasswordAuthentication no',
    replace => true,
}

file_line { 'identity file':
    ensure => present,
    path => '/etc/ssh/ssh_config',
    line => '  IdentityFile ~/.ssh/school',
    replace => true,
}
