from settings import TOP_PERCENT_REPOSITORIES
from top_owners_by_pagerank_commits import get_top_owners_by_pagerank_commits
from utils import get_distinct_awesome_python_owners_found_in_commits, \
    get_top_repositories_by_contributors_count, \
    get_distinct_repositories_count, \
    get_awesome_python_repositories_found_in_commits


def get_top_pr_owners_also_in_awesome_owners_percentage():
    top_owners_by_pr_commits = get_top_owners_by_pagerank_commits()
    distinct_awesome_python_owners_found_in_commits = list(get_distinct_awesome_python_owners_found_in_commits())
    distinct_awesome_python_owners_found_in_commits_count = len(distinct_awesome_python_owners_found_in_commits)
    top_pr_owners_also_in_awesome_owners = set(top_owners_by_pr_commits) & set(
        distinct_awesome_python_owners_found_in_commits)
    top_pr_owners_also_in_awesome_owners_count = len(top_pr_owners_also_in_awesome_owners)
    top_pr_owners_also_in_awesome_owners_percentage = 100 * top_pr_owners_also_in_awesome_owners_count / distinct_awesome_python_owners_found_in_commits_count
    return top_pr_owners_also_in_awesome_owners_percentage


def get_top_repositories_by_contributors_count_also_in_awesome_repositories_percentage():
    topx_repositories_count = int(get_distinct_repositories_count() * TOP_PERCENT_REPOSITORIES)
    awesome_python_repositories_found_in_commits = list(get_awesome_python_repositories_found_in_commits())
    awesome_python_repositories_found_in_commits_count = len(awesome_python_repositories_found_in_commits)
    top_repositories_by_contributors_count = list(get_top_repositories_by_contributors_count(topx_repositories_count))
    top_repositories_by_contributors_count_also_in_awesome_repositories = set(top_repositories_by_contributors_count) & set(
        awesome_python_repositories_found_in_commits)
    top_repositories_by_contributors_count_also_in_awesome_repositories_count = len(top_repositories_by_contributors_count_also_in_awesome_repositories)
    top_repositories_by_contributors_count_also_in_awesome_repositories_percentage = 100 * top_repositories_by_contributors_count_also_in_awesome_repositories_count / awesome_python_repositories_found_in_commits_count
    return top_repositories_by_contributors_count_also_in_awesome_repositories_percentage


def main():
    top_pr_owners_also_in_awesome_owners_percentage = get_top_pr_owners_also_in_awesome_owners_percentage()
    print(f"top_pr_owners_also_in_awesome_owners_percentage = {top_pr_owners_also_in_awesome_owners_percentage}%")
    top_repositories_by_contributors_count_also_in_awesome_repositories_percentage = get_top_repositories_by_contributors_count_also_in_awesome_repositories_percentage()
    print(f"top_repositories_by_contributors_count_also_in_awesome_repositories_percentage = {top_repositories_by_contributors_count_also_in_awesome_repositories_percentage}%")


if __name__ == "__main__":
    main()

# top_pr_owners_also_in_awesome_owners_percentage = 25.278810408921935%
# top_repositories_by_contributors_count_also_in_awesome_repositories_percentage = 22.80701754385965%