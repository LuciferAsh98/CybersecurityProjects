#!/bin/bash

# Function to check if a command exists
check_command() {
    if ! command -v "$1" &> /dev/null; then
        echo "$1 is not installed. Installing..."
        return 1
    else
        echo "$1 is already installed."
        return 0
    fi
}

# Install Terraform
check_command terraform || {
    sudo apt-get update
    sudo apt-get install -y terraform
}

# Install Azure CLI
check_command az || {
    echo "Installing Azure CLI..."
    curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
}

# Login to Azure
echo "Logging in to Azure..."
az login

# Initialize Terraform
echo "Initializing Terraform..."
cd ../terraform
terraform init

echo "Setup complete. You can now apply the Terraform configuration."