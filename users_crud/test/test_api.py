#!/usr/bin/env python3.7
import requests
import unittest


class TestApi(unittest.TestCase):
    """ Class to execute unit tests for api.py """

    @classmethod
    def setUpClass(self):
        """ Set up func called when class is constructed """
        self.base_url = 'http://127.0.0.1:5000/graphql'
        self.headers = {'content-type': 'application/json'}

    def test_query_tournament(self):
        pass
        payload = '{"query": "{tournament(tournament_id:\\"INSERT\\"){tournament{name,owner}}}"}'
        response = requests.post(
            self.base_url, headers=self.headers, data=payload)
        json = response.json()
        #self.assertEqual(response.status_code, 200)
        #self.assertEqual(json['data']['tournament']['name'], 'The F Bois')


    def test_query_user(self):
        # Get Batch list
        payload = '{"query": "{user(id:\\"VXNlcjox\\"){name}}"}'
        response = requests.post(
            self.base_url, headers=self.headers, data=payload)
        json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json['data']['user']['name'], 'David A. Bernal')

    def test_query_user_list(self):
        # Get batch list
        payload = '{"query": "{usersList{edges{node{id}}}}"}'
        response = requests.post(self.base_url, headers=self.headers,
                                 data=payload)
        json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(json['data']['usersList']['edges']), 0)

    def test_create_tournament(self):
        payload = '{"query": "mutation{createTournament(input:{ownerId:\\"VXNlcjo2\\"}){tournament{name,ownerId}}}"}'
        pass


    def test_create_user(self):
        payload = '{"query": "mutation{createUser(input:{name:\\"TestCase\\"}){user{name}}}"}'
        response = requests.post(
            self.base_url, headers=self.headers, data=payload)
        json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json['data']['createUser']
                         ['user']['name'], 'TestCase')

    def test_update_user(self):
        payload = '{"query": "mutation{updateUser(input:{id:\\"VXNlcjo2\\",steamId:12345}){user{name,steamId}}}"}'
        response = requests.post(
            self.base_url, headers=self.headers, data=payload)
        json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json['data']['updateUser']['user']['name'], 'TestCase')
        self.assertEqual(json['data']['updateUser']['user']['steamId'], 12345)

    @classmethod
    def tearDownClass(self):
        """Tear down function called when class is Deconstructed."""
        pass


if __name__ == "__main__":
    # Test Api Endpoints
    suite = unittest.TestLoader().loadTestsFromTestCase(TestApi)
    unittest.TextTestRunner(verbosity=2).run(suite)
