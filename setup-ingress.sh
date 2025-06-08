#!/bin/bash

# Add the ingress-nginx Helm repository
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx

# Update the Helm repository
helm repo update

# Install the ingress-nginx Helm chart
helm install ingress-nginx ingress-nginx/ingress-nginx --namespace ingress-nginx --create-namespace