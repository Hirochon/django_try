from django.contrib.auth import get_user_model
from django.db import models

class Article(models.Model):
    """記事投稿"""

    class Meta:
        db_table = 'article'

    author = ForeignKey(get_user_model(), on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=50)
    text = models.TextField(verbose_name='テキスト')
    time = models.DateTimeField(verbose_name='作成日時', default=timezone.now)

    def __str__(self):
        return self.title