from django.db import models

# Create your models here.


class BaseModel (models.Model) :
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class AnimationStudio(BaseModel):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    FoundedDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class AnimeList(BaseModel):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    episode = models.IntegerField()
    description = models.TextField()
    studio = models.ForeignKey(AnimationStudio, on_delete=models.CASCADE)
    awards = models.ManyToManyField('AnimeAward', related_name='anime_awards')

    def __str__(self):
        return self.title

class AnimeAward(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    GetDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class TopTierWaifu(BaseModel):
    name = models.CharField(max_length=255)
    anime_list = models.ForeignKey(AnimeList, on_delete=models.CASCADE, null=True, blank=True) 
    resultDate = models.DateField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True, upload_to="images/")


    def __str__(self):
        return self.name

class BestAnimeOfAllTime(BaseModel):
    name = models.CharField(max_length=255)
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=10,default=0,decimal_places=2,null=True)
    genres = models.CharField(max_length=255)
    studio = models.ForeignKey(AnimationStudio, on_delete=models.CASCADE)
    waifus = models.ManyToManyField(TopTierWaifu, related_name='best_anime_waifus')

    def __str__(self):
        return self.name
