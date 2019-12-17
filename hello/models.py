from django.db import models

class Member(models.Model):
    name = models.CharField(verbose_name="名前", max_length=25)
    age = models.IntegerField(verbose_name="年齢")
    choices = (("0","女"),("1","男"))
    sex = models.CharField(verbose_name="性別", max_length=5, choices=choices)

    def __str__(self):
        return self.name

class Group(models.Model):
    member = models.ForeignKey(Member, verbose_name="名前", on_delete=models.CASCADE)
    choices = ((0,"乃木坂46"),(1,"日向坂46"),(2,"キモオタ"))
    name = models.IntegerField(verbose_name="グループ名", choices=choices)

    def __str__(self):
        if self.name == 0:
            group_name = "乃木坂46"
        elif self.name == 1:
            group_name = "日向坂46"
        else:
            group_name = "キモオタ"
        return str(self.member) + "(" + group_name + ")"