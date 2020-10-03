-- commits_owner_actor_count
select      project_owner, actor, count(*)
from        commits
group by    project_owner, actor

-- distinct_owners_count
select      count(distinct project_owner)
from        commits

-- distinct_repositories_count
select      count(distinct(project_owner, project_name))
from        commits

-- distinct_awesome_python_owners_found_in_commits
select      distinct owner
from        awesome_python
where       owner in (select    project_owner
                      from      commits)

-- awesome_python_repositories_found_in_commits
select      owner, repo
from        awesome_python
where       (owner, repo) in (select    project_owner, project_name
                              from      commits)

-- top_repositories_by_contributors_count
select project_owner as owner, project_name as repo
from (
    select project_owner, project_name, actor
    from commits
    group by (project_owner, project_name, actor)
) dis
group by (project_owner, project_name)
order by count(*) desc
limit
