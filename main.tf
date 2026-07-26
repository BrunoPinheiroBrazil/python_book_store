terraform {
  required_version = ">= 1.0.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Configuração da Região AWS (us-east-1 é N. Virginia, com Free Tier garantido)
provider "aws" {
  region = "us-east-1"
}

# 1. Busca automaticamente a imagem mais recente do Ubuntu 22.04 LTS
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"] # Canonical

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
}

# 2. Criar o Security Group (Firewall da AWS)
resource "aws_security_group" "api_sg" {
  name        = "security-group-api-livros"
  description = "Liberar portas para a API Python"

  # Libera a porta 5002 (onde a sua API roda)
  ingress {
    description = "Acesso HTTP para API Python"
    from_port   = 5002
    to_port     = 5002
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Libera a porta SSH (22) para gerenciamento
  ingress {
    description = "Acesso SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Regra de saída: permite a EC2 acessar a internet (para baixar pacotes/pip)
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "sg-api-livros"
  }
}

# 3. Criar a Instância EC2 (Servidor na Nuvem)
resource "aws_instance" "api_server" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro" # 100% coberto pelo AWS Free Tier
  key_name      = "chave-api-livros"

  vpc_security_group_ids = [aws_security_group.api_sg.id]

  tags = {
    Name = "EC2-API-Livros-Python"
  }

  # Script de Boot Automático (Roda no segundo em que a máquina nasce)
  user_data = <<-EOF
              #!/bin/bash
              sudo apt-get update -y
              sudo apt-get install -y python3-pip python3-venv git
              EOF
}

# 4. Output: Exibe o IP Público gerado na tela do terminal ao finalizar
output "ip_publico_aws" {
  value       = aws_instance.api_server.public_ip
  description = "IP Público da sua API rodando na AWS"
}

output "url_api" {
  value       = "http://${aws_instance.api_server.public_ip}:5002/api/livros"
  description = "Endpoint para testar no navegador ou Postman"
}