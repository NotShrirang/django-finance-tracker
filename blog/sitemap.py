from django.contrib.sitemaps import Sitemap
from .models import BlogPost
from django.urls import reverse

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return BlogPost.objects.all()

    def location(self, item):
        return reverse('blog_detail', args=[item.slug])

    def lastmod(self, item):
        return item.updated_date
