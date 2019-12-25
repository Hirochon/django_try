from django.db import models

class Favorite(models.Model):
    """ファボ"""

    class Meta:
        db_table = 'favorite'

    photo = models.ImageField(verbose_name='フォト', blank=True, null=True, upload_to = 'images/')