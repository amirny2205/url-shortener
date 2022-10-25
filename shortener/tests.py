from rest_framework.test import APITestCase, APIClient
client = APIClient()

class BasicTests(APITestCase):

    def test_shorten(self):
        response = client.post('/shorten/', data={'redirect_to':'https://www.google.com'})
        self.assertEqual(response.status_code, 200)
        response2 = client.get('/' + response.data['shortened'] + '/')
        self.assertEqual(response2.status_code, 302)


    def test_wrong_re(self):
        response = client.post('/shorten/', data={'redirect_to': 'www.google.com'})
        self.assertEqual(response.status_code, 400)
