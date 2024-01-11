# Django app with opa


## Introduction


## Start the Cluster

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/nargessalehi98/django-app-with-opa.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd django-app-with-op
   ```

3. **Run with ansible**:
   ```bash
   cd bootstrap
   ansible-playbook main.yaml
   ```
   - To modify the cluster values or Helm charts, you can make changes to the vars/main.yml file.