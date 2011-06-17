#!/usr/bin/env python

"""Unit tests for Python API wrapper."""

import unittest

from mock import Mock

try:
    from urllib import unquote 
except ImportError:  # pragma: no cover
    # For Python 3.
    from urllib.parse import unquote

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
                        'doing%20business%20as.json')
        self.assertEquals(url, expected_url)

    def testmethod_by_state(self):
        api.Licenses_And_Permits().by_state('ca')
        url = called_url()
        expected_url = ('http://api.sba.gov/license_permit/all_by_state/ca.json')
        self.assertEquals(url, expected_url)

    def testmethod_by_business_type(self):
        api.Licenses_And_Permits().by_business_type('general business license')
        url = called_url()
        expected_url = ('http://api.sba.gov/license_permit/by_business_type/'
                        'general%20business%20license.json')
        self.assertEquals(url, expected_url)

    def testmethod_by_business_type_state(self):
        api.Licenses_And_Permits().by_business_type_state('child care services', 'va')
        url = called_url()
        expected_url = ('http://api.sba.gov/license_permit/state_only/'
                        'child%20care%20services/va.json')
        self.assertEquals(url, expected_url)

    def testmethod_by_business_type_state_county(self):
        api.Licenses_And_Permits().by_business_type_state_county('child care services', 'ca', 'los angeles county')
        url = called_url()
        expected_url = ('http://api.sba.gov/license_permit/state_and_county/'
                        'child%20care%20services/ca/los%20angeles%20county.json')
        self.assertEquals(url, expected_url)

    def testmethod_by_business_type_state_city(self):
        api.Licenses_And_Permits().by_business_type_state_city('restaurant', 'ny', 'albany')
        url = called_url()
        expected_url = ('http://api.sba.gov/license_permit/state_and_city/'
                        'restaurant/ny/albany.json')
        self.assertEquals(url, expected_url)

    def testmethod_by_business_type_zipcode(self):
        api.Licenses_And_Permits().by_business_type_zipcode('restaurant', '49684') 
        url = called_url()
        expected_url = ('http://api.sba.gov/license_permit/by_zip/'
                        'restaurant/49684.json')
        self.assertEquals(url, expected_url)


class TestMethod_Loans_And_Grants(unittest.TestCase):

    #def __init__(self): 
        #self.base_url = 'http://api.sba.gov/loans_grants'
    
    def testmethod_federal(self):
        api.Loans_And_Grants().federal()
        url = called_url()
        expected_url = ('http://api.sba.gov/loans_grants/federal.json')
        self.assertEquals(url, expected_url)

    def testmethod_state(self):
        api.Loans_And_Grants().state('ia')
        url = called_url()
        expected_url = ('http://api.sba.gov/loans_grants/state_financing_for/'
                        'ia.json')
        self.assertEquals(url, expected_url)

    def testmethod_federal_and_state(self):
        api.Loans_And_Grants().federal_and_state('me')
        url = called_url()
        expected_url = ('http://api.sba.gov/loans_grants/'
                        'federal_and_state_financing_for/me.json')
        self.assertEquals(url, expected_url)

    def testmethod_by_industry(self):
        api.Loans_And_Grants().by_industry('manufacturing')
        url = called_url()
        expected_url = ('http://api.sba.gov/loans_grants/nil/for_profit/'
                        'manufacturing/nil.json')
        self.assertEquals(url, expected_url)

    def testmethod_by_speciality(self):
        api.Loans_And_Grants().by_speciality('woman')
        url = called_url()
        expected_url = ('http://api.sba.gov/loans_grants/nil/for_profit/nil/'
                        'woman.json')
        self.assertEquals(url, expected_url)

    def testmethod_by_speciality_multiple(self):
        api.Loans_And_Grants().by_speciality('woman-general_purpose')
        url = called_url()
        expected_url = ('http://api.sba.gov/loans_grants/nil/for_profit/nil/'
                        'woman-general_purpose.json') 
        self.assertEquals(url, expected_url)

    def testmethod_by_industry_specialty(self):
        api.Loans_And_Grants().by_industry_specialty('manufacturing', 'woman')
        url = called_url()
        expected_url = ('http://api.sba.gov/loans_grants/nil/for_profit/'
                        'manufacturing/woman.json')
        self.assertEquals(url, expected_url)

    def testmethod_by_industry_specialty_multiple(self):
        api.Loans_And_Grants().by_industry_specialty('manufacturing',
                'woman-minority')
        url = called_url()
        expected_url = ('http://api.sba.gov/loans_grants/nil/for_profit/'
                        'manufacturing/woman-minority.json')
        self.assertEquals(url, expected_url)

    def testmethod_by_state_industry(self):
        api.Loans_And_Grants().by_state_industry('me', 'manufacturing') 
        url = called_url()
        expected_url = ('http://api.sba.gov/loans_grants/me/for_profit/'
                        'manufacturing/nil.json')
        self.assertEquals(url, expected_url)

    def testmethod_by_state_specialty(self):
        api.Loans_And_Grants().by_state_specialty('ny', 'general_purpose')
        url = called_url()
        expected_url = ('http://api.sba.gov/loans_grants/ny/for_profit/nil/'
                        'general_purpose.json')
        self.assertEquals(url, expected_url)

    def testmethod_by_state_specialty_multiple(self):
        api.Loans_And_Grants().by_state_specialty('ny', 'general_purpose-woman')
        url = called_url()
        expected_url = ('http://api.sba.gov/loans_grants/ny/for_profit/nil/'
                        'general_purpose-woman.json')
        self.assertEquals(url, expected_url)

    def testmethod_by_state_industry_specialty(self):
        api.Loans_And_Grants().by_state_industry_specialty('me',
                'manufacturing', 'woman')
        url = called_url()
        expected_url = ('http://api.sba.gov/loans_grants/me/for_profit/'
                        'manufacturing/woman.json')
        self.assertEquals(url, expected_url)

    def testmethod_by_state_industry_specialty_multiple(self):
        api.Loans_And_Grants().by_state_industry_specialty('me',
                'manufacturing', 'development-woman')
        url = called_url()
        expected_url = ('http://api.sba.gov/loans_grants/me/for_profit/'
                        'manufacturing/development-woman.json')
        self.assertEquals(url, expected_url)


class TestMethod_Recommended_Sites(unittest.TestCase):

    #def __init__(self):
        #url = called_url()
        #expected_url = ('')
        #self.assertEquals(url, expected_url)
        #self.base_url = 'http://api.sba.gov/rec_sites'
    def testmethod_all_sites(self):
        api.Recommended_Sites().all_sites()
        url = called_url()
        expected_url = ('http://api.sba.gov/rec_sites/all_sites/keywords.json')
        self.assertEquals(url, expected_url)

    def testmethod_by_keyword(self):
        api.Recommended_Sites().by_keyword('contracting')
        url = called_url()
        expected_url = ('http://api.sba.gov/rec_sites/keywords/contracting.json')
        self.assertEquals(url, expected_url)

    def testmethod_by_category(self):
        api.Recommended_Sites().by_category('managing a business')
        url = called_url()
        expected_url = ('http://api.sba.gov/rec_sites/category/'
                        'managing%20a%20business.json')
        self.assertEquals(url, expected_url)

    def testmethod_by_master_term(self):
        api.Recommended_Sites().by_master_term('export')
        url = called_url()
        expected_url = ('http://api.sba.gov/rec_sites/keywords/master_term/'
                        'export.json')
        self.assertEquals(url, expected_url)

    def testmethod_by_domain(self):
        api.Recommended_Sites().by_domain('irs')
        url = called_url()
        expected_url = ('http://api.sba.gov/rec_sites/keywords/domain/irs.json')
        self.assertEquals(url, expected_url)


#class TestMethod_City_And_County_Web_Data(unittest.TestCase):

    #def __init__(self):
        #url = called_url()
        #expected_url = ('')
        #self.assertEquals(url, expected_url)
        #self.base_url = 'http://api.sba.gov/geodata'

    #def testmethod_all_urls_by_state(self):
        #url = called_url()
        #expected_url = ('')
        #self.assertEquals(url, expected_url)

    #def testmethod_all_urls_by_county(self):
        #url = called_url()
        #expected_url = ('')
        #self.assertEquals(url, expected_url)

    #def testmethod_primary_urls_by_city(self):
        #url = called_url()
        #expected_url = ('')
        #self.assertEquals(url, expected_url)

    #def testmethod_primary_urls_by_county(self):
        #url = called_url()
        #expected_url = ('')
        #self.assertEquals(url, expected_url)

    #def testmethod_all_data_by_state(self):
        #url = called_url()
        #expected_url = ('')
        #self.assertEquals(url, expected_url)

    #def testmethod_all_data_by_city(self):
        #url = called_url()
        #expected_url = ('')
        #self.assertEquals(url, expected_url)

    #def testmethod_all_data_by_county(self):
        #url = called_url()
        #expected_url = ('')
        #self.assertEquals(url, expected_url)


if __name__ == '__main__':
    unittest.main()
