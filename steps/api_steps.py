# A step that would handle any request
#
# A step that would load a payload with the option of updating it by JSONPath
#
# A step that would verify the response value
from behave import step

from common import TOKEN
from components.payload_api import PayloadAPI


@step('Making {GET} request to {url} with auth token')
@step('Making {method} request to {url} with {filename} with auth token')
def step_impl(context, method, url, filename=None):
    if method == 'GET':
        context.response = context.client.get_request(url, headers={"Authorization": f"Bearer {TOKEN}"})
    elif method == 'POST':
        payload = PayloadAPI(filename)
        context.response = context.client.post_request(url, payload, headers={"Authorization": f"Bearer {TOKEN}"})
    elif method == 'PATCH':
        payload = PayloadAPI(filename)
        context.response = context.client.patch_request(url, payload, headers={"Authorization": f"Bearer {TOKEN}"})
    elif method == 'DELETE':
        context.response = context.client.delete_request(url, headers={"Authorization": f"Bearer {TOKEN}"})
    else:
        raise ValueError("Unsupported method")



@step('Making {method} request to {url}')
def step_impl(context, request, url):
    context.browser.get(url)

@step('Verify status code is {status_code}')
def step_impl(context, status_code):
    context.response.verify_status_code(status_code)


@step('Verify jsonpath {jsonpath} finds {number} matches in response payload')
def step_impl(context, jsonpath, number):
    context.response.verify_length(jsonpath, number)

@step('Verify payload contains jsonpath {jsonpath}')
def step_impl(context, jsonpath):
    context.response.verify_contains(jsonpath)

@step('Verify in payload value by jsonpath {jsonpath} equals {value}')
def step_impl(context, jsonpath, value):
    context.response.verify_equals(jsonpath, value)
