from InstagramAPI import InstagramAPI


def getUserFromUsername(api, username):
    if type(api) != InstagramAPI:
        print("Api should be InstagramApi instance")
    api.searchUsername(username)
    return api.LastJson
