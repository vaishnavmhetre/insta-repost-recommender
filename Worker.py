import json
import random

from DB.Models import ClientUser, Post
from Instagram import Instantiator
from Instagram.Post import getPostsOfClients, registerPostToDB
from Instagram.Recommender.Recommender import Recommender
from app import INSTAGRAM_CONFIG, MAX_CLIENTS


def getUnpostedPosts(api):
    clients = random.choices(population=ClientUser.select(), k=MAX_CLIENTS)
    return getPostsOfClients(api, clients)


def getUnregisteredPosts(posts):
    postsIds = [post['pk'] for post in posts]
    registeredPostsPks = [post.pk for post in Post.select().where(Post.pk.in_(postsIds))]

    for post in posts:
        if post['pk'] not in registeredPostsPks:
            yield post


def run():
    api = Instantiator.getApiInstance(INSTAGRAM_CONFIG['username'], INSTAGRAM_CONFIG['password'])
    posts = getUnpostedPosts(api)
    posts = Recommender(posts).recommended

    with open("recommendedposts.json", "w+") as f:
        json.dump(posts, f)

    unregisteredPosts = getUnregisteredPosts(posts)

    # print([post['user']['username'] for post in unregisteredPosts])

    for post in unregisteredPosts:
        # print("creating post {}".format(post['pk']))
        registerPostToDB(post=post,
                         client=ClientUser.select().where(ClientUser.username == post['user']['username'])[0])


if __name__ == '__main__':
    run()
