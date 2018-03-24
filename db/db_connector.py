from pony.orm import Database, Required, Set, set_sql_debug, db_session, select

db = Database()


class Track(db.Entity):
    energy = Required(float)
    liveness = Required(float)
    tempo = Required(float)
    speechiness = Required(float)
    acousticness = Required(float)
    instrumentalness = Required(float)
    time_signature = Required(int)
    danceability = Required(float)
    key = Required(int)
    duration_ms = Required(float)
    loudness = Required(float)
    valence = Required(float)
    tid = Required(str)
    mode = Required(int)


class Meta(db.Entity):
    energy = Required(float)
    liveness = Required(float)


def init_db():
    # PostgreSQL bindings
    db.bind(provider='postgres', user='mgr', password='a', host='localhost', port='5432', database='mgr_db')
    db.generate_mapping(create_tables=True)
    set_sql_debug(True)


@db_session
def create_track(spotify_track):
    p1 = Track(energy=spotify_track['energy'],
               liveness=spotify_track['liveness'],
               tempo=spotify_track['tempo'],
               speechiness=spotify_track['speechiness'],
               acousticness=spotify_track['acousticness'],
               instrumentalness=spotify_track['instrumentalness'],
               time_signature=spotify_track['time_signature'],
               danceability=spotify_track['danceability'],
               key=spotify_track['key'],
               duration_ms=spotify_track['duration_ms'],
               loudness=spotify_track['loudness'],
               valence=spotify_track['valence'],
               tid=spotify_track['id'],
               mode=spotify_track['mode']
               )
    # select(p for p in Track).order_by(Track.name)[:2].show()
    Track.select().show()


@db_session
def print_track(track_id):
    t = Track[track_id]
    print t.tid
    # database session cache will be cleared automatically
    # database connection will be returned to the pool




