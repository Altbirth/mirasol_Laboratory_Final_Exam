from django.core.management.base import BaseCommand
from anime.models import AnimationStudio, AnimeAward

class Command (BaseCommand) :
    help = 'Create Initial data for the application'

    def handle(self, *args, **kwargs) :
        self.create_AnimationStudio()
        self.create_AnimeAward()

    def create_AnimationStudio (self) :
        card1 = AnimationStudio(name="Ufotable", country="Japan")
        card1.save()
      
        self.stdout.write(self.style.SUCCESS('Successfuly created Anime Studio.'))

    def create_AnimeAward(self) :
        trainer1 = AnimeAward(name="Best Film", description= "Cyberpunk: Edgerunners won the Anime of the Year award.",GetDate= "2023-03-04")
        trainer1.save()
     
        self.stdout.write(self.style.SUCCESS('Successfuly created Anime Award.'))