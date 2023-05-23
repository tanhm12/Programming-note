# OSI model
- <MAC><IP><TCP/IP><HTTP>
- MAC address chỉ dùng để trỏ đến vị trí hiện tại và next hop, thay đổi khi tới hop
- Tìm địa chỉ router thông qua IP
- Tìm địa chỉ service/app thông qua port (tcp/udp), trong trường hơp mạng local (nhiều PCs) thì router map port của máy sang port của router (trường hơp gateway thì tương tự: gateway là router, router sẽ là PC). Vì vậy 1 router chỉ có 1 ip address, http trỏ tới cổng 80 trên router.

# Iptables
## save iptables records
save `sudo sh -c "iptables-save > /etc/iptables/rules.v4"`
## add new record
`sudo   iptables  -A  INPUT  -p  tcp  --dport  18443  -j  ACCEPT`

# reverse ssh tunnel
Q: Let's say my local machine is Z, target machine X in an private network and I have a public machine Y which has static ip. Show me how to setup a ssh connection from Z to X through Y using reverse ssh tunnel  

  A:
ChatGPT
You can use a reverse SSH tunnel to achieve this. Here are the steps:

On your target machine X (the one in the private network), initiate an SSH connection to your public machine Y, while also specifying a reverse tunnel. For example:

ssh -R 8888:localhost:22 username_on_Y@public_ip_of_Y
In this command, -R specifies the reverse tunnel. 8888 is the port on machine Y that will be used for the reverse tunnel. localhost:22 is the destination of the tunnel, which is the SSH server on machine X.

After running this command, an SSH session from X to Y will start. The reverse tunnel is also set up at this point. Now you can SSH from your local machine Z to X, through Y. Here's the command:

ssh -p 8888 username_on_X@public_ip_of_Y
-p 8888 specifies that you should connect to port 8888, which is the port we specified for the reverse tunnel.

This is a basic setup and has some limitations. If the SSH session from X to Y is disconnected, the reverse tunnel will also be disconnected. You could use tools like autossh to automatically restart the session if it disconnects.

Security note: Be aware that anyone who can connect to machine Y on port 8888 will be able to attempt to SSH to machine X. You should still need to provide valid credentials for X, but this could be a potential security risk. Make sure to use strong, unique passwords for your SSH accounts and consider using SSH keys for authentication. It's also recommended to use a firewall to limit who can connect to port 8888 on machine Y.
