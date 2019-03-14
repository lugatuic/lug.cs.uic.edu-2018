"""Configuration settings for this project"""

from os import path, pardir
from itertools import product

BACKEND_DIR = path.abspath(path.dirname(__file__))  # This directory
PROJECT_ROOT = path.abspath(path.join(BACKEND_DIR, pardir))

STATIC_DIR = path.join(PROJECT_ROOT, 'frontend-site', 'dist')
STATIC_ROUTE = '/static/'

CORS_ORIGIN_WHITELIST = [
    'http://lug.cs.uic.edu',
    'https://lug.cs.uic.edu'
]

# Ensure all combinations of the below lists are included in the whitelist
CORS_ORIGIN_WHITELIST_DEV = ["".join(x) for x in product(
    ["http", "https"],
    ["://"],
    ["localhost", "0.0.0.0", "127.0.0.1"],
    [":*"])]

# CORS_ORIGIN_WHITELIST_DEV = ["".join(x) for x in product(
#     ["http", "https"],
#     ["://"],
#     ["localhost", "0.0.0.0"],
#     [":"],
#     ["5000", "8080"])]

class Config:
    """Base configuration."""
    BACKEND_DIR = BACKEND_DIR
    PROJECT_ROOT = PROJECT_ROOT
    # DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.


class ProdConfig(Config):
    """Production configuration."""
    ENV = 'prod'
    DEBUG = False
    CORS_ORIGIN_WHITELIST = CORS_ORIGIN_WHITELIST


class DevConfig(Config):
    """Development configuration."""
    ENV = 'dev'
    DEBUG = True
    CORS_ORIGIN_WHITELIST = CORS_ORIGIN_WHITELIST_DEV + CORS_ORIGIN_WHITELIST


class TestConfig(Config):
    """Test configuration."""
    ENV = 'test'
    TESTING = True
    DEBUG = True
    CORS_ORIGIN_WHITELIST = CORS_ORIGIN_WHITELIST_DEV + CORS_ORIGIN_WHITELIST
