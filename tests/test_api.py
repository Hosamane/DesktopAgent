import requests

posts = requests.get(
    "https://jsonplaceholder.typicode.com/posts"
).json()


posts = posts[:1]
text = f"Title: {post['title']}\n\n{post['body']}"