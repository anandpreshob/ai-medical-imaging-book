# AI in Medical Imaging — Manuscript Plan & Table of Contents

**Author:** Anand Preshob · **Working title:** *AI in Medical Imaging: From Pixels to Practice*
**Audience:** Dual-track — clinicians/medical students AND ML engineers/researchers. Every chapter explains clinical context for engineers and ML concepts for clinicians.
**Companion project:** [MedAI OS](https://github.com/anandpreshob/medai-os) (`medai-os-release`) — the book stands alone, but every applied chapter ends with a hands-on "Doing this in MedAI OS" section.

---

## 1. Vision & Positioning

The book serves three roles at once:

1. **A textbook** — a rigorous, modality-by-modality introduction to AI in medical imaging that a radiology resident or an ML graduate student could learn from cover to cover.
2. **A field guide** — living catalogs of datasets, open-source models, and FDA-cleared products per modality, kept current because the book is a website, not a printed artifact.
3. **A soft on-ramp to MedAI OS** — each applied chapter closes by showing how to actually *do* the things discussed using MedAI OS (upload a chest X-ray, run CheXagent detection, generate a report), without the book depending on MedAI OS to be useful.

**Differentiator:** no existing book combines (a) modality-level clinical grounding, (b) the current dataset/model/product landscape, and (c) a runnable open-source platform the reader can use immediately.

---

## 2. Publishing Architecture

### Stack
- **Quarto book project** (`.qmd` chapters) — citations via BibTeX, cross-references, callouts, dark/light themes, built-in search.
- **GitHub repo** (suggested: `anandpreshob/ai-medical-imaging-book`) — public, so the book itself is a portfolio artifact and accepts community PRs for dataset/product tables.
- **Two mirrors from one source (Option A, decided 2026-08-19):** the book repo's GitHub Action renders on every push to `main` and (1) publishes to GitHub Pages at `anandpreshob.github.io/ai-medical-imaging-book`, and (2) pushes the rendered static HTML into `personal-website/book/`, whose existing Firebase workflow auto-deploys it to **www.anandpreshob.com/book/**. No subdomain needed — the personal site is plain static hosting serving the repo root, so the book folder slots in like the existing `blogs/`.

### Repo layout
```
ai-medical-imaging-book/
├── _quarto.yml              # book config, chapter order, theme
├── index.qmd                # landing page / preface
├── chapters/
│   ├── 01-introduction.qmd
│   ├── 02-universe-of-medical-images.qmd
│   └── ...
├── data/                    # CSVs powering the living tables
│   ├── datasets.csv         # modality, name, size, license, link
│   ├── models.csv           # modality, task, model, weights?, license
│   └── fda-products.csv     # modality, product, vendor, clearance no.
├── figures/
├── references.bib
└── .github/workflows/publish.yml
```

**Living tables pattern:** dataset/model/FDA-product listings live as CSVs rendered into tables at build time. Updating the landscape = editing one CSV row, not rewriting prose. This is what keeps the "field guide" role honest over time.

### Cross-referencing with MedAI OS (both directions)
- **Book → MedAI OS:** every "Doing this in MedAI OS" section links to the exact repo doc (e.g., chest X-ray chapter → `docs/suites/CHEST_XRAY_SUITE_PRD.md`, quick-start blocks adapted from the README's `VITE_FEATURES` flags).
- **MedAI OS → Book:** add a "📖 Learn the concepts" section to the medai-os README and each suite PRD linking to the matching book chapter. Suite auto-detection docs can link to the modality chapters.
- Keep versions loose: the book references stable concepts + linked docs, never pinned line numbers, so the two repos evolve independently.

---

## 3. The Standard Modality-Chapter Template

Every Part III/IV chapter follows the same skeleton (your chest X-ray example, generalized):

1. **What is this modality?** — physics in one page, what the image actually measures, dimensions (2D/3D/4D), typical resolutions and file sizes.
2. **Why and when it's ordered** — clinical indications, where it sits in the diagnostic pathway.
3. **What diagnoses are made from it** — the finding taxonomy a model would need to learn.
4. **How it works in a modern hospital** — acquisition protocol, PACS/RIS flow, who reads it, reporting conventions, turnaround expectations.
5. **The data landscape** — public datasets (living table): size, labels, license, known biases.
6. **The model landscape** — open-source models (living table) and notable closed/commercial ones; what tasks are solved vs. open problems.
7. **FDA-cleared AI products** — living table with clearance numbers; what "cleared" actually covered.
8. **Open challenges** — dataset shift, label noise, deployment gaps specific to this modality.
9. **🔧 Doing this in MedAI OS** — concrete walkthrough mapped to real features (see §5 mapping below).
10. **Further reading + references.**

---

## 4. Table of Contents

### Front matter
- Preface: who this book is for, how to read it (clinician track vs. engineer track), how it relates to MedAI OS
- How to use the living tables & how to contribute

### Part I — The Landscape of Medical Imaging

**Ch. 1 — Introduction: Why AI in Medical Imaging**
The scale problem (imaging volume vs. radiologist supply), a short history from CAD to foundation models, what AI realistically does and doesn't do today, how the book is organized.

**Ch. 2 — The Universe of Medical Images**
The complete modality atlas — every modality, every dimension. Projection radiography (X-ray, mammography, fluoroscopy, DEXA), cross-sectional (CT, MRI and its sequences, PET/SPECT and hybrids), real-time (ultrasound incl. echo and Doppler, endoscopy, surgical video), ophthalmic (fundus, OCT, OCT-A), microscopy-based (pathology/histology WSI, cytology, hematology), dermatology, dental/maxillofacial (OPG, CBCT), and emerging modalities. For each: what it measures, dimensionality (2D / 3D / 2D+t / 3D+t), typical diagnoses. Includes the master modality-×-diagnosis reference table.

**Ch. 3 — How Images Live in a Hospital**
DICOM (the standard, metadata, why it matters for ML), NIfTI/NRRD and research formats, PACS/RIS/EHR, DICOMweb, HL7/FHIR, the acquisition→storage→reading→report loop, de-identification and data governance. *MedAI OS hook: Orthanc PACS + the viewer's DICOM/NIfTI loaders as a live playground.*

### Part II — Foundations: Machine Learning & Computer Vision

**Ch. 4 — Machine Learning: The Concepts**
Supervised / semi-supervised / self-supervised / unsupervised learning, clustering, reinforcement learning; training-validation-test discipline; overfitting; transfer learning, fine-tuning, domain adaptation (the medical-imaging superpower concepts — placed here, before any architecture, per your ordering). Written so a clinician can follow every term.

**Ch. 5 — What Computer Vision Can Do**
The task taxonomy: classification, detection/localization, semantic segmentation, instance segmentation, keypoint/landmark detection, registration, depth estimation, image-to-image (denoising, super-resolution, modality translation), image-to-text (report generation, VQA), text-to-image (synthesis/augmentation). Each task defined with a medical example and its evaluation metrics (AUROC, Dice, Hausdorff, mAP, etc.).

**Ch. 6 — Deep Learning Architectures**
CNNs from first principles, U-Net and the encoder-decoder family, nnU-Net, vision transformers, detection architectures, 3D and video architectures, promptable segmentation (SAM family). How architecture choice follows from task + modality dimensionality.

**Ch. 7 — Generative & Frontier Models**
Diffusion models, GANs (historical + niche uses), vision-language models, LLMs in imaging (report generation, RAG assistants), RLHF and reasoning models, medical foundation models (MedSAM, BiomedParse, CheXagent, MedGemma, TotalSegmentator as a "model-as-infrastructure" case), agentic workflows. *MedAI OS hook: nearly every model discussed here ships in MedAI OS.*

**Ch. 8 — From Model to Product: Evaluation, Regulation, Deployment**
Clinical validation vs. benchmark performance, reader studies, dataset shift and bias, FDA pathways (510(k), De Novo, PMA) and CE-MDR in plain language, what a clearance summary actually claims, post-market surveillance, audit trails, MLOps for hospitals. *MedAI OS hook: the audit hash-chain logging and batch-inference features as teaching examples.*

### Part III — Diagnostic Imaging, Modality by Modality
*(each follows the §3 template)*

**Ch. 9 — Chest X-ray** *(flagship chapter — written first, sets the template)*
Datasets: ChestX-ray14, CheXpert, MIMIC-CXR, PadChest, VinDr-CXR… Models: CheXagent, MedGemma, TorchXRayVision… Products: the largest FDA-cleared category (triage, TB, pneumothorax). *MedAI OS: the Chest X-Ray Suite — CheXagent abnormality detection, phrase grounding, tube/fracture/foreign-object detection, structured report generation, triage.*

**Ch. 10 — Computed Tomography (CT)**
Hounsfield units, windowing, contrast phases; stroke/PE/nodule/trauma AI; TotalSegmentator's 117 structures; lung-cancer screening. *MedAI OS: TotalSegmentator + BiomedParse auto-segmentation, MPR/3D rendering, volumetrics & radiomics, Oncology Suite lesion tracking.*

**Ch. 11 — Magnetic Resonance Imaging (MRI)**
Sequences as "channels," neuro/MSK/cardiac/breast/prostate applications, reconstruction AI (fastMRI). *MedAI OS: Neurology Suite (MS/dementia/stroke workflows, ICV normalization), breast DCE-MRI nnU-Net, registration + propagation.*

**Ch. 12 — Ultrasound & Echocardiography**
Real-time 2D+t imaging, operator dependence, POCUS democratization, EF estimation, obstetric biometry, FDA-cleared guidance products (e.g., Caption-style).

**Ch. 13 — Mammography & Breast Imaging**
Screening at population scale, DBT/3D, the densest FDA-cleared market, landmark reader studies, risk prediction (Mirai-style).

**Ch. 14 — Nuclear Medicine: PET & SPECT**
SUV quantification, hybrid PET/CT–PET/MR, lesion detection, theranostics, dose-reduction AI. *MedAI OS: SUV analytics, Oncology Suite trial endpoints.*

**Ch. 15 — Ophthalmic Imaging: Fundus & OCT**
Diabetic retinopathy screening (the first autonomous FDA clearance — IDx-DR), OCT layer segmentation, glaucoma/AMD, oculomics.

### Part IV — Interventional, Lab-Based & Video

**Ch. 16 — Surgical & Endoscopic Video**
Video as 2D+t at scale; phase recognition, tool detection, skill assessment; GI endoscopy polyp detection (cleared products); datasets (Cholec80, EndoVis…). *MedAI OS: Surgical Suite — 3D models, FLR, mesh export for planning.*

**Ch. 17 — Digital Pathology & Histology**
Whole-slide images (gigapixel tiling), stains, IHC; MIL and slide-level foundation models (UNI, Virchow, Prov-GigaPath); FDA-cleared primary-diagnosis viewers + AI (Paige-style); the pathology data problem.

**Ch. 18 — The Remaining Map**
Dermatology imaging, dental/CBCT, DEXA & opportunistic screening, ECG-as-image, emerging modalities — condensed template treatment so coverage is complete.

### Part V — Systems & The Road Ahead

**Ch. 19 — Building an Imaging AI Platform (MedAI OS as case study)**
This is the "user manual" chapter: viewer architecture (Cornerstone3D/VTK.js), feature flags & suites, PACS integration, model serving (MONAI Label, session-based interactive segmentation), GPU memory budgeting, adding your own model. The one chapter that is explicitly MedAI-OS-centric.

**Ch. 20 — Ethics, Bias, Safety & The Future**
Fairness across populations, automation bias, liability, sustainability of AI products, foundation-model consolidation, agentic radiology, what to watch next.

### Appendices
- **A.** The Dataset Directory (master living table, all modalities)
- **B.** The Model Zoo (master living table)
- **C.** FDA-Cleared AI Product Index (living table)
- **D.** DICOM quick reference for ML engineers
- **E.** MedAI OS setup guide (condensed from repo README)
- **F.** Dual glossary: clinical terms for engineers / ML terms for clinicians

---

## 5. Chapter ↔ MedAI OS Feature Map

| Chapter | MedAI OS features referenced |
|---|---|
| 3 (Hospital data) | Orthanc PACS, DICOM/NIfTI/NRRD loaders, upload flow |
| 6 (Architectures) | SAM2/MedSAM2/nnInteractive interactive segmentation |
| 7 (Frontier models) | BiomedParse text-prompted seg, CheXagent, RAG chat, agentic workflows |
| 8 (Regulation) | Audit hash-chain logging, batch inference, "not a medical device" framing |
| 9 (Chest X-ray) | Chest X-Ray Suite: detection, grounding, reports, triage |
| 10 (CT) | TotalSegmentator, MPR/3D, volumetrics, radiomics, Oncology Suite |
| 11 (MRI) | Neurology Suite, breast DCE-MRI nnU-Net, registration |
| 14 (Nuclear) | SUV analytics, Oncology Suite |
| 16 (Surgical video) | Surgical Suite: 3D models, FLR, mesh export |
| 19 (Platform) | Entire architecture, suites system, adding models |

(RT Suite and Cardiology Suite get sidebars in Ch. 10/11 and Ch. 12 respectively.)

---

## 6. Build Plan — Phases & Milestones

**Phase 0 — Infrastructure (week 1)**
Create repo, scaffold Quarto book, set up GitHub Action → Pages deploy, wire `book.anandpreshob.com` CNAME, add link/card on www.anandpreshob.com, create the three CSV living-table schemas, add cross-links in the medai-os README. *Deliverable: an empty-but-live book at your domain.*

**Phase 1 — Foundations text (weeks 2–5)**
Write Ch. 1–3 (Part I) and Ch. 4–5. These are pure-prose, research-light chapters that establish voice and the dual-audience style. *Deliverable: Parts I live, book announceable.*

**Phase 2 — Flagship chapter (weeks 6–8)**
Write Ch. 9 (Chest X-ray) end-to-end, including its three living tables and the full MedAI OS walkthrough with screenshots. This chapter is the quality bar and reusable template for all modality chapters. *Deliverable: the template chapter + populated dataset/model/FDA CSVs for CXR.*

**Phase 3 — Complete foundations (weeks 9–12)**
Ch. 6–8 (architectures, frontier models, regulation). These benefit from having the CXR chapter done — examples can point forward/backward.

**Phase 4 — Modality sweep (weeks 13–24, ~1.5 weeks per chapter)**
Ch. 10–18 in this order: CT → MRI → pathology → ultrasound → mammography → ophtho → nuclear → surgical video → remaining map. (Ordered by MedAI OS overlap + product-market size.)

**Phase 5 — Systems chapters + appendices (weeks 25–28)**
Ch. 19 (the MedAI OS deep-dive), Ch. 20, appendices, dual glossary, full-book editing pass.

**Ongoing** — quarterly refresh of the three living CSVs (new datasets, models, clearances); community PRs welcomed via CONTRIBUTING.md.

**Suggested working rhythm:** each chapter = research pass (populate CSVs + collect references) → draft → MedAI OS walkthrough with real screenshots → dual-audience review pass ("would a clinician follow §4? would an engineer follow §2?").

**Target sizes:** modality chapters 4,000–6,000 words + 3 tables + 4–8 figures; foundation chapters 5,000–8,000 words.

---

## 7. Status (updated 2026-08-19)

**Done — Phase 0 scaffold:**
- Quarto book scaffolded and test-rendered at `/Users/anandkadumberi/Projects/ai-medical-imaging-book` (git-initialized, `main`): full TOC as chapter stubs, living-table CSVs seeded (`data/datasets.csv`, `models.csv`, `fda-products.csv`), site-matching theme (Inter/Space Grotesk), publish workflow (GitHub Pages + website sync).
- Personal website: "Textbook" nav link on all four pages + homepage highlight card pointing to `/book/` (files written locally, **not yet git-committed/pushed** — deploy the book first so /book/ isn't a 404).
- medai-os README: "Learn the concepts" cross-link section added (local working tree, not committed).

**Anand's one-time steps (see SETUP.md in the book repo):** clean stale `.git` lock/tmp files, create GitHub repo + push, enable Pages from `gh-pages`, add `WEBSITE_SYNC_TOKEN` fine-grained PAT (contents:write on `personal-website`), then commit/push the website nav changes.

**Next writing step:** Ch. 2 (modality atlas) or Ch. 9 (chest X-ray flagship).
