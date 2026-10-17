# lazyllama

Local models management utility - discovers and lists models from HuggingFace, Ollama, and LM Studio.

![alt text](https://raw.githubusercontent.com/ctx-0/lazyllama/refs/heads/main/image.png)


## Installation

```sh
pip install lazyllama
```


## Usage

### CLI Commands

#### Basic Usage
```sh
# Default simple overview
lazyllama

# Different display modes
lazyllama --mode simple     # Compact overview (default)
lazyllama --mode detailed   # Show filenames and comprehensive info
lazyllama --mode tree       # Hierarchical tree view

# Output only specific information
lazyllama --dirs            # Print model directories only
lazyllama --list            # Tab-separated list (name, source, size, path)
lazyllama --summary         # Show only summary statistics
lazyllama --json            # Output raw scanned data as JSON
lazyllama --raw             # Output raw scanned data in plain format
```


#### Custom Directories
```sh
# Include a custom scan directory for the current command
lazyllama --add-dir lmstudio /path/to/custom/models
lazyllama --add-dir huggingface /custom/hf/cache
```

#### Raw Data Output
```sh
# JSON format - structured data for programmatic use
lazyllama --json > models.json

# Plain text format - human-readable raw data
lazyllama --raw > models.txt
```

The `--json` flag outputs complete model information in structured JSON format including:
- Model metadata (name, source, size, file count, etc.)
- File details (path, size, format, type, quantization, etc.)
- Timestamps and cache information
- All discovered model attributes

The `--raw` flag outputs the same comprehensive data in a plain text format that's easier to read and parse manually.

### Complete Command Reference

```
lazyllama [OPTIONS]

Options:
  -h, --help                Show help message
  -m, --mode MODE           Display mode: simple, detailed, tree (default: simple)
  --add-dir CACHE DIR       Add custom directory to model cache
  --dirs                    Print model directories only
  --list                    Tab-separated list output
  --summary                 Show only summary statistics
  --json                    Output raw scanned data as JSON
  --raw                     Output raw scanned data in plain format
  --debug                   Show debug info (cache dirs, scan timing)

Examples:
  lazyllama                              # Simple overview
  lazyllama --mode detailed              # Detailed view with filenames
  lazyllama --mode tree                  # Full hierarchical tree
  lazyllama --summary                    # Summary statistics only
  lazyllama --json                       # Raw data as JSON
  lazyllama --raw                        # Raw data in plain format
  lazyllama --debug                      # Debug info only
  lazyllama --debug --list               # Debug + parsable output
  lazyllama --add-dir lmstudio /my/path  # Add custom directory
```
