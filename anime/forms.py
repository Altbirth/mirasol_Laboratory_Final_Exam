from django.forms import ModelForm
from django import forms
from anime.models import AnimeAward, BestAnimeOfAllTime, AnimeList, AnimationStudio, TopTierWaifu

class AnimeListForm(ModelForm):
    release_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = AnimeList
        fields = "__all__"

class AnimeAwardForm(ModelForm):
    GetDate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = AnimeAward
        fields = "__all__"

class BestAnimeOfAllTimeForm(ModelForm):
    release_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = BestAnimeOfAllTime
        fields = "__all__"


class AnimationStudioForm(ModelForm):
    FoundedDate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = AnimationStudio
        fields = "__all__"

class TopTierWaifuForm(ModelForm):
    resultDate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = TopTierWaifu
        fields = "__all__"