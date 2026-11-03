# 🧪 ai-lab

**Testovací repozitár pre online kurzy AI, ChatGPT a GPTZero.**

Tento repozitár slúži na **praktické školenie GPTZero a detekcie AI generovaného textu**, prácu s AI vo výučbe, marketingu a výskume, preverovanie citácií a zodpovednú interpretáciu výsledkov. Štruktúrou nadväzuje na [curl-lab](https://github.com/miroslav-reiter/curl-lab): hlavný README, podrobné príklady, cheat sheet, laboratórne úlohy, tréningové dáta a vlastné skripty.

Materiály sú určené pre **učiteľov, lektorov, vysokoškolských pedagógov, doktorandov, výskumníkov, vedeckých pracovníkov, znalcov, forenzných analytikov, SEO a marketingových špecialistov, redaktorov, správcov webov, WordPress používateľov a technicky orientovaných záujemcov**.

> **Najdôležitejšie pravidlo:** GPTZero odhaduje pôvod textu. Nevie samo osebe dokázať, kto text napísal, či ide o podvod alebo či je text plagiát. Preto oddeľujeme AI Detection, Plagiarism Check, overovanie zdrojov a Writing Replay.

## 📌 Čo je GPTZero

**GPTZero** je online nástroj na analýzu pravdepodobného pôvodu textu. Pomocou klasifikačných modelov odhaduje, či text vykazuje znaky **Human (ľudský pôvod), AI (generatívna AI) alebo Mixed (kombinovaný pôvod)**. Podľa dostupného plánu ponúka základnú aj podrobnejšiu analýzu, zvýrazňovanie problematických viet, rozšírenie pre webový prehliadač, Microsoft Word a Writing Report v Google Dokumentoch.

- Web: [gptzero.me](https://gptzero.me/)
- Oficiálna dokumentácia: [GPTZero Support](https://support.gptzero.me/)
- Prehliadač: **GPTZero: AI Detection & Writing Replay** (Chrome, Edge, Firefox)
- Word: oficiálny doplnok **GPTZero for Word**
- Google Dokumenty: **Writing Report / Writing Replay** cez rozšírenie
- Pokročilé funkcie: Plagiarism Check, AI Hallucinations / Fact Check, Possible AI Paraphrasing podľa dostupného plánu

## 🧪 Hotové testovacie texty GPTZero

**[Súbor testovacích textov – data/gptzero-testovacie-texty/](data/gptzero-testovacie-texty/README.md)** · **[Stiahnuť DOCX (ZIP)](data/gptzero-testovacie-texty/gptzero-testovacie-texty-word.zip)** obsahuje 10 AI-generovaných vzoriek od krátkeho komentára po odborné, akademické a marketingové články v slovenčine aj angličtine. Dopĺňajú ich metodiky na skutočne ľudskú kontrolnú vzorku a zmiešaný text, metadáta so známym pôvodom a postup zaznamenávania reálnych výsledkov z GPTZero.

**Upozornenie:** Hotové texty vytvorila AI; GPTZero ich môže klasifikovať aj inak. Nesmieme ich vydávať za ľudské.

## 🧠 Základný model práce

1. Pripravíme testovací text alebo dokument so **známym pôvodom**.
2. Zvolíme **Basic Scan, Advanced Scan alebo inú príslušnú kontrolu**.
3. Vyhodnotíme klasifikáciu a sprievodné vysvetlenie.
4. Rozlíšime modelový odhad od skutočných informácií o tvorbe dokumentu.
5. Výsledok zapíšeme do protokolu a doplníme overiteľné podklady.
6. Pri študentských alebo klientskych dokumentoch chránime osobné údaje a nevyvodzujeme automatické obvinenia.

| Prvok | Význam |
|---|---|
| GPTZero | detektor pravdepodobného pôvodu textu |
| Human | predikcia ľudského pôvodu |
| AI | predikcia AI generovania |
| Mixed | predikcia zmiešaného pôvodu |
| Confidence | miera istoty klasifikácie, nie dokázaný podiel AI viet |
| False positive | ľudský text mylne označený za AI |
| False negative | AI text mylne označený za ľudský |
| Writing Replay | zaznamenaná história písania a vložení |
| Plagiarism Check | podobnosť s existujúcimi zdrojmi |
| Source Check | existencia a relevancia citácií a ich podpora tvrdení |
| AI Vision | priebežná analýza textu na podporovaných weboch |

## 🎯 Na čo GPTZero používame v praxi

- predbežná analýza AI textov v školských a akademických prácach;
- rozlíšenie možného AI a ľudského pôvodu článkov;
- kontrola textov na Facebooku, LinkedIne, X, Reddite, YouTube a ďalších podporovaných službách;
- kontrola blogov, webových stránok, marketingových opisov a recenzií;
- práca s doplnkom GPTZero priamo v Microsoft Worde;
- analýza histórie písania v Google Dokumentoch;
- zisťovanie podobnosti s existujúcimi zdrojmi;
- preverovanie existencie publikácií, citácií a DOI;
- diskusia o prípustnom použití AI pri vzdelávaní a výskume;
- kontrolované experimenty s falošnými pozitívami a negatívami.

## 💻 Kde GPTZero využijeme

| Prostredie | Praktické využitie |
|---|---|
| Google Chrome / Microsoft Edge / Firefox | rozšírenie, Scan Selection, Scan Page, AI Vision |
| Microsoft Word | doplnok, označenie textu, Get Results |
| Google Dokumenty | Writing Report a Writing Replay |
| Online služba GPTZero | Basic/Advanced Scan, upload DOCX/PDF, ďalšie dostupné nástroje |
| Facebook a LinkedIn | predbežná analýza príspevkov |
| Reddit, X, YouTube, Medium | analýza dostupného textového obsahu |
| WordPress a webové stránky | kontrola vlastných článkov a opisov |
| Windows, Ubuntu, Kali Linux, macOS | lokálne spracovanie CSV tréningových výsledkov v Pythone |

## 📁 Štruktúra repozitára

| Súbor / priečinok | Obsah |
|---|---|
| [gptzero-priklady.md](gptzero-priklady.md) | **16 praktických príkladov** s postupmi, vysvetlením a cieľom |
| [gptzero-socialne-siete-web.md](gptzero-socialne-siete-web.md) | AI Vision, Facebook, LinkedIn, Reddit, X, YouTube, webové stránky |
| [gptzero-word-google-docs.md](gptzero-word-google-docs.md) | Word Add-in, Google Docs Writing Report a Writing Replay |
| [gptzero-plagiatorstvo-citacie.md](gptzero-plagiatorstvo-citacie.md) | Plagiarism Check, kontrola citácií, DOI a AI parafrázovania |
| [ai-povod-textu-principy.md](ai-povod-textu-principy.md) | čo detektor hodnotí, falošné pozitíva, metodika experimentu |
| [gptzero-metodika-etika.md](gptzero-metodika-etika.md) | akademická integrita, súkromie, auditná karta, zodpovedné závery |
| [gptzero-cheatsheet.md](gptzero-cheatsheet.md) | rýchle tabuľky a prehľad nastavení |
| [gptzero-otazky-odpovede.md](gptzero-otazky-odpovede.md) | 10 otázok a odpovedí podľa prezentácie |
| [ai-prompty-trening.md](ai-prompty-trening.md) | 8 príkladov na tvorbu kontrolovaných AI vzoriek |
| [examples/](examples/) | päť laboratórnych úloh s očakávaným výstupom |
| [data/](data/) | syntetické AI texty, sociálne príspevky, citácie, CSV šablóna |
| [scripts/vyhodnotenie-gptzero.py](scripts/vyhodnotenie-gptzero.py) | **offline** výpočet výsledkov klasifikácie bez GPTZero API |
| [.gitignore](.gitignore) | vylúčenie dočasných a súkromných súborov |

## ⚙️ 1. Stiahnutie repozitára – Windows PowerShell

```powershell
git clone https://github.com/miroslav-reiter/ai-lab.git
cd ai-lab
py -3 --version
```

Ak nemáme Git, na GitHube otvoríme **Code → Download ZIP** a archív rozbalíme.

## 🐧 2. Stiahnutie – Ubuntu alebo Kali Linux

```bash
git clone https://github.com/miroslav-reiter/ai-lab.git
cd ai-lab
python3 --version
```

Pre samotné používanie webového GPTZero nie je Python nevyhnutný. Použijeme ho iba na **lokálne vyhodnotenie manuálne získaných výsledkov**.

## 🎬 3. Praktické príklady vo videu

### **1. AI text na GPTZero.me**

Otvoríme `data/text-ai-vzor.txt`, vložíme jeho obsah do GPTZero, spustíme sken a zapíšeme skutočnú klasifikáciu.

### **2. Human vs. AI**

Účastník sám napíše dostatočne dlhý **autenticky ľudský text** a porovná výsledok s AI vzorkou. AI vzorku nevydávame za ľudskú.

### **3. Mixed dokument**

Spojíme vlastný ľudský odsek s AI odsekom a zaznamenáme hranice oboch častí.

### **4. AI Vision na sociálnych sieťach**

Nainštalujeme rozšírenie GPTZero a na vlastnom tréningovom príspevku ukážeme automatické označenie a manuálne skenovanie.

### **5. Detekcia na webových stránkach**

Použijeme Scan Selection alebo Scan Page na vlastnej testovacej podstránke, blogu či dlhšom článku.

### **6. GPTZero v Microsoft Worde**

**Home → Add-ins → More Add-ins → GPTZero → Add → Show GPTZero → Get Results**. Vysvetlíme minimálnu dĺžku označeného textu a rozdiel medzi odsekom a celým dokumentom.

### **7. Google Docs Writing Replay**

Vytvoríme vlastný Google Dokument, text postupne napíšeme, časť upravíme a vložíme pripravený odsek. Porovnáme záznamy Writing Report.

### **8. Plagiarism Check**

V podporovanom pláne preveríme podobnosť vlastného textu s dostupnými zdrojmi. Vysvetlíme, prečo **percento zhody ≠ percento plagiátorstva**.

### **9. Kontrola citácií a DOI**

V súbore `data/citacie-kontrola.md` preskúmame existujúci a zámerne fiktívny bibliografický záznam. Zistenia overíme v originálnych zdrojoch.

### **10. Vyhodnotenie experimentu bez API**

Z reálnych skenovaní vyplníme `data/vysledky-vzor.csv` a spustíme lokálny audit.

## 🧪 4. Spustenie lokálneho vyhodnotenia

**Windows PowerShell:**

```powershell
py -3 scripts/vyhodnotenie-gptzero.py --input data/vysledky-vzor.csv
```

**Ubuntu / Kali Linux / macOS:**

```bash
python3 scripts/vyhodnotenie-gptzero.py --input data/vysledky-vzor.csv
```

Skript nepotrebuje žiadnu externú knižnicu a neodosiela požiadavky na internet. Očakáva CSV stĺpce **id, skutocny_povod, predikcia** (ďalšie stĺpce sú voliteľné).

### Ako čítať výsledok

| Údaj | Význam |
|---|---|
| Záznamov v CSV | celkový počet testovacích vzoriek |
| Bez predikcie | vzorky, ktoré ešte neboli skenované |
| Zhodná klasifikácia | počet príkladov, kde predikcia zodpovedá známemu pôvodu |
| False positives (Human → AI) | nesprávne označenie ľudského textu ako AI |
| False negatives (AI → Human) | nesprávne označenie AI textu ako ľudského |
| Mixed / Uncertain | kategórie evidované samostatne |

**Pozor:** Percento vypočítané z niekoľkých cvičných vzoriek nepredstavuje všeobecnú presnosť GPTZero.

## 🧩 5. Laboratórne zadania na samostatnú prácu

1. [Základná detekcia](examples/01-zakladna-detekcia.md)
2. [Sociálne siete a web](examples/02-socialne-siete-web.md)
3. [Word a Google Dokumenty](examples/03-word-google-docs.md)
4. [Plagiátorstvo a citácie](examples/04-plagiatorstvo-citacie.md)
5. [Vyhodnotenie výsledkov](examples/05-vyhodnotenie-vysledkov.md)

Každé zadanie obsahuje cieľ, postup, očakávaný výstup a upozornenia na nesprávnu interpretáciu.

## 🧾 6. GPTZero Cheat Sheet

| Nástroj | Cesta alebo základná operácia |
|---|---|
| GPTZero Basic Scan | gptzero.me → vložiť text → Scan |
| GPTZero Advanced Scan | zvoliť rozšírenú analýzu podľa plánu |
| AI Vision | rozšírenie → AI Vision → Auto-scan my feed |
| Scan Selection | označiť text → menu rozšírenia |
| Word | Home → Show GPTZero → označiť text → Get Results |
| Google Docs | rozšírenie GPTZero → Watch Writing Report |
| Plagiarism Check | Dashboard → Plagiarism Check → Scan |
| Source / Fact Check | kontrola dostupná v Dashboarde alebo rozšírení podľa plánu |
| Offline výsledky | `python3 scripts/vyhodnotenie-gptzero.py` |

Podrobný [GPTZero Cheat Sheet](gptzero-cheatsheet.md).

## 🔒 7. Bezpečnosť, akademická etika a ochrana údajov

- **AI detekcia nie je dôkazom podvodu ani plagiátorstva.** Sú potrebné aj ďalšie nezávislé indície.
- **Textová podobnosť nie je automaticky plagiát.** Riadne citované pasáže sa môžu zhodovať s originálom.
- **Writing Replay nie je identifikácia osoby.** Hromadný paste nemusí znamenať využitie AI.
- **Neuverejňujeme výsledky o cudzích osobách bez kontextu.** Nezakladáme na nich automatické sankcie.
- **Chránime študentské a klientské dokumenty.** Pred uploadom preveríme podmienky spracúvania osobných údajov.
- **Niektoré funkcie sú platené.** Plány a kvóty kontrolujeme podľa aktuálnej dokumentácie.
- **Pracujeme s kontrolovanými vzorkami.** V repozitári je syntetický AI text, nie fiktívne označený „ľudský“ text.
- **Neukladáme do repozitára API kľúče ani neverejné dáta.**

## 📚 Užitočné odkazy

- GPTZero: https://gptzero.me/
- GPTZero Support: https://support.gptzero.me/
- Free vs. Paid: https://support.gptzero.me/articles/1272562776-what-is-the-difference-between-the-free-and-paid-for-planspricing
- Browser Extension: https://support.gptzero.me/articles/3430302841-what-is-the-origin-extension
- AI Vision: https://support.gptzero.me/articles/1675846160-ai-vision
- Microsoft Word Add-In: https://support.gptzero.me/articles/4982038962-How-can-I-get-the-Microsoft-Word-Add-In
- Google Docs Writing Report: https://support.gptzero.me/articles/7001890416-what-is-the-google-docs-writing-report-for-origin
- Plagiarism Check: https://support.gptzero.me/articles/1988519176-What-is-Plagiarism-Check
- AI Hallucinations / Fact Check: https://support.gptzero.me/articles/7953436668-what-are-ai-hallucinations-and-fact-check
- VITA Academy: https://www.vita.sk/

**Účel repozitára:** Naučiť účastníkov prakticky a zodpovedne používať GPTZero, rozumieť jeho výsledkom a preverovať texty bez zamieňania algoritmického odhadu za definitívny dôkaz.
