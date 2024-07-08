#!/bin/zsh

# Create a Docker Buildx context
docker context create buildx-context

# Use the created context with Buildx
docker buildx use buildx-context

# docker context use buildx-context

# # Initialize the Buildx builder
# docker buildx init