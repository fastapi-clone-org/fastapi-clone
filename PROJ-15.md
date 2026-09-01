# PROJ-15 — Document and verify response-model field exclusion

## Issue type

Story

## Summary

Clarify how response models exclude internal fields from API responses and add focused coverage for the documented behavior.

## Priority

Medium

## Status

To Do

## Component

Documentation, response models, and OpenAPI

## Labels

`documentation`, `response-model`, `openapi`, `security`

## Description

Response models help applications expose only the fields intended for API consumers. The existing tutorial should more clearly demonstrate the distinction between an internal input model and the public response model, including the response payload a client receives and the corresponding generated OpenAPI contract.

This work is intentionally planned in two delivery increments. The first increment establishes the documented example and validates the successful response path. The second increment completes the contract-level and regression coverage needed to ensure the filtering behavior remains correctly represented over time.

## Acceptance criteria

### Increment 1 — documentation and response behavior

- The relevant response-model tutorial explains that fields excluded from the declared response model are not returned to API consumers.
- The tutorial includes a request/response example where submitted input includes an internal-only field and the returned JSON excludes that field.
- Focused coverage verifies a successful request and confirms that the response contains the expected public fields.

### Increment 2 — contract and regression coverage

- Focused coverage explicitly asserts that the internal-only field is absent from the response body.
- The generated OpenAPI schema describes the successful response with the public response model, not the input model containing the internal-only field.
- The relevant schema assertion verifies the public response model reference or fields without relying only on a complete schema snapshot.
- No unrelated tutorials, request validation behavior, error formats, or public API contracts are changed.

## Out of scope

- Adding authentication or authorization features.
- Changing global response serialization behavior.
- Revising unrelated response-model examples.

## Definition of done

- Both acceptance-criteria increments are complete.
- Relevant validation is run, or any local environment limitation is documented.
- Each implementation commit references `PROJ-15`.
