# Changelog

## [1.13.1](https://github.com/ZeitOnline/deployment-notify/compare/1.13.0...1.13.1) (2026-10-30)


### Maintenance

* release with Release Please via the shared pypi-release workflow ([#5](https://github.com/ZeitOnline/deployment-notify/issues/5)) ([44cf5d6](https://github.com/ZeitOnline/deployment-notify/commit/44cf5d6db6083908f9f69adc6f424fdbaad8023c))

## 1.13.0 (2026-01-08)

- Implement gha-workflow command to send repository_dispatch event to GHA (gha)

## 1.12.0 (2025-09-10)

- jira: Ignore issues that cannot be transitioned (jira)

## 1.11.0 (2025-05-06)

- MAINT: Consider ES project when updating Jira tickets (jira-project)

## 1.10.2 (2025-04-25)

- Correctly return empty changelog diff (empty)

## 1.10.1 (2025-04-23)

- Return empty changelog diff if previous version equals current version (previous)

## 1.10.0 (2025-02-27)

- Specify separate title for postdeploy message (postdeploy)

## 1.9.1 (2025-02-25)

- Ignore status Backlog by default (jira)

## 1.9.0 (2025-02-20)

- Move printing of changelog diff to CLI for reusability (printdiff)

## 1.8.1 (2024-12-11)

- Retrieve workloadVersion, not appVersion from keptn context (keptn)

## 1.7.0 (2024-12-10)

- Make retrieving the changelog from tag configurable (jira)

## 1.6.0 (2024-10-18)

- WCM-457: new custom command slack-reminder (reminder)
- WCM-457: new custom command slack-reminder (reminder)

## 1.5.0 (2024-08-07)

- issues: Support multiple issue prefixes (issues)
- jira: Select jira status by name insead of id (jira)

## 1.4.1 (2024-07-30)

- ZO-5636: Set all hny dataset as default (ZO-5636)

## 1.4.0 (2024-07-30)

- ZO-5636: Support honeycomb environments marker (ZO-5636)

## 1.3.0 (2024-02-22)

- Update to keptn-0.10 context API (keptn)

## 1.2.3 (2024-01-17)

- Fix jira status change (jira)

## 1.2.2 (2024-01-16)

- Don't set jira status if status is already 'more done' (jira)

## 1.2.1 (2024-01-11)

- Detect empty postdeploy properly (postdeploy)

## 1.1.1 (2024-01-08)

- Quote changelog text correctly for slack (changelog)

## 1.1.0 (2024-01-08)

- ZO-4171: Implement posting the changelog diff to slack (changelog)

## 1.0.4 (2024-01-08)

- postdeploy: Retrieve changelog of the deployed version (postdeploy)

## 1.0.3 (2023-12-18)

- Fix jira changelog parsing (jira)

## 1.0.2 (2023-12-18)

- Fix bugsnag cli parsing (bugsnag)

## 1.0.1 (2023-12-18)

- Allow calling multiple tasks in a single invocation (chain)

## 1.0.0 (2023-12-13)

- Initial release (initial)
