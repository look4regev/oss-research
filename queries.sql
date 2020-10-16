-- commits_owner_actor_count
select      project_owner, actor, count(*)
from        commits
group by    project_owner, actor

-- distinct_owners_count
select      count(distinct project_owner)
from        commits

-- distinct_repositories_count
select      count(distinct project_name)
from        commits

-- distinct_awesome_python_owners_found_in_commits
select      distinct owner
from        awesome_python
where       owner in (select    project_owner
                      from      commits)

-- awesome_python_repositories_found_in_commits
select      repo
from        awesome_python
where       repo in (select    project_name
                     from      commits)

-- top_repositories_by_contributors_count
select project_name as repo
from (
    select project_name, actor
    from commits
    group by (project_name, actor)
) dis
group by project_name
order by count(*) desc
limit

-- top_repositories_by_contributors_pr_grade_sum
select project_name as repo
from (
    select c.project_name, c.actor, u.grade
    from commits c
    join user_pr_grade u on c.actor = u.owner_actor
    group by (c.project_name, c.actor, u.grade)
) dis
group by project_name
order by sum(grade) desc
limit

-- top_owners_by_contributors_count
select project_owner
from (
    select project_owner, project_name, actor
    from commits
    group by (project_owner, project_name, actor)
) dis
group by project_owner
order by count(*) desc
limit

-- repos_of_owners
select distinct project_name
from commits
where project_owner in

-- get_organizations
select distinct project_owner
from commits
where project_owner not in (select distinct actor from commits)

-- get_distinct_actors_of_owner
select distinct actor
from commits
where project_owner =

-- get_repos_of_top_pr_actors
select c.project_owner, c.project_name, c.actor, u.grade
from commits c
join user_pr_grade u on c.actor = u.owner_actor
group by (c.project_owner, c.project_name, c.actor, u.grade)
order by u.grade desc
limit

-- get_repos_of_top_pr_actors_and_indication_to_whether_it_is_awesome
select c.project_owner, c.project_name, c.actor, u.grade, a.repo
from commits c
join user_pr_grade u on c.actor = u.owner_actor
left join awesome_python a on c.project_owner = a.owner and c.project_name = a.repo
group by (c.project_owner, c.project_name, c.actor, u.grade, a.repo)
order by u.grade desc
limit
