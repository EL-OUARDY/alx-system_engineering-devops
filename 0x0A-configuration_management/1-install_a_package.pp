#!/usr/bin/pup
# install Python version (3.8.10)
package { 'python3.8':
  ensure => '3.8.10',
}

# install pip
package { 'python3-pip':
  ensure => present,
}

# install flask version (2.1.0) from pip
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Package['python3-pip'],
}

# Install Werkzeug version (2.1.1)
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip',
  require  => Package['python3-pip'],
}
