from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from playlists.models import Track
from playlists.serializers import TrackSerializer
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return render(request, "playlists/index.html")


def index(request):
    print("------------------------- I AM HERE")
    queryset = Track.objects.all()
    return render(request, "playlists/index.html", {'tracks': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'playlists/index.html'

    def get(self, request):
        queryset = Track.objects.all()
        return Response({'tracks': queryset})


class list_all_tracks(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'playlists/track_list.html'

    def get(self, request):
        queryset = Track.objects.all()
        return Response({'playlists': queryset})


@api_view(['GET', 'POST', 'DELETE'])
def track_list(request):
    if request.method == 'GET':
        tracks = Track.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            tracks = tracks.filter(name__icontains=name)

        tracks_serializer = TrackSerializer(tracks, many=True)
        return JsonResponse(tracks_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        track_data = JSONParser().parse(request)
        track_serializer = TrackSerializer(data=track_data)
        if track_serializer.is_valid():
            track_serializer.save()
            return JsonResponse(track_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(track_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Track.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Tracks were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def track_detail(request, pk):
    try:
        track = Track.objects.get(pk=pk)
    except Track.DoesNotExist:
        return JsonResponse({'message': 'The track does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        track_serializer = TrackSerializer(track)
        return JsonResponse(track_serializer.data)

    elif request.method == 'PUT':
        track_data = JSONParser().parse(request)
        track_serializer = TrackSerializer(track, data=track_data)
        if track_serializer.is_valid():
            track_serializer.save()
            return JsonResponse(track_serializer.data)
        return JsonResponse(track_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        track.delete()
        return JsonResponse({'message': 'Track was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)

