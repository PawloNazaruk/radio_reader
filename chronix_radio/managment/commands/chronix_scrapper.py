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

    """# url_img = "https://fastcast4u.com/player/gebacher/"  # example: +"_user/cover/g/gebacher/deveria.jpg"
    url_img = "https://fastcast4u.com/player/gebacher/" + res_data["image"]
    res_img = scrap_img(url_img, "")
    with open("test."+url[-3:], "wb+") as fp:
        for chunk in res.iter_content(100000):
            fp.write(chunk)"""

    return res


def scrap_radio_song(url):
    res = requests.get(url)
    try:
        res.raise_for_status()
        res_track = json.loads(res.text)

        print(f"===========================")
        print(f'Currently played at ChronixAggresion: ')
        print(f'title: {res_track["title"]}')
        print(f'artist: {res_track["artist"]}')
        print(f'album: {res_track["album"]}')

        track_played_now = Track(
            title=res_track["title"],
            artist=res_track["artist"],
            album=res_track["album"],
        )
        tracks = Track.objects.all()

        if track_played_now not in tracks:
            track_played_now.save()  # Saved to Track db

            track_from_station = ChronixAggressionTrack(played_time=timezone.now(), track=track_played_now)
            track_from_station.save()
            print(f"Was added: {track_played_now}, id={track_played_now.pk}")
        else:
            last_played_track = ChronixAggressionTrack.objects.last()
            if not track_played_now == last_played_track.track:
                track_played_now = Track.objects.get(
                    title=track_played_now.title,
                    artist=track_played_now.artist,
                    album=track_played_now.album)
                track_from_station = ChronixAggressionTrack(
                    played_time=timezone.now(),
                    track=track_played_now
                )
                track_from_station.save()
                print("Track was added to sub table.")
            else:
                print("Track is already in sub table.")
    except:
        print("========================")
        print("Something is not yes with accessing radio web page. ")
        print("========================")

def scrap_song_data():
    pass

def scrap_img_data():
    pass



@background(schedule=60)
def scrap_chronix():
    """
    Function for reading currently played song at chronix radio.
    """
    log_time()

    ChronixStation = namedtuple('ChronixStation', "name db_name url")
    grit = ChronixStation(name='grit',
                          db_name=ChronixGritTrack,
                          url="https://fastcast4u.com/player/chronixg/index.php?c=ChroniX%20|%20GRIT"
                          )
    metal = ChronixStation(name="metal",
                           db_name=ChronixMetalTrack,
                           url="https://fastcast4u.com/player/chronixr/index.php?c=ChroniX%20|%20METALCORE"
                           )
    aggression = ChronixStation(name="aggression",
                                db_name=ChronixAggressionTrack,
                                url="https://fastcast4u.com/player/gebacher/index.php?c=ChroniX%20AGGRESSION"
                                )
    stations = [grit, metal, aggression]

    for station in stations:
        print(station)






    time.sleep(20)
    # TODO return data to be added to db


scrap_chronix(repeat=60, repeat_until=None)
