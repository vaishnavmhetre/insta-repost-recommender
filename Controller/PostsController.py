from datetime import datetime

from flask import jsonify
from peewee import SQL
from playhouse.shortcuts import model_to_dict

from DB.Models import Post


def showPosts():
    posts = [post for post in Post.select().order_by(SQL('created_at').desc()).where(
        Post.posted_at.is_null() & Post.ignored_at.is_null())]
    data = jsonify({'data': [model_to_dict(post, backrefs=True, extra_attrs=['instagramURL']) for post in posts]})
    return data


def markAsIgnored(postId):
    try:
        post = Post.select().where(Post.id == postId)[0]
    except Post.DoesNotExist as e:
        return ""

    post.ignored_at = datetime.now()
    post.save()

    return jsonify({'data': model_to_dict(post, backrefs=True, extra_attrs=['instagramURL'])})


def markAsPosted(postId):
    try:
        post = Post.select().where(Post.id == postId)[0]
    except Post.DoesNotExist as e:
        return ""

    post.posted_at = datetime.now()
    post.save()

    return jsonify({'data': model_to_dict(post, backrefs=True, extra_attrs=['instagramURL'])})
