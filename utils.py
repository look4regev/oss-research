from functools import lru_cache

import psycopg2

from settings import DB_PASSWORD, DB_NAME


def _queries_file_read_sql():
    queries = {}
    sql = ""
    sql_name = ""
    with open("queries.sql", "rt") as queries_file:
        for line in queries_file.readlines():
            if line.startswith("-- "):
                if sql:
                    queries[sql_name] = sql
                    sql = ""
                sql_name = line.split("-- ")[1][:-1]
            else:
                sql += line
    queries[sql_name] = sql
    return queries


_QUERIES = _queries_file_read_sql()


def _single_tuples_strip(cursor):
    return list([tup[0] for tup in cursor])


def get_commits_owner_actor_count():
    return _get_cursor(_QUERIES["commits_owner_actor_count"])


def get_distinct_owners_count():
    return _get_one(_QUERIES["distinct_owners_count"])[0]


def get_distinct_repositories_count():
    return _get_one(_QUERIES["distinct_repositories_count"])[0]


def get_distinct_awesome_python_owners_found_in_commits():
    return _single_tuples_strip(_get_cursor(_QUERIES["distinct_awesome_python_owners_found_in_commits"]))


def get_awesome_python_repositories_found_in_commits():
    return _get_cursor(_QUERIES["awesome_python_repositories_found_in_commits"])


def get_awesome_python_repositories_distinct_found_in_commits():
    return _single_tuples_strip(_get_cursor(_QUERIES["awesome_python_repositories_distinct_found_in_commits"]))


def get_top_repositories_by_contributors_count(limit):
    return _get_cursor(_QUERIES["top_repositories_by_contributors_count"] + str(limit))


def get_top_owners_by_contributors_count(limit):
    return _single_tuples_strip(_get_cursor(_QUERIES["top_owners_by_contributors_count"] + str(limit)))


def get_repos_of_owners(owners):
    owners_csv = "','".join(owners)
    owners_csv_in_sql = f"('{owners_csv}')"
    return _single_tuples_strip(_get_cursor(_QUERIES["repos_of_owners"] + owners_csv_in_sql))


def _get_cursor(sql):
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute(sql)
    return cur


def _get_one(sql):
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute(sql)
    fetched = cur.fetchone()
    cur.close()
    return fetched


@lru_cache()
def _get_conn():
    print(f"connecting to db {DB_NAME}")
    return psycopg2.connect(f"dbname={DB_NAME} user=supergod password={DB_PASSWORD}")
