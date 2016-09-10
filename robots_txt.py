import io
import urllib.request


def get_robot_txt(url):
    if url.endswith("/"):
        path = url
    else:
        path = url + "/"

    req = urllib.request.urlopen(path + "robots.txt", data=None)
    data = io.TextIOWrapper(req, encoding="utf-8")
    return data.read()
