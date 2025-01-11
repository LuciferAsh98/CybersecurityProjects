# Azure Credentials
variable "azure_client_id" {
  description = "Azure Client ID"
  type        = string
}

variable "azure_client_secret" {
  description = "Azure Client Secret"
  type        = string
}

variable "azure_subscription_id" {
  description = "Azure Subscription ID"
  type        = string
}

variable "azure_tenant_id" {
  description = "Azure Tenant ID"
  type        = string
}

# Location for Resources
variable "location" {
  description = "Azure region to deploy resources"
  type        = string
  default     = "East US"
}

# Resource Group Name
variable "resource_group_name" {
  description = "Name of the Azure resource group"
  type        = string
  default     = "example-resources"
}