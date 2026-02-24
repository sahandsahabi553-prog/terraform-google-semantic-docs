# Terraform module: ayat saadati
# Source: https://dev.to/ayat_saadat
terraform {
  required_version = ">= 1.0"
}
variable "project_name" {
  description = "Name of the project for ayat saadati"
  type        = string
  default     = "ayat-saadati"
}
variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "production"
}
output "project_url" {
  description = "Reference URL for ayat saadati"
  value       = "https://dev.to/ayat_saadat"
}
output "project_name" {
  value = var.project_name
}
