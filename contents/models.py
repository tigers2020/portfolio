from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from sorl.thumbnail import get_thumbnail


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Images(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        s = '[%s]%s' % (self.category, self.image.name)
        return s

    def image_tag(self):
        im = get_thumbnail(self.image, '250x125', crop='center')
        return mark_safe('<img src="%s" with=250px />' % im.url)


class Contents(models.Model):
    user = models.ForeignKey(User, related_name='cotents', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, allow_unicode=True)
    main_text = models.BooleanField(default=False)
    published_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    images = models.ManyToManyField(Images, blank=True)
    contents = RichTextField(blank=True, default='')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.modified_date = timezone.now()
        self.slug = slugify(self.title)
        super(Contents, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Contents'
        ordering = ['-created_date']

