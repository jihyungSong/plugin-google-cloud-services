from spaceone.inventory.libs.schema.metadata.dynamic_field import TextDyField, SearchField, DateTimeDyField
from spaceone.inventory.libs.schema.cloud_service_type import CloudServiceTypeResource, CloudServiceTypeResponse, \
    CloudServiceTypeMeta

cst_instance_group = CloudServiceTypeResource()
cst_instance_group.name = 'InstanceGroup'
cst_instance_group.provider = 'google_cloud'
cst_instance_group.group = 'ComputeEngine'
cst_instance_group.labels = ['Compute']
cst_instance_group.tags = {
    'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/google_cloud/Compute_Engine.svg',
    'spaceone:is_major': 'true',
}

cst_instance_group._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source('Name', 'data.name'),
        TextDyField.data_source('Instances', 'data.instance_counts'),
        TextDyField.data_source('Template', 'data.template'),
        TextDyField.data_source('Group Type', 'data.template'),
        TextDyField.data_source('Recommendation', 'data.template'),
        TextDyField.data_source('Auto Scaling', 'data.template'),
        TextDyField.data_source('Zone', 'data.zone'),
        DateTimeDyField.data_source('Creation Time', 'data.creation_timestamp'),
    ],
    search=[
        SearchField.set(name='Name', key='data.name'),

    ]
)

CLOUD_SERVICE_TYPES = [
    CloudServiceTypeResponse({'resource': cst_instance_group}),
]
