from django.db import models


class Anime(models.Model):
    title = models.CharField('title', max_length=50)
    description = models.TextField('description')
    picture = models.TextField('picture')
    genre = models.CharField('genre', max_length=25)
    released = models.DateField('released')
    slugTitle = models.SlugField('slugTitle', max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Anime'
        verbose_name_plural = 'Animes'

# class User(models.Model):
#     username = models.CharField('username', max_length=50)
#     password = models.CharField('password', max_length=50)
#     email    = models.CharField('email', max_length=320)
#     date     = models.DateField('date')
#     # title = models.CharField('Name', max_length=50)
#     # task = models.TextField('Desctiption')

#     def __str__(self):
#         return self.username