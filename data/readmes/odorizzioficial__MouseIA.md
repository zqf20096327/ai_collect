<p align="center"><img src="src/MouseIA/Assets/banner.png" alt="MouseIA — selecione qualquer coisa na tela e pergunte à IA"></p>

<h1 align="center">MouseIA <sup>BETA</sup></h1>
<p align="center"><b>Selecione qualquer coisa na tela e pergunte à IA.</b><br>
Traduza para qualquer idioma (até por voz), copie textos de imagens, vídeos e arquivos e leia QR Codes.</p>

---

## Como usar

1. **Balance o mouse** de um lado para o outro, ou aperte **Alt+Shift+M**. Uma onda de luz sai do cursor, que ganha um brilho azul. Funciona em todos os monitores (ou só no que você escolher).
2. **Passe o mouse** sobre um parágrafo, botão, imagem ou janela: ele se ilumina.
   - **Botão esquerdo** (clicar ou arrastar): abre o cartão para perguntar.
   - **Botão direito arrastando**: traduz a área ali mesmo, por cima da tela, sem abrir o cartão.
     Como no Circule para Pesquisar: cada texto (título, parágrafo, botão) é reescrito no próprio lugar, sobre a cor de fundo original.
     Uma barrinha embaixo copia, lê em voz alta, mostra o original ou fecha.
   - As ações de cada botão (e da rolagem) podem ser trocadas em Configurações > Ativação.
3. No cartão que aparece, **pergunte o que quiser** ou use os botões:

| Botão | O que faz |
|---|---|
| 🌐 **Traduzir → idioma** | Traduz o texto da seleção para mais de 110 idiomas |
| 📋 **Copiar texto** | Reconhece o texto da imagem (offline, OCR do Windows) e copia |
| ▦ **QR Code** | Lê QR Codes e códigos de barras e põe o botão **Abrir link** em cima do próprio código |
| 🔍 **Google Lens** | Pesquisa a imagem no Google Lens do navegador (lá também tem o Modo IA) |
| 🔊 **Ouvir tradução** | Traduz a seleção e lê em voz alta no idioma escolhido |
| 📁 **Arquivo** | Imagens, PDF, vídeos, Word, PowerPoint, Excel e textos (ou arraste para o cartão) |

Mais coisas:
- **Digite direto:** com o MouseIA aberto, comece a digitar para perguntar sem selecionar nada.
- **Várias seleções:** o botão **+** junta outra área da tela na mesma pergunta.
- **Ditado:** o 🎤 no campo de texto transforma sua fala em pergunta.
- **Tradução ao vivo (beta):** em testes, ainda não disponível.
- **10 idiomas no app:** inglês, chinês, hindi, espanhol, árabe, bengali, francês, português, russo e urdu.
- **Apps de administrador:** o MouseIA abre como administrador por padrão (o Windows pede permissão uma vez), para o balanço funcionar sobre qualquer app. Se recusar, ele abre normal e dá para ligar depois em Ativação.
- **Instalados:** mostra chaves de API, IAs locais, cache, motor e vozes naturais, com tamanho e pasta, e deixa remover cada um.
- **Privacidade:** sem servidor próprio, sem conta e sem coleta de dados. Detalhes em Configurações > Sobre.
- **Botão do meio:** clique com a rodinha (Scroll) em algo destacado, ou segure e arraste, para rodar a ação escolhida em Ativação > Ações do mouse.
- **Atalho das configurações:** opcional, em Configurações > Ativação.
- **Visual:** efeito vidro com opacidade ajustável (Configurações > Geral). As animações rodam na taxa do seu monitor (120, 144, 240 Hz…).
- **Vozes naturais do MouseIA:** voz feminina e masculina com som humano, offline (português, inglês, espanhol, francês, italiano e hindi).
  O MouseIA baixa sozinho uma vez (cerca de 370 MB, qualidade máxima); nada para configurar.
- Respostas com **Copiar**, **Ouvir** e **Tentar de novo**.
- **Esc** ou **clique com o botão direito** fecha.
- O cartão pode ser **arrastado** pelo topo para qualquer lugar da tela, e ele lembra a posição em cada monitor.

## Qual IA responde

Em **Configurações > Inteligência artificial**:

- **Gemini**: chave grátis em [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
- **ChatGPT**: chave da [OpenAI](https://platform.openai.com/api-keys)
- **Claude**: chave da [Anthropic](https://platform.claude.com/settings/keys)
- **Grok**: chave da [xAI](https://console.x.ai)
- **IA local**: roda no seu PC e nada sai da sua rede. Dois jeitos:
  - **Arquivo de modelo**: escolha um `.gguf` ou `.litertlm` baixado do Hugging Face e pronto.
    O MouseIA baixa e instala o motor sozinho no primeiro uso, numa pasta só dele: **llama.cpp** para `.gguf`,
    **LiteRT-LM** (com Python próprio) para `.litertlm`. Usa a placa de vídeo ou o processador.
    Para perguntar sobre imagens, baixe também o arquivo **mmproj** do mesmo modelo na mesma pasta.
    O cache do LiteRT-LM fica em **Documentos\MouseIA Cache\<nome do PC>**, e não ao lado do modelo.
  - Antes de tudo, o MouseIA instala o **motor** (llama.cpp e LiteRT-LM) numa pasta própria, com um clique.
  - **Baixar IAs**: as 10 melhores IAs locais (Gemma 4 e Qwen3.5) separadas por categoria (Recomendado, PC fraco, PC médio, PC super forte),
    com os requisitos no (i) e o link da página oficial de cada uma. Um clique baixa e já deixa em uso.
    Em **Suas IAs** dá para trocar de modelo, apagar (com o cache junto, se quiser) e limpar o cache.
  - **Servidor**: Ollama, LM Studio, llama.cpp, LiteRT-LM, Jan… O botão **Detectar** encontra e lista os modelos.

As chaves ficam guardadas **criptografadas** (DPAPI) no seu usuário do Windows.
Copiar texto e ler QR Code funcionam **sem IA e sem internet**.

## Instalar

Baixe o `MouseIA-Setup.exe` na página de **Releases** e instale. Não precisa ser administrador.
Também há a versão **portátil** (`MouseIA-Portable.exe`), que roda sem instalar.

**Atualizações automáticas:** o MouseIA confere o GitHub e se atualiza sozinho (Configurações > Atualizações).
Para publicar uma versão nova, crie uma *release* com a tag `vX.Y.Z` (ex.: `v1.4.1`): o GitHub Actions compila e anexa os instaladores, e os usuários recebem.

Requer Windows 10 (versão 2004) ou mais novo, 64 bits.

## Compilar

**No GitHub (mais fácil):** envie este projeto para um repositório. A aba **Actions** compila e gera
o instalador sozinha a cada envio. Para publicar uma versão, crie uma tag (ex.: `v1.0.0`), e o instalador
aparece em **Releases**.

**No seu PC:**
1. Instale o .NET 8 SDK: `winget install Microsoft.DotNet.SDK.8`
2. (Opcional, para o instalador) `winget install JRSoftware.InnoSetup`
3. Dê dois cliques em **`build.bat`**.

## Estrutura

```
src/MouseIA/
  Core/       IA (Gemini, OpenAI, Claude, local), idiomas, textos, configurações, detector de balanço
  Native/     atalho global, gancho do mouse, captura de tela, ícone da bandeja, DPAPI
  Services/   OCR, voz (falar e ouvir), QR Code, importação de arquivos
  UI/         visual liquid glass: sobreposição, cartão, tradutor de voz, configurações
tests/CoreTests/   testes do núcleo (rodam com tools/mock_ai.py)
installer/         instalador Inno Setup
```

## Créditos

Feito por **Odorizzi**: [YouTube](https://www.youtube.com/@odorizzioficial) ·
[GitHub](https://github.com/odorizzioficial) · [Instagram](https://www.instagram.com/odorizzidicas) ·
[TikTok](https://www.tiktok.com/@odorizzioficial)

Inspirado no [Magic Pointer](https://github.com/rono-zeroseven/magic-pointer), mod para Windhawk de Rono
(licença MIT). Leitura de códigos com [ZXing.Net](https://github.com/micjahn/ZXing.Net) (Apache 2.0).
Veja `THIRD-PARTY-NOTICES.md`.

Licença: MIT.
