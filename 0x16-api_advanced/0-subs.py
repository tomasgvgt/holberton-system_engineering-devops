#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API.
If you’re getting errors related to Too Many Requests, ensure you’re
setting a custom User-Agent.

Requirements:

    Prototype: def number_of_subscribers(subreddit)
    If not a valid subreddit, return 0.
    NOTE: Invalid subreddits may return a redirect to search results.
    Ensure that you are not following redirects.
"""
import requests


def number_of_subscribers(subreddit):
    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    parameters = {'User-Agent' : 'python:api_advanced-holberton:v1.0.0'
                  '(by /u/tomasgomezvelez)'}
    response = requests.get(api_url, params=parameters)
    
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    return 0
