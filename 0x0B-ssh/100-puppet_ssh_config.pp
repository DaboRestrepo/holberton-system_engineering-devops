# Change the config file with puppet
Include stdlib
file_line { 'Turn off password auth':
    path    => '/etc/ssh/sshd_config',
    line    => '    PasswordAuthentication no',
    replace => true,
}

file_line {'Declare Identity File':
    path    => '/etc/ssh/sshd_config',
    line    => '    IdentityFile ~/.ssh/school',
    replace => true,
}
