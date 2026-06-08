import os
import pathlib

projects = [
    ("01-web-server-hardening", "Web Server Hardening & Load Balancing"),
    ("02-database-deployment", "Database Deployment & Backup"),
    ("03-docker-orchestration", "Docker Container Orchestration"),
    ("04-ssh-vpn-management", "SSH & VPN Access Management"),
    ("05-firewall-network", "Firewall & Network Policies"),
    ("06-ssl-certificate", "SSL Certificate Automation"),
    ("07-monitoring-stack", "Monitoring Stack Deployment"),
    ("08-system-metrics", "System Metrics Collection"),
    ("09-backup-recovery", "Backup & Disaster Recovery"),
    ("10-file-sync", "File Synchronization & Replication"),
    ("11-multi-tier-app", "Multi-Tier Application Deployment"),
    ("12-cicd-pipeline", "CI/CD Pipeline Infrastructure"),
    ("13-user-access", "User & Access Management"),
    ("14-license-management", "Software License Management"),
    ("15-incident-response", "Incident Response Automation"),
    ("16-infrastructure-code", "Infrastructure as Code"),
    ("17-kubernetes-cluster", "Kubernetes Cluster Setup"),
    ("18-container-registry", "Container Registry Management"),
    ("19-dev-environment", "Development Environment Provisioning"),
    ("20-testing-infra", "Testing Infrastructure"),
]

for proj_dir, proj_title in projects:
    os.chdir(proj_dir)
    
    # Create playbook
    with open("playbook.yml", "w") as f:
        f.write(f"""---
- name: {proj_title}
  hosts: all
  become: yes
  gather_facts: true

  vars_files:
    - vars/common.yml

  roles:
    - role1
    - role2
""")
    
    # Create inventory
    with open("inventory.ini", "w") as f:
        f.write("""[all]
# Add your hosts here

[production]
# Production servers

[staging]
# Staging servers

[all:vars]
ansible_user=ansible
ansible_become=yes
""")
    
    # Create ansible.cfg
    with open("ansible.cfg", "w") as f:
        f.write("""[defaults]
inventory = ./inventory.ini
roles_path = ./roles
host_key_checking = False
log_path = ./ansible.log
gathering = smart

[ssh_connection]
ssh_args = -o ControlMaster=auto -o ControlPersist=60s
pipelining = True
""")
    
    # Create requirements
    with open("requirements.txt", "w") as f:
        f.write("""ansible>=2.9.0
jinja2>=2.11
pyyaml>=5.1
""")
    
    # Create common vars
    with open("vars/common.yml", "w") as f:
        f.write("""---
# Common variables
project_name: automation
environment: production
""")
    
    # Create README
    with open("README.md", "w") as f:
        f.write(f"""# {proj_title}

Ansible automation project for {proj_title.lower()}.

## Quick Start

1. Update `inventory.ini` with your hosts
2. Customize `vars/common.yml`
3. Run: `ansible-playbook -i inventory.ini playbook.yml`

## File Structure

```
{proj_dir}/
├── playbook.yml
├── inventory.ini
├── ansible.cfg
├── requirements.txt
├── vars/
│   └── common.yml
├── roles/
│   ├── role1/
│   ├── role2/
│   └── ...
└── README.md
```

## Prerequisites

- Ansible 2.9+
- Python 3.6+

## Usage

### Dry-run
```bash
ansible-playbook -i inventory.ini playbook.yml --check
```

### Full execution
```bash
ansible-playbook -i inventory.ini playbook.yml
```

### Verbose output
```bash
ansible-playbook -i inventory.ini playbook.yml -vvv
```
""")
    
    # Create .gitignore
    with open(".gitignore", "w") as f:
        f.write("""*.retry
*.log
__pycache__/
*.pyc
.venv/
venv/
*.tmp
*.bak
""")
    
    print(f"✓ Templates created for: {proj_dir}")
    os.chdir("..")

print("\nAll 20 projects initialized with templates!")
