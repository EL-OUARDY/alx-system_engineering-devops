# 0x11. What happens when you type google.com in your browser and press Enter


```DevOps```
```Network```
```SysAdmin```

Ever wondered what really happens when you type `"google.com"` or any of your favorite sites and press Enter?
It's pretty impressive when you think about it – these sites are packed with loads of data and provide such seamless user experiences.

Today, let's delve into the journey of accessing a webpage and uncover what happens behind the scenes during those crucial milliseconds while you're waiting for the results to pop up in your browser!

Before we move on, let's define some key elements that are very important to grasp - just to make sure we are on the same page:

- `Browser:` It's just the program you're using right now to preview this website, probably Chrome, Safari, or Firefox.
- `Server`: It's simply a computer! Nothing too crazy, haha. We call it that name because it serves a purpose, which in this context, is serving us a website! Servers are located in data centers and they are on all the time. Every company has a server(s) where they host their websites.
- `IP Address`: is like a digital address for computers or any device connected to the internet. Ex. **142.250.184.174**
- `Domain Name`: It's the name you use to access a website! For example, google.com. Domains are here because humans cannot remember IP addresses.

## DNS Request
When you type ``"google.com"`` your browser sends a request to a Domain Name System (DNS) server to translate "google.com" into an **IP address**

## TCP/IP
Once the IP address is retrieved, We know now where the server of the website is located, your browser initiates a connection using Transmission Control Protocol (**TCP**) and Internet Protocol (**IP**). This ensures reliable communication between your computer and Google's servers.

## Firewall
If you have a firewall enabled on your machine, it may inspect the outgoing request to ensure it's safe and not malicious. It's like a digital barrier that protects your computer or network from unauthorized access. It filters incoming and outgoing traffic based on predetermined security rules, blocking potentially harmful data while allowing safe information to pass through. and it could exist on the user machine as well as in the server itslef.

## HTTPS/SSL
The browser can initiates two type of connections ``HTTP`` (Hypertext Transfer Protocol) and ``HTTPS``, the 's' stands for **secure**. So, If you're accessing Google using HTTPS (Hypertext Transfer Protocol Secure), your browser establishes a secure connection using ``SSL`` (Secure Sockets Layer) or its successor ``TLS`` (Transport Layer Security). This encryption protects your data from being intercepted by malicious actors. in simple words it adds an extra layer of security.

## Load Balancer
Big companies receives millions of visitors a day! a massive amount of traffic that a single server can't handle no matter how strong the hardware it has. for this specific case, They use a ``load balancer``! which in his turn distributes incoming requests across multiple servers
So, our request to Google is getting to the load balancer and switched to the right server.

## Web Server
Once the request reaches Google's servers, it's directed to a program called ``Web server``. This one hosts the Google website's files and content. it's like a storage unit for website files that responds to requests from your browser.

## Application Server
Behind the web server, there is an ``Application server`` responsible for processing dynamic content. This could involve executing scripts, accessing databases, or handling user authentication. in our case "google.com" is doing all of these to serve you a dynamic we page filled with data and ready to intact with.

## Database
Speaking about databases, A `database` is a structured collection of data that is organized in a way that makes it easy to access, manage, and update. think of it as an **Excel sheet**.
In our request the application server communicates with a database. This could be to retrieve search results, user information, or any other data stored by Google.


## Response
Finally, Google's servers gather all the necessary information, generate a response, and send it back to your browser through the established **TCP/IP** connection. This response includes the ``HTML``, ``CSS``, ``JavaScript``, and other resources needed to render the Google homepage on your screen such as media files (images, video ..etc)

## How does the browser preview web page?
When the browser receives the response content from the server, it goes through several steps to display the web page:

- ``HTML``: The browser unwraps the HTML code to understand how the page is built. Then it constructs the **DOM**, which is like a blueprint of the web page's structure.
- ``CSS``: Applying styles from CSS files, making everything look pretty and organized.
- ``JavaScript``: It adds interactive elements like pop-ups, animations, and dynamic content.
- ``Media files``: The browser goes on a quick process to fetch images, videos, and other media to complete the page's look.

After accomplishing those steps, the browser unveils the fully dressed web page for you to enjoy, complete with all the bells and whistles 🙌

## Conclusion
And there you have it! From typing ``"google.com"`` to seeing the search engine's homepage, there's a whole journey of technology and infrastructure. I hope you enjoyed taking this trip with me to understand what goes on behind the scenes in just a matter of milliseconds.

## Author
**Twitter:** https://twitter.com/_ELOUARDY \
**Email:** ouadia@elouardy.com
