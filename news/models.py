from django.db import models


class Article(models.Model):
    title = models.CharField('Title', max_length=50, default='No title')
    preview = models.CharField('Preview', max_length=250)
    full_text = models.TextField('Article')
    date = models.DateTimeField('Publication date')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
