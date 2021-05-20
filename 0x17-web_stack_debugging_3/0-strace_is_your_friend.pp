# Apache 500 error
exec { 'debug':
    command  => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
}
