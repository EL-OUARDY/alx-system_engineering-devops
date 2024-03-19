# Firewall — Alx System Engineering DevOps
0x13. Firewall

```DevOps```
```SysAdmin```
```Security```

## Introduction
A ``firewall`` is a crucial component of network security, acting as a barrier between your network and potentially harmful incoming traffic. In this guide, we'll cover how to set up a basic firewall using UFW (Uncomplicated Firewall) on a Linux system.

## UFW
``UFW`` stands for **Uncomplicated Firewall**. It is a user-friendly command-line interface for managing firewall rules on Linux systems. UFW provides a simplified syntax for configuring firewall rules and is designed to make the process of setting up and managing a firewall easier for users who may not be familiar with more complex firewall solutions. It is commonly used on Ubuntu and other Debian-based distributions, but it can also be installed on other Linux distributions.

### Installing UFW
If ``UFW`` is not already installed on your system, you can install it using the package manager of your Linux distribution. For example, on Ubuntu or Debian, you can use:
```bash
sudo apt-get install ufw
```
### Basic Firewall Configuration
Once UFW is installed, you can start configuring it. The simplest way to configure UFW is to block all incoming traffic by default and allow only specific connections.

To block all incoming traffic, use the following command:
```bash
sudo ufw default deny incoming
```
### Allowing Specific Traffic
To allow specific incoming connections, you can open the desired ports. For example, to allow SSH connections (port 22), you can use:
```bash
sudo ufw allow ssh
```
Similarly, if you're running a web server and want to allow **HTTP (port 80)** and **HTTPS (port 443)** traffic, you can use:
```bash
sudo ufw allow http
sudo ufw allow https
```
### Port Forwarding
Port forwarding allows you to redirect traffic from one port to another. This can be useful for accessing services hosted on your local network from the internet.

To forward a port, you can use the ``ufw`` command followed by the port number and the protocol (usually **TCP** or **UDP**). For example, to forward traffic from port **8080** to port **80** on a local server, you can use:
```bash
sudo ufw allow 8080/tcp
```

Then, enable port forwarding by editing **UFW configuration file**:
```bash
sudo vi /etc/ufw/before.rules
```
Add the following lines before the ***filter** section:
```bash
*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
COMMIT
```
Save the file and exit.

### Enabling UFW
After configuring the firewall rules, you need to enable UFW to start enforcing them. Use the following command to enable UFW:
```bash
sudo ufw enable
```
### Checking Status
To check the status of UFW and see the current firewall rules, you can use:
```bash
sudo ufw status
```

## Contact Me
**Twitter:** https://twitter.com/_ELOUARDY \
**Email:** ouadia@elouardy.com

