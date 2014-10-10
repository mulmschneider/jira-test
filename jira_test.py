#!/usr/bin/python
#click?

from jira.client import JIRA
import inspect
import pprint


jira = JIRA(basic_auth=('Alice', 'alice'), options={ 'server': 'https://ulmi-test2.atlassian.net'})
issue = jira.issue('DEV-2')
print issue.fields.project.key # 'JRA' 
print issue.fields.issuetype.name # 'New Feature'
print issue.fields.reporter.displayName # 'Mike Cannon-Brookes [Atlassian]'
#issue.update(customfield_10025=['develop', 'next', 'stage1'])
pp.pprint(inspect.getmembers(issue.fields()))
#new_issue= jira.create_issue(project={'key' : 'DEV'}, summary='Auto-created bug', description='This bug was created via the jira python API', issuetype={'name': 'Bug'})
