from DB.Models import Post
from DB.Util.Post import getNecessaryPosts
import random
from time import sleep


def filterImageOnlyPosts(posts):
    for post in posts:
        if 'image_versions2' in post:
            yield post


def getImageUrlFromPost(post):
    return post['image_versions2']['candidates'][0]['url']


def parseFileNameFromUrl(url):
    return url.split("/")[-1].split("?")[0]


def registerPostToDB(post, client):
    # print(post['pk'], post['code'], getImageUrlFromPost(post), client)
    post = Post.create(pk=post['pk'], code=post['code'], image_url=getImageUrlFromPost(post), client=client)
    return post


def getUnpostedPostsOfClient(api, client):
    posts = api.getTotalUserFeed(client.pk)
    posts = filterImageOnlyPosts(posts)
    posts = sorted(posts, key=lambda k: k['like_count'], reverse=True)

    posts = getNecessaryPosts(posts)

    return posts


def getPostsOfClients(api, clients):
    posts = []

    for client in clients:
        sleep(random.randint(200, 800) / 1000)
        print("Getting posts os Client \"{}\"".format(client.username))
        posts.extend(getUnpostedPostsOfClient(api, client))

    return posts
