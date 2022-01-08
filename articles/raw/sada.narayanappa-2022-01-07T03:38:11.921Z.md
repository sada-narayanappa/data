# Run jupyter notebook on remote server 
####	ssh tunnel 

---

SSH Tunneling, also known as port forwarding. What this means is that you setup a network tunnel (a connection for data to flow) from a local point to remote point.

<img src="/static/articles/imgs/sshtunnel.png" width=512px> 

Run the remote server on a particular port and run the following command on your local computer.
 
---
```
ssh -NL 6000:localhost:1234 username@172.26.36.128
```
---

Now you can access your server from your local browser by navigating to http://localhost:6000‣


<div class="alert alert-success">
<strong>Tip:</strong> 
It is best to set up pub/private keys to remote into your server to avaoid the hazzle of typing in password each time
</div>
