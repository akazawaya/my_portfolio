from django.contrib import admin
from .models import Choice, Question

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):   
    model = Choice
    extra = 3

# ChoiceオブジェクトはQuestion管理ページで編集されます。
# デフォルトでは、3つの選択肢に対応できるフィールドを用意してください。
class QuestionAdmin(admin.ModelAdmin):
    #fields = ["pub_date", "question_text"]
    fieldsets = [
    (None, {"fields": ["question_text"]}),
    ("Date information", {
        "fields": ["pub_date"], 
        "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
#　並び順を変えられるらしい