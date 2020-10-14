import json
from itertools import islice

from networkx import Graph, pagerank

from utils import get_commits_owner_actor_count, insert_pr

PR_CACHE_FILE_NAME = "pr_owners.csv"
TOP_PR_CACHE_FILE_NAME = "top_pr_owners.csv"


def get_pr(read_from_cache_file=True):
    if read_from_cache_file:
        with open(PR_CACHE_FILE_NAME, "rt") as f:
            return json.loads(f.read())

    graph = Graph()
    commits_owner_actor_count = get_commits_owner_actor_count()

    print("Iterating commits_owner_actor_count")
    for (owner, actor, commits_count) in commits_owner_actor_count:
        graph.add_edge(actor, owner, weight=commits_count)

    print("Running page rank")
    pr = pagerank(graph, weight=commits_count)

    with open(PR_CACHE_FILE_NAME, "wt") as f:
        f.write(json.dumps(pr))

    print("Updating user_pr_grade table")
    insert_pr(pr)

    return pr


def get_top_owners_by_pagerank_commits(top_count, read_from_cache_file=True):
    if read_from_cache_file:
        with open(TOP_PR_CACHE_FILE_NAME, "rt") as f:
            return set(islice(
                map(lambda x: x[1:-1], f.read()[1:-1].split(", "))
                , top_count))

    pr = get_pr(read_from_cache_file)

    pr_ordered = {
        k: v for k, v in sorted(pr.items(), key=lambda item: item[1], reverse=True)
    }

    top_pr_owners = set(list(islice(pr_ordered, top_count)))

    with open(TOP_PR_CACHE_FILE_NAME, "wt") as f:
        f.write(str(top_pr_owners))
    return top_pr_owners

# top10_owners: ['ansible', 'benoitc', 'biopython', 'audreyr', 'bear',
# 'aparo', 'alex', 'bbangert', 'asciimoo', 'benhoff']
