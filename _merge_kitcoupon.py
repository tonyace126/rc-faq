# -*- coding: utf-8 -*-
"""把『通路禮盒（幼貓幼犬／絕育／成貓成犬）問卷完成後的加菜金推播規則』FAQ 合併進 data/faqs.json。
冪等:可重跑(會先移除既有 kitcoupon 分類 / KIT-* 題目再重加)。
不印中文到 stdout,只印 ASCII 狀態,結束寫旗標檔。
來源:GitLab rc-line-mtlr005 #526(2026-02-05 規則紀錄)、#521、#522、#461(成貓成犬 3/19 上線)。
只寫對客服有用的規則,不放系統標籤、coupon 連結與內部判斷細節。"""
import json

PATH = "data/faqs.json"

with open(PATH, encoding="utf-8") as f:
    d = json.load(f)

# --- 1. 分類 ---
d["categories"] = [c for c in d["categories"] if c["id"] != "kitcoupon"]
d["categories"].append({"id": "kitcoupon", "name": "通路禮盒加菜金", "color": "#6C5CE7"})

# --- 2. FAQ 題目 ---
UPD = "2026-11-03"
CAT = "kitcoupon"
KIT_IDS = ["KIT-%03d" % i for i in range(1, 5)]
new_faqs = [
{
  "id": "KIT-001",
  "category": CAT,
  "title": "通路禮盒加菜金：哪些會員會收到？（客服總表）",
  "tags": ["加菜金","coupon","通路禮盒","幼貓幼犬禮盒","絕育禮盒","成貓成犬禮盒","問卷","通路","總覽"],
  "memberSymptom": "（客服判斷用）會員問「領了禮盒、填了問卷，有沒有加菜金？」先確認他領的是哪一種禮盒、問卷通路填了什麼",
  "rootCause": "會員在通路領取實體禮盒後，掃 QR code／點專屬連結填寫通路問卷。符合通路條件者，官方帳號會在『完成問卷後第 3 天』推播加菜金（coupon）訊息。是否發送依『問卷所填的通路類別』判斷。",
  "csSteps": [
    "幼貓幼犬禮盒：問卷通路填『收容所/協會』或『貓舍/犬舍』→ 完成問卷後第 3 天推播加菜金。",
    "絕育禮盒：問卷通路填『獸醫院』→ 完成問卷後第 3 天推播加菜金。",
    "成貓成犬禮盒：問卷通路只有『收容所/協會』→ 比照幼貓幼犬，完成問卷後第 3 天推播（訊息標題『恭喜你獲得500元加菜金！』）。",
    "通路不在上述條件內的問卷，不會收到加菜金推播。",
    "加菜金 coupon 的使用方式與期限，依推播訊息內的說明。",
  ],
  "replyTemplate": "您好～填寫禮盒問卷後，若符合活動的通路條件，法國皇家官方帳號會在完成問卷後第 3 天傳送「加菜金」訊息給您，使用方式請依訊息內的說明喔！",
  "images": [],
  "updated": UPD,
},
{
  "id": "KIT-002",
  "category": CAT,
  "title": "填完禮盒問卷，什麼時候會收到加菜金？",
  "tags": ["加菜金","coupon","問卷","第3天","什麼時候"],
  "memberSymptom": "我填完禮盒問卷了，加菜金什麼時候會來？",
  "rootCause": "加菜金不是填完當下發送，而是在完成問卷後第 3 天由官方帳號推播。",
  "csSteps": [
    "詢問會員填寫問卷的日期。",
    "未滿 3 天：說明加菜金會在第 3 天推播，請會員稍候。",
    "已超過 3 天仍沒收到：依 KIT-003 排查。",
  ],
  "replyTemplate": "您好～加菜金會在您完成問卷後的第 3 天，由法國皇家官方帳號傳送給您喔！請再稍候一下～",
  "images": [],
  "updated": UPD,
},
{
  "id": "KIT-003",
  "category": CAT,
  "title": "填了禮盒問卷，卻沒收到加菜金",
  "tags": ["加菜金","coupon","沒收到","問卷","通路","封鎖"],
  "memberSymptom": "我領了禮盒也填了問卷，為什麼沒收到加菜金？",
  "rootCause": "常見原因：① 還沒到完成問卷後第 3 天 ② 問卷所填通路不符該禮盒的加菜金條件（見 KIT-001）③ 會員封鎖了法國皇家官方帳號，收不到推播。",
  "csSteps": [
    "確認填寫問卷的日期，未滿 3 天請會員稍候（見 KIT-002）。",
    "確認會員領的是哪一種禮盒、問卷通路填了什麼，對照 KIT-001；不符通路條件就不會發送。",
    "確認會員沒有封鎖官方帳號（解除方式見 FAIR-005）。",
    "以上都符合仍未收到：收集 LINE 暱稱、禮盒種類、問卷填寫日期與通路、截圖，依 MEM-001 回報。",
  ],
  "replyTemplate": "您好～加菜金會在完成問卷後第 3 天由官方帳號傳送，麻煩您先確認是否已滿 3 天，以及沒有封鎖法國皇家官方帳號喔！若已超過 3 天仍沒收到，請提供您的 LINE 暱稱、領取的禮盒種類與填寫問卷的日期，我們協助您查詢～",
  "images": [],
  "updated": UPD,
},
{
  "id": "KIT-004",
  "category": CAT,
  "title": "通路領的禮盒，和 FB 宅配的成長禮盒有什麼不同？",
  "tags": ["通路禮盒","成長禮盒","宅配","FB連結","差別","加菜金"],
  "memberSymptom": "我在店家／收容所領了禮盒，跟 FB 上的成長禮盒活動是同一個嗎？",
  "rootCause": "兩者領取管道不同：通路禮盒是在收容所/協會、貓舍/犬舍、獸醫院等通路現場領取，填通路問卷後符合條件者第 3 天收到加菜金；成長禮盒（宅配）是 FB 指定連結活動，免扣點宅配到府（見 BOX-001）。",
  "csSteps": [
    "先確認會員是在通路現場領取，還是透過 FB 指定連結申請宅配。",
    "通路禮盒的加菜金問題：依 KIT-001～KIT-003 處理。",
    "成長禮盒（宅配）問題：依 BOX-001 起的題目處理。",
    "注意：2026 年已透過通路領過幼貓幼犬成長禮盒的會員，不符 FB 宅配活動資格（見 BOX-007）。",
  ],
  "replyTemplate": "您好～在店家或收容所現場領取的禮盒，和 Facebook 上的成長禮盒宅配活動是不同的領取管道喔！請問您是在哪裡領取禮盒的呢？我們依您的情況協助您～",
  "images": [],
  "updated": UPD,
},
]

assert [q["id"] for q in new_faqs] == KIT_IDS

# 先移除既有 KIT-* 再加(冪等)
d["faqs"] = [q for q in d["faqs"] if not str(q.get("id", "")).startswith("KIT-")]
d["faqs"].extend(new_faqs)

d["meta"]["lastUpdated"] = "2026-11-03 通路禮盒加菜金 FAQ"

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

# 驗證:重讀 + 計數,只印 ASCII
with open(PATH, encoding="utf-8") as f:
    chk = json.load(f)
kit = [q for q in chk["faqs"] if str(q["id"]).startswith("KIT-")]
cats = [c["id"] for c in chk["categories"]]
dup = len(chk["faqs"]) - len({q["id"] for q in chk["faqs"]})
bad_cat = [q["id"] for q in chk["faqs"] if q["category"] not in cats]
with open("/tmp/merge_kitcoupon.done.txt", "w") as f:
    f.write("OK total_faqs=%d kit=%d kitcoupon_cat=%s dup=%d bad_cat=%s\n" % (
        len(chk["faqs"]), len(kit), ("kitcoupon" in cats), dup, bad_cat))
print("MERGE_DONE faqs=%d kit=%d" % (len(chk["faqs"]), len(kit)))
