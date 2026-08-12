# PROJ-1: Add max_length constraint example to query parameter validation tutorial

## Description

The query parameter validation tutorial (`docs_src/query_params_str_validations/tutorial006_py310.py`) currently demonstrates `min_length` on the `q` query parameter but does not demonstrate `max_length`. Add a `max_length=50` constraint alongside the existing `min_length` constraint on the same parameter, so the example shows both together.

## Acceptance criteria

- The `q` query parameter demonstrates both `min_length=3` and `max_length=50`.
- No unrelated changes are included.
