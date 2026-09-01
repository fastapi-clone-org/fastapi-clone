# PROJ-12 — Preserve validation metadata for optional string query parameters

## Issue type

Bug

## Summary

Ensure optional string query parameters retain declared validation metadata in the generated OpenAPI schema.

## Priority

Medium

## Status

To Do

## Component

OpenAPI and request validation

## Labels

`bug`, `openapi`, `query-parameters`, `validation`

## Description

Optional string query parameters can combine a default value with validation constraints. API consumers rely on the generated OpenAPI contract to discover those constraints before submitting requests.

Add focused regression coverage for an optional string query parameter with a default value and length validation. The coverage must confirm that the public schema accurately exposes the parameter's optional status, default value, and validation constraints.

## Acceptance criteria

- The generated OpenAPI schema marks the query parameter as optional.
- The declared default value is included in the parameter schema.
- The configured string length validation is included in the parameter schema.
- Runtime coverage confirms that an omitted parameter resolves to its default value.
- Runtime coverage confirms that an invalid provided value receives a validation error.

## Out of scope

- Changing framework-level validation behavior.
- Adding new query parameter configuration options.
- Updating unrelated tutorial examples or API schemas.

## Definition of done

- All acceptance criteria are met.
- Relevant validation is run, or any local environment limitation is documented.
- The implementation commit references `PROJ-12`.
