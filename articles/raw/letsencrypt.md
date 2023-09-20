# Creating certificate to Apache 
‣
### Renew encrypt certicate

Let’s Encrypt uses the client Certbot to install, manage, and automatically renew the certificates they provide. 

>`
sudo certbot renew
`

If you have multiple certificates for different domains and you want to renew a specific certificate, use:


>`
certbot certonly --force-renew -d example.com
`

The --force-renew flag tells Certbot to request a new certificate with the same domains as an existing certificate. The -d flag allows you renew certificates for multiple specific domains.

To verify that the certificate renewed, run:

>`
sudo certbot renew --dry-run
`
