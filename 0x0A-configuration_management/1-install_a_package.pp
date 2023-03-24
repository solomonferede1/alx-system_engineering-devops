# install flask using pip3

exec { 'flask':
  command => '/usr/bin/apt pip3 install flask -v 2.1.0',
}
