from djongo import models


class List(models.Model):
    pass


class Item(models.Model):
    list = models.ForeignKey(
        List,
        on_delete=models.CASCADE,
        null=True)
    text = models.TextField(default='')
