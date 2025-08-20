from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm

form sample_app.models import Post

# この中にView（処理の定義）をすべて実装する
"""
create_post「作成」
 ページロード時にはPostオブジェクトによりフォームを生成、実行ボタン押下時にはフォームに入力された値から、Postオブジェクトを生成。
read_post「一覧表示」
　データベースから全データを所得し、そのままtemplateへ渡す。
edit_post「編集」
　引数で渡されたidにより、Post オブジェクトを取得し、フォームを生成。
delete_post「削除」
　引数で渡されたidにより、Post オブジェクトを取得し、オブジェクトを削除。
"""

def create_post():
    post = Post()
    if requesr.method == 'GET':
        form = PostForm(instance=post)
        return render(request,'sample_app/post_form.html',
                {'form':form})
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            # チェック結果に問題なければデータを作成する
            post = form.save(commit=False)
            post.save()

        return redirect('sample_app:read_post')


def read_post(request):
    posts = Post.objects.all().order_by('id')
    return render(request,
                  'sample_app/post_list.html',
                  {'posts':posts})

def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'GET':
        form = PostForm(instance=post)
        return render(request,
                      'sample_app/post_form/html',
                      {'form':form, 'post_id':post_id})
    
    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.isvalid():
            post = form.save(commit=False)
            post.save()
        return redirect('sample_app:read_post')
    
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('sample_app:read_post')


class PostForm(ModelForm):
    class Meta:
        model = Post
        # fields は models.py で定義している変数名
        fields = ('name', 'micropost')