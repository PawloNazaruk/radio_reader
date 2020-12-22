import requests
import json

# TODO: saving song attributes on local dir
# TODO: saving song img on local dir
# TODO: return data functionality
# TODO: processing errors

def get_song_chronix():
    """
    Function for reading currently played song at chronix radio.
    """
    url_song = "https://fastcast4u.com/player/gebacher/index.php?c=ChroniX%20AGGRESSION;"
    url_img = "https://fastcast4u.com/player/gebacher/"  # example: +"_user/cover/g/gebacher/deveria.jpg"

    res_song = requests.get(url_song)
    res_song.raise_for_status()

    song_metadata = json.loads(res_song.text)
    # artist
    # title
    # album
    print(res_song._content)


    url_img += str(song_metadata["image"])
    res_img = requests.get(url_img)
    print(res_img._content)
    res_img.raise_for_status()
    with open("asd.jpg", "wb+") as fp:
        # file on storage
        pass


get_song_chronix()