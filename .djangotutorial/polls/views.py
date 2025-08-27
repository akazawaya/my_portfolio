from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
# レンダラーは、HttpResponse テンプレートを処理して最終的なレスポンスに変換する仕組み（バックエンド） 
# 引数はrequest(現在処理している HttpRequest)とtemplateのアドレス名
#　request（HttpRequest オブジェクト）は　なんか色々な情報の塊らしい（request.method、くっきーなど）
# 第三引数はテンプレートに渡す辞書データで、{{ latest_question_list }} のように参照される
from .models import Choice, Question
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    #DetailView では model = Question と書くだけで内部的に 
    # queryset = Question.objects.all() と同等になる
    # models.Model を継承したクラスには、Djangoが自動で objects という Manager を付けます。
    # Manager は DB への窓口で、all() / filter() / get() / create() などのQuerySet操作を生むメソッドを持ちます
    template_name = "polls/detail.html"
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))