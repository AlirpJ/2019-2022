## ITMD 362, Production Problem 04: GitHub Team Repos and Pull Requests

For this Production Problem, you and your team for Project Two are going to establish a GitHub
Organization (see https://help.github.com/articles/creating-a-new-organization-account/), create a
shared team repository within the organization, and then fork individual repositories for Project
Two. You will also practice submitting a pull request.

1. **Before you can do this Production Problem, you have to establish a team of three or four
students, including yourself. Organize into teams however you’d like, including on the find-a-team
Basecamp thread, and then choose as a team what coordination software you will use to communicate
(e.g., your own Basecamp project [NOT the class-wide one], Slack, Discord, or something else).

Write the name of the communication service your team has decided to use:

2. **Only one member of your team should complete this step.** In your project coordination software
of choice, discuss and choose one member who will create the free GitHub Organization account for
your team, as well as your shared Project Two repository in that organization. **Again, only one
member of your team should complete this step.**

That member can click the + (plus sign) next to their avatar, or go straight to
https://github.com/organizations/new to create a new organization for your team. As part of that
process, the member creating the organization should also invite the other team members to join (be
sure to share GitHub usernames in your project coordination software of choice). GitHub may also ask
you to take a survey, which you can take or just skip. Finally, create a new repository within the
organization. Initializing it on GitHub with a `README.md` file is fine, unless you’ve already begun
a repository on a team member’s computer. **That will be your shared repository for Project Two.**

3. Copy and paste the URL for your team’s GitHub organization here: https://github.com/ITMD362-Team-BEJJ

4. Copy and paste the URL showing your team’s GitHub organization members here: https://github.com/orgs/ITMD362-Team-BEJJ/people

5. Copy and paste the URL for your team’s shared repository for Project Two here: https://github.com/ITMD362-Team-BEJJ/project2

6. Each member of the team should then fork the team repository from within the team organization
on GitHub (so, too, should the team member who created the GitHub organization for your project).

Copy and paste the URL for your personal fork of the repository here: https://github.com/AlirpJ/project2

7. Each member of the team should clone their forked copy of the repository to their local
computer. Once you have cloned the forked copy, you should add the *upstream*, team repository as a
second remote. Run `git remote add upstream` followed by the URL for your team’s repository.

Write or copy & paste the output of `git remote -v` from your copy of the forked repository here:

origin  git@github.com:AlirpJ/project2.git (fetch)

origin  git@github.com:AlirpJ/project2.git (push)

upstream        https://github.com/ITMD362-Team-BEJJ/project2 (fetch)

upstream        https://github.com/ITMD362-Team-BEJJ/project2 (push)

8. Next, on a feature branch called `self-intro`, all team members should add their names to the
`README.md` file, along with brief sentence or two of what the member believes are his/her primary
strengths. Prior to creating the `self-intro` branch, be sure to pull from the remote repo (`git
pull upstream main`) to get any other team members’ names and strengths. Add and commit your own
work, and push to your own repository (`git push origin self-intro`).

Copy and paste the URL of your pull request here: https://github.com/AlirpJ/project2/pull/1

9. Finally, within your fork of the repository on GitHub, open up a pull request from your
`self-intro` branch to `main` branch in the shared  repository. Each team member should review the
pull request before it is merged, and then pull from the team repository to have a complete,
up-to-date `README.md` file.


https://github.com/ITMD362-Team-BEJJ/project2/pull/1
