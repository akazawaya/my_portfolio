from django.shortcuts import render

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


