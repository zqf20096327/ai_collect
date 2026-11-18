# AFE <sup>beta</sup>

**Português (BR)** · [English](README.en.md)

> **Um recado antes de tudo:** eu não sou programador. Sou designer e criei o AFE com a ajuda de IA para resolver
> um problema meu — editar as artes HTML que a IA gera sem precisar mexer no código. Estou abrindo o projeto para
> que a comunidade use, teste, corrija e faça ele crescer. Contribuições de todo tipo são bem-vindas
> (veja [CONTRIBUINDO.md](CONTRIBUINDO.md)).
>
> **Beta:** funciona e tem teste automático, mas ainda pode ter arestas. Se algo quebrar, abra uma *issue*.

### ⬇ [Baixe o AFE grátis](https://github.com/adrianofernandesvideo/afe/releases) — Windows, macOS e Linux

Ou teste agora no navegador, sem instalar nada: **[abrir o live preview](https://adrianofernandesvideo.github.io/afe/)**

Editor visual para artes feitas em HTML — posts, carrosséis, stories, banners. Você abre a arte no
navegador e ajusta **manualmente**, sem mexer no código: mover, mudar tamanho e texto, glows e sombras,
cantos e contornos, acrescentar imagens e formas, animar com keyframes e gerar o vídeo.

![O AFE editando a própria propaganda: a arte no meio, a animação à esquerda, as camadas à direita e a folha de keyframes embaixo](docs/imagens/afe-editor.png)

<p align="center"><img src="docs/imagens/afe-post.gif" width="360" alt="A arte de demonstração animada, exportada pelo próprio AFE"><br><sub>A arte acima, animada no AFE e exportada em vídeo (com motion blur).</sub></p>

## O que ele faz

- **Edita qualquer arte `.html` de tamanho fixo** — inclusive artes montadas por script.
- **Não reescreve a arte:** as mudanças ficam num arquivo de dados ao lado dela (`<arte>.edicoes.js`). Apagar
  esse arquivo devolve a arte ao original.
- **Efeitos:** glow e sombras em camadas, cor, ajustes de imagem, cantos, preenchimento e contorno em
  gradiente, **modos de mesclagem** (Multiplicação, Tela, Sobrepor…) e **granulado** de filme animado.
- **Imagens do computador:** arraste e solte em cima da arte (vira camada) ou na aba Assets.
- **Assets:** formas, texto, imagens, bibliotecas de assets de fora (os da sua marca, por exemplo) e
  **peças em código** de um design system.
- **Animação:** keyframes com curvas (easing), folha de keyframes, tempo de cada camada, entradas prontas,
  efeitos contínuos em loop, frame da capa.
- **Vídeo:** gera o MP4 da página, com motion blur opcional.
- **Atalhos configuráveis**, desfazer/refazer, cópia da versão anterior a cada salvar.

## Requisitos

- **Pelo executável (Releases):** só um navegador (Edge ou Chrome). Não precisa de Python.
- **Pelo código:** Python 3 (o servidor usa só a biblioteca padrão) e um navegador Edge ou Chrome.
- **Para gerar vídeo e rodar o teste automático:** também o [Playwright para Python](https://playwright.dev/python/)
  e o [ffmpeg](https://ffmpeg.org) no PATH.

O editor não instala nada sozinho: se faltar algo, ele avisa o quê.

> Desenvolvido e usado no **Windows** com Python 3.14. macOS, Linux e versões mais antigas do Python ainda não
> foram testados — relatos e correções são bem-vindos.

## Baixar e usar

- **Baixe:** na página de [Releases](https://github.com/adrianofernandesvideo/afe/releases), pegue o `.zip` do seu sistema (Windows, macOS ou Linux),
  descompacte e dê dois cliques em **AFE**. Não precisa de Python. Para usar com uma arte sua, arraste o `.html`
  dela em cima do AFE.
- **Usa uma IA (Claude, ChatGPT, Cursor…)?** Peça para ela ler o `AGENTS.md` que vem no `.zip`: ele explica como
  o AFE funciona, como criar artes que dão certo no editor e o que não mexer para não perder as suas edições.
- **Quer ver antes de instalar?** O **[live preview](https://adrianofernandesvideo.github.io/afe/)** é o editor de verdade, no navegador, com as artes
  de demonstração. As edições ficam só no seu navegador (dá para baixá-las). Gerar vídeo e as bibliotecas de
  assets só funcionam no AFE baixado.

Cada push na `main` gera sozinho um release novo (`2.3.0-beta`, `2.3.1-beta`…) e atualiza a demo online — veja
[distribuir/LEIA.md](distribuir/LEIA.md).

## Começar em 2 minutos (com Python)

Dentro da pasta do AFE:

```bash
python servidor.py --raiz demos/artes
```

Abra `http://localhost:8765/editor/?arquivo=afe-post.html`, clique em **✎ Editar** e mexa à
vontade: é a arte de demonstração da imagem acima (ligue o **🎬 Animar** para ver a animação). Nada
do que você fizer muda o código dela — só o arquivo de edições ao lado.

Na mesma pasta há um **carrossel de 7 páginas** sobre o AFE — cada página mostra a função que descreve. Veja
[demos/LEIA.md](demos/LEIA.md).

![As 7 páginas do carrossel de demonstração](docs/imagens/afe-carrossel.png)

## Usar com as suas artes

Os comandos rodam de dentro da pasta do AFE; as artes podem ficar em qualquer lugar.

```bash
python ligar.py ../minhas-artes/arte.html        # uma vez por arte
python servidor.py --raiz ../minhas-artes        # abre o editor
```

Com uma biblioteca de assets (aparece na aba Assets de todas as artes):

```bash
python servidor.py --raiz ../minhas-artes --biblioteca Marca=../minha-marca/assets
```

O passo a passo completo, com o que a arte precisa ter, está no [LEIA.md](LEIA.md).

## Documentação

| Quero… | Leia |
|---|---|
| instalar, ligar uma arte, abrir o editor | [LEIA.md](LEIA.md) |
| usar o editor | [docs/MANUAL.md](docs/MANUAL.md) |
| saber o que existe e as ideias para depois | [docs/ROTEIRO.md](docs/ROTEIRO.md) |
| mexer no código | [docs/ARQUITETURA.md](docs/ARQUITETURA.md) e [CONTRIBUINDO.md](CONTRIBUINDO.md) |
| entender por que algo é feito de um jeito estranho | [docs/DESCOBERTAS.md](docs/DESCOBERTAS.md) |
| ver o que mudou em cada versão | [docs/CHANGELOG.md](docs/CHANGELOG.md) |

## Segurança

O servidor só atende este computador (`127.0.0.1`) e confere de onde vem cada pedido. Ele só grava o arquivo
de edições de cada arte e cópias de imagens/CSS das bibliotecas dentro da pasta da arte. O único programa que
ele roda é o `render_anim.py` desta pasta.

## Contribuir

Ideias, correções e relatos de uso são bem-vindos. Veja [CONTRIBUINDO.md](CONTRIBUINDO.md).

## Licença

Copyright (C) 2026 Adriano Fernandes

Este programa é software livre, sob a **[GNU Affero General Public License v3](LICENSE)** (AGPL-3.0).
Em resumo: você pode usar, estudar, modificar e até vender — mas quem distribuir uma versão modificada, ou
oferecer o editor para outras pessoas usarem pela internet, precisa liberar o código dessa versão sob a
mesma licença. O texto que vale é o do arquivo [LICENSE](LICENSE).

## Idiomas

Toda a documentação existe em português e em inglês (a versão em inglês fica em [docs/en/](docs/en/)). A tela
do editor ainda está só em português; deixar o editor multi-idioma está nas ideias do
[ROTEIRO](docs/ROTEIRO.md).
