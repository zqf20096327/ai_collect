**English** | [中文](README-CN.md)

# Arco Design — AI Skills

> Complete skill sets for `@arco-design/web-react` and `@arco-design/web-vue`, enabling AI agents to accurately use Arco Design when building React or Vue applications.

## What is this?

A collection of **skill files** covering the [Arco Design](https://arco.design) React and Vue component libraries:

- **React skill** for `@arco-design/web-react` — 70 components, 5 overview guides, 5 pattern guides, and 2 hooks references
- **Vue skill** for `@arco-design/web-vue` — 74 components, 5 overview guides, and 5 pattern guides

When writing code with Arco Design, AI agents automatically load the relevant skill to get accurate API info and best practices.

## Directory Structure

```
skills/
└── arco-design/
    ├── SKILL.md                           # Entry point (auto-loaded by agents)
    └── references/                        # All referenced skill files
        ├── overview/                      # Setup & configuration
        │   ├── getting-started.md         #   Install, import, on-demand loading
        │   ├── config-provider.md         #   ConfigProvider global settings
        │   ├── theming.md                 #   CSS variables, Less, dark mode
        │   ├── internationalization.md    #   i18n locale switching
        │   └── architecture.md            #   Component patterns, controlled/uncontrolled, ref
        ├── components/                    # Component skills (by category)
        │   ├── general/                   #   Button, Icon, Typography, Link, Divider
        │   ├── layout/                    #   Grid, Layout, Space
        │   ├── navigation/               #   Menu, Tabs, Breadcrumb, Dropdown, Pagination...
        │   ├── data-entry/                #   Form, Input, Select, DatePicker, Upload...
        │   ├── data-display/              #   Table, List, Card, Tree, Tooltip...
        │   ├── feedback/                  #   Modal, Message, Notification, Drawer...
        │   └── other/                     #   Portal, Trigger, BackTop, Watermark, ResizeBox
        ├── patterns/                      # Common patterns & best practices
        │   ├── form-patterns.md           #   Dynamic forms, validation, async submit
        │   ├── table-patterns.md          #   Remote data, editable rows, virtual scroll
        │   ├── modal-patterns.md          #   Form-in-modal, confirmation, nested drawers
        │   ├── controlled-uncontrolled.md #   Controlled vs uncontrolled patterns
        │   └── responsive-design.md       #   Grid breakpoints, adaptive layout
        └── hooks/
            ├── use-verification-code.md   #   useVerificationCode hook
            └── use-watermark.md           #   useWatermark hook
```

The Vue skill lives in `skills/arco-design-vue/` and follows the same entry/reference structure for `@arco-design/web-vue`.

## Skill File Structure

Each component skill file follows a consistent format:

1. **YAML Frontmatter** — `name`, `description` (English, scenario-based), `user-invocable: false`
2. **Basic Usage** — Runnable TSX code examples
3. **API Tables** — Complete Props, Events, Methods reference
4. **Common Patterns** — Real-world code snippets
5. **Best Practices** — Usage tips and pitfalls to avoid

## Entry Point

[skills/arco-design/SKILL.md](skills/arco-design/SKILL.md) is the React entry skill for `@arco-design/web-react`.
[skills/arco-design-vue/SKILL.md](skills/arco-design-vue/SKILL.md) is the Vue entry skill for `@arco-design/web-vue`.

Each entry skill contains:

- **Critical conventions** — Import patterns, controlled mode, sub-component access, Arco-specific differences from Ant Design
- **Component index** — Categorized tables with "Use for" descriptions for every component
- **Pattern references** — Links to detailed guides for complex scenarios

All sub-skills have `user-invocable: false` — agents load them automatically based on description matching.

## Component Index

### General

| Component | File | Description |
|-----------|------|-------------|
| Button | [button.md](skills/arco-design/references/components/general/button.md) | Buttons, button groups, icon buttons, loading state |
| Icon | [icon.md](skills/arco-design/references/components/general/icon.md) | Built-in icons, custom SVG, IconFont |
| Typography | [typography.md](skills/arco-design/references/components/general/typography.md) | Headings, paragraphs, ellipsis, copyable/editable text |
| Link | [link.md](skills/arco-design/references/components/general/link.md) | Hyperlinks with icon and hover states |
| Divider | [divider.md](skills/arco-design/references/components/general/divider.md) | Horizontal/vertical dividers with text |

### Layout

| Component | File | Description |
|-----------|------|-------------|
| Grid | [grid.md](skills/arco-design/references/components/layout/grid.md) | 24-column Row/Col grid, responsive breakpoints |
| Layout | [layout.md](skills/arco-design/references/components/layout/layout.md) | Page skeleton: Header, Sider, Content, Footer |
| Space | [space.md](skills/arco-design/references/components/layout/space.md) | Consistent spacing between elements |

### Navigation

| Component | File | Description |
|-----------|------|-------------|
| Menu | [menu.md](skills/arco-design/references/components/navigation/menu.md) | Sidebar nav, top nav, sub-menus, collapsible |
| Tabs | [tabs.md](skills/arco-design/references/components/navigation/tabs.md) | Tab switching, card tabs, editable tabs |
| Dropdown | [dropdown.md](skills/arco-design/references/components/navigation/dropdown.md) | Dropdown menus, context menus |
| Breadcrumb | [breadcrumb.md](skills/arco-design/references/components/navigation/breadcrumb.md) | Navigation hierarchy path |
| Pagination | [pagination.md](skills/arco-design/references/components/navigation/pagination.md) | Page navigation, size changer |
| Steps | [steps.md](skills/arco-design/references/components/navigation/steps.md) | Step-by-step workflows |
| Affix | [affix.md](skills/arco-design/references/components/navigation/affix.md) | Pin element to viewport on scroll |
| Anchor | [anchor.md](skills/arco-design/references/components/navigation/anchor.md) | In-page anchor navigation |
| PageHeader | [page-header.md](skills/arco-design/references/components/navigation/page-header.md) | Page title + back button + actions |

### Data Entry

| Component | File | Description |
|-----------|------|-------------|
| Form | [form.md](skills/arco-design/references/components/data-entry/form.md) | Form building, validation, Form.List, useForm |
| Input | [input.md](skills/arco-design/references/components/data-entry/input.md) | Text, password, search, textarea, prefix/suffix |
| Select | [select.md](skills/arco-design/references/components/data-entry/select.md) | Dropdown select, multi-select, remote search |
| DatePicker | [date-picker.md](skills/arco-design/references/components/data-entry/date-picker.md) | Date/range picker, week/month/year (dayjs) |
| TimePicker | [time-picker.md](skills/arco-design/references/components/data-entry/time-picker.md) | Time selection, range, 12h format |
| InputNumber | [input-number.md](skills/arco-design/references/components/data-entry/input-number.md) | Numeric input, stepper, precision |
| Checkbox | [checkbox.md](skills/arco-design/references/components/data-entry/checkbox.md) | Multi-select, select all, indeterminate |
| Radio | [radio.md](skills/arco-design/references/components/data-entry/radio.md) | Single select, button-style radio |
| Switch | [switch.md](skills/arco-design/references/components/data-entry/switch.md) | Toggle switch, loading, text labels |
| Slider | [slider.md](skills/arco-design/references/components/data-entry/slider.md) | Range slider, marks, vertical |
| Rate | [rate.md](skills/arco-design/references/components/data-entry/rate.md) | Star rating, half-star, custom characters |
| Cascader | [cascader.md](skills/arco-design/references/components/data-entry/cascader.md) | Multi-level cascade selection |
| TreeSelect | [tree-select.md](skills/arco-design/references/components/data-entry/tree-select.md) | Select from tree structure |
| Transfer | [transfer.md](skills/arco-design/references/components/data-entry/transfer.md) | Transfer items between two lists |
| AutoComplete | [auto-complete.md](skills/arco-design/references/components/data-entry/auto-complete.md) | Input autocomplete, search suggestions |
| Mentions | [mentions.md](skills/arco-design/references/components/data-entry/mentions.md) | @mention users/topics |
| InputTag | [input-tag.md](skills/arco-design/references/components/data-entry/input-tag.md) | Tag input, add/remove tags |
| Upload | [upload.md](skills/arco-design/references/components/data-entry/upload.md) | File upload, drag-and-drop, image preview |
| ColorPicker | [color-picker.md](skills/arco-design/references/components/data-entry/color-picker.md) | Color selection (hex/rgb/hsl) |
| VerificationCode | [verification-code.md](skills/arco-design/references/components/data-entry/verification-code.md) | OTP / verification code input |

### Data Display

| Component | File | Description |
|-----------|------|-------------|
| Table | [table.md](skills/arco-design/references/components/data-display/table.md) | Data tables, sort, filter, pagination, virtual scroll |
| List | [list.md](skills/arco-design/references/components/data-display/list.md) | Data lists, paginated, virtual scroll |
| Card | [card.md](skills/arco-design/references/components/data-display/card.md) | Card containers, cover, grid, actions |
| Tree | [tree.md](skills/arco-design/references/components/data-display/tree.md) | Tree structure, checkable, draggable |
| Tooltip | [tooltip.md](skills/arco-design/references/components/data-display/tooltip.md) | Hover text hints |
| Popover | [popover.md](skills/arco-design/references/components/data-display/popover.md) | Popup cards with rich content |
| Avatar | [avatar.md](skills/arco-design/references/components/data-display/avatar.md) | User avatars, avatar groups |
| Badge | [badge.md](skills/arco-design/references/components/data-display/badge.md) | Numeric badges, status dots |
| Tag | [tag.md](skills/arco-design/references/components/data-display/tag.md) | Status tags, closable, checkable |
| Carousel | [carousel.md](skills/arco-design/references/components/data-display/carousel.md) | Image carousels, slideshows |
| Collapse | [collapse.md](skills/arco-design/references/components/data-display/collapse.md) | Collapsible panels, accordion |
| Descriptions | [descriptions.md](skills/arco-design/references/components/data-display/descriptions.md) | Key-value detail display |
| Calendar | [calendar.md](skills/arco-design/references/components/data-display/calendar.md) | Calendar view, event marking |
| Comment | [comment.md](skills/arco-design/references/components/data-display/comment.md) | Comments, nested replies |
| Empty | [empty.md](skills/arco-design/references/components/data-display/empty.md) | Empty state placeholder |
| Image | [image.md](skills/arco-design/references/components/data-display/image.md) | Image display, preview, lazy load |
| Statistic | [statistic.md](skills/arco-design/references/components/data-display/statistic.md) | Numeric display, countdown |
| Timeline | [timeline.md](skills/arco-design/references/components/data-display/timeline.md) | Timelines, activity feeds |

### Feedback

| Component | File | Description |
|-----------|------|-------------|
| Modal | [modal.md](skills/arco-design/references/components/feedback/modal.md) | Modal dialogs, Modal.confirm(), useModal |
| Message | [message.md](skills/arco-design/references/components/feedback/message.md) | Global toast messages |
| Notification | [notification.md](skills/arco-design/references/components/feedback/notification.md) | Rich notification toasts |
| Drawer | [drawer.md](skills/arco-design/references/components/feedback/drawer.md) | Slide-out side panels |
| Alert | [alert.md](skills/arco-design/references/components/feedback/alert.md) | Inline alert banners |
| Progress | [progress.md](skills/arco-design/references/components/feedback/progress.md) | Linear/circular progress bars |
| Popconfirm | [popconfirm.md](skills/arco-design/references/components/feedback/popconfirm.md) | Confirmation popup |
| Result | [result.md](skills/arco-design/references/components/feedback/result.md) | Result pages (success/fail/404) |
| Skeleton | [skeleton.md](skills/arco-design/references/components/feedback/skeleton.md) | Loading skeleton placeholders |
| Spin | [spin.md](skills/arco-design/references/components/feedback/spin.md) | Loading spinners |

### Other

| Component | File | Description |
|-----------|------|-------------|
| BackTop | [back-top.md](skills/arco-design/references/components/other/back-top.md) | Scroll-to-top button |
| Portal | [portal.md](skills/arco-design/references/components/other/portal.md) | Render into different DOM node |
| ResizeBox | [resize-box.md](skills/arco-design/references/components/other/resize-box.md) | Resizable containers, split panes |
| Trigger | [trigger.md](skills/arco-design/references/components/other/trigger.md) | Base popup positioning |
| Watermark | [watermark.md](skills/arco-design/references/components/other/watermark.md) | Text/image watermarks |

### Patterns & Hooks

| Topic | File | Description |
|-------|------|-------------|
| Form Patterns | [form-patterns.md](skills/arco-design/references/patterns/form-patterns.md) | Dynamic forms, linked validation, async submit |
| Table Patterns | [table-patterns.md](skills/arco-design/references/patterns/table-patterns.md) | Remote data, editable rows, virtual scroll |
| Modal Patterns | [modal-patterns.md](skills/arco-design/references/patterns/modal-patterns.md) | Form-in-modal, confirmation flows, nested drawers |
| Controlled vs Uncontrolled | [controlled-uncontrolled.md](skills/arco-design/references/patterns/controlled-uncontrolled.md) | Choosing value+onChange vs defaultValue |
| Responsive Design | [responsive-design.md](skills/arco-design/references/patterns/responsive-design.md) | Grid breakpoints, adaptive layout |
| useVerificationCode | [use-verification-code.md](skills/arco-design/references/hooks/use-verification-code.md) | Custom OTP input hook |
| useWatermark | [use-watermark.md](skills/arco-design/references/hooks/use-watermark.md) | Dynamic canvas watermark hook |
