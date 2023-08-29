#!/bin/bash

# NFS enum scan

ip=$1

#run rpcinfo to get information about whats servicses are availible
rpcinfo -p $ip > rpc_info.out

#run showmount to see what we have access to
showmount -e $ip

#if we have access to shares, mount them with the following commands
# mkdir /mnt/nfs
# mount -t nfs <remote IP>:/ /mnt/nfs
### now you should have a path to that share


