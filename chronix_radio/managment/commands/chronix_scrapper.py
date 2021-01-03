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


def print_currently_played_song(station, track_json):
    print(f"===========================")
    print(f'Currently played at {station.name}: ')
    print(f'title: {track_json["title"]}')
    print(f'artist: {track_json["artist"]}')
    print(f'album: {track_json["album"]}')


def scrap_song_data(station):
    res = requests.get(station.url)
    track_json = {}
    try:
        res.raise_for_status()
        track_json = json.loads(res.text)
        print_currently_played_song(station, track_json)
    except:
        print("========================")
        print("Something is not yes with accessing radio web page.")
        print("========================")

    img_url = "https://fastcast4u.com/player/gebacher/" + track_json["image"]
    res_img = requests.get(img_url)
    img_extension = "." + img_url.split(".")[-1]
    try:
        res_img.raise_for_status()
    except:
        print("========================")
        print("Img file not found.")
        print("========================")
    return track_json, res_img, img_extension


def save_img(res_img, img_extension, track_id):
    path = "media/track." + str(track_id).zfill(6) + img_extension
    with open(path, "wb+") as fp:
        for chunk in res_img.iter_content(100000):
            fp.write(chunk)


@background(schedule=60)
def scrap_chronix():
    """
    Function for reading currently played song at chronix radio.
    """
    log_time()

    ChronixStation = namedtuple('ChronixStation', "name db_name url")
    grit = ChronixStation(name='grit',
                          db_name=ChronixGritTrack,
                          url="https://fastcast4u.com/player/chronixg/index.php?c=ChroniX%20|%20GRIT",
    )
    metal = ChronixStation(name="metal",
                           db_name=ChronixMetalTrack,
                           url="https://fastcast4u.com/player/chronixr/index.php?c=ChroniX%20|%20METALCORE",
    )
    aggression = ChronixStation(name="aggression",
                                db_name=ChronixAggressionTrack,
                                url="https://fastcast4u.com/player/gebacher/index.php?c=ChroniX%20AGGRESSION",
    )
    stations = [grit, metal, aggression]

    for station in stations:
        #TODO processing img
        print(station)
        track_json, res_img, img_extension = scrap_song_data(station)
        track_played_now = Track(
            title=track_json["title"],
            artist=track_json["artist"],
            album=track_json["album"],
        )

        print_this(track_json["album"])

        tracks = Track.objects.all()
        if track_played_now not in tracks:
            track_played_now.save()  # Saved to Track db
            track_to_station = station.db_name(played_time=timezone.now(), track=track_played_now)
            track_to_station.save()
            save_img(res_img, img_extension, track_played_now.id)
            print(f"Was added: {track_played_now}, id={track_played_now.pk}")
        else:
            track_last_played = station.db_name.objects.last()
            if not track_played_now == track_last_played.track:
                # creating track with id from db
                track_played_now = Track.objects.get(title=track_played_now.title,
                                                    artist=track_played_now.artist,
                                                    album=track_played_now.album,
                )
                track_to_station = station.db_name(played_time=timezone.now(),
                                                   track=track_played_now,
                )
                track_to_station.save()
                print("Track was added to sub table.")
            else:
                print("Track was already added to sub table just before.")
    time.sleep(60)


def print_this(text):
    print("===========================================")
    print("===========================================")
    print(f"{text}")
    print("===========================================")
    print("===========================================")


scrap_chronix(repeat=60, repeat_until=None)
