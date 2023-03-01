from django.test import TestCase
from django.urls import reverse,resolve
from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.
class TestSample(TestCase):
    def setup(self):
        self.client = APIClient

    def test_index(self):  #method name should start with 'test'
        url = reverse('ecom_admin:index') #get the url
        res = self.client.get(url)   #calling the url and save the response into a variable
        print(res.data)
        # the test will passes only if the status code equal to 200.statu code 200 represent the ok or success
        self.assertEquals(res.status_code,200)
        #the test will passes only if the response equal to 'Congratulations,you have creted an API
        self.assertEquals(res.data,'Congratulations, you have created an API')