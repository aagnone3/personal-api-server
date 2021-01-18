import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from app.app import app
from a2wsgi import ASGIMiddleware

# Phusion Passenger expects an 'application' object in the namespace
application = ASGIMiddleware(app)
