variable "app_env" {
  description = "Environment (dev, staging, prod)"
  type        = string
  default     = "prod"
}

variable "project_name" {
  description = "Project identifier"
  type        = string
  default     = "neil-munoz-portfolio"
}

variable "database_url" {
  description = "Database connection string"
  type        = string
  sensitive   = true
  default     = null
}
