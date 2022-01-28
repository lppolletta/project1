from django.urls import path
from playlists import views as playlists_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', playlists_views.index.as_view(), name='home'),
    path('api/playlists/', playlists_views.track_list),
    path('api/playlists/<int:pk>/', playlists_views.track_detail)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
