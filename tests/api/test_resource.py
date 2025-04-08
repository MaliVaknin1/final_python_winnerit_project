import pytest
from assertpy import assert_that
from api_requests.resource_api import ResourceApi
from utils.configs import RESOURCES_DATA, SINGLE_RESOURCE_DATA, NON_EXISTENT_RESOURCE_DATA

#Get resource list and Verify status code is 200 and verify response contains page, per_page, total, total_pages, data, and first resource data
def test_get_resource_list():
    resource_api = ResourceApi()
    response = resource_api.get_resource_list()
    assert_that(response.status_code).is_equal_to(200)
    response_json = response.json()
    assert_that(response_json["page"]).is_equal_to(RESOURCES_DATA["expected_page"])
    assert_that(response_json["per_page"]).is_equal_to(RESOURCES_DATA["expected_per_page"])
    assert_that(response_json["total"]).is_equal_to(RESOURCES_DATA["expected_total"])
    assert_that(response_json["total_pages"]).is_equal_to(RESOURCES_DATA["expected_total_pages"])
    first_resource = response_json["data"][0]
    expected_resource = RESOURCES_DATA["expected_first_resource"]
    assert_that(first_resource["id"]).is_equal_to(expected_resource["id"])
    assert_that(first_resource["name"]).is_equal_to(expected_resource["name"])
    assert_that(first_resource["year"]).is_equal_to(expected_resource["year"])
    assert_that(first_resource["color"]).is_equal_to(expected_resource["color"])

#Get single resource and Verify status code is 200 and verify response contains data and support
def test_get_single_resource():
    resource_api = ResourceApi()
    response = resource_api.get_single_resource(resource_id=SINGLE_RESOURCE_DATA["resource_id"])
    assert_that(response.status_code).is_equal_to(200)
    response_json = response.json()
    assert_that(response_json).contains_key("data")
    assert_that(response_json).contains_key("support")
    resource_data = response_json["data"]
    expected_resource = SINGLE_RESOURCE_DATA["expected_resource"]
    assert_that(resource_data["id"]).is_equal_to(expected_resource["id"])
    assert_that(resource_data["name"]).is_equal_to(expected_resource["name"])
    assert_that(resource_data["year"]).is_equal_to(expected_resource["year"])


#Get non-existent resource and Verify status code is 404 and response is empty
def test_get_non_existent_resource():
    resource_api = ResourceApi()
    response = resource_api.get_single_resource(resource_id=NON_EXISTENT_RESOURCE_DATA["resource_id"])
    assert_that(response.status_code).is_equal_to(404)
    response_json = response.json()
    assert_that(response_json).is_equal_to({})
