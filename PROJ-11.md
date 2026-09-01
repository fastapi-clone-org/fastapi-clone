# PROJ-11 — Add regression coverage for query parameter aliases

## Issue type

Bug

## Summary

Ensure query parameter aliases are consistently documented in the generated OpenAPI schema.

## Priority

Medium

## Status

To Do

## Component

Request validation

## Labels

`bug`, `openapi`, `query-parameters`

## Description

Query parameter aliases allow API consumers to use request names that differ from the Python function argument. The tutorial example demonstrates this behavior at runtime, but its generated OpenAPI contract is not explicitly protected by focused regression coverage.

Add coverage that verifies the alias is exposed to API consumers in the generated schema and that the Python parameter name does not leak into the public query-parameter contract.

## Acceptance criteria

- The generated OpenAPI schema exposes the configured public query parameter name.
- The schema identifies the parameter as a query parameter and preserves its optional status.
- The internal Python function argument name is not presented as the public query parameter name.
- Existing runtime behavior for requests using the alias remains covered.
- Changes are limited to the relevant tutorial example and its focused test coverage.

## Out of scope

- Changing alias behavior in the framework.
- Introducing new parameter configuration options.
- Updating unrelated OpenAPI schemas or tutorials.

## Definition of done

- All acceptance criteria are met.
- Relevant validation is run, or any local environment limitation is documented.
- The implementation commit references `PROJ-11`.
