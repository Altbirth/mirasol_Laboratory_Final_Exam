from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from anime.models import AnimationStudio, AnimeList, AnimeAward, TopTierWaifu, BestAnimeOfAllTime
from anime.forms import AnimeListForm, AnimeAwardForm, BestAnimeOfAllTimeForm, AnimationStudioForm, TopTierWaifuForm
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(ListView):
    model = AnimeList
    context_object_name = 'home'
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
#-----------------------------Anime Studio------------------------------
class AnimationStudioList(ListView):
    model = AnimationStudio
    context_object_name = 'AnimationStudio'
    template_name = "AnimationStudio.html"
    paginate_by = 8

class AnimationStudioCreateView(CreateView):
    model = AnimationStudio
    form_class = AnimationStudioForm
    template_name = 'AnimationStudio_add.html'
    success_url = reverse_lazy('AnimationStudio-list')


class AnimationStudioUpdateView(UpdateView):
    model = AnimationStudio
    form_class = AnimationStudioForm
    template_name = 'AnimationStudio_edit.html'
    success_url = reverse_lazy('AnimationStudio-list')


class AnimationStudioDeleteView(DeleteView):
    model = AnimationStudio
    template_name = 'AnimationStudio_del.html'
    success_url = reverse_lazy('AnimationStudio-list')


#-----------------------------Anime List------------------------------
class AnimeListList(ListView):
    model = AnimeList
    context_object_name = 'AnimeList'
    template_name = "AnimeList.html"
    paginate_by = 5
    

class AnimeListCreateView(CreateView):
    model = AnimeList
    form_class = AnimeListForm
    template_name = 'AnimeList_add.html'
    success_url = reverse_lazy('AnimeList-list')


class AnimeListUpdateView(UpdateView):
    model = AnimeList
    form_class = AnimeListForm
    template_name = 'AnimeList_edit.html'
    success_url = reverse_lazy('AnimeList-list')


class AnimeListDeleteView(DeleteView):
    model = AnimeList
    template_name = 'AnimeList_del.html'
    success_url = reverse_lazy('AnimeList-list')



#-----------------------------Anime Awards------------------------------
class AnimeAwardList(ListView):
    model = AnimeAward
    context_object_name = 'AnimeAward'
    template_name = "AnimeAward.html"
    paginate_by = 5

class AnimeAwardCreateView(CreateView):
    model = AnimeAward
    form_class = AnimeAwardForm
    template_name = 'AnimeAward_add.html'
    success_url = reverse_lazy('AnimeAward-list')


class AnimeAwardUpdateView(UpdateView):
    model = AnimeAward
    form_class = AnimeAwardForm
    template_name = 'AnimeAward_edit.html'
    success_url = reverse_lazy('AnimeAward-list')


class AnimeAwardDeleteView(DeleteView):
    model = AnimeAward
    template_name = 'AnimeAward_del.html'
    success_url = reverse_lazy('AnimeAward-list')



#-----------------------------Anime Waifu------------------------------
class TopTierWaifuList(ListView):
    model = TopTierWaifu
    context_object_name = 'TopTierWaifu'
    template_name = "TopTierWaifu.html"
    paginate_by = 8

class TopTierWaifuCreateView(CreateView):
    model = TopTierWaifu
    form_class = TopTierWaifuForm
    template_name = 'TopTierWaifu_add.html'
    success_url = reverse_lazy('TopTierWaifu-list')


class TopTierWaifuUpdateView(UpdateView):
    model = TopTierWaifu
    form_class = TopTierWaifuForm
    template_name = 'TopTierWaifu_edit.html'
    success_url = reverse_lazy('TopTierWaifu-list')


class TopTierWaifuDeleteView(DeleteView):
    model = TopTierWaifu
    template_name = 'TopTierWaifu_del.html'
    success_url = reverse_lazy('TopTierWaifu-list')


#-----------------------------Anime Best All Time------------------------------
class BestAnimeOfAllTimeList(ListView):
    model = BestAnimeOfAllTime
    context_object_name = 'BestAnimeOfAllTimeList'
    template_name = "BestAnimeOfAllTimeList.html"
    paginate_by = 8

class BestAnimeOfAllTimeCreateView(CreateView):
    model = BestAnimeOfAllTime
    form_class = BestAnimeOfAllTimeForm
    template_name = 'BestAnimeOfAllTimeList_add.html'
    success_url = reverse_lazy('BestAnimeOfAllTime-list')


class BestAnimeOfAllTimeUpdateView(UpdateView):
    model = BestAnimeOfAllTime
    form_class = BestAnimeOfAllTimeForm
    template_name = 'BestAnimeOfAllTimeList_edit.html'
    success_url = reverse_lazy('BestAnimeOfAllTime-list')


class BestAnimeOfAllTimeDeleteView(DeleteView):
    model = BestAnimeOfAllTime
    template_name = 'BestAnimeOfAllTimeList_del.html'
    success_url = reverse_lazy('BestAnimeOfAllTime-list')
