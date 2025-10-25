import os, re, csv, sys
from ames.harvesters import get_pending_requests
from ames.harvesters import get_request_id_title
from ames.harvesters import get_publisher
import requests

token = os.environ["CTATOK"]

community = "aedd135f-227e-4fdf-9476-5b3fd011bac6"

pending = get_pending_requests(token, community)
url = "https://authors.library.caltech.edu/api/records"

for p in pending:
    rdm_id, title, updated = get_request_id_title(token, p)
    full_url = f"{url}/{rdm_id}/quota"
    data = {
        "max_file_size": 100000000000,
        "notes": "Setting default quota.",
        "quota_size": 1000000000000,
    }
    response = requests.post(
        full_url, headers={"Authorization": f"Bearer {token}"}, json=data
    )
    if response.status_code == 200:
        print(f"Set quota for {rdm_id} - {title}")
    else:
        print(
            f"Error setting quota for {rdm_id} - {title}: {response.status_code} {response.text}"
        )
