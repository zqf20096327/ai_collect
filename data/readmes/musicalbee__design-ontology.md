<div align="center">

# design-ontology

### Your agent has no taste. Give it a style it can execute.

**<!-- n:styles -->551<!-- /n --> styles in <!-- n:domains -->16<!-- /n --> domains, as data. Each one compiles into a skill that any coding agent can load.**<br>
Bauhaus to visionOS. JSON in, `SKILL.md` + `tokens.css` out. No runtime, no API key, no lock-in.

[![validate](https://github.com/musicalbee/design-ontology/actions/workflows/validate.yml/badge.svg)](https://github.com/musicalbee/design-ontology/actions/workflows/validate.yml)
![styles](https://img.shields.io/badge/styles-551-111111)
![domains](https://img.shields.io/badge/domains-16-111111)
![code](https://img.shields.io/badge/code-MIT-111111)
![data](https://img.shields.io/badge/data-CC%20BY%204.0-111111)
![PRs](https://img.shields.io/badge/PRs-one%20JSON%20file-E30613)

<a href="https://musicalbee.github.io/design-ontology/demo/"><img src="assets/showreel.gif" width="640" alt="Showreel: fast cuts across 536 styles in 16 domains, material close-ups, and a lineage route from a Victorian lamp to punk in 3 hops"></a>

[**Live demo**](https://musicalbee.github.io/design-ontology/demo/) · [Skill index](skills/SKILL_INDEX.md) · [Add a style](#add-a-style) · [The schema](schema/domains/internet.schema.json)

</div>

---

Ask an agent for "a neo-brutalist landing page" and you get rounded cards, a soft grey shadow and a purple gradient. The model knows the word. It does not know the rules.

This repository holds the rules. A style here is not a mood board and not a paragraph of adjectives. It is a record with a thesis, numbered directives, a list of things that break it, five scores, a palette, a type system and a set of CSS tokens. A compiler turns each record into a file your agent reads before it writes a line of code.

```text
- **NEVER:** Blurred drop shadows with a blur radius above 0px.
- **NEVER:** Subtle grey gradients or glossy highlights on surfaces.
- **NEVER:** Pastel, low-saturation fills with grey text.
```

That is three lines of [`skills/neo-brutalism-ui/SKILL.md`](skills/neo-brutalism-ui/SKILL.md). The agent gets them, plus `--shadow-elevation: 4px 4px 0 0 #000000`, plus the Tailwind classes for a button that presses into the page.

## Try it in 30 seconds

No install. Take one file.

**Claude Code**

```bash
mkdir -p .claude/skills/neo-brutalism-ui && curl -fsSL https://raw.githubusercontent.com/musicalbee/design-ontology/main/skills/neo-brutalism-ui/SKILL.md -o .claude/skills/neo-brutalism-ui/SKILL.md
```

**Cursor**

```bash
mkdir -p .cursor/rules && curl -fsSL https://raw.githubusercontent.com/musicalbee/design-ontology/main/skills/neo-brutalism-ui/SKILL.md -o .cursor/rules/neo-brutalism-ui.mdc
```

**Any other agent** (Windsurf, Cline, Codex, a LangGraph node, a system prompt): paste the contents of a `SKILL.md` into the context. Each file stands alone and needs no other file.

Then say: *"Build a pricing page in neo-brutalism."*

**Let the agent choose.** Give it [`skills/SKILL_INDEX.md`](skills/SKILL_INDEX.md). That one small table routes a request to a style by trigger words, use case, mood and vector score. The agent loads the full skill only after it has picked.

## What is in a style

| Section | What the agent gets |
|---|---|
| **Philosophy** | One thesis, 4 to 10 directives it can execute, 4 to 10 anti-patterns it must not ship |
| **Vectors** | Five integer scores, 1 to 5: ornamentation, dimensionality, grid rigidity, skeuomorphic realism, typographic expressiveness |
| **Layout** | Grid mechanics, whitespace ratio, alignment, container geometry, with numbers |
| **Typography** | Type classes, open-source font pairings, tracking, leading, hierarchy rules |
| **Colour** | Palette with hex and role, contrast rules, surface treatment, light and shadow |
| **Materiality** | What the surface imitates, border rules, blur and elevation in px |
| **Ornament** | Icon stroke, illustration rules, decorative elements |
| **Motion** | Physics, a CSS easing function, a duration, hover and active states |
| **Lineage** | Where it came from, what it rejects, what it mixes with |
| **Emotion** | Target response, keywords, brand archetypes |
| **Agent routing** | Trigger words, use cases, when not to use it, and where to go for "softer" or "bolder" |
| **Visual** | Type treatment, icon treatment, a hero picture recipe, a pattern and a page layout |
| **Tokens** | 16 required CSS custom properties and Tailwind patterns for common elements |

Every style fills the same 16 tokens. So a style is a drop-in replacement for another style: change `data-style="flat-design"` to `data-style="glassmorphism"` and the page changes its skin. The [live demo](https://musicalbee.github.io/design-ontology/demo/) is that one trick, 17 times: one landing page, "Grow your taste", that wears each style in turn.

The compiler adds two things to each style:

- **A text colour for each field.** An author writes `--color-text` for the main field only. The compiler derives `--color-on-bg`, `--color-on-surface`, `--color-on-primary`, `--color-on-accent`, two muted colours and two link colours. Each one reaches 4.5 to 1 on its field, or the compiler replaces it.
- **A visual pack.** `skills/<id>/pack/hero.svg` is a hero picture in the style. `pattern.svg` is a tile that repeats. `icons.svg` is a sprite of 14 icons, cut from an open-source icon family that fits the style.

## Weights: each style has a budget

Weight is an accent, and a style decides how much of it to spend. `visual.type` gives a weight to five roles: display, subhead, body, bold in text, and labels. It also names where the accent lives: in weight, size, case or colour.

- **Few weights, far apart.** Bauhaus and Swiss use 400 and 700 and no other. The hierarchy comes from size.
- **A light display.** Flat design and Frutiger Aero set the headline at 300, lighter than the body. Size and colour carry it, and bold goes to the buttons.
- **A heavy floor.** Text on glass starts at 500, because a thin stem breaks up on a blurred field.
- **One weight in the display face.** A poster face such as Shrikhand has one weight. The contrast comes from the face and the size, and the bold lives in the text face.

The compiler writes the roles as tokens: `--display-weight`, `--subhead-weight`, `--body-weight`, `--strong-weight`, `--label-weight`. A weight must exist in its face: the display face for display and subhead, the text face for the other three.

## Icons: a rule, and a stand-in

A style does not own an icon set. It owns a rule for the choice of one. `icons/principles.json` holds the eight rules, and each `SKILL.md` carries them: the stroke matches the stem of the text face, the terminals follow the radius token, the fill mode follows the technology of the era, one family on one grid, and the licence permits the use.

Each style names the open-source family that the rules select for it, in `visual.icon.pack`, with the reason. Bauhaus takes Material Symbols Sharp. Neo-brutalism takes Phosphor Bold. Y2K takes Pixelarticons. `npm run icons` vendors 14 icons of each family into `icons/packs/`, with the licence, and the build cuts the sprite from that file. [icons/README.md](icons/README.md) lists each family, its author and its licence.

The open-source families are a stand-in for the demo. A product with a brand uses its licensed icon library and applies the same rules to choose the family and the weight.

## The lineage graph

Styles do not appear from nowhere. Flat design rejects skeuomorphism. Neumorphism rejects flat design. Neo-brutalism rejects the friendly corporate look that flat design became. The graph records these edges, so that an agent asked for "the same, but softer" moves to a named neighbour and does not improvise.

**[Open the interactive lineage graph](https://musicalbee.github.io/design-ontology/demo/graph.html)**: all styles on one time line, a lane for each domain. Select a style to see its edges and open it in its domain demo.

<details>
<summary>The same graph as Mermaid (wide)</summary>

Solid arrows show descent. Red dotted arrows show rejection. Grey dotted arrows show kinship across domains.

<!-- lineage:start -->
```mermaid
flowchart LR
  subgraph internet_terminals_bbs["Terminals, BBS and Usenet · 1969–1993"]
    cassette_futurism["Cassette Futurism"]
    punk_zine["Punk Zine"]
    usenet_thread["Usenet Thread"]
    memphis_design["Memphis Design"]
    ansi_bbs_art["ANSI BBS Art"]
    kaomoji_emoticon["Kaomoji and Emoticon"]
    cyberdelia["Cyberdelia"]
    grunge_editorial["Grunge Editorial"]
  end
  subgraph internet_web_1["Web 1.0 · 1994–2003"]
    net_art_browser["Net Art Browser"]
    geocities_homepage["GeoCities Homepage"]
    bulletin_board_forum["Bulletin Board Forum"]
    portal_table_layout["Portal Table Layout"]
    y2k_aesthetic["Y2K Aesthetic"]
    flash_intro_site["Flash Intro Site"]
    japanese_dense_web["Japanese Dense Web"]
    apple_aqua["Apple Aqua"]
    anonymous_imageboard["Anonymous Imageboard"]
    myspace_profile["Myspace Profile"]
  end
  subgraph internet_web_2_social["Web 2.0 and the social web · 2004–2011"]
    demotivational_poster["Demotivational poster"]
    frutiger_aero["Frutiger Aero"]
    web_2_0_gloss["Web 2.0 Gloss"]
    reddit_thread["Reddit Thread"]
    impact_image_macro["Impact image macro"]
    unboxing_video["Unboxing Video"]
    skeuomorphism["Skeuomorphism"]
    rage_comic["Rage comic"]
    reaction_gif["Reaction GIF"]
    asmr_video["ASMR Video"]
    glitch_gif["Glitch GIF"]
    instagram_vintage_filter["Instagram Vintage Filter"]
    lets_play_facecam["Let's Play Facecam"]
    metro_ui["Metro UI"]
    pixel_art_web["Pixel Art Web"]
    unicode_emoji["Unicode Emoji"]
    wojak_feels["Wojak and feels"]
    chat_sticker_pack["Chat Sticker Pack"]
    cinemagraph["Cinemagraph"]
    livestream_overlay["Livestream Overlay"]
    seapunk["Seapunk"]
  end
  subgraph internet_feed_mobile["The feed and the phone · 2012–2019"]
    utopian_virtual["Utopian virtual"]
    bohemian_web["Bohemian Web"]
    clickbait_thumbnail["Clickbait Thumbnail"]
    flat_design["Flat Design"]
    mallsoft["Mallsoft"]
    minimalism_web["Minimalism Web"]
    tumblr_soft_grunge["Tumblr Soft Grunge"]
    vaporwave["Vaporwave"]
    cyberpunk_web["Cyberpunk Web"]
    future_funk["Future funk"]
    health_goth["Health Goth"]
    normcore["Normcore"]
    synthwave_web["Synthwave Web"]
    vsco_preset_look["VSCO Preset Look"]
    brutalist_web["Brutalist Web (2014)"]
    flat_lay_feed["Flat Lay Feed"]
    luxury_typography_web["Luxury Typography Web"]
    material_design["Material Design"]
    starter_pack["Starter pack"]
    video_essay["Video Essay"]
    blob_world["Blob World"]
    conceptual_sketch_ui["Conceptual Sketch UI"]
    deepdream_psychedelia["DeepDream Psychedelia"]
    discord_server["Discord Server"]
    tweet_screenshot_meme["Tweet screenshot meme"]
    wabi_sabi_web["Wabi-Sabi Web"]
    anti_design["Anti-Design"]
    cohesive_feed_grid["Cohesive Feed Grid"]
    dark_devtool_ui["Dark-Mode Developer Tool"]
    lip_sync_dance_short["Lip-Sync Dance Short"]
    surreal_meme["Surreal meme"]
    surrealism_web["Surrealism Web"]
    vtuber_avatar["VTuber Avatar"]
    3d_avatar_emoji["3D Avatar Emoji"]
    corporate_memphis["Corporate Memphis"]
    deep_fried_meme["Deep-fried meme"]
    deepfake_face_swap["Deepfake Face Swap"]
    label_meme["Label meme"]
    terminal_tui_web["Terminal / TUI Web"]
    aurora_gradient_ui["Aurora Gradient UI"]
    cottagecore["Cottagecore"]
    duet_split_screen["Duet Split-Screen"]
    gan_portrait["GAN Portrait"]
    scrapbook_ui["Scrapbook UI"]
    dark_academia["Dark academia"]
    dreamcore["Dreamcore"]
    glitchcore["Glitchcore"]
    grwm_short["Get Ready With Me"]
    hyperpop_visual["Hyperpop Visual"]
    kidcore["Kidcore"]
    liminal_spaces["Liminal spaces"]
    neumorphism["Neumorphism"]
  end
  subgraph internet_short_video_ai["Short video and AI · 2020–now"]
    cybercore_web["Cybercore Web"]
    glassmorphism["Glassmorphism"]
    goblincore["Goblincore"]
    green_screen_short["Green-Screen Short"]
    neo_brutalism_ui["Neo-Brutalism UI"]
    photo_dump["Photo Dump"]
    pov_short["POV Short"]
    velocity_edit["Velocity Edit"]
    weirdcore["Weirdcore"]
    word_caption_clip["Word Caption Clip"]
    claymorphism["Claymorphism"]
    editorial_serif_revival["Editorial Serif Revival"]
    ethereal_web["Ethereal Web"]
    ai_avatar_portrait["AI Avatar Portrait"]
    ai_chat_ui["AI Chat Interface"]
    barbiecore["Barbiecore"]
    bento_grid_ui["Bento Grid UI"]
    clean_girl["Clean girl"]
    diffusion_gloss["Diffusion Gloss"]
    dual_camera_snapshot["Dual Camera Snapshot"]
    mini_diffusion_meme["Mini-Diffusion Meme"]
    photo_carousel_slideshow["Photo Carousel Slideshow"]
    spatial_visionos["Spatial UI (visionOS)"]
    ai_slop["AI Slop"]
    liquid_glass_ui["Liquid Glass"]
  end
  subgraph architecture_medieval["Architecture · Medieval · 1200–1520"]
    gothic_architecture["Gothic"]
  end
  subgraph architecture_early_modern["Architecture · Early Modern · 1420–1750"]
    renaissance_architecture["Renaissance"]
    baroque_architecture["Baroque"]
  end
  subgraph architecture_revival_and_academy["Architecture · Revival and Academy · 1750–1914"]
    neoclassical_architecture["Neoclassicism"]
    arts_and_crafts_architecture["Arts and Crafts"]
    beaux_arts_architecture["Beaux-Arts"]
  end
  subgraph architecture_fin_de_siecle["Architecture · Fin de Siècle · 1885–1914"]
    art_nouveau_architecture["Art Nouveau"]
    prairie_school_architecture["Prairie School"]
    organic_architecture["Organic Architecture"]
    expressionist_architecture["Expressionist Architecture"]
  end
  subgraph architecture_modern_movement["Architecture · Modern Movement · 1919–1975"]
    bauhaus_architecture["Bauhaus Architecture"]
    art_deco_architecture["Art Deco"]
    international_style_architecture["International Style"]
    nordic_modernism_architecture["Nordic Modernism"]
    mid_century_modern_architecture["Mid-century Modern"]
    googie_architecture["Googie"]
    brutalist_architecture["Brutalism"]
    metabolism_architecture["Metabolism"]
    adaptive_reuse_architecture["Adaptive Reuse"]
  end
  subgraph architecture_postmodern_and_after["Architecture · Postmodern and After · 1966–present"]
    postmodern_architecture["Postmodernism"]
    radical_architecture["Radical architecture"]
    high_tech_architecture["High-tech"]
    critical_regionalism_architecture["Critical Regionalism"]
    deconstructivist_architecture["Deconstructivism"]
    mass_timber_architecture["Mass Timber"]
    parametricism_architecture["Parametricism"]
  end
  subgraph interior_classical_house["Interior · Classical house · 1700–1830"]
    georgian_interior["Georgian"]
  end
  subgraph interior_industrial_century["Interior · Industrial century · 1800–1890"]
    shaker_interior["Shaker"]
    victorian_interior["Victorian"]
    arts_and_crafts_interior["Arts and Crafts"]
  end
  subgraph interior_modern_reform["Interior · Modern reform · 1890–1940"]
    art_nouveau_interior["Art Nouveau"]
    bauhaus_interior["Bauhaus interior"]
    art_deco_interior["Art Deco"]
  end
  subgraph interior_post_war_modern["Interior · Post-war modern · 1940–1990"]
    hollywood_regency_interior["Hollywood Regency"]
    mid_century_modern_interior["Mid-century modern interior"]
    scandinavian_interior["Scandinavian interior"]
    industrial_loft_interior["Industrial loft"]
    memphis_interior["Memphis interior"]
  end
  subgraph interior_global_minimal["Interior · Global minimal · 1990–2010"]
    coastal_interior["Coastal interior"]
    minimalist_interior["Minimalist"]
  end
  subgraph interior_networked_home["Interior · Networked home · 2010–present"]
    japandi_interior["Japandi"]
    grandmillennial_interior["Grandmillennial"]
    neo_deco_interior["Neo-deco"]
    dopamine_decor["Dopamine decor"]
    quiet_luxury_interior["Quiet luxury"]
  end
  subgraph photography_art_photography["Photography · Photography as art · 1885–1950"]
    pictorialism["Pictorialism"]
    straight_photography["Straight photography"]
    group_f64["Group f/64"]
  end
  subgraph photography_documentary_century["Photography · The small camera · 1930–today"]
    new_objectivity["New Objectivity photography"]
    humanist_photography["Humanist photography"]
    street_photography["Street photography"]
    documentary_photography["Documentary photography"]
    are_bure_boke["Are-bure-boke"]
  end
  subgraph photography_colour_and_topography["Photography · Colour and the topographic turn · 1970–1990"]
    new_colour["New Colour"]
    new_topographics["New Topographics"]
    duesseldorf_school["Düsseldorf School"]
  end
  subgraph photography_digital_and_grade["Photography · Digital and the grade · 1999–today"]
    y2k_digicam["Y2K digicam"]
    cinematic_teal_orange["Cinematic teal and orange"]
    party_flash["Party flash"]
    film_grain_revival["Film grain revival"]
    ai_hyperreal["AI hyperreal image"]
  end
  subgraph photography_commercial_and_staged["Photography · Constructed images · 1930–today"]
    architectural_photography["Architectural photography"]
    fashion_editorial["Fashion editorial photography"]
    film_noir_still["Film noir still photography"]
    food_photography["Food photography"]
    scandinavian_interior_photography["Scandinavian interior photography"]
  end
  subgraph film_silent_era["Film & Video · The silent era · 1895–1929"]
    german_expressionist_cinema["German Expressionist cinema"]
    soviet_montage["Soviet montage"]
  end
  subgraph film_studio_system["Film & Video · The sound studio system · 1930–1957"]
    classical_hollywood["Classical Hollywood"]
    film_noir["Film noir"]
    italian_neorealism["Italian Neorealism"]
    one_take_oner["The oner"]
  end
  subgraph film_new_waves["Film & Video · Portable cameras and the new waves · 1958–1975"]
    french_new_wave["French New Wave"]
    documentary_verite["Direct cinema and vérité"]
    giallo["Giallo"]
    spaghetti_western["Spaghetti western"]
    new_hollywood["New Hollywood"]
    third_cinema["Third Cinema"]
  end
  subgraph film_tape_and_cable["Film & Video · Tape, cable and the blockbuster · 1976–1994"]
    music_video["Music video"]
    neon_noir["Neon noir"]
    hong_kong_action["Hong Kong action"]
  end
  subgraph film_digital_cinema["Film & Video · Lightweight digital and the manifesto · 1995–2009"]
    slow_cinema["Slow cinema"]
    dogme_95["Dogme 95"]
    planimetric_symmetry["Planimetric symmetry"]
    found_footage["Found footage"]
    mumblecore["Mumblecore"]
  end
  subgraph film_platform_video["Film & Video · Platform and creator video · 2005–today"]
    creator_vlog["Creator vlog"]
    phone_cinema["Phone cinema"]
    vertical_short_form["Vertical short-form"]
    cinematic_fpv["Cinematic FPV"]
    camcorder_revival["Camcorder revival"]
  end
  subgraph painting_early_modern["Painting · Early modern · 1400–1860"]
    renaissance_painting["Renaissance painting"]
    mannerism_painting["Mannerism"]
    baroque_painting["Baroque painting"]
    ukiyo_e["Ukiyo-e"]
    rococo_painting["Rococo"]
  end
  subgraph painting_nineteenth_century["Painting · Nineteenth century · 1840–1910"]
    romanticism_painting["Romanticism"]
    realism_painting["Realism"]
    impressionism["Impressionism"]
    nordic_national_romanticism_painting["Nordic national romanticism"]
    pointillism["Pointillism"]
    post_impressionism["Post-Impressionism"]
    symbolism_painting["Symbolism"]
    synthetism["Synthetism"]
  end
  subgraph painting_avant_garde["Painting · Avant-garde · 1905–1970"]
    expressionism_painting["Expressionism"]
    fauvism["Fauvism"]
    cubism_painting["Cubism"]
    futurism_painting["Futurism"]
    rayonism["Rayonism"]
    orphism["Orphism"]
    suprematism["Suprematism"]
    de_stijl_painting["De Stijl painting"]
    surrealism_painting["Surrealism"]
    abstract_expressionism["Abstract Expressionism"]
    colour_field_painting["Colour Field Painting"]
    pop_art_painting["Pop Art"]
    minimalism_painting["Minimalism"]
    photorealism["Photorealism"]
    airbrush_surrealism["Airbrush Surrealism"]
  end
  subgraph logo_trademark_age["Logo · Trademark age · 1860–1918"]
    victorian_trademark["Victorian trademark"]
    art_nouveau_monogram["Art Nouveau monogram"]
    emblem_badge["Emblem and badge"]
  end
  subgraph logo_modernist_identity["Logo · Modernist identity · 1919–1995"]
    swiss_modernist_mark["Swiss modernist corporate mark"]
    geometric_symbol["Geometric abstract symbol"]
    minimal_wordmark["Wordmark-led minimal"]
  end
  subgraph logo_screen_identity["Logo · Screen identity · 1995–now"]
    glossy_3d_logo["Gradient 3D and glass"]
    flat_logo["Flat 2010s mark"]
  end
  subgraph icon_bitmap["Icons · Bitmap · 1981–1995"]
    pixel_icon["Pixel icon"]
  end
  subgraph icon_rendered["Icons · Rendered · 1995–2013"]
    isometric_icon["Isometric icon"]
    skeuomorphic_icon["Skeuomorphic icon"]
  end
  subgraph icon_vector_system["Icons · Vector system · 2010–present"]
    flat_icon["Flat icon"]
    solid_glyph_icon["Solid glyph icon"]
    outline_icon["Outline icon"]
    material_symbols_icon["Material Symbols"]
    duotone_icon["Duotone icon"]
  end
  subgraph icon_post_flat["Icons · Post-flat · 2019–present"]
    clay_3d_icon["3D clay icon"]
  end
  subgraph typeface_hand_press["Typeface · Hand press · 1450–1820"]
    blackletter["Blackletter"]
    garalde_old_style["Garalde old-style serif"]
    formal_script["Formal script"]
    transitional_serif["Transitional serif"]
    didone_serif["Didone"]
  end
  subgraph typeface_industrial["Typeface · Industrial · 1810–1914"]
    fat_face_display["Fat face display"]
    slab_serif["Slab serif"]
    grotesque_sans["Grotesque sans"]
    monospace["Monospace"]
  end
  subgraph typeface_modernist["Typeface · Modernist · 1914–1975"]
    humanist_sans["Humanist sans"]
    geometric_sans["Geometric sans"]
    neo_grotesque_sans["Neo-grotesque sans"]
  end
  subgraph game_arcade_age["Video game · Arcade age · 1971–1985"]
    vector_display_arcade["Vector display arcade"]
  end
  subgraph game_tile_and_sprite["Video game · Tile and sprite · 1983–2002"]
    eight_bit_tile["8-bit tile graphics"]
    isometric_pixel_world["Isometric pixel world"]
    sixteen_bit_sprite["16-bit sprite and parallax"]
    four_shade_handheld["Four-shade handheld"]
    fantasy_console_pixel["Fantasy console pixel"]
  end
  subgraph game_early_polygon["Video game · Early polygon · 1993–2001"]
    pre_rendered_backgrounds["Pre-rendered backgrounds"]
    fifth_gen_low_poly["Fifth-generation low poly"]
  end
  subgraph game_programmable_shader["Video game · Programmable shader · 2000–2013"]
    cel_shaded_3d["Cel-shaded 3D"]
    hand_painted_texture["Hand-painted texture"]
    seventh_gen_desaturated["Seventh-generation desaturated bloom"]
    voxel_block_world["Voxel block world"]
  end
  subgraph game_physically_based_and_indie["Video game · Physically based and indie · 2013–now"]
    pbr_photoreal["PBR photoreal"]
    impossible_isometric_mobile["Flat geometric isometric"]
    hd_2d_diorama["HD-2D diorama"]
    low_poly_ps1_revival["Low-poly PS1 revival"]
  end
  subgraph print_hand_press["Print · Hand press · 1400–1800"]
    woodcut_relief_print["Woodcut relief print"]
    engraving_print["Copper engraving"]
    drypoint_print["Drypoint"]
    ebru_marbled_paper["Ottoman ebru marbled paper"]
    chiaroscuro_woodcut_print["Chiaroscuro woodcut"]
    etching_print["Etching"]
    dong_ho_folk_woodblock["Dong Ho folk woodblock painting"]
    katagami_stencil_print["Katazome and Ise katagami stencil print"]
    nianhua_new_year_print["Chinese nianhua New Year woodblock print"]
    ten_bamboo_studio_polychrome["Ten Bamboo Studio polychrome block print"]
    mezzotint_print["Mezzotint"]
    russian_lubok_print["Russian lubok folk print"]
    nishiki_e_polychrome_woodblock["Nishiki-e multi-block colour woodblock print"]
    aquatint_print["Aquatint"]
    stipple_engraving_print["Stipple (crayon-manner) engraving"]
    surimono_print["Surimono privately published print"]
    wood_engraving_print["End-grain wood engraving"]
    senjafuda_slip["Senjafuda pilgrim name slip"]
  end
  subgraph print_industrial_press["Print · Industrial press · 1800–1945"]
    battala_woodcut["Battala woodcut"]
    banknote_engraving_print["Steel-engraved banknote and stamp"]
    crayon_lithograph_print["Crayon lithograph"]
    wood_type_poster["Wood-type poster"]
    qajar_lithographed_book["Qajar lithographed book"]
    collotype_print["Collotype"]
    chromolithograph_poster["Chromolithograph poster"]
    meiji_kosen_ga_print["Meiji kosen-ga and aniline-red woodblock print"]
    photogravure_print["Photogravure"]
    posada_broadside["Posada broadside"]
    private_press_book["Private-press book"]
    ravi_varma_oleograph["Ravi Varma oleograph"]
    ben_day_comic_print["Ben-Day comic print"]
    mir_iskusstva_book_graphics["Mir iskusstva book graphics"]
    cordel_xilogravura["Cordel xilogravura"]
    yuefenpai_calendar_poster["Shanghai yuefenpai calendar poster"]
    sosaku_hanga_print["Sosaku-hanga creative print"]
    expressionist_woodcut_print["Die Brucke woodcut"]
    pochoir_plate["Pochoir plate"]
    narbut_ukrainian_graphics["Narbut Ukrainian Baroque graphics"]
    shin_hanga_print["Shin-hanga new print"]
    rosta_window_stencil_poster["ROSTA Window stencil poster"]
    constructivist_photomontage_poster["Constructivist photomontage poster"]
    linocut_print["Expressive linocut"]
    chinese_modern_woodcut["Chinese modern woodcut"]
    taller_grafica_popular_linocut["Taller de Gráfica Popular linocut"]
  end
  subgraph print_studio_press["Print · Studio press · 1945–1995"]
    pop_screen_print["Pop screen print"]
    psychedelic_concert_poster["Psychedelic concert poster"]
    xerox_zine["Xerox zine"]
    chicha_poster["Chicha poster"]
  end
  subgraph print_digital_press["Print · Digital press · 1995–"]
    risograph_print["Risograph print"]
  end
  subgraph graphic_movement_fin_de_siecle["Graphic movements · Fin de Siècle · 1880–1918"]
    victorian_web["Victorian Web"]
    art_nouveau_web["Art Nouveau (web)"]
  end
  subgraph graphic_movement_modernist["Graphic movements · Modernist · 1919–1975"]
    de_stijl_web["De Stijl (web)"]
    bauhaus["Bauhaus"]
    constructivism_web["Constructivism (web)"]
    art_deco_web["Art Deco (web)"]
    mid_century_modern["Mid-Century Modern"]
    swiss_international["Swiss International Style"]
    japanese_graphic_modernism["Japanese Graphic Modernism"]
    rams_functionalism_ui["Rams Functionalism (UI)"]
    pop_art_web["Pop Art (web)"]
    space_age["Space Age Design"]
    psychedelic["Psychedelic"]
  end
  subgraph industrial_proto_industrial["Industrial design · Proto-industrial · 1760–1840"]
    georgian_neoclassical_manufacture["Georgian neoclassical manufacture"]
    shaker_object["Shaker object"]
  end
  subgraph industrial_victorian_mass_production["Industrial design · Victorian mass production · 1840–1900"]
    victorian_manufacture["Victorian manufacture"]
  end
  subgraph industrial_reform_and_craft["Industrial design · Reform and craft · 1880–1918"]
    arts_and_crafts_object["Arts and Crafts object"]
    art_nouveau_object["Art Nouveau object"]
    industrial_utility_product["Industrial utility product"]
  end
  subgraph industrial_machine_modern["Industrial design · Machine modern · 1919–1945"]
    bauhaus_product["Bauhaus product"]
    art_deco_product["Art Deco product"]
    scandinavian_modern_product["Scandinavian modern product"]
    streamline_moderne_product["Streamline Moderne product"]
  end
  subgraph industrial_post_war_modern["Industrial design · Post-war modern · 1945–1975"]
    mid_century_modern_product["Mid-century modern product"]
    japanese_modern_craft_product["Japanese modern craft product"]
    ulm_braun_functionalism["Ulm and Braun functionalism"]
    space_age_pop_product["Space Age pop product"]
    pop_foam_furniture["Pop foam furniture"]
  end
  subgraph industrial_postmodern_plural["Industrial design · Postmodern plural · 1976–2000"]
    memphis_product["Memphis product"]
  end
  subgraph industrial_contemporary["Industrial design · Contemporary · 2000–now"]
    contemporary_craft_product["Contemporary craft product"]
    super_normal_product["Super Normal product"]
  end
  subgraph fashion_court_and_guild["Fashion · Court and guild · 1550–1788"]
    whalebone_stays["Whalebone Stays"]
    georgian_jewellery["Georgian Jewellery"]
    rococo_court_dress["Rococo court dress"]
    breguet_classical_watch["Breguet classical watch"]
  end
  subgraph fashion_revolution_and_regency["Fashion · Revolution and Regency · 1789–1836"]
    empire_line_dress["Empire line dress"]
    english_bespoke_tailoring["English bespoke tailoring"]
  end
  subgraph fashion_victorian_dress["Fashion · Victorian dress · 1837–1899"]
    victorian_sentimental_jewellery["Victorian Sentimental Jewellery"]
    victorian_corsetry["Victorian Corsetry"]
    victorian_millinery["Victorian millinery"]
    american_pocket_watch["American pocket watch"]
    victorian_boot["Victorian boot"]
    malletier_luggage["Malletier luggage"]
    crinoline_and_bustle_dress["Crinoline and bustle dress"]
    country_sporting_tweed["Country sporting tweed"]
    english_welted_dress_shoe["English welted dress shoe"]
    americana_workwear["Americana workwear"]
    brass_era_car["Brass-Era Car"]
    arts_and_crafts_jewellery["Arts and Crafts Jewellery"]
    art_nouveau_jewellery["Art Nouveau Jewellery"]
  end
  subgraph fashion_belle_epoque_and_war["Fashion · Belle Époque and the Great War · 1900–1918"]
    straight_front_corset["Straight-Front Corset"]
    garland_style_jewellery["Garland Style Jewellery"]
    early_wristwatch["Early wristwatch"]
    bandeau_brassiere["Bandeau Brassiere"]
    trench_and_field_military["Trench and field military"]
    art_deco_watch["Art Deco watch"]
    canvas_court_sneaker["Canvas court sneaker"]
  end
  subgraph fashion_interwar_modern["Fashion · Interwar modern · 1919–1938"]
    vintage_coachbuilt_car["Vintage Coachbuilt Car"]
    art_deco_dance_shoe["Art Deco dance shoe"]
    early_mountaineering["Early mountaineering"]
    garconne_flapper_dress["Garçonne and flapper dress"]
    costume_jewellery["Costume Jewellery"]
    art_deco_evening_accessory["Art Deco evening accessory"]
    art_deco_jewellery["Art Deco Jewellery"]
    bias_cut_glamour["Bias-cut glamour"]
    pilot_and_field_watch["Pilot and field watch"]
    streamline_car["Streamline Car"]
    modern_mens_briefs["Modern Men's Briefs"]
    retro_cocktail_jewellery["Retro Cocktail Jewellery"]
    quilted_down_outerwear["Quilted down outerwear"]
    mid_century_eyewear["Mid-century eyewear"]
  end
  subgraph fashion_war_and_new_look["Fashion · War and the New Look · 1939–1959"]
    modernist_studio_jewellery["Modernist Studio Jewellery"]
    italian_gran_turismo["Italian Gran Turismo"]
    new_look["New Look"]
    nylon_foundation_garments["Nylon Foundation Garments"]
    tailfin_era_car["Tailfin-Era Car"]
    ivy_style["Ivy style"]
    dive_watch["Dive watch"]
    stiletto_heel["Stiletto heel"]
    ladylike_handbag["Ladylike handbag"]
    racing_chronograph["Racing chronograph"]
  end
  subgraph fashion_youthquake["Fashion · Youthquake · 1960–1979"]
    brutalist_jewellery["Brutalist Jewellery"]
    mod_and_mini["Mod and mini"]
    nordic_functional_outdoor["Nordic functional outdoor"]
    subculture_workboot["Subculture workboot"]
    muscle_and_pony_car["Muscle and Pony Car"]
    soft_natural_lingerie["Soft Natural Lingerie"]
    space_age_couture["Space Age couture"]
    hippie_bohemian_dress["Hippie bohemian dress"]
    wedge_design_car["Wedge Design Car"]
    electronic_and_digital_watch["Electronic and digital watch"]
    glam_platform_shoe["Glam platform shoe"]
    luxury_steel_sports_watch["Luxury steel sports watch"]
    performance_running_shoe["Performance running shoe"]
    punk_fashion["Punk fashion"]
    technical_shell_alpinism["Technical shell alpinism"]
  end
  subgraph fashion_power_and_subculture["Fashion · Power and subculture · 1980–1999"]
    power_dressing["Power dressing"]
    streetwear["Streetwear"]
    japanese_avant_garde_fashion["Japanese avant-garde fashion"]
    designer_logo_underwear["Designer Logo Underwear"]
    swiss_plastic_pop_watch["Swiss plastic pop watch"]
    underwear_as_outerwear["Underwear as Outerwear"]
    logomania["Logomania"]
    sneaker_culture["Sneaker culture"]
    biodesign_car["Biodesign Car"]
    minimalist_fashion["Minimalist fashion"]
    ura_harajuku_streetwear["Ura-Harajuku streetwear"]
    it_bag["It bag"]
    retro_revival_car["Retro Revival Car"]
  end
  subgraph fashion_contemporary_fashion["Fashion · Contemporary · 2000–now"]
    shapewear_and_seamless["Shapewear and Seamless"]
    techwear["Techwear"]
    quiet_luxury_fashion["Quiet luxury fashion"]
    stealth_luxury_accessory["Stealth luxury accessory"]
    electric_minimal_car["Electric Minimal Car"]
    smartwatch["Smartwatch"]
    gorpcore["Gorpcore"]
  end
  subgraph ceramics_ancient_clay["Ceramics · Ancient clay · before 600"]
    jomon_pottery["Jōmon pottery"]
    greek_black_figure["Greek black-figure pottery"]
    babylonian_glazed_brick["Babylonian glazed brick"]
    greek_red_figure["Greek red-figure pottery"]
    qin_terracotta_warriors["Qin terracotta warriors"]
    roman_terra_sigillata["Roman terra sigillata"]
  end
  subgraph ceramics_medieval_glaze["Ceramics · Medieval glaze · 600–1368"]
    tang_sancai_figures["Tang sancai figures"]
    abbasid_lustreware["Abbasid lustreware"]
    ding_white_ware["Ding white ware"]
    jian_tenmoku_ware["Jian tenmoku ware"]
    goryeo_celadon["Goryeo celadon"]
    longquan_celadon["Longquan celadon"]
    islamic_tile_mosaic["Islamic tile mosaic"]
    hispano_moresque_lustreware["Hispano-Moresque lustreware"]
    zellige["Zellige"]
    yuan_ming_blue_and_white["Yuan and Ming blue-and-white porcelain"]
  end
  subgraph ceramics_blue_and_white["Ceramics · Blue and white · 1368–1600"]
    joseon_buncheong["Joseon buncheong"]
    rhenish_salt_glaze_stoneware["Rhenish salt-glaze stoneware"]
    liuli_glazed_roof["Liuli glazed roof tile"]
    della_robbia_relief["Della Robbia relief"]
    albarello_apothecary_ware["Albarello apothecary ware"]
    iznik_pottery["Iznik pottery"]
    istoriato_maiolica["Istoriato maiolica"]
    yixing_zisha_teapot["Yixing zisha teapot"]
    iznik_tiles["Iznik tiles"]
    azulejo["Azulejo"]
    kraak_porcelain["Kraak porcelain"]
    mino_tea_ceramics["Mino tea ceramics"]
    raku_tea_bowl["Raku tea bowl"]
  end
  subgraph ceramics_porcelain_race["Ceramics · The porcelain race · 1600–1750"]
    delft_tiles["Delft tiles"]
    delftware["Delftware"]
    joseon_moon_jar["Joseon moon jar"]
    kyo_yaki_overglaze["Kyo-yaki overglaze"]
    kakiemon_imari_export["Kakiemon and Imari export porcelain"]
    english_slipware["English slipware"]
    famille_rose_qing["Famille rose (Qing)"]
    meissen_baroque_porcelain["Meissen baroque porcelain"]
    rococo_porcelain_figures["Rococo porcelain figures"]
    georgian_porcelain_tea_service["Georgian porcelain tea service"]
    staffordshire_figures["Staffordshire figures"]
  end
  subgraph ceramics_industrial_pottery["Ceramics · Industrial pottery · 1750–1880"]
    scandinavian_tiled_stove["Scandinavian tiled stove"]
    biscuit_porcelain_figures["Biscuit porcelain figures"]
    sevres_rococo_porcelain["Sèvres rococo porcelain"]
    creamware_neoclassical["Creamware, neoclassical"]
    mocha_banded_ware["Mocha and banded ware"]
    jasperware_neoclassical["Jasperware (Neoclassical)"]
    blue_willow_transferware["Blue willow transferware"]
    american_stoneware_crock["American stoneware crock"]
    regency_gilded_bone_china["Regency gilded bone china"]
    spongeware["Spongeware"]
    victorian_encaustic_tiles["Victorian encaustic tiles"]
    parian_statuary["Parian statuary"]
    porcelain_insulator["Porcelain insulator"]
    victorian_architectural_terracotta["Victorian architectural terracotta"]
    victorian_sanitary_ware["Victorian sanitary ware"]
    arts_and_crafts_art_pottery["Arts and Crafts art pottery"]
  end
  subgraph ceramics_art_pottery["Ceramics · Art pottery and reform · 1880–1918"]
    american_art_pottery["American art pottery"]
    fireclay_butler_sink["Fireclay butler sink"]
    chicago_school_terracotta["Chicago School terracotta"]
    art_nouveau_ceramics["Art Nouveau ceramics"]
    hungarian_secession_ceramics["Hungarian Secession ceramics"]
    art_nouveau_tiles["Art Nouveau tiles"]
    trencadis["Trencadís"]
    subway_tile["Subway tile"]
  end
  subgraph ceramics_modern_ceramics["Ceramics · Modern ceramics · 1919–1975"]
    anglo_oriental_studio_pottery["Anglo-Oriental studio pottery"]
    suprematist_porcelain["Suprematist porcelain"]
    cornishware["Cornishware"]
    art_deco_ceramic_figures["Art Deco ceramic figures"]
    art_deco_faience_facade["Art Deco faience facade"]
    mingei_folk_craft["Mingei folk craft"]
    coloured_bathroom_suite["Coloured bathroom suite"]
    art_deco_tableware["Art Deco tableware"]
    bauhaus_modern_tableware["Bauhaus modern tableware"]
    fiesta_colourware["Fiesta colourware"]
    organic_modern_tableware["Organic modern tableware"]
    british_modernist_studio["British modernist studio ceramics"]
    artist_ceramics_vallauris["Artist ceramics of Vallauris"]
    scandinavian_modern_tableware["Scandinavian modern tableware"]
    abstract_expressionist_ceramics["Abstract Expressionist ceramics"]
    glass_ceramic_cookware["Glass-ceramic cookware"]
    west_german_fat_lava["West German fat lava"]
    funk_ceramics["Funk ceramics"]
  end
  subgraph ceramics_plural_contemporary["Ceramics · Plural and contemporary · 1976–now"]
    large_format_porcelain_tiles["Large-format porcelain tiles"]
    washlet_toilet["Washlet toilet"]
    memphis_postmodern_ceramics["Memphis postmodern ceramics"]
    terracotta_rainscreen["Terracotta rainscreen"]
    designer_wall_hung_sanitary["Designer wall-hung sanitary ware"]
    chef_studio_tableware["Chef studio tableware"]
    digital_3d_printed_ceramics["Digital 3D-printed ceramics"]
  end
  subgraph cuisine_court_and_banquet["Cuisine · Court and banquet · 1300–1650"]
    medieval_court_cuisine["Medieval court cuisine"]
    renaissance_banquet["Renaissance banquet"]
  end
  subgraph cuisine_classical_codification["Cuisine · Classical codification · 1650–1800"]
    cuisine_francoise["Cuisine françoise"]
  end
  subgraph cuisine_grande_and_classique["Cuisine · Grande and classique · 1800–1914"]
    grande_cuisine["Grande cuisine"]
    cuisine_classique["Cuisine classique"]
  end
  subgraph cuisine_regional_and_bourgeois["Cuisine · Regional and bourgeois · 1914–1965"]
    haute_regionale["Haute cuisine régionale"]
  end
  subgraph cuisine_nouvelle_and_new_world["Cuisine · Nouvelle and new world · 1965–1990"]
    nouvelle_cuisine["Nouvelle cuisine"]
    california_cuisine["California cuisine"]
    cuisine_minceur["Cuisine minceur"]
    naturalist_cuisine["Naturalist cuisine"]
    pacific_rim_fusion["Pacific Rim fusion"]
    novoandina_and_nikkei["Novoandina and Nikkei cuisine"]
  end
  subgraph cuisine_modernist_and_global["Cuisine · Modernist and global · 1988–2011"]
    molecular_gastronomy["Molecular gastronomy"]
    bistronomie["Bistronomie"]
    modernist_cuisine["Modernist cuisine"]
  end
  subgraph cuisine_terroir_and_plant["Cuisine · Terroir and plant · 2004–now"]
    new_nordic["New Nordic cuisine"]
    plant_based_fine_dining["Plant-based fine dining"]
  end
  3d_avatar_emoji <-. echoes .-> clay_3d_icon
  abstract_expressionism <-. echoes .-> abstract_expressionist_ceramics
  abstract_expressionism <-. echoes .-> brutalist_architecture
  adaptive_reuse_architecture <-. echoes .-> industrial_loft_interior
  ai_avatar_portrait <-. echoes .-> airbrush_surrealism
  ai_hyperreal <-. echoes .-> ai_slop
  ai_hyperreal <-. echoes .-> diffusion_gloss
  ai_hyperreal <-. echoes .-> gan_portrait
  ai_hyperreal <-. echoes .-> pbr_photoreal
  airbrush_surrealism <-. echoes .-> pop_art_web
  airbrush_surrealism <-. echoes .-> psychedelic
  airbrush_surrealism <-. echoes .-> space_age
  airbrush_surrealism <-. echoes .-> surrealism_web
  american_art_pottery <-. echoes .-> arts_and_crafts_interior
  american_pocket_watch <-. echoes .-> industrial_utility_product
  american_pocket_watch <-. echoes .-> victorian_manufacture
  americana_workwear <-. echoes .-> industrial_utility_product
  americana_workwear <-. echoes .-> shaker_object
  anglo_oriental_studio_pottery <-. echoes .-> contemporary_craft_product
  anglo_oriental_studio_pottery <-. echoes .-> japanese_modern_craft_product
  ansi_bbs_art <-. echoes .-> pixel_icon
  anti_design <-. echoes .-> deconstructivist_architecture
  anti_design <-. echoes .-> swiss_international
  anti_design <-. echoes .-> xerox_zine
  apple_aqua <-. echoes .-> glossy_3d_logo
  apple_aqua <-. echoes .-> skeuomorphic_icon
  architectural_photography <-. echoes .-> bauhaus_architecture
  architectural_photography <-. echoes .-> brutalist_architecture
  architectural_photography <-. echoes .-> international_style_architecture
  architectural_photography <-. echoes .-> isometric_pixel_world
  architectural_photography <-. echoes .-> mid_century_modern_architecture
  architectural_photography <-. echoes .-> pbr_photoreal
  architectural_photography <-. echoes .-> pre_rendered_backgrounds
  art_deco_architecture <-. echoes .-> art_deco_ceramic_figures
  art_deco_architecture <-. echoes .-> art_deco_faience_facade
  art_deco_architecture <-. echoes .-> art_deco_interior
  art_deco_architecture <-. echoes .-> art_deco_jewellery
  art_deco_architecture <-. echoes .-> art_deco_product
  art_deco_architecture <-. echoes .-> art_deco_watch
  art_deco_architecture <-. echoes .-> art_deco_web
  art_deco_architecture <-. echoes .-> classical_hollywood
  art_deco_architecture <-. echoes .-> neo_deco_interior
  art_deco_architecture <-. echoes .-> streamline_moderne_product
  art_deco_ceramic_figures <-. echoes .-> art_deco_jewellery
  art_deco_ceramic_figures <-. echoes .-> art_deco_product
  art_deco_dance_shoe <-. echoes .-> art_deco_interior
  art_deco_dance_shoe <-. echoes .-> art_deco_product
  art_deco_evening_accessory <-. echoes .-> art_deco_interior
  art_deco_evening_accessory <-. echoes .-> art_deco_product
  art_deco_faience_facade <-. echoes .-> art_deco_interior
  art_deco_faience_facade <-. echoes .-> art_deco_product
  art_deco_interior <-. echoes .-> art_deco_jewellery
  art_deco_interior <-. echoes .-> art_deco_product
  art_deco_interior <-. echoes .-> art_deco_tableware
  art_deco_interior <-. echoes .-> art_deco_web
  art_deco_interior <-. echoes .-> bias_cut_glamour
  art_deco_interior <-. echoes .-> garconne_flapper_dress
  art_deco_interior <-. echoes .-> pochoir_plate
  art_deco_interior <-. echoes .-> streamline_moderne_product
  art_deco_jewellery <-. echoes .-> art_deco_product
  art_deco_product <-. echoes .-> art_deco_tableware
  art_deco_product <-. echoes .-> art_deco_watch
  art_deco_product <-. echoes .-> art_deco_web
  art_deco_product <-. echoes .-> coloured_bathroom_suite
  art_deco_product <-. echoes .-> costume_jewellery
  art_deco_product <-. echoes .-> fiesta_colourware
  art_deco_product <-. echoes .-> garconne_flapper_dress
  art_deco_product <-. echoes .-> neo_deco_interior
  art_deco_product <-. echoes .-> vintage_coachbuilt_car
  art_deco_tableware <-. echoes .-> streamline_moderne_product
  art_deco_web <-. echoes .-> hollywood_regency_interior
  art_deco_web <-. echoes .-> luxury_typography_web
  art_deco_web <-. echoes .-> neo_deco_interior
  art_deco_web <-. echoes .-> pochoir_plate
  art_nouveau_architecture <-. echoes .-> art_nouveau_ceramics
  art_nouveau_architecture <-. echoes .-> art_nouveau_interior
  art_nouveau_architecture <-. echoes .-> art_nouveau_monogram
  art_nouveau_architecture <-. echoes .-> art_nouveau_object
  art_nouveau_architecture <-. echoes .-> art_nouveau_tiles
  art_nouveau_architecture <-. echoes .-> art_nouveau_web
  art_nouveau_architecture <-. echoes .-> chicago_school_terracotta
  art_nouveau_architecture <-. echoes .-> hungarian_secession_ceramics
  art_nouveau_architecture <-. echoes .-> rococo_painting
  art_nouveau_architecture <-. echoes .-> symbolism_painting
  art_nouveau_architecture <-. echoes .-> trencadis
  art_nouveau_ceramics <-. echoes .-> art_nouveau_interior
  art_nouveau_ceramics <-. echoes .-> art_nouveau_object
  art_nouveau_interior <-. echoes .-> art_nouveau_jewellery
  art_nouveau_interior <-. echoes .-> art_nouveau_monogram
  art_nouveau_interior <-. echoes .-> art_nouveau_object
  art_nouveau_interior <-. echoes .-> art_nouveau_tiles
  art_nouveau_interior <-. echoes .-> art_nouveau_web
  art_nouveau_interior <-. echoes .-> chromolithograph_poster
  art_nouveau_jewellery <-. echoes .-> art_nouveau_object
  art_nouveau_monogram <-. echoes .-> art_nouveau_web
  art_nouveau_object <-. echoes .-> art_nouveau_tiles
  art_nouveau_object <-. echoes .-> art_nouveau_web
  art_nouveau_object <-. echoes .-> mir_iskusstva_book_graphics
  art_nouveau_web <-. echoes .-> bohemian_web
  art_nouveau_web <-. echoes .-> chromolithograph_poster
  art_nouveau_web <-. echoes .-> psychedelic_concert_poster
  art_nouveau_web <-. echoes .-> symbolism_painting
  artist_ceramics_vallauris <-. echoes .-> cubism_painting
  arts_and_crafts_architecture <-. echoes .-> arts_and_crafts_interior
  arts_and_crafts_architecture <-. echoes .-> arts_and_crafts_object
  arts_and_crafts_architecture <-. echoes .-> private_press_book
  arts_and_crafts_art_pottery <-. echoes .-> arts_and_crafts_interior
  arts_and_crafts_art_pottery <-. echoes .-> arts_and_crafts_object
  arts_and_crafts_interior <-. echoes .-> arts_and_crafts_jewellery
  arts_and_crafts_interior <-. echoes .-> arts_and_crafts_object
  arts_and_crafts_interior <-. echoes .-> cottagecore
  arts_and_crafts_interior <-. echoes .-> hand_painted_texture
  arts_and_crafts_interior <-. echoes .-> humanist_sans
  arts_and_crafts_interior <-. echoes .-> nordic_national_romanticism_painting
  arts_and_crafts_interior <-. echoes .-> private_press_book
  arts_and_crafts_jewellery <-. echoes .-> arts_and_crafts_object
  arts_and_crafts_object <-. echoes .-> country_sporting_tweed
  azulejo <-. echoes .-> baroque_architecture
  barbiecore <-. echoes .-> dopamine_decor
  barbiecore <-. echoes .-> hollywood_regency_interior
  barbiecore <-. echoes .-> mod_and_mini
  barbiecore <-. echoes .-> space_age_pop_product
  baroque_architecture <-. echoes .-> baroque_painting
  baroque_architecture <-. echoes .-> cuisine_francoise
  baroque_painting <-. echoes .-> etching_print
  baroque_painting <-. echoes .-> film_noir_still
  baroque_painting <-. echoes .-> food_photography
  baroque_painting <-. echoes .-> german_expressionist_cinema
  baroque_painting <-. echoes .-> meissen_baroque_porcelain
  baroque_painting <-. echoes .-> mezzotint_print
  baroque_painting <-. echoes .-> narbut_ukrainian_graphics
  bauhaus <-. echoes .-> bauhaus_architecture
  bauhaus <-. echoes .-> bauhaus_interior
  bauhaus <-. echoes .-> bauhaus_modern_tableware
  bauhaus <-. echoes .-> bauhaus_product
  bauhaus <-. echoes .-> de_stijl_painting
  bauhaus <-. echoes .-> geometric_sans
  bauhaus <-. echoes .-> geometric_symbol
  bauhaus <-. echoes .-> international_style_architecture
  bauhaus_architecture <-. echoes .-> bauhaus_interior
  bauhaus_architecture <-. echoes .-> bauhaus_product
  bauhaus_architecture <-. echoes .-> geometric_sans
  bauhaus_architecture <-. echoes .-> new_objectivity
  bauhaus_interior <-. echoes .-> bauhaus_modern_tableware
  bauhaus_interior <-. echoes .-> bauhaus_product
  bauhaus_interior <-. echoes .-> de_stijl_painting
  bauhaus_interior <-. echoes .-> international_style_architecture
  bauhaus_modern_tableware <-. echoes .-> bauhaus_product
  bauhaus_product <-. echoes .-> modernist_studio_jewellery
  beaux_arts_architecture <-. echoes .-> cuisine_classique
  beaux_arts_architecture <-. echoes .-> garland_style_jewellery
  ben_day_comic_print <-. echoes .-> pop_art_painting
  ben_day_comic_print <-. echoes .-> pop_art_web
  ben_day_comic_print <-. echoes .-> rage_comic
  bento_grid_ui <-. echoes .-> swiss_international
  bias_cut_glamour <-. echoes .-> classical_hollywood
  biscuit_porcelain_figures <-. echoes .-> georgian_neoclassical_manufacture
  biscuit_porcelain_figures <-. echoes .-> rococo_painting
  blackletter <-. echoes .-> gothic_architecture
  blackletter <-. echoes .-> private_press_book
  blackletter <-. echoes .-> punk_zine
  blackletter <-. echoes .-> woodcut_relief_print
  blue_willow_transferware <-. echoes .-> victorian_manufacture
  bohemian_web <-. echoes .-> hippie_bohemian_dress
  bohemian_web <-. echoes .-> psychedelic
  breguet_classical_watch <-. echoes .-> georgian_neoclassical_manufacture
  british_modernist_studio <-. echoes .-> contemporary_craft_product
  brutalist_architecture <-. echoes .-> brutalist_jewellery
  brutalist_architecture <-. echoes .-> brutalist_web
  brutalist_architecture <-. echoes .-> constructivism_web
  brutalist_architecture <-. echoes .-> dogme_95
  brutalist_architecture <-. echoes .-> duesseldorf_school
  brutalist_architecture <-. echoes .-> industrial_loft_interior
  brutalist_architecture <-. echoes .-> liminal_spaces
  brutalist_architecture <-. echoes .-> neo_brutalism_ui
  brutalist_architecture <-. echoes .-> new_topographics
  brutalist_architecture <-. echoes .-> seventh_gen_desaturated
  brutalist_web <-. echoes .-> monospace
  camcorder_revival <-. echoes .-> dual_camera_snapshot
  camcorder_revival <-. echoes .-> fifth_gen_low_poly
  camcorder_revival <-. echoes .-> film_grain_revival
  camcorder_revival <-. echoes .-> glitch_gif
  camcorder_revival <-. echoes .-> grunge_editorial
  camcorder_revival <-. echoes .-> kidcore
  camcorder_revival <-. echoes .-> low_poly_ps1_revival
  camcorder_revival <-. echoes .-> party_flash
  camcorder_revival <-. echoes .-> vaporwave
  camcorder_revival <-. echoes .-> weirdcore
  camcorder_revival <-. echoes .-> y2k_aesthetic
  camcorder_revival <-. echoes .-> y2k_digicam
  cassette_futurism <-. echoes .-> electronic_and_digital_watch
  cassette_futurism <-. echoes .-> high_tech_architecture
  cassette_futurism <-. echoes .-> rams_functionalism_ui
  cassette_futurism <-. echoes .-> vector_display_arcade
  cel_shaded_3d <-. echoes .-> flat_design
  cel_shaded_3d <-. echoes .-> pop_art_painting
  cel_shaded_3d <-. echoes .-> ukiyo_e
  chat_sticker_pack <-. echoes .-> flat_icon
  chicago_school_terracotta <-. echoes .-> prairie_school_architecture
  chromolithograph_poster <-. echoes .-> post_impressionism
  cinematic_teal_orange <-. echoes .-> neon_noir
  cinematic_teal_orange <-. echoes .-> seventh_gen_desaturated
  cinematic_teal_orange <-. echoes .-> vsco_preset_look
  classical_hollywood <-. echoes .-> ladylike_handbag
  classical_hollywood <-. echoes .-> pre_rendered_backgrounds
  clay_3d_icon <-. echoes .-> claymorphism
  clean_girl <-. echoes .-> fashion_editorial
  clean_girl <-. echoes .-> minimalist_fashion
  clean_girl <-. echoes .-> minimalist_interior
  clean_girl <-. echoes .-> quiet_luxury_fashion
  clickbait_thumbnail <-. echoes .-> pop_art_web
  clickbait_thumbnail <-. echoes .-> vertical_short_form
  coloured_bathroom_suite <-. echoes .-> streamline_moderne_product
  conceptual_sketch_ui <-. echoes .-> swiss_international
  constructivism_web <-. echoes .-> constructivist_photomontage_poster
  constructivism_web <-. echoes .-> cubism_painting
  constructivism_web <-. echoes .-> futurism_painting
  constructivism_web <-. echoes .-> grotesque_sans
  constructivism_web <-. echoes .-> rosta_window_stencil_poster
  constructivism_web <-. echoes .-> soviet_montage
  constructivism_web <-. echoes .-> suprematism
  constructivism_web <-. echoes .-> suprematist_porcelain
  contemporary_craft_product <-. echoes .-> digital_3d_printed_ceramics
  contemporary_craft_product <-. echoes .-> japandi_interior
  contemporary_craft_product <-. echoes .-> large_format_porcelain_tiles
  contemporary_craft_product <-. echoes .-> modernist_studio_jewellery
  contemporary_craft_product <-. echoes .-> new_nordic
  contemporary_craft_product <-. echoes .-> quiet_luxury_interior
  contemporary_craft_product <-. echoes .-> wabi_sabi_web
  corporate_memphis <-. echoes .-> risograph_print
  cottagecore <-. echoes .-> grandmillennial_interior
  cottagecore <-. echoes .-> mingei_folk_craft
  cottagecore <-. echoes .-> romanticism_painting
  creamware_neoclassical <-. echoes .-> georgian_interior
  creamware_neoclassical <-. echoes .-> georgian_neoclassical_manufacture
  creamware_neoclassical <-. echoes .-> neoclassical_architecture
  creator_vlog <-. echoes .-> duet_split_screen
  creator_vlog <-. echoes .-> green_screen_short
  creator_vlog <-. echoes .-> grwm_short
  creator_vlog <-. echoes .-> lets_play_facecam
  creator_vlog <-. echoes .-> photo_carousel_slideshow
  creator_vlog <-. echoes .-> pov_short
  creator_vlog <-. echoes .-> unboxing_video
  creator_vlog <-. echoes .-> video_essay
  crinoline_and_bustle_dress <-. echoes .-> victorian_interior
  crinoline_and_bustle_dress <-. echoes .-> victorian_manufacture
  cubism_painting <-. echoes .-> deconstructivist_architecture
  cuisine_classique <-. echoes .-> victorian_interior
  cyberdelia <-. echoes .-> party_flash
  cyberdelia <-. echoes .-> psychedelic
  cyberpunk_web <-. echoes .-> film_noir_still
  cyberpunk_web <-. echoes .-> techwear
  dark_academia <-. echoes .-> gothic_architecture
  dark_academia <-. echoes .-> ivy_style
  dark_academia <-. echoes .-> romanticism_painting
  dark_academia <-. echoes .-> victorian_interior
  dark_academia <-. echoes .-> victorian_web
  dark_devtool_ui <-. echoes .-> monospace
  de_stijl_painting <-. echoes .-> de_stijl_web
  de_stijl_painting <-. echoes .-> geometric_symbol
  de_stijl_painting <-. echoes .-> international_style_architecture
  de_stijl_painting <-. echoes .-> prairie_school_architecture
  de_stijl_painting <-. echoes .-> swiss_international
  de_stijl_painting <-. echoes .-> voxel_block_world
  de_stijl_web <-. echoes .-> international_style_architecture
  de_stijl_web <-. echoes .-> prairie_school_architecture
  deconstructivist_architecture <-. echoes .-> grunge_editorial
  deep_fried_meme <-. echoes .-> xerox_zine
  deepdream_psychedelia <-. echoes .-> psychedelic
  deepdream_psychedelia <-. echoes .-> psychedelic_concert_poster
  deepfake_face_swap <-. echoes .-> vertical_short_form
  della_robbia_relief <-. echoes .-> renaissance_architecture
  demotivational_poster <-. echoes .-> xerox_zine
  designer_wall_hung_sanitary <-. echoes .-> minimalist_interior
  designer_wall_hung_sanitary <-. echoes .-> super_normal_product
  didone_serif <-. echoes .-> engraving_print
  didone_serif <-. echoes .-> fashion_editorial
  didone_serif <-. echoes .-> neoclassical_architecture
  digital_3d_printed_ceramics <-. echoes .-> parametricism_architecture
  dive_watch <-. echoes .-> industrial_utility_product
  dive_watch <-. echoes .-> mid_century_modern_product
  documentary_photography <-. echoes .-> dogme_95
  documentary_verite <-. echoes .-> street_photography
  documentary_verite <-. echoes .-> video_essay
  dogme_95 <-. echoes .-> straight_photography
  dopamine_decor <-. echoes .-> food_photography
  dopamine_decor <-. echoes .-> kidcore
  dopamine_decor <-. echoes .-> memphis_design
  dopamine_decor <-. echoes .-> memphis_product
  dreamcore <-. echoes .-> y2k_digicam
  dual_camera_snapshot <-. echoes .-> vertical_short_form
  duesseldorf_school <-. echoes .-> international_style_architecture
  duet_split_screen <-. echoes .-> vertical_short_form
  duotone_icon <-. echoes .-> risograph_print
  early_wristwatch <-. echoes .-> industrial_utility_product
  editorial_serif_revival <-. echoes .-> risograph_print
  editorial_serif_revival <-. echoes .-> swiss_international
  eight_bit_tile <-. echoes .-> pixel_art_web
  eight_bit_tile <-. echoes .-> pixel_icon
  electric_minimal_car <-. echoes .-> minimalist_interior
  electric_minimal_car <-. echoes .-> super_normal_product
  electronic_and_digital_watch <-. echoes .-> space_age_pop_product
  electronic_and_digital_watch <-. echoes .-> vector_display_arcade
  emblem_badge <-. echoes .-> mid_century_modern
  emblem_badge <-. echoes .-> space_age
  empire_line_dress <-. echoes .-> georgian_neoclassical_manufacture
  empire_line_dress <-. echoes .-> neoclassical_architecture
  english_bespoke_tailoring <-. echoes .-> georgian_neoclassical_manufacture
  engraving_print <-. echoes .-> victorian_trademark
  etching_print <-. echoes .-> realism_painting
  expressionism_painting <-. echoes .-> expressionist_woodcut_print
  expressionism_painting <-. echoes .-> german_expressionist_cinema
  expressionism_painting <-. echoes .-> sosaku_hanga_print
  expressionist_architecture <-. echoes .-> german_expressionist_cinema
  fantasy_console_pixel <-. echoes .-> pixel_art_web
  fashion_editorial <-. echoes .-> grunge_editorial
  fashion_editorial <-. echoes .-> new_look
  fashion_editorial <-. echoes .-> quiet_luxury_interior
  fat_face_display <-. echoes .-> victorian_trademark
  fat_face_display <-. echoes .-> victorian_web
  fat_face_display <-. echoes .-> wood_type_poster
  fauvism <-. echoes .-> new_colour
  fauvism <-. echoes .-> pochoir_plate
  fiesta_colourware <-. echoes .-> streamline_moderne_product
  fifth_gen_low_poly <-. echoes .-> y2k_aesthetic
  film_grain_revival <-. echoes .-> impressionism
  film_grain_revival <-. echoes .-> instagram_vintage_filter
  film_grain_revival <-. echoes .-> low_poly_ps1_revival
  film_grain_revival <-. echoes .-> vsco_preset_look
  film_noir <-. echoes .-> film_noir_still
  film_noir <-. echoes .-> pre_rendered_backgrounds
  film_noir_still <-. echoes .-> german_expressionist_cinema
  film_noir_still <-. echoes .-> mezzotint_print
  fireclay_butler_sink <-. echoes .-> industrial_utility_product
  fireclay_butler_sink <-. echoes .-> victorian_manufacture
  flat_design <-. echoes .-> flat_icon
  flat_design <-. echoes .-> flat_logo
  flat_design <-. echoes .-> impossible_isometric_mobile
  flat_design <-. echoes .-> minimalist_interior
  flat_design <-. echoes .-> rams_functionalism_ui
  flat_design <-. echoes .-> smartwatch
  flat_design <-. echoes .-> swiss_international
  flat_design <-. echoes .-> ukiyo_e
  flat_icon <-. echoes .-> metro_ui
  flat_icon <-. echoes .-> unicode_emoji
  flat_lay_feed <-. echoes .-> food_photography
  flat_lay_feed <-. echoes .-> scandinavian_interior_photography
  flat_logo <-. echoes .-> material_design
  flat_logo <-. echoes .-> metro_ui
  formal_script <-. echoes .-> hollywood_regency_interior
  formal_script <-. echoes .-> rococo_painting
  found_footage <-. echoes .-> liminal_spaces
  found_footage <-. echoes .-> low_poly_ps1_revival
  found_footage <-. echoes .-> y2k_digicam
  four_shade_handheld <-. echoes .-> pixel_icon
  four_shade_handheld <-. echoes .-> terminal_tui_web
  french_new_wave <-. echoes .-> street_photography
  frutiger_aero <-. echoes .-> glossy_3d_logo
  frutiger_aero <-. echoes .-> skeuomorphic_icon
  funk_ceramics <-. echoes .-> pop_art_painting
  futurism_painting <-. echoes .-> soviet_montage
  garalde_old_style <-. echoes .-> private_press_book
  garalde_old_style <-. echoes .-> renaissance_architecture
  garalde_old_style <-. echoes .-> renaissance_painting
  geometric_symbol <-. echoes .-> mid_century_modern
  georgian_interior <-. echoes .-> georgian_jewellery
  georgian_interior <-. echoes .-> georgian_neoclassical_manufacture
  georgian_interior <-. echoes .-> georgian_porcelain_tea_service
  georgian_interior <-. echoes .-> regency_gilded_bone_china
  georgian_interior <-. echoes .-> renaissance_painting
  georgian_interior <-. echoes .-> rococo_court_dress
  georgian_interior <-. echoes .-> transitional_serif
  georgian_jewellery <-. echoes .-> georgian_neoclassical_manufacture
  georgian_neoclassical_manufacture <-. echoes .-> georgian_porcelain_tea_service
  georgian_neoclassical_manufacture <-. echoes .-> jasperware_neoclassical
  georgian_neoclassical_manufacture <-. echoes .-> neoclassical_architecture
  georgian_neoclassical_manufacture <-. echoes .-> regency_gilded_bone_china
  german_expressionist_cinema <-. echoes .-> new_objectivity
  giallo <-. echoes .-> psychedelic
  glam_platform_shoe <-. echoes .-> pop_art_painting
  glam_platform_shoe <-. echoes .-> space_age_pop_product
  glitchcore <-. echoes .-> music_video
  glitchcore <-. echoes .-> vertical_short_form
  glossy_3d_logo <-. echoes .-> skeuomorphism
  glossy_3d_logo <-. echoes .-> y2k_aesthetic
  goblincore <-. echoes .-> hippie_bohemian_dress
  goblincore <-. echoes .-> mingei_folk_craft
  goblincore <-. echoes .-> naturalist_cuisine
  goblincore <-. echoes .-> organic_architecture
  googie_architecture <-. echoes .-> space_age
  googie_architecture <-. echoes .-> space_age_pop_product
  gorpcore <-. echoes .-> health_goth
  gorpcore <-. echoes .-> normcore
  gorpcore <-. echoes .-> street_photography
  gothic_architecture <-. echoes .-> medieval_court_cuisine
  gothic_architecture <-. echoes .-> victorian_architectural_terracotta
  gothic_architecture <-. echoes .-> victorian_encaustic_tiles
  grande_cuisine <-. echoes .-> neoclassical_architecture
  grandmillennial_interior <-. echoes .-> impressionism
  green_screen_short <-. echoes .-> vertical_short_form
  group_f64 <-. echoes .-> international_style_architecture
  grunge_editorial <-. echoes .-> party_flash
  grunge_editorial <-. echoes .-> street_photography
  grunge_editorial <-. echoes .-> swiss_international
  grunge_editorial <-. echoes .-> xerox_zine
  grwm_short <-. echoes .-> vertical_short_form
  hand_painted_texture <-. echoes .-> impressionism
  hd_2d_diorama <-. echoes .-> new_topographics
  hd_2d_diorama <-. echoes .-> planimetric_symmetry
  high_tech_architecture <-. echoes .-> industrial_loft_interior
  high_tech_architecture <-. echoes .-> industrial_utility_product
  high_tech_architecture <-. echoes .-> luxury_steel_sports_watch
  high_tech_architecture <-. echoes .-> space_age
  high_tech_architecture <-. echoes .-> technical_shell_alpinism
  high_tech_architecture <-. echoes .-> terracotta_rainscreen
  hippie_bohemian_dress <-. echoes .-> psychedelic
  hippie_bohemian_dress <-. echoes .-> psychedelic_concert_poster
  humanist_sans <-. echoes .-> scandinavian_interior
  hyperpop_visual <-. echoes .-> music_video
  hyperpop_visual <-. echoes .-> vertical_short_form
  impact_image_macro <-. echoes .-> pop_art_painting
  impossible_isometric_mobile <-. echoes .-> isometric_icon
  impossible_isometric_mobile <-. echoes .-> postmodern_architecture
  impossible_isometric_mobile <-. echoes .-> surrealism_painting
  impressionism <-. echoes .-> pictorialism
  industrial_loft_interior <-. echoes .-> industrial_utility_product
  industrial_loft_interior <-. echoes .-> new_topographics
  industrial_loft_interior <-. echoes .-> seventh_gen_desaturated
  industrial_utility_product <-. echoes .-> pilot_and_field_watch
  industrial_utility_product <-. echoes .-> porcelain_insulator
  industrial_utility_product <-. echoes .-> subculture_workboot
  industrial_utility_product <-. echoes .-> subway_tile
  industrial_utility_product <-. echoes .-> trench_and_field_military
  international_style_architecture <-. echoes .-> large_format_porcelain_tiles
  international_style_architecture <-. echoes .-> mid_century_modern_interior
  international_style_architecture <-. echoes .-> minimalist_interior
  international_style_architecture <-. echoes .-> neo_grotesque_sans
  international_style_architecture <-. echoes .-> new_topographics
  international_style_architecture <-. echoes .-> rams_functionalism_ui
  international_style_architecture <-. echoes .-> straight_photography
  international_style_architecture <-. echoes .-> subway_tile
  international_style_architecture <-. echoes .-> swiss_international
  international_style_architecture <-. echoes .-> swiss_modernist_mark
  isometric_icon <-. echoes .-> isometric_pixel_world
  it_bag <-. echoes .-> y2k_aesthetic
  italian_neorealism <-. echoes .-> street_photography
  japandi_interior <-. echoes .-> japanese_modern_craft_product
  japandi_interior <-. echoes .-> minimalism_painting
  japandi_interior <-. echoes .-> scandinavian_interior_photography
  japandi_interior <-. echoes .-> ukiyo_e
  japandi_interior <-. echoes .-> wabi_sabi_web
  japanese_avant_garde_fashion <-. echoes .-> japanese_graphic_modernism
  japanese_avant_garde_fashion <-. echoes .-> wabi_sabi_web
  japanese_dense_web <-. echoes .-> swiss_international
  japanese_graphic_modernism <-. echoes .-> swiss_modernist_mark
  japanese_graphic_modernism <-. echoes .-> ukiyo_e
  japanese_modern_craft_product <-. echoes .-> mingei_folk_craft
  japanese_modern_craft_product <-. echoes .-> mino_tea_ceramics
  japanese_modern_craft_product <-. echoes .-> raku_tea_bowl
  japanese_modern_craft_product <-. echoes .-> washlet_toilet
  jasperware_neoclassical <-. echoes .-> neoclassical_architecture
  kaomoji_emoticon <-. echoes .-> pixel_icon
  katagami_stencil_print <-. echoes .-> mingei_folk_craft
  kidcore <-. echoes .-> memphis_interior
  kidcore <-. echoes .-> memphis_product
  kidcore <-. echoes .-> pop_art_web
  large_format_porcelain_tiles <-. echoes .-> minimalist_interior
  liminal_spaces <-. echoes .-> low_poly_ps1_revival
  liminal_spaces <-. echoes .-> new_topographics
  lip_sync_dance_short <-. echoes .-> music_video
  lip_sync_dance_short <-. echoes .-> vertical_short_form
  logomania <-. echoes .-> pop_art_painting
  logomania <-. echoes .-> pop_screen_print
  low_poly_ps1_revival <-. echoes .-> weirdcore
  luxury_typography_web <-. echoes .-> quiet_luxury_interior
  luxury_typography_web <-. echoes .-> swiss_international
  malletier_luggage <-. echoes .-> victorian_manufacture
  malletier_luggage <-. echoes .-> victorian_trademark
  mass_timber_architecture <-. echoes .-> scandinavian_interior
  material_design <-. echoes .-> material_symbols_icon
  material_design <-. echoes .-> smartwatch
  memphis_design <-. echoes .-> memphis_interior
  memphis_design <-. echoes .-> memphis_postmodern_ceramics
  memphis_design <-. echoes .-> memphis_product
  memphis_design <-. echoes .-> music_video
  memphis_design <-. echoes .-> pop_art_painting
  memphis_design <-. echoes .-> pop_art_web
  memphis_design <-. echoes .-> postmodern_architecture
  memphis_design <-. echoes .-> radical_architecture
  memphis_design <-. echoes .-> swiss_international
  memphis_design <-. echoes .-> swiss_plastic_pop_watch
  memphis_interior <-. echoes .-> memphis_postmodern_ceramics
  memphis_interior <-. echoes .-> memphis_product
  memphis_interior <-. echoes .-> postmodern_architecture
  memphis_postmodern_ceramics <-. echoes .-> memphis_product
  memphis_product <-. echoes .-> swiss_plastic_pop_watch
  metro_ui <-. echoes .-> swiss_international
  mid_century_eyewear <-. echoes .-> mid_century_modern_product
  mid_century_modern <-. echoes .-> mid_century_modern_architecture
  mid_century_modern <-. echoes .-> mid_century_modern_interior
  mid_century_modern <-. echoes .-> mid_century_modern_product
  mid_century_modern <-. echoes .-> punk_zine
  mid_century_modern_architecture <-. echoes .-> mid_century_modern_interior
  mid_century_modern_architecture <-. echoes .-> mid_century_modern_product
  mid_century_modern_architecture <-. echoes .-> space_age
  mid_century_modern_interior <-. echoes .-> mid_century_modern_product
  mid_century_modern_interior <-. echoes .-> space_age
  mid_century_modern_product <-. echoes .-> modernist_studio_jewellery
  mid_century_modern_product <-. echoes .-> organic_modern_tableware
  mid_century_modern_product <-. echoes .-> racing_chronograph
  mid_century_modern_product <-. echoes .-> scandinavian_modern_tableware
  mingei_folk_craft <-. echoes .-> russian_lubok_print
  minimal_wordmark <-. echoes .-> minimalist_interior
  minimal_wordmark <-. echoes .-> rams_functionalism_ui
  minimalism_painting <-. echoes .-> minimalist_fashion
  minimalism_painting <-. echoes .-> rams_functionalism_ui
  minimalism_painting <-. echoes .-> swiss_international
  minimalism_web <-. echoes .-> minimalist_fashion
  minimalism_web <-. echoes .-> minimalist_interior
  minimalism_web <-. echoes .-> super_normal_product
  minimalism_web <-. echoes .-> swiss_international
  minimalist_fashion <-. echoes .-> minimalist_interior
  minimalist_fashion <-. echoes .-> normcore
  minimalist_interior <-. echoes .-> nouvelle_cuisine
  minimalist_interior <-. echoes .-> rams_functionalism_ui
  minimalist_interior <-. echoes .-> super_normal_product
  mod_and_mini <-. echoes .-> pop_art_painting
  mod_and_mini <-. echoes .-> pop_art_web
  monospace <-. echoes .-> terminal_tui_web
  mumblecore <-. echoes .-> photo_dump
  muscle_and_pony_car <-. echoes .-> space_age_pop_product
  music_video <-. echoes .-> velocity_edit
  music_video <-. echoes .-> y2k_aesthetic
  myspace_profile <-. echoes .-> y2k_digicam
  neo_grotesque_sans <-. echoes .-> swiss_international
  neoclassical_architecture <-. echoes .-> parian_statuary
  neoclassical_architecture <-. echoes .-> transitional_serif
  neon_noir <-. echoes .-> synthwave_web
  new_hollywood <-. echoes .-> street_photography
  new_nordic <-. echoes .-> scandinavian_interior
  new_nordic <-. echoes .-> scandinavian_modern_product
  new_topographics <-. echoes .-> normcore
  new_topographics <-. echoes .-> photorealism
  new_topographics <-. echoes .-> planimetric_symmetry
  new_topographics <-. echoes .-> slow_cinema
  nishiki_e_polychrome_woodblock <-. echoes .-> ukiyo_e
  nordic_functional_outdoor <-. echoes .-> scandinavian_modern_product
  nordic_modernism_architecture <-. echoes .-> scandinavian_interior
  nordic_modernism_architecture <-. echoes .-> scandinavian_modern_product
  nordic_modernism_architecture <-. echoes .-> scandinavian_modern_tableware
  nordic_national_romanticism_painting <-. echoes .-> scandinavian_interior
  normcore <-. echoes .-> super_normal_product
  organic_architecture <-. echoes .-> organic_modern_tableware
  organic_architecture <-. echoes .-> scandinavian_interior
  organic_architecture <-. echoes .-> trencadis
  organic_modern_tableware <-. echoes .-> streamline_moderne_product
  outline_icon <-. echoes .-> rams_functionalism_ui
  outline_icon <-. echoes .-> swiss_international
  parian_statuary <-. echoes .-> victorian_manufacture
  party_flash <-. echoes .-> photo_dump
  party_flash <-. echoes .-> y2k_aesthetic
  pbr_photoreal <-. echoes .-> photorealism
  photo_carousel_slideshow <-. echoes .-> vertical_short_form
  photo_dump <-. echoes .-> y2k_digicam
  photogravure_print <-. echoes .-> pictorialism
  pictorialism <-. echoes .-> victorian_interior
  pixel_art_web <-. echoes .-> pixel_icon
  pixel_art_web <-. echoes .-> sixteen_bit_sprite
  pixel_art_web <-. echoes .-> voxel_block_world
  planimetric_symmetry <-. echoes .-> renaissance_painting
  pop_art_painting <-. echoes .-> pop_art_web
  pop_art_painting <-. echoes .-> pop_foam_furniture
  pop_art_painting <-. echoes .-> pop_screen_print
  pop_art_painting <-. echoes .-> radical_architecture
  pop_art_painting <-. echoes .-> space_age_pop_product
  pop_art_painting <-. echoes .-> swiss_plastic_pop_watch
  pop_art_web <-. echoes .-> pop_screen_print
  pop_foam_furniture <-. echoes .-> radical_architecture
  porcelain_insulator <-. echoes .-> victorian_manufacture
  pov_short <-. echoes .-> vertical_short_form
  psychedelic <-. echoes .-> psychedelic_concert_poster
  psychedelic_concert_poster <-. echoes .-> surrealism_painting
  punk_fashion <-. echoes .-> punk_zine
  punk_fashion <-. echoes .-> xerox_zine
  punk_zine <-. echoes .-> subculture_workboot
  punk_zine <-. echoes .-> swiss_international
  punk_zine <-. echoes .-> victorian_web
  punk_zine <-. echoes .-> xerox_zine
  quiet_luxury_fashion <-. echoes .-> quiet_luxury_interior
  quiet_luxury_interior <-. echoes .-> stealth_luxury_accessory
  racing_chronograph <-. echoes .-> swiss_international
  raku_tea_bowl <-. echoes .-> wabi_sabi_web
  rams_functionalism_ui <-. echoes .-> ulm_braun_functionalism
  reaction_gif <-. echoes .-> vertical_short_form
  realism_painting <-. echoes .-> straight_photography
  renaissance_architecture <-. echoes .-> renaissance_banquet
  renaissance_architecture <-. echoes .-> renaissance_painting
  renaissance_painting <-. echoes .-> woodcut_relief_print
  retro_cocktail_jewellery <-. echoes .-> streamline_moderne_product
  rococo_court_dress <-. echoes .-> rococo_painting
  rococo_court_dress <-. echoes .-> rococo_porcelain_figures
  rococo_court_dress <-. echoes .-> sevres_rococo_porcelain
  rococo_painting <-. echoes .-> rococo_porcelain_figures
  rococo_painting <-. echoes .-> sevres_rococo_porcelain
  scandinavian_interior <-. echoes .-> scandinavian_interior_photography
  scandinavian_interior <-. echoes .-> scandinavian_modern_product
  scandinavian_interior <-. echoes .-> scandinavian_modern_tableware
  scandinavian_interior <-. echoes .-> scandinavian_tiled_stove
  scandinavian_modern_product <-. echoes .-> scandinavian_modern_tableware
  seapunk <-. echoes .-> y2k_digicam
  shaker_interior <-. echoes .-> shaker_object
  sixteen_bit_sprite <-. echoes .-> ukiyo_e
  skeuomorphic_icon <-. echoes .-> skeuomorphism
  skeuomorphic_icon <-. echoes .-> web_2_0_gloss
  slab_serif <-. echoes .-> victorian_interior
  slab_serif <-. echoes .-> victorian_web
  slab_serif <-. echoes .-> wood_type_poster
  smartwatch <-. echoes .-> super_normal_product
  solid_glyph_icon <-. echoes .-> swiss_international
  space_age <-. echoes .-> space_age_couture
  space_age <-. echoes .-> space_age_pop_product
  space_age_couture <-. echoes .-> space_age_pop_product
  space_age_pop_product <-. echoes .-> tailfin_era_car
  space_age_pop_product <-. echoes .-> wedge_design_car
  space_age_pop_product <-. echoes .-> west_german_fat_lava
  space_age_pop_product <-. echoes .-> y2k_aesthetic
  staffordshire_figures <-. echoes .-> victorian_manufacture
  straight_photography <-. echoes .-> swiss_international
  streamline_car <-. echoes .-> streamline_moderne_product
  super_normal_product <-. echoes .-> washlet_toilet
  suprematism <-. echoes .-> suprematist_porcelain
  surreal_meme <-. echoes .-> surrealism_painting
  surrealism_painting <-. echoes .-> surrealism_web
  surrealism_painting <-. echoes .-> vaporwave
  swiss_international <-. echoes .-> swiss_modernist_mark
  swiss_international <-. echoes .-> ulm_braun_functionalism
  swiss_international <-. echoes .-> wabi_sabi_web
  synthwave_web <-. echoes .-> vector_display_arcade
  tumblr_soft_grunge <-. echoes .-> y2k_digicam
  velocity_edit <-. echoes .-> vertical_short_form
  vertical_short_form <-. echoes .-> word_caption_clip
  victorian_architectural_terracotta <-. echoes .-> victorian_interior
  victorian_architectural_terracotta <-. echoes .-> victorian_manufacture
  victorian_encaustic_tiles <-. echoes .-> victorian_interior
  victorian_encaustic_tiles <-. echoes .-> victorian_manufacture
  victorian_interior <-. echoes .-> victorian_manufacture
  victorian_interior <-. echoes .-> victorian_millinery
  victorian_interior <-. echoes .-> victorian_sanitary_ware
  victorian_interior <-. echoes .-> victorian_sentimental_jewellery
  victorian_interior <-. echoes .-> victorian_trademark
  victorian_manufacture <-. echoes .-> victorian_millinery
  victorian_manufacture <-. echoes .-> victorian_sanitary_ware
  victorian_manufacture <-. echoes .-> victorian_sentimental_jewellery
  victorian_trademark <-. echoes .-> victorian_web
  victorian_trademark <-. echoes .-> wood_type_poster
  victorian_web <-. echoes .-> wood_type_poster
  y2k_aesthetic <-. echoes .-> y2k_digicam
  unicode_emoji --> 3d_avatar_emoji
  cubism_painting --> abstract_expressionism
  surrealism_painting --> abstract_expressionism
  mingei_folk_craft --> abstract_expressionist_ceramics
  gan_portrait --> ai_avatar_portrait
  flat_design --> ai_chat_ui
  cinematic_teal_orange --> ai_hyperreal
  fashion_editorial --> ai_hyperreal
  diffusion_gloss --> ai_slop
  hispano_moresque_lustreware --> albarello_apothecary_ware
  arts_and_crafts_art_pottery --> american_art_pottery
  breguet_classical_watch --> american_pocket_watch
  rhenish_salt_glaze_stoneware --> american_stoneware_crock
  arts_and_crafts_art_pottery --> anglo_oriental_studio_pottery
  joseon_buncheong --> anglo_oriental_studio_pottery
  longquan_celadon --> anglo_oriental_studio_pottery
  y2k_aesthetic --> apple_aqua
  etching_print --> aquatint_print
  new_objectivity --> architectural_photography
  straight_photography --> architectural_photography
  art_nouveau_architecture --> art_deco_architecture
  rococo_porcelain_figures --> art_deco_ceramic_figures
  victorian_boot --> art_deco_dance_shoe
  garconne_flapper_dress --> art_deco_evening_accessory
  chicago_school_terracotta --> art_deco_faience_facade
  garland_style_jewellery --> art_deco_jewellery
  art_nouveau_object --> art_deco_product
  art_nouveau_ceramics --> art_deco_tableware
  early_wristwatch --> art_deco_watch
  american_art_pottery --> art_nouveau_ceramics
  arts_and_crafts_art_pottery --> art_nouveau_ceramics
  arts_and_crafts_interior --> art_nouveau_interior
  arts_and_crafts_jewellery --> art_nouveau_jewellery
  victorian_trademark --> art_nouveau_monogram
  arts_and_crafts_object --> art_nouveau_object
  art_nouveau_ceramics --> art_nouveau_tiles
  delft_tiles --> art_nouveau_tiles
  victorian_encaustic_tiles --> art_nouveau_tiles
  greek_black_figure --> artist_ceramics_vallauris
  hispano_moresque_lustreware --> artist_ceramics_vallauris
  gothic_architecture --> arts_and_crafts_architecture
  hispano_moresque_lustreware --> arts_and_crafts_art_pottery
  rhenish_salt_glaze_stoneware --> arts_and_crafts_art_pottery
  shaker_interior --> arts_and_crafts_interior
  shaker_object --> arts_and_crafts_object
  unboxing_video --> asmr_video
  flat_design --> aurora_gradient_ui
  hispano_moresque_lustreware --> azulejo
  islamic_tile_mosaic --> azulejo
  istoriato_maiolica --> azulejo
  engraving_print --> banknote_engraving_print
  y2k_aesthetic --> barbiecore
  renaissance_architecture --> baroque_architecture
  renaissance_painting --> baroque_painting
  woodcut_relief_print --> battala_woodcut
  creamware_neoclassical --> bauhaus_modern_tableware
  arts_and_crafts_object --> bauhaus_product
  industrial_utility_product --> bauhaus_product
  baroque_architecture --> beaux_arts_architecture
  neoclassical_architecture --> beaux_arts_architecture
  chromolithograph_poster --> ben_day_comic_print
  flat_design --> bento_grid_ui
  garconne_flapper_dress --> bias_cut_glamour
  streamline_car --> biodesign_car
  rococo_porcelain_figures --> biscuit_porcelain_figures
  haute_regionale --> bistronomie
  nouvelle_cuisine --> bistronomie
  creamware_neoclassical --> blue_willow_transferware
  kraak_porcelain --> blue_willow_transferware
  art_nouveau_ceramics --> british_modernist_studio
  international_style_architecture --> brutalist_architecture
  modernist_studio_jewellery --> brutalist_jewellery
  usenet_thread --> bulletin_board_forum
  nouvelle_cuisine --> california_cuisine
  fifth_gen_low_poly --> cel_shaded_3d
  unicode_emoji --> chat_sticker_pack
  scandinavian_modern_tableware --> chef_studio_tableware
  woodcut_relief_print --> chiaroscuro_woodcut_print
  victorian_architectural_terracotta --> chicago_school_terracotta
  pop_screen_print --> chicha_poster
  expressionist_woodcut_print --> chinese_modern_woodcut
  woodcut_relief_print --> chinese_modern_woodcut
  reaction_gif --> cinemagraph
  new_colour --> cinematic_teal_orange
  german_expressionist_cinema --> classical_hollywood
  skeuomorphic_icon --> clay_3d_icon
  neumorphism --> claymorphism
  minimalism_web --> clean_girl
  normcore --> clean_girl
  scandinavian_interior --> coastal_interior
  flat_lay_feed --> cohesive_feed_grid
  vsco_preset_look --> cohesive_feed_grid
  abstract_expressionism --> colour_field_painting
  victorian_sanitary_ware --> coloured_bathroom_suite
  rosta_window_stencil_poster --> constructivist_photomontage_poster
  arts_and_crafts_object --> contemporary_craft_product
  japanese_modern_craft_product --> contemporary_craft_product
  woodcut_relief_print --> cordel_xilogravura
  mocha_banded_ware --> cornishware
  flat_design --> corporate_memphis
  memphis_design --> corporate_memphis
  georgian_jewellery --> costume_jewellery
  bohemian_web --> cottagecore
  wabi_sabi_web --> cottagecore
  english_bespoke_tailoring --> country_sporting_tweed
  english_slipware --> creamware_neoclassical
  empire_line_dress --> crinoline_and_bustle_dress
  nordic_modernism_architecture --> critical_regionalism_architecture
  grande_cuisine --> cuisine_classique
  renaissance_banquet --> cuisine_francoise
  nouvelle_cuisine --> cuisine_minceur
  dark_devtool_ui --> cybercore_web
  y2k_aesthetic --> cybercore_web
  flat_design --> dark_devtool_ui
  cubism_painting --> de_stijl_painting
  deepdream_psychedelia --> deepfake_face_swap
  azulejo --> delft_tiles
  istoriato_maiolica --> delft_tiles
  kraak_porcelain --> delft_tiles
  istoriato_maiolica --> delftware
  kraak_porcelain --> delftware
  hispano_moresque_lustreware --> della_robbia_relief
  modern_mens_briefs --> designer_logo_underwear
  coloured_bathroom_suite --> designer_wall_hung_sanitary
  transitional_serif --> didone_serif
  gan_portrait --> diffusion_gloss
  british_modernist_studio --> digital_3d_printed_ceramics
  pilot_and_field_watch --> dive_watch
  straight_photography --> documentary_photography
  soviet_montage --> documentary_verite
  woodcut_relief_print --> dong_ho_folk_woodblock
  memphis_interior --> dopamine_decor
  vaporwave --> dreamcore
  engraving_print --> drypoint_print
  photo_dump --> dual_camera_snapshot
  new_objectivity --> duesseldorf_school
  new_topographics --> duesseldorf_school
  lip_sync_dance_short --> duet_split_screen
  outline_icon --> duotone_icon
  solid_glyph_icon --> duotone_icon
  country_sporting_tweed --> early_mountaineering
  biodesign_car --> electric_minimal_car
  victorian_trademark --> emblem_badge
  victorian_boot --> english_welted_dress_shoe
  engraving_print --> etching_print
  aurora_gradient_ui --> ethereal_web
  glassmorphism --> ethereal_web
  post_impressionism --> expressionism_painting
  art_nouveau_architecture --> expressionist_architecture
  woodcut_relief_print --> expressionist_woodcut_print
  kakiemon_imari_export --> famille_rose_qing
  yuan_ming_blue_and_white --> famille_rose_qing
  pictorialism --> fashion_editorial
  straight_photography --> fashion_editorial
  didone_serif --> fat_face_display
  pointillism --> fauvism
  art_deco_tableware --> fiesta_colourware
  new_colour --> film_grain_revival
  street_photography --> film_grain_revival
  german_expressionist_cinema --> film_noir
  straight_photography --> film_noir_still
  victorian_sanitary_ware --> fireclay_butler_sink
  cyberdelia --> flash_intro_site
  y2k_aesthetic --> flash_intro_site
  flat_design --> flat_lay_feed
  geometric_symbol --> flat_logo
  straight_photography --> food_photography
  documentary_verite --> found_footage
  eight_bit_tile --> four_shade_handheld
  italian_neorealism --> french_new_wave
  soviet_montage --> french_new_wave
  y2k_aesthetic --> frutiger_aero
  abstract_expressionist_ceramics --> funk_ceramics
  artist_ceramics_vallauris --> funk_ceramics
  cubism_painting --> futurism_painting
  deepdream_psychedelia --> gan_portrait
  georgian_jewellery --> garland_style_jewellery
  cyberdelia --> geocities_homepage
  swiss_modernist_mark --> geometric_symbol
  kraak_porcelain --> georgian_porcelain_tea_service
  meissen_baroque_porcelain --> georgian_porcelain_tea_service
  german_expressionist_cinema --> giallo
  stiletto_heel --> glam_platform_shoe
  frutiger_aero --> glassmorphism
  reaction_gif --> glitch_gif
  y2k_aesthetic --> glitchcore
  geometric_symbol --> glossy_3d_logo
  cottagecore --> goblincore
  art_deco_architecture --> googie_architecture
  technical_shell_alpinism --> gorpcore
  longquan_celadon --> goryeo_celadon
  cuisine_francoise --> grande_cuisine
  georgian_interior --> grandmillennial_interior
  victorian_interior --> grandmillennial_interior
  greek_black_figure --> greek_red_figure
  straight_photography --> group_f64
  fifth_gen_low_poly --> hand_painted_texture
  cuisine_classique --> haute_regionale
  sixteen_bit_sprite --> hd_2d_diorama
  vaporwave --> health_goth
  international_style_architecture --> high_tech_architecture
  abbasid_lustreware --> hispano_moresque_lustreware
  art_deco_interior --> hollywood_regency_interior
  georgian_interior --> hollywood_regency_interior
  new_hollywood --> hong_kong_action
  garalde_old_style --> humanist_sans
  islamic_tile_mosaic --> hungarian_secession_ceramics
  victorian_architectural_terracotta --> hungarian_secession_ceramics
  frutiger_aero --> hyperpop_visual
  y2k_aesthetic --> hyperpop_visual
  isometric_pixel_world --> impossible_isometric_mobile
  realism_painting --> impressionism
  bauhaus_interior --> industrial_loft_interior
  victorian_manufacture --> industrial_utility_product
  skeuomorphism --> instagram_vintage_filter
  abbasid_lustreware --> islamic_tile_mosaic
  pixel_icon --> isometric_icon
  eight_bit_tile --> isometric_pixel_world
  hispano_moresque_lustreware --> istoriato_maiolica
  ladylike_handbag --> it_bag
  logomania --> it_bag
  streamline_car --> italian_gran_turismo
  vintage_coachbuilt_car --> italian_gran_turismo
  english_bespoke_tailoring --> ivy_style
  islamic_tile_mosaic --> iznik_pottery
  yuan_ming_blue_and_white --> iznik_pottery
  islamic_tile_mosaic --> iznik_tiles
  iznik_pottery --> iznik_tiles
  yuan_ming_blue_and_white --> iznik_tiles
  scandinavian_interior --> japandi_interior
  bauhaus --> japanese_graphic_modernism
  swiss_international --> japanese_graphic_modernism
  arts_and_crafts_object --> japanese_modern_craft_product
  creamware_neoclassical --> jasperware_neoclassical
  greek_red_figure --> jasperware_neoclassical
  goryeo_celadon --> joseon_buncheong
  joseon_buncheong --> joseon_moon_jar
  yuan_ming_blue_and_white --> joseon_moon_jar
  kraak_porcelain --> kakiemon_imari_export
  yuan_ming_blue_and_white --> kakiemon_imari_export
  ansi_bbs_art --> kaomoji_emoticon
  scrapbook_ui --> kidcore
  y2k_aesthetic --> kidcore
  yuan_ming_blue_and_white --> kraak_porcelain
  mino_tea_ceramics --> kyo_yaki_overglaze
  raku_tea_bowl --> kyo_yaki_overglaze
  impact_image_macro --> label_meme
  art_deco_evening_accessory --> ladylike_handbag
  new_look --> ladylike_handbag
  subway_tile --> large_format_porcelain_tiles
  victorian_encaustic_tiles --> large_format_porcelain_tiles
  unboxing_video --> lets_play_facecam
  vaporwave --> liminal_spaces
  expressionist_woodcut_print --> linocut_print
  woodcut_relief_print --> linocut_print
  glassmorphism --> liquid_glass_ui
  spatial_visionos --> liquid_glass_ui
  tang_sancai_figures --> liuli_glazed_roof
  lets_play_facecam --> livestream_overlay
  malletier_luggage --> logomania
  fifth_gen_low_poly --> low_poly_ps1_revival
  dive_watch --> luxury_steel_sports_watch
  renaissance_painting --> mannerism_painting
  flat_design --> material_design
  flat_icon --> material_symbols_icon
  solid_glyph_icon --> material_symbols_icon
  nishiki_e_polychrome_woodblock --> meiji_kosen_ga_print
  kraak_porcelain --> meissen_baroque_porcelain
  art_deco_tableware --> memphis_postmodern_ceramics
  space_age_pop_product --> memphis_product
  international_style_architecture --> metabolism_architecture
  engraving_print --> mezzotint_print
  bauhaus --> mid_century_modern
  international_style_architecture --> mid_century_modern_architecture
  prairie_school_architecture --> mid_century_modern_architecture
  bauhaus_interior --> mid_century_modern_interior
  bauhaus_product --> mid_century_modern_product
  scandinavian_modern_product --> mid_century_modern_product
  joseon_buncheong --> mingei_folk_craft
  mino_tea_ceramics --> mingei_folk_craft
  gan_portrait --> mini_diffusion_meme
  swiss_modernist_mark --> minimal_wordmark
  de_stijl_painting --> minimalism_painting
  suprematism --> minimalism_painting
  flat_design --> minimalism_web
  bias_cut_glamour --> minimalist_fashion
  bauhaus_interior --> minimalist_interior
  jian_tenmoku_ware --> mino_tea_ceramics
  chromolithograph_poster --> mir_iskusstva_book_graphics
  russian_lubok_print --> mir_iskusstva_book_graphics
  english_slipware --> mocha_banded_ware
  english_bespoke_tailoring --> mod_and_mini
  ivy_style --> mod_and_mini
  molecular_gastronomy --> modernist_cuisine
  arts_and_crafts_jewellery --> modernist_studio_jewellery
  nouvelle_cuisine --> molecular_gastronomy
  slab_serif --> monospace
  dogme_95 --> mumblecore
  italian_gran_turismo --> muscle_and_pony_car
  geocities_homepage --> myspace_profile
  engraving_print --> narbut_ukrainian_graphics
  mir_iskusstva_book_graphics --> narbut_ukrainian_graphics
  nouvelle_cuisine --> naturalist_cuisine
  flat_design --> neo_brutalism_ui
  art_deco_interior --> neo_deco_interior
  grotesque_sans --> neo_grotesque_sans
  film_noir --> neon_noir
  ansi_bbs_art --> net_art_browser
  skeuomorphism --> neumorphism
  street_photography --> new_colour
  french_new_wave --> new_hollywood
  crinoline_and_bustle_dress --> new_look
  naturalist_cuisine --> new_nordic
  straight_photography --> new_objectivity
  straight_photography --> new_topographics
  woodcut_relief_print --> nianhua_new_year_print
  woodcut_relief_print --> nishiki_e_polychrome_woodblock
  early_mountaineering --> nordic_functional_outdoor
  international_style_architecture --> nordic_modernism_architecture
  minimalism_web --> normcore
  cuisine_classique --> nouvelle_cuisine
  nouvelle_cuisine --> novoandina_and_nikkei
  straight_front_corset --> nylon_foundation_garments
  classical_hollywood --> one_take_oner
  art_nouveau_architecture --> organic_architecture
  prairie_school_architecture --> organic_architecture
  art_deco_tableware --> organic_modern_tableware
  bauhaus_modern_tableware --> organic_modern_tableware
  cubism_painting --> orphism
  flat_icon --> outline_icon
  california_cuisine --> pacific_rim_fusion
  nouvelle_cuisine --> pacific_rim_fusion
  deconstructivist_architecture --> parametricism_architecture
  biscuit_porcelain_figures --> parian_statuary
  y2k_digicam --> party_flash
  seventh_gen_desaturated --> pbr_photoreal
  canvas_court_sneaker --> performance_running_shoe
  dogme_95 --> phone_cinema
  mumblecore --> phone_cinema
  grwm_short --> photo_carousel_slideshow
  aquatint_print --> photogravure_print
  pop_art_painting --> photorealism
  early_wristwatch --> pilot_and_field_watch
  y2k_aesthetic --> pixel_art_web
  new_nordic --> plant_based_fine_dining
  impressionism --> pointillism
  mid_century_modern --> pop_art_web
  ben_day_comic_print --> pop_screen_print
  meissen_baroque_porcelain --> porcelain_insulator
  engraving_print --> posada_broadside
  woodcut_relief_print --> posada_broadside
  impressionism --> post_impressionism
  english_bespoke_tailoring --> power_dressing
  sixteen_bit_sprite --> pre_rendered_backgrounds
  woodcut_relief_print --> private_press_book
  chromolithograph_poster --> psychedelic_concert_poster
  minimalist_fashion --> quiet_luxury_fashion
  japandi_interior --> quiet_luxury_interior
  early_mountaineering --> quilted_down_outerwear
  dive_watch --> racing_chronograph
  pilot_and_field_watch --> racing_chronograph
  impact_image_macro --> rage_comic
  bauhaus --> rams_functionalism_ui
  swiss_international --> rams_functionalism_ui
  chromolithograph_poster --> ravi_varma_oleograph
  cubism_painting --> rayonism
  futurism_painting --> rayonism
  kaomoji_emoticon --> reaction_gif
  creamware_neoclassical --> regency_gilded_bone_china
  sevres_rococo_porcelain --> regency_gilded_bone_china
  medieval_court_cuisine --> renaissance_banquet
  art_deco_jewellery --> retro_cocktail_jewellery
  muscle_and_pony_car --> retro_revival_car
  xerox_zine --> risograph_print
  baroque_painting --> rococo_painting
  meissen_baroque_porcelain --> rococo_porcelain_figures
  greek_red_figure --> roman_terra_sigillata
  russian_lubok_print --> rosta_window_stencil_poster
  woodcut_relief_print --> russian_lubok_print
  shaker_interior --> scandinavian_interior
  new_objectivity --> scandinavian_interior_photography
  arts_and_crafts_object --> scandinavian_modern_product
  bauhaus_product --> scandinavian_modern_product
  bauhaus_modern_tableware --> scandinavian_modern_tableware
  organic_modern_tableware --> scandinavian_modern_tableware
  delft_tiles --> scandinavian_tiled_stove
  corporate_memphis --> scrapbook_ui
  punk_zine --> scrapbook_ui
  y2k_aesthetic --> seapunk
  nishiki_e_polychrome_woodblock --> senjafuda_slip
  fifth_gen_low_poly --> seventh_gen_desaturated
  meissen_baroque_porcelain --> sevres_rococo_porcelain
  nylon_foundation_garments --> shapewear_and_seamless
  soft_natural_lingerie --> shapewear_and_seamless
  nishiki_e_polychrome_woodblock --> shin_hanga_print
  eight_bit_tile --> sixteen_bit_sprite
  pixel_icon --> skeuomorphic_icon
  didone_serif --> slab_serif
  italian_neorealism --> slow_cinema
  electronic_and_digital_watch --> smartwatch
  canvas_court_sneaker --> sneaker_culture
  performance_running_shoe --> sneaker_culture
  flat_icon --> solid_glyph_icon
  pixel_icon --> solid_glyph_icon
  woodcut_relief_print --> sosaku_hanga_print
  mid_century_modern --> space_age
  mod_and_mini --> space_age_couture
  mid_century_modern_product --> space_age_pop_product
  glassmorphism --> spatial_visionos
  mocha_banded_ware --> spongeware
  english_slipware --> staffordshire_figures
  impact_image_macro --> starter_pack
  english_bespoke_tailoring --> stealth_luxury_accessory
  minimalist_fashion --> stealth_luxury_accessory
  art_deco_dance_shoe --> stiletto_heel
  engraving_print --> stipple_engraving_print
  etching_print --> stipple_engraving_print
  victorian_corsetry --> straight_front_corset
  art_deco_product --> streamline_moderne_product
  straight_photography --> street_photography
  ivy_style --> streetwear
  delft_tiles --> subway_tile
  victorian_encaustic_tiles --> subway_tile
  ulm_braun_functionalism --> super_normal_product
  cubism_painting --> suprematism
  futurism_painting --> suprematism
  nishiki_e_polychrome_woodblock --> surimono_print
  vaporwave --> surrealism_web
  bauhaus --> swiss_international
  electronic_and_digital_watch --> swiss_plastic_pop_watch
  post_impressionism --> synthetism
  vaporwave --> synthwave_web
  y2k_aesthetic --> synthwave_web
  streamline_car --> tailfin_era_car
  posada_broadside --> taller_grafica_popular_linocut
  woodcut_relief_print --> taller_grafica_popular_linocut
  qin_terracotta_warriors --> tang_sancai_figures
  nordic_functional_outdoor --> technical_shell_alpinism
  technical_shell_alpinism --> techwear
  woodcut_relief_print --> ten_bamboo_studio_polychrome
  art_deco_faience_facade --> terracotta_rainscreen
  victorian_architectural_terracotta --> terracotta_rainscreen
  documentary_verite --> third_cinema
  soviet_montage --> third_cinema
  garalde_old_style --> transitional_serif
  azulejo --> trencadis
  zellige --> trencadis
  country_sporting_tweed --> trench_and_field_military
  grunge_editorial --> tumblr_soft_grunge
  impact_image_macro --> tweet_screenshot_meme
  bauhaus_product --> ulm_braun_functionalism
  nylon_foundation_garments --> underwear_as_outerwear
  victorian_corsetry --> underwear_as_outerwear
  kaomoji_emoticon --> unicode_emoji
  y2k_aesthetic --> vaporwave
  lip_sync_dance_short --> velocity_edit
  creator_vlog --> vertical_short_form
  della_robbia_relief --> victorian_architectural_terracotta
  victorian_encaustic_tiles --> victorian_architectural_terracotta
  whalebone_stays --> victorian_corsetry
  delft_tiles --> victorian_encaustic_tiles
  islamic_tile_mosaic --> victorian_encaustic_tiles
  georgian_interior --> victorian_interior
  georgian_neoclassical_manufacture --> victorian_manufacture
  empire_line_dress --> victorian_millinery
  blue_willow_transferware --> victorian_sanitary_ware
  georgian_jewellery --> victorian_sentimental_jewellery
  lets_play_facecam --> video_essay
  brass_era_car --> vintage_coachbuilt_car
  eight_bit_tile --> voxel_block_world
  livestream_overlay --> vtuber_avatar
  coloured_bathroom_suite --> washlet_toilet
  apple_aqua --> web_2_0_gloss
  italian_gran_turismo --> wedge_design_car
  vaporwave --> weirdcore
  organic_modern_tableware --> west_german_fat_lava
  rage_comic --> wojak_feels
  woodcut_relief_print --> wood_engraving_print
  woodcut_relief_print --> wood_type_poster
  clickbait_thumbnail --> word_caption_clip
  new_colour --> y2k_digicam
  ding_white_ware --> yuan_ming_blue_and_white
  chromolithograph_poster --> yuefenpai_calendar_poster
  islamic_tile_mosaic --> zellige
  abstract_expressionism -. rejects .-> de_stijl_painting
  abstract_expressionist_ceramics -. rejects .-> anglo_oriental_studio_pottery
  adaptive_reuse_architecture -. rejects .-> international_style_architecture
  americana_workwear -. rejects .-> english_bespoke_tailoring
  anti_design -. rejects .-> flat_design
  anti_design -. rejects .-> material_design
  are_bure_boke -. rejects .-> documentary_photography
  art_deco_ceramic_figures -. rejects .-> parian_statuary
  art_deco_interior -. rejects .-> art_nouveau_interior
  art_deco_jewellery -. rejects .-> art_nouveau_jewellery
  art_deco_product -. rejects .-> arts_and_crafts_object
  art_deco_tableware -. rejects .-> blue_willow_transferware
  art_deco_watch -. rejects .-> garland_style_jewellery
  art_deco_web -. rejects .-> art_nouveau_web
  art_nouveau_interior -. rejects .-> victorian_interior
  art_nouveau_jewellery -. rejects .-> victorian_sentimental_jewellery
  art_nouveau_object -. rejects .-> victorian_manufacture
  arts_and_crafts_architecture -. rejects .-> neoclassical_architecture
  arts_and_crafts_art_pottery -. rejects .-> blue_willow_transferware
  arts_and_crafts_interior -. rejects .-> victorian_interior
  arts_and_crafts_jewellery -. rejects .-> georgian_jewellery
  arts_and_crafts_jewellery -. rejects .-> victorian_sentimental_jewellery
  arts_and_crafts_object -. rejects .-> victorian_manufacture
  bandeau_brassiere -. rejects .-> straight_front_corset
  bauhaus_modern_tableware -. rejects .-> meissen_baroque_porcelain
  bauhaus_modern_tableware -. rejects .-> regency_gilded_bone_china
  biodesign_car -. rejects .-> wedge_design_car
  bistronomie -. rejects .-> cuisine_classique
  blob_world -. rejects .-> flat_design
  british_modernist_studio -. rejects .-> anglo_oriental_studio_pottery
  brutalist_jewellery -. rejects .-> retro_cocktail_jewellery
  brutalist_web -. rejects .-> flat_design
  brutalist_web -. rejects .-> material_design
  canvas_court_sneaker -. rejects .-> english_welted_dress_shoe
  chef_studio_tableware -. rejects .-> regency_gilded_bone_china
  clay_3d_icon -. rejects .-> flat_icon
  claymorphism -. rejects .-> flat_design
  clean_girl -. rejects .-> goblincore
  clickbait_thumbnail -. rejects .-> minimalism_web
  conceptual_sketch_ui -. rejects .-> flat_design
  constructivism_web -. rejects .-> art_nouveau_web
  costume_jewellery -. rejects .-> garland_style_jewellery
  cottagecore -. rejects .-> flat_design
  crayon_lithograph_print -. rejects .-> engraving_print
  creamware_neoclassical -. rejects .-> delftware
  critical_regionalism_architecture -. rejects .-> international_style_architecture
  critical_regionalism_architecture -. rejects .-> postmodern_architecture
  cubism_painting -. rejects .-> impressionism
  cubism_painting -. rejects .-> renaissance_painting
  cuisine_francoise -. rejects .-> medieval_court_cuisine
  cuisine_minceur -. rejects .-> cuisine_classique
  cybercore_web -. rejects .-> flat_design
  cyberpunk_web -. rejects .-> flat_design
  cyberpunk_web -. rejects .-> minimalism_web
  dark_academia -. rejects .-> flat_design
  de_stijl_web -. rejects .-> art_nouveau_web
  deconstructivist_architecture -. rejects .-> international_style_architecture
  deconstructivist_architecture -. rejects .-> postmodern_architecture
  deep_fried_meme -. rejects .-> impact_image_macro
  designer_wall_hung_sanitary -. rejects .-> victorian_sanitary_ware
  didone_serif -. rejects .-> garalde_old_style
  diffusion_gloss -. rejects .-> mini_diffusion_meme
  documentary_photography -. rejects .-> pictorialism
  dogme_95 -. rejects .-> french_new_wave
  dopamine_decor -. rejects .-> japandi_interior
  dopamine_decor -. rejects .-> scandinavian_interior
  dual_camera_snapshot -. rejects .-> cohesive_feed_grid
  early_wristwatch -. rejects .-> american_pocket_watch
  editorial_serif_revival -. rejects .-> corporate_memphis
  editorial_serif_revival -. rejects .-> flat_design
  electric_minimal_car -. rejects .-> retro_revival_car
  electronic_and_digital_watch -. rejects .-> breguet_classical_watch
  empire_line_dress -. rejects .-> rococo_court_dress
  english_bespoke_tailoring -. rejects .-> rococo_court_dress
  english_slipware -. rejects .-> delftware
  ethereal_web -. rejects .-> brutalist_web
  expressionist_architecture -. rejects .-> beaux_arts_architecture
  fashion_editorial -. rejects .-> new_objectivity
  fiesta_colourware -. rejects .-> blue_willow_transferware
  fifth_gen_low_poly -. rejects .-> sixteen_bit_sprite
  film_grain_revival -. rejects .-> y2k_digicam
  film_noir -. rejects .-> classical_hollywood
  flash_intro_site -. rejects .-> portal_table_layout
  flat_design -. rejects .-> skeuomorphism
  flat_icon -. rejects .-> skeuomorphic_icon
  flat_logo -. rejects .-> glossy_3d_logo
  funk_ceramics -. rejects .-> anglo_oriental_studio_pottery
  garalde_old_style -. rejects .-> blackletter
  garconne_flapper_dress -. rejects .-> crinoline_and_bustle_dress
  garland_style_jewellery -. rejects .-> art_nouveau_jewellery
  geometric_sans -. rejects .-> garalde_old_style
  geometric_sans -.