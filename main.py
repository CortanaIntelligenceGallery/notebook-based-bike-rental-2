from azureml.api.schema.schemaUtil import *
import azureml.api.schema.utilities as util
from azureml.api.exceptions.BadRequest import BadRequestException
from azureml.api.realtime.swagger_spec_generator import generate_service_swagger
import os
from bikescore import init as user_init_func
from bikescore import run as user_run_func

def run(http_body):
    if aml_service_schema is not None:
        arguments = parse_service_input(http_body, aml_service_schema.input)
        try:
            return_obj = user_run_func(**arguments)
        except TypeError as exc:
            raise BadRequestException(str(exc))
    else:
        return_obj = user_run_func(http_body)
    return return_obj


def init():
    global aml_service_schema
    schema_file = "bikeschema.json"
    service_name = os.getenv('SERVICE_NAME', 'ML service')
    service_path_prefix = os.getenv('SERVICE_PATH_PREFIX', '')
    service_version = os.getenv('SERVICE_VERSION', '1.0')

    if schema_file:
        aml_service_schema = load_service_schema(schema_file)
    else:
        aml_service_schema = None

    swagger_json = generate_service_swagger(service_name=service_name,
                                            service_schema_file_path=schema_file,
                                            service_version=service_version,
                                            service_path_prefix=service_path_prefix)

    with open('swagger.json', 'w') as swagger_file:
        json.dump(swagger_json, swagger_file)

    user_init_func()