from django.db import models
from django.utils.translation import ugettext_lazy as _


class Blog(models.Model):
    title = models.CharField(max_length=140, unique=True)
    slug = models.SlugField(max_length=140, unique=True)
    body = models.TextField()

    posted = models.DateTimeField(auto_now_add=True, verbose_name=_('postDate'))
    modified = models.DateTimeField(null=True, verbose_name=_('modified'))
    category = models.ForeignKey('blog.Category', on_delete=models.CASCADE)

    class Meta:
        verbose_name=_('post')
        verbose_name_plural=_('posts')
        ordering = ['-posted']

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=140, db_index=True)
    slug = models.SlugField(max_length=140, db_index=True)

    def __str__(self):
        return self.title