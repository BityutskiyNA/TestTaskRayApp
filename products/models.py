from django.db import models


class DateTimeMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Images(DateTimeMixin):
    link = models.CharField(max_length=1000)


class Product(DateTimeMixin):
    type = [
        ("foods", "foods"),
        ("dishes", "dishes"),
        ("clothing", "clothing"),
    ]
    name = models.CharField(max_length=500)
    article = models.CharField(max_length=10, default='')
    description = models.CharField(max_length=5000)
    image = models.ForeignKey(Images, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=50, choices=type)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name
