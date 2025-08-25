from django.db import models
import datetime
from django.utils import timezone



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        # これは_str_メゾットのオーバーライドらしい
        #print(obj)としたときもobj.__str__()をオーバーライド
        return self.question_text
    def was_published_recently(self):
                return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
"""
Question クラスの中で objects を定義していないのに、Question.objects で
データベース操作ができるのは Django が自動的に「マネージャ (Manager)」
を追加しているから
models.Model を継承したクラスを定義すると、Django は内部的にそのクラスに対して
「メタ情報」や「データベースとやり取りする仕組み」を付け加える
"""

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

# Create your models here.
