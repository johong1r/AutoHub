from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="AutoHub",
        default_version='v1',
        description='AutoHub — это удобная и понятная площадка для покупки автомобилей. Мы собрали всё в одном месте: актуальные объявления, честные характеристики, прозрачные цены и удобный поиск. У нас нет лишней воды — только реальная информация о машинах, чтобы ты смог выбрать авто быстро и без головной боли.'
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
]