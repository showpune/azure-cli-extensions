# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements


def load_arguments(self, _):

    with self.argument_context('quota request status list') as c:
        c.argument('scope', type=str, help='The target Azure resource URI.')
        c.argument('filter', options_list=['--filter'], type=str, help='The filter that is applied to packet capture '
                                                                       'request. Multiple filters can be applied')
        c.argument('top', type=int, help='Number of records to return.')
        c.argument('skip_token', type=str, help='SkipToken is only used if a previous operation returned a partial '
                   'result. If a previous response contains a nextLink element, the value of the nextLink element will '
                   'include a skipToken parameter that specifies a starting point to use for subsequent calls.')

    with self.argument_context('quota request status show') as c:
        c.argument('name', type=str, help='Quota request ID.')
        c.argument('scope', type=str, help='The target Azure resource URI.')

    with self.argument_context('quota operation list') as c:
        c.argument('top', type=int, help='An optional query parameter which specifies the maximum number of records to '
                   'be returned by the server.')
        c.argument('skip_token', type=str, help='SkipToken is only used if a previous operation returned a partial '
                   'result. If a previous response contains a nextLink element, the value of the nextLink element will '
                   'include a skipToken parameter that specifies a starting point to use for subsequent calls.')
