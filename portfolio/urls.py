from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/<int:pk>', views.category_posts, name='category_posts'),
    path('details/<int:pk>', views.details, name='details')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
