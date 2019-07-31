from django.db import models


class Catalog(models.Model):
    text = models.CharField(max_length=200, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Каталог Мебели'

    def __str__(self):
        return self.text


class Furniture(models.Model):
    name = models.ForeignKey('Catalog', on_delete=models.PROTECT)
    name_furniture = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='image/evroclassik/furniture', help_text='300x300px',
                              verbose_name='Ссылка картинки', blank=True)
    price = models.IntegerField()
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Мебель'

    def __str__(self):
        return (f'{self.name_furniture}, {self.price} рублей, добавили: ({self.date_added})')


class CatalogPlumbing(models.Model):
    text = models.CharField(max_length=200, blank=True)
    # image = models.ImageField(upload_to='media')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Каталог Сантехники'

    def __str__(self):
        return self.text


class Plumbing(models.Model):
    name = models.ForeignKey('CatalogPlumbing', on_delete=models.PROTECT)
    name_plumbing = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='image/evroclassik/plumbing', help_text='300x300px',
                              verbose_name='Ссылка картинки', blank=True)
    price = models.IntegerField()
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Сантехника и ванные принадлежности'

    def __str__(self):
        return (f'{self.name_plumbing}, {self.price} рублей, добавили: ({self.date_added})')

class HeadSlider(models.Model):
    image = models.ImageField(upload_to='image/evroclassik/headslider',
                              verbose_name='Ссылка картинки', blank=True)
    name = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = 'Главный слайд'

    def __str__(self):
        return self.name

class Slider(models.Model):
    image = models.ImageField(upload_to='image/evroclassik/slider',
                              verbose_name='Ссылка картинки', blank=True)
    name = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = 'Cлайды'

    def __str__(self):
        return self.name

class InfoCompany(models.Model):
    headache = models.CharField(max_length=50, blank=True)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'Информация о компании'

    def __str__(self):
        return (f'Заголово: {self.headache} текст: {self.text}')