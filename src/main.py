#!/usr/bin/env python3
import logging
import os

from keycloak import KeycloakConnectionError
from retry.api import retry_call

import identityutils.logger as logger
from identityutils.configuration import load_configuration, edit_keycloak_config
from identityutils.keycloak_client import KeycloakClient

mode = os.environ.get('FLASK_ENV')
if mode == 'develop':
    config_file = "config.develop.ini"
elif mode == 'demo':
    config_file = "config.demo.ini"
elif mode == 'production':
    config_file = "config.production.ini"
else:
    config_file = "config.ini"
config_path = os.path.join(os.path.dirname(__file__), "../conf/", config_file)

logger.Logger.get_instance().load_configuration(os.path.join(os.path.dirname(__file__), "../conf/logging.yaml"))
logger = logging.getLogger("IDENTITY_SETUP")


def register_default_resources():
    """
    Create default resources and policies associated
    """
    # TODO


def register_default_users():
    """
    Create default users
    """
    eric_id = keycloak.create_user("eric", "eric")
    logger.debug('Created Eric user: ' + eric_id)
    alice_id = keycloak.create_user("alice", "alice")
    logger.debug('Created Alice user: ' + alice_id)


def register_oauth2_proxy_client():
    proxy_server_endpoint = config.get("Keycloak", "proxy_server_endpoint")
    options = {
        'clientId': 'oauth2-proxy',
        'secret': 'secret',  # TODO changeme
        "bearerOnly": False,
        "publicClient": False,
        'baseUrl': proxy_server_endpoint,
        'redirectUris': [
            proxy_server_endpoint + '/*'
        ]
    }
    keycloak.register_client(options=options)


def keycloak_client(config):
    logger.info("Starting Keycloak client...")
    return KeycloakClient(server_url=config.get("Keycloak", "auth_server_url"),
                          realm=config.get("Keycloak", "realm"),
                          resource_server_endpoint=config.get("Keycloak", "resource_server_endpoint"),
                          username=config.get("Keycloak", "admin_username"),
                          password=config.get("Keycloak", "admin_password")
                          )


if __name__ == '__main__':
    config = load_configuration(config_path)
    keycloak = retry_call(keycloak_client, fargs=[config], exceptions=KeycloakConnectionError, delay=1, backoff=1.5,
                          jitter=(1, 2), logger=logger)
    register_oauth2_proxy_client()
    register_default_resources()
    register_default_users()
