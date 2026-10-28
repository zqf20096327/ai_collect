# AI Video Agent

> A free, open-source video production playbook for the AI assistant you already use.

Give Claude, Claude Code, Codex, Cursor, Windsurf, or another AI assistant a
complete video-production workflow. Ask it to plan a story, generate shots,
preserve a character or product, create a social video, make a talking-head or
faceless explainer, repurpose long-form footage, or prepare a draft for review.

Connect a compatible media generation and editing service when you want the
assistant to execute the workflow. The repository itself is a portable set of
instructions and references: it does not host a rendering service, publish
content, or require a particular user interface.

## Why use it?

- Use the AI assistant you already know instead of learning another video
  dashboard.
- Start with a complete production plan or run one focused workflow at a time.
- Keep scripts, storyboards, asset roles, job IDs, QA findings, and decisions
  together in your project folder.
- Choose a live model/schema per shot instead of assuming one model fits every
  duration, ratio, reference, audio, or motion requirement.
- Read, adapt, and extend the workflows because the project is open source.

## What you can ask it to do

Use plain language. For example:

- “Turn this product brief into three 9:16 ad concepts. Preserve the label and
  return draft URLs with QA notes.”
- “Create a storyboard for this short story, approve the keyframes, then
  animate the selected shots with consistent characters.”
- “Make a cinematic one-shot reveal with a slow dolly and controlled lighting.”
- “Turn this topic into a narrated faceless explainer with sourced claims and
  captions.”
- “Create a paper-collage explainer from this topic and keep the beats in order.”
- “Make a curiosity-led 3D educational short with an approved character sheet.”
- “Find the strongest moments in this long video, reframe them vertically, and
  proofread the captions.”
- “Animate this authorized logo treatment and return a transparent end-card
  recommendation.”
- “Create a music-led visual sequence from this track and return the beat map.”
- “Apply a short artistic effect to this approved clip without presenting it as
  real footage.”

The assistant chooses the narrowest workflow, asks for missing decisions that
materially change the result, and returns evidence, assumptions, failures, and
next steps.

## Use it with your AI assistant

This repository works with the assistant you already use:

| Assistant | How to add the video playbook |
|---|---|
| Claude Code | Keep `AGENTS.md` in the project and add selected skill folders to `.claude/skills/`. |
| Codex | Keep `AGENTS.md` in the project and load the relevant `SKILL.md` with the task. |
| Cursor or Windsurf | Add `AGENTS.md` and the relevant skill as project instructions. |
| Claude.ai or another file-aware assistant | Add the files to project knowledge or the conversation, then connect the available media tools. |
| Other AI assistants | Load `AGENTS.md` and the relevant skill through the assistant's project-instruction or file-upload feature. |

See [installation for existing agents](references/agent-installation.md) for
setup patterns. Load [AGENTS.md](AGENTS.md) for the common routing, lifecycle,
privacy, and approval rules.

## Quick start

1. Choose an assistant that can read project files and use tools.
2. Add `AGENTS.md` and the native skill folder you need from `agents/`. Each
   workflow is a self-contained `SKILL.md`; external repository links are only
   source attribution and are not required at runtime.
3. Connect a compatible media provider through MCP or REST. Keep credentials
   in the assistant's secure settings or environment.
4. Give the assistant the brief, source media, reference roles, target format,
   rights/consent state, budget, and definition of done.
5. Ask it to plan first when the request has multiple shots or material cost.

The assistant only writes local project artifacts when you ask for them or the
project convention permits it. It does not publish to an external channel as
part of these workflows.

## Video workflows

Start with [Video Strategist](agents/video-strategist/SKILL.md) for a broad
request. For a focused task, load the matching workflow directly.

| Workflow | What it helps with |
|---|---|
| [Video Strategist](agents/video-strategist/SKILL.md) | Route a broad brief, build a dependency graph, select workflows, and return a production plan |
| [Video Project Setup](agents/video-project-setup/SKILL.md) | Set up project context, delivery rules, asset roles, rights, and approval gates |
| [Video Generation](agents/video-generation/SKILL.md) | Generate prompt-led, image-led, or reference-led video clips |
| [Storyboard to Video](agents/storyboard-to-video/SKILL.md) | Turn a premise or script into ordered beats, keyframes, shots, and an assembly plan |
| [Micro-drama Video](agents/micro-drama-video/SKILL.md) | Develop a short scripted drama through story, character sheets, keyframes, animated shots, and assembly |
| [Cinematic Direction](agents/cinematic-direction/SKILL.md) | Translate intent into composition, camera, lens, lighting, motion, and sound direction |
| [Social Video](agents/social-video/SKILL.md) | Turn brand context and a social brief into copy, storyboard, references, and video drafts |
| [Music Video](agents/music-video/SKILL.md) | Pair a track or music brief with beat-mapped visual keyframes and animated scenes |
| [Faceless Video](agents/faceless-video/SKILL.md) | Create a narrated, non-presenter video from a topic, voice asset, coverage, and captions |
| [B-roll Generation](agents/b-roll-generation/SKILL.md) | Identify visual gaps and generate supplemental, clearly labeled coverage |
| [Paper-collage Explainer](agents/paper-collage-explainer/SKILL.md) | Create a high-contrast editorial collage explainer from a topic, presenter, or anchor photo |
| [Curiosity 3D Explainer](agents/curiosity-3d-explainer/SKILL.md) | Create a curiosity-led 3D educational short with character/object continuity |
| [Logo Animation](agents/logo-animation/SKILL.md) | Approve a logo treatment and animate a controlled brand reveal |
| [Video Effects](agents/video-effects/SKILL.md) | Apply a short artistic effect or VFX transformation to an approved parent |
| [Meme Video](agents/meme-video/SKILL.md) | Develop a short humorous concept with setup, escalation, punchline, and safe variants |
| [Consented Romantic Video](agents/consented-romantic-video/SKILL.md) | Draft non-explicit romantic scenes only from authorized adult references |
| [Video Editing](agents/video-editing/SKILL.md) | Edit, extend, transition, and combine existing clips with parent tracking |
| [Video Assembly](agents/video-assembly/SKILL.md) | Turn approved clips, audio, captions, and timing decisions into a reproducible final draft |
| [Video Captioning](agents/video-captioning/SKILL.md) | Prepare, proofread, render, or hand off captions and subtitles for an approved cut |
| [Character Continuity](agents/character-continuity/SKILL.md) | Preserve an authorized person, fictional character, product, or world across shots |
| [Product Video Ads](agents/product-video-ads/SKILL.md) | Build product-led ads while protecting geometry, labels, claims, and rights |
| [Avatar / UGC](agents/avatar-ugc/SKILL.md) | Create consented presenter, avatar, lip-sync, and UGC-style drafts |
| [Short-form Repurposing](agents/short-form-repurposing/SKILL.md) | Find highlights, rank clips, reframe them, and produce caption candidates |
| [YouTube Shorts](agents/youtube-shorts/SKILL.md) | Apply a focused 9:16 Shorts workflow with timestamps, ranking, crop, captions, and provenance |
| [Motion Control](agents/motion-control/SKILL.md) | Use driving video, first/last frames, last-image controls, and controlled movement |
| [Video Enhancement](agents/video-enhancement/SKILL.md) | Upscale a selected parent and verify the enhanced child for new defects |
| [Video Model Selection](agents/video-model-selection/SKILL.md) | Compare live model schemas, constraints, cost, and fallback paths before rendering |
| [Ad Creative Remake](agents/ad-creative-remake/SKILL.md) | Design performance-informed ad variations when external data is supplied |

Workflows can be combined. For example, a product launch can use project
setup, product ads, cinematic direction, character continuity, social video,
and short-form repurposing. A narrated explainer can combine project setup,
curiosity 3D or paper collage, B-roll, music, captions, and enhancement.

## Logical capability map

The skills use provider-neutral capability names so a host can map them to MCP
tools, REST endpoints, or another approved media runtime:

| Capability | What it covers |
|---|---|
| `media.generate_video` | Text-to-video, image-to-video, reference video, motion, and model-specific generation |
| `media.generate_image` | Optional still/keyframe, product, character, or logo preparation |
| `media.generate_music` | Optional original music or music variation for a video workflow |
| `media.generate_speech` | Optional narration handoff to an approved voice workflow |
| `media.edit_video` | Prompt-based video transformation, effects, or video-to-video editing |
| `media.extend_video` | Continue an existing clip through an endpoint-specific extension path |
| `media.lipsync` | Align authorized audio with an image or video presenter |
| `media.clip_video` | Find highlights or candidate segments in a source video |
| `media.reframe_video` | Adapt a selected segment to a target aspect ratio |
| `media.caption_video` | Generate or burn captions from an approved source |
| `media.combine_video` | Join approved clips in a known order |
| `media.upscale_video` | Upscale a selected parent for delivery |
| `media.upload_file` | Convert a local media input into a hosted URL |
| `media.check_result` | Poll an asynchronous job and retrieve its result |
| `media.search_models` | Discover current models, schemas, endpoints, and cost metadata |
| `media.account_balance` | Check available credits before an expensive render |

The map describes intent, not guaranteed availability. A host must check the
connected tool surface and selected schema at execution time.

## Connect media tools

The included provider adapter currently targets Muapi through MCP or REST, but
the skills remain portable. See [installation for existing agents](references/agent-installation.md)
and [the media-tool reference](references/muapi-video-tools.md) for the
connection, upload, polling, webhook, schema, and fallback details.

| Setup | Connection guidance |
|---|---|
| Claude Code or Claude Desktop | Use the local stdio connection described in the installation reference. |
| Cursor, Windsurf, or another hosted MCP assistant | Use the provider's hosted MCP endpoint with a secret-backed authorization header. |
| Codex, Claude.ai, or REST-only setup | Use the assistant's supported connector or the provider's REST API with a secret-backed request. |
| Different provider or self-hosted runtime | Map the logical capabilities to its live schemas and keep the same input/output contracts. |

Keep API keys, OAuth credentials, signed URLs, and private media out of prompts,
reports, committed files, and webhook URLs. If a transport lacks local-file
upload, use a hosted URL or an approved upload path.

## Model and workflow selection

[MODELS.md](MODELS.md) is a dated decision guide, not a frozen model catalog.
Choose the operation and production workflow first, then verify the connected
runtime's live schema, supported references, duration, ratio, output shape,
retention, and cost.

Use these general rules:

- prompt-led text-to-video for deliberately unconstrained shots;
- image-to-video or reference-led generation when a character, product,
  location, or composition must carry across shots;
- video editing or extension when an approved parent should remain the source;
- first/last-frame or driving-video controls when camera or motion endpoints
  are explicitly supported;
- clipping, reframing, captioning, assembly, and enhancement as separate
  stages unless the live schema proves that one operation includes them; and
- adjacent image or voice skills for still references, keyframes, narration,
  dubbing, or audio that the video runtime does not provide.

Use [Video Model Selection](agents/video-model-selection/SKILL.md) when model
choice is the main question. Use [Video Strategist](agents/video-strategist/SKILL.md)
when selection is part of a larger production plan. Never copy fields from one
model family into another or treat a successful submission as a completed
video.

## Costs and approvals

The repository is free and open source. Connected providers may charge for
generation, editing, audio, uploads, or utilities and may enforce quotas or
retention limits. Check the live model/schema and estimate a material batch
before running it.

Before a paid call, the assistant should:

- identify the operation, model/endpoint, and expected output count;
- check balance and a live estimate when available;
- explain an estimate as a planning signal, not a quote;
- confirm the draft, exploration, or production-candidate budget;
- ask before broad variants, premium models, native audio, lip-sync, long
  clips, repeated retries, final upscaling, or publication; and
- start with a small representative batch and preserve failed/partial jobs.

A successful submission is not proof that a video completed. Retain the job ID,
poll or receive the result, and report the final status, output URL, retention
expectation, and unresolved failures.

## Video coverage

The native skill folders cover:

- project context, asset roles, rights, approvals, and repeatable series;
- model selection, prompt/image/reference-led generation, storyboards, and
  scripted micro-dramas;
- character, product, presenter, avatar, UGC, social, cinematic, music-led,
  faceless, paper-collage, and curiosity-led 3D videos;
- B-roll, logo animation, motion control, VFX/effects, editing, assembly,
  captioning, enhancement, and audio/voice handoffs;
- long-form clipping, ranked short-form repurposing, and a focused YouTube
  Shorts preset; and
- meme concepts, consented non-explicit romantic scenes, and performance-data-
  gated ad creative drafts.

Actual model support, input limits, output retention, platform rules, and tool
availability depend on the connected runtime and assistant transport.

Run the dependency-free package check with:

~~~sh
python3 scripts/validate_package.py
git diff --check
~~~

## Reports and saved work

When you ask the assistant to save its work, it can keep project context,
continuity notes, asset manifests, run receipts, and QA notes in a `.video/`
folder. A typical project looks like this:

~~~text
.video/
  project.md
  assets/<asset-id>.json
  continuity/<continuity-id>.md
  runs/YYYY-MM-DD/<run-id>/plan.md
  runs/YYYY-MM-DD/<run-id>/receipt.json
  runs/YYYY-MM-DD/<run-id>/qa.md
  exports/<export-id>.json
~~~

See [reports and receipts](references/reports-and-receipts.md) for the format.
Receipts contain job IDs and sanitized references, not API keys, raw private
media, or unnecessary personal data.

## Quality, privacy, and rights

- Confirm the brief, audience, language, duration, ratio, audio, source roles,
  and definition of done before paid work.
- Report provider output, measured technical checks, creative judgment, and
  hypotheses separately.
- Treat missing data, unsupported fields, uncertain transcription, and unknown
  rights as unknown—not as success.
- Confirm rights for footage, music, logos, products, locations, voices,
  performances, private media, and identifiable people.
- Do not create non-consensual impersonation, exploitative sexual content,
  deceptive political media, or harmful likeness manipulation. Treat minors
  and public-figure likenesses as high-risk.
- Generated visuals are not evidence of a real event, product performance,
  medical result, historical scene, testimonial, or claim.
- Proofread exact copy, labels, captions, names, numbers, and regulated claims
  in an editable post-production layer whenever possible.
- Review the complete clip—not just the poster frame—for temporal drift,
  flicker, anatomy, product geometry, audio sync, captions, crop safety, and
  export compatibility.
- External platforms, ad accounts, creator outreach, and publishing are
  outside this repository unless a separate agent and explicit approval handle
  them.

See [video QA](references/video-qa.md) for the full review protocol.

See [cross-repository coverage](references/repo-coverage.md) for the source
audit, promoted workflows, adjacent agents, model references, and intentional
exclusions behind this package.

## Limitations

The assistant must be able to read the files and connect to the required media
tools. Model names, schemas, availability, pricing, output retention, and
platform rules can change. Hosted and stdio tools may differ, and a provider's
generic generation tool is not a universal frame-extraction, editing, or
assembly contract.

The image and voice agents are optional adjacent handoffs:

- [open-ai-image-agent](https://github.com/SamurAIGPT/open-ai-image-agent) —
  stills, reference frames, product imagery, and thumbnails.
- [open-ai-voice-agent](https://github.com/SamurAIGPT/open-ai-voice-agent) —
  narration, dubbing, voice, and audio-source workflows.

[Ad Creative Remake](agents/ad-creative-remake/SKILL.md) remains data-gated
until an approved performance-data source supplies campaign evidence. Long-form
editorial judgment, final color/audio mastering, music licensing, disclosure,
and platform publishing remain human or adjacent-agent responsibilities.

## Related projects and source libraries

- [Agency Agents OS](https://github.com/Anil-matcha/agency-agents-os) — the
  wider catalog of specialized agents.
- [Generative-Media-Skills](https://github.com/SamurAIGPT/Generative-Media-Skills)
  — reusable media primitives and workflow recipes.
- [OpenMontage](https://github.com/Anil-matcha/OpenMontage) — agentic video
  production and montage workflow inspiration.
- [vox-ai-motion-graphics-generator](https://github.com/Anil-matcha/vox-ai-motion-graphics-generator)
  — source inspiration for paper-collage explainers.
- [zack-d-films-ai-video-generator](https://github.com/Anil-matcha/zack-d-films-ai-video-generator)
  — source inspiration for staged 3D curiosity explainers.
- [ai-meme-generator](https://github.com/SamurAIGPT/ai-meme-generator) — source
  inspiration for short, caption-led meme video concepts.
- [ai-kissing-video-generator](https://github.com/SamurAIGPT/ai-kissing-video-generator)
  — source inspiration for strictly consented, non-explicit romantic-scene
  workflows.
- [open-ai-content-repurposing-agent](https://github.com/SamurAIGPT/open-ai-content-repurposing-agent)
  — adjacent content repurposing workflows.
- [AI-Youtube-Shorts-Generator](https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator)
  — source inspiration for long-form highlight extraction and Shorts packaging.
- [open-ai-ads-agent](https://github.com/SamurAIGPT/open-ai-ads-agent) —
  campaign-level ad decisions and publishing boundaries.

## Contributing

Improvements are welcome. Keep workflows focused, reusable, evidence-based,
rights-aware, and usable by more than one AI assistant. For a new skill:

1. Give it its own `agents/<name>/SKILL.md` with complete frontmatter.
2. Define its inputs, routing boundary, logical capabilities, approval/cost
   gate, output contract, QA, rights, and failure behavior.
3. Update `AGENTS.md`, `MODELS.md` when model facts change, this README, and
   the validator.
4. Keep provider details in the connection reference and verify live schemas
   before hard-coding fields.
5. Add source attribution or a focused reference when the workflow introduces
   a new risk, artifact type, or approval boundary.

Before opening a change, run:

~~~sh
python3 scripts/validate_package.py
git diff --check
~~~

## License

[MIT](LICENSE)
