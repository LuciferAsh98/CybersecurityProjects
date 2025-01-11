# Configure Azure provider
provider "azurerm" {
  features {}
}

# Create a resource group
resource "azurerm_resource_group" "example" {
  name     = var.resource_group_name
  location = var.location
}

# Create a storage account
resource "azurerm_storage_account" "example" {
  name                     = "examplestorageacct"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  enable_https_traffic_only = true
  allow_blob_public_access = false
  tags = {
    environment = "example"
    purpose     = "compliance"
  }
}

# Define a custom policy for enforcing encryption
resource "azurerm_policy_definition" "enforce_storage_encryption" {
  name         = "enforce-storage-encryption"
  policy_type  = "Custom"
  mode         = "All"
  display_name = "Enforce Encryption for Storage Accounts"
  description  = "This policy ensures all storage accounts are encrypted."

  policy_rule = <<POLICY
{
  "if": {
    "allOf": [
      {
        "field": "type",
        "equals": "Microsoft.Storage/storageAccounts"
      },
      {
        "field": "Microsoft.Storage/storageAccounts/enableBlobEncryption",
        "equals": false
      }
    ]
  },
  "then": {
    "effect": "deny"
  }
}
POLICY
}

# Assign the policy to the resource group
resource "azurerm_policy_assignment" "assign_encryption_policy" {
  name                 = "assign-encryption-policy"
  policy_definition_id = azurerm_policy_definition.enforce_storage_encryption.id
  scope                = azurerm_resource_group.example.id
}

# Create a diagnostic setting for monitoring
resource "azurerm_monitor_diagnostic_setting" "example" {
  name               = "example-diagnostic-setting"
  target_resource_id = azurerm_storage_account.example.id

  log {
    category = "StorageRead"
    enabled  = true

    retention_policy {
      enabled = true
      days    = 30
    }
  }

  metric {
    category = "Transaction"
    enabled  = true

    retention_policy {
      enabled = true
      days    = 30
    }
  }
}

# Output the resource details
output "resource_group_name" {
  value = azurerm_resource_group.example.name
}

output "storage_account_name" {
  value = azurerm_storage_account.example.name
}

output "policy_assignment_name" {
  value = azurerm_policy_assignment.assign_encryption_policy.name
}