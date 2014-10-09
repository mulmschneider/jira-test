#!/usr/bin/python

from jira.client import JIRA


jira = JIRA(basic_auth=('Alice', 'alice'), options={ 'server': 'https://ulmi-test2.atlassian.net'})
issue = jira.issue('DEV-2')
print issue.fields.project.key # 'JRA' 
print issue.fields.issuetype.name # 'New Feature'
print issue.fields.reporter.displayName # 'Mike Cannon-Brookes [Atlassian]'
print issue.fields
