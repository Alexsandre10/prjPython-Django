from django.urls import path, include
from django.contrib import admin
from simplemooc.core.views import home
admin.autodiscover()
app_name='core'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('simplemooc.core.urls', namespace='core')),
    path('aa/', include('simplemooc.core.home.views'), name='home'),
]
