from django.db import models
# CharFieldとは文字列を保存するためのフィールド
# __str__(self) は特殊メソッド　オブジェクトを人間が読む文字列に変換

class Post(models.Model):
    name = models.CharField(max_length=100)
    micropost = models.CharField(max_length=140, blank=True)
    
    def __str__(self):
        return self.name