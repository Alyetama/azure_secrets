"""azure secrets"""
import functools
import os
from pathlib import Path

from dotenv import load_dotenv
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


class AzureSecretsClient:
	def __init__(self, env_file='~/.zshenv'):
		self.env_file = env_file

	@functools.cache
	def client(self):
		load_dotenv(Path(self.env_file).expanduser())
		keyVaultName = os.environ["KEY_VAULT_NAME"]
		KVUri = f"https://{keyVaultName}.vault.azure.net"
		credential = DefaultAzureCredential()
		client = SecretClient(vault_url=KVUri, credential=credential)
		return client


class AzureSecrets:
	"""
	client = AzureSecretsClient().client()
	az = AzureSecrets(client)
	- set a secret:
		az.set_secret(secret_name, secret_value)
	- get a secret:
		az.get_secret(secret_name)
	- delete a secret:
		az.delete_secret(secret_name)
	"""
	def __init__(self, client):
		self.client = client

	def get_secret(self, name, **kwargs):
		return self.client.get_secret(name, **kwargs)

	def set_secret(self, name, value, **kwargs):
		return self.client.set_secret(name, value, **kwargs)

	def delete_secret(self, secret_name):
		poller = self.client.begin_delete_secret(secret_name)
		deleted_secret = poller.result()


__version__ = "0.0.7"
