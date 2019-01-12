"""Backend entry point. Build app from factory using config."""

from flask.helpers import get_debug_flag
from backend_site.app import createApp
from backend_site.settings import DevConfig, ProdConfig

CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = createApp(CONFIG)
