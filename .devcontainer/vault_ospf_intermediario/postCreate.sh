#!/usr/bin/env bash

set +e

#pip install eos-downloader
#ardl --token ${ARTOKEN} get eos --version ${ANO_ARISTA_ROUTER_VERSION} --format cEOS --import-docker --docker-tag latest

# Set the VPN CodeSpaces DNS based on the codespace name
# CODESPACE_NAME is created by the codespaces by default
echo 'export TF_VAR_VPN_CODESPACES_2222="https://$CODESPACE_NAME-2222.app.github.dev/docs"' >> ~/.bashrc
echo 'export TF_VAR_VPN_CODESPACES_IP=$(curl -s ifconfig.me)' >> ~/.bashrc

echo 'export TF_VAR_VPN_CODESPACES_2222="https://$CODESPACE_NAME-2222.app.github.dev/docs"'
echo 'export TF_VAR_VPN_CODESPACES_IP=$(curl -s ifconfig.me)'
