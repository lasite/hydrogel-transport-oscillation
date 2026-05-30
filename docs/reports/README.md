# Reports

Codex reports record what changed, what was checked, and what should happen next. Each completed task should produce a report in the corresponding stage directory.

The report is the handoff artifact from Codex back to ChatGPT review. It must be factual, auditable, and tied to the Git state of the repository.

# CODEX Report Template

## Task ID

## Base commit

## Final commit

## Branch or worktree name

## Files changed

## Summary of changes

## Commands run

Include exit code for each command.

## Environment

* OS if known:
* Python version:
* Dependency setup command used:

## Artifacts produced

## Checks passed

## Checks failed

## Known limitations

## Deviations from task instructions

## Forbidden actions avoided

When applicable, explicitly state:

No model or claim was promoted to validated status.

## Next recommended task

Use `docs/reports/CODEX-REPORT-TEMPLATE.md` for new reports.
