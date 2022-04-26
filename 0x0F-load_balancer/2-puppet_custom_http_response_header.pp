# Add a custom HTTP header with Puppet
exec { 'update':
    command  => 'sudo apt-get update',
    provider => shell,
}
package { 'nginx':
    ensure  => installed,
    require => exec['update'],
}
file_line { 'header_custom':
    ensure  => present,
    path    => '/etc/nginx/sites-enabled/default',
    after   => 'server_name _;',
    line    => 'add_header X-Served-By $(hostname);',
    require => package['nginx'],
}
service { 'nginx':
    ensure  => 'running',
    require => file_line['header_custom'],
}
