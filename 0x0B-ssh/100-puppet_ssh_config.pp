# Change the config file with puppet
file_line { 'Passwd off':
    path => '/etc/ssh/ssh_config',
    line => 'PasswordAuthentication no',
}

file_line {'Identity File':
    path => '/etc/ssh/ssh_config',
    line => 'IdentityFile ~/.ssh/school',
}
