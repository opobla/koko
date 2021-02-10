# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inputfeed import Inputfeed  # noqa: E501
from swagger_server.test import BaseTestCase


class TestProjectController(BaseTestCase):
    """ProjectController integration test stubs"""

    def test_project_post(self):
        """Test case for project_post

        Create a new project for the autenticated user
        """
        response = self.client.open(
            '/m8765/PetStore/1.0.0/project',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_project_project_id_get(self):
        """Test case for project_project_id_get

        List the projects of the authenticated user
        """
        response = self.client.open(
            '/m8765/PetStore/1.0.0/project/{project_id}'.format(project_id='project_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_project_project_id_inputfeed_get(self):
        """Test case for project_project_id_inputfeed_get

        Get the feeds of a project
        """
        body = Inputfeed()
        response = self.client.open(
            '/m8765/PetStore/1.0.0/project/{project_id}/inputfeed'.format(project_id='project_id_example'),
            method='GET',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_project_project_id_inputfeed_post(self):
        """Test case for project_project_id_inputfeed_post

        Add a new input feed to the project
        """
        body = Inputfeed()
        response = self.client.open(
            '/m8765/PetStore/1.0.0/project/{project_id}/inputfeed'.format(project_id='project_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
