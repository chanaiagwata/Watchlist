from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views,forms
from . import views,forms