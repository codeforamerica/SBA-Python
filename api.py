#!/usr/bin/env python

"""
Python wrapper for the SBA (U.S. Small Business Administration) API.  

SBA API Documentation:  http://developer.usatoday.com/docs/read/Census
"""

try:
    import json
except ImportError:  # pragma: no cover
    # For older versions of Python.
    import simplejson as json

try:
    from urllib import urlencode
except ImportError:  # pragma: no cover
    # For Python 3.
    from urllib.parse import urlencode

try:
    from urllib2 import urlopen
except ImportError:  # pragma: no cover
    # For Python 3.
    from urllib.request import urlopen


class SBA_Wrapper(object):
    """Wrapper for the SBA Loans and Grants API."""

    def __init__(self):
	self.base_url = 'http://api.sba.gov'
	#self.apis_dict = ['license_permit', 'loans_grants', 'rec_sites', 'geodata']
	#business_categories = ['doing business as', 'entity filing', 'employer requirements', 'state licenses', 'tax registration']
	#business_type = ['general business licenses', 'auto dealership', 'barber shop', 'beauty salon', 'child care services', 'construction contractor', 'debt collection agency', 'electrician', 'massage', 'therapist', 'plumber', 'restaurant', 'insurance requirements', 'new hire reporting requirements', 'state tax registration', 'workplace poster requirements']

    def api(self, directory):
	url_list = [self.base_url]
	url_list.append('/%s.json' % directory)
	url = ''.join(url_list)
	#print 'final url' + url
	data = urlopen(url).read()
	return json.loads(data)

    def licenses_permits_category(self, category):
	url = 'license_permit/by_category/%s' % category
	return self.api(url)

    def license_permits_all_by_state(self, state):
	url = 'license_permit/all_by_state/%s' % state 
	return self.api(url)

    def licenses_permits_by_business_type(self, business_type):
	url = 'license_permit/by_business_type/%s' % business_type
	return self.api(url)

    def licenses_permits_by_business_type_state(self, business, state):
	url = 'license_permit/state_only/%s/%s' % (business, state)

    def licenses_permits_by_business_type_state_county(self, business, state, county):
	url = 'license_permit/state_and_county/%s/%s/%s' % (business, state, county)
	return self.api(url)

    def licenses_permits_by_business_type_state_city(self, business, state, city):
	url = 'license_permit/state_and_city/%s/%s/%s' % (business, state, city)
	return self.api(url)

    def licenses_permits_by_business_type_zipcode(self, business, zipcode):
	url = 'license_permit/by_zip/%s/%s' % (business, zipcode)
	return self.api(url)


    def loans_and_grants_federal(self):
	return self.api('loans_grants/federal')

    def loans_and_grants_state(self, state):
	url = 'loans_grants/state_financing_for/%s' % state
	return self.api(url)

    def loans_and_grants_federal_and_state(self, state):
	url = 'loans_grants/federal_and_state_financing_for/%s' % state
	return self.api(url)

    def loans_and_grants_by_industry(self, industry):
	url = 'loans_grants/nil/for_profit/%s/nil' % industry
	return self.api(url)

    def loans_grants_by_speciality(self, specialty):
	url = 'loans_grants/nil/for_profit/nil/%s' % specialty
	return self.api(url)

    def loan_grants_by_industry_specialty(self, industry, specialty):
	url = 'loans_grants/nil/for_profit/%s/%s' % (industry, specialty)
	return self.api(url)

    def loan_grants_by_state_industry(self, state, industry):
	url = 'loans_grants/%s/for_profit/%s/nil' % (state, industry)
	return self.api(url)

    def loan_grants_by_state_specialty(self, state, specialty):
	url = 'loans_grants/%s/for_profit/nil/%s' % (state, specialty)
	return self.api(url)

    def loan_grants_by_state_industry_specialty(self, state, industry, specialty):
	url = 'loans_grants/%s/for_profit/%s/%s' % (state, industry, specialty)
	return self.api(url)


    def sites_by_keyword(self, keyword):
	url = 'rec_sites/keywords/%s' % keyword
	return self.api(url)

    def sites_by_category(self, category):
	url = 'rec_sites/category/%s' % category
	return self.api(url)

    def sites_by_master_term(self, term):
	url = 'rec_sites/keywords/master_term/%s' % term
	return self.api(url)

    def sites_by_domain(self, domain):
	url = 'rec_sites/keywords/domain/%s' % domain
	return self.api(url)


    def city_county_data_urls(self, state, county = None, city = None):
	if county == '_yes' and city == '_yes':
	    url = 'city_county_links_for_state_of/%s' % state
	elif not county and city == '_yes':
	    url = 'city_links_for_state_of/%s' % state
	elif county == '_yes' and not city:
	    url = 'county_links_for_state_of/%s' % state
	elif not county and city:
	    url = 'all_links_for_city_of/%s/%s' % (city, state) 
	elif county and not city:
	    url = 'all_links_for_county_of/%s/%s' % (county, state)
	return self.api('geodata/' + url)
	
    def city_county_data_primary_urls(self, state, county = None, city = None):
	if county == '_yes' and city == '_yes':
	    url = 'primary_city_county_links_for_state_of/%s' % state
	elif not county and city == '_yes':
	    url = 'primary_city_links_for_state_of/%s' % state
	elif county == '_yes' and not city:
	    url = 'primary_county_links_for_state_of/%s' % state
	elif not county and city:
	    url = 'primary_links_for_city_of/%s/%s' % (city, state) 
	elif county and not city:
	    url = 'primary_links_for_county_of/%s/%s' % (county, state)
	return self.api('geodata/' + url)
	  
    def city_county_data_all(self, state, county = None, city = None):
	if county == '_yes' and city == '_yes':
	    url = 'city_county_data_for_state_of/%s' % state
	elif not county and city == '_yes':
	    url = 'city_data_for_state_of/%s' % state
	elif county == '_yes' and not city:
	    url = 'county_data_for_state_of/%s' % state
	elif not county and city:
	    url = 'all_data_for_city_of/%s/%s' % (city, state) 
	elif county and not city:
	    url = 'all_data_for_county_of/%s/%s' % (county, state)
	return self.api('geodata/' + url)
	  
   
