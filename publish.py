from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.web import WebSiteManagementClient
from azure.identity import DefaultAzureCredential

# Authenticate with Azure using the DefaultAzureCredential
credential = DefaultAzureCredential()

# Initialize the ResourceManagementClient
resource_client = ResourceManagementClient(credential, "<your_subscription_id>")

# Create a Resource Group
resource_group_params = {"location": "westus"}
resource_client.resource_groups.create_or_update("my_resource_group", resource_group_params)

# Initialize the WebSiteManagementClient
web_client = WebSiteManagementClient(credential, "<your_subscription_id>")

# Create an App Service Plan
app_service_plan = web_client.app_service_plans.begin_create_or_update(
    "my_resource_group",
    "my_app_service_plan",
    {
        "location": "westus",
        "sku": {"name": "B1", "tier": "Basic"}
    }
).result()

# Create a Web App
web_app = web_client.web_apps.begin_create_or_update(
    "my_resource_group",
    "my_web_app",
    {
        "location": "westus",
        "server_farm_id": app_service_plan.id
    }
).result()