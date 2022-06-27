from django.db import models


class News(models.Model):
    """ model for news object """

    title = models.CharField(max_length=150, verbose_name='заголовок')
    content = models.TextField(verbose_name='Описание')
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')
    image = models.ImageField(upload_to='news', verbose_name='фотография', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'