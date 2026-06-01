# Reports

Codex reports record what changed, what was checked, and what should happen next. Each completed Codex task should produce a report in the corresponding stage directory.

The report is the handoff artifact from Codex back to ChatGPT review. It must be factual, auditable, and tied to the Git state of the repository.

Use reports for repository edits, command execution, and state-transition preparation. Do not use full CODEX reports for non-state-changing physics notes.

A report should include:

* concrete task name;
* task ID or slug;
* human-readable stage;
* internal stage anchor, if needed;
* base commit;
* final commit;
* branch or worktree name;
* files changed;
* summary of changes;
* commands run with exit code;
* environment;
* artifacts produced;
* checks passed;
* checks failed;
* known limitations;
* deviations from task instructions;
* forbidden actions avoided;
* recommended next task.

When applicable, explicitly state:

No model or claim was promoted to validated status.

Use `docs/reports/CODEX-REPORT-TEMPLATE.md` for new reports.
