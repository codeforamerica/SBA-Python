#!/usr/bin/env python

"""Unit tests for Python API wrapper."""

import unittest

from mock import Mock

import api 
from api import (SBA_API, Licenses_And_Permits, Loans_And_Grants,
Recommended_Sites, City_And_County_Web_Data)

def set_up_tests():
	"""Cut down on boilerplate setup testing code."""
	api.urlopen = Mock()
	api.json = Mock()

def called_url():
	"""Test what URL was called through the mocked urlopen."""
	url = api.urlopen.call_args[0][0]
	return url


class Test_SBA_API(unittest.TestCase):

	def setUp(self):
		set_up_tests()

	def test_base_url(self):
		example = SBA_API()
		self.assertEquals(example.base_url, 'http://api.sba.gov')

class TestApiMethod(unittest.TestCase):

	def setUp(self):
		set_up_tests()

	def test_empty_api_method_fails(self):
		self.assertRaises(TypeError, SBA_API())

class TestMethod_Licenses_And_Permits(unittest.TestCase):

	#def __init__(self): 
	#self.base_url = 'http://api.sba.gov/license_permit'

	def setUp(self):
		set_up_tests()

	def testmethod_by_category(self):
	    api.Licenses_And_Permits().by_category('doing business as')
	    url = called_url()
	    expected_url = ('http://api.sba.gov/license_permit/by_category/'
		    'doing business as.json')
	    self.assertEquals(url, expected_url)

	def testmethod_by_state(self):
	    api.Licenses_And_Permits().by_state('ca')
	    url = called_url()
	    expected_url = ('http://api.sba.gov/license_permit/all_by_state/ca.json')
	    self.assertEquals(url, expected_url)

	#def testmethod_by_business_type(self):
	    #api.Licenses_And_Permits().by_business_type('general business license')
	    #url = called_url()
	    #expected_url = ('http://api.sba.gov/license_permit/by_business_type/'
		    #'general business license.json')
	    #self.assertEquals(url, expected_url)

	#def testmethod_by_business_type_state(self):
	    #api.Licenses_And_Permits().by_business_type_state('child care services', 'va')
	    #url = called_url()
	    #expected_url = ('http://api.sba.gov/license_permit/state_only/'
		#'child care services/va.json')
	    #self.assertEquals(url, expected_url)

	#def testmethod_by_business_type_state_city(self):
	    #api.Licenses_And_Permits().by_business_type_state_city('restaurant',
		    #'ny', 'albany')
	    #url = called_url()
	    #expected_url = ('')
	    #self.assertEquals(url, expected_url)

	#def testmethod_by_business_type_zipcode(self):
	    #api.Licenses_And_Permits().by_business_type_zipcode
	    #url = called_url()
	    #expected_url = ('')
	    #self.assertEquals(url, expected_url)

	#def testmethod_by_business_type_state_county(self):
	    #api.Licenses_And_Permits().by_business_type_state_county('')
	    #url = called_url()
	    #expected_url = ('')
	    #self.assertEquals(url, expected_url)


#class TestMethod_Loans_And_Grants(SBA_API):

	#def __init__(self): 
	    #self.base_url = 'http://api.sba.gov/loans_grants'

	    #def federal(self):
	    #url = called_url()
	    #expected_url = ('')
	    #self.assertEquals(url, expected_url)

	#def state(self):
	    #url = called_url()
	    #expected_url = ('')
	    #self.assertEquals(url, expected_url)

	#def federal_and_state(self):
	    #url = called_url()
	    #expected_url = ('')
	    #self.assertEquals(url, expected_url)

	#def by_industry(self):
	    #url = called_url()
	    #expected_url = ('')
	    #self.assertEquals(url, expected_url)

	#def by_speciality(self):
	    #url = called_url()
	    #expected_url = ('')
	    #self.assertEquals(url, expected_url)

	#def by_industry_specialty(self):
	    #url = called_url()
	    #expected_url = ('')
	    #self.assertEquals(url, expected_url)

	#def by_state_industry(self):
	    #url = called_url()
	    #expected_url = ('')
	    #self.assertEquals(url, expected_url)

	#def by_state_specialty(self):
	    #url = called_url()
	    #expected_url = ('')
	    #self.assertEquals(url, expected_url)

	#def by_state_industry_specialty(self):
	    #url = called_url()
	    #expected_url = ('')
	    #self.assertEquals(url, expected_url)


#class TestMethod_Recommended_Sites(SBA_API):

	#def __init__(self):
	    #url = called_url()
	    #expected_url = ('')
	    #self.assertEquals(url, expected_url)
	    #self.base_url = 'http://api.sba.gov/rec_sites'

	#def by_keyword(self):
	    #url = called_url()
	    #expected_url = ('')
	    #self.assertEquals(url, expected_url)

	#def by_category(self):
	    #url = called_url()
	    #expected_url = ('')
	    #self.assertEquals(url, expected_url)

	#def by_master_term(self):
	    #url = called_url()
	    #expected_url = ('')
	    #self.assertEquals(url, expected_url)

	#def by_domain(self):
	    #url = called_url()
	    #expected_url = ('')
	    #self.assertEquals(url, expected_url)


#class TestMethod_City_And_County_Web_Data(SBA_API):

	#def __init__(self):
	    #url = called_url()
	    #expected_url = ('')
	    #self.assertEquals(url, expected_url)
	    #self.base_url = 'http://api.sba.gov/geodata'

	#def all_urls_by_state(self):
	    #url = called_url()
	    #expected_url = ('')
	    #self.assertEquals(url, expected_url)

	#def all_urls_by_county(self):
	    #url = called_url()
	    #expected_url = ('')
	    #self.assertEquals(url, expected_url)

	#def primary_urls_by_city(self):
	    #url = called_url()
	    #expected_url = ('')
	    #self.assertEquals(url, expected_url)

	#def primary_urls_by_county(self):
	    #url = called_url()
	    #expected_url = ('')
	    #self.assertEquals(url, expected_url)

	#def all_data_by_state(self):
	    #url = called_url()
	    #expected_url = ('')
	    #self.assertEquals(url, expected_url)

	#def all_data_by_city(self):
	    #url = called_url()
	    #expected_url = ('')
	    #self.assertEquals(url, expected_url)

	#def all_data_by_county(self):
	    #url = called_url()
	    #expected_url = ('')
	    #self.assertEquals(url, expected_url)


if __name__ == '__main__':
	unittest.main()
