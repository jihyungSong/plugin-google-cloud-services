from spaceone.inventory.libs.manager import GoogleCloudManager
from spaceone.inventory.libs.schema.base import ReferenceModel
from spaceone.inventory.connector.cloud_sql import CloudSQLConnector
from spaceone.inventory.model.cloud_sql.data import *
from spaceone.inventory.model.cloud_sql.cloud_service import *
from spaceone.inventory.model.cloud_sql.cloud_service_type import CLOUD_SERVICE_TYPES
import time

class CloudSQLManager(GoogleCloudManager):
    connector_name = 'CloudSQLConnector'
    cloud_service_types = CLOUD_SERVICE_TYPES

    def collect_cloud_service(self, params):
        print("** Cloud SQL START **")
        start_time = time.time()
        """
        Args:
            params:
                - options
                - schema
                - secret_data
                - filter
                - zones
        Response:
            CloudServiceResponse
        """

        cloud_sql_conn: CloudSQLConnector = self.locator.get_connector(self.connector_name, **params)

        collected_cloud_services = []
        for instance in cloud_sql_conn.list_instances():
            instance_name = instance['name']

            # Get Databases
            databases = cloud_sql_conn.list_databases(instance_name)

            # Get Users
            users = cloud_sql_conn.list_users(instance_name)

            instance.update({
                'display_state': self._get_display_state(instance),
                'databases': [Database(database, strict=False) for database in databases],
                'users': [User(user, strict=False) for user in users],
            })

            # No labels!!
            instance_data = Instance(instance, strict=False)
            instance_resource = InstanceResource({
                'data': instance_data,
                'region_code': instance['region'],
                'reference': ReferenceModel(instance_data.reference())
            })

            self.set_region_code(instance['region'])
            collected_cloud_services.append(InstanceResponse({'resource': instance_resource}))

        print(f'** Cloud SQL Finished {time.time() - start_time} Seconds **')
        return collected_cloud_services

    @staticmethod
    def _get_display_state(instance):
        activation_policy = instance.get('settings', {}).get('activationPolicy', 'UNKNOWN')

        if activation_policy in ['ALWAYS']:
            return 'RUNNING'
        elif activation_policy in ['NEVER']:
            return 'STOPPED'
        elif activation_policy in ['ON_DEMAND']:
            return 'ON-DEMAND'
        else:
            return 'UNKNOWN'
