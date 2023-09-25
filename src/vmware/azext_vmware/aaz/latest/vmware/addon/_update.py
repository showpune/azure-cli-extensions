# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


class Update(AAZCommand):
    """Update a addon in a private cloud
    """

    _aaz_info = {
        "version": "2022-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.avs/privateclouds/{}/addons/{}", "2022-05-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.addon_name = AAZStrArg(
            options=["-n", "--name", "--addon-name"],
            help="Name of the addon for the private cloud",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.private_cloud = AAZStrArg(
            options=["-c", "--private-cloud"],
            help="Name of the private cloud",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.arc = AAZObjectArg(
            options=["--arc"],
            arg_group="Properties",
            help="an Arc addon for a private cloud.",
        )
        _args_schema.hcx = AAZObjectArg(
            options=["--hcx"],
            arg_group="Properties",
            help="a HCX addon for a private cloud.",
        )
        _args_schema.srm = AAZObjectArg(
            options=["--srm"],
            arg_group="Properties",
            help="a Site Recovery Manager (SRM) addon for a private cloud.",
        )
        _args_schema.vr = AAZObjectArg(
            options=["--vr"],
            arg_group="Properties",
            help="a vSphere Replication (VR) addon for a private cloud",
        )

        arc = cls._args_schema.arc
        arc.vcenter = AAZStrArg(
            options=["vcenter"],
            help="The VMware vCenter resource ID",
        )

        hcx = cls._args_schema.hcx
        hcx.offer = AAZStrArg(
            options=["offer"],
            help="The HCX offer, example VMware MaaS Cloud Provider (Enterprise)",
        )

        srm = cls._args_schema.srm
        srm.license_key = AAZStrArg(
            options=["license-key"],
            help="The Site Recovery Manager (SRM) license",
        )

        vr = cls._args_schema.vr
        vr.vrs_count = AAZIntArg(
            options=["vrs-count"],
            help="The vSphere Replication Server (VRS) count",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.AddonsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.AddonsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class AddonsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AVS/privateClouds/{privateCloudName}/addons/{addonName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "addonName", self.ctx.args.addon_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "privateCloudName", self.ctx.args.private_cloud,
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
                    "api-version", "2022-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

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
            _UpdateHelper._build_schema_addon_read(cls._schema_on_200)

            return cls._schema_on_200

    class AddonsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AVS/privateClouds/{privateCloudName}/addons/{addonName}",
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
                    "addonName", self.ctx.args.addon_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "privateCloudName", self.ctx.args.private_cloud,
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
                    "api-version", "2022-05-01",
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
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_addon_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType)

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_const("addonType", "Arc", AAZStrType, ".arc", typ_kwargs={"flags": {"required": True}})
                properties.set_const("addonType", "HCX", AAZStrType, ".hcx", typ_kwargs={"flags": {"required": True}})
                properties.set_const("addonType", "SRM", AAZStrType, ".srm", typ_kwargs={"flags": {"required": True}})
                properties.set_const("addonType", "VR", AAZStrType, ".vr", typ_kwargs={"flags": {"required": True}})
                properties.discriminate_by("addonType", "Arc")
                properties.discriminate_by("addonType", "HCX")
                properties.discriminate_by("addonType", "SRM")
                properties.discriminate_by("addonType", "VR")

            disc_arc = _builder.get(".properties{addonType:Arc}")
            if disc_arc is not None:
                disc_arc.set_prop("vCenter", AAZStrType, ".arc.vcenter", typ_kwargs={"flags": {"required": True}})

            disc_hcx = _builder.get(".properties{addonType:HCX}")
            if disc_hcx is not None:
                disc_hcx.set_prop("offer", AAZStrType, ".hcx.offer", typ_kwargs={"flags": {"required": True}})

            disc_srm = _builder.get(".properties{addonType:SRM}")
            if disc_srm is not None:
                disc_srm.set_prop("licenseKey", AAZStrType, ".srm.license_key", typ_kwargs={"flags": {"required": True}})

            disc_vr = _builder.get(".properties{addonType:VR}")
            if disc_vr is not None:
                disc_vr.set_prop("vrsCount", AAZIntType, ".vr.vrs_count", typ_kwargs={"flags": {"required": True}})

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_addon_read = None

    @classmethod
    def _build_schema_addon_read(cls, _schema):
        if cls._schema_addon_read is not None:
            _schema.id = cls._schema_addon_read.id
            _schema.name = cls._schema_addon_read.name
            _schema.properties = cls._schema_addon_read.properties
            _schema.type = cls._schema_addon_read.type
            return

        cls._schema_addon_read = _schema_addon_read = AAZObjectType()

        addon_read = _schema_addon_read
        addon_read.id = AAZStrType(
            flags={"read_only": True},
        )
        addon_read.name = AAZStrType(
            flags={"read_only": True},
        )
        addon_read.properties = AAZObjectType()
        addon_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_addon_read.properties
        properties.addon_type = AAZStrType(
            serialized_name="addonType",
            flags={"required": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )

        disc_arc = _schema_addon_read.properties.discriminate_by("addon_type", "Arc")
        disc_arc.v_center = AAZStrType(
            serialized_name="vCenter",
            flags={"required": True},
        )

        disc_hcx = _schema_addon_read.properties.discriminate_by("addon_type", "HCX")
        disc_hcx.offer = AAZStrType(
            flags={"required": True},
        )

        disc_srm = _schema_addon_read.properties.discriminate_by("addon_type", "SRM")
        disc_srm.license_key = AAZStrType(
            serialized_name="licenseKey",
            flags={"required": True},
        )

        disc_vr = _schema_addon_read.properties.discriminate_by("addon_type", "VR")
        disc_vr.vrs_count = AAZIntType(
            serialized_name="vrsCount",
            flags={"required": True},
        )

        _schema.id = cls._schema_addon_read.id
        _schema.name = cls._schema_addon_read.name
        _schema.properties = cls._schema_addon_read.properties
        _schema.type = cls._schema_addon_read.type


__all__ = ["Update"]