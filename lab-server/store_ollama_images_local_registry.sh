#!/bin/bash
# docker run -d -p 5000:5000 --restart always --name registry registry:2

models=(
    "qwen2.5:1.5b"
)

for MODEL in "${models[@]}"; do
    ollama pull --insecure http://localhost:9200/library/$MODEL

done

