from flask import current_app


class Utils(object):

    def __init__(self):
        pass

    @staticmethod
    def get_api_url():
        ''' Get Water Surface Quality API URL.
        '''
        api_url = current_app.config['API_WATER_SURFACE_QUALITY']

        return api_url
