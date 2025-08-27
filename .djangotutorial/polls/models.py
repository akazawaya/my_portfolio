from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin


class Question(models.Model):
    # XXXFieldというのはDBでのカラム、列を意味する！！！
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    # pub_date は変数として、 Question(pub_date=timezone.now())のように呼ぶ
    def __str__(self):
        # これは_str_メゾットのオーバーライドらしい
        #print(obj)としたときもobj.__str__()をオーバーライド
        return self.question_text
    
    @admin.display(
        boolean=True,       # True/False をアイコン（✔/✘）で表示
        ordering="pub_date",# 一覧でこの列をソートすると pub_date を基準にする
        description="Published recently?", # 管理画面の列見出し
    )
    #デコレータは直後の関数 or クラスを引数に取って加工して返す
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    # この場合 was_published_recently = admin.display(...)(was_published_recently)
    #デコレータがすでにdecorator(func)で関数を受け取れるように制御されている
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
