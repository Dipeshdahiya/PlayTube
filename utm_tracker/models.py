from django.db import models

class Source(models.Model):
    name = models.CharField(max_length=100, unique=True, primary_key=True)

    def __str__(self):
        return self.name

class Traffic(models.Model):
    source = models.OneToOneField(Source, on_delete=models.SET_DEFAULT, default='direct')
    visits = models.PositiveIntegerField(default=0)
    last_visit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.source.name

    class Meta:
        verbose_name_plural = 'Traffic'
        ordering = ['-last_visit']

class SiteHit(models.Model):
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip_address

    class Meta:
        verbose_name = 'Site Hit'
        verbose_name_plural = 'Site Hits'
        ordering = ['-timestamp']
