from flask import Response, request
from flask.views import View
from urllib2 import urlopen

from wsqv import utils


class Measurements(View):

    methods = ['GET']

    def dispatch_request(self):

        api_url = utils.get_api_url()

        year = request.args.get('viti', '')
        month = request.args.get('muji', '')
        station = request.args.get('stacion', '')

        request_url = "%s/measurements?year=%s&month=%s&station=%s" % (api_url, year, month, station)

        measurements = urlopen(request_url).read()

        # Build response object.
        resp = Response(
            response=measurements, mimetype='application/json')

        # Return response.
        return resp
