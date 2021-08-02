from django.urls import path
from tg_processor import views as tg_views

urlpatterns = [
#    path('admin/', admin.site.urls),
    path('', tg_views.index),
    path('e656371110e5497bf12bde143b4908ae/', tg_views.bot_input),
]
