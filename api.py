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
    """WRapper for SBA APIs."""

    def __init__(self):
        """Base URLs should have no '/' at the end"""
        self.base_url = 'http://api.sba.gov'

    def call_api(self, directory):
        url_list = [self.base_url]
        # Use urllib.quote to replace spaces with %20
        url_list.append('/%s.json' % quote(str(directory)))
        url = ''.join(url_list)
        data = urlopen(url).read()
        return json.loads(data)


class Licenses_And_Permits(SBA_API):
    """Wrapper for the SBA Licenses and Permits API.
    http://www.sba.gov/about-sba-services/7615
    """

    def __init__(self):
        self.base_url = 'http://api.sba.gov/license_permit'

    def by_category(self, category):
        """
        Returns results for a matching license or permit category for each 54
        states and territories.

        @param category [String] One of the following categories:
        doing business as, entity filing, employer requirements,
        states licenses, tax registration

        @see http://www.sba.gov/content/business-licenses-permits-api-category-method

        >>> api.Licenses_And_Permits().by_category('doing business as')
        """
        url = 'by_category/%s' % category
        return self.call_api(url)

    def by_state(self, state):
        """
        Returns all business licenses for all business types required to
        operate in an specific state or territory.

        @param state [String] Input the two letter postal code for the state
        abbreviation.

        @see http://www.sba.gov/content/business-licenses-permits-api-state-method

        >>> api.Licenses_And_Permits().by_state('ca')
        """
        url = 'all_by_state/%s' % state
        return self.call_api(url)

    def by_business_type(self, business_type):
        """
        Returns business licenses and permits required for a specific type of
        business for all 54 states and territories

        @param business [String] The business parameter includes standard
        values that allow you to return license and permit information for a
        specific type of business or for specific employer requirements
        Allowed values: 'general business licenses', 'auto dealership',
        'barber shop', 'beauty salon', 'child care services',
        'construction contractor', 'debt collection agency', 'electrician',
        'massage', 'therapist', 'plumber', 'restaurant',
        'insurance requirements', 'new hire reporting requirements',
        'state tax registration', 'workplace poster requirements'

        @see http://www.sba.gov/content/business-licenses-permits-api-business-type-method

        >>> api.Licenses_And_Permits().by_business_type('general business license')

        """
        url = 'by_business_type/%s' % business_type
        return self.call_api(url)

    def by_business_type_state(self, business, state):
        """
        Returns business licenses and permits required for a specific type of
        business in a specific state.

        @param business [String] The business parameter includes standard
        values that allow you to return license and permit information for a
        specific type of business or for specific employer requirements
        Allowed values: 'general business licenses', 'auto dealership',
        'barber shop', 'beauty salon', 'child care services',
        'construction contractor', 'debt collection agency', 'electrician',
        'massage', 'therapist', 'plumber', 'restaurant',
        'insurance requirements', 'new hire reporting requirements',
        'state tax registration', 'workplace poster requirements'
        @param state [String] Input the two letter postal code for the state
        abbreviation.

        @see http://www.sba.gov/content/business-licenses-permits-api-business-type-and-state-method

        >>> api.Licenses_And_Permits().by_business_type_state(
                'child care services', 'va')
        """
        url = 'state_only/%s/%s' % (business, state)
        return self.call_api(url)

    def by_business_type_state_county(self, business, state, county):
        """
        Returns business licenses and permits required for a specific type of
        business in a specific state and county.

        @param business [String] The business parameter includes standard
        values that allow you to return license and permit information for a
        specific type of business or for specific employer requirements.
        Allowed values: 'general business licenses', 'auto dealership',
        'barber shop', 'beauty salon', 'child care services',
        'construction contractor', 'debt collection agency', 'electrician',
        'massage', 'therapist', 'plumber', 'restaurant',
        'insurance requirements', 'new hire reporting requirements',
        'state tax registration', 'workplace poster requirements'
        @param state [String] Input the two letter postal code for the state
        abbreviation.
        @param county [String] Input the name of the county (or its
        equivalent).  County (or equivalent) name should including the word "
        county" (or "parish" etc.)  For example, input Orange County, not Orange.

        @see http://www.sba.gov/content/business-licenses-permits-api-business-type-state-and-county-method

        >>> api.Licenses_And_Permits().by_business_type_state_county(
                'child care services', 'ca', 'los angeles county')
        """
        url = 'state_and_county/%s/%s/%s' % (business, state, county)
        return self.call_api(url)

    def by_business_type_state_city(self, business, state, city):
        """
        Returns business licenses and permits required for a specific type of
        business in a specific state and city

        @param business [String] The business parameter includes standard
        values that allow you to return license and permit information for a
        specific type of business or for specific employer requirements.
        Allowed values: 'general business licenses', 'auto dealership',
        'barber shop', 'beauty salon', 'child care services',
        'construction contractor', 'debt collection agency', 'electrician',
        'massage', 'therapist', 'plumber', 'restaurant',
        'insurance requirements', 'new hire reporting requirements',
        'state tax registration', 'workplace poster requirements'
        @param state [String] Input the two letter postal code for the state
        abbreviation.
        @param city [String] Input the name of the City.

        @see http://www.sba.gov/content/business-licenses-permits-api-business-type-state-and-city-method

        >>> api.Licenses_And_Permits().by_business_type_state_city(
                'restaurant', 'ny', 'albany')
        """
        url = 'state_and_city/%s/%s/%s' % (business, state, city)
        return self.call_api(url)

    def by_business_type_zipcode(self, business, zipcode):
        """
        Returns business licenses and permits required for a specific type of
        business in a specific zip code

        @param business [String] The business parameter includes standard
        values that allow you to return license and permit information for a
        specific type of business or for specific employer requirements.
        Allowed values: 'general business licenses', 'auto dealership',
        'barber shop', 'beauty salon', 'child care services',
        'construction contractor', 'debt collection agency', 'electrician',
        'massage', 'therapist', 'plumber', 'restaurant',
        'insurance requirements', 'new hire reporting requirements',
        'state tax registration', 'workplace poster requirements'
        @param zip [String] Input a valid five digit zip code.

        @see http://www.sba.gov/content/business-licenses-permits-api-business-type-state-and-city-method

        >>> api.Licenses_And_Permits().by_business_type_zipcode('restaurant',
                '49684')
        """
        url = 'by_zip/%s/%s' % (business, str(zipcode))
        return self.call_api(url)


class Loans_And_Grants(SBA_API):
    """Wrapper for the SBA Licenses and Permits API.
    http://www.sba.gov/about-sba-services/7615
    """

    def __init__(self):
        self.base_url = 'http://api.sba.gov/loans_grants'

    def federal(self):
        """
        Returns financing programs available from Federal government agencies
        and select non-profit organizations nationwide.

        @see http://www.sba.gov/content/loans-grants-search-api-federal-program-method

        >>> api.Loans_And_Grants().federal()
        """
        return self.call_api('federal')

    def state(self, state):
        """
        Returns all small business financing programs sponsored by state
        government agencies and select non-profit and commercial organizations.

        @param state [String] input the two leter postal code for the state abbreviation

        @see http://www.sba.gov/content/loans-grants-search-api-programs-specific-state-method

        >>> api.Loans_And_Grants().state('ia')
        """
        url = 'state_financing_for/%s' % state
        return self.call_api(url)

    def federal_and_state(self, state):
        """
        Returns all small business financing programs sponsored by federal
        and state government agencies and selected non-profit and commercial
        organizations.

        @param state [String] input the two leter postal code for the state
        abbreviation

        @see http://www.sba.gov/content/loans-grants-search-api-federal-and-state-specific-method
        >>>  api.Loans_And_Grants().federal_and_state('me')
        """
        url = 'federal_and_state_financing_for/%s' % state
        return self.call_api(url)

    def by_industry(self, industry):
        """
        Returns all small business financing programs for a specific industry
        in all 54 states and territories (when available).

        @param industry [String] input one of the standard industry values:
        'agriculture', 'child care', 'environmental management', 'health care',
        'manufacturing', 'technology', 'tourism'

        @see http://www.sba.gov/content/loans-grants-search-api-industry-method

        >>> api.Loans_And_Grants().by_industry('manufacturing')
        """
        url = 'nil/for_profit/%s/nil' % industry
        return self.call_api(url)

    def by_speciality(self, specialty):
        """
        Returns small business special financing programs for certain business owner
        groups (e.g., women, veterans, minorities, etc.); or business activities
        (e.g., export, energy efficiency, disaster assistance, etc.).

        @param specialty [String] input one or more of the standard industry
        values. Multiple specialities should be separated by dashes. Specialties:
        'general_purpose', 'development', 'exporting', 'contractor', 'green',
        'military', 'minority', 'woman', 'disabled', 'rural', 'disaster'

        @see http://www.sba.gov/content/loans-grants-search-api-specialty-method

        >>> api.Loans_And_Grants().by_speciality('woman')
        >>> api.Loans_And_Grants().by_speciality('woman-general_purpose')
        """
        url = 'nil/for_profit/nil/%s' % specialty
        return self.call_api(url)

    def by_industry_specialty(self, industry, specialty):
        """
        Returns financing programs for specific industries AND specific business
        groups (e.g., women, veterans, minorities, etc.); or business activities
        (e.g., export, energy efficiency, disaster assistance, etc.).

        @param industry [String] input one of the standard industry values:
        'agriculture', 'child care', 'environmental management', 'health care',
        'manufacturing', 'technology', 'tourism'
        @param specialty [String] input one or more of the standard industry
        values. Multiple specialities should be separated by dashes. Specialties:
        'general_purpose', 'development', 'exporting', 'contractor', 'green',
        'military', 'minority', 'woman', 'disabled', 'rural', 'disaster'

        @see http://www.sba.gov/content/loans-grants-search-api-industry-and-specialty-method
        >>> api.Loans_And_Grants().by_industry_specialty('manufacturing', 'woman')
        >>> api.Loans_And_Grants().by_industry_specialty('manufacturing',
                'woman-minority')
        """
        url = 'nil/for_profit/%s/%s' % (industry, specialty)
        return self.call_api(url)

    def by_state_industry(self, state, industry):
        """
        Returns all small business financing programs for a specific industry
        in a specific state.

        @param state [String]  input the two leterl postal code for state abbreviation
        @param industry [String] input one of the standard industry values:
        'agriculture', 'child care', 'environmental management', 'health care',
        'manufacturing', 'technology', 'tourism'

        @see http://www.sba.gov/content/loans-grants-search-api-state-and-industry-method

        >>> api.Loans_And_Grants().by_state_industry('me', 'manufacturing')
        """
        url = '%s/for_profit/%s/nil' % (state, industry)
        return self.call_api(url)

    def by_state_specialty(self, state, specialty):
        """
        Returns state programs for specific business groups or specialized
        business activities.

        @param state [String]  input the two leterl postal code for state abbreviation
        @param specialty [String] input one or more of the standard industry
        values. Multiple specialities should be separated by dashes. Specialties:
        'general_purpose', 'development', 'exporting', 'contractor', 'green',
        'military', 'minority', 'woman', 'disabled', 'rural', 'disaster'

        @see http://www.sba.gov/content/loans-grants-search-api-state-and-specialty-method

        >>> api.Loans_And_Grants().by_state_specialty('ny', 'general_purpose')
        >>> api.Loans_And_Grants().by_state_specialty('ny'
                'general_purpose-woman')
        >>> api.Loans_And_Grants().by_industry_specialty('manufacturing',
                'woman-minority')
        """
        url = '%s/for_profit/nil/%s' % (state, specialty)
        return self.call_api(url)

    def by_state_industry_specialty(self, state, industry, specialty):
        """
        Returns state programs by industry and specific business groups or
        specialized business activities.

        @param state [String]  input the two letter postal code for state abbreviation
        @param industry [String] input one of the standard industry values:
        'agriculture', 'child care', 'environmental management', 'health care',
        'manufacturing', 'technology', 'tourism'
        @param specialty [String] input one or more of the standard industry
        values. Multiple specialities should be separated by dashes. Specialties:
        'general_purpose', 'development', 'exporting', 'contractor', 'green',
        'military', 'minority', 'woman', 'disabled', 'rural', 'disaster'

        @see http://www.sba.gov/content/loans-grants-search-api-state-industry-and-specialty-method
        >>> api.Loans_And_Grants().by_state_industry_specialty('me',
                'manufacturing', 'woman')

        >>> api.Loans_And_Grants().by_state_industry_specialty('me',
                'manufacturing', 'development-woman')
        """
        url = '%s/for_profit/%s/%s' % (state, industry, specialty)
        return self.call_api(url)


class Recommended_Sites(SBA_API):
    """Wrapper for the SBA Licenses and Permits API.
    http://www.sba.gov/about-sba-services/7630
    """

    def __init__(self):
        self.base_url = 'http://api.sba.gov/rec_sites'

    def all_sites(self):
        """
        Returns all recommended sites for all keywords and phrases.

        @see http://www.sba.gov/about-sba-services/7630#all

        >>> api.Recommended_Sites().all_sites()
        """
        return self.call_api('all_sites/keywords')

    def by_keyword(self, keyword):
        """
        Returns all recommended sites for a specific keyword.

        @param keyword [String] A search word or phrase.

        @see http://www.sba.gov/about-sba-services/7630#keyword

        >>> api.Recommended_Sites().by_keyword('contracting')
        """
        url = 'keywords/%s' % keyword
        return self.call_api(url)

    def by_category(self, category):
        """
        Returns all recommended sites for a specific category.

        @param category [String] Name of standard category.

        @see http://www.sba.gov/about-sba-services/7630#category

        >>> api.Recommended_Sites().by_category('managing a business')
        """
        url = 'category/%s' % category
        return self.call_api(url)

    def by_master_term(self, term):
        """
        Returns all recommended sites assigned a specific master term.

        @param term [String] A standard search word or phrase assigned to
        group of synonyms

        @see http://www.sba.gov/about-sba-services/7630#master

        >>> api.Recommended_Sites().by_master_term('export')
        """
        url = 'keywords/master_term/%s' % term
        return self.call_api(url)

    def by_domain(self, domain):
        """
        Returns all recommended sites belonging to a specific domain

        @param domain [String] Domain name without the www or .com, .gov, .net

        @see http://www.sba.gov/about-sba-services/7630#domain

        >>> api.Recommended_Sites().by_domain('irs')
        """
        url = 'keywords/domain/%s' % domain
        return self.call_api(url)


class City_And_County_Web_Data(SBA_API):
    """Wrapper for the SBA Licenses and Permits API.
    http://www.sba.gov/about-sba-services/7617
    """

    def __init__(self):
        self.base_url = 'http://api.sba.gov/geodata'

    def all_urls_by_state(self, state, show_county, show_city):
        """
        Returns city and county geographic data from GNIS and all associated
        URLs (many city and county governments have multiple web sites) for a
        given state. If both show_county and show_city are set to False, this
        method will default to showing URLs for both cities and counties in
        the given state.

        @param state [String] The two letter postal code for the state abbreviation.
        @param show_county [Boolean] Show URLs for counties in given state.
        @param show_city [Boolean] Show URLs for cities in given state.

        @see http://www.sba.gov/content/us-city-and-county-web-data-api-city-county-data-all-urls

        >>> api.City_And_County_Web_Data().all_urls_by_state('mi', True, True)
        >>> api.City_And_County_Web_Data().all_urls_by_state('mi', True, False)
        >>> api.City_And_County_Web_Data().all_urls_by_state('tx', False, True)
        """
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
        Returns All County URLS in a State

        @param state [String] The two letter postal code for the state abbreviation.
        @param county [String] Input the name of the county (or its equivalent), including the word county in the name

        @see http://www.sba.gov/content/us-city-and-county-web-data-api-city-county-data-all-urls

        >>> api.City_And_County_Web_Data().all_urls_by_county('ca',
                'orange county')
        """
        url = 'all_links_for_county_of/%s/%s' % (county, state)
        return self.call_api(url)

    def all_urls_by_city(self, state, city):
        """
        Returns All City URLS in a State

        @param state [String] The two letter postal code for the state abbreviation.
        @param city [String] Input the name of the city, town or village.

        @see http://www.sba.gov/content/us-city-and-county-web-data-api-city-county-data-all-urls

        >>> api.City_And_County_Web_Data().all_urls_by_city('tx', 'dallas')
        """
        url = 'all_links_for_city_of/%s/%s' % (city, state)
        return self.call_api(url)

    def primary_urls_by_state(self, state, show_county, show_city):
        """
        Returns only primary URLS. A primary URL is the official government
        website for a city or county government. If a city or county
        government has more than one domain or URL, one URL has been tagged
        as the primary city or county URL. If both show_county and show_city
        are set to False, this method will default to showing URLs for both
        cities and counties in the given state.

        @param state [String] The two letter postal code for the state abbreviation.
        @param show_county [Boolean] Show primary URLs for counties in given state.
        @param show_city [Boolean] Show primary URLs for cities in given state.

        @see http://www.sba.gov/content/us-city-and-county-web-data-api-city-county-data-all-urls

        >>> api.City_And_County_Web_Data().primary_urls_by_state('mi', True, True)
        >>> api.City_And_County_Web_Data().primary_urls_by_state('mi', True, False)
        >>> api.City_And_County_Web_Data().primary_urls_by_state('tx', False, True)
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
        """Returns the primary URL for a specific County

        @param county [String] Input the name of the county (or its equivalent), including the word county in the name
        @param state [String] The two letter postal code for the state abbreviation.

        @see http://www.sba.gov/content/us-city-and-county-web-data-api-city-county-data-primary-methods#county

        >>> api.City_And_County_Web_Data().primary_urls_by_county('wa',
                'king county')
        """
        url = 'primary_links_for_county_of/%s/%s' % (county, state)
        return self.call_api(url)

    def primary_url_for_city(self, state, city):
        """Returns the primary URL for a specific city

        @param state [String] The two letter postal code for the state abbreviation.
        @param city [String] Input the name of the city, town or village.

        @see http://www.sba.gov/content/us-city-and-county-web-data-api-city-county-data-primary-methods#city

        >>> api.City_And_County_Web_Data().primary_url_for_city('tx', 'dallas')
        """
        url = 'primary_links_for_city_of/%s/%s' % (city, state)
        return self.call_api(url)

    def all_data_by_state(self, state, show_county, show_city):
        """
        Returns data for city and counties, including those that do not
        have URLs associated with them, in a given state. If both show_county
        and show_city are set to False, this method will default to showing
        URLs for both cities and counties in the given state.

        @param state [String] The two letter postal code for the state abbreviation.
        @param show_county [Boolean] Show data for counties in given state.
        @param show_city [Boolean] Show data for cities in given state.

        @see http://www.sba.gov/content/us-city-and-county-web-data-api-city-county-data-all-urls

        >>> api.City_And_County_Web_Data().all_data_by_state('ca', True, True)
        >>> api.City_And_County_Web_Data().all_data_by_state('mi', True, False)
        >>> api.City_And_County_Web_Data().all_data_by_state('tx', False, True)
        """
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
        Returns Data for a specific City

        @param city [String] Input the name of the city, town or village.
        @param state [String] The two letter postal code for the state abbreviation.

        @see http://www.sba.gov/content/us-city-and-county-web-data-api-city-county-data-all-data-methods

        >>> api.City_And_County_Web_Data().all_data_by_city('wa', 'seattle')
        """
        url = 'all_data_for_city_of/%s/%s' % (city, state)
        return self.call_api(url)

    def all_data_by_county(self, state, county):
        """
        Returns Data for a specific County

        @param county [String]  Input the name of the County
        @param state [String]  Input the two leter postal code for state abbreviation.

        @see http://www.sba.gov/content/us-city-and-county-web-data-api-city-county-data-all-data-methods

        >>> api.City_And_County_Web_Data().all_data_by_county('md',
               'frederick county')
        """
        url = 'all_data_for_county_of/%s/%s' % (county, state)
        return self.call_api(url)
