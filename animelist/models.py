from django.db import models


class Subscriber(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return "Пользователь %s %s" % (self.email, self.password)

    class Meta:
        verbose_name = 'MySubscriber'
        verbose_name_plural = 'A lot of Subscribers'
