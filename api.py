#!/usr/bin/env python

"""
Python wrapper for the SBA (U.S. Small Business Administration) API.

SBA API Documentation: http://www.sba.gov/api/
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
    from urllib import quote
except ImportError:  # pragma: no cover
    # For Python 3.
    from urllib.parse import quote

try:
    from urllib2 import urlopen
except ImportError:  # pragma: no cover
    # For Python 3.
    from urllib.request import urlopen


class SBA_API(object):
    """Wrapper for the SBA Loans and Grants API."""

    def __init__(self):
        self.base_url = 'http://api.sba.gov'
        #self.apis_dict = ['license_permit', 'loans_grants', 'rec_sites', 'geodata']
        #business_categories = ['doing business as', 'entity filing', 'employer requirements', 'state licenses', 'tax registration']
        #business_type = ['general business licenses', 'auto dealership', 'barber shop', 'beauty salon', 'child care services', 'construction contractor', 'debt collection agency', 'electrician', 'massage', 'therapist', 'plumber', 'restaurant', 'insurance requirements', 'new hire reporting requirements', 'state tax registration', 'workplace poster requirements']

    def call_api(self, directory):
        url_list = [self.base_url]
        # Use urllib.quote to replace spaces with %20
        url_list.append('/%s.json' % quote(str(directory)))
        url = ''.join(url_list)
        #print 'final url', url
        data = urlopen(url).read()
        return json.loads(data)

class Licenses_And_Permits(SBA_API):

    def __init__(self):
        self.base_url = 'http://api.sba.gov/license_permit'

    def by_category(self, state):
        url = 'by_category/%s' % state
        return self.call_api(url)

    def by_state(self, state):
        url = 'all_by_state/%s' % state
        return self.call_api(url)

    def by_business_type(self, business_type):
        url = 'by_business_type/%s' % business_type
        return self.call_api(url)

    def by_business_type_state(self, business, state):
        url = 'state_only/%s/%s' % (business, state)
        return self.call_api(url)

    def by_business_type_state_county(self, business, state, county):
        url = 'state_and_county/%s/%s/%s' % (business, state, county)
        return self.call_api(url)

    def by_business_type_state_city(self, business, state, city):
        url = 'state_and_city/%s/%s/%s' % (business, state, city)
        return self.call_api(url)

    def by_business_type_zipcode(self, business, zipcode):
        url = 'by_zip/%s/%s' % (business, str(zipcode))
        return self.call_api(url)


class Loans_And_Grants(SBA_API):

    def __init__(self):
        self.base_url = 'http://api.sba.gov/loans_grants'

    def federal(self):
        return self.call_api('federal')

    def state(self, state):
        url = 'state_financing_for/%s' % state
        return self.call_api(url)

    def federal_and_state(self, state):
        url = 'federal_and_state_financing_for/%s' % state
        return self.call_api(url)

    def by_industry(self, industry):
        url = 'nil/for_profit/%s/nil' % industry
        return self.call_api(url)

    def by_speciality(self, specialty):
        url = 'nil/for_profit/nil/%s' % specialty
        return self.call_api(url)

    def by_industry_specialty(self, industry, specialty):
        url = 'nil/for_profit/%s/%s' % (industry, specialty)
        return self.call_api(url)

    def by_state_industry(self, state, industry):
        url = '%s/for_profit/%s/nil' % (state, industry)
        return self.call_api(url)

    def by_state_specialty(self, state, specialty):
        url = '%s/for_profit/nil/%s' % (state, specialty)
        return self.call_api(url)

    def by_state_industry_specialty(self, state, industry, specialty):
        url = '%s/for_profit/%s/%s' % (state, industry, specialty)
        return self.call_api(url)


class Recommended_Sites(SBA_API):

    def __init__(self):
        self.base_url = 'http://api.sba.gov/rec_sites'

    def all_sites(self):
        return self.call_api('all_sites/keywords')

    def by_keyword(self, keyword):
        url = 'keywords/%s' % keyword
        return self.call_api(url)

    def by_category(self, category):
        url = 'category/%s' % category
        return self.call_api(url)

    def by_master_term(self, term):
        url = 'keywords/master_term/%s' % term
        return self.call_api(url)

    def by_domain(self, domain):
        url = 'keywords/domain/%s' % domain
        return self.call_api(url)


class City_And_County_Web_Data(SBA_API):

    def __init__(self):
        self.base_url = 'http://api.sba.gov/geodata'

    def all_urls_by_state(self, state, show_county, show_city):
        if show_county and show_city:
            url = 'city_county_links_for_state_of/%s' % state
        elif not show_county and show_city:
            url = 'city_links_for_state_of/%s' % state
        elif show_county and not show_city:
            url = 'county_links_for_state_of/%s' % state
        else:
            url = 'city_county_links_for_state_of/%s' % state
        return self.call_api(url)

    def all_urls_by_county(self, state, county):
        """
        Semi-internal method for calling USA Today's Census API. Most of the
        other methods rely on this method.

        >>> Census().api('locations', keypat='KY')
        """
        url = 'all_links_for_county_of/%s/%s' % (county, state)
        return self.call_api(url)

    def all_urls_by_city(self, state, city):
        url = 'all_links_for_city_of/%s/%s' % (city, state)
        return self.call_api(url)

    def primary_urls_by_state(self, state, show_county, show_city):
        """
        Semi-internal method for calling USA Today's Census API. Most of the
        other methods rely on this method.

        >>> Census().api('locations', keypat='KY')
        """
        if show_county and show_city:
            url = 'primary_city_county_links_for_state_of/%s' % state
        elif show_county and not show_city:
            url = 'primary_county_links_for_state_of/%s' % state
        elif not show_county and show_city:
            url = 'primary_city_links_for_state_of/%s' % state
        else:
            url = 'primary_city_county_links_for_state_of/%s' % state
        return self.call_api(url)

    def primary_urls_by_county(self, state, county):
        url = 'primary_links_for_county_of/%s/%s' % (county, state)
        return self.call_api(url)

    def primary_urls_by_city(self, state, city):
        url = 'primary_links_for_city_of/%s/%s' % (city, state)
        return self.call_api(url)

    def all_data_by_state(self, state, show_county, show_city):
        if show_county and show_city:
            url = 'city_county_data_for_state_of/%s' % state
        elif show_county and not show_city:
            url = 'county_data_for_state_of/%s' % state
        elif not show_county and show_city:
            url = 'city_data_for_state_of/%s' % state
        else:
            url = 'city_county_data_for_state_of/%s' % state
        return self.call_api(url)

    def all_data_by_city(self, state, city):
        """
        Semi-internal method for calling USA Today's Census API. Most of the
        other methods rely on this method.

        >>> Census().api('locations', keypat='KY')
        """
        url = 'all_data_for_city_of/%s/%s' % (city, state)
        return self.call_api(url)

    def all_data_by_county(self, state, county):
        url = 'all_data_for_county_of/%s/%s' % (county, state)
        return self.call_api(url)

#Licenses_And_Permits().by_category('doing business as')
