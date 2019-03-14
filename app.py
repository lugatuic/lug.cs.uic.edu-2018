"""Backend entry point. Build app from factory using config."""

from flask.helpers import get_debug_flag
from backend_site.app import createApp
from backend_site.settings import DevConfig, ProdConfig

if get_debug_flag():
    CONFIG = DevConfig
    print("Using DEV config!")
else:
    CONFIG = ProdConfig
    print("Using PROD config!")
# CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = createApp(CONFIG)
