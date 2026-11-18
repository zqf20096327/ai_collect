# YBS Bus Data (Yangon Bus Service)

ရန်ကုန်မြို့ YBS ဘတ်စ်ကားလိုင်းများ၏ လမ်းကြောင်း၊ မှတ်တိုင်အမည်နှင့် မှတ်တိုင်တည်နေရာများကို JSON ဖိုင်များဖြင့် စုစည်းထားသော open data repository ဖြစ်သည်။ Mobile App, Website, AI assistant, chatbot/bot နှင့် data visualization များတွင် အသုံးပြုနိုင်သည်။

> **သတိပြုရန်:** ဤ repository သည် static data files များပေးထားခြင်းသာဖြစ်ပြီး hosted API server, live bus tracking သို့မဟုတ် real-time arrival times မပါဝင်ပါ။ Raw GitHub URL များကို API endpoint ကဲ့သို့ fetch လုပ်နိုင်သော်လည်း production အသုံးပြုမှုအတွက် ကိုယ်ပိုင် backend/cache တည်ဆောက်ရန် အကြံပြုသည်။ လမ်းကြောင်းနှင့် မှတ်တိုင်အချက်အလက်များ ပြောင်းလဲနိုင်သောကြောင့် အသုံးမပြုမီ အတည်ပြုပါ။

## ပါဝင်သည့်အချက်အလက်

- `ybs_*_data.json` — bus route တစ်ခုစီအတွက် JSON data (အောက်ပါ catalog တွင် လက်ရှိဖိုင် 147 ခုစာရင်းပြုထားသည်)
- `api/routes.json` — route catalog နှင့် ဖိုင်တစ်ခုချင်း၏ raw URL

ဖိုင်အမည်များတွင် route အလိုက် ကွဲပြားသည့် suffix များ ပါနိုင်သည် (ဥပမာ `ybs_111_industrial_zone_data.json`)။ ထို့ကြောင့် route number ဖြင့်ဖိုင်အမည်ကို ခန့်မှန်းမည့်အစား `api/routes.json` ကိုသုံးပါ။

## JSON ဖွဲ့စည်းပုံ

```json
{
  "bus_line": "100",
  "route_info": {
    "Route Name": "100",
    "Line Name": "...",
    "Agency": "...",
    "Route Type": "route",
    "Total Stops": "104 stops",
    "QR Payment": "✅ Supported"
  },
  "stops": [
    {
      "index": "1",
      "stop_name_en": "Kyi Su",
      "stop_name_mm": "ကျီစုသုဿန်",
      "road": "...",
      "latitude": 16.874687,
      "longitude": 96.280012
    }
  ]
}
```

`route_info` ထဲက key အမည်များသည် လက်ရှိ data အတိုင်း space ပါသော English keys ဖြစ်သည်။ `Total Stops` သည် text ဖြစ်နိုင်သောကြောင့် stop အရေအတွက်ကိုတွက်ရာတွင် `stops.length` ကိုအသုံးပြုပါ။ Latitude/longitude တန်ဖိုးများသည် number ဖြစ်သည်။

## Static JSON API အသုံးပြုပုံ

Catalog endpoint (GitHub raw):

```text
https://raw.githubusercontent.com/hidecard/YBS-Bus-Data/main/api/routes.json
```

Route data URL များကို catalog ၏ `routes[].data_url` မှ ရယူပါ။ ဥပမာ route `100` အတွက်:

```text
https://raw.githubusercontent.com/hidecard/YBS-Bus-Data/main/ybs_100_data.json
```

### JavaScript / Web / App

```js
const catalogUrl =
  "https://raw.githubusercontent.com/hidecard/YBS-Bus-Data/main/api/routes.json";

const catalog = await fetch(catalogUrl).then((r) => {
  if (!r.ok) throw new Error(`HTTP ${r.status}`);
  return r.json();
});

const route = catalog.routes.find((item) => item.bus_line === "100");
if (!route) throw new Error("Route not found");
const routeData = await fetch(route.data_url).then((r) => r.json());
console.log(routeData.route_info, routeData.stops);
```

### Python / Backend / AI pipeline

```python
import requests

catalog_url = "https://raw.githubusercontent.com/hidecard/YBS-Bus-Data/main/api/routes.json"
catalog = requests.get(catalog_url, timeout=20).json()
route = next(item for item in catalog["routes"] if item["bus_line"] == "100")
data = requests.get(route["data_url"], timeout=20).json()
for stop in data["stops"]:
    print(stop["index"], stop["stop_name_mm"], stop["stop_name_en"])
```

### Bot / AI အတွက် အသုံးပြုနိုင်သည့်ပုံစံ

1. `api/routes.json` ကို စတင်ဖတ်ပြီး route catalog ကို cache လုပ်ပါ။
2. အသုံးပြုသူက မေးသော bus line ကို `routes[].bus_line` နှင့်ကိုက်ညီအောင်ရှာပါ။
3. ကိုက်ညီသည့် `data_url` ကို fetch လုပ်ပြီး `stops` ကို ရှာဖွေ/ပြန်ဖြေပါ။
4. AI ကိုပေးသည့် context တွင် ဒီအချက်အလက်သည် static ဖြစ်ပြီး real-time data မဟုတ်ကြောင်း ထည့်သွင်းဖော်ပြပါ။
5. API request များကို cache လုပ်ပြီး HTTP error, timeout နှင့် route မတွေ့သည့်အခြေအနေများကို ကိုင်တွယ်ပါ။

## Local အသုံးပြုခြင်း

```bash
git clone https://github.com/hidecard/YBS-Bus-Data.git
cd YBS-Bus-Data
```

လိုအပ်သည့် `ybs_..._data.json` ဖိုင်ကို တိုက်ရိုက်ဖတ်နိုင်သည်၊ သို့မဟုတ် catalog မှ ဖိုင်အမည်/URL ကိုရှာနိုင်သည်။ Python 3 standard library ဖြင့် စစ်ဆေးရန်:

```bash
python -m json.tool ybs_100_data.json
```

## Data အရည်အသွေးနှင့် ကန့်သတ်ချက်များ

- ဖိုင်များသည် static community data ဖြစ်ပြီး ပြောင်းလဲမှု၊ မပြည့်စုံမှု သို့မဟုတ် typo များ ရှိနိုင်သည်။
- Real-time bus location, arrival prediction, fare နှင့် schedule များကို ဤ repository က အာမခံ/မပေးထားပါ။
- GitHub raw content ကို production API အဖြစ် အသုံးပြုရာတွင် availability/rate limit အာမခံမရှိပါ။ လိုအပ်ပါက ကိုယ်ပိုင် mirror, cache သို့မဟုတ် API server အသုံးပြုပါ။
- အချက်အလက်ကို လုံခြုံရေးအရေးကြီးသည့် ဆုံးဖြတ်ချက်အတွက် တစ်ခုတည်းသောရင်းမြစ်အဖြစ် မသုံးပါနှင့်။

## ပါဝင်ကူညီခြင်း

JSON ဖိုင်အသစ်ထည့်ခြင်း/ပြင်ဆင်ခြင်းမပြုမီ အနီးစပ်ဆုံး format နှင့်ကိုက်ညီမှု၊ stop index အစဉ်၊ latitude/longitude number ဖြစ်မှုနှင့် JSON validity ကို စစ်ဆေးပါ။ Pull Request တွင် ပြောင်းလဲသည့် route၊ source/verification date နှင့် သတိပြုစရာများကို ရှင်းပြပါ။

## License / Attribution

အသုံးမပြုမီ repository ၏ လက်ရှိ license နှင့် data အရင်းအမြစ်/အသုံးပြုခွင့်ကို စစ်ဆေးပါ။ License သတ်မှတ်မထားပါက permission ရှိသည်ဟု မယူဆပါနှင့်။ အသုံးပြုသည့်အခါ မူရင်း repository ကို attribution ပေးပြီး data မှားယွင်းနိုင်ကြောင်း ဖော်ပြပါ။

## English summary

Static JSON dataset for Yangon Bus Service (YBS) routes and stops. Route records include route metadata and ordered stops with English/Myanmar names and coordinates. Use `api/routes.json` as the route catalog and fetch each record's `data_url`. This repository does not provide a hosted API, live tracking, or real-time arrivals. Verify the repository license and data accuracy before production use.
