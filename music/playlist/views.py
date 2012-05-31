from playlist.models  import Artist, Album, Track
from django.shortcuts import render_to_response
import pylast

def index(request):
    latest_songs = Track.objects.all()
    for song in latest_songs:
# lookup the song on lstt.fm	
    return render_to_response('tracks.html',{'latest_songs':latest_songs})
    
def artist_page(request, artist_name=None, id=None):
    if artist_name: 
        artist_name = artist_name.replace('_',' ')
        artist = Artist.objects.get(name=artist_name)
    else:
        artist = Artist.objects.get(pk=id)
    albums = Album.objects.filter(artist=artist) 
    tracks = [Track.objects.filter(album=album) for album in albums]
    return render_to_response('artist_page.html',{'artist':artist,'albums':albums,'tracks':tracks})

def album_page(request,album_title=None,id=None):
    if album_title:
        album_title = album_title.replace('_',' ')
        album       = Album.objects.get(title=album_title)
    else:
        album       = Album.objects.get(pk=id)
    tracks          = Track.objects.filter(album=album)
    return render_to_response('album_page.html',{'album':album,'tracks':tracks})

def track_page(request,track_title=None,id=None):
    if track_title:
        track_title = track_title.replace('_',' ')
        track       = Track.objects.get(title=track_title)
    else:
        track       = Track.objects.get(pk=id)
    return render_to_response('track_page.html',{'track':track})

def song_proxy(request, artist, title):
	artist = Artist.objects.get(name=artist)
	track  = Track.objects.get(name=track)
    network = pylast.LastFMNetwork()