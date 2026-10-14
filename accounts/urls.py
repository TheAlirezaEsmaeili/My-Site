from django.urls import include, path

app_name = 'accounts'

urlpatterns = [
    path("api/v1/", include("blog.api.v1.urls")),
    path("", include("django.contrib.auth.urls")),
]