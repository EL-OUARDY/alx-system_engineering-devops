# Web server — Alx System Engineering DevOps
0x0C. Web server

```DevOps```
```SysAdmin```

## How the Web Works
The web functions through a `client-server` model. **Clients**, such as web browsers, send requests to servers for resources like web pages. **Servers**, in turn, process these requests and deliver the requested content back to the clients.

## Nginx
`Nginx` is a popular open-source web server software known for its high performance, stability, and scalability. It's commonly used to serve static and dynamic content over HTTP and HTTPS protocols.

## Configuring Nginx
To configure Nginx, you typically work with its configuration files located in the ***/etc/nginx*** directory on Linux systems. These files include ***nginx.conf*** for global configurations and sites-available directory for configuring individual sites or applications.

Example:
```nginx
server {
    listen 80;
    server_name example.com;
    location / {
        root /var/www/html;
        index index.html;
    }
}
```
## Parent and Child Processes
Web servers often employ a parent-child process model for managing incoming requests efficiently. The parent process handles tasks like listening for incoming connections, while child processes are responsible for serving requests. This architecture allows for better resource management and scalability.

## Root and Subdomains
Root domain refers to the main domain name (e.g., example.com), while subdomains are variations of this domain (e.g., blog.example.com). Web servers can be configured to serve different content for each subdomain.

## HTTP Requests
HTTP (Hypertext Transfer Protocol) requests are messages sent by a client to request resources from a server. These requests typically include methods like GET, POST, PUT, DELETE, etc., along with headers and optional data.

The main HTTP requests include:

- ``GET``: Requests data from a specified resource.
- ``POST``: Submits data to be processed to a specified resource.
- ``PUT``: Updates a specified resource.
- ``DELETE``: Deletes the specified resource.

These requests, along with others like *HEAD*, *OPTIONS*, and *PATCH*, facilitate various interactions between clients and servers on the web.

## HTTP Redirection
HTTP redirection is the process of forwarding a client's request from one URL to another. This is often used for purposes like URL rewriting, domain forwarding, or handling outdated URLs.

Example:
```nginx
server {
    listen 80;
    server_name old-domain.com;
    return 301 http://new-domain.com$request_uri;
}
```

## SCP and cURL
``scp`` (secure copy) is a command-line utility for securely copying files between hosts on a network. It uses SSH for data transfer and authentication.
```bash
# SCP: Copying a local file to a remote server
scp /path/to/local/file.txt username@remote_host:/path/to/remote/directory/

# SCP: Copying a remote file to the local machine
scp username@remote_host:/path/to/remote/file.txt /path/to/local/directory/
```

``curl`` (Client URL) is a command-line tool for transferring data with URLs. It supports various protocols, including HTTP, HTTPS, FTP, and more, making it useful for testing web services and APIs.

```bash
# cURL: Sending a GET request to a URL and printing the response
curl http://example.com

# cURL: Downloading a file from a URL and saving it locally
curl -O http://example.com/file.txt

# cURL: Uploading a file to a server using POST
curl -X POST -F "file=@/path/to/local/file.txt" http://example.com/upload

# cURL: Following HTTP redirection and retrieving the final destination content
curl -L http://example.com
```

## Contact Me
**Email:** ouadia@elouardy.com \
**Twitter:** https://twitter.com/_ELOUARDY
