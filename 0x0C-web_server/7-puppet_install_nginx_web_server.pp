#installs a nginx server

exec {'install_nginx':
    command => 'sudo apt-get -y update; sudo apt-get -y install nginx',
    unless  => '/usr/bin/dpkg -l | grep nginx',
}

exec {'index_html':
    command => "echo 'Hello World!' > /var/www/html/index.html",
}

exec {'redirect_config':
    command => "sudo sed -i 's/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/www.youtube.com\/watch?v=dQw4w9WgXcQ permanent;/' /etc/nginx/sites-available/default"
}

exec {'reload_nginx':
    command => 'sudo service nginx start',
}
