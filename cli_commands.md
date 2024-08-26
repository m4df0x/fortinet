# FortiManager
## update Software from tftp ##

    fmg01 # execute restore image tftp FMG_VM64-v7.2.5-build1574-FORTINET.out <ip-tftp-server>
    Start getting file from TFTP Server...
    ##########################################################################################################################################################################################################################################################################

    Upgrade FMG_VM64 image from v7.2.5-b1574-240313(GA) to v7.2.5-b1574-240313

    This operation will replace the current firmware version and reboot the system!
    Do you want to continue? (y/n)y


    fmg01-grau # Connection to <ip-fmg> closed by remote host.
    Connection to <ip-fmg> closed.

## reset
    fmg01 # execute reset all-except-ip 
    This operation will reset all settings to factory defaults, but will keep all interface IP and route configuration.
    Do you want to continue? (y/n)y

    Resetting ...
    Connection to <ip-fmg> closed by remote host.
    Connection to <ip-fmg> closed.

## restore from sftp
    fmg01 # execute restore all-settings sftp <ip-tftp-server> /opt/tftpboot/configuration/SYS_FMG-<serial>_fmg01_20240624_2300.dat admin <Password-SFTP> <Password-Backup> 
    This operation will replace the current settings and reboot the system
    Do you want to continue? (y/n)y

    Starting transfer the backup file from SFTP server...
    Transferred 220.795M of 220.795M in 0:00:02s (82.310M/s)

    fmg01 # Connection to <ip-fmg> closed by remote host.
    Connection to <ip-fmg> closed.
# FortiAnalyzer

# FortiGate
