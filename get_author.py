import os, re, csv, sys
from ames.harvesters import get_pending_requests
from ames.harvesters import get_request_id_title
from ames.harvesters import get_authors

token = os.environ["CTATOK"]

community = "aedd135f-227e-4fdf-9476-5b3fd011bac6"

data = []
completed = []

infile = "completed_records.csv"
if os.path.exists(infile):
    with open(infile, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            completed.append(row[0].strip())

completed_writer = csv.writer(open(infile, "a"))

infile = "author_queue.csv"
if os.path.exists(infile):
    writer = csv.writer(open(infile, "a"))
else:
    header = ["rdm_id", "title", "request_id"]
    writer = csv.writer(open(infile, "w"))
    writer.writerow(header)

pending = get_pending_requests(token, community)

match_name = sys.argv[1] if len(sys.argv) > 1 else None

for p in pending:
    rdm_id, title, updated = get_request_id_title(token, p)
    if rdm_id not in completed:
        print(rdm_id)
        authors = get_authors(token, rdm_id)
        for author in authors:
            name = author["person_or_org"]["name"]
            if match_name in name:
                writer.writerow([rdm_id, title, p])
        completed_writer.writerow([rdm_id])
