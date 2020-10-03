from itertools import islice

from networkx import DiGraph, pagerank

from settings import TOP_PERCENT_OWNERS
from utils import get_commits_owner_actor_count, get_distinct_owners_count

CACHE_FILE_NAME = "top_pr_owners.csv"


def get_top_owners_by_pagerank_commits(read_from_cache_file=False):
    if read_from_cache_file:
        with open(CACHE_FILE_NAME, "rt") as f:
            return set(map(lambda x: x[1:-1], f.read()[1:-1].split(", ")))

    topx_pr_owners_count = int(get_distinct_owners_count() * TOP_PERCENT_OWNERS)
    graph = DiGraph()
    commits_owner_actor_count = get_commits_owner_actor_count()

    print("Iterating commits_owner_actor_count")
    for (owner, actor, commits_count) in commits_owner_actor_count:
        graph.add_edge(actor, owner, weight=commits_count)

    print("Running page rank")
    pr = pagerank(graph, weight="weight")

    pr_ordered = {
        k: v for k, v in sorted(pr.items(), key=lambda item: item[1], reverse=True)
    }

    top_pr_owners = set(list(islice(pr_ordered, topx_pr_owners_count)))

    with open(CACHE_FILE_NAME, "wt") as f:
        f.write(str(top_pr_owners))
    return top_pr_owners

# top10_owners: ['ansible', 'benoitc', 'biopython', 'audreyr', 'bear',
# 'aparo', 'alex', 'bbangert', 'asciimoo', 'benhoff']
