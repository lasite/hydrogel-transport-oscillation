# Workflow Evaluation

## Purpose

Evaluate the AI-assisted research workflow using evidence from completed tasks rather than intuition.

This file is for workflow retrospectives only. It does not validate the physical model, numerical results, or manuscript claims.

## Retrospective cadence

Review the workflow after every three to five completed Codex tasks, or after any task that causes major rework.

## Metrics

For each retrospective, record:

1. Scientific progress: which blocker was reduced, and whether it was P0, P1, or P2.
2. Error rate: whether ChatGPT or Codex produced unsupported claims, wrong equations, wrong boundary signs, stale status, or unauthorized state promotion.
3. Verification quality: whether the correct commands were run and exit codes recorded.
4. Rework cost: whether unclear scope, stale tests, oversized context, or excessive formality caused rework.
5. Formality friction: whether more effort went into template compliance than physical reasoning.

## Adjustment rules

If formality friction is high and no state transition occurred, convert similar future work into a physics note.

If Codex changes files outside scope or omits evidence, tighten TASK allowed files, forbidden actions, and acceptance criteria.

If reports omit command outcomes, add a structural check to `make quickcheck`.

If claims are strengthened without evidence, tighten the claim-evidence and validated-status gate rather than adding ceremony to all tasks.

Record durable workflow decisions as ADRs under `docs/decisions/`.
