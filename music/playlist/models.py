from django.db import models
import musicbrainz2.webservice as ws


class Artist(models.Model):
    name = models.CharField(max_length=200)
    mbid = models.CharField(max_length=66,blank=True,null=True)

    def get_mbid(self):
	query = ws.Query()
        filter = ws.ArtistFilter(name=self.name,limit=1 )
        mb = query.getArtists(filter=filter)
        if mb[0].score >=90:
            self.mbid = mb[0].artist.id

    def __unicode__(self):
        return self.name
    

class Album(models.Model):
    title  = models.CharField(max_length=200)
    artist = models.ForeignKey('Artist')
    mbid   = models.CharField(max_length=36,blank=True,null=True)

    def get_mbid(self):
	query = ws.Query()
        filter = ws.ReleaseFilter(title=self.title, artistName=self.artist.name,limit=1 )
        mb = query.getReleases(filter=filter)
        if mb[0].score >=90:
            self.mbid = mb[0].release.id

    def __unicode__(self):
        return self.title


class Track(models.Model):
    title  = models.CharField(max_length=200)
    artist = models.ForeignKey('Artist')
    album  = models.ForeignKey('Album')
    guest  = models.BooleanField(True)
    mbid   = models.CharField(max_length=36,blank=True,null=True)

    def get_mbid(self):
	query = ws.Query()
        filter = ws.TrackFilter(title=self.title, artistName=self.artist.name,releaseTitle=self.album.title, limit=1 )
        mb = query.getTracks(filter=filter)
        if mb[0].score >=90:
            self.mbid = mb[0].track.id

    def __unicode__(self):
        return self.title


class GuestArtist(models.Model):
    track = models.ForeignKey('Track')
    guest = models.ForeignKey('Artist')

    def __unicode__(self):
        return self.guest
