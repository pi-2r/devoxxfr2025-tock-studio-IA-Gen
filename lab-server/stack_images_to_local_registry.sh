#!/bin/bash
# docker run -d -p 5000:5000 --restart always --name registry registry:2

images=(
    "mongo:7.0.9"
    "tock/build_worker:24.9.3"
    "tock/duckling:24.9.3"
    "tock/kotlin_compiler:24.9.3"
    "tock/bot_admin:24.9.3"
    "tock/nlp_api:24.9.3"
    "tock/bot_api:24.9.3"
    "pgvector/pgvector:pg16"
    "tock/gen-ai-orchestrator-server:24.9.3"
    "langfuse/langfuse:2.84"
    "tock/llm-indexing-tools:24.9.3"
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

