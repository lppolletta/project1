# project1 - my_playlists

This project allows a User to create a new music playlist. Then user can add tracks to or remove tracks from the playlist.
A list of all tracks on the playlist can be displayed. The user needs to create each track first to add to a playlist.

## Usage

Working:

    add Track:
        POST {{ _.base_url }}/api/playlists/
        {  
            "name":"Karma Police",
            "artist":"Radiohead",
            "length":"4.21"
        }
    
    Track List:   
        GET {{ _.base_url }}/api/playlists/

    Track Detail:   
        GET {{ _.base_url }}/api/playlists/

Not Working:

    add Playlist:
    Playlist Detail:

    All Tracks on PLaylist:

### Server

* URL: http://ec2-54-166-115-145.compute-1.amazonaws.com:8000


### Postgres DB

* endpoint: project1.cluyel9qcqsq.us-east-1.rds.amazonaws.com
* db name: my_playlists

