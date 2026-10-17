# Virtual Neuroendocrine AI

A computational experiment that connects a **dynamic neuroendocrine simulation** to a large language model.

The idea is simple:

The project models hormones and neurotransmitters as interacting dynamic systems, converts their combined state into higher-level behavioral variables, and uses those variables to influence a Gemini-powered language model.

---

## How it works

```text
                    USER INPUT
                        │
                        ▼
                    ┌────────┐
                    │ Parser │
                    └────┬───┘
                         │
                         ▼
               Physiological stimuli
                         │
                         ▼
              ┌────────────────────┐
              │ Endocrine System   │
              │                    │
              │ Hormone models     │
              │ Feedback loops     │
              │ Interactions       │
              │ Homeostasis        │
              └─────────┬──────────┘
                        │
                        ▼
              Neuroendocrine state
                        │
                        ▼
              ┌───────────────────┐
              │ Behavioral state  │
              │                   │
              │ Arousal           │
              │ Threat sensitivity│
              │ Reward sensitivity│
              │ Attention         │
              │ Social affiliation│
              │ Impulse control   │
              │ Flexibility       │
              │ Persistence       │
              └─────────┬─────────┘
                        │
                        ▼
                 Gemini controller
                        │
                        ▼
                     RESPONSE
```

The important part is that the LLM does not directly receive a label such as `mood = happy`.

Instead, the simulated physiological state produces several interacting control signals that influence generation.

---

### `endocrine/`

Contains the simulated biological system.

### `endocrine/hormones/`

Contains the individual mathematical models.

### `endocrine/behavior.py`

Converts the simulated neuroendocrine state into computational behavioral dimensions.

### `llm/`

The interface between the simulated system and **Google Gemini**.

It is responsible for:

1. Building the system prompt from the current behavioral state.
2. Translating behavioral state into generation parameters.
3. Sending the request to Gemini.
4. Returning Gemini's response.

### `tests/`

Tests the individual models and the system as a whole.

Every implemented hormone/neurotransmitter model has its own test module.

---

## Gemini integration

The project uses Google's Gemini API.

Create a `.env` file containing:

```env
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-3.6-flash
```

Run

```bash
python main.py
```
---

## License

This project is licensed under the MIT License.
