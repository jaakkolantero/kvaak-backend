from django.conf.urls import url, include
from rest_framework import routers
from .views import species_list


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'species', SpeciesViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^test/$', species_list),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
