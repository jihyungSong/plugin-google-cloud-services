from spaceone.inventory.libs.schema.metadata.dynamic_field import TextDyField, SearchField, DateTimeDyField, EnumDyField
from spaceone.inventory.libs.schema.cloud_service_type import CloudServiceTypeResource, CloudServiceTypeResponse, \
    CloudServiceTypeMeta

cst_instance_group = CloudServiceTypeResource()
cst_instance_group.name = 'InstanceGroup'
cst_instance_group.provider = 'google_cloud'
cst_instance_group.group = 'ComputeEngine'
cst_instance_group.service_code = 'compute'
cst_instance_group.labels = ['Compute']
cst_instance_group.tags = {
    'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/google_cloud/Compute_Engine.svg',
}

cst_instance_group._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source('Name', 'data.name'),
        TextDyField.data_source('Instances', 'data.instance_counts'),
        EnumDyField.data_source('Type', 'data.instance_group_type',
                                default_outline_badge=['STATELESS', 'STATEFUL', 'UNMANAGED']),
        TextDyField.data_source('Template', 'data.template.name'),
        TextDyField.data_source('Autoscaling', 'data.autoscaling_display'),
        DateTimeDyField.data_source('Creation Time', 'data.creation_timestamp'),
    ],
    search=[
        SearchField.set(name='Name', key='data.name'),
        SearchField.set(name='Instance Counts', key='data.name', data_type='integer'),
        SearchField.set(name='Template', key='data.template.name'),
        SearchField.set(name='Region', key='region_code'),
        SearchField.set(name='Zone', key='data.zone'),
        SearchField.set(name='Creation Time', key='data.creation_timestamp', data_type='datetime'),
    ]
)

CLOUD_SERVICE_TYPES = [
    CloudServiceTypeResponse({'resource': cst_instance_group}),
]
