# -*- coding: utf-8 -*-
"""套用「會員平台活動」tab 改名 + 活動說明結構化區塊 到 index.html。
用法：python3 _apply_event_ui.py <index.html 路徑>
單一真相來源：同一支轉換同時套用到工作區檔與隔離用的 HEAD 版檔，
確保兩邊改動一致，且不夾帶 petfair 未 commit 的內容。
冪等：若已套用（偵測到 renderDetailSections）則只做無害的重複替換。
只印 ASCII 狀態。"""
import sys

path = sys.argv[1]
with open(path, encoding="utf-8") as f:
    s = f.read()

orig = s
errors = []


def rep(old, new, key, required=True):
    global s
    if old not in s:
        if required and new not in s:  # 若新內容也不在，才算真的漏
            errors.append(key)
        return
    s = s.replace(old, new, 1)


# R1 tab 改名
rep(
    '<button class="tab" data-tab="event" id="tab-event" hidden>\U0001f3ab 發票加碼活動</button>',
    '<button class="tab" data-tab="event" id="tab-event" hidden>\U0001f3ab 會員平台活動</button>',
    "R1-tab-rename",
)

# R2 isOpen：active + upcoming 皆展開，只有 expired 收合
rep(
    "    const isOpen = (status === 'active');",
    "    const isOpen = (status !== 'expired');",
    "R2-isOpen",
)

# R3 header 摘要改用 tagline 優先
rep(
    '          <p class="event-summary-text">${escapeHtml(e.summary || \'\')}</p>',
    '          <p class="event-summary-text">${escapeHtml(e.tagline || e.summary || \'\')}</p>',
    "R3-header-tagline",
)

# R4 body 加入 detailHtml
rep(
    """      <div class="event-card-body">
        ${flowHtml}
        ${faqsHtml}
      </div>""",
    """      <div class="event-card-body">
        ${detailHtml}
        ${flowHtml}
        ${faqsHtml}
      </div>""",
    "R4-body-detail",
)

# R5 renderEventCard 內計算 detailHtml（守衛：避免重複插入）
if "const detailHtml = renderDetailSections" not in s:
    rep(
        """    const banner = e.bannerImage
      ? `<img class="event-card-banner" src="${escapeHtml(e.bannerImage)}" data-full="${escapeHtml(e.bannerImage)}" data-cap="${escapeHtml(e.name)}" alt="${escapeHtml(e.name)}" loading="lazy">`
      : '';""",
        """    const banner = e.bannerImage
      ? `<img class="event-card-banner" src="${escapeHtml(e.bannerImage)}" data-full="${escapeHtml(e.bannerImage)}" data-cap="${escapeHtml(e.name)}" alt="${escapeHtml(e.name)}" loading="lazy">`
      : '';
    const detailHtml = renderDetailSections(e);""",
        "R5-detailHtml-const",
    )

# R6 新增 renderDetailSections 函式（放在 renderEventCard 前）
RENDER_FN = r"""  function renderDetailSections(e){
    if(!e.detailSections || !e.detailSections.length) return '';
    const blocks = e.detailSections.map(sec => {
      let inner;
      if(sec.text){
        inner = `<p>${escapeHtml(sec.text)}</p>`;
      } else {
        inner = `<ul>${(sec.items || []).map(it => {
          const i = it.indexOf('｜');
          if(i > -1){
            return `<li class="has-chip"><span class="dchip">${escapeHtml(it.slice(0, i))}</span><span>${escapeHtml(it.slice(i + 1))}</span></li>`;
          }
          return `<li>${escapeHtml(it)}</li>`;
        }).join('')}</ul>`;
      }
      return `<div class="event-detail-block ${escapeHtml(sec.type || '')}">
        <div class="event-detail-h"><span class="ic">${escapeHtml(sec.icon || '')}</span>${escapeHtml(sec.label || '')}</div>
        ${inner}
      </div>`;
    }).join('');
    return `<div class="event-detail">${blocks}</div>`;
  }

  function renderEventCard(e, status){"""
if "function renderDetailSections" not in s:
    rep("  function renderEventCard(e, status){", RENDER_FN, "R6-render-fn")

# R7 CSS 區塊（插在 .event-card-body 前）
CSS = """  /* ===== 活動說明結構化區塊 ===== */
  .event-detail{padding:16px 18px 2px;display:flex;flex-direction:column;gap:12px}
  .event-detail-block{--acc:#888;border:1px solid var(--border);border-left:4px solid var(--acc);
    border-radius:10px;padding:12px 15px;background:#fff}
  .event-detail-block.background{--acc:#8E44AD;background:#FBF7FD}
  .event-detail-block.timeline{--acc:#2E86DE;background:#F2F8FE}
  .event-detail-block.reward{--acc:#27AE60;background:#F1FAF4}
  .event-detail-block.draw{--acc:#E8850C;background:#FEF8EF}
  .event-detail-block.note{--acc:#C8102E;background:#FDF3F4}
  .event-detail-h{display:flex;align-items:center;gap:7px;font-weight:800;font-size:14px;
    margin:0 0 9px;color:var(--acc);letter-spacing:.3px}
  .event-detail-h .ic{font-size:16px}
  .event-detail-block ul{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:6px}
  .event-detail-block li{position:relative;padding:1px 0 1px 16px;font-size:13.5px;
    line-height:1.6;color:#2a2a2a}
  .event-detail-block li::before{content:'';position:absolute;left:2px;top:9px;width:6px;height:6px;
    border-radius:50%;background:var(--acc);opacity:.5}
  .event-detail-block li.has-chip{padding-left:0;display:flex;align-items:flex-start;gap:9px}
  .event-detail-block li.has-chip::before{display:none}
  .event-detail-block .dchip{flex-shrink:0;min-width:54px;padding:2px 9px;border-radius:6px;
    background:var(--acc);color:#fff;font-size:12px;font-weight:700;text-align:center;
    font-variant-numeric:tabular-nums;margin-top:1px}
  .event-detail-block p{margin:0;font-size:13.5px;line-height:1.7;color:#2a2a2a}

  .event-card-body{padding:0 18px 20px;border-top:1px solid var(--border)}"""
if ".event-detail-block" not in s:
    rep(
        "  .event-card-body{padding:0 18px 20px;border-top:1px solid var(--border)}",
        CSS,
        "R7-css",
    )

if errors:
    print("MISSING_ANCHORS:" + ",".join(errors))
    sys.exit(2)

if s == orig:
    print("NOCHANGE")
else:
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)
    print("APPLIED")
