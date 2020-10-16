from settings import TOP_REPOSITORIES_COUNT, TOP_OWNERS_COUNT
from top_owners_by_pagerank_commits import get_top_owners_by_pagerank_commits
from utils import get_distinct_awesome_python_owners_found_in_commits, \
    get_top_repositories_by_contributors_count, \
    get_awesome_python_repositories_found_in_commits, \
    get_top_owners_by_contributors_count, \
    get_top_repositories_by_contributors_pr_grade_sum, \
    get_repos_of_owners


def print_stats(prefix, precision, recall, algo_results_count):
    precision_f = precision / 100
    recall_f = recall / 100
    f1 = round(2 * (precision_f * recall_f) / (precision_f + recall_f), 5)
    prefix = prefix.ljust(85)
    print(f"[{prefix}] precision: {round(precision, 5)}% \t recall: {round(recall, 5)}% \t f1: {f1} \t algo_results_count: {algo_results_count}")


def get_common(a, b):
    return set(a) & set(b)


def get_top_pr_owners_also_in_awesome_owners_percentage():
    top_owners_by_pr_commits = get_top_owners_by_pagerank_commits(TOP_OWNERS_COUNT)
    top_owners_by_pr_commits_count = len(top_owners_by_pr_commits)
    distinct_awesome_python_owners_found_in_commits = list(get_distinct_awesome_python_owners_found_in_commits())
    distinct_awesome_python_owners_found_in_commits_count = len(distinct_awesome_python_owners_found_in_commits)
    top_pr_owners_also_in_awesome_owners = get_common(top_owners_by_pr_commits, distinct_awesome_python_owners_found_in_commits)
    top_pr_owners_also_in_awesome_owners_count = len(top_pr_owners_also_in_awesome_owners)
    precision = 100 * top_pr_owners_also_in_awesome_owners_count / top_owners_by_pr_commits_count
    recall = 100 * top_pr_owners_also_in_awesome_owners_count / distinct_awesome_python_owners_found_in_commits_count
    print_stats("top_pr_owners_also_in_awesome_owners_percentage", precision, recall, TOP_OWNERS_COUNT)


def get_top_pr_repos_also_in_awesome_repos_percentage():
    top_owners_by_pr_commits = get_top_owners_by_pagerank_commits(TOP_OWNERS_COUNT)
    distinct_awesome_python_owners_found_in_commits = list(get_distinct_awesome_python_owners_found_in_commits())
    top_pr_owners_also_in_awesome_owners = get_common(top_owners_by_pr_commits, distinct_awesome_python_owners_found_in_commits)
    top_pr_owners_repos = get_repos_of_owners(top_pr_owners_also_in_awesome_owners)
    awesome_python_repositories_found_in_commits = list(get_awesome_python_repositories_found_in_commits())
    awesome_python_repositories_found_in_commits_count = len(awesome_python_repositories_found_in_commits)
    top_pr_owners_repos_also_in_awesome_repositories = get_common(top_pr_owners_repos, awesome_python_repositories_found_in_commits)
    top_pr_owners_repos_also_in_awesome_repositories_count = len(top_pr_owners_repos_also_in_awesome_repositories)
    top_pr_owners_repos_count = len(top_pr_owners_repos)
    precision = 100 * top_pr_owners_repos_also_in_awesome_repositories_count / top_pr_owners_repos_count
    recall = 100 * top_pr_owners_repos_also_in_awesome_repositories_count / awesome_python_repositories_found_in_commits_count
    print_stats("top_pr_repos_also_in_awesome_repos_percentage", precision, recall, top_pr_owners_repos_count)


def get_top_repositories_by_contributors_count_also_in_awesome_repositories_percentage():
    awesome_python_repositories_found_in_commits = list(get_awesome_python_repositories_found_in_commits())
    awesome_python_repositories_found_in_commits_count = len(awesome_python_repositories_found_in_commits)
    top_repositories_by_contributors_count = list(get_top_repositories_by_contributors_count(TOP_REPOSITORIES_COUNT))
    top_repositories_by_contributors_count_also_in_awesome_repositories = get_common(top_repositories_by_contributors_count, awesome_python_repositories_found_in_commits)
    top_repositories_by_contributors_count_also_in_awesome_repositories_count = len(top_repositories_by_contributors_count_also_in_awesome_repositories)
    precision = 100 * top_repositories_by_contributors_count_also_in_awesome_repositories_count / TOP_REPOSITORIES_COUNT
    recall = 100 * top_repositories_by_contributors_count_also_in_awesome_repositories_count / awesome_python_repositories_found_in_commits_count
    print_stats("top_repositories_by_contributors_count_also_in_awesome_repositories_percentage", precision, recall, TOP_REPOSITORIES_COUNT)


def get_top_repositories_by_contributors_pr_grade_sum_also_in_awesome_repositories_percentage():
    awesome_python_repositories_found_in_commits = list(get_awesome_python_repositories_found_in_commits())
    awesome_python_repositories_found_in_commits_count = len(awesome_python_repositories_found_in_commits)
    top_repositories_by_contributors_count = list(get_top_repositories_by_contributors_pr_grade_sum(TOP_REPOSITORIES_COUNT))
    top_repositories_by_contributors_count_also_in_awesome_repositories = get_common(
        top_repositories_by_contributors_count, awesome_python_repositories_found_in_commits)
    top_repositories_by_contributors_count_also_in_awesome_repositories_count = len(
        top_repositories_by_contributors_count_also_in_awesome_repositories)
    precision = 100 * top_repositories_by_contributors_count_also_in_awesome_repositories_count / TOP_REPOSITORIES_COUNT
    recall = 100 * top_repositories_by_contributors_count_also_in_awesome_repositories_count / awesome_python_repositories_found_in_commits_count
    print_stats("top_repositories_by_contributors_pr_grade_sum_also_in_awesome_repositories_percentage", precision, recall,
                TOP_REPOSITORIES_COUNT)


def get_top_owners_by_contributors_count_also_in_awesome_repositories_percentage():
    distinct_awesome_python_owners_found_in_commits = list(get_distinct_awesome_python_owners_found_in_commits())
    distinct_awesome_python_owners_found_in_commits_count = len(distinct_awesome_python_owners_found_in_commits)
    top_owners_by_contributors_count = list(get_top_owners_by_contributors_count(TOP_OWNERS_COUNT))
    top_owners_by_contributors_count_also_in_awesome_owners = get_common(top_owners_by_contributors_count, distinct_awesome_python_owners_found_in_commits)
    top_owners_by_contributors_count_also_in_awesome_owners_count = len(top_owners_by_contributors_count_also_in_awesome_owners)
    precision = 100 * top_owners_by_contributors_count_also_in_awesome_owners_count / TOP_OWNERS_COUNT
    recall = 100 * top_owners_by_contributors_count_also_in_awesome_owners_count / distinct_awesome_python_owners_found_in_commits_count
    print_stats("top_owners_by_contributors_count_also_in_awesome_owners_percentage", precision, recall, TOP_OWNERS_COUNT)


def main():
    get_top_pr_repos_also_in_awesome_repos_percentage()
    get_top_pr_owners_also_in_awesome_owners_percentage()
    get_top_repositories_by_contributors_pr_grade_sum_also_in_awesome_repositories_percentage()
    get_top_repositories_by_contributors_count_also_in_awesome_repositories_percentage()
    get_top_owners_by_contributors_count_also_in_awesome_repositories_percentage()


if __name__ == "__main__":
    main()

# [top_pr_repos_also_in_awesome_repos_percentage                                        ] precision: 15.98441% 	 recall: 29.07801% 	 f1: 0.20629 	 algo_results_count: 513
# [top_pr_owners_also_in_awesome_owners_percentage                                      ] precision: 28.62454% 	 recall: 28.73134% 	 f1: 0.28678 	 algo_results_count: 269
# [top_repositories_by_contributors_pr_grade_sum_also_in_awesome_repositories_percentage] precision: 28.50877% 	 recall: 23.04965% 	 f1: 0.2549 	 algo_results_count: 228
# [top_repositories_by_contributors_count_also_in_awesome_repositories_percentage       ] precision: 28.50877% 	 recall: 23.04965% 	 f1: 0.2549 	 algo_results_count: 228
# [top_owners_by_contributors_count_also_in_awesome_owners_percentage                   ] precision: 28.99628% 	 recall: 29.10448% 	 f1: 0.2905 	 algo_results_count: 269
