from InstagramAPI import InstagramAPI


def getApiInstance(username, password):
    api = InstagramAPI(username, password)
    api.login()
    return api
