from django.conf.urls import include, url
from django.contrib import admin

from almaz.views import *       # мой личное приложение
from django.urls import path


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('hedge_martin/', index_4),          # edit json file hedge_martin
    path('trade_extremum/', index_5),        # edit json file trade_extremum
    path('global_levels/', global_levels),   # edit json file global_levels
    path('otchet/', index_6),           # отчет из json
    path('table/', index_7),            # вывод итога из json_files to Html + Css
]
