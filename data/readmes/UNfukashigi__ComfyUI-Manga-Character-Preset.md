# ComfyUI Manga Character Preset

A custom node for switching between character prompts and up to three LoRAs with a single selection. Designed for manga and other projects with recurring characters.

漫画など、同じキャラクターを繰り返し生成するためのComfyUIカスタムノードです。キャラクターを選ぶだけでプロンプトとLoRA設定をまとめて切り替えられます。

## Features / 機能

- Character presets with positive and negative prompts.
- Up to three LoRAs per character, with independent model and CLIP strengths and ON/OFF toggles.
- Add and delete characters; edits automatically update the selected preset.
- Twelve one-click prompt shortcuts with hover tooltips.
- Presets are stored in the workflow, not shared across workflows.
- No additional Python dependencies.

## Installation / インストール

1. Download the repository as a ZIP and extract it.
2. Place the extracted folder directly inside `ComfyUI/custom_nodes/`.
3. Restart ComfyUI and refresh the browser.

ZIPを解凍し、`__init__.py` と `web/` が入っているフォルダを `ComfyUI/custom_nodes/` に配置してください。ComfyUIを再起動し、ブラウザを再読み込みします。

## Usage / 使い方

1. Add `Character Preset (Prompt + 3 LoRAs)` from the `Anima` category.
2. Connect the base MODEL and CLIP inputs from your model loaders.
3. Fill in the positive and negative prompts and select up to three compatible LoRAs. Select `None` for unused slots, or use the individual ON/OFF toggles to temporarily disable a LoRA without changing its filename or strengths.
4. Click **Add character (copy current)** and enter a name.
5. Change characters using the **Character** dropdown. Changes to prompts and LoRA settings update the selected preset automatically.
6. Connect the MODEL, positive and negative conditioning outputs to your sampler. Save the workflow to keep the presets for future sessions.

登録するにはプロンプトとLoRAを設定してから **Add character (copy current)** を押します。キャラクター切替後も編集内容が保持されます。**Delete character** で選択中のプリセットを削除できます。

The Japanese prompt shortcut buttons append their full prompt text to the positive prompt. Hover over a button to see the text before inserting it.

LoRAは個別にON/OFF切り替えできます。OFFにしてもファイル名・強度は保持され、キャラごとに状態が保存されます。

## Sample workflow / サンプルワークフロー

Open [`example_workflows/ANIMA_basic.json`](example_workflows/ANIMA_basic.json) in ComfyUI. It uses only this custom node and built-in nodes, with two generic character presets and no LoRAs.

サンプルをComfyUIで開くと、ANIMAの基本設定ですぐに生成を試せます。キャラクター2種類の切り替えも試せます。

Download the required files from the [official ANIMA model repository](https://huggingface.co/circlestone-labs/Anima) and place them in these folders:

| File | Directory |
| --- | --- |
| `anima-base-v1.0.safetensors` | `ComfyUI/models/diffusion_models/` |
| `qwen_3_06b_base.safetensors` | `ComfyUI/models/text_encoders/` |
| `qwen_image_vae.safetensors` | `ComfyUI/models/vae/` |

Sample settings: 896 × 1152, 32 steps, CFG 4.5, `er_sde`, `normal` scheduler. The model files are not included in this repository.

## Notes / 注意事項

- Use LoRAs compatible with your chosen base model and text encoder. Model weights and LoRAs are not included.
- Presets are embedded in the workflow JSON. Sharing a saved workflow may also share the character prompts and LoRA filenames recorded in it.
- Copying a node between workflows copies its presets; the two copies are independent.
- This node uses ComfyUI's built-in LoRA loading and text encoding nodes. A recent ComfyUI frontend is recommended.
