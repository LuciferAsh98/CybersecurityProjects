# Output Resource Group Name
output "resource_group_name" {
  description = "Name of the created resource group"
  value       = azurerm_resource_group.example.name
}

# Output Storage Account Name
output "storage_account_name" {
  description = "Name of the created storage account"
  value       = azurerm_storage_account.example.name
}

# Output Policy Assignment Name
output "policy_assignment_name" {
  description = "Name of the policy assignment"
  value       = azurerm_policy_assignment.assign_encryption_policy.name
}