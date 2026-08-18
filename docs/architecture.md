# Architecture

The application is intentionally small. Flask handles three pages and one JSON endpoint, while the project logic lives under `src/`.

```text
browser
   |
   v
Flask /api/analyze
   |
   +-- payload validation
   +-- reference-range analysis
   +-- model input preparation
   +-- serialized Random Forest inference
   |
   v
JSON response -> results page
```

The model is loaded once when the application starts. Missing numeric inputs are rebuilt in the original training-column order and passed through the saved median imputer before inference.
