from flask import Response, request
from flask.views import View
from urllib2 import urlopen

from wsqv import utils


class Measurements(View):

    methods = ['GET']

    def dispatch_request(self):

        print 'asasas'

        api_url = utils.get_api_url()

        year = request.args.get('year', '')
        month = request.args.get('month', '')

        request_url = "%s/measurements?year=%s&month=%s" % (api_url, year, month)

        print request_url

        measurements = urlopen(request_url).read()

        # Build response object.
        resp = Response(
            response=measurements, mimetype='application/json')

        # Return response.
        return resp
