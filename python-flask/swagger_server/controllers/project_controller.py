import connexion
import six

from swagger_server.models.inputfeed import Inputfeed  # noqa: E501
from swagger_server import util


def project_post():  # noqa: E501
    """Create a new project for the autenticated user

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def project_project_id_get(project_id):  # noqa: E501
    """List the projects of the authenticated user

     # noqa: E501

    :param project_id: ID of the project
    :type project_id: 

    :rtype: None
    """
    return 'do some magic!'


def project_project_id_inputfeed_get(project_id, body):  # noqa: E501
    """Get the feeds of a project

     # noqa: E501

    :param project_id: ID of the project
    :type project_id: 
    :param body: Description of the transfer to initiate
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Inputfeed.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def project_project_id_inputfeed_post(project_id, body):  # noqa: E501
    """Add a new input feed to the project

     # noqa: E501

    :param project_id: ID of the project
    :type project_id: 
    :param body: Description of the transfer to initiate
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Inputfeed.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
