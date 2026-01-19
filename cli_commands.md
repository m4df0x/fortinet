# Table of Content
* [FortiManager](#FortiManager);
* [FortiAnalyzer](#FortiAnalyzer);
* [FortiWeb](#FortiWeb);
* [FortiGate](#FortiGate);
* [FortiMail](#FortiMail);
* [FortiPAM](#FortiPAM);

# <a name="FortiManager"></a>FortiManager
## Update Software from tftp

    fmg01 # execute restore image tftp FMG_VM64-v7.2.5-build1574-FORTINET.out <ip-tftp-server>
    Start getting file from TFTP Server...
    ##########################################################################################################################################################################################################################################################################

    Upgrade FMG_VM64 image from v7.2.5-b1574-240313(GA) to v7.2.5-b1574-240313

    This operation will replace the current firmware version and reboot the system!
    Do you want to continue? (y/n)y


    fmg01-grau # Connection to <ip-fmg> closed by remote host.
    Connection to <ip-fmg> closed.

## update Software from SFTP

    fmg01 # execute restore image sftp opt/tftpboot/firmware/FortiManager/FMG_VM64-v7.2.5-build1574-FORTINET.out <ip-sftp-server>:22 <user-sftp> <Password-SFTP>
    Start getting file from SFTP Server...
    Transferred 265.938M of 265.938M in 0:00:03s (67.511M/s)

    Upgrade FMG_VM64 image from v7.2.6-b1632-240809(GA) to v7.2.6-b1632-240809

    This operation will replace the current firmware version and reboot the system!
    Do you want to continue? (y/n)y


    fmg01 # Connection to <ip-fmg> closed by remote host.
    Connection to <ip-fmg> closed.

## Reset
    fmg01 # execute reset all-except-ip 
    This operation will reset all settings to factory defaults, but will keep all interface IP and route configuration.
    Do you want to continue? (y/n)y

    Resetting ...
    Connection to <ip-fmg> closed by remote host.
    Connection to <ip-fmg> closed.
    
## Backup to sftp
    fmg01 # execute backup all-settings sftp <ip-sftp-server> /opt/tftpboot/ <user-sftp> <Password-SFTP> <Password-Backup>
    Starting backup all settings in background please wait.

    Starting transfer the backup file to SFTP server...
    Transferred 241.810M of 241.810M  in 0:00:04s (53.265M/s)
    Backup all settings...Ok.
    
## Restore from sftp
    fmg01 # execute restore all-settings sftp <ip-tftp-server> /opt/tftpboot/configuration/SYS_FMG-<serial>_fmg01_20240624_2300.dat admin <Password-SFTP> <Password-Backup> 
    This operation will replace the current settings and reboot the system
    Do you want to continue? (y/n)y

    Starting transfer the backup file from SFTP server...
    Transferred 220.795M of 220.795M in 0:00:02s (82.310M/s)

    fmg01 # Connection to <ip-fmg> closed by remote host.
    Connection to <ip-fmg> closed.

# <a name="FortiAnalyzer"></a>FortiAnalyzer
## import Entitlementfile for airgapped setups
    faz01 # execute fmupdate tftp import license EntitlementExport <ip-sftp-server>
    This operation will replace the current fmupdate data!
    Do you want to continue? (y/n)y

    Start getting file from TFTP Server...

    TFTP transfer is successful.
    Package installation is in process... This could take some time.
    Update successfully

    faz01 # The session is expired.
    exit
    Connection to <ip-faz> closed.
    
## resize logdisk
### before
    faz01 # execute lvm info
    LVM Status: OK
    LVM Size: 1000GB
    File System: ext4 983GB

    Disk1 :         Used     1000GB of 2000GB

    faz01 # execute lvm extend
    This operation will need to reboot the system.
    And all data in unused disks will be lost.
    Do you want to continue? (y/n)y
### after
    faz01 # execute lvm info
    LVM Status: OK
    LVM Size: 2000GB
    File System: ext4 1968GB

    Disk1 :         Used     2000GB
    

# <a name="FortiWeb"></a>FortiWeb
## redirect FortiGuard to FortiManager for airgapped setups
    fwb01 # config system autoupdate override
    set status enable
    set address <fortimanager_ip>:8890
    set fail-over disable
    end
## manually upload vmlicence into FortiWeb
    fwb01# execute restore vmlicense tftp <license>.lic <ip-tftp-server>
    This operation will replace the current VM license !
    Do you want to continue? (y/n)y

    Connect to tftp server <ip-tftp-server> ...
    Please wait...

    Get license from tftp server OK.
    License has been uploaded. Please wait a few seconds for license authentication with Fortinet registration servers.
    Requires Internet connection. After verification, the system will reboot.

    Please wait a few seconds for license authentication.

# <a name="FortiGate"></a>FortiGate

# <a name="FortiMail"></a>FortiMail
### Backup CLI TFTP with FilePassword
    fem01 # execute backup full-config tftp fortimail.cfg <ip-tftp-server> <FILE-PASSWORD>
    User defined configuartion can be updated with command "exec user-config generate".
    User defined configuration last updated time: Mon Jan 13 09:00:00 2025
    IBE data can be updated with command "execute ibe data export-to-file".
    IBE data last updated time: Sun Jan 12 21:00:05 2025
    System time: Mon Jan 13 09:00:00 2025
    Backup with current user defined configuration and current ibe data. Do you want to continue? (y/n)y
    Connect to tftp server <ip-tftp-server> ...
    Please wait...
    #
    Send file to tftp server OK.

### Backup CLI TFTP without FilePassword
    fem01 # execute backup full-config tftp fortimail.cfg <ip-tftp-server>
    User defined configuartion can be updated with command "exec user-config generate".
    User defined configuration last updated time: Mon Jan 13 09:00:00 2025
    IBE data can be updated with command "execute ibe data export-to-file".
    IBE data last updated time: Sun Jan 12 21:00:05 2025
    System time: Mon Jan 13 09:00:00 2025
    Backup with current user defined configuration and current ibe data. Do you want to continue? (y/n)y
    Connect to tftp server <ip-tftp-server> ...
    Please wait...
    #
    Send file to tftp server OK.

### Backup CLI SCP
    fem01 # execute backup full-config scp /opt/tftpboot/fortimail.cfg <ip-scp-server> <scp-user> <scp-password>
    User defined configuartion can be updated with command "exec user-config generate".
    User defined configuration last updated time: Mon Jan 13 09:00:00 2025
    IBE data can be updated with command "execute ibe data export-to-file".
    IBE data last updated time: Mon Jan 13 09:00:05 2025
    System time: Mon Jan 13 09:28:36 2025
    Backup with current user defined configuration and current ibe data. Do you want to continue? (y/n)y
    Send file to server with SCP OK.
# <a name="FortiPAM"></a>FortiPAM
## manually upload vmlicence into FortiPAM
    jumphost # scp -O FPAVULTM26000106.lic admin@<ip-fortipam>:vmlicense
    admin@<ip-fortipam>'s password: 
    <license>.lic     100% 9108    12.1MB/s   00:00    
    100-install VM license completed
