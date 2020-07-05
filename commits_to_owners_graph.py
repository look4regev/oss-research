from itertools import islice

import psycopg2
from networkx import DiGraph, pagerank

from settings import DB_PASSWORD

DBNAME = "github"

print(f"connecting to db {DBNAME}")
conn = psycopg2.connect(f"dbname={DBNAME} user=supergod password={DB_PASSWORD}")
cur = conn.cursor()
graph = DiGraph()

cur.execute(
    """
select project_owner, actor, count(*)
from commits
group by project_owner, actor
"""
)

print("Iterating project_owner,actor,count(*)")
for (owner, actor, commits_count) in cur:
    graph.add_edge(actor, owner, weight=commits_count)

print("Running page rank")
pr = pagerank(graph, weight="weight")

print("10 highest owners:")
pr_ordered = {
    k: v for k, v in sorted(pr.items(), key=lambda item: item[1], reverse=True)
}
print(list(islice(pr_ordered, 10)))
# ['ansible', 'benoitc', 'biopython', 'audreyr', 'bear',
# 'aparo', 'alex', 'bbangert', 'asciimoo', 'benhoff']

cur.close()
conn.close()
print("Done")
