# kill a process
exec { 'killmenow':
    command => 'usr/bin/bash/pkill killmenow'
}