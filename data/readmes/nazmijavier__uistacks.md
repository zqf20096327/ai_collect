# UI Stacks

**UI Stacks components for AI agents.** Animated React components for AI chat and agents, dashboards and charts, checkout and forms. Built with React, TypeScript, Tailwind CSS and Motion, with Light and Dark themes, keyboard support and screen reader labels.

This repository holds the 71 free components, MIT licensed. Every component has a live preview, props, accessibility notes and a prompt for your coding agent at **[uistacks.dev](https://uistacks.dev)**.

## Quick start

1. Install the two packages the components use:

   ```bash
   npm install motion lucide-react
   ```

2. Add the tokens: paste [`styles/tokens.css`](styles/tokens.css) into your global CSS, after `@import "tailwindcss";`. Dark mode applies under a `.dark` parent.

3. Copy any component from [`components/`](components) into your project and import it.

Prefer an agent? Open the component on uistacks.dev, copy its prompt, and hand it to Claude Code, Cursor or Copilot.

## Install with the shadcn CLI

```bash
npx shadcn add https://uistacks.dev/r/approval-request
```

Or add the registry once to `components.json` (`"registries": { "@uistacks": "https://uistacks.dev/r/{name}.json" }`) and run `npx shadcn add @uistacks/<name>`. The same registry works with the shadcn MCP server, so your agent can search and install by name. Setup for agents, including Pro: [uistacks.dev/docs/agents](https://uistacks.dev/docs/agents).

## Agent skill (Claude Code)

```bash
npx skills add https://uistacks.dev
```

The skill in [`skills/uistacks`](skills/uistacks/SKILL.md) tells your agent to search UI Stacks before writing UI, how to install, and which tokens keep new screens consistent.

## Requirements

- React 19.2 or later and Tailwind CSS 4
- `motion` and `lucide-react`

## Components

### AI Chat

- [Message](https://uistacks.dev/components/message) · `components/ai-chat/message.tsx`
- [Citation](https://uistacks.dev/components/citation) · `components/ai-chat/citation.tsx`
- [Suggestions](https://uistacks.dev/components/suggestions) · `components/ai-chat/suggestions.tsx`
- [Feedback](https://uistacks.dev/components/feedback) · `components/ai-chat/feedback.tsx`
- [Starter cards](https://uistacks.dev/components/starter-cards) · `components/ai-chat/starter-cards.tsx`
- [Citation row](https://uistacks.dev/components/citation-row) · `components/ai-chat/citation-row.tsx`
- [Branch switcher](https://uistacks.dev/components/branch-switcher) · `components/ai-chat/branch-switcher.tsx`

### AI Agents

- [Approval request](https://uistacks.dev/components/approval-request) · `components/ai-agents/approval-request.tsx`

### Actions

- [Button](https://uistacks.dev/components/button) · `components/actions/button.tsx`
- [Icon button](https://uistacks.dev/components/icon-button) · `components/actions/icon-button.tsx`
- [Split button](https://uistacks.dev/components/split-button) · `components/actions/split-button.tsx`
- [Bell button](https://uistacks.dev/components/bell-button) · `components/actions/bell-button.tsx`
- [Copy button](https://uistacks.dev/components/copy-button) · `components/actions/copy-button.tsx`

### Text entry

- [Input](https://uistacks.dev/components/input) · `components/text-entry/input.tsx`
- [Textarea](https://uistacks.dev/components/textarea) · `components/text-entry/textarea.tsx`
- [Chip input](https://uistacks.dev/components/chip-input) · `components/text-entry/chip-input.tsx`
- [Currency input](https://uistacks.dev/components/currency-input) · `components/text-entry/currency-input.tsx`
- [Password input](https://uistacks.dev/components/password-input) · `components/text-entry/password-input.tsx`
- [OTP input](https://uistacks.dev/components/otp-input) · `components/text-entry/otp-input.tsx`
- [Inline edit](https://uistacks.dev/components/inline-edit) · `components/text-entry/inline-edit.tsx`
- [Number input](https://uistacks.dev/components/number-input) · `components/text-entry/number-input.tsx`
- [Search input](https://uistacks.dev/components/search-input) · `components/text-entry/search-input.tsx`
- [Phone input](https://uistacks.dev/components/phone-input) · `components/text-entry/phone-input.tsx`
- [Time input](https://uistacks.dev/components/time-input) · `components/text-entry/time-input.tsx`
- [Copy field](https://uistacks.dev/components/copy-field) · `components/text-entry/copy-field.tsx`
- [Expanding search](https://uistacks.dev/components/expanding-search) · `components/text-entry/expanding-search.tsx`

### Choice

- [Checkbox](https://uistacks.dev/components/checkbox) · `components/choice/checkbox.tsx`
- [Radio group](https://uistacks.dev/components/radio-group) · `components/choice/radio-group.tsx`
- [Switch](https://uistacks.dev/components/switch) · `components/choice/switch.tsx`
- [Combobox](https://uistacks.dev/components/combobox) · `components/choice/combobox.tsx`
- [Quantity stepper](https://uistacks.dev/components/quantity-stepper) · `components/choice/quantity-stepper.tsx`
- [Rating](https://uistacks.dev/components/rating) · `components/choice/rating.tsx`
- [Filter chips](https://uistacks.dev/components/filter-chips) · `components/choice/filter-chips.tsx`
- [Step slider](https://uistacks.dev/components/step-slider) · `components/choice/step-slider.tsx`
- [Theme toggle](https://uistacks.dev/components/theme-toggle) · `components/choice/theme-toggle.tsx`

### Navigation

- [Tabs](https://uistacks.dev/components/tabs) · `components/navigation/tabs.tsx`
- [Accordion](https://uistacks.dev/components/accordion) · `components/navigation/accordion.tsx`
- [Pagination](https://uistacks.dev/components/pagination) · `components/navigation/pagination.tsx`
- [Breadcrumbs](https://uistacks.dev/components/breadcrumbs) · `components/navigation/breadcrumbs.tsx`
- [Tree view](https://uistacks.dev/components/tree-view) · `components/navigation/tree-view.tsx`

### Overlays

- [Tooltip](https://uistacks.dev/components/tooltip) · `components/overlays/tooltip.tsx`
- [Popover](https://uistacks.dev/components/popover) · `components/overlays/popover.tsx`

### Feedback

- [Badge](https://uistacks.dev/components/badge) · `components/feedback/badge.tsx`
- [Progress](https://uistacks.dev/components/progress) · `components/feedback/progress.tsx`
- [Skeleton](https://uistacks.dev/components/skeleton) · `components/feedback/skeleton.tsx`
- [Empty state](https://uistacks.dev/components/empty-state) · `components/feedback/empty-state.tsx`
- [Alert banner](https://uistacks.dev/components/alert-banner) · `components/feedback/alert-banner.tsx`
- [Priority icon](https://uistacks.dev/components/priority-icon) · `components/feedback/priority-icon.tsx`
- [Status icon](https://uistacks.dev/components/status-icon) · `components/feedback/status-icon.tsx`
- [Date chip](https://uistacks.dev/components/date-chip) · `components/feedback/date-chip.tsx`

### Data display

- [Kbd](https://uistacks.dev/components/kbd) · `components/data-display/kbd.tsx`
- [Avatar](https://uistacks.dev/components/avatar) · `components/data-display/avatar.tsx`
- [Stat card](https://uistacks.dev/components/stat-card) · `components/data-display/stat-card.tsx`
- [Code block](https://uistacks.dev/components/code-block) · `components/data-display/code-block.tsx`
- [Avatar stack](https://uistacks.dev/components/avatar-stack) · `components/data-display/avatar-stack.tsx`
- [Leaderboard](https://uistacks.dev/components/leaderboard) · `components/data-display/leaderboard.tsx`
- [Timeline](https://uistacks.dev/components/timeline) · `components/data-display/timeline.tsx`
- [Sortable list](https://uistacks.dev/components/sortable-list) · `components/data-display/sortable-list.tsx`
- [Audio player](https://uistacks.dev/components/audio-player) · `components/data-display/audio-player.tsx`
- [Rolling number](https://uistacks.dev/components/rolling-number) · `components/data-display/rolling-number.tsx`

### Charts

- [Grouped bar](https://uistacks.dev/components/grouped-bar) · `components/charts/grouped-bar.tsx`
- [Compare bars](https://uistacks.dev/components/compare-bars) · `components/charts/compare-bars.tsx`
- [Ring stats](https://uistacks.dev/components/ring-stats) · `components/charts/ring-stats.tsx`
- [Donut chart](https://uistacks.dev/components/donut-chart) · `components/charts/donut-chart.tsx`

### Marketing

- [Announcement pill](https://uistacks.dev/components/announcement-pill) · `components/marketing/announcement-pill.tsx`
- [Copy-prompt box](https://uistacks.dev/components/copy-prompt-box) · `components/marketing/copy-prompt-box.tsx`
- [Newsletter signup](https://uistacks.dev/components/newsletter-signup) · `components/marketing/newsletter-signup.tsx`
- [Changelog entry](https://uistacks.dev/components/changelog-entry) · `components/marketing/changelog-entry.tsx`
- [Metric strip](https://uistacks.dev/components/metric-strip) · `components/marketing/metric-strip.tsx`
- [CTA banner](https://uistacks.dev/components/cta-banner) · `components/marketing/cta-banner.tsx`

### Effects

- [Confetti](https://uistacks.dev/components/confetti) · `components/effects/confetti.tsx`

## UI Stacks Pro

The rest of the library (every component, plus blocks and full app templates) is part of UI Stacks Pro and is not in this repository. See [uistacks.dev/pricing](https://uistacks.dev/pricing).

## Contributing

Bug reports and ideas are welcome in [Issues](../../issues). See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

The components in this repository are [MIT licensed](LICENSE). Pro components, blocks and templates are covered by the [UI Stacks license](https://uistacks.dev/license).
