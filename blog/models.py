from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')  # link to another module
    title = models.CharField(max_length=200)
    text = models.TextField()
    url = models.URLField(blank=True, null=True)
    source = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to="matrices", blank= True,null =True)
    top_sent = models.TextField(blank=True, null=True)
    trogram = models.CharField(max_length=100, null =True, blank=True)

    #created_date = models.DateField(
        #default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def image_tag(self):
        return u'<img src="%s" />'
    image_tag.short_description ='Image'
    image_tag.allow_tags = True

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u'{f}'.format(f=self.url)
