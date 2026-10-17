<div align="center">

***Česky** · [English](README.en.md)*

<img src="docs/header.jpg" alt="Video Director" width="820">

# 🎬 Video Director

### Skill pro Claude Code, který natočí celé video na tvém vlastním počítači

**Plán · Reference · Záběry · Kontrola · Opravy · Dabing · Upscale · Sestřih**

Zadáš scénář. Claude z něj naplánuje scény, vyrobí reference postav a prostředí,
natočí všechny záběry na tvém ComfyUI, **sám se na ně podívá**, ohodnotí je,
přetočí ty, které neprošly, a nakonec je sestříhá do hotového videa.

![Claude Code](https://img.shields.io/badge/Claude%20Code-skill-D97757)
![ComfyUI](https://img.shields.io/badge/ComfyUI-lokálně-1a1a2e)
![Licence](https://img.shields.io/badge/licence-MIT-blue)
![Cloud](https://img.shields.io/badge/cloud-0%20%25-success)

</div>

---

## Co to dělá

Většina nástrojů umí vygenerovat **jeden** hezký záběr. Problém začne u druhého:
jiná tvář, jiné oblečení, jiné světlo, jiný hlas. Tenhle skill řeší přesně tohle.

Pracuje ve smyčce, kterou zná každý štáb:

```
ZADÁNÍ → PLÁN → BIBLE POSTAV A PROSTŘEDÍ → STORYBOARD → REFERENCE
→ KLÍČOVÉ SNÍMKY → ZÁBĚRY → KONTROLA → OPRAVY → DABING → UPSCALE → SESTŘIH
```

Klíčová část je **kontrola**. Po každém záběru se vytáhnou snímky a kontaktní
list, Claude se na ně podívá a oboduje identitu, prostředí, návaznost, pohyb
a artefakty. Co spadne pod práh, se přetočí — a mění se jen to, co selhalo,
ne celý prompt. Stav projektu je v `project.json`, takže výroba přežije
restart počítače i novou konverzaci.

## Co to umí

| | |
|---|---|
| **Obrázky z textu** | Z-Image Turbo, FLUX.2 Klein — reference postav, prostředí, rekvizit |
| **Stejná postava z jiného úhlu** | Qwen Image Edit + Multiple Angles |
| **Změna oblečení bez ztráty obličeje** | Krea 2 + Identity Edit |
| **Otočný list postavy** | 6 pohledů z jedné fotky (MiniMax H3) |
| **Záběry** | MiniMax H3 — z textu, z klíčového snímku, z referencí, s přesným lip-syncem |
| **Navázání delší scény** | prodloužení hotového záběru přes poslední snímek |
| **Mluvené slovo** | nativní zvuk H3 včetně češtiny, nebo klonovaný hlas přes Higgs Audio |
| **Zvětšení** | SeedVR2 (kvalitně) nebo RTX Video SR (rychle) |
| **Sestřih** | ffmpeg — střihy, hudba pod dialogem, výstup 1080p |

Zvuk vzniká **rovnou v modelu** — motor, kroky, vítr i repliky. Není to
podložená stopa z knihovny.

## Jak to vypadá v praxi

Reklamní spot o 51 sekundách, jedenáct záběrů, dvě a půl hodiny generování
na jedné kartě s 16 GB VRAM. Zadání mělo pět vět; kamera, tempo a ruchy
vznikly cestou. Ta samá herečka a to samé auto ve všech záběrech drží pěti
referenčními obrázky a zvukovou referencí hlasu.

## Co potřebuješ

- **Claude Code** ([claude.com/claude-code](https://claude.com/claude-code))
- **ComfyUI** s modely MiniMax H3, Z-Image Turbo a dalšími podle toho, co chceš
  používat — workflow šablony najdeš v [PocketComfy](https://github.com/Promptlab37/PocketComfy)
- **Python 3.10+** a `ffmpeg`/`ffprobe` na PATH
- **Grafická karta** — doporučeno 16 GB VRAM, a hlavně **64 GB+ RAM**:
  jeden běh MiniMax H3 si drží zhruba 50 GB v operační paměti

## Instalace

Podrobně v [INSTALACE.md](INSTALACE.md), ve zkratce:

```bash
git clone https://github.com/Promptlab37/VideoDirector.git
cp -r VideoDirector ~/.claude/skills/video-director
```

Pak nastav proměnné prostředí podle svého počítače:

```bash
export COMFY_ROOT="/cesta/ke/ComfyUI"     # kořen instalace ComfyUI
export WORKFLOWS="/cesta/k/workflows"     # složka s workflow šablonami
export FILMY="/cesta/k/filmum"            # kam se zakládají projekty
export COMFY_URL="http://127.0.0.1:8188"  # volitelné, tohle je výchozí
```

A v Claude Code řekni:

> natoč mi video podle tohohle scénáře: …

## Co v tom je

```
SKILL.md                      hlavní instrukce pro Claude
reference/
  workflows.md                které workflow, které uzly, jaké hodnoty
  prompt-format.md            formát promptů pro MiniMax H3
  prompty-modelu.md           jak promptuje který model podle jeho autorů
  cesky-dialog.md             pravidla pro český dialog a držení hlasu
  qa-and-retry.md             kontrola výsledků a strategie oprav
scripts/director.py           CLI nad ComfyUI (generování, kontrola, sestřih)
```

Nejcennější část nejsou skripty, ale **`reference/`** — je v nich sepsané,
co se v praxi pokazilo a proč. Například že zápor do promptu nepatří u žádného
z těch modelů, že konec řeči se čte z obálky signálu a ne z přepisu, nebo
že co reference postavy neukazuje, si model v každém záběru domyslí jinak.

## Co to neumí

- **Nestahuje modely.** Počítá s tím, že ComfyUI máš funkční a modely v něm.
- **Nemění workflow šablony**, jen do nich dosazuje hodnoty.
- **Čeština u MiniMax H3 není mezi stabilními jazyky.** Funguje, ale každou
  repliku je potřeba změřit; postup je v `reference/cesky-dialog.md`.
- **Není to jednominutová záležitost.** Jeden záběr je řádově deset minut
  generování. Půlminutové video je několik hodin.
- Hodnocení kvality je odhad ze statických snímků. Poslední slovo má člověk.

## MiniMax H3 — licence modelu

Kód v tomto repozitáři je pod licencí MIT. **Model MiniMax H3 pod MIT není**
a MIT se na něj nevztahuje.

Když tenhle skill použiješ s MiniMax H3, řídí se model i jeho výstupy licencí
**MiniMax H3 Community License Agreement** a její přílohou **Acceptable Use
Policy (Exhibit A)**. Používáním se zavazuješ je dodržovat.

Na co si dát pozor především:

- **Územní omezení.** Licence platí celosvětově *s výjimkou* Evropské unie,
  Spojeného království, Korejské republiky a Spojených států. Jsi-li v některé
  z nich, potřebuješ vlastní autorizaci od MiniMaxu — autorizace vydaná autorovi
  tohoto repozitáře se na tebe nevztahuje.
- **Komerční použití.** U komerčního produktu nebo služby musíš v uživatelském
  rozhraní viditelně uvádět „MiniMax H3".
- **Označování výstupů.** Obsah zveřejňovaný na veřejnosti je potřeba jasně
  a viditelně označit jako strojově vytvořený.
- **Předávání dál.** Když nástroj někomu poskytneš, musíš ho zavázat pravidly
  nejméně stejně přísnými a upozornit ho, že platí.

Plné znění licence:
<https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE>

Podezření na porušení nahlaš přes Issues v tomto repozitáři.

## Související

- **[PocketComfy](https://github.com/Promptlab37/PocketComfy)** — Android
  klient k tomu samému ComfyUI serveru; jsou v něm i workflow šablony,
  které tenhle skill používá.

## Licence

Kód: MIT — viz [LICENSE](LICENSE).

Model MiniMax H3 pod MIT nespadá — viz [NOTICE](NOTICE) a oddíl výše.
