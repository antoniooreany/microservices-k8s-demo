## Setting Up Ingress Controller

To automate the setup of the NGINX Ingress Controller for this project, you can use the provided shell script.

### Steps to Set Up

1. **Create the Setup Script**  
   A shell script named `setup-ingress.sh` is included in the project. It contains the following commands:

   ```bash
   #!/bin/bash

   # Add the ingress-nginx Helm repository
   helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx

   # Update the Helm repository
   helm repo update

   # Install the ingress-nginx Helm chart
   helm install ingress-nginx ingress-nginx/ingress-nginx --namespace ingress-nginx --create-namespace