terraform {
  required_version = ">= 1.6.0"

  required_providers {
    random = {
      source  = "hashicorp/random"
      version = "~> 3.5"
    }
  }

  cloud {
    organization = "NeilandAPIs"

    workspaces {
      name = "neil-munoz-portfolio"
    }
  }
}

# -------------------------
# VARIABLES
# -------------------------

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

# -------------------------
# LOCALS
# -------------------------

locals {
  common_tags = {
    project = var.project_name
    env     = var.app_env
    managed = "terraform"
  }
}

# -------------------------
# RANDOM SECRET
# -------------------------

resource "random_password" "session_secret" {
  length  = 32
  special = true
}

# -------------------------
# OUTPUTS
# -------------------------

output "session_secret_generated" {
  description = "Generated session secret"
  value       = random_password.session_secret.result
  sensitive   = true
}
