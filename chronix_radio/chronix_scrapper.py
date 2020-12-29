import requests
import json


# TODO: processing errors

def scrap_img(url, path_to_save):
    """
    Downloads image from given url and saves it at given path.
    """
    # TODO: save img at correct path (where is this correct path?)
    res = requests.get(url)
    res.raise_for_status()
    with open("test."+url[-3:], "wb+") as fp:
        for chunk in res.iter_content(100000):
            fp.write(chunk)


def scrap_chronix():
    """
    Function for reading currently played song at chronix radio.
    """
    url = "https://fastcast4u.com/player/gebacher/index.php?c=ChroniX%20AGGRESSION;"
    res = requests.get(url)
    res.raise_for_status()
    res_metadata = json.loads(res.text)
    print(res_metadata["artist"])
    print(res_metadata["title"])
    print(res_metadata["album"])

    # url_img = "https://fastcast4u.com/player/gebacher/"  # example: +"_user/cover/g/gebacher/deveria.jpg"
    url_img = "https://fastcast4u.com/player/gebacher/" + res_metadata["image"]
    scrap_img(url_img, "")

    # TODO return data to be added to db

scrap_chronix()


