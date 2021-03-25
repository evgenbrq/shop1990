from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return "Товар %s цена %s" % (self.name, self.price)

    class Meta:
        verbose_name = "Прайс"
        verbose_name_plural = "Прайсы"

        