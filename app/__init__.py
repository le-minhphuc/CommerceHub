from flask import Flask

commerce_hub_app = Flask(__name__)

from app import routes # work around for circular imports