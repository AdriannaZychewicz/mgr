from db.db_connector import init_db, create_track
from spotify_connector import get_track_ids_by_genre, get_track_features, get_track_analytics

tid = 'spotify:track:5dvBeCMTzUNjyWIcuykzyh'
user_me = 'maka_pszenna'
user ='theblackkeysofficial'


def main():
    init_db()
    # get_playlist_by_user(user)
    ids = get_track_ids_by_genre('rock', 1)
    # print_tracks_from_playlist(user)
    #
    # tracks = get_tracks_from_playlist(user)
    tracks = get_track_features(ids)
    for track in tracks:
        create_track(track)
    get_track_analytics(tid)


if __name__ == "__main__":
    main()
