# Create a file /tmp/school

str = "I love Puppet"
file { '/tmp/school':
    ensure => 'file',
    path => '/tmp/school
    owner => 'www-data',
    group => 'www-data',
    mode => 0744,
    content => $str
}