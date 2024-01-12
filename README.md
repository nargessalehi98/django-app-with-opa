# Django app with OPA
## Table of Contents
   * [Introduction](#introduction)
   * [What is OPA?](#what-is-opa)
   * [Prerequisites](#prerequisites)
   * [Start the Cluster on a macOS machine](#start-the-cluster-on-a-macos-machine)
   * [Database migrations](#database-migrations)
   * [Create SuperUser](#create-superuser)

## Introduction
This application combines the power of Django, a robust web framework in Python, with Open Policy Agent (OPA), a versatile policy engine for access control management. By integrating OPA into your Django app, you can enforce fine-grained authorization policies and make dynamic access control decisions


## What is OPA?
Open Policy Agent (OPA) is an open-source policy engine that enables you to define and enforce policies for controlling access to resources and data. OPA provides a declarative language called Rego to express authorization policies in a concise and flexible manner. By integrating OPA into your Django app, you can dynamically evaluate policies and make access control decisions based on runtime information.

## Prerequisites
- Ansible: Make sure Ansible is installed on your machine. You can download and install Ansible from the official website: [https://www.ansible.com/](https://www.ansible.com/) or run the following command in the terminal:
   ``` bash
  brew install ansible
  ```
- This command will display the installed Ansible version information if the installation was successful.
  ```bash
  ansible --version
  ```


## Start the Cluster on a macOS Machine

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/nargessalehi98/django-app-with-opa.git
   ```

2. Navigate to the Project Directory:

   ```bash
   cd django-app-with-opa
   ```

3. Run with ansible:
   ```bash
   cd bootstrap
   ansible-playbook main.yaml
   ```
- To modify the cluster values or Helm charts, you can make changes to the vars/main.yml file.

## Database migrations

1. Open a terminaland, Execute the following command to access the pod:
   ```bash
   kubectl exec -it <pod_name> -- /bin/bash
   ```
- Replace `<pod_name>` with the name of the pod where you want to execute the migrations.

2. Run the database migration command to apply the migrations:
   ```bash
   python manage.py migrate
   ```
- This command will execute the necessary database migrations for your Django application.

## Create SuperUser

1. After your application Pod is running, you can create a superuser by running the following commands:
    ```bash 
   kubectl exec -it <pod_name> -- /bin/bash
   python manage.py create superuser
   ```