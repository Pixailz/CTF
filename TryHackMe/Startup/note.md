ftp anon allowed

# URL FOUND
/files

lennie:c4ntg3t3n0ughsp1c3


# linPEAS output


```
./linPEAS.sh
 Starting linpeas. Caching Writable Folders...

                     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
             ▄▄▄▄▄▄▄             ▄▄▄▄▄▄▄▄▄
      ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄
  ▄▄▄▄     ▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄
  ▄    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  ▄▄▄▄▄▄▄▄▄▄▄          ▄▄▄▄▄▄               ▄▄▄▄▄▄ ▄
  ▄▄▄▄▄▄              ▄▄▄▄▄▄▄▄                 ▄▄▄▄ 
  ▄▄                  ▄▄▄ ▄▄▄▄▄                  ▄▄▄
  ▄▄                ▄▄▄▄▄▄▄▄▄▄▄▄                  ▄▄
  ▄            ▄▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄
  ▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄                                ▄▄▄▄
  ▄▄▄▄▄  ▄▄▄▄▄                       ▄▄▄▄▄▄     ▄▄▄▄
  ▄▄▄▄   ▄▄▄▄▄                       ▄▄▄▄▄      ▄ ▄▄
  ▄▄▄▄▄  ▄▄▄▄▄        ▄▄▄▄▄▄▄        ▄▄▄▄▄     ▄▄▄▄▄
  ▄▄▄▄▄▄  ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄   ▄▄▄▄▄ 
   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄        ▄          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
  ▄▄▄▄▄▄▄▄▄▄▄▄▄                       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  ▄▄▄▄▄▄▄▄▄▄▄                         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
   ▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄
        ▄▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄ 
             ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    linpeas v2.9.6 by carlospolop

ADVISORY: This script should be used for authorized penetration testing and/or educational purposes only. Any misuse of this software will not be the responsibility of the author or of any other collaborator. Use it at your own networks and/or with the network owner's permission.

Linux Privesc Checklist: https://book.hacktricks.xyz/linux-unix/linux-privilege-escalation-checklist
 LEGEND:
  RED/YELLOW: 95% a PE vector
  RED: You must take a look at it
  LightCyan: Users with console
  Blue: Users without console & mounted devs
  Green: Common things (users, groups, SUID/SGID, mounts, .sh scripts, cronjobs) 
  LightMangeta: Your username


====================================( Basic information )=====================================
OS: Linux version 4.4.0-190-generic (buildd@lcy01-amd64-026) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.12) ) #220-Ubuntu SMP Fri Aug 28 23:02:15 UTC 2020
User & Groups: uid=33(www-data) gid=33(www-data) groups=33(www-data)
Hostname: startup
Writable folder: /dev/shm
[+] /bin/ping is available for network discovery (linpeas can discover hosts, learn more with -h)
[+] /bin/nc is available for network discover & port scanning (linpeas can discover hosts and scan ports, learn more with -h)


Caching directories . . . . . . . . . . . . . . . . . . . . . . . DONE
====================================( System Information )====================================
[+] Operative system
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#kernel-exploits
Linux version 4.4.0-190-generic (buildd@lcy01-amd64-026) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.12) ) #220-Ubuntu SMP Fri Aug 28 23:02:15 UTC 2020
Distributor ID:	Ubuntu
Description:	Ubuntu 16.04.7 LTS
Release:	16.04
Codename:	xenial

[+] Sudo version
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-version
Sudo version 1.8.16

[+] USBCreator
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation/d-bus-enumeration-and-command-injection-privilege-escalation

[+] PATH
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-path-abuses
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
New path exported: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

[+] Date
Sat Dec 19 05:33:53 UTC 2020

[+] System stats
Filesystem      Size  Used Avail Use% Mounted on
udev            235M     0  235M   0% /dev
tmpfs            49M  1.8M   47M   4% /run
/dev/xvda1      9.7G  1.2G  8.5G  13% /
tmpfs           244M     0  244M   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           244M     0  244M   0% /sys/fs/cgroup
              total        used        free      shared  buff/cache   available
Mem:         497976       65516       15876       10780      416584      384824
Swap:             0           0           0

[+] CPU info
Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                1
On-line CPU(s) list:   0
Thread(s) per core:    1
Core(s) per socket:    1
Socket(s):             1
NUMA node(s):          1
Vendor ID:             GenuineIntel
CPU family:            6
Model:                 63
Model name:            Intel(R) Xeon(R) CPU E5-2676 v3 @ 2.40GHz
Stepping:              2
CPU MHz:               2394.496
BogoMIPS:              4788.99
Hypervisor vendor:     Xen
Virtualization type:   full
L1d cache:             32K
L1i cache:             32K
L2 cache:              256K
L3 cache:              30720K
NUMA node0 CPU(s):     0
Flags:                 fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx rdtscp lm constant_tsc rep_good nopl xtopology pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm invpcid_single kaiser fsgsbase bmi1 avx2 smep bmi2 erms invpcid xsaveopt

[+] Environment
[i] Any private information inside environment variables?
HISTFILESIZE=0
SHLVL=1
APACHE_RUN_DIR=/var/run/apache2
APACHE_PID_FILE=/var/run/apache2/apache2.pid
_=./linPEAS.sh
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
APACHE_LOCK_DIR=/var/lock/apache2
LANG=C
HISTSIZE=0
APACHE_RUN_USER=www-data
APACHE_RUN_GROUP=www-data
APACHE_LOG_DIR=/var/log/apache2
HISTFILE=/dev/null

[+] Searching Signature verification failed in dmseg
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#dmesg-signature-verification-failed
 Not Found

[+] AppArmor enabled? .............. You do not have enough privilege to read the profile set.
apparmor module is loaded.
[+] grsecurity present? ............ grsecurity Not Found
[+] PaX bins present? .............. PaX Not Found
[+] Execshield enabled? ............ Execshield Not Found
[+] SELinux enabled? ............... sestatus Not Found
[+] Is ASLR enabled? ............... Yes
[+] Printer? ....................... lpstat Not Found
[+] Is this a virtual machine? ..... Yes (xen)
[+] Is this a container? ........... No
[+] Any running containers? ........ No


=========================================( Devices )==========================================
[+] Any sd*/disk* disk in /dev? (limit 20)
disk

[+] Unmounted file-system?
[i] Check if you can mount umounted devices
LABEL=cloudimg-rootfs	/	ext4	defaults	0 0


====================================( Available Software )====================================
[+] Useful software
/bin/nc
/bin/netcat
/usr/bin/wget
/usr/bin/curl
/bin/ping
/usr/bin/base64
/usr/bin/python
/usr/bin/python2
/usr/bin/python3
/usr/bin/python2.7
/usr/bin/perl
/usr/bin/php
/usr/bin/sudo
/usr/bin/lxc

[+] Installed Compiler
/usr/share/gcc-5


================================( Processes, Cron, Services, Timers & Sockets )================================
[+] Cleaned processes
[i] Check weird & unexpected proceses run by root: https://book.hacktricks.xyz/linux-unix/privilege-escalation#processes
root         1  0.3  1.1  37844  5736 ?        Ss   04:55   0:07 /sbin/init
root       393  0.0  0.6  27700  3024 ?        Ss   04:55   0:01 /lib/systemd/systemd-journald
root       414  0.0  0.3  94768  1580 ?        Ss   04:55   0:00 /sbin/lvmetad -f
root       457  0.0  0.7  42496  3604 ?        Ss   04:55   0:00 /lib/systemd/systemd-udevd
root       787  0.0  0.5  16120  2764 ?        Ss   04:55   0:00 /sbin/dhclient -1 -v -pf /run/dhclient.eth0.pid -lf /var/lib/dhcp/dhclient.eth0.leases -I -df /var/lib/dhcp/dhclient6.eth0.leases eth0
root       987  0.0  0.0   5216   148 ?        Ss   04:56   0:00 /sbin/iscsid
root       988  0.0  0.7   5716  3508 ?        S<Ls 04:56   0:00 /sbin/iscsid
daemon[0m     993  0.0  0.3  26040  1948 ?        Ss   04:56   0:00 /usr/sbin/atd -f
root       996  0.0  5.4 457784 26972 ?        Ssl  04:56   0:00 /usr/bin/amazon-ssm-agent
message+   999  0.0  0.7  42884  3812 ?        Ss   04:56   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation
root      1007  0.0  0.5  27724  2572 ?        Ss   04:56   0:00 /usr/sbin/cron -f
root      1008  0.0  0.2  20096  1220 ?        Ss   04:56   0:00 /lib/systemd/systemd-logind
syslog    1025  0.0  0.6 260624  3072 ?        Ssl  04:56   0:00 /usr/sbin/rsyslogd -n
root      1029  0.0  0.1   4392   692 ?        Ss   04:56   0:00 /usr/sbin/acpid
root      1049  0.0  1.1 274484  5780 ?        Ssl  04:56   0:00 /usr/lib/accountsservice/accounts-daemon[0m
root      1053  0.0  0.3 621716  1736 ?        Ssl  04:56   0:00 /usr/bin/lxcfs /var/lib/lxcfs/
root      1064  0.0  1.2  65508  6128 ?        Ss   04:56   0:00 /usr/sbin/sshd -D
root      1066  0.0  0.4  24040  2476 ?        Ss   04:56   0:00 /usr/sbin/vsftpd /etc/vsftpd.conf
root      1078  0.0  3.8 173348 19004 ?        Ssl  04:56   0:01 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
root      1108  0.0  0.0  13368   164 ?        Ss   04:56   0:00 /sbin/mdadm --monitor --pid-file /run/mdadm/monitor.pid --daemon[0mise --scan --syslog
root      1146  0.0  1.1 277176  5808 ?        Ssl  04:56   0:00 /usr/lib/policykit-1/polkitd --no-debug
root      1167  0.0  0.3  14468  1744 ttyS0    Ss+  04:56   0:00 /sbin/agetty --keep-baud 115200 38400 9600 ttyS0 vt220
root      1168  0.0  0.3  14652  1504 tty1     Ss+  04:56   0:00 /sbin/agetty --noclear tty1 linux
root      1240  0.0  4.7 257068 23408 ?        Ss   04:56   0:00 /usr/sbin/apache2 -k start
www-data  1248  0.0  1.4 257320  7200 ?        S    04:56   0:00  \_ /usr/sbin/apache2 -k start
www-data  1249  0.0  1.4 257320  7204 ?        S    04:56   0:00  \_ /usr/sbin/apache2 -k start
www-data  1250  0.0  1.4 257140  7012 ?        S    04:56   0:00  \_ /usr/sbin/apache2 -k start
www-data  1505  0.0  1.1 257140  5664 ?        S    05:11   0:00  \_ /usr/sbin/apache2 -k start
www-data  1507  0.0  1.4 257256  7136 ?        S    05:11   0:00  \_ /usr/sbin/apache2 -k start
www-data  1510  0.0  2.6 257376 13092 ?        S    05:11   0:00  \_ /usr/sbin/apache2 -k start
www-data  1651  0.0  0.1   4500   848 ?        S    05:26   0:00  |   \_ sh -c /bin/sh 
www-data  1652  0.0  0.3   4500  1588 ?        S    05:26   0:00  |   |   \_ /bin/sh
www-data  1675  0.0  0.1   4500   780 ?        S    05:29   0:00  |   \_ sh -c /bin/sh 
www-data  1676  0.0  0.1   4500   752 ?        S    05:29   0:00  |       \_ /bin/sh
www-data  1705  0.0  1.3  32108  6496 ?        S    05:30   0:00  |           \_ python -c import pty; pty.spawn("/bin/bash")
www-data  1706  0.0  0.5  18208  2968 pts/0    Ss   05:30   0:00  |               \_ /bin/bash
www-data  1735  0.0  0.4   4900  2140 pts/0    S+   05:33   0:00  |                   \_ /bin/sh ./linPEAS.sh
www-data  2346  0.0  0.1   4900   548 pts/0    S+   05:33   0:00  |                       \_ /bin/sh ./linPEAS.sh
www-data  2359  0.0  0.6  34552  3000 pts/0    R+   05:33   0:00  |                       |   \_ ps fauxwww
www-data  1511  0.0  1.1 257140  5664 ?        S    05:11   0:00  \_ /usr/sbin/apache2 -k start
www-data  1513  0.0  1.4 257140  6988 ?        S    05:11   0:00  \_ /usr/sbin/apache2 -k start
www-data  1518  0.0  1.4 257256  7140 ?        S    05:11   0:00  \_ /usr/sbin/apache2 -k start
www-data  1519  0.0  1.1 257140  5664 ?        S    05:11   0:00  \_ /usr/sbin/apache2 -k start

[+] Binary processes permissions
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#processes
-rwxr-xr-x 1 root root  1037528 Jul 12  2019 /bin/bash
lrwxrwxrwx 1 root root        4 Feb 17  2016 /bin/sh -> dash
-rwxr-xr-x 1 root root   326232 Sep  4 09:31 /lib/systemd/systemd-journald
-rwxr-xr-x 1 root root   622616 Sep  4 09:31 /lib/systemd/systemd-logind
-rwxr-xr-x 1 root root   453240 Sep  4 09:31 /lib/systemd/systemd-udevd
-rwxr-xr-x 1 root root    44104 Jan 27  2020 /sbin/agetty
-rwxr-xr-x 1 root root   487248 Mar  5  2018 /sbin/dhclient
lrwxrwxrwx 1 root root       20 Sep  4 09:31 /sbin/init -> /lib/systemd/systemd
-rwxr-xr-x 1 root root   783984 Dec 11  2018 /sbin/iscsid
-rwxr-xr-x 1 root root    51336 Apr 16  2016 /sbin/lvmetad
-rwxr-xr-x 1 root root   513216 Nov  8  2017 /sbin/mdadm
-rwxr-xr-x 1 root root 31295080 Aug 11 00:34 /usr/bin/amazon-ssm-agent
-rwxr-xr-x 1 root root   224208 Jun 11  2020 /usr/bin/dbus-daemon[0m
-rwxr-xr-x 1 root root    18504 Nov  9  2017 /usr/bin/lxcfs
lrwxrwxrwx 1 root root        9 Mar 23  2016 /usr/bin/python3 -> python3.5
-rwxr-xr-x 1 root root   164928 Nov  3  2016 /usr/lib/accountsservice/accounts-daemon[0m
-rwxr-xr-x 1 root root    15048 Mar 27  2019 /usr/lib/policykit-1/polkitd
-rwxr-xr-x 1 root root    48112 Apr  8  2016 /usr/sbin/acpid
-rwxr-xr-x 1 root root   662560 Aug 13 01:36 /usr/sbin/apache2
-rwxr-xr-x 1 root root    26632 Jan 14  2016 /usr/sbin/atd
-rwxr-xr-x 1 root root    44472 Apr  5  2016 /usr/sbin/cron
-rwxr-xr-x 1 root root   599328 Mar 25  2019 /usr/sbin/rsyslogd
-rwxr-xr-x 1 root root   791024 May 26  2020 /usr/sbin/sshd
-rwxr-xr-x 1 root root   168200 Apr 13  2016 /usr/sbin/vsftpd

[+] Processes with credentials in memory (root req)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#credentials-from-process-memory
gdm-password Not Found
gnome-keyring-daemon Not Found
lightdm Not Found
vsftpd process found (dump creds from memory as root)
apache2 process found (dump creds from memory as root)
sshd Not Found

[+] Cron jobs
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#scheduled-cron-jobs
-rw-r--r-- 1 root root  722 Apr  5  2016 /etc/crontab

/etc/cron.d:
total 24
drwxr-xr-x  2 root root 4096 Nov 12 04:52 .
drwxr-xr-x 96 root root 4096 Nov 12 05:08 ..
-rw-r--r--  1 root root  102 Apr  5  2016 .placeholder
-rw-r--r--  1 root root  589 Jul 16  2014 mdadm
-rw-r--r--  1 root root  670 Jun 22  2017 php
-rw-r--r--  1 root root  190 Sep 25 08:12 popularity-contest

/etc/cron.daily:
total 60
drwxr-xr-x  2 root root 4096 Nov 12 04:52 .
drwxr-xr-x 96 root root 4096 Nov 12 05:08 ..
-rw-r--r--  1 root root  102 Apr  5  2016 .placeholder
-rwxr-xr-x  1 root root  539 Jul 15 07:08 apache2
-rwxr-xr-x  1 root root  376 Mar 31  2016 apport
-rwxr-xr-x  1 root root 1474 May  7  2019 apt-compat
-rwxr-xr-x  1 root root  355 May 22  2012 bsdmainutils
-rwxr-xr-x  1 root root 1597 Nov 26  2015 dpkg
-rwxr-xr-x  1 root root  372 May  6  2015 logrotate
-rwxr-xr-x  1 root root 1293 Nov  6  2015 man-db
-rwxr-xr-x  1 root root  539 Jul 16  2014 mdadm
-rwxr-xr-x  1 root root  435 Nov 18  2014 mlocate
-rwxr-xr-x  1 root root  249 Nov 12  2015 passwd
-rwxr-xr-x  1 root root 3449 Feb 26  2016 popularity-contest
-rwxr-xr-x  1 root root  214 Dec  7  2018 update-notifier-common

/etc/cron.hourly:
total 12
drwxr-xr-x  2 root root 4096 Sep 25 08:10 .
drwxr-xr-x 96 root root 4096 Nov 12 05:08 ..
-rw-r--r--  1 root root  102 Apr  5  2016 .placeholder

/etc/cron.monthly:
total 12
drwxr-xr-x  2 root root 4096 Sep 25 08:10 .
drwxr-xr-x 96 root root 4096 Nov 12 05:08 ..
-rw-r--r--  1 root root  102 Apr  5  2016 .placeholder

/etc/cron.weekly:
total 24
drwxr-xr-x  2 root root 4096 Sep 25 08:12 .
drwxr-xr-x 96 root root 4096 Nov 12 05:08 ..
-rw-r--r--  1 root root  102 Apr  5  2016 .placeholder
-rwxr-xr-x  1 root root  210 Jan 27  2020 fstrim
-rwxr-xr-x  1 root root  771 Nov  6  2015 man-db
-rwxr-xr-x  1 root root  211 Dec  7  2018 update-notifier-common

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin


[+] Services
[i] Search for outdated versions
 [ + ]  acpid
 [ + ]  apache-htcacheclean
 [ + ]  apache2
 [ + ]  apparmor
 [ + ]  apport
 [ + ]  atd
 [ - ]  bootmisc.sh
 [ - ]  checkfs.sh
 [ - ]  checkroot-bootclean.sh
 [ - ]  checkroot.sh
 [ + ]  console-setup
 [ + ]  cron
 [ - ]  cryptdisks
 [ - ]  cryptdisks-early
 [ + ]  dbus
 [ + ]  grub-common
 [ - ]  hostname.sh
 [ - ]  hwclock.sh
 [ + ]  irqbalance
 [ + ]  iscsid
 [ + ]  keyboard-setup
 [ - ]  killprocs
 [ + ]  kmod
 [ - ]  lvm2
 [ + ]  lvm2-lvmetad
 [ + ]  lvm2-lvmpolld
 [ + ]  lxcfs
 [ - ]  lxd
 [ + ]  mdadm
 [ - ]  mdadm-waitidle
 [ - ]  mountall-bootclean.sh
 [ - ]  mountall.sh
 [ - ]  mountdevsubfs.sh
 [ - ]  mountkernfs.sh
 [ - ]  mountnfs-bootclean.sh
 [ - ]  mountnfs.sh
 [ + ]  networking
 [ + ]  ondemand
 [ + ]  open-iscsi
 [ - ]  open-vm-tools
 [ - ]  plymouth
 [ - ]  plymouth-log
 [ + ]  procps
 [ + ]  rc.local
 [ + ]  resolvconf
 [ - ]  rsync
 [ + ]  rsyslog
 [ - ]  screen-cleanup
 [ - ]  sendsigs
 [ + ]  ssh
 [ + ]  udev
 [ + ]  ufw
 [ - ]  umountfs
 [ - ]  umountnfs.sh
 [ - ]  umountroot
 [ + ]  unattended-upgrades
 [ + ]  urandom
 [ - ]  uuidd
 [ + ]  virtualbox-guest-utils
 [ + ]  vsftpd

[+] Systemd PATH
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#systemd-path-relative-paths
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin

[+] Analyzing .service files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#services
/etc/systemd/system/multi-user.target.wants/networking.service is executing some relative path
/etc/systemd/system/network-online.target.wants/networking.service is executing some relative path
/lib/systemd/system/emergency.service is executing some relative path
/lib/systemd/system/networking.service is executing some relative path
/lib/systemd/system/rescue.service is executing some relative path
You can't write on systemd PATH

[+] System timers
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#timers
NEXT                         LEFT          LAST                         PASSED    UNIT                         ACTIVATES
Sat 2020-12-19 06:05:44 UTC  31min left    Sat 2020-12-19 04:56:19 UTC  37min ago apt-daily-upgrade.timer      apt-daily-upgrade.service
Sat 2020-12-19 08:45:08 UTC  3h 11min left Sat 2020-12-19 04:56:19 UTC  37min ago apt-daily.timer              apt-daily.service
Sat 2020-12-19 09:30:25 UTC  3h 56min left Sat 2020-12-19 04:56:19 UTC  37min ago motd-news.timer              motd-news.service
Sun 2020-12-20 05:10:18 UTC  23h left      Sat 2020-12-19 05:10:18 UTC  23min ago systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service
n/a                          n/a           n/a                          n/a       snapd.snap-repair.timer      snapd.snap-repair.service
n/a                          n/a           n/a                          n/a       ureadahead-stop.timer        ureadahead-stop.service

[+] Analyzing .timer files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#timers

[+] Analyzing .socket files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sockets

[+] HTTP sockets
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sockets

[+] D-Bus config files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#d-bus
Possible weak user policy found on /etc/dbus-1/system.d/dnsmasq.conf (        <policy user="dnsmasq">)
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.network1.conf (        <policy user="systemd-network">)
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.resolve1.conf (        <policy user="systemd-resolve">)

[+] D-Bus Service Objects list
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#d-bus
NAME                                 PID PROCESS         USER             CONNECTION    UNIT                      SESSION    DESCRIPTION        
:1.0                                   1 systemd         root             :1.0          init.scope                -          -                  
:1.1                                1008 systemd-logind  root             :1.1          systemd-logind.service    -          -                  
:1.181                             15508 busctl          www-data         :1.181        apache2.service           -          -                  
:1.2                                1049 accounts-daemon root             :1.2          accounts-daemon.service   -          -                  
:1.3                                1146 polkitd         root             :1.3          polkitd.service           -          -                  
:1.4                                1078 unattended-upgr root             :1.4          unattended-upgrades.se... -          -                  
com.ubuntu.LanguageSelector            - -               -                (activatable) -                         -         
com.ubuntu.SoftwareProperties          - -               -                (activatable) -                         -         
org.freedesktop.Accounts            1049 accounts-daemon root             :1.2          accounts-daemon.service   -          -                  
org.freedesktop.DBus                 999 dbus-daemon     messagebus       org.freedesktop.DBus dbus.service              -          -                  
org.freedesktop.PolicyKit1          1146 polkitd         root             :1.3          polkitd.service           -          -                  
org.freedesktop.hostname1              - -               -                (activatable) -                         -         
org.freedesktop.locale1                - -               -                (activatable) -                         -         
org.freedesktop.login1              1008 systemd-logind  root             :1.1          systemd-logind.service    -          -                  
org.freedesktop.network1               - -               -                (activatable) -                         -         
org.freedesktop.resolve1               - -               -                (activatable) -                         -         
org.freedesktop.systemd1               1 systemd         root             :1.0          init.scope                -          -                  
org.freedesktop.timedate1              - -               -                (activatable) -                         -         


===================================( Network Information )====================================
[+] Hostname, hosts and DNS
startup
127.0.0.1	localhost

::1	ip6-localhost	ip6-loopback
fe00::0	ip6-localnet
ff00::0	ip6-mcastprefix
ff02::1	ip6-allnodes
ff02::2	ip6-allrouters
ff02::3	ip6-allhosts
127.0.1.1	ubuntu-xenial	ubuntu-xenial

nameserver 10.0.0.2
search eu-west-1.compute.internal
dnsdomainname Not Found

[+] Content of /etc/inetd.conf & /etc/xinetd.conf
/etc/inetd.conf Not Found

[+] Interfaces
# symbolic names for networks, see networks(5) for more information
link-local 169.254.0.0
eth0      Link encap:Ethernet  HWaddr 02:4c:c2:13:f3:5d  
          inet addr:10.10.51.110  Bcast:10.10.255.255  Mask:255.255.0.0
          inet6 addr: fe80::4c:c2ff:fe13:f35d/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:9001  Metric:1
          RX packets:22377 errors:0 dropped:0 overruns:0 frame:0
          TX packets:15681 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:2272700 (2.2 MB)  TX bytes:4572060 (4.5 MB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:96 errors:0 dropped:0 overruns:0 frame:0
          TX packets:96 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1 
          RX bytes:9504 (9.5 KB)  TX bytes:9504 (9.5 KB)


[+] Networks and neighbours
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
default         ip-10-10-0-1.eu 0.0.0.0         UG    0      0        0 eth0
10.10.0.0       *               255.255.0.0     U     0      0        0 eth0
Address                  HWtype  HWaddress           Flags Mask            Iface
ip-10-10-0-1.eu-west-1.  ether   02:c8:85:b5:5a:aa   C                     eth0

[+] Iptables rules
iptables rules Not Found

[+] Active Ports
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-ports
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:21              0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -               
tcp        0      0 10.10.51.110:45936      10.8.110.17:4444        ESTABLISHED 1651/sh         
tcp6       0      0 :::80                   :::*                    LISTEN      -               
tcp6       0      0 :::22                   :::*                    LISTEN      -               
tcp6       0      0 10.10.51.110:80         10.8.110.17:37586       ESTABLISHED -               
udp        0      0 0.0.0.0:68              0.0.0.0:*                           -               

[+] Can I sniff with tcpdump?
No

[+] Internet Access?
icmp is not available
Port 443 is not accessible
Port 80 is not accessible


====================================( Users Information )=====================================
[+] My user
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#users
uid=33(www-data) gid=33(www-data) groups=33(www-data)

[+] Do I have PGP keys?
/usr/bin/gpg
netpgpkeys Not Found
netpgp Not Found

[+] Clipboard or highlighted text?
xsel and xclip Not Found

[+] Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-and-suid

[+] Checking sudo tokens
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-and-suid
/proc/sys/kernel/yama/ptrace_scope is not enabled (1)
gdb wasn't found in PATH

[+] Checking doas.conf
/etc/doas.conf Not Found

[+] Checking Pkexec policy
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation/interesting-groups-linux-pe#pe-method-2

[Configuration]
AdminIdentities=unix-user:0
[Configuration]
AdminIdentities=unix-group:sudo;unix-group:admin

[+] Do not forget to test 'su' as any other user with shell: without password and with their names as password (I can't do it...)
[+] Do not forget to execute 'sudo -l' without password or with valid password (if you know it)!!

[+] Superusers
root:x:0:0:root:/root:/bin/bash

[+] Users with console
root:x:0:0:root:/root:/bin/bash
vagrant:x:1000:1000:,,,:/home/vagrant:/bin/bash

[+] All users & groups
uid=0(root) gid=0(root) groups=0(root)
uid=1(daemon[0m) gid=1(daemon[0m) groups=1(daemon[0m)
uid=10(uucp) gid=10(uucp) groups=10(uucp)
uid=100(systemd-timesync) gid=102(systemd-timesync) groups=102(systemd-timesync)
uid=1000(vagrant) gid=1000(vagrant) groups=1000(vagrant)
uid=1002(lennie) gid=1002(lennie) groups=1002(lennie)
uid=1003(ftpsecure) gid=1003(ftpsecure) groups=1003(ftpsecure)
uid=101(systemd-network) gid=103(systemd-network) groups=103(systemd-network)
uid=102(systemd-resolve) gid=104(systemd-resolve) groups=104(systemd-resolve)
uid=103(systemd-bus-proxy) gid=105(systemd-bus-proxy) groups=105(systemd-bus-proxy)
uid=104(syslog) gid=108(syslog) groups=108(syslog),4(adm)
uid=105(_apt) gid=65534(nogroup) groups=65534(nogroup)
uid=106(lxd) gid=65534(nogroup) groups=65534(nogroup)
uid=107(messagebus) gid=111(messagebus) groups=111(messagebus)
uid=108(uuidd) gid=112(uuidd) groups=112(uuidd)
uid=109(dnsmasq) gid=65534(nogroup) groups=65534(nogroup)
uid=110(sshd) gid=65534(nogroup) groups=65534(nogroup)
uid=111(pollinate) gid=1(daemon[0m) groups=1(daemon[0m)
uid=112(ftp) gid=118(ftp) groups=118(ftp),33(www-data)
uid=13(proxy) gid=13(proxy) groups=13(proxy)
uid=2(bin) gid=2(bin) groups=2(bin)
uid=3(sys) gid=3(sys) groups=3(sys)
uid=33(www-data) gid=33(www-data) groups=33(www-data)
uid=34(backup) gid=34(backup) groups=34(backup)
uid=38(list) gid=38(list) groups=38(list)
uid=39(irc) gid=39(irc) groups=39(irc)
uid=4(sync) gid=65534(nogroup) groups=65534(nogroup)
uid=41(gnats) gid=41(gnats) groups=41(gnats)
uid=5(games) gid=60(games) groups=60(games)
uid=6(man) gid=12(man) groups=12(man)
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
uid=7(lp) gid=7(lp) groups=7(lp)
uid=8(mail) gid=8(mail) groups=8(mail)
uid=9(news) gid=9(news) groups=9(news)

[+] Login now
 05:36:12 up 40 min,  0 users,  load average: 0.05, 0.06, 0.03
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT

[+] Last logons
reboot   system boot  4.4.0-190-generi Sat Dec 19 04:55   still running
reboot   system boot  4.4.0-190-generi Thu Nov 12 05:08 - 05:11  (00:02)
vagrant  pts/0        10.0.2.2         Thu Nov 12 04:50 - crash  (00:17)
reboot   system boot  4.4.0-190-generi Thu Nov 12 04:50 - 05:11  (00:20)

wtmp begins Thu Nov 12 04:50:21 2020

[+] Last time logon each user
Username         Port     From             Latest
vagrant          pts/0    10.0.2.2         Thu Nov 12 04:50:52 +0000 2020

[+] Password policy
PASS_MAX_DAYS	99999
PASS_MIN_DAYS	0
PASS_WARN_AGE	7
ENCRYPT_METHOD SHA512


===================================( Software Information )===================================
[+] MySQL version
mysql Not Found

[+] MySQL connection using default root/root ........... No
[+] MySQL connection using root/toor ................... No
[+] MySQL connection using root/NOPASS ................. No
[+] Searching mysql credentials and exec

[+] PostgreSQL version and pgadmin credentials
 Not Found

[+] PostgreSQL connection to template0 using postgres/NOPASS ........ No
[+] PostgreSQL connection to template1 using postgres/NOPASS ........ No
[+] PostgreSQL connection to template0 using pgsql/NOPASS ........... No
[+] PostgreSQL connection to template1 using pgsql/NOPASS ........... No

[+] Apache server info
Version: Server version: Apache/2.4.18 (Ubuntu)
Server built:   2020-08-12T21:35:50
PHP exec extensions
/etc/apache2/mods-available/php7.0.conf-<FilesMatch ".+\.ph(p[3457]?|t|tml)$">
/etc/apache2/mods-available/php7.0.conf:    SetHandler application/x-httpd-php
--
/etc/apache2/mods-available/php7.0.conf-<FilesMatch ".+\.phps$">
/etc/apache2/mods-available/php7.0.conf:    SetHandler application/x-httpd-php-source
--
/etc/apache2/mods-enabled/php7.0.conf-<FilesMatch ".+\.ph(p[3457]?|t|tml)$">
/etc/apache2/mods-enabled/php7.0.conf:    SetHandler application/x-httpd-php
--
/etc/apache2/mods-enabled/php7.0.conf-<FilesMatch ".+\.phps$">
/etc/apache2/mods-enabled/php7.0.conf:    SetHandler application/x-httpd-php-source

[+] Searching PHPCookies
 Not Found

[+] Searching Wordpress wp-config.php files
wp-config.php Not Found

[+] Searching Drupal settings.php files
/default/settings.php Not Found

[+] Searching Tomcat users file
tomcat-users.xml Not Found

[+] Mongo information
mongo binary Not Found

[+] Searching supervisord configuration file
supervisord.conf Not Found

[+] Searching cesi configuration file
cesi.conf Not Found

[+] Searching Rsyncd config file
/usr/share/doc/rsync/examples/rsyncd.conf
[ftp]
	comment = public archive
	path = /var/www/pub
	use chroot = yes
	lock file = /var/lock/rsyncd
	read only = yes
	list = yes
	uid = nobody
	gid = nogroup
	strict modes = yes
	ignore errors = no
	ignore nonreadable = yes
	transfer logging = no
	timeout = 600
	refuse options = checksum dry-run
	dont compress = *.gz *.tgz *.zip *.z *.rpm *.deb *.iso *.bz2 *.tbz

[+] Searching Hostapd config file
hostapd.conf Not Found

[+] Searching wifi conns file
 Not Found

[+] Searching Anaconda-ks config files
anaconda-ks.cfg Not Found

[+] Searching .vnc directories and their passwd files
.vnc Not Found

[+] Searching ldap directories and their hashes
/etc/ldap
The password hash is from the {SSHA} to 'structural'

[+] Searching .ovpn files and credentials
.ovpn Not Found

[+] Searching ssl/ssh files
Port 22
PermitRootLogin prohibit-password
PubkeyAuthentication yes
PermitEmptyPasswords no
ChallengeResponseAuthentication no
PasswordAuthentication yes
UsePAM yes
  --> Some certificates were found (out limited):
/etc/pollinate/entropy.ubuntu.com.pem

 --> /etc/hosts.allow file found, read the rules:
/etc/hosts.allow


Searching inside /etc/ssh/ssh_config for interesting info
Host *
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes
    GSSAPIDelegateCredentials no

[+] Searching unexpected auth lines in /etc/pam.d/sshd
No

[+] Searching Cloud credentials (AWS, Azure, GC)

[+] NFS exports?
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation/nfs-no_root_squash-misconfiguration-pe
/etc/exports Not Found

[+] Searching kerberos conf files and tickets
[i] https://book.hacktricks.xyz/pentesting/pentesting-kerberos-88#pass-the-ticket-ptt
krb5.conf Not Found
tickets kerberos Not Found
klist Not Found

[+] Searching Kibana yaml
kibana.yml Not Found

[+] Searching Knock configuration
Knock.config Not Found

[+] Searching logstash files
 Not Found

[+] Searching elasticsearch files
 Not Found

[+] Searching Vault-ssh files
vault-ssh-helper.hcl Not Found

[+] Searching AD cached hashes
cached hashes Not Found

[+] Searching screen sessions
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-shell-sessions
No Sockets found in /var/run/screen/S-www-data.

[+] Searching tmux sessions
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-shell-sessions
tmux Not Found

[+] Searching Couchdb directory

[+] Searching redis.conf

[+] Searching dovecot files
dovecot credentials Not Found

[+] Searching mosquitto.conf

[+] Searching neo4j auth file

[+] Searching Cloud-Init conf file
Found readable /etc/cloud/cloud.cfg
     lock_passwd: True

[+] Searching Erlang cookie file

[+] Searching GVM auth file

[+] Searching IPSEC files

[+] Searching IRSSI files

[+] Searching Keyring files
Keyring folder: /usr/share/keyrings
/usr/share/keyrings:
total 32
-rw-r--r-- 1 root root 14076 Jun  3  2020 ubuntu-archive-keyring.gpg
-rw-r--r-- 1 root root     0 Jun  3  2020 ubuntu-archive-removed-keys.gpg
-rw-r--r-- 1 root root     0 Nov 11  2013 ubuntu-cloudimage-keyring-removed.gpg
-rw-r--r-- 1 root root  2294 Nov 11  2013 ubuntu-cloudimage-keyring.gpg
-rw-r--r-- 1 root root  2253 Nov  5  2017 ubuntu-esm-keyring.gpg
-rw-r--r-- 1 root root  1139 Nov  5  2017 ubuntu-fips-keyring.gpg
-rw-r--r-- 1 root root  1227 Jun  3  2020 ubuntu-master-keyring.gpg
Keyring folder: /var/lib/apt/keyrings
/var/lib/apt/keyrings:
total 16
-rw-r--r-- 1 root root 12335 Sep 25 08:10 ubuntu-archive-keyring.gpg

[+] Searching Filezilla sites file

[+] Searching backup-manager files

[+] Searching uncommon passwd files (splunk)
passwd file: /etc/cron.daily/passwd
passwd file: /etc/pam.d/passwd
passwd file: /usr/bin/passwd
passwd file: /usr/share/bash-completion/completions/passwd
passwd file: /usr/share/lintian/overrides/passwd

[+] Searching GitLab related files


[+] Searching PGP/GPG
PGP/GPG software:
/usr/bin/gpg
netpgpkeys Not Found
netpgp Not Found


====================================( Interesting Files )=====================================
[+] SUID - Check easy privesc, exploits and write perms
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-and-suid
-rwsr-xr-x 1 root   root        44K May  7  2014 /bin/ping6
-rwsr-xr-x 1 root   root        44K May  7  2014 /bin/ping
-rwsr-sr-x 1 daemon daemon      51K Jan 14  2016 /usr/bin/at  --->  RTru64_UNIX_4.0g(CVE-2002-1614)
-rwsr-xr-x 1 root   root        31K Jul 12  2016 /bin/fusermount
-rwsr-xr-x 1 root   root        10K Mar 27  2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root   root        53K Mar 26  2019 /usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)
-rwsr-xr-x 1 root   root        74K Mar 26  2019 /usr/bin/gpasswd
-rwsr-xr-x 1 root   root        40K Mar 26  2019 /usr/bin/chsh
-rwsr-xr-x 1 root   root        71K Mar 26  2019 /usr/bin/chfn  --->  SuSE_9.3/10
-rwsr-xr-x 1 root   root        39K Mar 26  2019 /usr/bin/newgrp  --->  HP-UX_10.20
-rwsr-xr-x 1 root   root        40K Mar 26  2019 /bin/su
-rwsr-xr-x 1 root   root        33K Mar 26  2019 /usr/bin/newuidmap
-rwsr-xr-x 1 root   root        33K Mar 26  2019 /usr/bin/newgidmap
-rwsr-xr-x 1 root   root        15K Mar 27  2019 /usr/lib/policykit-1/polkit-agent-helper-1
-rwsr-xr-x 1 root   root        23K Mar 27  2019 /usr/bin/pkexec  --->  Linux4.10_to_5.1.17(CVE-2019-13272)/rhel_6(CVE-2011-1485)
-rwsr-xr-x 1 root   root        83K Apr  9  2019 /usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
-rwsr-xr-x 1 root   root        27K Jan 27  2020 /bin/umount  --->  BSD/Linux(08-1996)
-rwsr-xr-x 1 root   root        40K Jan 27  2020 /bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
-rwsr-xr-x 1 root   root       134K Jan 31  2020 /usr/bin/sudo  --->  /sudo$
-rwsr-xr-x 1 root   root       419K May 26  2020 /usr/lib/openssh/ssh-keysign
-rwsr-xr-- 1 root   messagebus  42K Jun 11  2020 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root   root       109K Sep  8 09:01 /usr/lib/snapd/snap-confine

[+] SGID
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-and-suid
-rwxr-sr-x 1 root   mlocate  39K Nov 18  2014 /usr/bin/mlocate
-rwsr-sr-x 1 daemon daemon   51K Jan 14  2016 /usr/bin/at
-rwxr-sr-x 1 root   utmp    425K Feb  7  2016 /usr/bin/screen
-rwxr-sr-x 1 root   tty      15K Mar  1  2016 /usr/bin/bsd-write
-rwxr-sr-x 1 root   utmp     10K Mar 11  2016 /usr/lib/x86_64-linux-gnu/utempter/utempter
-rwxr-sr-x 1 root   crontab  36K Apr  5  2016 /usr/bin/crontab
-rwxr-sr-x 1 root   shadow   35K Apr  9  2018 /sbin/unix_chkpwd
-rwxr-sr-x 1 root   shadow   35K Apr  9  2018 /sbin/pam_extrausers_chkpwd
-rwxr-sr-x 1 root   shadow   23K Mar 26  2019 /usr/bin/expiry
-rwxr-sr-x 1 root   shadow   61K Mar 26  2019 /usr/bin/chage
-rwxr-sr-x 1 root   tty      27K Jan 27  2020 /usr/bin/wall
-rwxr-sr-x 1 root   ssh     351K May 26  2020 /usr/bin/ssh-agent

[+] Checking misconfigurations of ld.so
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#ld-so
/etc/ld.so.conf
include /etc/ld.so.conf.d/*.conf

/etc/ld.so.conf.d
  /etc/ld.so.conf.d/libc.conf
/usr/local/lib
  /etc/ld.so.conf.d/x86_64-linux-gnu.conf
/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu

[+] Capabilities
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#capabilities
Current capabilities:
CapInh:	0000000000000000
CapPrm:	0000000000000000
CapEff:	0000000000000000
CapBnd:	0000003fffffffff
CapAmb:	0000000000000000

Shell capabilities:
CapInh:	0000000000000000
CapPrm:	0000000000000000
CapEff:	0000000000000000
CapBnd:	0000003fffffffff
CapAmb:	0000000000000000

Files with capabilities:
/usr/bin/systemd-detect-virt = cap_dac_override,cap_sys_ptrace+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/mtr = cap_net_raw+ep

[+] Users with capabilities
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#capabilities
/etc/security/capability.conf Not Found

[+] Files with ACLs
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#acls
files with acls in searched folders Not Found

[+] .sh files in path
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#script-binaries-in-path
/usr/bin/gettext.sh

[+] Unexpected in root
/vagrant
/recipe.txt
/vmlinuz.old
/vmlinuz
/incidents
/initrd.img
/lost+found
/initrd.img.old

[+] Files (scripts) in /etc/profile.d/
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#profiles-files
total 32
drwxr-xr-x  2 root root 4096 Sep 25 08:12 .
drwxr-xr-x 96 root root 4096 Nov 12 05:08 ..
-rw-r--r--  1 root root 1557 Apr 14  2016 Z97-byobu.sh
-rwxr-xr-x  1 root root 3417 Aug 28 05:53 Z99-cloud-locale-test.sh
-rwxr-xr-x  1 root root  873 Aug 28 05:53 Z99-cloudinit-warnings.sh
-rw-r--r--  1 root root  833 Sep  8 09:01 apps-bin-path.sh
-rw-r--r--  1 root root  663 May 18  2016 bash_completion.sh
-rw-r--r--  1 root root 1003 Dec 29  2015 cedilla-portuguese.sh

[+] Permissions in init, init.d, systemd, and rc.d
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#init-init-d-systemd-and-rc-d

[+] Hashes inside passwd file? ........... No
[+] Writable passwd file? ................ No
[+] Credentials in fstab/mtab? ........... No
[+] Can I read shadow files? ............. No
[+] Can I read opasswd file? ............. No
[+] Can I write in network-scripts? ...... No
[+] Can I read root folder? .............. No

[+] Searching root files in home dirs (limit 30)
/home/
/root/

[+] Searching folders owned by me containing others files on it

[+] Readable files belonging to root and readable by me but not world readable

[+] Modified interesting files in the last 5mins (limit 100)
/var/log/auth.log
/var/log/amazon/ssm/hibernate.log
/var/log/kern.log
/var/log/syslog
/tmp/linPEAS.sh

[+] Writable log files (logrotten) (limit 100)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#logrotate-exploitation

[+] Files inside /home/www-data (limit 20)

[+] Files inside others home (limit 20)

[+] Searching installed mail applications

[+] Mails (limit 50)

[+] Backup folders
drwxr-xr-x 2 root root 4096 Dec 19 04:56 /var/backups
total 4
-rw-r--r-- 1 root root 2752 Nov 12 04:52 apt.extended_states.0

[+] Backup files
-rw-r--r-- 1 root root 128 Sep 25 08:12 /var/lib/sgml-base/supercatalog.old
-rw-r--r-- 1 root root 298 Dec 19 04:55 /run/blkid/blkid.tab.old
-rw-r--r-- 1 root root 610 Sep 25 08:12 /etc/xml/catalog.old
-rw-r--r-- 1 root root 673 Sep 25 08:12 /etc/xml/xml-core.xml.old
-rw-r--r-- 1 root root 0 Aug 29 01:25 /usr/src/linux-headers-4.4.0-190-generic/include/config/net/team/mode/activebackup.h
-rw-r--r-- 1 root root 0 Aug 29 01:25 /usr/src/linux-headers-4.4.0-190-generic/include/config/wm831x/backup.h
-rw-r--r-- 1 root root 191098 Aug 29 01:25 /usr/src/linux-headers-4.4.0-190-generic/.config.old
-rw-r--r-- 1 root root 35792 May  8  2018 /usr/lib/open-vm-tools/plugins/vmsvc/libvmbackup.so
-rw-r--r-- 1 root root 7867 May  6  2015 /usr/share/doc/telnet/README.telnet.old.gz
-rw-r--r-- 1 root root 298768 Dec 29  2015 /usr/share/doc/manpages/Changes.old.gz
-rwxr-xr-x 1 root root 226 Apr 14  2016 /usr/share/byobu/desktop/byobu.desktop.old
-rw-r--r-- 1 root root 665 Apr 16  2016 /usr/share/man/man8/vgcfgbackup.8.gz
-rw-r--r-- 1 root root 10100 Sep 25 08:12 /usr/share/info/dir.old
-rw-r--r-- 1 root root 1496 Sep 25 08:12 /usr/share/sosreport/sos/plugins/__pycache__/ovirt_engine_backup.cpython-35.pyc
-rw-r--r-- 1 root root 1758 Mar 24  2020 /usr/share/sosreport/sos/plugins/ovirt_engine_backup.py

[+] Searching tables inside readable .db/.sql/.sqlite files (limit 100)
Found: /var/lib/mlocate/mlocate.db: regular file, no read permission

[+] Web files?(output limit)

[+] Readable *_history, .sudo_as_admin_successful, profile, bashrc, httpd.conf, .plan, .htpasswd, .gitconfig, .git-credentials, .git, .svn, .rhosts, hosts.equiv, Dockerfile, docker-compose.yml
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#read-sensitive-data
-rw-r--r-- 1 root root 2188 Aug 31  2015 /etc/bash.bashrc
-rw-r--r-- 1 root root 3771 Aug 31  2015 /etc/skel/.bashrc
-rw-r--r-- 1 root root 655 Jul 12  2019 /etc/skel/.profile
-rw-r--r-- 1 root root 3106 Aug 14  2019 /usr/share/base-files/dot.bashrc
-rw-r--r-- 1 root root 3161 Apr 14  2016 /usr/share/byobu/profiles/bashrc
-rw-r--r-- 1 root root 870 Jul  2  2015 /usr/share/doc/adduser/examples/adduser.local.conf.examples/bash.bashrc
-rw-r--r-- 1 root root 1865 Jul  2  2015 /usr/share/doc/adduser/examples/adduser.local.conf.examples/skel/dot.bashrc

[+] All hidden files (not in /sys/ or the ones listed in the previous check) (limit 70)

[+] Readable files inside /tmp, /var/tmp, /private/tmp, /private/var/at/tmp, /private/var/tmp, and backup folders (limit 70)
-rwxr-xr-x 1 www-data www-data 307433 Dec 19 05:32 /tmp/linPEAS.sh
-rw-r--r-- 1 root root 2752 Nov 12 04:52 /var/backups/apt.extended_states.0

[+] Interesting writable files owned by me or writable by everyone (not in Home) (max 500)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files
/dev/mqueue
/dev/shm
/incidents
/incidents/suspicious.pcapng
/recipe.txt
/run/cloud-init/tmp
/run/lock
/run/lock/apache2
/run/screen/S-www-data
/tmp
/tmp/.ICE-unix
/tmp/.Test-unix
/tmp/.X11-unix
/tmp/.XIM-unix
/tmp/.font-unix
#)You_can_write_even_more_files_inside_last_directory
/var/cache/apache2/mod_cache_disk
/var/crash
/var/lib/lxcfs/cgroup/memory/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/init.scope/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/-.mount/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/accounts-daemon.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/acpid.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/amazon-ssm-agent.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/apache2.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/apparmor.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/apport.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/atd.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/cloud-config.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/cloud-final.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/cloud-init-local.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/cloud-init.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/console-setup.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/cron.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/dbus.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/dev-hugepages.mount/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/dev-mqueue.mount/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/grub-common.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/ifup@eth0.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/irqbalance.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/iscsid.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/keyboard-setup.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/kmod-static-nodes.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/lvm2-lvmetad.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/lvm2-monitor.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/lxcfs.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/lxd-containers.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/mdadm.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/networking.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/ondemand.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/open-iscsi.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/polkitd.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/proc-sys-fs-binfmt_misc.mount/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/rc-local.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/resolvconf.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/rsyslog.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/setvtrgb.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/snapd.apparmor.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/snapd.seeded.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/ssh.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/sys-fs-fuse-connections.mount/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/sys-kernel-debug.mount/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/system-getty.slice/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/system-serialx2dgetty.slice/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-journal-flush.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-journald.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-logind.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-modules-load.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-random-seed.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-remount-fs.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-sysctl.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-tmpfiles-setup-dev.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-tmpfiles-setup.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-udev-trigger.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-udevd.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-update-utmp.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-user-sessions.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/ufw.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/unattended-upgrades.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/var-lib-lxcfs.mount/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/virtualbox-guest-utils.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/vsftpd.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/user.slice/cgroup.event_control
/var/lib/php/sessions
/var/tmp

[+] Interesting GROUP writable files (not in Home) (max 500)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files
  Group www-data:


[+] Searching passwords in config PHP files

[+] Checking for TTY (sudo/su) passwords in audit logs

[+] Finding IPs inside logs (limit 70)
      9 /var/log/dpkg.log:1.16.04.3
      1 /var/log/cloud-init-output.log:172.30.21.236
      1 /var/log/cloud-init-output.log:172.30.16.1
      1 /var/log/cloud-init-output.log:10.10.51.110
      1 /var/log/apt/history.log:1.16.04.3

[+] Finding passwords inside logs (limit 70)
/var/log/cloud-init.log:2020-11-12 04:50:34,606 - cc_set_passwords.py[DEBUG]: Leaving SSH config 'PasswordAuthentication' unchanged. ssh_pwauth=None
/var/log/cloud-init.log:2020-11-12 05:08:53,905 - helpers.py[DEBUG]: config-set-passwords already ran (freq=once-per-instance)
/var/log/cloud-init.log:2020-12-19 04:56:42,521 - helpers.py[DEBUG]: config-set-passwords already ran (freq=once-per-instance)

[+] Finding emails inside logs (limit 70)

[+] Finding *password* or *credential* files in home (limit 70)

[+] Finding 'pwd' or 'passw' variables (and interesting php db definitions) inside key folders (limit 70) - only PHP files

[+] Finding 'pwd' or 'passw' variables (and interesting php db definitions) inside key folders (limit 70) - no PHP files
/etc/acpi/powerbtn.sh:                userhome=`getent passwd $user | cut -d: -f6`
/etc/apache2/sites-available/default-ssl.conf:		#	 file needs this password: `xxj31ZMTZzkVA'.
/etc/bash_completion.d/grub:__grub_mkpasswd_pbkdf2_program="grub-mkpasswd-pbkdf2"
/etc/cloud/cloud.cfg:     lock_passwd: True
/etc/cloud/cloud.cfg:     sudo: ["ALL=(ALL) NOPASSWD:ALL"]
/etc/debconf.conf:#BindPasswd: secret
/etc/nsswitch.conf:passwd:         compat
/etc/overlayroot.conf:#      $ MAPNAME="secure"; DEV="/dev/vdg"; PASSWORD="foobar"
/etc/overlayroot.conf:#     crypt:dev=/dev/vdb,pass=somepassword,mkfs=0
/etc/pam.d/common-password:password	[success=1 default=ignore]	pam_unix.so obscure sha512
/etc/security/namespace.init:                gid=$(echo "$passwd" | cut -f4 -d":")
/etc/security/namespace.init:        homedir=$(echo "$passwd" | cut -f6 -d":")
/etc/security/namespace.init:        passwd=$(getent passwd "$user")
/etc/ssl/openssl.cnf:# input_password = secret
/etc/ssl/openssl.cnf:# output_password = secret
/etc/ssl/openssl.cnf:challengePassword		= A challenge password
/etc/ssl/openssl.cnf:challengePassword_max		= 20
/etc/ssl/openssl.cnf:challengePassword_min		= 4
/etc/vmware-tools/vm-support:         sed 's/password[[:space:]]\+\(.*\)[[:space:]]\+\(.*\)$/password  xxxxxx/g' > \

[+] Finding possible password variables inside key folders (limit 140)

[+] Finding possible password in config files
 /etc/sysctl.d/10-ptrace.conf
credentials that exist in memory (re-using existing SSH connections,
 /etc/adduser.conf
passwd
 /etc/debconf.conf
passwords.
password
passwords.
passwords
password
passwords.dat
passwords and one for everything else.
passwords
password is really
Passwd: secret
 /etc/nsswitch.conf
passwd:         compat
 /etc/overlayroot.conf
password is randomly generated
password will be stored for recovery in
passwd
password,mkfs=0
PASSWORD="foobar"
PASSWORD" |
PASSWORD" |
PASSWORD HERE IN THIS CLEARTEXT CONFIGURATION
passwords are more secure, but you won't be able to
passwords are generated by calculating the sha512sum
 /etc/init/passwd.conf
passwd - clear locks on passwd and related files
passwd to avoid million duplicate bug reports
passwd locks"
passwd.lock /etc/group.lock /etc/subuid.lock /etc/subgid.lock
 /etc/apache2/apache2.conf
passwd files from being

[+] Finding 'username' string inside key folders (limit 70)
/tmp/linPEAS.sh:      cat "$f" 2>/dev/null | grep -E "port.*=|username.*=|password.*=" | sed -E "s,port|username|password,${C}[1;31m&${C}[0m,"; 

[+] Searching specific hashes inside files - less false positives (limit 70)
```