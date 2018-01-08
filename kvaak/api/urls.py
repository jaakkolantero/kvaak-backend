from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import species_list
from .views import species_detail
from .views import sightings_list
from .views import sighting_detail


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'species', SpeciesViewSet)


urlpatterns = [
    url(r'^species/$', species_list),
    url(r'^species/(?P<pk>[0-9]+)$', species_detail),
    url(r'^sightings/$', sightings_list),
    url(r'^sightings/(?P<pk>[0-9]+)$', sighting_detail),
    # url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
