# CLAUDE.md

Guidance for AI assistants (and humans) working in this repository.

## What this is

**RC 集點平台 客服查詢中心** — an internal reference site for the SugarFun
customer-service team supporting the Royal Canin (法國皇家) points platform,
which lives inside a LINE LIFF app. It is **not** the platform itself; it is a
static lookup/cheat-sheet site that centralizes:

1. **QA 查詢 (FAQ lookup)** — common member problems with root cause, CS handling
   SOP, one-click copyable reply scripts (話術), and reference screenshots.
2. **平台頁面流程 (platform screen flows)** — screenshots of each LIFF screen
   organized into the paths a member walks, so CS can match a member's
   screenshot to "which page is this and what should it look like".

Almost all content is in **Traditional Chinese (zh-Hant)**. Preserve the
language and tone of existing content when editing.

## Tech stack & architecture

- **Pure static site. No build step, no framework, no dependencies, no
  `package.json`, no Node/npm.** Just hand-written HTML + inline CSS + vanilla JS.
- Deployed via **GitHub Pages** (`Deploy from a branch`, `main` / root).
  `.nojekyll` disables Jekyll processing.
- Content lives in two JSON files under `data/`; the HTML pages `fetch()` them at
  runtime. Editing content = editing JSON + images, never touching HTML.

### Files

```
rc-faq/
├── index.html        ← Customer-facing viewer (the link CS bookmarks). Password-gated.
├── admin.html        ← Editor tool (for the maintainer, TONY). Edits JSON & pushes to GitHub.
├── data/
│   ├── faqs.json     ← FAQ content + site meta (title, quick links, events, tracker form)
│   └── screens.json  ← Platform screen-flow content
├── images/
│   └── screens/      ← Platform flow screenshots (.jpg / .png)
├── .nojekyll         ← Tell GitHub Pages to serve files as-is
├── robots.txt        ← Disallow all crawlers (internal tool)
└── README.md         ← End-user/maintainer guide (Chinese)
```

Note: `images/` may also hold ad-hoc FAQ supplement images directly (not only
`images/screens/`). README mentions a `.gitignore` but none currently exists.

### index.html (viewer)

- Two tabs: **QA** (`#panel-qa`) and **平台流程** (`#panel-flows`). The flows tab
  has two modes: 流程 (flow) and 圖庫 (library/grid).
- Loads both JSON files in parallel via `Promise.all`, with a `?_=Date.now()`
  cache-buster. On failure it shows a "載入失敗" message hinting the page must be
  served over `http(s)://`, not `file://`.
- Deep-linking via URL hash (`handleHash` / `hashchange`): e.g. tab selection,
  jumping to a specific FAQ, `#event`/`#events`.
- Keyboard: `/` focuses the active search box; lightbox supports `Esc` / arrow
  keys / swipe.
- Renders from `FAQS.meta`: `siteTitle`, `lastUpdated`, `quickLinks`
  (primary + events bars), `events` (campaign cards), `trackerFormUrl` /
  `trackerFormLabel` (floating "問題追蹤申報" button).
- **Password gate**: an early inline script in `<head>` adds `html.locked` unless
  `localStorage['rcfaq-auth-v1']` equals a hard-coded SHA-256 `HASH`. A second
  script verifies typed input via `sha256()` and stores the hash on success. The
  password itself is not in the repo — only its hash. To change the password,
  update the `HASH` constant in **both** places it appears in `index.html`.

### admin.html (editor)

- Client-side editor for `faqs.json` and `screens.json`. Can **load** JSON (auto
  via fetch, or manual file picker), edit through forms, **export/download** the
  JSON, or **push directly to GitHub**.
- GitHub push uses the GitHub Contents API with a Personal Access Token. Settings
  (owner / repo / branch / token) are stored only in `localStorage`
  (key around `LS_KEY`), never committed. `pushFile()` does a GET (to obtain the
  blob `sha`) then a PUT to update the file.
- ID helpers: `nextId(list, prefix)` and `today()` for new entries.

## Data format

### faqs.json

- `meta`: `siteTitle`, `siteSubtitle`, `lastUpdated`, `trackerFormUrl`,
  `trackerFormLabel`, `quickLinks { primary[], events[] }`, `events[]`
  (campaign cards with `id`, `name`, dates, `summary`, `bannerImage`, `flowId`,
  `faqIds[]`).
- `categories[]`: `{ id, name, color }` (e.g. `invoice`, `pet`, `points`,
  `health`, `member`, `campaign`, `product`, `other`).
- `faqs[]`:

  | field | meaning | required |
  |-------|---------|----------|
  | `id` | unique, e.g. `INV-001`, `PTS-002` | ✓ |
  | `category` | category id | ✓ |
  | `title` | problem title | ✓ |
  | `memberSymptom` | how the member describes it | |
  | `rootCause` | actual cause | |
  | `csSteps` | array of CS handling steps | |
  | `replyTemplate` | copy-paste reply script | |
  | `tags` | search tags | |
  | `images` | array of image paths | |
  | `updated` | `YYYY-MM-DD` | |

### screens.json

- `meta`: `lastUpdated`, `note`.
- `categories[]`: `{ id, name, color }`. **Note:** the screens categories differ
  from the FAQ categories (e.g. `platform`, `pet`, `invoice`, `exchange`,
  `service`, `campaign`, `backend`) — keep the two sets independent.
- `flows[]`: `id` (e.g. `FLOW-XXX`), `category`, `name`, `description`,
  `steps[]`.
- `flows[].steps[]`: `title`, `description`, `image` (single) **or** `images[]`
  (multiple — `getStepImages()` supports both for backward compat),
  `relatedFaqs[]` (array of FAQ ids, which become links into the QA tab).

## ID & naming conventions

- FAQ ids: `<PREFIX>-NNN`, e.g. `INV-001` (invoice), `PTS-002` (points). Prefix
  loosely tracks the topic, not strictly the category id.
- Flow ids: `FLOW-...`, often descriptive (`FLOW-POINT-EXCHANGE`,
  `FLOW-INVOICE-BONUS-0518`).
- Images: `images/screens/<area>-<step>.jpg`, descriptive kebab-case
  (`contact-01-menu.jpg`, `exchange-step4-serial.png`). Both `.jpg` and `.png`
  exist; a few filenames contain Chinese characters. Paths are **case-sensitive**
  on GitHub Pages — match filenames exactly.

## Running locally

Must be served over HTTP — opening `index.html` via `file://` breaks the JSON
`fetch()`.

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

(For viewing past the gate locally, you need the password, or temporarily set
`localStorage['rcfaq-auth-v1']` to the hash in the console.)

## Editing workflow & conventions

- **Content changes go in `data/*.json` and `images/`, not in the HTML.** Reserve
  HTML edits for behavior/layout/style or the password hash.
- JSON must stay valid — a stray comma or quote breaks the whole page (shows
  blank / "載入失敗"). Prefer editing through `admin.html` to avoid hand-editing,
  or validate JSON before committing.
- When adding/updating content, bump the relevant `meta.lastUpdated`.
- When adding a screenshot, commit the file under `images/` (usually
  `images/screens/`) and reference its exact path in the JSON.
- Cross-references: FAQ `images` and flow `relatedFaqs`/`flowId` must point to ids
  / paths that actually exist.

## Git & commit conventions

- Commit messages are short and scoped, frequently prefixed by the affected id or
  type, in Chinese, e.g.:
  - `INV-107: 補資格說明`
  - `FLOW-POINT-EXCHANGE: 修正 Step2 自動入帳錯誤`
  - `feat: 加上 noindex 跟密碼門`
  - `update:` / `tweak:` for content tweaks and image swaps.
- Develop on the branch you were assigned; create it locally if missing. Do not
  push to `main` without explicit permission. Do not open a PR unless explicitly
  asked.

## Gotchas

- This is an **internal, deliberately non-public** tool: `robots.txt` disallows
  all, `index.html` has `noindex` meta tags and a password gate. Don't add it to
  search indexes or make it discoverable.
- No automated tests, linters, or CI. Verification = serve locally and eyeball, or
  validate JSON.
- The two JSON files have **separate** category lists — don't assume an FAQ
  category id is valid in screens (or vice versa).
- The README is written for a non-developer maintainer using the GitHub web UI;
  its absolute paths (e.g. `/Volumes/Tony-X9 Pro/...`) are the maintainer's local
  machine, not this environment.
