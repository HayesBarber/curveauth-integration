# curveauth-integration

This project ensures that signatures and key exchanges between library implementations of curveauth are interoperable.

## Structure

- `scripts/`: Language-specific utilities for testing
- `tests/`: Cross-language tests (e.g., Dart signs, Python verifies)

## Usage

Run the tests:

```bash
pytest
```

Ensure both Dart and Python dependencies are installed. Python dependencies are listed in `requirements.txt`; Dart dependencies in `pubspec.yaml`.
