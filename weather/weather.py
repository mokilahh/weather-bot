import requests
from datetime import datetime

# ==== 把这里换成你自己的 SendKey ====
SENDKEY = "SCT436057TTIXzXvQABLvQJ3A0fs16FvE6"

# ==== 把这里换成你所在的城市拼音 ====
CITY = "Wuhu"

# 1. 抓天气
url = f"https://wttr.in/{CITY}?format=j1"
data = requests.get(url).json()

today = data["weather"][0]
date = today["date"]
mintemp = int(today["mintempC"])
maxtemp = int(today["maxtempC"])
desc = today["hourly"][4]["weatherDesc"][0]["value"]
wind = today["hourly"][4]["windspeedKmph"]

# 2. 判断是否带伞
if "rain" in desc.lower() or "shower" in desc.lower():
    umbrella = "☔ 今天有雨，记得带伞！"
elif "snow" in desc.lower():
    umbrella = "❄️ 今天有雪，注意保暖！"
else:
    umbrella = "🌞 今天没雨，放心出门~"

# 3. 穿衣建议
avg = (mintemp + maxtemp) / 2
if avg >= 28:
    cloth = "👕 短袖短裤，热"
elif avg >= 20:
    cloth = "👔 薄外套或长袖，舒适"
elif avg >= 12:
    cloth = "🧥 外套 + 长裤，微凉"
elif avg >= 5:
    cloth = "🧣 厚外套 + 毛衣，冷"
else:
    cloth = "🧤 羽绒服 + 围巾，非常冷"

# 4. 问候语
hour = datetime.now().hour
if hour < 12:
    hi = "早上好！新的一天开始啦 ☀️"
elif hour < 18:
    hi = "下午好！继续加油 💪"
else:
    hi = "晚上好！辛苦一天啦 🌙"

# 5. 拼消息
msg = f"""{hi}

【今日天气】{date}
📍 {CITY}：{desc}
🌡️ 气温：{mintemp}℃ ~ {maxtemp}℃
💨 风速：{wind} km/h

{umbrella}
{cloth}
"""

# 6. 推到微信
requests.post(
    f"https://sctapi.ftqq.com/{SENDKEY}.send",
    data={"title": "今日天气", "desp": msg}
)

print("发送成功：")
print(msg)