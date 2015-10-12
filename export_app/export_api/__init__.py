from __future__ import absolute_import

from flask import Blueprint
from flask_restful import Api

from export_app.export_api.resources import ApiRoot, ScoredDataCsvExport
from .routes import API_ROUTES

api_b = Blueprint('api', __name__)
api_v1 = Api(api_b)

api_v1.add_resource(ApiRoot, API_ROUTES['api_root'], endpoint='exports')
api_v1.add_resource(ScoredDataCsvExport, API_ROUTES['csv_export'], endpoint='csv')
