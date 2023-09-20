# Installing and configuring Elastic Search


---
#### INSTALL Elastic Search
* Goto https://www.elastic.co/downloads/elasticsearch
* Download the tar file - untar the file
* [ ] `sudo mv elasticsearch-* /opt/ `
* *NOTE* If you have previous version of elastic search move it out
* [ ] `cd /opt; sudo ln -s elasticsearch-* elasticsearch` 

#### START
* [ ] `cd /opt/elasticsearch`
* Before starting edit the configutation file 
`vi conf/elasticsearch.yml`

Comment following lines

>```
# Enable security features
xpack.security.enabled: false
.
xpack.security.enrollment.enabled: false
.
# Enable encryption for HTTP API...‣
xpack.security.http.ssl:
  enabled: false
#keystore.path: certs/http.p12
.
xpack.security.transport.ssl:
  enabled: false
#verification_mode: certificate
#keystore.path: certs/transport.p12
#truststore.path: certs/transport.p12
```
`
`

* [ ] `bin/elasticsearch &`




        