output "zenml_server_url" {
  value = var.create_ingress_controller? "https://${data.kubernetes_service.ingress-controller[0].status.0.load_balancer.0.ingress.0.ip}.nip.io/${var.ingress_path}" : "https://${var.ingress_controller_hostname}.nip.io/${var.ingress_path}"
}
output "username" {
  value = var.username
}
output "password" {
  value = var.password
  sensitive = true
}
output "ca_crt" {
  value = base64decode(data.kubernetes_secret.certificates.binary_data["ca.crt"])
  sensitive = true
}
