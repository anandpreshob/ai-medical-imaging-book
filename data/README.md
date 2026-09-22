# Catalog scope and maintenance

These CSVs power the chapter tables and the three reference directories. The non-CXR entries were reviewed for this edition on **2026-09-22**; the CXR rows retain their earlier source-review notes. This is a selected educational directory, not a complete market survey, endorsement, or guarantee of current availability.

- `datasets.csv`: counts refer to the named release and unit. Where releases differ, the table deliberately gives no combined count. Access agreements and image rights must be checked at the source.
- `models.csv`: distinguish code, weights, data, and clinical-use terms. `any` means a reusable development framework or model family, not proven compatibility with every modality. Pin an exact checkpoint and inspect its input contract.
- `fda-products.csv`: each row links to a specific historical FDA submission. A 510(k) clearance and a De Novo authorization are different pathways. Names, ownership, versions, and current labeling can change; consult the actual applicable device documentation before implementation. This table includes quantitative software and does not claim every entry uses deep learning.

Modality keys: `cxr` chest radiography; `ct` computed tomography; `mri` magnetic resonance; `us` ultrasound/echo; `mammo` mammography/DBT; `nm` nuclear medicine; `ophtho` ophthalmic imaging; `video` endoscopy/surgery; `path` pathology; `derm` dermatology; `ecg` electrocardiography; `any` general development resources.

To update: edit a CSV with proper quoting, retain a primary source URL, qualify release and task scope, and render the book. Do not copy a product family's marketing claims into the indication of one submission. The renderer is `scripts/book_catalog.py` and uses Python's standard library.
