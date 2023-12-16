from django.db import models

class YapayZekaSonuc(models.Model):
    isim = models.CharField(max_length=100)
    sonuc = models.FloatField()
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.isim} - {self.sonuc}"
