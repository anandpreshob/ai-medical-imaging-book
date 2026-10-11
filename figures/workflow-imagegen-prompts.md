# Generated workflow and evaluation figures

Created 2026-10-11 with the built-in image generation tool using the imagegen skill. These ten PNGs replace all ten SVG figures previously displayed in chapters 11 and 20–22. SVGs and their regeneration scripts are retained as archives. Real chest radiographs remain unchanged. All image-like thumbnails within the new figures are synthetic illustrations, not patient studies. Labels and arrows were visually reviewed; numbers in the workload example are hypothetical. The projection drawing is qualitative, not a ray-tracing or scale reference.

## ch11/projection-geometry.png

Title: Why projection changes apparent size

Prompt:

```text
Use case: scientific-educational. Asset type: final landscape medical textbook figure. Title (verbatim): "Why projection changes apparent size". Primary request: Two side-by-side precise geometrical ray schematics, each with an X-ray point source on left, upright object and detector on right. Equal source-to-detector distance and equal object height. Left object close to detector, small projected shadow. Right object farther from detector, larger projected shadow. Divergent rays pass exactly through both object endpoints to corresponding shadow endpoints. Labels only: 'Near detector', 'Farther from detector', 'Source', 'Object', 'Detector', 'Smaller shadow', 'Larger shadow'. Avoid claiming PA/AP alone causes every silhouette change. Style: polished editorial medical illustration, crisp precise infographic, subtle dimension in icons, navy and teal with muted coral on clean warm white background, large highly legible sans-serif labels, generous whitespace. Landscape 3:2 composition. All text must be accurate, sparse, readable, and never overlap. A small footer "Illustrative teaching figure". No watermark, no brand logos, no patient identifiers. Make scientific relationships explicit and correct.
```

## ch11/evaluation-splits.png

Title: Split patients before images

Prompt:

```text
Use case: scientific-educational. Asset type: final landscape medical textbook figure. Title (verbatim): "Split patients before images". Primary request: Patient cards each contain three small radiograph thumbnails. Three separated lanes labeled 'Training', 'Validation', 'Internal test'; every card and its thumbnails stay wholly in one lane. A fourth visually separate lane 'External site test' contains new patient cards from another building. No arrow from test back to training. Footer 'Keep every patient and derivative in one partition'. Style: polished editorial medical illustration, crisp precise infographic, subtle dimension in icons, navy and teal with muted coral on clean warm white background, large highly legible sans-serif labels, generous whitespace. Landscape 3:2 composition. All text must be accurate, sparse, readable, and never overlap. A small footer "Illustrative teaching figure". No watermark, no brand logos, no patient identifiers. Make scientific relationships explicit and correct.
```

## ch11/triage-workload.png

Title: What 1,000 studies mean for workload

Prompt:

```text
Use case: scientific-educational. Asset type: final landscape medical textbook figure. Title (verbatim): "What 1,000 studies mean for workload". Primary request: Exact confusion matrix infographic, four equally sized labeled cells; no falsely proportional icon counts. Column labels 'Disease present', 'Disease absent'; row labels 'Flagged', 'Not flagged'. Values and labels: '45 true positives', '95 false positives', '5 false negatives', '855 true negatives'. Clear notes: '140 flags', 'PPV = 32.1%', 'Sensitivity = 90%', 'Specificity = 90%', 'Illustrative prevalence: 5%'. These are hypothetical numbers, not measured model performance. No additional statistics. Style: polished editorial medical illustration, crisp precise infographic, subtle dimension in icons, navy and teal with muted coral on clean warm white background, large highly legible sans-serif labels, generous whitespace. Landscape 3:2 composition. All text must be accurate, sparse, readable, and never overlap. A small footer "Illustrative teaching figure". No watermark, no brand logos, no patient identifiers. Make scientific relationships explicit and correct.
```

Accepted revision prompt:

```text
Edit this medical textbook confusion matrix. Remove ALL human silhouettes and pictogram arrays from the four matrix cells; they imply misleading counts. Keep the matrix values 45, 95, 5, 855, row/column labels, 140 flags, PPV 32.1%, sensitivity 90%, specificity 90%, prevalence 5%, and hypothetical disclaimer exactly unchanged. Keep overall layout, palette and large type. Plain whitespace above each number, no replacement icons. Everything else unchanged.
```

## ch11/agent-workflow.png

Title: A reviewed chest X-ray workflow

Prompt:

```text
Use case: scientific-educational. Asset type: final landscape medical textbook figure. Title (verbatim): "A reviewed chest X-ray workflow". Primary request: Four clear panels connected left to right: 'Check eligibility' radiograph plus metadata checklist; 'Retrieve evidence' source-linked priors and supporting documents; 'Prepare draft' evidence-linked report marked 'Draft'; 'Clinician review' clinician checks source image before signoff. A branch from eligibility labeled 'Unsupported / exception' leads to 'Routine reading'. Final smaller arrow after clinician review to 'Sign and track follow-up'. Automation does not sign or diagnose autonomously. Style: polished editorial medical illustration, crisp infographic, subtle dimension in icons, navy and teal with muted coral on warm white background, large highly legible sans-serif labels, generous whitespace. Landscape 3:2. All text accurate, sparse, readable, never overlapping. Small footer "Illustrative teaching figure". No logos, no real patient identifiers. Scientific relationships explicit and correct.
```

Accepted revision prompt:

```text
Edit this chest X-ray educational workflow. In the first panel, replace the entire checklist and its existing examples with exactly three bullets: 'Supported acquisition', 'Required metadata present', 'Adequate image quality'. Remove 'Indication present', 'No exclusion criteria', and ALL parenthetical exclusion examples (postoperative, portable only, research). Replace the caption 'Eligible for AI-assisted workflow' with 'Eligible for the defined task'. Preserve the other stages, routine-reading exception branch and human-review-before-signing flow. Avoid adding extra medical eligibility rules or examples. Keep visual style and layout unchanged.
```

## ch20/measurement.png

Title: Three different kinds of numbers

Prompt:

```text
Use case: scientific-educational. Asset type: final landscape medical textbook figure. Title (verbatim): "Three different kinds of numbers". Primary request: Three parallel equal-size illustrated panels, clearly separate, with no arrows implying interchangeability. 'Native measurement': calibrated DXA acquisition with native numerical measurement. 'Cross-modal estimate': CT image paired with model prediction for a target measure. 'Extracted report value': OCR on existing report with source highlight. Each uses a simple corresponding instrument or evidence illustration. Footer 'Validate measurement, prediction, and extraction separately'. No fake numerical values or invented precision. Style: polished editorial medical illustration, crisp infographic, subtle dimension in icons, navy and teal with muted coral on warm white background, large highly legible sans-serif labels, generous whitespace. Landscape 3:2. All text accurate, sparse, readable, never overlapping. Small footer "Illustrative teaching figure". No logos, no real patient identifiers. Scientific relationships explicit and correct.
```

## ch20/router.png

Title: Route by representation and task

Prompt:

```text
Use case: scientific-educational. Asset type: final landscape medical textbook figure. Title (verbatim): "Route by representation and task". Primary request: Readable branching workflow 'Identify input' original waveform, CT volume, and photograph icons, then 'Check prerequisites' source identity, units, geometry, quality. Branch into 'Supported tool' with output then human review, and 'Unsupported / incomplete' with clear 'No result'. No route from unsupported to valid diagnosis. Minimal explanatory labels and spacious routed arrows; no tangled crossings. Style: polished editorial medical illustration, crisp infographic, subtle dimension in icons, navy and teal with muted coral on warm white background, large highly legible sans-serif labels, generous whitespace. Landscape 3:2. All text accurate, sparse, readable, never overlapping. Small footer "Illustrative teaching figure". No logos, no real patient identifiers. Scientific relationships explicit and correct.
```

## ch21/architecture.png

Title: A traceable imaging AI platform

Prompt:

```text
Use case: scientific-educational. Asset type: final landscape medical textbook figure. Title (verbatim): "A traceable imaging AI platform". Primary request: Spacious systems illustration of four labeled functional stations: 'Browser viewer', 'Authenticated gateway', 'Orchestrator and workers', 'Reviewed results'. PACS archive connected to gateway, worker model outputs return to viewer for clinician review, accepted result export to 'Clinical record'. Do not depict direct unauthenticated viewer-to-PACS or unreviewed worker-to-clinical-record arrow. Use clear, sparse arrows with tiny labels 'Retrieve', 'Versioned job', 'Draft output', 'Review', 'Accepted export'. Footer 'Source → transforms → model → review → record'. Depict logical responsibilities, not vendor product screenshots. Style: polished editorial medical illustration, crisp infographic, subtle dimensional icons, navy and teal with muted coral on warm white background, large legible sans-serif labels, generous whitespace. Landscape 3:2. All labels accurate, sparse, readable, never overlapping. Do not add paragraphs or unsolicited text. Small footer "Illustrative teaching figure". No logos or patient identifiers. Scientific relationships explicit and correct.
```

## ch21/lifecycle.png

Title: A computation is not an accepted result

Prompt:

```text
Use case: scientific-educational. Asset type: final landscape medical textbook figure. Title (verbatim): "A computation is not an accepted result". Primary request: State workflow exact labels 'Eligible', 'Queued', 'Running', 'Draft', 'Reviewed', 'Exported'. Distinct visual gate before Reviewed labeled 'Human acceptance'. Branch from Running to 'Failed' and 'Canceled'; both terminal states feed small 'Audit trail' log, do not become success. Reviewed can lead to Exported, which records version and source identity. Side note 'Preserve edits and superseded versions'. Spacious two-row composition with unambiguous arrows. Style: polished editorial medical illustration, crisp infographic, subtle dimensional icons, navy and teal with muted coral on warm white background, large legible sans-serif labels, generous whitespace. Landscape 3:2. All labels accurate, sparse, readable, never overlapping. Do not add paragraphs or unsolicited text. Small footer "Illustrative teaching figure". No logos or patient identifiers. Scientific relationships explicit and correct.
```

## ch22/fairness.png

Title: Who benefits across the care pathway?

Prompt:

```text
Use case: scientific-educational. Asset type: final landscape medical textbook figure. Title (verbatim): "Who benefits across the care pathway?". Primary request: Four connected illustrated stages: 'Access and acquisition', 'Valid output', 'Clinical action', 'Completed care'. Show diverse people in non-stereotyped neutral illustrations and source images, quality checks, review and follow-up. At every stage a small branch to 'Unresolved cases' retained in a visible lower tally, do not silently remove excluded people. Footer 'Keep denominators, uncertainty, and failures visible'. This diagram makes no numeric fairness or demographic performance claims. Style: polished editorial medical illustration, crisp infographic, subtle dimensional icons, navy and teal with muted coral on warm white background, large legible sans-serif labels, generous whitespace. Landscape 3:2. All labels accurate, sparse, readable, never overlapping. Do not add paragraphs or unsolicited text. Small footer "Illustrative teaching figure". No logos or patient identifiers. Scientific relationships explicit and correct.
```

## ch22/lifecycle.png

Title: Responsible change control

Prompt:

```text
Use case: scientific-educational. Asset type: final landscape medical textbook figure. Title (verbatim): "Responsible change control". Primary request: Four-stage spacious clockwise workflow 'Propose change' → 'Evaluate evidence' → 'Controlled release' → 'Monitor and respond'. Distinct monitoring branch 'Adverse signal' → 'Investigate / roll back' and return to evidence review. Release includes ownership and version; review includes technical, clinical and subgroup evidence. Use calm medical textbook editorial illustration with sparse labels; rollback visually explicit. Style: polished editorial medical illustration, crisp infographic, subtle dimensional icons, navy and teal with muted coral on warm white background, large legible sans-serif labels, generous whitespace. Landscape 3:2. All labels accurate, sparse, readable, never overlapping. Do not add paragraphs or unsolicited text. Small footer "Illustrative teaching figure". No logos or patient identifiers. Scientific relationships explicit and correct.
```
