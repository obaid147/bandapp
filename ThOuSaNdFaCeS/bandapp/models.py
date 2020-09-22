from django.db import models


class Music(models.Model):
    song_title = models.CharField(max_length=100, default=None)
    email = models.EmailField(max_length=254, default=None)
    Mp3 = models.FileField(upload_to='fans_files/mp3/', max_length=100,
                           help_text='Upload mp3 Format')
