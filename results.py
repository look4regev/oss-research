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
    return set(top_repositories_by_contributors_count_also_in_awesome_repositories)


def get_top_repositories_by_contributors_pr_grade_sum_also_in_awesome_repositories_percentage():
    awesome_python_repositories_found_in_commits = list(get_awesome_python_repositories_found_in_commits())
    awesome_python_repositories_found_in_commits_count = len(awesome_python_repositories_found_in_commits)
    top_repositories_by_contributors_pr_grade = list(get_top_repositories_by_contributors_pr_grade_sum(TOP_REPOSITORIES_COUNT))
    top_repositories_by_contributors_pr_grade_also_in_awesome_repositories = get_common(
        top_repositories_by_contributors_pr_grade, awesome_python_repositories_found_in_commits)
    top_repositories_by_contributors_pr_grade_also_in_awesome_repositories_count = len(
        top_repositories_by_contributors_pr_grade_also_in_awesome_repositories)
    precision = 100 * top_repositories_by_contributors_pr_grade_also_in_awesome_repositories_count / TOP_REPOSITORIES_COUNT
    recall = 100 * top_repositories_by_contributors_pr_grade_also_in_awesome_repositories_count / awesome_python_repositories_found_in_commits_count
    print_stats("top_repositories_by_contributors_pr_grade_sum_also_in_awesome_repositories_percentage", precision, recall,
                TOP_REPOSITORIES_COUNT)
    return set(top_repositories_by_contributors_pr_grade_also_in_awesome_repositories)


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
    # get_top_pr_repos_also_in_awesome_repos_percentage()
    # get_top_pr_owners_also_in_awesome_owners_percentage()
    mine = get_top_repositories_by_contributors_pr_grade_sum_also_in_awesome_repositories_percentage()
    bench = get_top_repositories_by_contributors_count_also_in_awesome_repositories_percentage()
    mine_not_in_bench = mine - bench
    bench_not_in_mine = bench - mine
    both = mine & bench
    print(f"mine: {len(mine)}, bench: {len(bench)}, mine_not_in_bench: {len(mine_not_in_bench)}, bench_not_in_mine: {len(bench_not_in_mine)}, both: {len(both)},")
    print(f"mine found in awesome but not in benchmark: {mine_not_in_bench}")
    print(f"benchmark found in awesome but not in mine: {bench_not_in_mine}")
    print(f"both mine and benchmark found from awesome: {both}")
    # get_top_owners_by_contributors_count_also_in_awesome_repositories_percentage()


if __name__ == "__main__":
    main()

# [top_repositories_by_contributors_pr_grade_sum_also_in_awesome_repositories_percentage] precision: 30.26316% 	 recall: 24.46809% 	 f1: 0.27059 	 algo_results_count: 228
# [top_repositories_by_contributors_count_also_in_awesome_repositories_percentage       ] precision: 28.50877% 	 recall: 23.04965% 	 f1: 0.2549 	 algo_results_count: 228
# mine: 69, bench: 65, mine_not_in_bench: 18, bench_not_in_mine: 14, both: 51,
# mine found in awesome but not in benchmark: {'watchdog', 'schematics', 'django-taggit', 'deform', 'vcrpy', 'pudb', 'django-activity-stream', 'django-shop', 'sh', 'model_mommy', 'factory_boy', 'cornice', 'tablib', 'vispy', 'django-devserver', 'freezegun', 'pip-tools', 'twython'}
# benchmark found in awesome but not in mine: {'pydal', 'thefuck', 'thumbor', 'coala', 'errbot', 'mxnet', 'statsmodels', 'spyder', 'zipline', 'faker', 'xgboost', 'pymc3', 'mrjob', 's3cmd'}
# both mine and benchmark found from awesome: {'django-debug-toolbar', 'mkdocs', 'flask-restful', 'dask', 'mezzanine', 'bokeh', 'supervisor', 'peewee', 'pelican', 'rq', 'virtualenv', 'mongoengine', 'django-allauth', 'conda', 'sanic', 'fabric', 'beets', 'flower', 'falcon', 'feincms', 'django-crispy-forms', 'cookiecutter', 'django-storages', 'urllib3', 'eve', 'sympy', 'keras', 'nikola', 'paramiko', 'django-oauth-toolkit', 'django-guardian', 'channels', 'ansible', 'django-pipeline', 'python-social-auth', 'requests', 'luigi', 'gunicorn', 'sphinx', 'werkzeug', 'oauthlib', 'kafka-python', 'pyinstaller', 'salt', 'splinter', 'hypothesis', 'pyenv', 'webassets', 'gensim', 'flask-admin', 'django-haystack'}
