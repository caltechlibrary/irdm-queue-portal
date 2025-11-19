import os, re, csv, sys
from ames.harvesters import get_pending_requests
from ames.harvesters import get_request_id_title
from ames.harvesters import get_authors

token = os.environ["CTATOK"]

community = "aedd135f-227e-4fdf-9476-5b3fd011bac6"

match_name = sys.argv[1] if len(sys.argv) > 1 else None

if match_name is None:
    infile = "author_queue.csv"
else:
    infile = f"{match_name}_queue.csv"

header = ["rdm_id", "title", "request_id"]
writer = csv.writer(open(infile, "w"))
writer.writerow(header)

pending = get_pending_requests(token, community)

match_name = sys.argv[1] if len(sys.argv) > 1 else None

for p in pending:
    rdm_id, title, updated = get_request_id_title(token, p)
    print(rdm_id)
    authors = get_authors(token, rdm_id)
    for author in authors:
        name = author["person_or_org"]["name"]
        if match_name in name:
            writer.writerow([rdm_id, title, p])
