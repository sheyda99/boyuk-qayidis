from django.db import models
from django.urls import reverse
from django.utils.text import slugify



# Create your models here.


class News(models.Model):

    # information
    image = models.ImageField('Əsas Şəkil', upload_to = 'news')
    title = models.CharField('Başlıq', max_length = 256)
    image1 = models.ImageField('Şəkil1', upload_to = 'news', null=True, blank=True)
    image2 = models.ImageField('Şəkil2', upload_to = 'news', null=True, blank=True)
    image3 = models.ImageField('Şəkil3', upload_to = 'news', null=True, blank=True)
    image4 = models.ImageField('Şəkil4', upload_to = 'news', null=True, blank=True)
    image5 = models.ImageField('Şəkil5', upload_to = 'news', null=True, blank=True)
    description1 = models.TextField('Qısa məzmun', max_length = 2000)
    description2 = models.TextField('Məzmun1', max_length = 2000, null=True, blank=True)
    description3 = models.TextField('Məzmun2', max_length = 2000, null=True, blank=True)
    description4 = models.TextField('Məzmun3', max_length = 2000, null=True, blank=True)
    description5 = models.TextField('Məzmun4', max_length = 2000, null=True, blank=True)
    pdf_title = models.CharField('Pdf faylının adı', max_length = 256, null=True, blank=True)
    pdf = models.FileField('Pdf faylı', upload_to='media/pdf', null=True, blank=True)
    slug = models.SlugField('Slug', max_length = 110, unique = True, editable = False)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('news_detail', kwargs = {'slug': self.slug})

    def get_uniqe_slug(self):
        slug = slugify(self.title.replace('ə', 'e'))
        unique_slug = slug
        counter = 1
        while News.objects.filter(slug = unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug


    def save(self, *args, **kwargs):
        self.slug = self.get_uniqe_slug()
        return super(News, self).save(*args, **kwargs)