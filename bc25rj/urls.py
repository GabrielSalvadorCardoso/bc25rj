from django.urls import path, include

app_name = "bc25rj"
urlpatterns = [
    path('api/bc25/rj/', include('rj.urls', namespace="entrypoint"))#, name="entrypoint"),
]