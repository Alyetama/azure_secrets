"""azure secrets"""
import os
from pathlib import Path

from dotenv import load_dotenv
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


class AzureSecrets:
	"""
	- set a secret:
		client.set_secret(secret_name, secret_value)
	- get a secret:
		client.get_secret(secret_name)
	- delete a secret:
		az.delete_secret(secret_name)
	"""
	def __init__(self, env_file='~/.zshenv'):
		self.env_file = env_file

	def client(self):
		load_dotenv(Path(self.env_file).expanduser())
		keyVaultName = os.environ["KEY_VAULT_NAME"]
		KVUri = f"https://{keyVaultName}.vault.azure.net"
		credential = DefaultAzureCredential()
		client = SecretClient(vault_url=KVUri, credential=credential)
		return client

	def delete_secret(self, secret_name):
		poller = client.begin_delete_secret(secret_name)
		deleted_secret = poller.result()


__version__ = "0.0.5"
