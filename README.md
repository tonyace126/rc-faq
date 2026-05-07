# RC 集點平台 客服 QA 查詢

給 SugarFun 客服團隊用的常見問題查詢網頁。
平台寄生在 LIFF（LINE）框架下，本網頁集中管理會員操作上常見的客服問題。

---

## 檔案結構

```
rc-faq/
├── index.html       ← 客服查詢頁（給客服連結用這個）
├── admin.html       ← QA 編輯工具（給 TONY 用）
├── data/
│   └── faqs.json    ← 所有 QA 內容
├── images/          ← 截圖
├── .nojekyll        ← 告訴 GitHub Pages 不要做 Jekyll 處理
└── README.md
```

---

## Part 1：第一次上線（建 GitHub Pages）

### 1. 建一個 GitHub repo

到 https://github.com/new 建立 repo：
- **Repository name**：`rc-faq`（隨意，但會出現在網址裡）
- **Public**：選 Public（因為 GitHub Pages 免費版只支援 Public repo）
- **不要勾** Add README
- 按「Create repository」

### 2. 把這個資料夾 push 上去

打開 Mac 的「終端機」（Terminal），輸入：

```bash
cd "/Volumes/Tony-X9 Pro/claude/RC集點平台/rc-faq"
git init
git add .
git commit -m "init: 客服 QA 第一版"
git branch -M main
git remote add origin https://github.com/<你的帳號>/rc-faq.git
git push -u origin main
```

把 `<你的帳號>` 換成你自己的 GitHub 帳號名稱。

> 第一次推上去如果跳出登入要求，照指示輸入帳號 / Personal Access Token 即可。
> 如果不熟 Git，也可以直接在 GitHub 網頁上點「Add file > Upload files」把整個資料夾拖上去。

### 3. 開啟 GitHub Pages

進入 repo > **Settings** > 左側選單 **Pages**：

- **Source**：選 `Deploy from a branch`
- **Branch**：選 `main` / `(root)`
- 點 Save

等 1–2 分鐘，Pages 會給你一個網址，例如：

```
https://<你的帳號>.github.io/rc-faq/
```

把這個網址傳給客服，他們把它加到瀏覽器書籤就可以用了。

---

## Part 2：日常維護（新增 / 修改 QA）

有兩種做法，挑一個你習慣的就好。

### 做法 A（推薦給非工程同仁）：用 admin.html 編輯

1. 打開 `admin.html`（雙擊也行，但建議部署到 GitHub Pages 後用 `.../admin.html` 開）
2. 點上方「📂 載入 faqs.json」載入現有 QA
3. 編輯或新增
4. 點「⬇️ 下載 faqs.json」下載新版檔案
5. 把下載的 `faqs.json` 蓋掉 GitHub repo 裡 `data/faqs.json`
6. （如果有新截圖）把圖檔上傳到 `images/` 資料夾
7. Commit + Push

GitHub 網頁上傳檔案的做法：
- 進 repo > 點 `data/faqs.json` > 右上鉛筆 ✏️ > 把整份貼進去 > 下方 Commit changes
- 或：進 repo > Add file > Upload files > 拖檔案進去 > Commit changes

### 做法 B：直接編 JSON

打開 `data/faqs.json`，依照範例新增一筆：

```json
{
  "id": "PTS-002",
  "category": "points",
  "title": "點數兌換時跳出系統錯誤",
  "tags": ["點數", "錯誤", "系統"],
  "memberSymptom": "我點兌換出現紅色錯誤訊息",
  "rootCause": "活動已結束或庫存售罄",
  "csSteps": [
    "請會員提供錯誤訊息截圖",
    "至漸強後台確認當下會員的點數",
    "若是活動結束，向會員說明"
  ],
  "replyTemplate": "您好，請問可以提供錯誤訊息的截圖嗎？...",
  "images": ["images/PTS-002-a.png"],
  "updated": "2026-05-08"
}
```

存檔、push 上 GitHub，1 分鐘內 Pages 就會更新。

---

## QA 欄位說明

| 欄位 | 說明 | 必填 |
|------|------|------|
| `id` | 唯一識別碼，建議格式 `INV-001`、`PTS-002` | ✓ |
| `category` | 分類 ID（見下方 categories） | ✓ |
| `title` | 問題標題（會顯示在卡片上） | ✓ |
| `memberSymptom` | 會員端會怎麼描述這個問題 | |
| `rootCause` | 問題的真正原因 | |
| `csSteps` | 客服處理步驟（陣列，每個元素是一步） | |
| `replyTemplate` | 給客服直接複製貼到 LINE 的話術 | |
| `tags` | 搜尋用的關鍵字標籤 | |
| `images` | 截圖路徑陣列（相對於 repo 根目錄） | |
| `updated` | 最後更新日期 `YYYY-MM-DD` | |

### 預設分類

| ID | 名稱 |
|----|------|
| `invoice` | 登錄發票 |
| `pet` | 曬寵打卡 |
| `points` | 點數兌換 |
| `health` | 健檢券兌換 |
| `member` | 會員 / 帳號 |
| `campaign` | 活動 / 給點訊息 |
| `product` | 產品相關 |
| `other` | 其他 |

要新增分類就到 `faqs.json` 的 `categories` 陣列加一筆即可。

---

## 截圖怎麼放

1. 把截圖檔丟到 `images/` 資料夾，建議命名為 `<QA-ID>-a.png`、`<QA-ID>-b.png`，例如 `INV-001-a.png`
2. 在那筆 QA 的 `"images"` 陣列填路徑：`["images/INV-001-a.png"]`
3. Push 到 GitHub，網頁就會顯示

主頁點圖會放大瀏覽，方便客服比對會員傳來的截圖。

---

## 本機測試

不想每次都 push 才看效果？在終端機用：

```bash
cd "/Volumes/Tony-X9 Pro/claude/RC集點平台/rc-faq"
python3 -m http.server 8000
```

打開瀏覽器到 http://localhost:8000 就能本機測試。

> ⚠️ 不能直接雙擊 `index.html` 開啟，瀏覽器會擋 `fetch('data/faqs.json')`。一定要用 http server 或部署後的 GitHub Pages 開。

---

## 常見問題

**Q：我的 repo 一定要 Public 嗎？**
A：用 GitHub Pages 免費版的話，是。如果要 Private repo + 公開頁面，需要 GitHub Pro 或 Team 方案。

**Q：客服需要 GitHub 帳號嗎？**
A：不需要，他們只要打開那個網址就能查。

**Q：我可以自訂網址嗎？**
A：可以，在 repo Settings > Pages 設定 Custom domain，需要你有自己的網域。

**Q：誰可以編輯 QA？**
A：只有有 repo 寫入權限的人。可以到 repo Settings > Collaborators 加同事。
