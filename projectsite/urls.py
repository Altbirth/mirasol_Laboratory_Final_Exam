"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from anime.views import HomePageView, AnimationStudioList,  AnimeListList, AnimeAwardList, TopTierWaifuList, BestAnimeOfAllTimeList
from anime.views import AnimationStudioCreateView, AnimeListCreateView, AnimeAwardCreateView, TopTierWaifuCreateView, BestAnimeOfAllTimeCreateView
from anime.views import AnimationStudioUpdateView, AnimeListUpdateView, AnimeAwardUpdateView, TopTierWaifuUpdateView, BestAnimeOfAllTimeUpdateView
from anime.views import AnimationStudioDeleteView, AnimeListDeleteView, AnimeAwardDeleteView, TopTierWaifuDeleteView, BestAnimeOfAllTimeDeleteView
from anime import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('AnimationStudio_list', AnimationStudioList.as_view(), name='AnimationStudio-list'),
    path('AnimationStudio_list/add', AnimationStudioCreateView.as_view(), name='AnimationStudio-add'),
    path('AnimationStudio_list/<pk>', AnimationStudioUpdateView.as_view(), name='AnimationStudio-update'),
    path('AnimationStudio_list/<pk>/delete',AnimationStudioDeleteView.as_view(), name='AnimationStudio-delete'),

    path('AnimeList_list', AnimeListList.as_view(), name='AnimeList-list'),
    path('AnimeList_list/add', AnimeListCreateView.as_view(), name='AnimeList-add'),
    path('AnimeList_list/<pk>', AnimeListUpdateView.as_view(), name='AnimeList-update'),
    path('AnimeList_list/<pk>/delete',AnimeListDeleteView.as_view(), name='AnimeList-delete'),
    
    path('AnimeAward_list', AnimeAwardList.as_view(), name='AnimeAward-list'),
    path('AnimeAward_list/add', AnimeAwardCreateView.as_view(), name='AnimeAward-add'),
    path('AnimeAward_list/<pk>', AnimeAwardUpdateView.as_view(), name='AnimeAward-update'),
    path('AnimeAward_list/<pk>/delete',AnimeAwardDeleteView.as_view(), name='AnimeAward-delete'),

    path('TopTierWaifu_list', TopTierWaifuList.as_view(), name='TopTierWaifu-list'),
    path('TopTierWaifu_list/add', TopTierWaifuCreateView.as_view(), name='TopTierWaifu-add'),
    path('TopTierWaifu_list/<pk>', TopTierWaifuUpdateView.as_view(), name='TopTierWaifu-update'),
    path('TopTierWaifu_list/<pk>/delete',TopTierWaifuDeleteView.as_view(), name='TopTierWaifu-delete'),

    path('BestAnimeOfAllTime_list', BestAnimeOfAllTimeList.as_view(), name='BestAnimeOfAllTime-list'),
    path('BestAnimeOfAllTime_list/add', BestAnimeOfAllTimeCreateView.as_view(), name='BestAnimeOfAllTime-add'),
    path('BestAnimeOfAllTime_list/<pk>', BestAnimeOfAllTimeUpdateView.as_view(), name='BestAnimeOfAllTime-update'),
    path('BestAnimeOfAllTime_list/<pk>/delete',BestAnimeOfAllTimeDeleteView.as_view(), name='BestAnimeOfAllTime-delete'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
