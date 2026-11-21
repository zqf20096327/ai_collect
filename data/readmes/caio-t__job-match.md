<p align="center">
  <img src="assets/logo.png" alt="job-match logo" width="128" height="128">
</p>

# job-match

> A Claude Code skill that reads your CV, searches for open jobs and ranks them by how well they fit you.
> It reads every posting in full and shows the gaps along with the matches.

Made by **Caio Teixeira** · [LinkedIn](https://www.linkedin.com/in/caio-teixeira-espirito-santo/) · [GitHub](https://github.com/caio-t)

[Português](#português) · [English](#english)

---

## English

### What it does

You ask for jobs. `job-match` then:

1. **Reads your CV** from the folder where the Claude Code session started. That can be PDF, DOCX,
   HTML, Markdown, or profile data in code such as `profile.ts` or `resume.json`. With no CV there,
   it asks you for one, or for your LinkedIn profile saved as PDF.
2. **Searches the right sources.** For a named company it starts with that company's careers page.
   Otherwise it uses the boards that work best for your region:

   | Region | Sources |
   |---|---|
   | Portugal | ITJobs.pt, LinkedIn Jobs, Landing.jobs, Net-Empregos, Indeed, Glassdoor |
   | Brazil | LinkedIn Jobs, Gupy, Programathor, Indeed, Glassdoor, Catho |
   | Remote | LinkedIn Jobs, We Work Remotely, Remote OK, Wellfound, Otta |

3. **Reads each posting in full**, not just the title. It scores required tech, seniority, role type,
   location and work model.
4. **Drops postings with hard blockers**, such as a required language you don't speak or a core stack
   you've never used, and tells you what it dropped.
5. **Lists the top 10**, or the number you ask for. Each entry has match stars, the reasons it fits,
   your gaps and a direct link.

6. **Writes a tailored CV on request.** Ask for "the CV for job #1" and it first asks about any
   requirement your CV doesn't show. It then writes an A4 CV in the posting's language that puts the
   matching experience first, saves it as PDF in your folder and lists the gaps it left out.

By default it only searches and lists. It never applies, fills in forms or sends messages unless
you ask.

### Install

**Claude app (claude.ai, desktop, mobile) and Cowork:** open **Customize → Plugins → Discover**,
search for **Job Match** and add it. Attach your CV to the chat when you ask for jobs. Needs a paid
plan.

**Claude Code:** install it from this repository in one step:

```text
/plugin install job-match --marketplace caio-t/job-match
```

On older versions, run `/plugin marketplace add caio-t/job-match` and then
`/plugin install job-match@caio-teixeira`. To install by hand instead, copy the `skills/job-match`
folder of this repository to `~/.claude/skills/job-match`.

Restart Claude Code (or open a new session) and the skill is available.

### Usage examples

Open Claude Code in the folder that holds your CV, then ask in plain language:

```text
List the top 10 openings at Aubay that match my profile
```

```text
Top 5 remote Node.js / TypeScript jobs that fit my CV
```

```text
15 senior .NET jobs in Lisbon or Porto, hybrid is fine
```

```text
Which tech lead roles in Portugal match me best? Ignore anything that needs French.
```

After the list, ask for a tailored CV (and, if you want, a cover letter):

```text
Make the CV for job #1, and a short cover letter
```

You can also call it directly:

```text
/job-match 20 jobs in Berlin, English-speaking teams
```

With no CV in the folder, it asks first:

```text
I couldn't find a CV in this folder. Where should I get your profile from?
  1. Path to a CV file
  2. Use my LinkedIn profile (saved as PDF or pasted)
```

### Example output

```markdown
| # | Job | Location · Model | Match | Why |
|---|---|---|---|---|
| 1 | Node.js Tech Lead | Porto · Hybrid | ⭐⭐⭐⭐⭐ | Node.js, Angular, TypeScript and SQL Server: all on your CV. Asks for 5+ yrs and mentoring. Gap: AWS SAM. |
| 2 | .NET / Angular Developer | Lisbon · not stated | ⭐⭐⭐⭐ | C# .NET, Angular, Azure DevOps. Gap: Azure Functions. |
| 3 | Senior Backend (.NET & Azure) | Lisbon · not stated | ⭐⭐⭐⭐ | Microservices, messaging, Docker, tests. Gap: Kubernetes. |
| … | | | | |

**Recommendation:** apply to #1 now with your Node.js CV, and put Angular and SQL Server in the summary.
**Dropped:** roles that require French, SAP/Dynamics functional roles, junior roles.
**Warnings:** #2 doesn't say whether it is hybrid, so confirm with the recruiter.
```

### Principles

- **Only facts from your CV.** A skill the job asks for and your CV doesn't show counts as a gap, not
  a match. Tailored CVs reorder and emphasise; they never add years, titles or degrees you don't have.
- **CVs stay in your folder.** They hold your phone and email, so they are never written into the
  skill, and you are warned if the folder is a git repository.
- **The source of truth is the company page.** Aggregator listings are checked there, because
  aggregators keep closed jobs.
- **Empty fields stay empty.** A posting that doesn't state its work model shows "not stated" instead
  of a guess.
- **No personal data is stored** in the skill.
- **Sites' terms are respected.** It never logs in, never browses LinkedIn, Indeed or Glassdoor on its
  own (their terms forbid automated access) and uses only what search results show for them. It
  prefers company career pages and the public job feeds of recruiting platforms.

---

## Português

### O que faz

Pedes vagas e o `job-match`:

1. **Lê o teu CV** na pasta onde a sessão do Claude Code começou. Pode ser PDF, DOCX, HTML, Markdown ou
   dados de perfil no código. Se não houver nenhum, pede-te o CV ou o teu perfil do LinkedIn
   guardado em PDF.
2. **Procura nas fontes certas.** Com uma empresa indicada, começa pela página de carreiras dela. Sem
   empresa, usa os melhores sites da tua região (ITJobs, Landing.jobs, Gupy, LinkedIn Jobs…).
3. **Lê cada vaga completa** e pontua tecnologias obrigatórias, senioridade, tipo de cargo, local e
   regime.
4. **Exclui as vagas com bloqueios**, como uma língua obrigatória que não falas, e diz quais excluiu.
5. **Lista as 10 melhores**, ou o número que pedires, com estrelas, o porquê, as tuas lacunas e o link
   direto.

6. **Cria um CV à medida, se pedires.** Pergunta primeiro pelos requisitos que o CV não mostra e gera
   um PDF A4 no idioma da vaga, com a experiência relevante em destaque e as lacunas listadas.

Por omissão só pesquisa e lista. Nunca se candidata, não preenche formulários nem envia mensagens sem
pedires.

### Instalar

- **App do Claude (claude.ai, desktop, telemóvel) e Cowork:** em **Customize → Plugins → Discover**,
  procura **Job Match** e adiciona. Anexa o CV à conversa quando pedires vagas. Precisa de um plano
  pago.
- **Claude Code:** corre `/plugin install job-match --marketplace caio-t/job-match` (em versões
  antigas: `/plugin marketplace add caio-t/job-match` e depois `/plugin install job-match@caio-teixeira`),
  ou copia a pasta
  `skills/job-match` deste repositório para `~/.claude/skills/job-match`.

### Exemplos de uso

```text
Liste as 10 principais vagas da Aubay com match no meu perfil
```

```text
5 vagas remotas de Node.js que combinem com o meu CV
```

```text
Quais vagas de tech lead em Portugal têm mais match comigo? Ignora as que pedem francês.
```

```text
Faz o CV para a vaga #2 e uma carta de apresentação curta
```

```text
/job-match 15 vagas de .NET em Lisboa ou Porto
```

## Self-install edition (unsupported, at your own risk)

The original edition of this skill is kept in a separate repository,
[caio-t/job-match-self-install](https://github.com/caio-t/job-match-self-install). It is **not** part
of the plugin above, was **not reviewed by Anthropic** and installs only by hand.

> [!CAUTION]
> That edition drives your own browser on LinkedIn and job sites and can call pages' internal
> endpoints. **LinkedIn, Indeed, Glassdoor and other sites forbid automated access in their terms of
> use**, so using it may get your account limited or banned. **You install and use it entirely at
> your own risk and are solely responsible for complying with each site's terms and the law.** It is
> provided "as is", without warranty, and the author accepts no liability.

**Português:** a edição original está num repositório à parte,
[caio-t/job-match-self-install](https://github.com/caio-t/job-match-self-install). Não faz parte do
plugin, não foi revista pela Anthropic e **instalas e usas por tua conta e risco**: pode violar os
termos de uso do LinkedIn, do Indeed e do Glassdoor, e és o único responsável por isso.

## Author

**Caio Teixeira** · [LinkedIn](https://www.linkedin.com/in/caio-teixeira-espirito-santo/) · [GitHub](https://github.com/caio-t)

## License

MIT
