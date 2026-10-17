# Medplum AI Concierge

<img width="3824" height="1758" alt="Screenshot from 2026-03-03 16-18-14" src="https://github.com/user-attachments/assets/ee8cb590-0ad8-4177-b227-72ba7fbb406c" />

Demo of a healthcare dashboard with AI-powered graph and report generation using [CopilotKit](https://www.copilotkit.ai/) and [Medplum](https://www.medplum.com/).

The patient can chat with an AI agent and analyze their health records. The AI agent can generate graphs to display the patient's health data dynamically and provide insights. Current version focuses on weight-loss and diabetes care.

This application demonstrates the usage of Generative UI techniques for healthcare dashboards, specifically with the [Agent–User Interaction (AG-UI) Protocol with CopilotKit](https://docs.ag-ui.com/introduction).


## Architecture

This project uses a monorepo structure with two main applications:

- **apps/web/** - Next.js frontend application with CopilotKit integration
- **apps/agent/** - LangGraph backend agent for AI orchestration

### Technology Stack

- **Frontend**: Next.js, React, Mantine UI, CopilotKit
- **Backend Agent**: LangGraph, LangChain, OpenAI
- **System of Record**: Medplum
- **Build**: pnpm workspaces, Turbo

## Getting Started

### Prerequisites

- Node.js 22.18+ or 24.12+
- pnpm 9.15.0+
- Configured Medplum project (see steps below)
- reCAPTCHA site key (for patient registration)
- OpenAI API key

### Medplum Project setup

Create a new Medplum project at https://app.medplum.com/register.

Get your Medplum project ID from the app.medplum.com [Project page](https://app.medplum.com/admin/project). Keep the project ID at hand to set it as an environment variable.

### Create a patient default access policy

1. Go to [app.medplum.com New AccessPolicy page, JSON tab](https://app.medplum.com/AccessPolicy/new/json)
2. Paste the contents from [patient-access-policy.json](patient-access-policy.json)
3. Click "OK"

### Set up open patient registration

To allow patients to self-register, set the patient access policy as the default.

1. Navigate to [app.medplum.com Project page](https://app.medplum.com/Project) and select your project.
2. In the "Edit" tab, set the "Default Patient Access Policy" field to your patient access policy and click "Update".

For more details, see the [Open Patient Registration documentation](https://www.medplum.com/docs/user-management/open-patient-registration).

### Set up reCAPTCHA

A reCAPTCHA configuration is required for the registration form to work.

1. Create a new reCAPTCHA configuration to get the site key and secret key at [google.com/recaptcha/admin/create](https://www.google.com/recaptcha/admin/create).
2. Go to [app.medplum.com](https://app.medplum.com), go to Project, then Sites. Create a Site with domains `localhost` and `127.0.0.1` and set the reCAPTCHA site key and secret key.

### OpenAI API key setup

Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys).

### Install Dependencies

```bash
pnpm install
```

### Configure Environment Variables

Copy `.env.example` to `.env.local` and configure:

```env
# Medplum Configuration
NEXT_PUBLIC_MEDPLUM_BASE_URL=https://api.medplum.com
NEXT_PUBLIC_MEDPLUM_PROJECT_ID=<your-medplum-project-id>
NEXT_PUBLIC_MEDPLUM_RECAPTCHA_SITE_KEY=<your-recaptcha-site-key>

# LangGraph Agent Configuration
LANGGRAPH_DEPLOYMENT_URL=http://localhost:8123
LANGSMITH_API_KEY=

# OpenAI Configuration
OPENAI_API_KEY=<your-openai-api-key>
OPENAI_MODEL=gpt-5-mini
```

Copy the `.env.local` to both apps:

```bash
cp .env.local apps/web/.env.local
cp .env.local apps/agent/.env
```

### Run Development Servers

**Option 1: Run all services with Turbo (recommended)**

```bash
pnpm dev
```

This starts both the LangGraph agent (port 8123) and Next.js web app (port 3000) in parallel.

**Option 2: Run services separately**

Terminal 1 - Start the LangGraph agent:
```bash
cd apps/agent
pnpm dev
```

Terminal 2 - Start the Next.js web app:
```bash
cd apps/web
pnpm dev
```

### Access the Application

- **Web Application**: http://localhost:3000
- **LangGraph API**: http://localhost:8123
- **LangSmith Studio**: https://smith.langchain.com/studio?baseUrl=http://localhost:8123

## Usage

### Patient Sign-up and Sign-in

1. **New users**: Click "Register here" to create a new patient account
2. **Existing users**: Sign in as a Patient user

### Load Sample Data

1. After signing in, click the "Load Sample Data" button to load sample data for the patient.
2. The AI assistant will then be able to generate widgets based on the sample data.

### Widget Queries

The AI assistant generates widgets dynamically based on natural language queries. Try these:

- My blood pressure, 6 months
- Show my glucose levels over the past year
- Show my waist circumference over the past year
- Display my cholesterol
- Show my kidney function results
- My glycated hemoglobin trends

### Available Widgets

The assistant can generate the following widgets:

| Widget Name | Action Name | Description |
|------------|-------------|-------------|
| **Vitals Chart - Blood Pressure** | `show_vitals_chart` | Display patient blood pressure with charts showing trends over time |
| **Vitals Chart - Heart Rate** | `show_vitals_chart` | Display patient heart rate with charts showing trends over time |
| **Vitals Chart - Weight** | `show_vitals_chart` | Display patient weight with charts showing trends over time |
| **Vitals Chart - BMI** | `show_vitals_chart` | Display patient BMI with charts showing trends over time |
| **Vitals Chart - Waist Circumference** | `show_vitals_chart` | Display patient waist circumference trends (better IR predictor than BMI) |
| **Vitals Chart - Temperature** | `show_vitals_chart` | Display patient temperature with charts showing trends over time |
| **Lab Results - Glucose** | `show_lab_results` | Display patient glucose levels with charts showing trends over time. Shows latest reading with normal/high status badges |
| **Lab Results - HbA1c** | `show_lab_results` | Display patient HbA1c (glycated hemoglobin) levels with charts. Shows latest reading with normal/high status badges |
| **Lab Results - Cholesterol** | `show_lab_results` | Display both Total Cholesterol and LDL together with dual-line charts. Shows latest readings for both values with status badges |
| **Lab Results - HDL** | `show_lab_results` | Display patient HDL levels with charts. Shows latest reading with normal/low status badges |
| **Lab Results - Triglycerides** | `show_lab_results` | Display patient triglyceride levels with charts. Shows latest reading with normal/high status badges |
| **Lab Results - eGFR** | `show_lab_results` | Display patient eGFR (estimated glomerular filtration rate, kidney function) with charts. Shows latest reading with normal/low status badges and Metformin safety indicator (Safe/Caution/Contraindicated) |
| **Lab Results - Fasting Insulin** | `show_lab_results` | Display patient fasting insulin levels with charts. Shows latest reading with normal/high/low status badges |
| **FHIR Search** | `render_fhir_data_table` | Search FHIR resources with structured filters, sorting, and pagination. Supports all FHIR resource types (Observation, Condition, MedicationRequest, etc.) |

All widgets can be updated or removed after creation using the corresponding update/remove actions.

### Interpret Data Feature

Once the patient has widgets displayed on their dashboard, they can click the **"Interpret Data"** button to get AI-powered insights.

The AI analyzes all visible widget data and presents the interpretation in the chat sidebar. This helps the patient prepare for doctor appointments and understand their health data better.

### Care Plans Page

The Care Plans page is accessible from the header and displays the patient's care plans with their activities, goals, timeline, and progress notes. The page exposes care plan data to the AI assistant via CopilotKit, so the patient can ask questions about their care plans in the chat.

### Medications Page

The Medications page is accessible from the header and allows the patient to view their medications and ask questions about them using the AI assistant.

## Project Structure

```
medplum-ai-concierge/
├── apps/
│   ├── agent/                 # LangGraph backend agent
│   │   ├── src/
│   │   │   ├── agent.ts       # Main agent graph definition
│   │   │   └── index.ts       # Agent exports
│   │   ├── langgraph.json     # LangGraph configuration
│   │   ├── package.json       # Agent dependencies
│   │   └── tsconfig.json      # TypeScript config
│   └── web/                   # Next.js frontend
│       ├── src/
│       │   ├── app/           # Next.js app router
│       │   ├── components/    # React components
│       │   ├── context/       # Dashboard state context
│       │   ├── constants/     # LOINC codes and constants
│       │   ├── fixtures/      # Sample FHIR data
│       │   ├── hooks/         # Custom hooks (incl. widget actions)
│       │   └── utils/         # Utility functions
│       ├── package.json       # Web app dependencies
│       └── next.config.mjs    # Next.js configuration
├── package.json               # Root workspace configuration
├── pnpm-workspace.yaml        # pnpm workspace definition
├── turbo.json                 # Turbo build orchestration
└── .env.local                 # Environment variables (gitignored)
```

## Development Workflow

### Adding New Widgets

1. Define widget types in `apps/web/src/types/widgets.ts`
2. Add widget actions in `apps/web/src/hooks/useCopilotWidgets.tsx`
3. Create widget component in `apps/web/src/components/widgets/`
4. Update widget renderer in `apps/web/src/components/Dashboard.tsx`
5. Add test cases for the new widget

### Extending the Agent

1. Add backend tools in `apps/agent/src/agent.ts` (tools array)
2. Update system message for new capabilities
3. The agent automatically receives frontend tools via CopilotKit

### Testing

```bash
# Run all tests
pnpm test

# Run tests for specific workspace
cd apps/web
pnpm test
```

### Linting

```bash
# Lint all workspaces
pnpm lint

# Lint and fix
pnpm lint:fix
```

## Key Integrations

### CopilotKit + LangGraph
- Frontend tools (`useCopilotAction`) are automatically available to the agent
- Agent receives frontend tools via `CopilotKitStateAnnotation`
- Tool execution happens client-side for UI operations
- Backend tools can be added for server-side operations

### Medplum FHIR
- Patient data stored in FHIR format

## License

Apache 2.0 - See [LICENSE.txt](LICENSE.txt) for details

## Resources

- **Medplum Documentation**: [docs.medplum.com](https://www.medplum.com/docs/)
- **CopilotKit Documentation**: [docs.copilotkit.ai](https://docs.copilotkit.ai/)
- **OpenAI Platform**: [platform.openai.com](https://platform.openai.com/)
- **Medplum Discord**: [discord.gg/medplum](https://discord.gg/medplum)

**Need Help?** Please feel free to create an issue!

## Commercial Support

[![alt text](https://avatars2.githubusercontent.com/u/5529080?s=80&v=4 "Vinta Logo")](https://www.vinta.com.br/)

This project is maintained by [Vinta Software](https://www.vinta.com.br/). We offer design and development services for healthcare companies. If you need any commercial support, feel free to get in touch: contact@vinta.com.br
