
import xadmin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include
from werobot.contrib.django import make_view
from apps.accounts import views

urlpatterns = [
    # add your own patterns here
    path('admin/', xadmin.site.urls, name="admin"),
    path('mdeditor/', include('mdeditor.urls')),
    path('comment/', include('apps.comment.urls')),
    path('', include('apps.notice.urls')),
    path('', include('apps.myzone.urls')),
    path('notifications/', include('notifications.urls', namespace='notifications')),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('', include('apps.mysite.urls')),
    path('', include('apps.blog.urls')),
    path('search/', include('haystack.urls')),
    path('api/', include([
        path('', include('apps.mysite.api.urls')),
    ])),
    
]
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)