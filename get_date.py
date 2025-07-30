import os, re, csv, sys
from ames.harvesters import get_pending_requests
from ames.harvesters import get_request_id_title
from ames.harvesters import get_doi

token = os.environ["CTATOK"]

community = "aedd135f-227e-4fdf-9476-5b3fd011bac6"

completed = []

infile = "to_close.csv"

if os.path.exists(infile):
    with open(infile, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            completed.append(row[0].strip())

completed_writer = csv.writer(open(infile, "a"))

pending = get_pending_requests(token, community)

for p in pending:
    if p not in completed:
        rdm_id, title, updated = get_request_id_title(token, p)
        doi = get_doi(token, rdm_id)
        completed_writer.writerow([p,rdm_id, updated, doi])
