# kill a process
exec { 'killmenow':
    path     => '/usr/bin:/usr/sbin:/bin',
    command => 'pkill killmenow',
    onlyif => '/usr/bin/pgrep killmenow'
}