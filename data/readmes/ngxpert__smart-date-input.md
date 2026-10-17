# Smart Date Input

A smart date input directive that uses the Writer API to parse natural language dates.

## Pre-requisites

Works only on Chrome. You need to enable the Writer API.

1. [For localhost](https://developer.chrome.com/docs/ai/writer-api#add_support_to_localhost)
2. [For origin trial](https://developer.chrome.com/docs/ai/writer-api#origin-trial.)

## Getting Started

### Step 1: Build the library

```bash
ng build @ngxpert/smart-date-input
```

### Step 2: Run the application

```bash
ng serve
```

## Usage

For single date input:

```html
<input
  type="text"
  smartDateInput
  (smartDateInputResponseReceived)="onResponseReceivedForSingleDate($event)"
/>
```

For date range input:

```html
<input
  type="text"
  smartDateInput
  [smartDateInputIsRange]="true"
  (smartDateInputResponseReceived)="onResponseReceivedForDateRange($event)"
/>
```

Checkout [src/app/app.html](src/app/app.html) for more details.
