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
        "chronix_radio": "",
        "chronix_grit": "",
        "chronix_metal": "",
        "chronix_aggression": "https://fastcast4u.com/player/gebacher/index.php?c=ChroniX%20AGGRESSION",
    }

    res = requests.get(stations_urls["chronix_aggression"])
    res.raise_for_status()
    res_data = json.loads(res.text)

    print(f"===========================")
    print(f'Currently played at ChronixAggresion: ')
    print(f'title: {res_data["title"]}')
    print(f'artist: {res_data["artist"]}')
    print(f'album: {res_data["album"]}')

    track_playing_now = Track(
        title=res_data["title"],
        artist=res_data["artist"],
        album=res_data["album"],
    )
    tracks = Track.objects.all()

    if track_playing_now not in tracks:
        track_playing_now.save()  # Saved to Track db
        track_from_station = ChronixAggressionTrack(played_time=timezone.now(), track=track_playing_now)
        track_from_station.save()
        print(f"Was added: {track_playing_now}, id={track_playing_now.pk}")
    else:
        last_played_track = ChronixAggressionTrack.objects.last()
        if not track_playing_now == last_played_track.track:
            track_playing_now = Track.objects.get(
                                        title=track_playing_now.title,
                                        artist=track_playing_now.artist,
                                        album=track_playing_now.album)
            print("AAAAAAAAAAAAAAAAAAAAA")
            track_from_station = ChronixAggressionTrack(
                                        played_time=timezone.now(),
                                        track=track_playing_now
                                        )
            track_from_station.save()
            print("Track was added to sub table.")
        else:
            print("Track is already in sub table.")
    """# url_img = "https://fastcast4u.com/player/gebacher/"  # example: +"_user/cover/g/gebacher/deveria.jpg"
    url_img = "https://fastcast4u.com/player/gebacher/" + res_data["image"]
    res_img = scrap_img(url_img, "")"""
    time.sleep(60)
    # TODO return data to be added to db


scrap_chronix_page(repeat=60, repeat_until=None)
