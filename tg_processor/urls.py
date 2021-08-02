from django.urls import path
from tg_processor import views as tg_views

from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from tg_processor.views import TutorialBotView

urlpatterns = [
#    path('admin/', admin.site.urls),
#     path('', tg_views.index),
    # path('e656371110e5497bf12bde143b4908ae/', tg_views.bot_input),
    path('e656371110e5497bf12bde143b4908ae/', csrf_exempt(TutorialBotView.as_view())),
]
