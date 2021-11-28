from django.urls import path
from .views import simple_get, wrike_incoming, wrike_outgoing
urlpatterns = [
    path('wrike-incoming', wrike_incoming),
    path('', simple_get),
    path("wrike-outgoing", wrike_outgoing)

]
