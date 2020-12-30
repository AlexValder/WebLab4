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


class Comments(models.Model):
    comment = models.TextField('comment')
    usrname = models.CharField('usrname', max_length=25)
    date = models.DateField('date')
    slugTitle = models.SlugField('slugTitle', max_length=30)


    def __str__(self):
        return f'{self.usrname}\'s comment.'


    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
