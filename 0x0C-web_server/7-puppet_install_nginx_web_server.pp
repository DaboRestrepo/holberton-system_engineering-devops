# Install Nginx web server (w/ Puppet)
exec { 'update':
    command => 'sudo apt-get update',
    provider => 'shell',
}
package { 'nginx':
    ensure => installed,
    require => Exec['update'],
}
file { '/var/www/html/index.html':
    ensure => present,
    content => 'Hellow World',
}
file_line { 'redirec':
    ensure => present,
    path => '/etc/nginx/sites-available/default',
    after => 'server_name _;',
    line => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}
service { 'nginx':
    ensure => running,
    require => Package['nginx'],
}
