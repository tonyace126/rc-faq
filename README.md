# RC 集點平台 客服查詢中心

給 SugarFun 客服團隊用的「常見問題 + 平台頁面流程」查詢網頁。
平台寄生在 LIFF（LINE）框架下，本網頁集中管理會員操作上常見的客服問題與平台各畫面參考。

---

## 兩大功能

**📋 QA 查詢分頁**
集中管理會員常見問題（發票、曬寵、點數、健檢等）。每筆 QA 包含問題描述、根因、客服處理 SOP、可一鍵複製的回覆話術、相關截圖。

**📱 平台頁面流程分頁**
集中管理 LIFF 平台各畫面截圖，依「會員會走的路徑」組織成一條條流程。客服收到會員截圖時可快速比對找出在哪一頁、該頁應該長什麼樣。
- **流程模式**：左側流程清單 + 右側逐步畫面（適合走完整流程或新人 onboarding）
- **圖庫模式**：所有畫面以網格呈現，適合快速搜尋畫面
- 每張畫面可掛「相關 QA」連結，點下去直接跳到 QA 分頁

---

## 檔案結構

```
rc-faq/
├── index.html              ← 客服查詢頁（給客服連結用這個）
├── admin.html              ← 編輯工具（給 TONY 用）
├── data/
│   ├── faqs.json           ← QA 內容
│   └── screens.json        ← 平台流程內容
├── images/
│   └── screens/            ← 平台流程截圖
├── .nojekyll
├── .gitignore
└── README.md
```

---

## Part 1：第一次上線（建 GitHub Pages）

### 推薦：用 GitHub 網頁版（不用裝任何東西）

1. 到 https://github.com/new 建 `rc-faq` repo（**Public**，不要勾任何 Add files）
2. 進入剛建好的 repo，點藍字「**uploading an existing file**」連結
3. 把整個 `rc-faq` 資料夾的內容**全選拖進**上傳框
4. 下方填 commit 訊息（例如 `init: 客服查詢中心 v2`），按 **Commit changes**
5. 進 **Settings** → **Pages**：Source 選 `Deploy from a branch`，Branch 選 `main` / `(root)`，Save
6. 等 1–2 分鐘，重新整理那頁，最上面會出現你的網址（類似 `https://<帳號>.github.io/rc-faq/`）

把這個網址傳給客服當書籤。

> ⚠️ 不能直接雙擊 `index.html` 開啟，瀏覽器會擋 fetch JSON。一定要用 GitHub Pages 或本機 server。

### 備選：用 Git 指令（需先裝 Xcode Command Line Tools）

```bash
cd "/Volumes/Tony-X9 Pro/claude/RC集點平台/rc-faq"
git init
git add .
git commit -m "init: 客服查詢中心"
git branch -M main
git remote add origin https://github.com/<你的帳號>/rc-faq.git
git push -u origin main
```

---

## Part 2：日常維護

### 加 / 改 QA

**做法 A（推薦）：用 admin.html**

1. 開啟 `https://<帳號>.github.io/rc-faq/admin.html`
2. 上方分頁選「📋 編輯 QA」
3. 點「📂 載入 faqs.json」（或頁面已自動載入）
4. 編輯 / 新增
5. 點右上「⬇️ 下載目前分頁的 JSON」拿到新 `faqs.json`
6. 到 GitHub repo > `data/faqs.json` > ✏️ > 把整份貼掉、Commit changes

**做法 B：直接編 `data/faqs.json`**
進 GitHub repo > 點 `data/faqs.json` > 鉛筆 ✏️ > 編輯 → Commit。
注意逗號跟引號別亂掉，否則整個網頁會壞掉。

### 加 / 改平台流程

跟 QA 流程一樣，只是分頁切到「📱 編輯平台流程」、檔案是 `data/screens.json`。

每條流程含多個步驟，每步可填截圖路徑（`images/screens/xxx.jpg`）跟相關 QA ID。

### 加截圖

1. 進 GitHub repo > 點 `images` 資料夾
2. 上 **Add file → Upload files**
3. 拖檔案進去（建議命名規則：`<分類>-<編號>.jpg`，例如 `invoice-valid-formats.jpg`）
4. Commit changes
5. 在 admin.html 或 JSON 裡填路徑：`images/INV-001-a.png`（QA 用）或 `images/screens/contact-01-menu.jpg`（流程用）

> 截圖通常放在 `images/screens/`（流程畫面），但 QA 自己的補充圖可以直接放在 `images/`。

---

## 資料格式

### faqs.json 欄位

| 欄位 | 說明 | 必填 |
|------|------|------|
| `id` | 唯一識別碼，建議 `INV-001`、`PTS-002` | ✓ |
| `category` | 分類 ID | ✓ |
| `title` | 問題標題 | ✓ |
| `memberSymptom` | 會員端會怎麼描述 | |
| `rootCause` | 真正原因 | |
| `csSteps` | 客服處理步驟陣列 | |
| `replyTemplate` | 給客服直接複製的話術 | |
| `tags` | 搜尋用標籤 | |
| `images` | 截圖路徑陣列 | |
| `updated` | `YYYY-MM-DD` | |

### screens.json 欄位

| 欄位 | 說明 |
|------|------|
| `flows[].id` | 流程 ID，建議 `FLOW-XXX` |
| `flows[].category` | 分類 ID（service / invoice / campaign / platform / backend） |
| `flows[].name` | 流程名稱 |
| `flows[].description` | 流程整體說明 |
| `flows[].steps[]` | 步驟陣列 |
| `flows[].steps[].title` | 步驟標題 |
| `flows[].steps[].description` | 步驟說明 |
| `flows[].steps[].image` | 截圖路徑 |
| `flows[].steps[].relatedFaqs` | 相關 QA ID 陣列 |

---

## 本機測試

不想每次都 push 才看效果？在終端機用：

```bash
cd "/Volumes/Tony-X9 Pro/claude/RC集點平台/rc-faq"
python3 -m http.server 8000
```

打開 http://localhost:8000 就能本機測試。

---

## 常見問題

**Q：載入失敗 / 空白頁？**
A：90% 是 JSON 語法錯誤（多/少逗號、引號）。打開瀏覽器 F12 看 Console。或用 admin.html 編輯 + 下載功能避免手刻 JSON。

**Q：圖片沒出現？**
A：檢查 JSON 裡的路徑跟 `images/` 裡的檔名是否一致（大小寫敏感）、副檔名 `.jpg` vs `.jpeg` vs `.png` 是否正確。

**Q：repo 一定要 Public 嗎？**
A：用 GitHub Pages 免費版的話，是。Private 需要 GitHub Pro。

**Q：客服需要 GitHub 帳號嗎？**
A：不需要，他們只要打開那個網址就能查。
