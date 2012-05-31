from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	url(r'^wras/playlist/$','playlist.views.index'),
     
     #artists
	url(r'^wras/artist/(?P<artist_name>[A-Za-z0-9_-]+)/$','playlist.views.artist_page'),
	url(r'^wras/artist/id/(?P<id>\d+)/$','playlist.views.artist_page'),
     
     #albums
	url(r'^wras/album/(?P<album_title>[A-Za-z0-9_-]+)/$','playlist.views.album_page'),
	url(r'^wras/album/id/(?P<id>\d+)/$','playlist.views.album_page'),
     
     #tracks
	url(r'^wras/track/(?P<track_title>[A-Za-z0-9_-]+)/$','playlist.views.track_page'),
	url(r'^wras/track/id/(?P<id>\d+)/$','playlist.views.track_page'),
)

