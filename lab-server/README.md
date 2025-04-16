# Lab server

Ce dossier contiens des indication sur le montage du serveur du lab contenant :
- Registry Docker
- Serveur d'inférence Ollama avec proxy de registry ollama
- Stack Tock complète avec 60+ comptes

Ces différents serveur sont à utilisé pour les participants qui n'arrivent pas à le faire tourner en local.

## Checklist avant lab

- [ ] Bien configuré l'IP gpu-server.lan `192.168.20.2` pour pointer vers la machine servant de serveur ollama
- [ ] Bien configuré l'IP tock.lan `192.168.20.3` pour pointer vers la machine servant de stack TOCK, s'il s'agit de la même machine bien mettre à jour la config host dans [step_1.md](../step_1.md)
- [ ] Pull les images sur la registry docker local.
- [ ] Pull les modèle ollama sur la registry local / proxy ollama.
- [ ] Initier un fichier Google Sheet pour que les gens puissent choisir les identifiants sur la stack tock de backup.

## MacOS - Collima augmenter la RAM et nb CPU

Editer :
```
nano ~/.colima/default/colima.yaml 
```

Changer :
```
cpu: 4
# [...]
memory: 9
```

Puis relancer collima 
```
colima stop
colima start
```

## Lancer la stack tock de backup

```bash
cp template.env .env
source .env
docker compose -p devoxx_lab_server -f docker-compose-tock-registry-reranker.yml up -d
```

## Registry local

Elle est lancé par le docker compose il faut penser à y push les images dedans avant via :
```bash
# Attention bien rm -rf ~/.ollama/models avant
./stack_images_to_local_registry.sh
```

## Serveur de reranking

Possible d'utiliser l'image docker pour une machine avec GPU Nvidia, voir registry ici :

Sinon sur Mac avec GPU MPS pas faisable en dokerisé à date (et via une install docker collima), voici les inscriptions pour installer et faire tourner le projet en dehors de docker (pré-requis [uv]()).

```bash
git clone https://github.com:CreditMutuelArkea/llm-inference.git
cd llm-inference
uv venv --python 3.10
source .venv/bin/activate
poetry install
echo 'export HUGGING_FACE_HUB_TOKEN="<YOUR HF HUB TOKEN>"' > .env
source .env
python -m llm_inference --task SCORING --port 8082 --model cmarkea/bloomz-560m-reranking
```
## Dataset file

Go to  [Séries TV](https://www.kaggle.com/datasets/asaniczka/full-tmdb-tv-shows-dataset-2023-150k-shows)
to download TMDB_tv_dataset_v3.csv place it into data/document_csv/TMDB_tv_dataset_v3.csv.

## Pré-ingérer les docs pour tous les comptes

C'est une reprise un peu "sale" du script d'ingestion mais bon it works.

```bash
docker run --name tooling_tock --rm -it \
    -v "$(pwd)/index_documents_for_all_accounts.py":/app/tock-llm-indexing-tools/index_documents_for_all_accounts.py \
    -v "$(pwd)/data/lab_accounts/":/data/lab_accounts \
    -v "$(pwd)/../data":/app/data \
    -e NO_PROXY="host.docker.internal,ollama-server,postgres-db,localhost" \
    -e no_proxy="host.docker.internal,ollama-server,postgres-db,localhost" \
    --add-host=ollama-server:$OLLAMA_SERVER \
    --add-host=postgres-db:$POSTGRES_DB_SERVER \
    "${PLATFORM}tock/llm-indexing-tools:${TAG}" \
    /bin/bash
```

Then :
```bash
export EMBEDDING_JSON_CONFIGURATION=/app/data/configurations/embeddings_ollama_settings.json
python tock-llm-indexing-tools/index_documents_for_all_accounts.py \
       --input-csv=data/documents_csv/filtered_tv_series.csv \
       --account-csv=/data/lab_accounts/Reordered_Indiana_Jones_Accounts.csv \
       --output-account-csv=/data/lab_accounts/accounts_with_sessions_uuid.csv \
       --embeddings-json-config=$EMBEDDING_JSON_CONFIGURATION \
       --vector-store-json-config=data/configurations/vector_store_pgvector_settings.json \
       --chunks-size=5000 -v
```

This will generate an output CSV with all indexing sessions UUIDs that you need to import to Google Drive / On Google Sheet.
