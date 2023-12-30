from django.contrib import admin
from .models import AnimationStudio, AnimeList, AnimeAward, TopTierWaifu, BestAnimeOfAllTime
# Register your models here.
class BaseModelAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'updated_at')

class AnimationStudioAdmin(BaseModelAdmin):
    list_display = ('name', 'country', 'FoundedDate', 'created_at', 'updated_at')
    
class AnimeListAdmin(BaseModelAdmin):
    list_display = (
        'title', 'release_date', 'episode', 'description', 'studio', 'created_at', 'updated_at'
    )
class AnimeAwardAdmin(BaseModelAdmin):
    list_display = ('name', 'description', 'GetDate', 'created_at', 'updated_at')

class TopTierWaifuAdmin(BaseModelAdmin):
    list_display = ('name','resultDate', 'img', 'created_at', 'updated_at')

class BestAnimeOfAllTimeAdmin(BaseModelAdmin):
    list_display = ('name', 'release_date', 'rating', 'genres', 'studio', 'created_at', 'updated_at')


admin.site.register(AnimationStudio, AnimationStudioAdmin)
admin.site.register(AnimeList, AnimeListAdmin)
admin.site.register(AnimeAward, AnimeAwardAdmin)
admin.site.register(TopTierWaifu, TopTierWaifuAdmin)
admin.site.register(BestAnimeOfAllTime, BestAnimeOfAllTimeAdmin)