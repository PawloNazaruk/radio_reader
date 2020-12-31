import requests
import json
import time
from collections import namedtuple

from background_task import background
from datetime import datetime

from django.utils import timezone
from chronix_radio.models import Track, ChronixRadioTrack, ChronixGritTrack, ChronixMetalTrack, ChronixAggressionTrack


def log_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)


def scrap_img(url, path_to_save):
    """
    Downloads image from given url and saves it at given path.
    """
    # TODO: save img at correct path (where is this correct path?)
    res = requests.get(url)
    res.raise_for_status()
    return res


"""
with open("test."+url[-3:], "wb+") as fp:
    for chunk in res.iter_content(100000):
        fp.write(chunk)"""


@background(schedule=60)
def scrap_chronix_page():
    """
    Function for reading currently played song at chronix radio.
    """
    log_time()
    stations_urls = {
        "radio": "",
        "grit": "",
        "metal": "",
        "aggression": "https://fastcast4u.com/player/gebacher/index.php?c=ChroniX%20AGGRESSION",
    }

    res = requests.get(stations_urls["aggression"])
    res.raise_for_status()
    res_data = json.loads(res.text)

    new_track = Track(
        title=res_data["title"],
        artist=res_data["artist"],
        album=res_data["album"],
    )


    tracks = Track.objects.all()
    if new_track in tracks:
        try:
            track = Track.objects.get(title=new_track.title, album=new_track.album, artist=new_track.artist)
            specific_station = ChronixRadioTrack(played_time=timezone.now(), track=track)
            specific_station.save()
        except:
            print("Something is not yes.")
    else:
        new_track.save()
        specific_station = ChronixRadioTrack(played_time=timezone.now(), track=new_track)
        specific_station.save()


    """# url_img = "https://fastcast4u.com/player/gebacher/"  # example: +"_user/cover/g/gebacher/deveria.jpg"
    url_img = "https://fastcast4u.com/player/gebacher/" + res_data["image"]
    res_img = scrap_img(url_img, "")"""

    time.sleep(60)
    # TODO return data to be added to db


scrap_chronix_page(repeat=60, repeat_until=None)


