from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
                  path('jet/', include('jet.urls', 'jet')),
                  path('admin/', admin.site.urls),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('search/', include('search.urls')),
                  path('news/', include('news.urls')),
                  path('sliders/', include('sliders.urls')),
                  path('menu/', include('menu.urls')),
                  path('auction/', include('auction.urls')),
                  path('ceo/', include('ceo.urls')),
                  path('feedback/', include('feedback.urls')),
                  path('', include('pages.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
