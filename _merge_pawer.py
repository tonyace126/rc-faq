"""把「10/12-11/8 毛孩能量 PAWER 活動」合併進 data/faqs.json 與 data/screens.json。

內容僅取自活動頁面與活動辦法（消費者端可見資訊），截圖已打碼。
重複執行會覆蓋同 id 的活動 / 流程 / 快速連結，不會重複新增。
"""
import json

FAQS = "data/faqs.json"
SCREENS = "data/screens.json"
IMG = "images/screens/pawer-2610/"
LIFF = "https://liff.line.me/1657147716-SC5KL3y9"

EVENT = {
    "id": "PAWER-2610",
    "name": "10/12-11/8 毛孩能量 PAWER 活動",
    "shortName": "毛孩能量 PAWER",
    "startDate": "2026-10-12",
    "endDate": "2026-11-08",
    "bannerImage": IMG + "01-home.jpg",
    "tagline": "上傳毛孩照片＋選一句能量小語，製作專屬「毛孩能量小卡」分享給好友；完成三大任務最高可獲 1,800 HP，全數完成再抽 2kg 飼料包（共 10 名）。需成為法國皇家會員，點數於活動後發放。",
    "summary": "活動期間 10/12–11/8，經由 LINE 官方帳號、活動連結或網路廣告進入活動網頁，完成 LINE 登入授權（無須加入官方帳號好友）即可製作「毛孩能量小卡」並分享給 LINE 好友。三大任務：製作 2 次小卡（最高 300 HP）、分享小卡給好友 3 次（最高 300 HP）、分享活動連結邀請 3 位好友完成小卡製作並成為會員（最高 1,200 HP）。遊玩與分享不需是會員，但 HP 與贈品須完成法國皇家會員登錄才能領取：HP 以活動截止時累積點數計算，11/30 派送至會員帳號；完成全部任務者具 2kg 飼料包抽獎資格（共 10 名），11/11 以 LINE 通知中獎，11/17 前回覆領獎資料，獎項預計 12/15 前寄出。",
    "flowId": "FLOW-PAWER-2610",
    "detailSections": [
        {
            "type": "background",
            "icon": "💡",
            "label": "活動背景",
            "text": "以「毛孩療癒小卡」為互動鉤子的邀請好友活動：會員上傳毛孩照片、選擇或自行輸入一句能量小語，生成專屬小卡分享給好友；好友透過分享者的活動連結進來、完成小卡製作並成為會員，分享者即可獲得點數。目的是帶動新會員註冊。"
        },
        {
            "type": "timeline",
            "icon": "📅",
            "label": "活動時間",
            "items": [
                "10/12｜活動開始",
                "11/08｜活動截止（點數以此時累積點數計算）",
                "11/11｜以 LINE 通知 2kg 飼料包中獎者",
                "11/17｜中獎者回覆並填寫領獎資料截止",
                "11/30｜HP 點數派送至會員帳號",
                "12/15｜獎項預計寄出（如遇不可抗力另行通知）"
            ]
        },
        {
            "type": "reward",
            "icon": "🎁",
            "label": "三大任務（最高 1,800 HP）",
            "items": [
                "任務一｜完成製作 2 次毛孩能量小卡：每次 150 HP，最高 300 HP",
                "任務二｜分享毛孩能量小卡給好友 3 次：每次 100 HP，最高 300 HP",
                "任務三｜分享活動連結給 3 位好友，好友透過連結完成小卡製作並成為會員：每位 400 HP，最高 1,200 HP"
            ]
        },
        {
            "type": "draw",
            "icon": "🎰",
            "label": "抽獎與贈品",
            "items": [
                "抽獎資格｜加入會員並完成活動所有任務",
                "獎項｜2kg 飼料包，共 10 名",
                "通知｜11/11 發送至與會員帳號連結之 LINE 帳號；封鎖官方帳號導致收不到訊息視為放棄",
                "領獎｜11/17 前回覆並填寫收件人姓名、電話、地址；逾期或資料不完整視為放棄，依序遞補"
            ]
        },
        {
            "type": "note",
            "icon": "⚠️",
            "label": "注意事項",
            "items": [
                "參加對象｜年滿 18 歲、持有中華民國國民身分證之台灣國民；獎項寄送限台灣地區",
                "會員資格｜遊玩與分享不需是會員；HP 與贈品須完成法國皇家會員登錄才能領取，活動結束後統一發送",
                "好友計數｜受邀好友須為「首次」進入活動網頁才算 1 次有效分享；同一人重複點擊、或用自己帳號重複進入不列入計算",
                "兩種分享｜任務二是結果頁「分享小卡」（送出小卡圖文訊息）；任務三是首頁點數任務區「分享活動，邀請好友」（送出帶分享者代碼的活動連結）",
                "上傳規範｜照片須以毛孩為主體且為本人拍攝或有合法使用權；不得含清晰可辨之他人臉部或個資、他牌商標、違法或侵權內容，違規內容可不經通知移除並取消資格",
                "分享環境｜分享功能須在 LINE App 內開啟活動頁才能使用（一般瀏覽器會顯示「目前的環境不支援分享功能」）"
            ]
        }
    ],
    "faqIds": []
}

QUICK_LINK = {
    "label": "毛孩能量 PAWER",
    "url": LIFF,
    "tag": "期間活動",
    "tagType": "event",
    "startDate": "2026-10-12",
    "endDate": "2026-11-08"
}

FLOW = {
    "id": "FLOW-PAWER-2610",
    "category": "campaign",
    "name": "2026/10/12-11/08 毛孩能量 PAWER 活動",
    "description": "會員從活動首頁登入 LINE、上傳毛孩照片、選擇能量小語，生成「毛孩能量小卡」後可下載、分享給好友或加入會員；首頁點數任務區顯示三大任務進度。客服收到會員截圖時可對照這條流程找出所在頁面。",
    "steps": [
        {
            "title": "Step 1：活動首頁與點數任務（不需登入）",
            "description": "首頁不需登入即可瀏覽主視覺、活動辦法與三大點數任務。點「登入 Line 後製作毛孩能量小卡」或「登入查看點數任務」才會導向 LINE Login。\n\n注意：在一般瀏覽器開啟時，任務三會顯示「目前的環境不支援分享功能，請在 LINE App 內開啟本頁」，請會員改從 LINE 內開啟。",
            "images": [IMG + "01-home.jpg", IMG + "02-home-tasks-1.jpg", IMG + "03-home-tasks-2.jpg"],
            "relatedFaqs": []
        },
        {
            "title": "Step 2：活動辦法彈窗",
            "description": "首頁「活動辦法」點開為彈窗，共九大段：壹 活動資訊、貳 參加資格、參 參加方式（含好友計數說明）、肆 獎項與資格、伍 得獎通知與領獎（含稅務規定）、陸 參加者上傳內容規範、柒 內容使用授權、捌 個人資料保護、玖 資格取消與爭議處理。會員問規則時可直接引用對應段落。",
            "images": [IMG + f"{i:02d}-rules-{i - 3:02d}.jpg" for i in range(4, 19)],
            "relatedFaqs": []
        },
        {
            "title": "Step 3：LINE Login 授權",
            "description": "點登入按鈕後導向 LINE 登入授權頁（手機 LINE 內會直接授權；電腦瀏覽器會出現帳號密碼 / 行動條碼登入畫面）。只需 LINE 授權，不需加入官方帳號好友。",
            "image": IMG + "19-line-login.jpg",
            "relatedFaqs": []
        },
        {
            "title": "Step 4：上傳毛孩照片＋同意隱私權政策",
            "description": "點擊或拖曳上傳照片，支援 JPG / PNG；上傳後點圖片可重新替換。須勾選「我已閱讀並同意隱私政策」，「下一步」才會亮起。隱私權政策為「毛孩能量 PAWER」個人資料蒐集同意聲明（利用期間至活動結束後 1 年）。",
            "images": [IMG + "20-upload-empty.jpg", IMG + "21-privacy-1.jpg", IMG + "22-privacy-2.jpg", IMG + "23-upload-done.jpg"],
            "relatedFaqs": []
        },
        {
            "title": "Step 5：選擇能量小語",
            "description": "畫面顯示 4 句能量小語範本（共 10 句隨機出現），最後一欄可自行輸入想對自己或毛孩說的話（20 字內）。選好後按「下一步」生成小卡。",
            "image": IMG + "24-choose-message.jpg",
            "relatedFaqs": []
        },
        {
            "title": "Step 6：小卡結果頁",
            "description": "顯示「你的毛孩能量小卡已準備好！」，下方按鈕導向：\n・下載毛孩能量小卡 → 另開視窗下載（Step 7）\n・分享毛孩能量小卡給好友 → 開啟 LINE 好友分享選單（Step 8，任務二）\n・立即加入會員 → 法國皇家集點平台（Step 9）\n・再玩一次 → 回到「上傳毛孩照片」\n・查看點數任務 → 首頁點數任務區",
            "image": IMG + "25-result.jpg",
            "relatedFaqs": []
        },
        {
            "title": "Step 7：下載毛孩能量小卡",
            "description": "結果頁點「下載毛孩能量小卡」會另開視窗顯示小卡，按「點我下載」存到手機。",
            "image": IMG + "26-download.jpg",
            "relatedFaqs": []
        },
        {
            "title": "Step 8：分享小卡給好友（任務二）",
            "description": "結果頁點「分享毛孩能量小卡給好友」會開啟 LINE 分享選單，可選群組、好友或聊天室。好友收到的是小卡圖文訊息，標題「〔分享者名稱〕毛孩能量已送達，立即補充今日份 Pawer！」，點「立即製作」即可進入活動。（截圖中的好友名單與人名已馬賽克）",
            "images": [IMG + "27-share-card-picker.jpg", IMG + "31-share-card-received.jpg"],
            "relatedFaqs": []
        },
        {
            "title": "Step 9：立即加入會員",
            "description": "點「立即加入會員」會導向法國皇家集點平台（法國皇家毛孩健康專寵計劃）加入會員。HP 與贈品須完成會員登錄才能領取。（截圖中的會員名稱已馬賽克）",
            "image": IMG + "28-join-member.jpg",
            "relatedFaqs": []
        },
        {
            "title": "Step 10：點數任務進度與邀請好友（任務三）",
            "description": "回到首頁點數任務區可看到累積點數與各任務進度，完成的任務按鈕變成灰色「已完成」。任務三每成功邀請 1 位好友會打勾 +400。點「分享活動，邀請好友」送出的是帶分享者代碼（shareCode）的活動首頁連結，不是小卡圖；好友須透過此連結完成小卡製作並成為會員才算成功邀請。（截圖中的 shareCode 已馬賽克）",
            "images": [IMG + "29-tasks-done-1.jpg", IMG + "30-tasks-done-2.jpg", IMG + "32-share-invite-link.jpg"],
            "relatedFaqs": []
        }
    ]
}


def upsert(lst, item, key):
    for i, x in enumerate(lst):
        if x.get(key) == item[key]:
            lst[i] = item
            return
    lst.append(item)


faqs = json.load(open(FAQS, encoding="utf-8"))
faqs["meta"]["lastUpdated"] = "2026-10-13 毛孩能量 PAWER 活動"
upsert(faqs["meta"]["events"], EVENT, "id")
upsert(faqs["meta"]["quickLinks"]["events"], QUICK_LINK, "label")
with open(FAQS, "w", encoding="utf-8") as f:
    json.dump(faqs, f, ensure_ascii=False, indent=2)
    f.write("\n")

screens = json.load(open(SCREENS, encoding="utf-8"))
upsert(screens["flows"], FLOW, "id")
with open(SCREENS, "w", encoding="utf-8") as f:
    json.dump(screens, f, ensure_ascii=False, indent=2)
    f.write("\n")

print("ok")
