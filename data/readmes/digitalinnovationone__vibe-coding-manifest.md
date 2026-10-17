# Manifesto Vibe Coding

> A IA acelera o código. O método protege o produto.

12 princípios para desenvolver com IA sem terceirizar o pensamento — transformando
velocidade em direção, prompts em decisões e geração em engenharia.

**Leia online:** https://digitalinnovationone.github.io/vibe-coding-manifest/

Autoria: [Felipe Aguiar](https://github.com/felipeAguiarCode) (@felipeAguiarCode)

---

## Os 12 princípios

| # | Princípio |
|---|---|
| 01 | **Saiba o que está construindo.** Antes de pedir código, crie um argumento. |
| 02 | **Pesquise antes de inventar.** A pesquisa reduz alucinação de produto. |
| 03 | **Visualize antes de implementar.** Conceito antes de código. |
| 04 | **PRD diz o quê. ADR diz como. Gates dizem quando.** |
| 05 | **Antes do build, ataque o plano.** Prompt Red Team no PRD e no ADR. |
| 06 | **Dê contexto ao agente. Não dê liberdade infinita.** Contexto é parte da arquitetura. |
| 07 | **Padronize antes que a geração vire entropia.** Coding Guidelines vivas. |
| 08 | **IA gera. Humano valida. Gate libera.** Human in the Loop. |
| 09 | **Valide o comportamento, não apenas o build.** "Compila" ≠ "funciona". |
| 10 | **Corrija a casa antes de construir outro andar.** Dívida removida continuamente. |
| 11 | **Escala começa na legibilidade da codebase.** Speed + Codebase + Specs. |
| 12 | **O código muda. A especificação precisa mudar junto.** Specs vivas. |

## O ciclo

```
PRD → ADR → Gates → Red Team → Código → Human in the Loop → Validação → Specs → PRD
```

## Sobre esta página

Página estática, sem build e sem dependências externas: todo o HTML, CSS e JS
vivem em `index.html`. Os checkboxes de cada princípio são persistidos no
`localStorage` do navegador, e a página tem folha de estilo de impressão para
exportar o manifesto em PDF.

### Rodando localmente

```bash
git clone https://github.com/digitalinnovationone/vibe-coding-manifest.git
cd vibe-coding-manifest
# abra index.html no navegador, ou:
python -m http.server 8000
```

## Estrutura

```
index.html   # o manifesto completo (HTML + CSS + JS inline)
.nojekyll    # publica os arquivos sem processamento do Jekyll
```

---

**Vibe coding não é ausência de processo.** É um processo novo: mais rápido, mais
iterativo e mais dependente de contexto explícito.

`Build fast. Validate hard.`
