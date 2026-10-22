import requests
import os

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = os.environ["PIXELA_USERNAME"]
TOKEN = os.environ["PIXELA_TOKEN"]


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.status_code)
#
#print(response.text)

#graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
#graph_config = {
#    "id": "graph1",
#    "name": "Cycling Graph",
#    "unit": "km",
#    "type": "float",
#    "color": "momiji"
#}
#
#headers = {
#    "X-USER-TOKEN": TOKEN
#}
#
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

# Post a pixel to the habit graph for the dtae when you are talking this lesson. You should see your new pixel displayed when you refresh the website

import datetime

today = datetime.date.today()
date_str = today.strftime("%Y%m%d")

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
pixel_data = {
    "date": date_str,
    "quantity": "5",
    "optionalData": '{"note": "Lesson completed"}'
}
headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)

# Post a pixel for yesterday
yesterday = today - datetime.timedelta(days=1)
yesterday_str = yesterday.strftime("%Y%m%d")

pixel_data_yesterday = {
    "date": yesterday_str,
    "quantity": "9",
    "optionalData": '{"note": "Lesson completed"}'
}

#response_yesterday = requests.post(url=pixel_endpoint, json=pixel_data_yesterday, headers=headers)
#print(response_yesterday.status_code)
#print(response_yesterday.text)

# Update yesterday's data point to a new value using an HTTP put request
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{yesterday_str}"
update_data = {
        "quantity": "8"
}

#response_update = requests.put(url=update_endpoint, json=update_data, headers=headers)
#print(response_update.status_code)
#print(response_update.text)

# Delete yesterday's data point using an HTTP delete request
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{yesterday_str}"
if os.getenv("DELETE_YESTERDAY_PIXEL", "false").lower() == "true":
    response_delete = requests.delete(url=delete_endpoint, headers=headers)
    print(response_delete.status_code)
    print(response_delete.text)
else:
    print("Deletion skipped. Set DELETE_YESTERDAY_PIXEL=true to enable it.")

