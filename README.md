# NYobikou
N予備校のデータを効率良く型安全にプログラムから取得するモジュール

## インストール方法
```bash
pip install n_yobikou@git+https://github.com/c7e715d1b04b17683718fb1e8944cc28/NYobikou.git
```

## 使い方
```python
from n_yobikou import NYobikou

n_yobikou = NYobikou()

user = n_yobikou.login_by_s_high_school(input('学籍番号: '), input('パスード: '))
csrf_token = n_yobikou.create_csrf_token()
user = n_yobikou.get_user()
notices = n_yobikou.get_notices()
notices = n_yobikou.get_notices(unread=False)
marked_as_read_notice = n_yobikou.mark_as_read_notice(notice_id=1)
material_courses = n_yobikou.get_material_courses(ids=[1])
material_chapters = n_yobikou.get_material_chapters(queries={1: 1})
material_recommendations = n_yobikou.get_meterial_recommendations()
material_course = n_yobikou.get_material_course(1)
material_chapter = n_yobikou.get_material_chapter(1, 1)
services = n_yobikou.get_my_courses()
```

## 貢献方法
このプロジェクトに貢献する方法は以下の通りです：

1. プロジェクトのリポジトリをフォークします。
2. ローカル環境にリポジトリをクローンします。
3. 新しい機能や修正を行うためのブランチを作成します。
4. コードの変更を行います。
5. 変更内容をコミットし、プッシュします。
6. プッシュしたブランチからオリジナルのリポジトリにプルリクエストを作成します。
7. レビュワーからのフィードバックを受けて、必要な修正を行います。
8. レビュワーが承認したら、プルリクエストをマージします。

プロジェクトに貢献する際は、コードの品質を保つためにテストを実行し、ドキュメントを更新することもお勧めします。また、他の貢献者とコミュニケーションを取りながら作業を進めることも重要です。

詳細な貢献ガイドラインやプロジェクトの方針については、プロジェクトのリポジトリのドキュメントを参照してください。

ご質問や疑問がある場合は、プロジェクトの連絡先にお問い合わせください。

## 免責事項
このモジュールはN予備校のデータを取得するための非公式のツールです。使用する際は自己責任でお願いします。モジュールの使用によって生じたいかなる損害や問題についても、開発者は一切の責任を負いません。

## 連絡先
info@lami.zip
