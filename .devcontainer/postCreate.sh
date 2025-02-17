#!/usr/bin/env bash

set +e

pip install eos-downloader
ardl get eos --image-type cEOS --version ${CEOS_LAB_VERSION} --import-docker
docker tag arista/ceos:${CEOS_LAB_VERSION} ceos:latest

# Set the VPN CodeSpaces DNS based on the codespace name
# CODESPACE_NAME is created by the codespaces by default
echo 'export TF_VAR_VPN_CODESPACES_2222="https://$CODESPACE_NAME-2222.app.github.dev"' >> ~/.bashrc
echo 'export TF_VAR_VPN_CODESPACES_IP=$(curl -s ifconfig.me)' >> ~/.bashrc
