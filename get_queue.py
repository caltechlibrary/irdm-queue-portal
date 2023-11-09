import os,re,csv
from ames.harvesters import get_pending_requests
from ames.harvesters import get_request_comments
from ames.harvesters import get_request_id_title

token = os.environ["CTATOK"]

community = "aedd135f-227e-4fdf-9476-5b3fd011bac6"

completed = []

pending = get_pending_requests(token, community)

for p in pending:
    rdm_id,title = get_request_id_title(token, p)
    comments = get_request_comments(token, p)
    tags = []
    for c in comments:
        if '@' in c:
            tags = re.findall(r'@(\w+)', c)
    tags.append('review')
    for tag in tags:
        completed.append([rdm_id, p, title, tag])

with open("queue.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(['rdm_id','request','title','tag'])
    for c in completed:
        writer.writerow(c)


