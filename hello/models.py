from django.db import models

class Member(models.Model):
    name = models.CharField(verbose_name="名前", max_length=25)
    age = models.IntegerField(verbose_name="年齢")
    choices = (("0","女"),("1","男"))
    sex = models.CharField(verbose_name="性別", max_length=5, choices=choices)

    def __str__(self):
        if self.sex=="0":
            sex_data = "女"
        else:
            sex_data = "男"
        return "名前:" + self.name + " 年齢:" + str(self.age) + "歳 性別:" + sex_data + "性"