from DB.Models import Post


def getNecessaryPosts(posts):
    postsPks = [post['pk'] for post in posts]
    toRejectPostsPks = [post.pk for post in
                        Post.select().where(
                            (Post.posted_at.is_null(True) | Post.ignored_at.is_null(True)) & Post.pk.in_(postsPks))]

    for post in posts:
        if post['pk'] not in toRejectPostsPks:
            yield post
