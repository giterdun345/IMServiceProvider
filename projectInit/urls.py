from django.urls import path
from .views import project_get, project_incoming
urlpatterns = [
    path('project-incoming/', project_incoming),
    path('', project_get),
    # path("project-outgoing", project_outgoing)

]