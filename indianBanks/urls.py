from django.conf.urls import url, include
# from django.contrib import admin
from banks import urls as bankUrl

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^banks/', include(bankUrl))
]
