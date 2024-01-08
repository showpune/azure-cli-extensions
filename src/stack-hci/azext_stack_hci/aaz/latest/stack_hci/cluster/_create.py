# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "stack-hci cluster create",
)
class Create(AAZCommand):
    """Create an HCI cluster.

    :example: Create cluster
        az stack-hci cluster create --location "East US" --aad-client-id "24a6e53d-04e5-44d2-b7cc-1b732a847dfc" --aad-tenant-id "7e589cc1-a8b6-4dff-91bd-5ec0fa18db94" --endpoint "https://98294836-31be-4668-aeae-698667faf99b.waconazure.com" --name "myCluster" --resource- group "test-rg"
    """

    _aaz_info = {
        "version": "2023-08-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.azurestackhci/clusters/{}", "2023-08-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.cluster_name = AAZStrArg(
            options=["-n", "--name", "--cluster-name"],
            help="The name of the cluster.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Cluster"

        _args_schema = cls._args_schema
        _args_schema.identity = AAZObjectArg(
            options=["--identity"],
            arg_group="Cluster",
            help="Identity of Cluster resource",
        )
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Cluster",
            help="The geo-location where the resource lives",
            required=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Cluster",
            help="Resource tags.",
        )

        identity = cls._args_schema.identity
        identity.type = AAZStrArg(
            options=["type"],
            help="Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).",
            required=True,
            enum={"None": "None", "SystemAssigned": "SystemAssigned", "SystemAssigned, UserAssigned": "SystemAssigned, UserAssigned", "UserAssigned": "UserAssigned"},
        )
        identity.user_assigned_identities = AAZDictArg(
            options=["user-assigned-identities"],
            help="The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.",
        )

        user_assigned_identities = cls._args_schema.identity.user_assigned_identities
        user_assigned_identities.Element = AAZObjectArg(
            blank={},
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.aad_application_object_id = AAZStrArg(
            options=["--aad-application-object-id"],
            arg_group="Properties",
            help="Object id of cluster AAD identity.",
        )
        _args_schema.aad_client_id = AAZStrArg(
            options=["--aad-client-id"],
            arg_group="Properties",
            help="App id of cluster AAD identity.",
        )
        _args_schema.aad_service_principal_object_id = AAZStrArg(
            options=["--aad-service-principal-object-id"],
            arg_group="Properties",
            help="Id of cluster identity service principal.",
        )
        _args_schema.aad_tenant_id = AAZStrArg(
            options=["--aad-tenant-id"],
            arg_group="Properties",
            help="Tenant id of cluster AAD identity.",
        )
        _args_schema.endpoint = AAZStrArg(
            options=["--endpoint"],
            arg_group="Properties",
            help="Endpoint configured for management from the Azure portal.",
        )
        _args_schema.desired_properties = AAZObjectArg(
            options=["--desired-properties"],
            arg_group="Properties",
            help="Desired properties of the cluster.",
        )

        desired_properties = cls._args_schema.desired_properties
        desired_properties.diagnostic_level = AAZStrArg(
            options=["diagnostic-level"],
            help="Desired level of diagnostic data emitted by the cluster.",
            enum={"Basic": "Basic", "Enhanced": "Enhanced", "Off": "Off"},
        )
        desired_properties.windows_server_subscription = AAZStrArg(
            options=["windows-server-subscription"],
            help="Desired state of Windows Server Subscription.",
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ClustersCreate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ClustersCreate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AzureStackHCI/clusters/{clusterName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "clusterName", self.ctx.args.cluster_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-08-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("identity", AAZObjectType, ".identity")
            _builder.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            identity = _builder.get(".identity")
            if identity is not None:
                identity.set_prop("type", AAZStrType, ".type", typ_kwargs={"flags": {"required": True}})
                identity.set_prop("userAssignedIdentities", AAZDictType, ".user_assigned_identities")

            user_assigned_identities = _builder.get(".identity.userAssignedIdentities")
            if user_assigned_identities is not None:
                user_assigned_identities.set_elements(AAZObjectType, ".")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("aadApplicationObjectId", AAZStrType, ".aad_application_object_id")
                properties.set_prop("aadClientId", AAZStrType, ".aad_client_id")
                properties.set_prop("aadServicePrincipalObjectId", AAZStrType, ".aad_service_principal_object_id")
                properties.set_prop("aadTenantId", AAZStrType, ".aad_tenant_id")
                properties.set_prop("cloudManagementEndpoint", AAZStrType, ".endpoint")
                properties.set_prop("desiredProperties", AAZObjectType, ".desired_properties")

            desired_properties = _builder.get(".properties.desiredProperties")
            if desired_properties is not None:
                desired_properties.set_prop("diagnosticLevel", AAZStrType, ".diagnostic_level")
                desired_properties.set_prop("windowsServerSubscription", AAZStrType, ".windows_server_subscription")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.identity = AAZObjectType()
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType(
                flags={"required": True},
            )
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.aad_application_object_id = AAZStrType(
                serialized_name="aadApplicationObjectId",
            )
            properties.aad_client_id = AAZStrType(
                serialized_name="aadClientId",
            )
            properties.aad_service_principal_object_id = AAZStrType(
                serialized_name="aadServicePrincipalObjectId",
            )
            properties.aad_tenant_id = AAZStrType(
                serialized_name="aadTenantId",
            )
            properties.billing_model = AAZStrType(
                serialized_name="billingModel",
                flags={"read_only": True},
            )
            properties.cloud_id = AAZStrType(
                serialized_name="cloudId",
                flags={"read_only": True},
            )
            properties.cloud_management_endpoint = AAZStrType(
                serialized_name="cloudManagementEndpoint",
            )
            properties.connectivity_status = AAZStrType(
                serialized_name="connectivityStatus",
                flags={"read_only": True},
            )
            properties.desired_properties = AAZObjectType(
                serialized_name="desiredProperties",
            )
            properties.isolated_vm_attestation_configuration = AAZObjectType(
                serialized_name="isolatedVmAttestationConfiguration",
            )
            properties.last_billing_timestamp = AAZStrType(
                serialized_name="lastBillingTimestamp",
                flags={"read_only": True},
            )
            properties.last_sync_timestamp = AAZStrType(
                serialized_name="lastSyncTimestamp",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.registration_timestamp = AAZStrType(
                serialized_name="registrationTimestamp",
                flags={"read_only": True},
            )
            properties.reported_properties = AAZObjectType(
                serialized_name="reportedProperties",
            )
            properties.resource_provider_object_id = AAZStrType(
                serialized_name="resourceProviderObjectId",
                flags={"read_only": True},
            )
            properties.service_endpoint = AAZStrType(
                serialized_name="serviceEndpoint",
                flags={"read_only": True},
            )
            properties.software_assurance_properties = AAZObjectType(
                serialized_name="softwareAssuranceProperties",
            )
            properties.status = AAZStrType(
                flags={"read_only": True},
            )
            properties.trial_days_remaining = AAZFloatType(
                serialized_name="trialDaysRemaining",
                flags={"read_only": True},
            )

            desired_properties = cls._schema_on_200.properties.desired_properties
            desired_properties.diagnostic_level = AAZStrType(
                serialized_name="diagnosticLevel",
            )
            desired_properties.windows_server_subscription = AAZStrType(
                serialized_name="windowsServerSubscription",
            )

            isolated_vm_attestation_configuration = cls._schema_on_200.properties.isolated_vm_attestation_configuration
            isolated_vm_attestation_configuration.attestation_resource_id = AAZStrType(
                serialized_name="attestationResourceId",
                flags={"read_only": True},
            )
            isolated_vm_attestation_configuration.attestation_service_endpoint = AAZStrType(
                serialized_name="attestationServiceEndpoint",
                flags={"read_only": True},
            )
            isolated_vm_attestation_configuration.relying_party_service_endpoint = AAZStrType(
                serialized_name="relyingPartyServiceEndpoint",
                flags={"read_only": True},
            )

            reported_properties = cls._schema_on_200.properties.reported_properties
            reported_properties.cluster_id = AAZStrType(
                serialized_name="clusterId",
                flags={"read_only": True},
            )
            reported_properties.cluster_name = AAZStrType(
                serialized_name="clusterName",
                flags={"read_only": True},
            )
            reported_properties.cluster_type = AAZStrType(
                serialized_name="clusterType",
                flags={"read_only": True},
            )
            reported_properties.cluster_version = AAZStrType(
                serialized_name="clusterVersion",
                flags={"read_only": True},
            )
            reported_properties.diagnostic_level = AAZStrType(
                serialized_name="diagnosticLevel",
            )
            reported_properties.imds_attestation = AAZStrType(
                serialized_name="imdsAttestation",
                flags={"read_only": True},
            )
            reported_properties.last_updated = AAZStrType(
                serialized_name="lastUpdated",
                flags={"read_only": True},
            )
            reported_properties.manufacturer = AAZStrType(
                flags={"read_only": True},
            )
            reported_properties.nodes = AAZListType(
                flags={"read_only": True},
            )
            reported_properties.oem_activation = AAZStrType(
                serialized_name="oemActivation",
                flags={"read_only": True},
            )
            reported_properties.supported_capabilities = AAZListType(
                serialized_name="supportedCapabilities",
                flags={"read_only": True},
            )

            nodes = cls._schema_on_200.properties.reported_properties.nodes
            nodes.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.reported_properties.nodes.Element
            _element.core_count = AAZFloatType(
                serialized_name="coreCount",
                flags={"read_only": True},
            )
            _element.ehc_resource_id = AAZStrType(
                serialized_name="ehcResourceId",
                flags={"read_only": True},
            )
            _element.id = AAZFloatType(
                flags={"read_only": True},
            )
            _element.last_licensing_timestamp = AAZStrType(
                serialized_name="lastLicensingTimestamp",
                flags={"read_only": True},
            )
            _element.manufacturer = AAZStrType(
                flags={"read_only": True},
            )
            _element.memory_in_gi_b = AAZFloatType(
                serialized_name="memoryInGiB",
                flags={"read_only": True},
            )
            _element.model = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.node_type = AAZStrType(
                serialized_name="nodeType",
                flags={"read_only": True},
            )
            _element.oem_activation = AAZStrType(
                serialized_name="oemActivation",
                flags={"read_only": True},
            )
            _element.os_display_version = AAZStrType(
                serialized_name="osDisplayVersion",
                flags={"read_only": True},
            )
            _element.os_name = AAZStrType(
                serialized_name="osName",
                flags={"read_only": True},
            )
            _element.os_version = AAZStrType(
                serialized_name="osVersion",
                flags={"read_only": True},
            )
            _element.serial_number = AAZStrType(
                serialized_name="serialNumber",
                flags={"read_only": True},
            )
            _element.windows_server_subscription = AAZStrType(
                serialized_name="windowsServerSubscription",
                flags={"read_only": True},
            )

            supported_capabilities = cls._schema_on_200.properties.reported_properties.supported_capabilities
            supported_capabilities.Element = AAZStrType()

            software_assurance_properties = cls._schema_on_200.properties.software_assurance_properties
            software_assurance_properties.last_updated = AAZStrType(
                serialized_name="lastUpdated",
                flags={"read_only": True},
            )
            software_assurance_properties.software_assurance_intent = AAZStrType(
                serialized_name="softwareAssuranceIntent",
            )
            software_assurance_properties.software_assurance_status = AAZStrType(
                serialized_name="softwareAssuranceStatus",
                flags={"read_only": True},
            )

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
