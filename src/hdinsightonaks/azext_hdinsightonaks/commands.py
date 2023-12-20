# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):  # pylint: disable=unused-argument

    hdinsightonaks_cluster_sdk = CliCommandType(
        operations_tmpl='azext_hdinsightonaks.custom#{}')

    with self.command_group('hdinsight-on-aks', hdinsightonaks_cluster_sdk) as g:
        g.command('cluster node-profile create', 'create_compute_node_profile', is_preview=True)
        g.command('cluster trino-hive-catalog create', 'create_trino_hive_catalog', is_preview=True)
        g.command('cluster secret create', 'create_secret_reference', is_preview=True)
