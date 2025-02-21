# zen-study
N予備校のデータを効率良く型安全にプログラムから取得するモジュール

## インストール方法
```bash
pip install zen_study@git+https://github.com/Lqm1/zen-study.git
```

## 使い方
```python
from zen_study import zen_study

zen_study = zen_study()

user = zen_study.login_by_s_high_school(input('学籍番号: '), input('パスード: '))
csrf_token = zen_study.create_csrf_token()
user = zen_study.get_user()
notices = zen_study.get_notices()
notices = zen_study.get_notices(unread=False)
marked_as_read_notice = zen_study.mark_as_read_notice(notice_id=1)
material_courses = zen_study.get_material_courses(ids=[1])
material_chapters = zen_study.get_material_chapters(queries={1: 1})
material_recommendations = zen_study.get_meterial_recommendations()
material_course = zen_study.get_material_course(1)
material_chapter = zen_study.get_material_chapter(1, 1)
services = zen_study.get_my_courses()
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
