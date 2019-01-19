from os import path, pardir

BACKEND_DIR = path.abspath(path.dirname(__file__))  # This directory
PROJECT_ROOT = path.abspath(path.join(BACKEND_DIR, pardir))

STATIC_DIR = path.join(PROJECT_ROOT, 'frontend-site', 'dist')
STATIC_ROUTE = '/static/'


class Config:
    """Base configuration."""
    BACKEND_DIR = BACKEND_DIR
    PROJECT_ROOT = PROJECT_ROOT
    # DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    CORS_ORIGIN_WHITELIST = [
        'http://0.0.0.0:5000',
        'http://localhost:5000',
    ]


class ProdConfig(Config):
    """Production configuration."""
    ENV = 'prod'
    DEBUG = False


class DevConfig(Config):
    """Development configuration."""
    ENV = 'dev'
    DEBUG = True


class TestConfig(Config):
    """Test configuration."""
    ENV = 'test'
    TESTING = True
    DEBUG = True
