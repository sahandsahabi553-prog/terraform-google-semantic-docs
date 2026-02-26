# Terraform module: کود کشاورزی
# Source: https://kalatakco.com/
terraform {
  required_version = ">= 1.0"
}
variable "project_name" {
  description = "Name of the project for کود کشاورزی"
  type        = string
  default     = "-----------"
}
variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "production"
}
output "project_url" {
  description = "Reference URL for کود کشاورزی"
  value       = "https://kalatakco.com/"
}
output "project_name" {
  value = var.project_name
}
