#!/bin/bash
# docker run -d -p 5000:5000 --restart always --name registry registry:2

images=(
    "mongo:8.0.6"
    "tock/build_worker:25.3.1"
    "tock/duckling:25.3.1"
    "tock/kotlin_compiler:25.3.1"
    "tock/bot_admin:25.3.1"
    "tock/nlp_api:25.3.1"
    "tock/bot_api:25.3.1"
    "pgvector/pgvector:pg17"
    "tock/gen-ai-orchestrator-server:25.3.1"
    "langfuse/langfuse:2.95.8"
    "tock/llm-indexing-tools:25.3.1"
)

platforms=("linux/arm64" "linux/amd64")

for IMAGE in "${images[@]}"; do
    for PLATFORM in "${platforms[@]}"; do
        ARCH_TAG="${PLATFORM##*/}"  # Extract "arm64" or "amd64" from platform string
        IMAGE_NAME="$(echo "$IMAGE" | cut -d':' -f1)"
        IMAGE_TAG="$(echo "$IMAGE" | cut -d':' -f2)"
        LOCAL_TAG="localhost:5000/${IMAGE_NAME}:${IMAGE_TAG}-${ARCH_TAG}"

        echo "Pulling $IMAGE for platform $PLATFORM..."
        docker pull --platform "$PLATFORM" "$IMAGE"

        echo "Tagging $IMAGE as $LOCAL_TAG..."
        docker tag "$IMAGE" "$LOCAL_TAG"

        echo "Pushing $LOCAL_TAG..."
        docker push "$LOCAL_TAG"
    done
done

