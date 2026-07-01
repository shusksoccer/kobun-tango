# 古文単語帳（辞典＋暗記テスト）— 引き継ぎ資料

高校生・受験生向けの古文単語学習サイト。**辞典ページ**と**暗記テストページ**の2枚を、ソース（Excel＋解説Markdown）から静的HTMLとして生成する。全330語。出力はオフラインで開ける単一HTML（データ埋め込み）。

## ドキュメント一覧

| ファイル | 内容 |
|---|---|
| `README.md`（本書） | 概要・構成・クイックスタート |
| `docs/ARCHITECTURE.md` | ビルドパイプライン、各ファイルの責務 |
| `docs/DATA_SCHEMA.md` | 中間データ `data_payload.json` の構造（全フィールド） |
| `docs/TAGGING.md` | タグ分類体系、意味の統合・終止形化ロジック、関連語の作り方 |
| `docs/FEATURES.md` | 辞典／テストのUI仕様（機能の挙動） |
| `docs/DATA_NOTES.md` | ソースデータの仕様・修正履歴・既知の注意点 |
| `docs/NEXT_STEPS.md` | 未対応・改善候補のバックログ |

## ディレクトリ構成

```
kobun-app/
├─ build.py            # ソース → build/data_payload.json（解析・タグ付け・意味統合・終止形化）
├─ build_site.py       # data_payload.json → dist/index.html, dist/quiz.html（HTML生成）
├─ data/
│  ├─ kobun-words.xlsx # 元データ（シート名 'リストa'、ヘッダは2行目＝header=1）
│  └─ explanations.md  # 各語の解説（「{番号} {見出し}（漢字） — {解説}」形式、330行）
├─ build/
│  └─ data_payload.json# 中間生成物（build.py の出力 / build_site.py の入力）
├─ dist/
│  ├─ index.html       # 辞典（生成物）
│  └─ quiz.html        # 暗記テスト（生成物）
├─ test/
│  └─ test.js          # jsdom スモークテスト
└─ docs/               # 上記ドキュメント
```

## クイックスタート

依存（Python 3.10+ / Node 18+）:

```bash
pip install pandas openpyxl fugashi unidic-lite
```

ビルド（必ず build.py → build_site.py の順）:

```bash
python3 build.py        # data/ を読み build/data_payload.json を生成
python3 build_site.py   # data_payload.json から dist/index.html, dist/quiz.html を生成
```

テスト:

```bash
npm install jsdom       # 初回のみ
node test/test.js       # dist/*.html に対するスモークテスト（17項目）
```

利用: `dist/index.html` をブラウザで開く。**`index.html` と `quiz.html` は同じフォルダに置くこと**（テスト⇄辞典のジャンプとリンクが相対パスで動く）。「覚えた」状態は `localStorage` のキー `koten_known` を両ページで共有。

## 重要な前提（先に知っておくこと）

- **意味（meanings）と例文の解答（example.imi）は別物**。意味一覧は統合・終止形化した「言い切り」、例文の解答は各例文に合う活用形のまま。詳細は `docs/TAGGING.md` / `docs/DATA_SCHEMA.md`。
- ソースを差し替えたら **build.py から再実行**。番号（no）が全ての対応キー（解説・関連語・テーマ等）。
- `build_site.py` は HTML/CSS/JS をPythonの文字列として持つ。**JSの `{}` と衝突するため f-string は使わず** `%プレースホルダ%` の `.replace()` で組み立てている。編集時は注意。
- 生成HTMLはデータを丸ごと内蔵するため各約1MB。`localStorage` は try/catch でガード済み（ローカルでは保存、制限環境では無視）。
