from django.conf import settings
from django.db import models


class Idea(models.Model):
    title = models.CharField(max_length=200, help_text="아이디어명")
    image = models.ImageField(
        upload_to="idea_site_image/%Y/%m/%d/", help_text="대표 사진"
    )
    content = models.TextField(help_text="아이디어 설명")
    interest = models.IntegerField(help_text="아이디어 관심도")
    devtool = models.ForeignKey(devtool, on_delete=models.CASCADE, related_name="idea", help_text="예상 개발툴")

    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Devtool(models.Model):
    name = models.CharField(max_length=200, help_text="이름")
    kind = models.CharField(max_length=200, help_text="종류")
    desc = models.TextField(help_text="개발툴 설명")

    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name