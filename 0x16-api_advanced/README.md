# API advanced — Alx System Engineering DevOps
0x16. API advanced

``Python``
``Scripting``
``Back-end``
``API``


## How to use an API with pagination
Using an API with pagination, such as the [``Reddit API``](https://www.reddit.com/dev/api/) , typically involves making multiple requests to fetch all the data, as the API limits the number of results returned in a single request. Here's a general approach using the Reddit API:

**Make an initial request**: Send a request to the API to retrieve the first page of data. This may involve specifying parameters such as the subreddit, sorting method, and number of items per page.

**Process the response**: Extract the relevant data from the response, such as posts or comments, and store it in a data structure like a list or dictionary.

**Check for pagination**: Look for pagination information in the response, such as a ***next*** or ***after*** parameter, which indicates there are more pages of data available.

**Make subsequent requests**: If there are more pages of data, construct a new request with the appropriate parameters to fetch the next page. Repeat this process until all pages have been retrieved.

**Combine and process data**: Once all pages have been fetched, combine the data from each page and process it as needed.


Here's a simple example using the Python ``requests`` library to fetch posts from a subreddit:

```python
import requests

def fetch_posts(subreddit, limit=25):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': limit}
    posts = []

    while True:
        response = requests.get(url, params=params, headers={'User-Agent': 'MyBot/0.1'})
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            posts.extend(data['data']['children'])
            after = data['data']['after']
            if after:
                params['after'] = after
            else:
                break
        else:
            break

    return posts

# Example usage
subreddit = 'python'
posts = fetch_posts(subreddit)
for post in posts:
    print(post['data']['title'])
```

In this example, the **fetch_posts()** function fetches posts from the specified subreddit using the Reddit API. It iterates through multiple pages of results by checking for the ***after*** parameter in the response and constructing subsequent requests until all pages have been fetched. Finally, it prints the titles of the fetched posts.

## Contact Me
**Email:** ouadia@elouardy.com \
**Twitter:** https://twitter.com/_ELOUARDY
