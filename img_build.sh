#!/bin/zsh

# Helper function to build and push the Docker image
build_and_push_image() {
    local imageName="$1"
    local imageVersion="$2"
    local imageArch="$3"

    # Build the Docker image with the specified architecture
    docker buildx build \
        --platform "linux/$imageArch" \
        -t "${imageName}:${imageVersion}-${imageArch}" \
        . --load

    # Save the Docker image to a tar file
    docker save -o "images/${imageVersion}-${imageArch}.tar" "${imageName}:${imageVersion}-${imageArch}"

    # Push the Docker image to the registry
    docker push "${imageName}:${imageVersion}-${imageArch}"
}

# Define the version variable for the Docker image
version="0.0.1"

# Build the Docker image for amd64 architecture
arch="amd64"
build_and_push_image "ztxtechnology/shuishui" "$version" "$arch"

# Build the Docker image for arm64 architecture
# arch="arm64"
# build_and_push_image "ztxtechnology/shuishui" "$version" "$arch"


