# This Puppet script installs nginx and configures it

# Ensure nginx package is present
package {'nginx':
  ensure => 'present',
}

# Execute command to update package lists and install nginx
exec {'install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,
}

# Create a basic index.html file with "Hello World!" content
exec {'create_hello_file':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

# Modify nginx configuration to add a redirection
exec {'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/elouardy.com\/;\\n\\t}/" /etc/nginx/sites-available/default':
  provider => shell,
}

# Restart nginx service to apply changes
exec {'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}

