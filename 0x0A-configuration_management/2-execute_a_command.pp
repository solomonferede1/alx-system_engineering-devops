# Create a manifest that kills a proccess named killmenow

exec {'killmenow':
command => '/usr/bin/pkill --full killmenow'
    }
