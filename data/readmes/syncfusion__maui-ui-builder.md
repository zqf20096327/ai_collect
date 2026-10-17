# Syncfusion MAUI UI Builder

**Syncfusion MAUI UI Builder** is an AI-powered agent skill that transforms your UI requirements into production-ready .NET MAUI components. It leverages Syncfusion's comprehensive MAUI control library to generate accessible, responsive, and multi-platform user interfaces for iOS, Android, Windows, and macOS.

### Key Features

- **AI Agent Orchestration**: Intelligent workflow handling design thinking, component selection, code generation, and validation
- **Syncfusion MAUI Integration**: Access to professional MAUI UI controls with native platform support
- **WCAG 2.1 AA Accessibility**: Built-in accessibility compliance with semantic controls and automation IDs
- **Responsive Design**: Mobile-first layouts with adaptive breakpoints and OnPlatform styling
- **Multi-Platform Support**: Single codebase generates UI for iOS 14+, Android 10+, macOS 11+, Windows 10+
- **Design System Support**: MAUI ResourceDictionary with Material/Cupertino theming and Syncfusion theme alignment
- **C# & MVVM Support**: Full MVVM pattern with INotifyPropertyChanged, ObservableCollections, and strong typing

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Troubleshooting](#support)

## Prerequisites

Before using MAUI UI Builder, ensure your environment meets these requirements:

| Requirement | Description |
|-------------|-------------|
| **APM** | [Install APM](https://microsoft.github.io/apm/getting-started/installation/) - Agent Package Manager for skill installation |
| **.NET MAUI Project** | Active .NET MAUI 9.0+ project with multi-platform targets (iOS, Android, Windows, macOS) |
| **.NET SDK 9.0+** | .NET 9.0 or .NET 10.0+ SDK installed |
| **Visual Studio 2022** | v17.8+ with MAUI workload, or VS Code with C# DevKit |
| **Syncfusion License** | [Commercial](https://www.syncfusion.com/sales/unlimitedlicense), [Free Community](https://www.syncfusion.com/products/communitylicense), or [Free Trial](https://www.syncfusion.com/account/manage-trials/start-trials) |

## Installation

```bash
# Install for GitHub Copilot
apm install syncfusion/maui-ui-builder -t copilot

# Install for Claude Code
apm install syncfusion/maui-ui-builder -t claude

# Install for Cursor
apm install syncfusion/maui-ui-builder -t cursor

```

## How It Works

The MAUI UI Builder uses an **8-stage AI orchestration workflow** that transforms your requirements into production-ready multi-platform components.

| Stage | Name | User Interaction | Description |
|-------|------|------------------|-------------|
| 1 | Intent Analysis | None | Parse query, identify component type and features |
| 2 | Project Detection | None | Auto-detect .NET version, target platforms, MVVM pattern |
| 3 | Component Mapping | ⭐ Confirm | Select 3+ Syncfusion MAUI controls |
| 4 | Theming & Design System | ⭐ Confirm | Lock design system (ResourceDictionary, theme, colors, spacing) |
| 5 | Code Generation | None | Generate .xaml, .xaml.cs, ViewModel.cs with MVVM |
| 6 | Validation | ⭐ Confirm | WCAG 2.1 AA + Syncfusion integration + security |
| 7 | Dependencies | None | Detect and install Syncfusion NuGet packages |
| 8 | Code Insertion | None | Insert files into project and verify build |

## Usage

Choose the `syncfusion-maui-ui-builder` agent in the AI chat panel and invoke the skill through your AI assistant by describing what you want to build:

```
Create a Customer Management Dashboard UI for a MAUI app with a header showing the app title and a profile icon, a navigation drawer on the left with menu items (Dashboard, Customers, Orders, Reports, Settings), a main content area with three metric cards showing Total Customers, Active Orders, and Revenue (with icons and change percentages), a searchable customer data grid with columns for Name, Email, Phone, Status, and Actions (edit/delete buttons), and a footer with pagination. The UI should be responsive on mobile (320pt), tablet (768pt), and desktop (1024pt+) with dark mode support using Material theme.
```

Generated code follows best practices with accessible semantic controls, responsive multi-platform layouts, full MVVM pattern with data binding, and built-in security measures such as input validation and proper null handling.

## Generated Output

The skill generates production-ready files for your MAUI project:

```
Views/
  ├── YourComponent.xaml          # MAUI view with Syncfusion control declarations
  └── YourComponent.xaml.cs       # Code-behind with event handlers
ViewModels/
  └── YourComponentViewModel.cs   # MVVM ViewModel with INotifyPropertyChanged
Resources/
  └── Colors.xaml                 # Design tokens and theming resources
```

All generated code:
- ✅ Works on iOS, Android, Windows, and macOS simultaneously
- ✅ Includes WCAG 2.1 AA accessibility features
- ✅ Follows MVVM pattern with proper data binding
- ✅ Uses Syncfusion MAUI controls for consistent design
- ✅ Responsive layouts that adapt to screen sizes
- ✅ Properly typed C# with nullable reference types

## Support

Product support is available through the following media.

- [Support ticket](https://support.syncfusion.com/support/tickets/create) - Guaranteed response in 24 hours | Unlimited tickets | Holiday support
- [Community forum](https://www.syncfusion.com/forums/maui)
- [Request feature or report bug](https://www.syncfusion.com/feedback/maui)
- [Live chat](https://www.syncfusion.com/support)
- [Syncfusion MAUI Documentation](https://help.syncfusion.com/maui/introduction/overview)