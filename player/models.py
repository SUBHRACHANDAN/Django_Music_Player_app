from django.db import models

class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    file = models.FileField(upload_to='music/')
    album_cover = models.ImageField(upload_to='album_covers/', blank=True, null=True)

    def __str__(self):
        return self.title

