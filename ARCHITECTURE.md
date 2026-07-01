# アーキテクチャ

## パイプライン

```
data/kobun-words.xlsx ─┐
                       ├─[ build.py ]─→ build/data_payload.json ─[ build_site.py ]─→ dist/index.html
data/explanations.md ──┘                                                          └─→ dist/quiz.html
```

2段構成。**build.py がデータ加工の全責務**を持ち、**build_site.py は表示（HTML/CSS/JS）の全責務**を持つ。ロジックとビューが分離しているので、タグ規則を変えるなら build.py、見た目や操作を変えるなら build_site.py を触る。

## build.py の責務（順に実行）

1. **Excel 読み込み**: シート `リストa`、`header=1`（2行目がヘッダ）。各行が「単語の1つの例文＋その解答」。列は `no, word, pos, keigo, imi, ko, koBlank, yk, ykBlank` を使用（11列目以降の第2テーブルは未使用・空）。
2. **クリーニング**: 意味 `imi` から `〔〕`・空白除去。例文 `ko` から末尾の出典 `（…）` を分離。訳 `yk` の先頭「（訳）」除去。
3. **下線位置の算出** `ko_underline()`: 例文（`ko`）と空欄版（`koBlank`）の差分から「空欄になっている語」を特定し、`\x01…\x02` で囲んだ文字列 `koU` を作る（順方向テストの下線用）。差分が取れない行はフォールバックで無印。
4. **意味の統合＋終止形化**（→ `docs/TAGGING.md` 詳細）: 例文ごとの解答を「同一語の活用違い・重複」だけクラスタリングし、代表ラベルを fugashi で終止形化、重複ラベルを統合。各例文に統合後の意味番号 `mi` を付与。
5. **重要度・敬語種別・テーマ・覚え方フラグ**の付与（番号ベースのルール＋自動判定）。
6. **関連語**（類義・対義・混同）を番号ベースのクラスタから生成（訳ごとの `sense` 付き、対称化）。
7. **解説の取り込み**: `explanations.md` を番号で突き合わせ、`note`（本文）と `kanji`（見出しの漢字）を付与。
8. **出力**: `build/data_payload.json`（`{words:[...], meta:{...}}`）。

## build_site.py の責務

- `data_payload.json` を読み、HTMLを2枚生成。
- 共通部品: `HEAD`（フォント・`<style>`・データ埋め込み `const DB=...`）、`COLORS`（色マップ＋ `esc`/`blankify`/`koUnder` 等のJSヘルパ）、`CSS`。
- `INDEX_BODY`（辞典）/`QUIZ_BODY`（テスト）に各ページのDOMとロジック。
- `build(title, body)` が `HEAD + body` を連結。**`%TITLE%`/`%CSS%`/`%DATA%`/`%COLORS%` を `.replace()` で差し込む**（f-string不使用：JSの波括弧と衝突するため）。
- データは各HTMLに**インライン埋め込み**（外部 `data.js` にしない）。理由: 単一ファイルでオフライン動作・プレビュー安定・配布が容易。その代償でファイルは各約1MB。

## ページ間連携

- テストの答え合わせ → `index.html#w{no}` で辞典の該当カードへジャンプ（`hashchange` で該当カードを中央表示＋ハイライト）。
- 「覚えた」は `localStorage['koten_known']`（番号の配列）を両ページで共有。辞典のチェックとテストの「覚えた」が同期。
- 同一フォルダ配置が前提（相対リンク）。

## ビルド再現の注意

- 文字コードは全て UTF-8。
- fugashi/unidic-lite 未導入でも build.py は動く（`lemmatize` が恒等関数にフォールバックし、意味は活用形のまま＝終止形化だけスキップ）。終止形化を効かせるには両方をインストールすること。
