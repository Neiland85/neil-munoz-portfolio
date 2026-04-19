output "session_secret_generated" {
  description = "Generated session secret"
  value       = random_password.session_secret.result
  sensitive   = true
}
