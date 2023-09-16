from django.db import models

'''
# при помощи CharField можно создавать текст не больше 250 символов
# при помощи TextField можно создавать текст более 20 тыс.символов
# DateTimeField - можно указать дату + время
'''


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    image = models.ImageField(default='news/image/no_image.jpg', upload_to='news/image/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
