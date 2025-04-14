#!/bin/bash
# Ensure you local ollama model folder is removed so that every layers get pulled !
# rm -rf ~/.cache/ollama/models

models=(
    "gemma3:12b"
    "gemma3:4b"
    "mistral:7b"
    "phi4:14b"
    "qwen2.5:14b"
    "qwen2.5:7b"
    "qwen2.5:3b"
    "nomic-embed-text:latest"
    "qwen2.5:1.5b"
)

for MODEL in "${models[@]}"; do
    echo "Pulling model $MODEL from local registry..."
    ollama pull --insecure http://localhost:9200/library/$MODEL
done

