<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo-dark.svg">
    <img src="assets/logo-light.svg" alt="omni-token-optimizer" width="220">
  </picture>
</p>

# Omni-Token Optimizer Suite

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-1a7f37?style=flat-square"></a>
  <img alt="Release" src="https://img.shields.io/github/v/release/Wennington123/omni-token-optimizer?style=flat-square&color=1a7f37&v=2">
  <img alt="Python" src="https://img.shields.io/badge/python-3.8%2B-1a7f37?style=flat-square&logo=python&logoColor=white">
  <a href="https://ko-fi.com/wenningtondaquino"><img alt="Ko-fi" src="https://img.shields.io/badge/Ko--fi-Apoie-FF5E5B?style=flat-square&logo=kofi&logoColor=white"></a>
  <a href="#guia-de-instalação-e-integração"><img alt="Install" src="https://img.shields.io/badge/install-curl_%7C_bash-3fb950?style=flat-square&logo=gnu-bash&logoColor=white"></a>
</p>

Suíte universal e de alto desempenho para **otimização rigorosa de tokens de LLM**, desenvolvida para atender tanto a **desenvolvimento de software** quanto a **tarefas de uso geral** (pesquisa, redação, análise de dados e automação de fluxos).

O repositório unifica a filosofia de 3 projetos de referência (**Caveman**, **Punisher Mode** e **Ponytail**) com as evidências empíricas e algoritmos de **6 artigos científicos de ponta** em compressão de contexto e raciocínio de agentes.

## Quick Start

```bash
curl -fsSL https://raw.githubusercontent.com/Wennington123/omni-token-optimizer/main/install.sh | bash
```

Reinicie a sessão do agente — a skill carrega sozinha. Prefere delegar? Cole o [bloco de prompt pronto](#2-colar-no-seu-agente-de-ia-claude-code-cursor-command-code-etc) no seu agente.

![Demonstração no OpenCode](assets/demo-opencode.gif)

*Tela real do OpenCode: instalação em uma linha, `seq 1 3000` passando pelo filtro local e o contexto final.*

---

## Sumário
1. [Visão Geral & Filosofia](#visão-geral--filosofia)
2. [Arquitetura Geral (Hooks + Skills)](#arquitetura-geral-hooks--skills)
3. [Fundamentação Teórica & Referências Bibliográficas](#fundamentação-teórica--referências-bibliográficas)
4. [Painel Visual & Gráficos de Desempenho](#painel-visual--gráficos-de-desempenho)
5. [Modelagem Matemática & ROI de Ativação](#modelagem-matemática--roi-de-ativação)
6. [Matriz Numérica de Economia por Camada](#3-exemplo-numérico-em-sessão-típica-15-turnos)
7. [Estrutura Detalhada dos Arquivos](#estrutura-detalhada-dos-arquivos)
8. [Guia de Instalação e Integração](#guia-de-instalação-e-integração)
9. [Licença & Contribuição](#licença--contribuição)

---

## Visão Geral & Filosofia

À medida que os agentes de IA realizam tarefas de longo horizonte, o **crescimento descontrolado do contexto** eleva os custos de inferência, aumenta a latência e degrada a capacidade de atenção do modelo.

O **Omni-Token Optimizer** atua em duas frentes complementares:
1. **Zero-Token Local Middleware (Hooks)**: Filtra e trunca saídas brutas de ferramentas (terminal, CSVs, respostas JSON) na máquina local antes que os dados cheguem à API do modelo. Custo de execução = **0 tokens**.
2. **Behavioral System Prompts (Skills)**: Molda o comportamento cognitivo do modelo para gerar respostas ultraconcisas, aplicar *diffs* cirúrgicos em código, adotar enquadramentos de papel (*Responsibility Tuning*) e manter uma memória de estado estruturada (`VARS`, `TODO`, `GUARDRAILS`).

---

## Arquitetura Geral (Hooks + Skills)

![Como funciona](assets/arch-flow.gif)

<details>
<summary><b>Diagrama em texto (para leitores de tela e cópia)</b></summary>

```text
[Solicitação do Usuário / Comando de Ferramenta]
                      │
                      ▼
 ┌──────────────────────────────────────────────────────────────┐
 │ CAMADA 1: HOOKS LOCAIS (Python / CPU Local - CUSTO: 0 TOKENS) │
 │  • observation_trimmer.py: Trunca logs/CSVs (CoACT / Caveman)│
 │  • context_monitor.py: Monitora limite de tokens da sessão   │
 └────────────────────────────┬─────────────────────────────────┘
                              │ (Envia observação filtrada)
                              ▼
 ┌──────────────────────────────────────────────────────────────┐
 │ CAMADA 2: MASTER SKILL & SUBSKILLS (Prompt / LLM Reasoning)  │
 │  • SKILL.md (Orquestrador Universal)                         │
 │  • subskills/01-terse-communication.md (Caveman + Punisher)  │
 │  • subskills/02-lazy-execution.md (Ponytail + Refactoring)   │
 │  • subskills/03-observation-trimmer.md (TRC + CoACT Rules)   │
 │  • subskills/04-state-compactor.md (ACON + TRACE Checkpoint) │
 │  • subskills/05-prompt-budgeting.md (LLMLingua Allocation)   │
 └──────────────────────────────────────────────────────────────┘
```

</details>

| Subskill | Foco | Base |
|---|---|---|
| [01 — Terse Communication](subskills/01-terse-communication.md) | Respostas secas, zero cerimônia | Caveman + Punisher |
| [02 — Lazy Execution](subskills/02-lazy-execution.md) | Menor diff que resolve, YAGNI | Ponytail |
| [03 — Observation Trimmer](subskills/03-observation-trimmer.md) | Corte de logs e outputs de API | CoACT + TRC |
| [04 — State Compactor](subskills/04-state-compactor.md) | Memória de estado estruturada | ACON + TRACE |
| [05 — Prompt Budgeting](subskills/05-prompt-budgeting.md) | Orçamento do contexto inicial | LLMLingua |

---

## Fundamentação Teórica & Referências Bibliográficas

O repositório é construído rigorosamente sobre 9 fontes de conhecimento:

<details>
<summary><b>3 repositórios + 6 artigos científicos — clique para expandir</b></summary>

### Repositórios Open-Source

1. **JuliusBrussee/caveman** — *“Why use many token when few token do trick.”*
   - **Repositório**: GitHub JuliusBrussee/caveman
   - **Contribuição**: Estilo de comunicação ultraconciso (*Caveman Voice*) e proxies locais de compressão de ferramentas. Reduz retornos de CSVs e logs em até **98.9%**.
2. **Wennington123/punisher-mode** — *High-autonomy, low-friction operational mode for Command Code.*
   - **Repositório**: GitHub Wennington123/punisher-mode
   - **Contribuição**: Modo operacional autônomo. Elimina preâmbulos de cortesia ("Certamente, vou ajudar...") e *loops* de confirmação desnecessários, reduzindo a latência e o consumo em conversas *multi-turn*.
3. **DietrichGebert/ponytail** — *Makes your AI agent think like the laziest senior dev in the room.*
   - **Repositório**: GitHub DietrichGebert/ponytail
   - **Contribuição**: Filosofia YAGNI (*You Aren't Gonna Need It*). Força alterações via patches/diffs curtos em vez de reemitir arquivos inteiros, reduzindo em **45% os tokens consumidos** e em **53% o código escrito**.

### Artigos Científicos Empíricos

4. **Code Smells & Chain of Thought Token Consumption** (2025)
   - **Citação**: *Investigating Token Efficiency in Automated Software Engineering via Chain of Thought Reasoning.* (arXiv:2504.15989)
   - **Contribuição**: Prova empírica de que códigos poluídos (*code smells*) inflam as etapas de raciocínio CoT do modelo. A refatoração prévia e o enquadramento de papel (*Responsibility Tuning*) reduzem os tokens por unidade de complexidade de `0.1015` para `0.0576` (**corte de 49.7% no CoT**).
5. **CoACT: Observation Compression via Next-Action Preservation** (2026)
   - **Citação**: *CoACT: Frame-guided Observation Compression for Long-Horizon Agent Workflows.* (arXiv:2607.02911)
   - **Contribuição**: Algoritmo de compressão de observações por preservação da próxima ação. Reduz os tokens de saída de ferramentas em **55.9%** sem reduzir a taxa de sucesso (*PASS@1*).
6. **Tool-Result Clearing (TRC) & Context Compression Policy** (2026)
   - **Citação**: *Context Compression Tradeoffs in Long-Horizon AI Agent Workflows.* (arXiv:2609.32961)
   - **Contribuição**: Prova que substituir resultados antigos de ferramentas por placeholders (`[output cleared]`) preserva o *reuso de KV-cache* e reduz o custo acumulado para **0.57x do baseline**.
7. **TRACE: Boundary-Local Execution Verifier** (2026)
   - **Citação**: *TRACE: Recurrent Context Compression with Boundary Execution Verification.* (arXiv:2608.06503)
   - **Contribuição**: Previne a perda do estado de execução local em resumos longos. Elimina *loops* de reexploração repetitiva e reduz os tokens de pico em **31% a 54%**.
8. **ACON: Agent Context Optimization** (2025)
   - **Citação**: *Agent Context Optimization via Contrastive Task Feedback & Compressor Distillation.* (arXiv:2510.00615)
   - **Contribuição**: Estruturação do contexto em tabelas de estado (`VARS`, `TODO`, `GUARDRAILS`) e destilação de modelos compressores leves (custo 99% menor).
9. **LLMLingua: Compressing Prompts for Accelerated Inference** (EMNLP 2023)
   - **Citação**: *LLMLingua: Compressing Prompts for Accelerated Inference via Small Language Models.* (arXiv:2023.emnlp-main.825)
   - **Contribuição**: Alocação orçamentária por entropia. Preserva 100% da instrução central e reduz demonstrações *few-shot* redundantes em até **5x**.

</details>

---

## Painel Visual & Gráficos de Desempenho

### Gráfico 1: Economia Percentual de Tokens por Camada de Otimização
![Redução Percentual de Tokens](assets/chart_token_savings.png)

### Gráfico 2: Evolução do Contexto Acumulado ao Longo de 15 Turnos
![Crescimento do Contexto](assets/chart_context_growth.png)

---

## Modelagem Matemática & ROI de Ativação

### 1. Custo de Ativação Ajustado por Prompt Caching
Quando a Master Skill e suas Sub-Skills são carregadas no prompt do sistema ($N_{skill} \approx 1.200 \text{ tokens}$), o custo acumulado em uma sessão de $T$ turnos com desconto de *Prompt Caching* ($d_{cache} \approx 0.90$) é:

$$C_{ativação} = N_{skill} + (T - 1) \times N_{skill} \times (1 - d_{cache})$$

Para uma sessão de 15 turnos:
$$C_{ativação} = 1.200 + (14 \times 1.200 \times 0.10) = 2.880 \text{ tokens de entrada.}$$

### 2. Equação da Economia Líquida
$$\Delta \text{Tokens}_{líquida} = \Delta \text{Output} + \Delta \text{Obs} + \Delta \text{CoT} + \Delta \text{State} - C_{ativação}$$

### 3. Exemplo Numérico em Sessão Típica (15 Turnos)

| Métrica / Camada | Sem Otimização | Com Omni-Token Optimizer | Economia Líquida |
| :--- | :---: | :---: | :---: |
| **Tokens de Resposta (Output)** | 6.000 (400/turno) | 1.200 (80/turno) | **-4.800 tokens** (~4x mais valiosos) |
| **Ferramentas / Observações** | 60.000 (5 chamadas) | 7.500 (CoACT/TRC/Hook) | **-52.500 tokens** |
| **Acúmulo de Histórico (Pico)** | 22.600 tokens | 7.200 tokens (ACON/TRACE) | **-15.400 tokens** |
| **Custo de Ativação da Skill** | 0 tokens | 2.880 tokens | +2.880 tokens |
| **TOTAL DA SESSÃO** | **140.000 tokens** | **58.000 tokens** | **-82.000 tokens (-58.5%)** |

**Fator de Retorno (ROI)**: Para cada 1 token gasto mantendo a suíte ativa, a sessão economiza **28.4 tokens de API**.

---

## Estrutura Detalhada dos Arquivos

```text
omni-token-optimizer/
├── SKILL.md                          # Master Skill (Orquestrador Universal)
├── AGENTS.md                         # Diretrizes enxutas para arquivos de sistema
├── README.md                         # Documentação completa e teórico-empírica
├── install.sh                        # Instalador de uma linha (curl | bash)
├── assets/
│   ├── logo-light.svg                # Logo (tema claro)
│   ├── logo-dark.svg                 # Logo (tema escuro)
│   ├── arch-flow.gif                 # Diagrama animado da arquitetura
│   ├── demo-opencode.gif             # Demo real: instalação + trim no OpenCode
│   ├── chart_token_savings.png       # Gráfico de economia por camada
│   └── chart_context_growth.png      # Gráfico de curva de crescimento de contexto
├── subskills/
│   ├── 01-terse-communication.md     # Estilo enxuto e autonomia (Caveman + Punisher)
│   ├── 02-lazy-execution.md          # Desenvolvimento enxuto e papéis (Ponytail + Refactoring)
│   ├── 03-observation-trimmer.md     # Regras de corte de observação (CoACT + TRC)
│   ├── 04-state-compactor.md         # Memória de estado estruturada (ACON + TRACE)
│   └── 05-prompt-budgeting.md        # Alocação de orçamento de prompt (LLMLingua)
├── hooks/
│   ├── observation_trimmer.py        # Hook Python local (Zero-Tokens) para truncar logs/APIs
│   └── context_monitor.py            # Hook Python local (Zero-Tokens) para monitorar limite da sessão
└── plugins/
    └── opencode/
        ├── index.ts                  # Plugin OpenCode v2: liga os hooks via API de plugins
        └── trim.ts                   # Lógica pura de trim/estimativa de tokens (testável)
```

---

## Guia de Instalação e Integração

### 1. Instalação em uma linha (Linux/macOS)

```bash
curl -fsSL https://raw.githubusercontent.com/Wennington123/omni-token-optimizer/main/install.sh | bash
```

O script auto-detecta a pasta de skills do seu agente (`~/.commandcode/skills`, `~/.claude/skills` ou `~/.config/opencode/skills`), instala a skill + subskills + hooks, copia os hooks para `~/.commandcode/hooks/` se existir e imprime o snippet de ativação. Se `~/.config/opencode/` existir, instala também a skill em `~/.config/opencode/skills/` e o plugin de hooks em `~/.config/opencode/plugins/` — mesmo que a raiz detectada seja outra. Opções: `--dir DIR` (raiz de skills alternativa) e `--uninstall`.

Reinicie a sessão do agente e a skill carrega automaticamente.

### 2. Colar no seu agente de IA (Claude Code, Cursor, Command Code, etc.)

Copie o bloco abaixo, cole no seu agente e peça para executar:

```text
Instale e ative a skill omni-token-optimizer do repo
https://github.com/Wennington123/omni-token-optimizer

Passos:
1. Clone o repo (shallow) em um diretório temporário.
2. Copie SKILL.md, AGENTS.md, subskills/ e hooks/ para a pasta de skills
   do seu agente, criando o subdiretório omni-token-optimizer/ (ex.:
   ~/.claude/skills/omni-token-optimizer/ — se ~/.commandcode/skills
   existir, use-a).
3. chmod +x em todos os hooks/*.py.
4. Se ~/.commandcode/hooks existir, copie hooks/*.py para lá também.
5. Liste os arquivos instalados para confirmar e diga como ativar a
   skill em uma nova sessão.
Não modifique nenhum outro arquivo do meu sistema.
```

### 3. Instalação manual

```bash
git clone --depth 1 https://github.com/Wennington123/omni-token-optimizer.git
cp -r omni-token-optimizer ~/.claude/skills/omni-token-optimizer   # ajuste ao seu agente
chmod +x ~/.claude/skills/omni-token-optimizer/hooks/*.py
```

### 4. Integração por agente

- **Claude Code / Command Code**: a skill é auto-descoberta na pasta de skills; para o `context_monitor.py` (que fala o protocolo JSON de hooks e injeta o aviso de compactação da subskill 04), use a config testada impressa pelo `install.sh` — limiar ajustável via `OMNI_TOKEN_THRESHOLD`. O `observation_trimmer.py` **não** tem wiring nesses agentes: hooks de PreToolUse não substituem o output que o modelo vê (só injetam contexto extra), então ligá-lo aumentaria tokens em vez de reduzir — ele existe para o caso abaixo.
- **OpenCode (v2)**: suporte completo via skill + plugin local — veja [Integração OpenCode](#5-integração-opencode-v2).
- **Cursor / VS Code Agent**: adicione o conteúdo do `AGENTS.md` ao seu `.cursorrules` ou `system_prompt.md`.
- **Agentes customizados em Python**: integre `hooks/observation_trimmer.py` no manipulador de retornos de ferramentas (onde o output pode ser substituído antes da API) e `hooks/context_monitor.py` no loop de sessão.

### 5. Integração OpenCode (v2)

Testado no OpenCode **2.4.1**. A integração usa dois mecanismos nativos: a skill auto-descoberta e um plugin de servidor (API v2 de plugins). Diferente do Claude Code/Command Code, no OpenCode o `observation_trimmer` ganha wiring de verdade: o hook `tool.execute.after` substitui o output que o modelo vê, então o corte de logs funciona de fato.

#### Instalação manual

```bash
git clone --depth 1 https://github.com/Wennington123/omni-token-optimizer.git
cd omni-token-optimizer

# 1. Skill global (auto-descoberta)
mkdir -p ~/.config/opencode/skills/omni-token-optimizer
cp SKILL.md AGENTS.md ~/.config/opencode/skills/omni-token-optimizer/
cp -r subskills hooks ~/.config/opencode/skills/omni-token-optimizer/

# 2. Plugin (hooks locais)
mkdir -p ~/.config/opencode/plugins
cp -r plugins/opencode ~/.config/opencode/plugins/omni-token-optimizer
```

No `~/.config/opencode/opencode.json` (o OpenCode recarrega skill e plugin ao salvar, sem restart):

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": [
    "~/.config/opencode/skills/omni-token-optimizer/SKILL.md"
  ],
  "plugins": [
    "/home/SEU_USUARIO/.config/opencode/plugins/omni-token-optimizer"
  ]
}
```

- `instructions` deixa a Master Skill **sempre ativa** (equivalente ao auto-load). Sem ela, a skill continua disponível sob demanda (mencione `@omni-token-optimizer` no prompt).
- Sem a chave `plugins`, a skill funciona, mas os hooks locais ficam desligados.
- O plugin também é carregado de `.opencode/plugins/` (por projeto) se preferir escopo local.

#### O que o plugin faz (custo 0 tokens de LLM)

| Hook | Subskill | Comportamento |
| --- | --- | --- |
| `tool.execute.after` | 03 — Observation Trimmer | Trunca saídas longas de `shell` acima de **160 linhas e 6.000 caracteres**: mantém as 40 primeiras linhas, linhas de erro do meio e as 30 últimas, com marcador `[... omni-token-optimizer: N lines / M chars trimmed ...]`. Nunca toca em resultados com anexos (imagens/PDFs). |
| `session.context` | 04 — State Compactor | Estima o histórico (~4 chars/token) e, acima do limiar, injeta o aviso `[TOKEN_WARNING]` no system prompt — **uma vez**, repetindo só se o contexto crescer ≥25% ou após 2 min. |

#### Opções

Via `options` na entrada do plugin em `opencode.json`, ou variáveis de ambiente (fallback):

```jsonc
"plugins": [
  {
    "package": "/home/SEU_USUARIO/.config/opencode/plugins/omni-token-optimizer",
    "options": { "contextThreshold": 120000, "debug": true }
  }
]
```

| Opção | Env | Padrão | Descrição |
| --- | --- | --- | --- |
| `contextThreshold` | `OMNI_TOKEN_THRESHOLD` | `120000` | Limiar de tokens para o aviso de compactação |
| `contextRewarnRatio` | — | `1.25` | Reavisa quando o contexto crescer essa fração desde o último aviso |
| `contextRewarnMs` | — | `120000` | Janela mínima (ms) entre avisos |
| `trimTools` | `OMNI_TRIM_TOOLS` | `"shell"` | Ferramentas cuja saída pode ser truncada (lista separada por vírgula) |
| `trimMaxChars` | `OMNI_TRIM_MAX_CHARS` | `6000` | Gatilho de caracteres para o trim |
| `trimMaxLines` | `OMNI_TRIM_MAX_LINES` | `160` | Gatilho de linhas para o trim |
| `debug` | `OMNI_DEBUG=1` | `false` | Loga estimativas e trims no stdout do servidor |

#### Verificação

Salve o `opencode.json` e, em uma sessão do agente, rode `seq 1 3000`: acima dos gatilhos, a saída vira head + marcador de trim + tail. Para conferir o monitor de contexto, baixe o limiar (`"contextThreshold": 100`) e veja o aviso `[TOKEN_WARNING]` entrar no system prompt da próxima chamada.

#### Logs esperados (não é bug)

O log do servidor mostra `msg="loading plugin"` **quatro vezes** no boot, sempre em dois pares: o plugin global é resolvido em duas localizações (global e projeto) e re-resolvido no `config.updated` que mescla o config do projeto. O `PluginSupervisor` deduplica por `id` e cacheia o módulo por `revision`, então o `setup` roda **uma vez** e cada hook dispara **uma vez** por evento — verificado com plugin-sonda: 1 `SETUP`, 1 `tool.execute.after` por chamada e 1 `[TOKEN_WARNING]` por request. Custo das linhas extras: poucos ms, zero token.

Ao salvar `index.ts` ou `trim.ts`, o watcher descarta a instância anterior antes de criar a nova, ou seja, hot reload sem restart e sem acúmulo de handlers.

### 6. Desinstalar

```bash
curl -fsSL https://raw.githubusercontent.com/Wennington123/omni-token-optimizer/main/install.sh | bash -s -- --uninstall
```

No OpenCode, remova também as entradas `instructions`/`plugins` do `~/.config/opencode/opencode.json` (o script remove a skill e o plugin, mas não edita esse arquivo).

---

## Licença & Contribuição

Este projeto é distribuído sob a licença **MIT**. Sinta-se à vontade para contribuir com novos hooks ou aprimoramentos empíricos via Pull Requests!

Gostou? Pague um café: [ko-fi.com/wenningtondaquino](https://ko-fi.com/wenningtondaquino) ☕
