import itertools
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import time

CLIENT_ID = 'c7c4991f2d17404982918a49010b7340'
CLIENT_SECTRET = '05dad06897514d4aabd4c91a40c755aa'
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECTRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_track_ids_by_genre(genre, limit):
    track_ids = []
    playlists = sp.category_playlists(category_id=genre,  limit=limit, offset=0)['playlists']
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            result = sp.user_playlist(user=playlist['owner']['id'], playlist_id=playlist['id'], fields="tracks,next")
            track_ids = track_ids + get_track_ids(result)
            print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'], playlist['name']))
        if i < limit:
            playlists = None
        elif playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None
    return track_ids


def get_playlist_by_user(user):
    playlists = sp.user_playlists(user)
    for playlist in playlists['items']:
        if playlist['owner']['id'] == user:
            print
            print playlist['name']
            print '  total tracks', playlist['tracks']['total']
            results = sp.user_playlist(user, playlist['id'],
                                       fields="tracks,next")
            tracks = results['tracks']
            show_tracks(tracks)
            while tracks['next']:
                tracks = sp.next(tracks)
                show_tracks(tracks)
    return results


def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print "   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name'])


def get_track_ids(playlist):
    track_ids = []
    for tr in playlist['tracks']['items']:
        track_ids.append(tr['track']['id'])
    return track_ids


def print_tracks_from_playlist(user):
    playlists = sp.user_playlists(user)
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None


def get_track_features(tracks):
    features = sp.audio_features(tracks)
    print(json.dumps(features, indent=4))
    for feature in features:
        print(json.dumps(feature, indent=4))
        print()
        # analysis = sp._get(feature['analysis_url'])
        # print(json.dumps(analysis, indent=4))
        # print()


def get_track_features(tid):
    features = sp.audio_features(tid)
    print(json.dumps(features, indent=4))
    for feature in features:
        print json.dumps(feature, indent=4)
    return features


def get_track_analytics(tid):
    analytics = sp.audio_analysis(tid)
    print(json.dumps(analytics, indent=4))
    # for feature in analytics:
    #     print json.dumps(feature, indent=4)
    return analytics

        # analysis = sp._get(feature['analysis_url'])
        # print(json.dumps(analysis, indent=4))
        # print()

# tid = 'spotify:track:5dvBeCMTzUNjyWIcuykzyh'
# analysis = sp.audio_analysis(tid)
# start = time.time()
# analysis = sp.audio_analysis(tid)
# delta = time.time() - start
# # print(json.dumps(analysis, indent=4))
# # print ("analysis retrieved in %.2f seconds" % (delta,))
#
# ##################################################################
# # results = sp.search(q=artist_name, limit=50)
# # tids = []
# # for i, t in enumerate(results['tracks']['items']):
# #     print(' ', i, t['name'])
# #     tids.append(t['uri'])
#
# start = time.time()
# features = sp.audio_features(tid)
# delta = time.time() - start
# for feature in features:
#     print(json.dumps(feature, indent=4))
#     print()
#     analysis = sp._get(feature['analysis_url'])
#     print(json.dumps(analysis, indent=4))
#     print()
# print ("features retrieved in %.2f seconds" % (delta,))