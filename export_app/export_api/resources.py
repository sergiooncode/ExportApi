# -*- coding: utf-8 -*-
import StringIO
import csv

from flask import make_response, request
from flask_restful import Resource, reqparse, fields, marshal

from authentication import requires_auth


class UrlField(fields.Url):
    def output(self, key, obj):
        result = super(UrlField, self).output(key, obj)
        url = 'http://' + request.host + result
        return url


resources = [
    {
        'description': 'scored data view in csv format'
    }
]

resource_fields = {
    'description': fields.String,
    'url': UrlField('api.csv')
}


class ApiRoot(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('description', type=str, required=True,
                                   help='No resource name provided', location='json')
        super(ApiRoot, self).__init__()

    def get(self):
        return {'resources': [marshal(resource, resource_fields) for resource in resources]}


class ScoredDataCsvExport(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('description', type=str, location='json')
        super(ScoredDataCsvExport, self).__init__()

    @requires_auth
    def get(self):
        from export_app.export_api.db import get_all_scored_data_rows
        d = get_all_scored_data_rows()
        si = StringIO.StringIO()
        cw = csv.writer(si)
        for row in d:
            cw.writerow(row)
        resp = make_response(si.getvalue())
        resp.headers['Content-type'] = 'text/csv'
        resp.headers['Content-Disposition'] = 'attachment; filename=export.csv'
        return resp
