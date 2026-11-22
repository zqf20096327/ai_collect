# Retrieval Augmented Generation (RAG) Application using OpenAI and ElasticSearch as Vector DB

> **Status: a compact reference app.** First published in 2024 and refreshed in November 2026 for
> Elasticsearch 9 and version 3 of the OpenAI Python SDK. A follow-up for video,
> `youtube-timestamped-rag`, is planned at [Aryabhatta Labs](https://github.com/AryabhattaLabs).

RAG *(Retrieval-Augmented Generation)* Application to offer Q&A on a long format text using OpenAI and
ElasticSearch. Here we are

- using ElasticSearch as VectorDB to store indexed data and use it for Retrieval.
- using OpenAI to create embeddings and generate answers to the questions after retrieving relevant chuncks from ES.

## Getting Started

### Prerequisites:

1. Python 3.10 or above
2. pip
3. virtualenv
4. Elasticsearch 9.x (the steps below run it in Docker)
5. OpenAI API Key (https://platform.openai.com/)

### Installation Steps:

- Create and Activate virtual environment

```bash
python -m venv venv
```

```bash
source venv/bin/activate
```

- Install dependencies

```bash
pip install -r requirements.txt
```

- Download spacy model for NLP and splitting the text into sentences.

```bash
python -m spacy download en_core_web_sm
```

- Elasticsearch Setup. The simplest way to run it locally is Docker. This starts a single node on
  `localhost:9200` with the user `elastic` and the password `password`, which match `.env-template`.
  It is for local use only.

```bash
docker run -d --name es-rag -p 127.0.0.1:9200:9200 -m 2g \
  -e discovery.type=single-node \
  -e ELASTIC_PASSWORD=password \
  -e xpack.security.http.ssl.enabled=false \
  docker.elastic.co/elasticsearch/elasticsearch:9.5.6
```

  Test it by running `curl -u elastic:password "localhost:9200/"` in terminal. If you install Elasticsearch
  another way (https://www.elastic.co/downloads/elasticsearch), put its URL, user and password in `.env`.

### Run App

Before running app, create `.env` file using `.env-template` and add OpenAI API Key and Elasticsearch credentials.

The app uses `gpt-6-luna` for answers and `text-embedding-3-small` for embeddings. Model names change over
time: to use others, set `OPENAI_CHAT_MODEL` and `OPENAI_EMBEDDING_MODEL` in `.env`. If you change the embedding
model, recreate the index with that model's dimensions and retune `BEST_SCORE_THRESHOLD` in
`app/services/answering_service.py`.

If you indexed data with an earlier version of this app, which used `text-embedding-ada-002`, delete the index
and index the data again. Embeddings from different models cannot be compared.

```bash
python run.py
```

App will start on `localhost` on port `8081`. Sanity check by running in terminal. It should return `Hello` message.

```bash
curl -X GET "localhost:8081"
```

## To Index and Query Data

### 1. Create ES Index

```bash
curl -u elastic:password --location --request PUT 'http://localhost:9200/first-index' \
--header 'Content-Type: application/json' \
--data-raw '{
    "mappings": {
        "properties": {
            "text": {
                "type": "text"
            },
            "embedding": {
                "type": "dense_vector",
                "dims": 1536
            }
        }
    }
}'
```

If you want to delete the index for clean start, use the following command.

```bash
curl -u elastic:password --location --request DELETE 'http://localhost:9200/first-index'
```

### 2. Index Data

The repository includes a sample text to try: the Universal Declaration of Human Rights, in
`sample_data/universal_declaration_of_human_rights.txt`. Make sure you have the server running on `localhost`
on port `8081`, then index the file:

```bash
python index_file.py sample_data/universal_declaration_of_human_rights.txt first-index
```

The script reads the file and sends it to the app's `/api/index` endpoint. The app splits the text into
sentences, creates an embedding for each one and stores it in Elasticsearch. A sentence that is already
indexed is skipped, so you can run it again safely.

To index your own text, pass any UTF-8 text file to the script, or send the text directly:

```bash
curl --location --request POST 'localhost:8081/api/index' \
--header 'Content-Type: application/json' \
--data-raw '{
  "text": "Your text goes here. It can be as long as you like.",
  "index_name": "first-index"
}'
```

### 3. Query Data

Example 1:

```bash
curl --location --request POST 'localhost:8081/api/query' \
--header 'Content-Type: application/json' \
--data-raw '{
  "question": "Is elementary education free and compulsory?",
  "index_name": "first-index"
}'
```

Example 2:

```bash
curl --location --request POST 'localhost:8081/api/query' \
--header 'Content-Type: application/json' \
--data-raw '{
  "question": "Can someone be stopped from changing their nationality?",
  "index_name": "first-index"
}'
```

## Sample data

`sample_data/universal_declaration_of_human_rights.txt` is the English text of the Universal Declaration of
Human Rights, adopted by the United Nations General Assembly on 10 December 1948 as resolution 217 A (III).
The text is taken from https://www.un.org/en/about-us/universal-declaration-of-human-rights.

## License

MIT. See [LICENSE](LICENSE).

#### Built by Ajeet with ☕️ and ❤️
