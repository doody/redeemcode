from django.db import models


class RedeemObject(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class User(models.Model):
    email = models.EmailField()
    redeemed_objects = models.ManyToManyField(RedeemObject, null=True, blank=True)


class RedeemCode(models.Model):
    code = models.CharField(max_length=8, unique=True)
    createTime = models.DateTimeField(auto_now_add=True)
    isValid = models.BooleanField(default=True)
    user = models.ForeignKey(User)