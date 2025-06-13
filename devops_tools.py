# devops_tools.py

devops_tools = {
    "CI/CD": [
        {"name": "Jenkins", "description": "Open-source automation server", "url": "https://www.jenkins.io/"},
        {"name": "GitHub Actions", "description": "CI/CD from GitHub", "url": "https://github.com/features/actions"},
    ],
    "Containerization": [
        {"name": "Docker", "description": "Container platform", "url": "https://www.docker.com/"},
        {"name": "Podman", "description": "Daemonless container engine", "url": "https://podman.io/"},
    ],
    "Infrastructure as Code": [
        {"name": "Terraform", "description": "IAC tool from HashiCorp", "url": "https://www.terraform.io/"},
        {"name": "Pulumi", "description": "IAC using real languages", "url": "https://www.pulumi.com/"},
    ]
}

def list_tools():
    for category, tools in devops_tools.items():
        print(f"\n{category}:")
        for tool in tools:
            print(f" - {tool['name']}: {tool['description']} ({tool['url']})")

if __name__ == "__main__":
    list_tools()
