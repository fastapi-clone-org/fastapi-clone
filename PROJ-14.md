# PROJ-14 — Improve OpenAPI documentation for response-model field filtering

## Issue type

Story

## Summary

Make the response-model tutorial clearer about how undeclared fields are filtered from API responses and represented in generated documentation.

## Priority

Medium

## Status

To Do

## Component

Documentation and OpenAPI

## Labels

`documentation`, `openapi`, `response-model`, `developer-experience`

## Description

Response models are commonly used to prevent internal fields from being exposed to API consumers. The tutorial should give readers a concise, verifiable explanation of the filtering behavior and the corresponding generated OpenAPI contract.

## Acceptance criteria

The response-model tutorial must include a complete, reader-facing example in which an application returns an object containing both public fields and at least one internal-only field, while the declared response model exposes only the public fields. The example must show a successful request and its JSON response, clearly demonstrating that the internal-only field is absent from the payload received by the client and explaining that response-model filtering occurs before data is sent. The accompanying source example must remain executable, use the project’s current supported typing style, and avoid introducing new framework behavior or configuration options. Focused automated coverage must exercise the endpoint with input that includes the internal-only field, assert a successful HTTP response, assert the expected public fields and values, and explicitly assert that the internal-only field is not present in the response body. The generated OpenAPI schema must continue to describe the response using the public response model rather than the input or internal model, and coverage must verify the relevant response schema reference or fields without relying solely on a full-schema snapshot. Existing behavior for valid requests must remain unchanged apart from the intended response filtering demonstration, and no unrelated tutorials, documentation pages, request-validation behavior, error formats, or public API contracts may be modified. The completed change must be limited to the relevant tutorial example, its documentation, and focused tests, must follow existing formatting conventions, and must include enough context for a developer reading the tutorial to understand why a response model is appropriate for preventing accidental exposure of sensitive or internal data.

## Out of scope

- Adding authentication or authorization behavior.
- Changing global response serialization behavior.
- Revising unrelated response-model tutorials.

## Definition of done

- The acceptance criteria are met.
- Relevant validation is run, or any environment limitation is documented.
- The implementation commit references `PROJ-14`.
