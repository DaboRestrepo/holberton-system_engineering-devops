# Use strace to debugging the server.
exec { 'deb_wordpress':
    command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
    path    => '/usr/bin/:/bin/',
}
