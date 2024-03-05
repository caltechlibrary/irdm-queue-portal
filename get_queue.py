import os,re,csv
from ames.harvesters import get_pending_requests
from ames.harvesters import get_request_comments
from ames.harvesters import get_request_id_title
from ames.harvesters import get_publisher

token = os.environ["CTATOK"]

community = "aedd135f-227e-4fdf-9476-5b3fd011bac6"

completed = []

pending = get_pending_requests(token, community)

for p in pending:
    rdm_id,title,updated = get_request_id_title(token, p)
    publisher = get_publisher(token, rdm_id)
    comments = get_request_comments(token, p)
    tags = []
    for c in comments:
        if '@' in c:
            tags = re.findall(r'@(\w+)', c)
    if tags == []:
        tags.append('new')
    for tag in tags:
        completed.append([tag,updated,title,publisher,rdm_id, p])

with open("queue.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(['tag','updated','title','publisher','rdm_id','request'])
    for c in completed:
        writer.writerow(c)


