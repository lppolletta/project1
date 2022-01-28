from rest_framework import serializers
from playlists.models import Playlist
from playlists.models import Track

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'name', 'artist', 'length')

class PlaylistSerializer(serializers.ModelSerializer):
    tracks_in_list = TrackSerializer(many=True)

    class Meta:
        model = Playlist
        fields = ('id', 'title')
