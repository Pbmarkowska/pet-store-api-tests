import allure

def attach_response(response):
    allure.attach(
        response.text,
        name="Response",
        attachment_type=allure.attachment_type.JSON
    )