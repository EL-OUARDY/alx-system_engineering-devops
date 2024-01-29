# Web infrastructure design — Alx System Engineering DevOps
0x09. Web infrastructure design

```SysAdmin```
```DevOps```

## Introduction
In this module, we will explore the foundational principles and best practices for designing and architecting robust web infrastructures.

## DNS
**DNS** is, in simple words, the technology that translates human-adapted, text-based domain names to machine-adapted, numerical-based IP.

### DNS record types
- **A Record** (Address Record): Maps a domain name to an IPv4 address.

- **AAAA Record**: Maps a domain name to an IPv6 address.

- **CNAME Record** (Canonical Name): Alias of one domain name to another, allowing multiple domain names to resolve to the same location.

- **MX Record** (Mail Exchange): Specifies the mail server responsible for receiving email on behalf of a domain.

- **TXT Record** (Text Record): Allows domain owners to add arbitrary text to a DNS record, often used for verification or to provide information.

- **NS Record** (Name Server): Specifies the authoritative name servers for a domain.

## Monitoring tools
Monitoring tools are essential for ensuring the smooth operation of websites and applications.
- **NewRelic** provides detailed performance analysis, including browser load times and error alerts. 
- **DataDog** offers comprehensive monitoring with easy-to-read graphs and numerous integrations. 
- **Uptime Robot** checks website availability globally
- **Nagios**, despite being considered somewhat outdated, still provides robust monitoring capabilities. 
- **Wavefront** stands out with its cutting-edge approach, enabling deep analysis of diverse data sources with a SQL-like query language.

Each tool addresses specific monitoring needs, catering to a range of preferences and requirements.

## Web Server
A **web server** is a software application that stores, processes, and delivers web pages to clients upon request over the internet. It handles requests from web browsers or other web clients and responds with the requested content, typically HTML pages, images, or other resources. Web servers use HTTP (Hypertext Transfer Protocol) to communicate with clients and may also support HTTPS (HTTP Secure) for encrypted communication. Popular web server software includes ```Apache HTTP Server```, ```Nginx```, ```Microsoft IIS```, and others.

## Load balancer
A ```load balancer``` is a device or software component that distributes incoming network traffic across multiple servers. Its purpose is to ensure that no single server becomes overwhelmed with requests, thereby optimizing resource utilization, and ensuring high availability and reliability of a website or application.

Load balancer algorithms determine how incoming requests are distributed among servers. Common ones include Round Robin, Least Connections, Weighted Round Robin ..

## Servers
Servers are computers or software systems that provide services or resources to other computers, known as clients, over a network.

In the context of **web hosting**, a server typically refers to a computer system that stores and delivers web pages, files, or applications to users accessing them through the internet. Servers can range from physical machines housed in data centers to virtual instances running on cloud platforms. They handle requests from clients and respond with the requested data or perform specific tasks, such as processing database queries or executing scripts.

## Databases
A ```database``` is a structured collection of data that is organized and stored in a way that allows for efficient retrieval, management, and manipulation. It acts as a central repository for storing and managing data used by applications.

```Database Management System``` (DBMS) is software that enables users to interact with databases. It provides an interface for creating, accessing, updating, and managing databases. DBMS software handles tasks such as data storage, retrieval, security, and data integrity.

```SQL``` (Structured Query Language) is a programming language used to communicate with and manipulate databases. It is the standard language for interacting with relational databases, allowing users to perform tasks such as querying data, inserting new records, updating existing records, and deleting records. SQL is essential for managing and working with relational databases efficiently.

## Single point of failure
A single point of failure refers to any component in a system whose failure can lead to the failure of the entire system. It represents a vulnerability where the loss or malfunction of a single part can disrupt the entire operation or functionality of a system, causing downtime or other significant issues.

To mitigate the risk of single points of failure, redundancy measures, failover systems, and robust disaster recovery plans are often implemented to ensure system reliability and availability.

## What is HTTPS
HTTPS (Hypertext Transfer Protocol Secure) is an extension of HTTP (Hypertext Transfer Protocol) that encrypts data sent between a web browser and a web server.

It starts with a handshake, verifies the server's identity with a certificate, and establishes a secure connection using encryption. This ensures data privacy and integrity, protecting against interception and tampering.

## What is Firewall
A firewall is a security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. It acts as a barrier between a trusted internal network and untrusted external networks, such as the internet, to prevent unauthorized access and protect against cyber threats. Firewalls can be implemented as hardware appliances, software programs, or a combination of both, and they inspect packets of data passing through them, blocking or allowing traffic based on defined criteria, such as IP addresses, ports, protocols, or application types. Firewalls are a fundamental component of network security, helping to safeguard networks and data from malicious attacks, unauthorized access, and other security risks.

## Conclusion
By the end of this module, we will have a solid understanding of how to design and architect web infrastructures that meet the demands of modern web applications.

## Contact Me
**Twitter:** https://twitter.com/_ELOUARDY \
**Email:** ouadia@elouardy.com

