# Contoso Retail Azure Cloud Infrastructure

> A practical Azure Cloud Engineering project demonstrating secure networking, Linux administration, Dockerized application deployment, Azure SQL integration, monitoring, backup, and GitHub Actions CI/CD.

---

## 📌 Project Overview

This project demonstrates the migration and deployment of a web application for **Contoso Retail Ltd** onto Microsoft Azure.

The application runs on an Azure Linux VM using Docker and Nginx, while Azure SQL Database provides the managed database layer.

The project also implements automated CI/CD using GitHub Actions and a self-hosted runner hosted on the Azure VM.

### Objectives

- Deploy a web application on Azure
- Implement VNet-based network architecture
- Secure VM access using NSGs and Azure Bastion
- Containerize the application using Docker
- Use Azure SQL Database as the managed database
- Implement monitoring and backup
- Automate testing and deployment using GitHub Actions
- Troubleshoot real-world cloud deployment issues

---

# 🏗️ Architecture

```text
                         Internet
                            |
                            | HTTP :80
                            v
                +----------------------+
                |     Azure Web VM     |
                |  Ubuntu 24.04 LTS    |
                | vm-web-prod-ci-001   |
                +----------+-----------+
                           |
                         Nginx
                           |
                    127.0.0.1:5000
                           |
                           v
                +----------------------+
                |   Docker Container   |
                |      Flask App       |
                +----------+-----------+
                           |
                           | SQL
                           v
                +----------------------+
                |   Azure SQL Database |
                +----------------------+

             Administration
                    |
                    v
             Azure Bastion
                    |
                    v
                 Azure VM

             CI/CD
                    |
                    v
             GitHub Actions
                    |
                    v
          Self-hosted Runner
                on VM
                    |
                    v
                 Docker
