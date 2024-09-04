# creacion de las rutas que necesita consultar el frontend
# api versioning
from django.urls import path, include
from rest_framework import routers
from tasks import views

# creando objeto router para contener la creacion de las urls
router = routers.DefaultRouter()
router.register(r"tasks", views.TaskView, "tasks")
urlpatterns = [path("api/v1/", include(router.urls))]
