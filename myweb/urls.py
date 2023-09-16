# отслеживание различных url адресов (ПРИМЕР: при переходе на главную страницу - отображается такой то шаблон)
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # с его помощью открывается панель администратора
    path('admin/', admin.site.urls),  # с его помощью открывается панель администратора
    path('', include('main.urls')),
    path('news/', include('news.urls')),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# было + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),

''' РАБОТАЕТ 
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
'''
