# -*- coding: utf-8 -*-
"""Cisco Spark Organizations API."""


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from builtins import *

from past.builtins import basestring

from ..generator_containers import generator_container
from ..restsession import RestSession
from ..utils import (
    check_type,
    dict_from_items_with_values,
)


__author__ = "Chris Lunsford"
__author_email__ = "chrlunsf@cisco.com"
__copyright__ = "Copyright (c) 2016-2018 Cisco and/or its affiliates."
__license__ = "MIT"


API_ENDPOINT = 'organizations'
OBJECT_TYPE = 'organization'


class OrganizationsAPI(object):
    """Cisco Spark Organizations API.

    Wraps the Cisco Spark Organizations API and exposes the API as native
    Python methods that return native Python objects.

    """

    def __init__(self, session, object_factory):
        """Init a new OrganizationsAPI object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Cisco Spark service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession, may_be_none=False)

        super(OrganizationsAPI, self).__init__()

        self._session = session
        self._object_factory = object_factory

    @generator_container
    def list(self, max=None, **request_parameters):
        """List Organizations.

        This method supports Cisco Spark's implementation of RFC5988 Web
        Linking to provide pagination support.  It returns a generator
        container that incrementally yields all objects returned by the
        query.  The generator will automatically request additional 'pages' of
        responses from Spark as needed until all responses have been returned.
        The container makes the generator safe for reuse.  A new API call will
        be made, using the same parameters that were specified when the
        generator was created, every time a new iterator is requested from the
        container.

        Args:
            max(int): Limit the maximum number of items returned from the Spark
                service per request.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            GeneratorContainer: A GeneratorContainer which, when iterated,
                yields the organizations returned by the Cisco Spark query.

        Raises:
            TypeError: If the parameter types are incorrect.
            SparkApiError: If the Cisco Spark cloud returns an error.

        """
        check_type(max, int)

        params = dict_from_items_with_values(
            request_parameters,
            max=max,
        )

        # API request - get items
        items = self._session.get_items(API_ENDPOINT, params=params)

        # Yield organization objects created from the returned JSON objects
        for item in items:
            yield self._object_factory(OBJECT_TYPE, item)

    def get(self, orgId):
        """Get the details of an Organization, by ID.

        Args:
            orgId(basestring): The ID of the Organization to be retrieved.

        Returns:
            Organization: An Organization object with the details of the
                requested organization.

        Raises:
            TypeError: If the parameter types are incorrect.
            SparkApiError: If the Cisco Spark cloud returns an error.

        """
        check_type(orgId, basestring, may_be_none=False)

        # API request
        json_data = self._session.get(API_ENDPOINT + '/' + orgId)

        # Return a organization object created from the returned JSON object
        return self._object_factory(OBJECT_TYPE, json_data)
