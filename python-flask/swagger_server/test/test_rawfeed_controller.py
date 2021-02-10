# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.rawfeed import Rawfeed  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRawfeedController(BaseTestCase):
    """RawfeedController integration test stubs"""

    def test_add_raw_feed(self):
        """Test case for add_raw_feed

        Add a new feed from the outside
        """
        body = Rawfeed()
        response = self.client.open(
            '/m8765/PetStore/1.0.0/rawfeed',
            method='POST',
            data=json.dumps(body),
            content_type='text/csv')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
