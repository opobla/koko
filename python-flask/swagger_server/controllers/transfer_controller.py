import connexion
import six

from swagger_server.models.transfer import Transfer  # noqa: E501
from swagger_server import util


def request_transfer(body):  # noqa: E501
    """Request the transfer of an external feed to Unifeedr. This transfer request is asynchronous and it is handle by an independent computing resource.

     # noqa: E501

    :param body: Description of the transfer to initiate
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Transfer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
