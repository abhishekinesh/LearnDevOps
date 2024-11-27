
# ADD ENVIRONMENT VARIABLE TO PATH

1. Add '/rnd' to the PATH environment variable temporarily
    ## export PATH=$PATH:/rnd

2. Verify the updated PATH
    ## echo $PATH

3. Display all environment variables
    ## env


# ADD USER and PATH

1. Create a User
    ## sudo useradd abhi

2. Set a Password for the User
    ## sudo passwd abhi

3. Create Home Directory for the User
    ## sudo mkdir /home/abhi

4. Set Ownership of Home Directory
    ## sudo chown abhi:abhi /home/abhi

5. Update User's Home Directory Information
    ## sudo usermod -d /home/abhi abhi

6. Switch to the User
    ## su - abhi

# GROUP MANAGEMENT

1. Create a new group named 'developers'
    ## sudo groupadd developers

2. Add user 'abhi' to the 'developers' group
    ## sudo usermod -aG developers abhi

3. Remove user 'abhi' from the 'developers' group
    ## sudo gpasswd -d abhi developers

4. Delete the 'developers' group
    ## sudo groupdel developers

5. List all groups
    ## cat /etc/group

6. Change a user's primary group
    ## sudo usermod -g groupname username



# FILE MANAGEMENT

1. Change file permissions to read, write, and execute for the owner, and read and execute for the group and others
    ## chmod 755 filename

2. Change file permissions to read and write for the owner, and read-only for the group and others
    ## chmod 644 filename

3. Change the owner of a file
    ## sudo chown new_owner filename

4. Change the owner and group of a file
    ## sudo chown new_owner:new_group filename

5. Change the group ownership of a file
    ## sudo chgrp new_group filename

6. Example: Set 'example.txt' to read, write, and execute for the owner, and read and execute for the group and others
    ## chmod 755 example.txt

7. Example: Change the owner of 'example.txt' to 'alice'
    ## sudo chown alice example.txt

8. Example: Change the owner and group of 'example.txt' to 'alice' and 'developers'
    ## sudo chown alice:developers example.txt

9. Example: Change the group of 'example.txt' to 'developers'
    ## sudo chgrp developers example.txt


# SERVER MANAGEMENT

1. A command often used for showing memory information

    free -m [-m : In megabytes] [-h : human readable / -g : gigabytes]

    free -h
                total        used        free      shared  buff/cache   available
    Mem:            7.7G        3.4G        2.2G        120M        2.0G        4.1G
    Swap:           2.0G        512M        1.5G

        total: The total amount of physical memory available in the system.
        used: The amount of memory currently used by processes and the operating system.
        free: The amount of unused memory.
        shared: The amount of memory used by shared resources, mainly used by tmpfs (shared memory file system).
        buff/cache: The amount of memory used by the kernel buffers and page cache.
        available: An estimate of the amount of memory available for starting new applications, without swapping.

        Swap: Represents the swap memory statistics.
        total: Total swap space in the system.
        used: Amount of swap space currently in use.
        free: Amount of swap space currently not in use.

<!-- The swap state refers to the status of the swap space or swap partition in a Linux system. Swap space is used as a virtual memory extension of the physical memory (RAM). When the RAM is full, inactive pages of memory are moved to the swap space to free up RAM for active processes. This helps prevent system crashes and ensures smooth operation even when the memory is heavily used -->

2. A command for showing disk usage
    df -h

3. A command for showing CPU load
    uptime

4. A command for showing Authentication logs
    tail /var/log/auth.log


5. List all services managed by systemd/service
    sudo systemctl list-units --type=service
    service --status-all


# MANAGING BACKGROUND AND FOREGROUND PROCESSES

1. Running a Process in the Foreground:
   command

2. Moving a Running Process to the Background:
   [Ctrl + Z]   
   bg           

3. Starting a Process in the Background:
   command &

4. Listing Background Jobs:
   jobs

5. Bringing a Background Job to the Foreground:
   fg %1

6. Killing a Background Job:
   kill %1

<!-- EXAMPLE COMMANDS -->

7. Starting a Command in the Background:
   sleep 100 &

8. Moving a Foreground Process to the Background:
   sleep 100  
   [Ctrl + Z]
   bg         

9. Listing Jobs and Bringing One to the Foreground:
   jobs       
   fg %1      

10. Killing a Background Job:
    kill %1    
