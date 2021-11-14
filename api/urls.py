from django.urls import path
from .views import simple_get, wrike_incoming
urlpatterns = [
    path('wrike-incoming', wrike_incoming),
    path('', simple_get),

]
