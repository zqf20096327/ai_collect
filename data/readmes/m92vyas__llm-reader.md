# Webpage to LLM Ready Input Text

Pre-processing webpage before giving it as input to the LLM improves extraction/scraping accuracy especially if you want to extract website and image links, tables required for most scraping operations like scraping an e-commerce website.

Use this library to turn any webpage/url to LLM friendly text. Fully open source alternative to firecrawl and jina reader api.

You can also refer to my other repo [AI-web_scraper](https://github.com/m92vyas/AI-web_scraper) for direct scraping tools that will do `web search` and `scrapes multiple links` with `just a simple query`. It supports multiple LLMs, Web Search and Extracts Data as per your written instructions.

---

### Free Tools:

[URL to Markdown](https://parseextract.com/url-to-markdown) (for direct URL to markdown conversion using bookmarklet)

[HTML to Markdown](https://parseextract.com/html-to-markdown) (if you have HTML file/text)

---

### Update for Old Users:

We have switched from Selenium to Playwright for concurrent web scraping support. Kindly install the required playwright dependencies as given below.

---
### Install:
```python
# install llm-reader
pip install git+https://github.com/m92vyas/llm-reader.git

# install playwright dependencies. we are using playwright for async/concurrent web scraping support.
playwright install  # to download browser.
playwright install-deps
```

### Import:
```python
from url_to_llm_text import url_to_llm_text
from url_to_llm_text.get_html_text import get_page_source   # you can also use your own code or other services to get the page source
from url_to_llm_text.get_llm_input_text import get_processed_text   # pass html source text to get llm ready text
from url_to_llm_text.config import ScraperConfig, load_config
```

### Get processed LLM input text:

```python
url = <url_to_scrape>

# Option 1: One-liner function
llm_text = await url_to_llm_text(url)
print(llm_text)

# Option 2: Separate HTML fetch and text processing
page_source = await get_page_source(url)
llm_text = await get_processed_text(page_source, url)
print(llm_text)
```

---

### Example Usage:

suppose we want to scrape the product name, main product page link, image link and price from the url "https://www.ikea.com/in/en/cat/corner-sofas-10671/" using any openai model.
```python
import requests
from url_to_llm_text.get_html_text import get_page_source
from url_to_llm_text.get_llm_input_text import get_processed_text

url = "https://www.ikea.com/in/en/cat/corner-sofas-10671/"

# get page html source text using this library function or any other means
page_source = await get_page_source(url)

# get llm ready text and pass the text to your LLM prompt template
llm_text = await get_processed_text(page_source, url)

# prompt template
prompt_format = """extract the product name, product link, image link and price for all the products given in the below webpage. The format should be:
{{
  "1": {{
        "Product Name": ,
        "Product Link": ,
        "Image Link": ,
        "Price":
        }},
  "2": {{
        "Product Name": ,
        ...
        }},
}}

webpage:
{llm_friendly_webpage_text}
"""

# calculate tokens and truncate the llm_text to fit your model context length and your requirements. sometimes you may need only initial part of the webpage.
# below we are manually truncating to 40000 characters. create a seperate function as per your need.
prompt = prompt_format.format(llm_friendly_webpage_text=llm_text[:40000])

api_key = <your openai api key>
headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}
payload = {
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": prompt
        }
  ]}],
  'seed': 0,
  "temperature": 0,
  "top_p": 0.001,
  # "max_tokens": 1024, # if you want to limit the output tokens. this may keep the output json structure incomplete.
  "n": 1,
  "frequency_penalty": 0, "presence_penalty": 0
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json()['choices'][0]['message']['content'])
```

```python
Output
{
    "1": {
        "Product Name": "SÖDERHAMN Corner sofa, 6-seat",
        "Product Link": "https://www.ikea.com/in/en/p/soederhamn-corner-sofa-6-seat-viarp-beige-brown-s69305895/",
        "Image Link": "https://www.ikea.com/in/en/images/products/soederhamn-corner-sofa-6-seat-viarp-beige-brown__0802771_pe768584_s5.jpg?f=xxs",
        "Price": "Rs.1,40,080"
    },
    "2": {
        "Product Name": "HOLMSUND Corner sofa-bed",
        "Product Link": "https://www.ikea.com/in/en/p/holmsund-corner-sofa-bed-borgunda-dark-grey-s49516894/",
        "Image Link": "https://www.ikea.com/in/en/images/products/holmsund-corner-sofa-bed-borgunda-dark-grey__1212713_pe910718_s5.jpg?f=xxs",
        "Price": "Rs.69,990"
    },
    "3": {
        "Product Name": "JÄTTEBO U-shaped sofa, 7-seat",
        "Product Link": "https://www.ikea.com/in/en/p/jaettebo-u-shaped-sofa-7-seat-with-chaise-longue-right-with-headrests-tonerud-grey-s39510618/",
        "Image Link": "https://www.ikea.com/in/en/images/products/jaettebo-u-shaped-sofa-7-seat-with-chaise-longue-right-with-headrests-tonerud-grey__1179836_pe896109_s5.jpg?f=xxs",
        "Price": "Rs.2,60,000"
    },
    "4": {
        "Product Name": "SÖDERHAMN Corner sofa, 4-seat",
        "Product Link": "https://www.ikea.com/in/en/p/soederhamn-corner-sofa-4-seat-with-open-end-tonerud-red-s09514420/",
        "Image Link": "https://www.ikea.com/in/en/images/products/soederhamn-corner-sofa-4-seat-with-open-end-tonerud-red__1213815_pe911323_s5.jpg?f=xxs",
        "Price": "Rs.98,540"
    },
    "5": {
        "Product Name": "JÄTTEBO Mod crnr sofa 2,5-seat w chaise lng",
        "Product Link": "https://www.ikea.com/in/en/p/jaettebo-mod-crnr-sofa-2-5-seat-w-chaise-lng-right-samsala-grey-beige-s09485173/",
        "Image Link": "https://www.ikea.com/in/en/images/products/jaettebo-mod-crnr-sofa-2-5-seat-w-chaise-lng-right-samsala-grey-beige__1109627_pe870119_s5.jpg?f=xxs",
        "Price": "Rs.1,32,000"
    },
    "6": {
        "Product Name": "JÄTTEBO Modular corner sofa, 6 seat",
        "Product Link": "https://www.ikea.com/in/en/p/jaettebo-modular-corner-sofa-6-seat-samsala-dark-yellow-green-s09485248/",
        "Image Link": "https://www.ikea.com/in/en/images/products/jaettebo-modular-corner-sofa-6-seat-samsala-dark-yellow-green__1109619_pe870109_s5.jpg?f=xxs",
        "Price": "Rs.2,06,000"
    },
    "7": {
        "Product Name": "SÖDERHAMN Corner sofa, 3-seat",
        "Product Link": "https://www.ikea.com/in/en/p/soederhamn-corner-sofa-3-seat-viarp-beige-brown-s09305884/",
        "Image Link": "https://www.ikea.com/in/en/images/products/soederhamn-corner-sofa-3-seat-viarp-beige-brown__0802711_pe768555_s5.jpg?f=xxs",
        "Price": "Rs.91,000"
    },
    ......}
```

---

### Documentation:
https://github.com/m92vyas/llm-reader/wiki/Documentation

---

### This open-source repository is sponsored by:
![Proxy-Seller](proxy-seller.png)
Proxy-Seller gives you reliable proxy infrastructure for any workflow: private residential, mobile (4G/5G/LTE), ISP, and datacenter IPv4/IPv6 proxies, all with HTTP(S) and SOCKS5 support. Tap into 47M+ residential IPs across 220+ locations, target exactly the country, city, or ISP you need, and count on 99.7% uptime backed by 24/7 support.

Get 15% off with promo code LLMREADER.

Visit [Proxy-Seller](https://proxy-seller.com/?partner=E031794D853648C8)

---

### To Scrape and Crawl without getting Blocked:

**Built-in Proxy Support**:
You can route requests directly through any residential, mobile, ISP, or datacenter proxy (for example, with [Proxy-Seller](https://proxy-seller.com/?partner=E031794D853648C8)). `llm-reader` provides 3 flexible ways to configure proxies and browser settings:

#### 1. Pass Directly in Code (URL String or Dict):
```python
from url_to_llm_text import url_to_llm_text, get_page_source

# Option A: Standard proxy URL string (e.g. from Proxy-Seller)
# Format: http://login:password@ip:port_http (or socks5://login:password@ip:port_socks)
proxy_url = "http://login:password@11.55.11.0:49353" # update host and port.
text = await url_to_llm_text("https://example.com", proxy=proxy_url)

# Option B: Dictionary format
proxy_dict = {
    "server": "http://11.55.11.0:49353", # update host and port
    "username": "login",
    "password": "password"
}
text = await url_to_llm_text("https://example.com", proxy=proxy_dict)
```

#### 2. Zero-Code Setup via Environment Variable:
Set the proxy in your `.env` or system environment, and `llm-reader` will automatically use it across all requests without altering your code:
```bash
export LLM_READER_PROXY="http://login:password@11.55.11.0:49353" # update host and port
```

#### 3. Using a Configuration File (`llm_reader.yaml` or `llm_reader.json`):
Copy `llm_reader.example.yaml` to `llm_reader.yaml` in your project root. Configure your proxy (e.g., using your Proxy-Seller credentials), browser stealth, and bandwidth savers:
```yaml
proxy:
  server: "http://11.55.11.0:49353" # update host and port
  username: "login"
  password: "password"

performance:
  block_images: false       # Keeps image downloads. If set to true, image URLs are still extracted from data-src!
  block_media: true         # Blocks heavy streaming video/audio (.mp4) to save paid proxy GB
  block_fonts: true         # Blocks web fonts (.woff2) to save proxy bandwidth
  block_trackers: true      # Blocks ads and analytics trackers for 2x faster loading

content:
  remove_header_footer: false # Set true to strip navbars and footers to save LLM tokens
  max_characters: null        # Max output character limit (default: null / no truncation)
```

- Turn on `block_media`, `block_fonts`, and `block_trackers` in your config to avoid wasting paid residential proxy GB on heavy assets.

- You can also replace `get_page_source` with any paid scraping API (e.g. [Scrappey](https://scrappey.com/?ref=rishi)) if you prefer API-based unblocking, and pass the HTML to `get_processed_text`.

- You can use [this guide](Cheaper_Alternative.md) to get an pay as you go option compared to subscription based solutions like Firecrawl.

- You can save in your subscription cost and also in downstream LLM usage cost.

---

### License:
This project is open-source and available under the MIT License.

---

### If you need OCR, Data Extraction, Table Extraction Solution:
Try out [ParseExtract](https://parseextract.com). Pay-As-you-Go Pricing, No Expiry, Accurate.

---

### To Redact your PDFs 100% locally:
Try out [RedactLocal](https://redactlocal.parseextract.com). 100% on device redactions. True redaction instead of just adding black bars.

---

### To Extract tables from PDFs/Images and convert them to Excel/CSV:
Try out [this free tool](https://parseextract.com/table-extraction-free)

or the [Offline Desktop App](https://parseextract.com/offline-table-extractor)

---

### Support & Feedback:
- Share and consider giving a Star if you found this repo helpful.
- Try out [ParseExtract](https://parseextract.com) for one stop API solution for OCR, Structured Data Extraction, Table Extraction for RAG, Agents, and other LLM Parsing / Extraction needs.
- Try out [RedactLocal](https://redactlocal.parseextract.com).
- Try out the [Table Extractor Free Tool](https://parseextract.com/table-extraction-free) or the [Offline Desktop App](https://parseextract.com/offline-table-extractor)
- Open any issues or feature request.
- Also try out the other repo [AI-web_scraper](https://github.com/m92vyas/AI-web_scraper) and leave a Star there if you find it useful.
- Found this repo useful? You can do a one time sponsor [here](https://checkout.dodopayments.com/buy/pdt_HpJcB5tvN3euViX9c4v7M?quantity=1).
