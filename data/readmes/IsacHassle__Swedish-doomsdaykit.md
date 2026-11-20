# Krislåda · Swedish-doomsdaykit

En krislåda för Mac som fungerar helt utan internet. När internet, mobilnätet eller elen ligger nere har du ändå:

- **Första hjälpen och sjukvård:** 29 akuta ämnen ett klick bort, medicinska uppslagsverk, fältsjukvårdsböcker och NHS läkemedelsguide
- **En AI du kan fråga på svenska**, som svarar ur krislådans böcker, visar källan och kan titta på foton
- **Karta över hela Sverige** ner till enskilda hus, med sökning på varje ort, gata och adress, och närmaste sjukhus, apotek, polis, dricksvatten, mat och bensin
- **Vad du gör i varje slags kris:** myndigheternas broschyr *Om krisen eller kriget kommer*, och guider för strålning, kemolyckor, strömavbrott, vinterstormar med mera
- **Mobiler på samma wifi kan använda allt.** Macen gör jobbet, inget internet behövs

Allt körs på din egen dator. Inget skickas någonstans.

| Startsidan | Fråga AI:n på svenska | Karta över hela Sverige |
|---|---|---|
| ![Startsidan med akuta ämnen](docs/screenshots/start-page.png) | ![AI:n svarar hur man håller lägenheten varm vid strömavbrott](docs/screenshots/ai.png) | ![Kartan med sökning, inzoomad på Södersjukhuset](docs/screenshots/map.png) |

## Ladda ner och installera

**Du behöver:** en Mac med Apple-chip (M1 eller nyare; se Apple-menyn → Om den här datorn → "Chip: Apple M…"), cirka **50 GB** ledigt utrymme, gärna 16 GB minne för AI:n, och internet medan den installeras. Installationen tar några timmar, mest nedladdning. Låt Macen vara på och ansluten till ström.

### Sätt 1: ladda ner och dubbelklicka

1. **[⬇️ Ladda ner Krislåda](https://github.com/IsacHassle/Swedish-doomsdaykit/releases/latest/download/Krislada.zip)** (cirka 11 MB).
2. Öppna **Hämtade filer** och dubbelklicka på **Krislada.zip**. Du får en mapp som heter **Krislåda**.
3. Öppna mappen och dubbelklicka på **Installera Krislåda.command**.
4. Macen säger troligen att den inte kan kontrollera filen, eftersom den inte kommer från App Store. Klicka **Klar**, öppna **Systeminställningar → Integritet och säkerhet**, scrolla ner och klicka **Öppna ändå** vid "Installera Krislåda.command". Bekräfta med ditt lösenord eller Touch ID.
5. Ett Terminal-fönster öppnas och visar hur det går. Krislådan flyttar sig själv till mappen **Krislåda** i din hemmapp.

### Sätt 2: en rad i Terminal

1. Öppna **Terminal** (tryck Cmd + mellanslag, skriv *Terminal*, tryck Enter).
2. Klistra in den här raden och tryck Enter:

```bash
curl -fsSL https://raw.githubusercontent.com/IsacHassle/Swedish-doomsdaykit/main/hamta.sh | bash
```

Krislådan hamnar i mappen **Krislåda** i din hemmapp.

### Bra att veta

- Om något avbryts: kör installationen igen (dubbelklicka igen eller klistra in raden igen). Den fortsätter där den slutade.
- Installationen hämtar allt från originalkällorna och kontrollerar varje bibliotek mot dess kontrollsumma. Den installerar **Ollama** och **AnythingLLM** (AI-apparna) om de saknas.
- Första gången AnythingLLM öppnas kan den visa en välkomstskärm. Klicka dig igenom den och kör installationen igen om den stannade där.
- Har du en äldre Mac eller lite utrymme: kör `./install.sh --utan-ai` i mappen, så får du allt utom AI:n (cirka 20 GB).
- När den är klar: **skriv ut `Krislåda - guide att skriva ut.pdf`**, och tryck **Skriv ut** på startsidan för första hjälpen, varningssignaler, vatten och värme från 1177, MCF och Livsmedelsverket (cirka 26 sidor). Lägg papperen hos din hemberedskap. Om Macen saknar ström är papperet det du fortfarande kan läsa.

---

Resten av sidan är bruksanvisningen. Samma text finns i utskriftsguiden, och AI:n har läst den.

## Börja här

1. Dubbelklicka på **Starta Krislåda.command** (i mappen Krislåda, eller genvägen **Krislåda** på skrivbordet). Den startar också AI-apparna Ollama och AnythingLLM i bakgrunden. Låt Terminal-fönstret som öppnas vara kvar.
2. **Startsidan** öppnas i webbläsaren på http://localhost:8091. Där finns:
    - **en sökruta** över alla bibliotek (engelska ord fungerar bäst, det finns en svensk knapp också)
    - **Fråga AI**: fråga AI:n på svenska, se guiden nedan
    - **Karta**: kartan över Sverige, med adressökning
    - **Var är jag?**: din position på kartan, med en USB GPS-mottagare i datorn
    - **Skriv ut**: det viktigaste från 1177, MCF och Livsmedelsverket på papper, att skriva ut medan det finns ström
    - **Checklista**: MCF:s lista för hemberedskap att bocka av, plus det krislådan själv behöver
    - **29 akutknappar**: hjärt-lungräddning, blödning, brännskador, nedkylning, kolmonoxid, förgiftning, förlossning med mera. De flesta öppnar 1177:s eller MCF:s råd på svenska, med den engelska artikeln ett tryck bort
    - **Svenska myndigheters råd**: 63 sidor från 1177, MCF, Livsmedelsverket och Krisinformation, sparade för läsning utan internet
    - **de 10 viktigaste böckerna** som PDF, och **alla dokument**
3. **Familjens mobiler:** anslut till samma wifi och öppna adressen som Terminal-fönstret visar, till exempel `http://Annas-MacBook-Air.local:8091` (samma adress varje gång, fungerar på iPhone) eller `http://192.168.1.23:8091` (kan ändras, fungerar överallt). Inget internet behövs. AI:n och kartan fungerar från mobilen också, Macen gör jobbet. Wifi-routern behöver ström: en router kopplad till en powerbank eller ett batteripaket räcker långt. Tips: tryck **Dela → Lägg till på hemskärmen** (iPhone) eller **⋮ → Lägg till på startskärmen** (Android), så får mobilen en Krislåda-ikon.

| Jag behöver... | Gör så här |
|---|---|
| Agera snabbt vid skada eller sjukdom | Startsidan → **Akut**-knapp. Ring **112** om någon telefon fungerar |
| Ställa en fråga på vanlig svenska | Startsidan → **Fråga AI**. Den svarar ur böckerna och visar källan |
| Fråga om ett foto (sår, utslag, växt, trasig sak) | **Fråga AI** → **Foto** |
| Fråga utan att skriva | Macens diktering: 🎤-tangenten, eller tryck Fn två gånger. På mobilen: mikrofonen på tangentbordet |
| Veta vad myndigheterna råder | Startsidan → *Om krisen eller kriget kommer* |
| Hitta en adress, närmaste sjukhus, apotek eller dricksvatten | Startsidan → **Karta** → sökrutan eller knapparna Sjukhus, Apotek och Vatten |
| Läsa av koordinater att skicka vidare | **Karta** → tryck på kartan |
| Höra viktiga meddelanden | Batteri- eller vevradio på **Sveriges Radio P4** |

Nummer: **112** nödsituation · **1177** sjukvårdsrådgivning · **113 13** information vid kris · **114 14** polisen, ej akut.

## Så använder du AI:n

AI:n körs helt på Macen. Öppna den från startsidan: **Fråga AI** (eller direkt på http://localhost:8091/ai/). Samma sida fungerar på familjens mobiler på wifi:t.

1. **Välj läge** under rubriken (flikarna Ur böckerna, Snabbt svar och Spara batteri):

    | Läge | Använd när | Tid |
    |---|---|---|
    | **Ur böckerna** | Det mesta: skador, sjukdom, läkemedel, vatten, mat, värme, myndigheternas råd. Den läser krislådans böcker (1177, MCF och Livsmedelsverket på svenska, sjukvårdsböcker, NHS läkemedelsfakta, vattenrening, mat, MCF-broschyren, Ready.gov-guiderna) och artiklar ur de stora medicinska biblioteken (WikiMed, MDWiki, MedlinePlus), och visar källorna under svaret. Tryck på en för att öppna den | Cirka 10 till 40 s |
    | **Snabbt svar** | När det är bråttom, eller för att fråga om ett **foto**. Samma stora AI, utan böckerna | Cirka 5 till 20 s |
    | **Spara batteri** | När Macen går på batteri och du inte vet när du kan ladda. Mindre AI, enklare svar, tar också foton | Snabbare, lättare |

2. **Skriv som när du ringer 1177.** Vem (ålder, vikt för barn), vad som hände, när, vad du ser, vad du har hemma. Exempel: *Min pappa är 72 år. Han föll i trappan för 20 minuter sedan och slog i huvudet. Han blöder lite från pannan och verkar förvirrad. Vi har plåster, kompresser och Alvedon. Vad ska vi göra?*
3. **Fortsätt fråga.** Den minns samtalet ("Vad gör jag om det blir värre?", "Förklara steg 3 enklare"). Tryck **Ny konversation** när du byter ämne.
4. **Foton:** tryck **Foto**. Bra ljus, nära, en sak per bild, och skriv vad du undrar.
5. **Prata i stället för att skriva:** Macens diktering (🎤-tangenten, eller Fn två gånger), eller mikrofonen på mobilens tangentbord.
6. **Kontrollera det viktiga.** AI kan ha fel. Öppna källan under svaret, särskilt för doser. Ät aldrig en svamp eller växt för att AI:n säger att den är ätlig.
7. **Spara ström:** AI:n drar mycket ström medan den svarar. Ställ få och tydliga frågor, välj Spara batteri, stäng andra appar.
8. **Om det inte fungerar** visar raden högst upp på AI-sidan vad som saknas: öppna appen **Ollama** för AI-motorn, eller appen **AnythingLLM** för böckerna (utan den svarar Ur böckerna bara ur biblioteken). Första svaret efter start tar längre tid medan AI:n laddas.

Livsfara går först: ring **112** om någon telefon fungerar, och använd **Akut**-knapparna i stället för att vänta på ett svar från AI:n.

### Andra sätt att använda samma AI på Macen

| Var | Modell | När |
|---|---|---|
| Appen **AnythingLLM**, arbetsytan **Crisis** | Gemma 4 26B via Ollama | Svarar ur böckerna, men inte ur WikiMed, MDWiki och MedlinePlus. Du kan dra in egna filer där |
| Appen **Ollama**, modellen **crisis** | Gemma 4 26B med krisinstruktionerna inbyggda | Samma som Snabbt svar. Dra in ett foto i rutan för att fråga om det |
| Appen **Ollama**, modellen **crisis-small** | Gemma 4 E4B, samma instruktioner | Samma som Spara batteri |
| Terminal: `ollama run crisis` | | Skriv frågan, `/bye` för att avsluta |

Instruktionerna som AI:n följer finns i `config/AI-PROMPT.txt`.

## Vad finns i krislådan, och varför

Cirka 45 GB totalt: 14 GB bibliotek, 4,5 GB kartor, 1 GB dokument, 27 GB AI-modeller. Den täcker det som spelar roll först när vardagen slutar fungera: att hålla människor vid liv, sedan vatten, värme, mat och information, sedan att hitta rätt.

### 1. Sjukvård: den viktigaste delen

När ambulansen dröjer eller inte går att nå avgör rätt första hjälpen hur det går. Flera källor finns med eftersom var och en täcker olika saker, och det är viktigt att kunna jämföra.

| Bibliotek | Varför det finns med |
|---|---|
| Medical Library | Böcker skrivna för när det inte finns någon läkare: Where There Is No Doctor, Survival and Austere Medicine, Emergency War Surgery, A Book for Midwives, Where There Is No Dentist |
| Military Medicine | Trauma: stoppa blödning, spjäla, nödförlossning, ta hand om någon i flera dagar med lite material |
| WikiMed och MDWiki | Medicinska uppslagsverk med bilder: symtom och sjukdomar, känna igen utslag, bett, skador |
| MedlinePlus | Lättläst information om hälsa och läkemedel från USA:s nationalbibliotek för medicin |
| NHS Medicines A to Z | Vad ett läkemedel är till för, biverkningar, vem som inte får ta det |
| CDC Health Information | Smittsamma sjukdomar och utbrott: hur sjukdom sprids, hur man skyddar ett hushåll |

### 2. Vatten, mat, skydd och varje slags kris

Man klarar sig veckor utan mat men bara dagar utan vatten.

| Bibliotek | Varför det finns med |
|---|---|
| Water Treatment Library | Koka, filtrera och rena vatten kemiskt |
| Food for Preppers | Förvara mat och laga mat utan el eller vanliga råvaror |
| Post Disaster Resource Library | Skydd, sanitet och återuppbyggnad efter en katastrof, plus SAS Survival Handbook |
| Low-tech Magazine | Värme, matlagning och vardag med lite eller ingen el |
| Ready.gov (USA:s FEMA) | Steg-för-steg-guider som den svenska broschyren inte går in på: strålning, kärnvapenexplosion, kemolyckor, explosioner, långa strömavbrott, vinterväder, pandemier. AI:n läser guiderna och FEMA:s handbok "Are You Ready?" |
| A Library of Knots | Knopar för skydd, surrning och bärande |

### 3. Svenska myndigheters råd och information

| Innehåll | Varför det finns med |
|---|---|
| 1177: första hjälpen och skador | Hjärt-lungräddning på vuxna och barn, stabilt sidoläge, luftvägsstopp, blödning, chock, allergisk chock, förgiftning, brännskador, köldskador, sår, hjärnskakning, huggorms- och fästingbett med mera, på svenska. Akutknapparna öppnar dem direkt |
| MCF: hemberedskap, varningar, skyddsrum | Vatten, värme, mat, medicin, kommunikation och kontanter för en vecka; VMA och Hesa Fredrik, varning kring kärnkraftverk, skyddsrum, utrymning, höjd beredskap, brand, översvämning, värmebölja |
| Livsmedelsverket | Dricksvatten i dunk, laga mat utan el, matförråd |
| MCF:s broschyr, på svenska och engelska | Myndigheternas råd: hemberedskap, varningssignaler, vad samhället förväntar sig av dig |
| Svenska Wikipedia | Inledningen av varje artikel: svenska platser, växter, djur, svampar och nästan allt annat |

### 4. Kartan

En offline-karta över hela Sverige (med delar av Norge, Finland och Danmark i samma ram) och en översikt över världen, från OpenStreetMap. Ortnamnen är på svenska. Den har de gator, hus, stigar och husnummer som finns i OpenStreetMap, och du kan zooma in på enskilda hus.

- **Sök** efter vilken ort, by, gata eller adress som helst i Sverige, till exempel *Hornsgatan 50* eller *Storgatan 30, Umeå*. Saknas ett husnummer i OpenStreetMap sätts nålen mellan grannhusen, och kartan säger att läget är ungefärligt.
- **Närmaste**-knapparna listar de närmaste sjukhusen, vårdcentralerna, apoteken, polisstationerna, brandstationerna, dricksvattenställena, matbutikerna och bensinstationerna från kartans mitt.
- Knapparna **Stockholm** och **Sverige** hoppar dit.
- **Var är jag?** visar din position på kartan, följer med när du rör dig, och då räknar närmaste-knapparna från där du står ("1,2 km från dig"). Det fungerar helt utan internet, men **Macen har ingen egen GPS**: koppla in en **USB GPS-mottagare**. Sök efter "USB GPS" (de flesta har en u-blox-krets och kostar cirka 200–400 kr), och skaffa en USB-C-adapter om datorn bara har USB-C. Krislådan hittar mottagaren själv, inga drivrutiner behövs. Första gången kan den behöva några minuter vid ett fönster eller utomhus för att hitta satelliterna. Utan mottagare: sök på en gata, adress eller plats du ser omkring dig.
- **Ingen USB-mottagare? Låt mobilen vara datorns GPS.** Varje mobil har en riktig GPS som fungerar utan internet. Ställ in mobilen en gång (öppna `/mobil/` på mobilen och följ stegen för iPhone eller Android), tryck sedan **Dela min position med Macen** och låt sidan vara öppen. Då visar Macens karta var du är när du trycker ⌖ (Var är jag?). Krislådan gör ett eget certifikat för det, som bara gäller adresser i ditt hemnätverk och inte kan användas för webbplatser på internet.
- **Tryck** på kartan för att läsa av exakta koordinater, som du kan skicka vidare via radio eller skriva ner.

### 5. Fler bibliotek, om du har plats

`config/libraries.txt` listar extra bibliotek som du slår på genom att ta bort `#` framför dem och köra `bash scripts/download-library.sh`: Svenska Wikipedia i sin helhet med bilder (17 GB), engelska Wikipedia (13 GB, eller 49 GB i sin helhet), iFixits reparationsguider, och frågor och svar om husreparationer, bilar, odling, matlagning, friluftsliv och amatörradio. Kör `bash scripts/get-documents.sh` och `bash scripts/embed-documents.sh` efteråt om du lägger till bibliotek med böcker i.

## Lägg till egna dokument

Lägg filer i krislådans mapp `documents/` (kontaktlistor, läkemedelslistor, försäkringspapper, manualer till elverk eller vattenfilter) och kör `bash scripts/embed-documents.sh`. Då kan AI:n svara ur dem också. Du kan också dra in filer direkt i arbetsytan Crisis i AnythingLLM. Dina egna dokument lämnar aldrig Macen.

## Mappar

| Sökväg | Innehåll |
|---|---|
| `Installera Krislåda.command` | Installerar eller lagar allt |
| `Starta Krislåda.command` | Dubbelklicka för att starta allt |
| `Kontrollera Krislåda.command` | Dubbelklicka för att kontrollera att allt fungerar |
| `config/` | `libraries.txt` (vilka bibliotek), `swedish-pages.txt` (vilka myndighetssidor), `AI-PROMPT.txt` (AI:ns instruktioner), `document-names.json` (boktitlar) |
| `scripts/` | `share-library.sh` (start), `serve-web.py` (webbservern, och kopplingen mellan AI-sidan och Ollama/AnythingLLM), `kit_search.py` (det AI:n läser i Ur böckerna), `build-home.py` (startsidan), nedladdningsstegen `get-*.sh`, `setup-ai.sh`, `embed-documents.sh`, `extract-documents.py`, `fetch-swedish-pages.py` (myndigheternas råd), `update-libraries.sh`, `kontroll.sh`, `make-cert.sh` (https för mobilens GPS), `build-map-index.py` (kartans sökning) |
| `web/` | Startsidan, AI-sidan (`web/ai/`), kartan (`web/map/`), läsaren för textdokument (`web/las/`), utskriftspaketet (`web/skriv-ut/`), checklistan (`web/checklista/`) och GPS-inställningen för mobiler (`web/mobil/`) |
| `library/` | Biblioteken (.zim-filer), nedladdade. Appen Kiwix kan också öppna dem |
| `documents/` | MCF-broschyren, och `library/` med varje bok som PDF, namngiven efter titel |
| `maps/` | Kartfilerna för Sverige och världen |
| `tools/`, `logs/` | Hjälpprogram och loggar |

## Håll den uppdaterad

Några gånger om året, med internet: kör `bash scripts/update-libraries.sh`. Den hämtar de senaste versionerna av biblioteken och myndigheternas sidor, tar bort de gamla versionerna och läser in nya böcker i AI:n. Det är alltid säkert att köra igen: färdiga filer hoppas över och avbrutna fortsätter. Startsidan bygger om sig själv varje gång du startar krislådan. `git pull` (eller en ny nedladdning) ger dig den senaste versionen av själva krislådan.

Om Kiwix har tagit bort en version som står i listan hämtar installationen automatiskt den senaste versionen av samma bibliotek, så krislådan går att installera även om några år.

Kartans sökning kan byggas om från färsk OpenStreetMap-data med `scripts/build-map-index.py` (kräver `brew install osmium-tool` och `maps/osm/sweden-latest.osm.pbf` från download.geofabrik.de).

**En gång i månaden:** stäng av wifi och dubbelklicka på **Kontrollera Krislåda.command**. Den går igenom bibliotek, kartor, dokument och AI (den ställer en testfråga) och visar ✅ eller ⚠️ för varje del, med vad du ska göra om något saknas.

## Gör också detta

- Installera **Organic Maps** på mobilen och ladda ner Sverige: en andra karta som klarar sig i dagar på en powerbank.
- Installera **Kiwix** på mobilen och kopiera över de medicinska biblioteken.
- Skaffa en batteri- eller vevradio för P4, och en powerbank eller ett batteripaket för Macen.
- Skaffa en **USB GPS-mottagare** till datorn (cirka 200–400 kr), så visar kartan var du är utan internet. Testa den en gång med Var är jag? på kartan.

## Tack och licenser

Krislådans egen kod har MIT-licens (`LICENSE`). Biblioteken, kartorna, broschyrerna och AI-modellerna hämtas från sina originalkällor och har sina egna licenser, se `CREDITS.md`. Inspirerad av [Project N.O.M.A.D.](https://github.com/Crosstalk-Solutions/project-nomad).

Krislådan är inte medicinsk rådgivning och ersätter inte räddningstjänsten. Vid nödsituation, ring 112.

## In English

Krislåda is an offline crisis kit for Sweden on a Mac with Apple Silicon: medical libraries and 29 one-tap emergency topics, a local AI (Ollama and AnythingLLM) that answers in Swedish from the kit's books and medical libraries and can look at photos, an offline map of all of Sweden with search for every town, street and address, and the official Swedish brochure *In case of crisis or war*. Phones on the same Wi-Fi can use it too. Install with the one line above (or download `Krislada.zip` and double-click `Installera Krislåda.command`); it needs about 50 GB and a few hours of downloading, then works with no internet. Sources and licences are in `CREDITS.md`.
