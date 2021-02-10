import connexion
import six

from swagger_server.models.rawfeed import Rawfeed  # noqa: E501
from swagger_server import util


def add_raw_feed(body):  # noqa: E501
    """Add a new feed from the outside

     # noqa: E501

    :param body: CSV file with the rawfeed to be imported
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Rawfeed.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
