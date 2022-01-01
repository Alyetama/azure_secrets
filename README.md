# azure_secrets
```python
from azure_secrets import AzureSecrets

az = AzureSecrets()
client = az.client()

client.set_secret(secret_name, secret_value)  # set a secret:
client.get_secret(secret_name)  # get a secret
az.delete_secret(secret_name)  # delete a secret
```
