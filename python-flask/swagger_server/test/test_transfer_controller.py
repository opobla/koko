# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.transfer import Transfer  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTransferController(BaseTestCase):
    """TransferController integration test stubs"""

    def test_request_transfer(self):
        """Test case for request_transfer

        Request the transfer of an external feed to Unifeedr. This transfer request is asynchronous and it is handle by an independent computing resource.
        """
        body = Transfer()
        response = self.client.open(
            '/m8765/PetStore/1.0.0/transfer',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
