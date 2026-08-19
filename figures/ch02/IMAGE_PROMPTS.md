# Chapter 2 Figure Spec — Image Generation Prompts

Figures for `chapters/02-universe-of-medical-images.qmd`. Each modality gets a **pair**:

- **(A) Acquisition illustration** — cartoonified scene of how the image is made (patient + equipment + energy path). AI-generate these.
- **(B) Representative image** — what the resulting scan looks like.

> **Editorial note for (B):** Prefer a real, openly licensed image when one is readily available — first choice: a screenshot from MedAI OS displaying a public sample study; second: Wikimedia Commons (check that the license allows reuse). Generated educational renderings are also acceptable under the book-wide visual-content note in the preface.

## Global style block — prepend to every (A) prompt

> Flat modern vector illustration in a clean medical-textbook style. Simple rounded geometric shapes, minimal detail, soft shading. Palette: indigo (#6366f1) and slate gray on a white background, one warm coral accent for the energy source/beam. Friendly gender-neutral patient figure, no facial detail. Absolutely no text, labels, arrows with words, logos, or brand names in the image. Anatomically plausible but stylized. Aspect ratio 3:2, high resolution.

## Global style block — prepend to every generated (B) prompt (fallback only)

> Photorealistic medical image rendering as displayed on a diagnostic monitor, correct characteristic appearance for the modality, neutral dark viewer background, no patient information, no text overlays, no annotations, no watermarks. Aspect ratio 1:1.

File naming: `figures/ch02/<slug>-acquisition.png` and `figures/ch02/<slug>-example.png`.

---

## 1. X-ray (radiography) — slug `xray`

**(A) Prompt:** A person standing upright in profile facing a wall-mounted flat detector panel, arms slightly raised to the sides of the panel. Behind them, an X-ray tube head on an articulated ceiling mount emits a subtle cone-shaped coral beam that passes through the person's chest and lands on the detector. Faint silhouette of ribs and lungs visible inside the chest where the beam passes, hinting at the shadow being cast. A lead-glass control booth with a technologist visible in the corner background.

**(B) Fallback prompt:** A frontal (PA) chest X-ray radiograph, grayscale: dark air-filled lungs, white heart shadow slightly left of center, visible rib cage, clavicles, and diaphragm domes, sharp and correctly exposed.
**(B) Real-image source:** MedAI OS screenshot of a sample chest X-ray, or NIH ChestX-ray14 sample (CC0-adjacent, verify), or Wikimedia Commons "Chest radiograph".

**Caption:** How a radiograph is made: the X-ray tube projects a beam through the patient onto a detector — every structure along each ray is superimposed into one 2D shadow. | **Alt:** Illustration of a patient standing between an X-ray tube and a flat detector panel.

## 2. Mammography / DBT — slug `mammo`

**(A) Prompt:** A standing woman at a mammography unit shown from the side: a tall column-shaped machine with two clear compression paddles gently flattening breast tissue between them, a compact X-ray tube head above angled slightly, sweeping arc of faint coral dashed positions suggesting the tomosynthesis sweep. A technologist stands beside her at a small control panel. Calm, dignified, non-graphic depiction.

**(B) Fallback prompt:** A mediolateral-oblique screening mammogram, grayscale: fibroglandular tissue as wispy white strands over darker fat, pectoral muscle edge in the corner, a few tiny bright microcalcification dots.
**(B) Real-image source:** Wikimedia Commons "Mammogram"; or a VinDr-Mammo sample if license permits.

**Caption:** Mammography compresses the breast between paddles and images it with low-energy X-rays; tomosynthesis sweeps the tube through an arc to build a pseudo-3D stack. | **Alt:** Illustration of a patient at a mammography unit with compression paddles and a sweeping X-ray tube.

## 3. Fluoroscopy / angiography — slug `fluoro`

**(A) Prompt:** An interventional suite: a patient lying on a narrow table with a large C-shaped arm (C-arm) wrapping over and under the torso, X-ray tube below the table and detector above, a faint continuous coral beam passing through the patient. Two monitors on a boom show a stylized live vessel tree in white on black. A physician in a lead apron stands at the table guiding a thin catheter line.

**(B) Fallback prompt:** A digital subtraction angiography frame, grayscale inverted look: dark contrast-filled arteries branching like a tree against a nearly uniform light background, catheter faintly visible.
**(B) Real-image source:** Wikimedia Commons "Digital subtraction angiography".

**Caption:** Fluoroscopy is X-ray as live video: a C-arm streams frames while the operator works, contrast dye tracing vessels in real time. | **Alt:** Illustration of a C-arm fluoroscopy suite with a physician guiding a catheter.

## 4. DEXA — slug `dexa`

**(A) Prompt:** A person lying flat on an open padded table while a slim horizontal scanner arm hovers above the hips, projecting two parallel thin coral beams (one slightly lighter) down through the pelvis to a detector strip under the table. Clean open geometry — no tunnel. A small screen beside the table shows a stylized skeleton pelvis with a shaded density region.

**(B) Fallback prompt:** A DEXA bone-density report image of the hip: low-resolution grayscale skeleton outline of a proximal femur with a color-shaded region-of-interest overlay box.
**(B) Real-image source:** Wikimedia Commons "DXA scan".

**Caption:** DEXA measures attenuation at two X-ray energies to compute bone mineral density — imaging as measurement more than picture. | **Alt:** Illustration of a patient on an open DEXA table with a scanning arm above the pelvis.

## 5. CT — slug `ct`

**(A) Prompt:** A patient lying on a motorized table sliding into the short open bore of a large donut-shaped CT gantry, shown in three-quarter cutaway view: inside the gantry ring, an X-ray tube and an opposing curved detector arc are visible mid-rotation, with a coral fan-beam sweeping across the patient's chest and circular motion lines indicating spin. A stack of thin translucent axial slices floats above the patient's torso hinting at the reconstructed volume.

**(B) Fallback prompt:** An axial chest CT slice in lung window, grayscale: black lungs with fine bronchovascular branching, gray mediastinum, white vertebra and ribs, patient oriented supine.
**(B) Real-image source:** MedAI OS screenshot of a sample CT (best — shows MPR); Wikimedia Commons "CT scan of the chest".

**Caption:** CT spins an X-ray tube and detector around the patient and reconstructs calibrated 3D slices from hundreds of projections. | **Alt:** Cutaway illustration of a CT gantry showing the rotating tube, detector arc, and fan beam.

## 6. MRI — slug `mri`

**(A) Prompt:** A patient on a table entering the long cylindrical bore of an MRI scanner, cutaway view revealing nested rings inside the housing (magnet coils), gentle concentric indigo field lines wrapping the bore, and a soft coral radio-wave symbol pulsing from a head coil around the patient's head. Beside the scanner, four small floating panels show the same stylized brain in different contrast tints, suggesting sequences. No metal objects anywhere in the room.

**(B) Fallback prompt:** An axial T1-weighted brain MRI slice, grayscale: bright white-matter tracts, darker cortical gray matter ribbon, black CSF in ventricles, smooth skull outline with bright subcutaneous fat.
**(B) Real-image source:** MedAI OS screenshot of a sample multi-sequence brain MRI (shows the sequence list — pedagogically ideal); Wikimedia Commons "MRI of the brain".

**Caption:** MRI tips hydrogen nuclei in a strong magnetic field and listens to them relax; reordering the pulses — the sequence — renders the same anatomy in entirely different contrasts. | **Alt:** Cutaway illustration of an MRI bore with field lines, a head coil, and floating panels of differently-contrasted brain images.

## 7. PET / PET-CT — slug `pet`

**(A) Prompt:** A two-stage scene: on the left, a seated patient receives a small injection, with a stylized glowing tracer molecule icon; on the right, the same patient lies in a long dual-ring scanner (two donut gantries in one housing). Inside the patient's silhouette, a few soft coral glowing spots emit tiny photon rays outward in opposite directions toward the detector ring. A faint gray anatomical outline overlays one glowing spot, suggesting PET fused on CT.

**(B) Fallback prompt:** A whole-body FDG-PET maximum-intensity projection: grayscale-inverted body silhouette with dark brain and bladder (normal uptake) and a fused axial PET/CT slice beside it with a hot color-mapped lesion.
**(B) Real-image source:** Wikimedia Commons "FDG PET scan"; MedAI OS SUV analytics screenshot when available.

**Caption:** PET images emission, not transmission: an injected tracer accumulates where its target biology is active, and the ring detects the photons the patient emits. | **Alt:** Illustration of tracer injection and a PET/CT scanner detecting glowing regions inside the patient.

## 8. Ultrasound / echocardiography — slug `us`

**(A) Prompt:** A sonographer holding a handheld probe against a reclining patient's chest, with a translucent coral wedge-shaped beam fanning from the probe tip into the body and faint echo arcs returning to the probe. The cart-mounted machine beside them shows a stylized fan-shaped (sector) image of a four-chambered heart on screen. Gel bottle on the cart.

**(B) Fallback prompt:** An echocardiogram still frame, apical four-chamber view: fan-shaped sector image, speckled grayscale myocardium outlining four cardiac chambers as dark blood pools, ECG trace strip along the bottom edge, depth markers along the side — no text.
**(B) Real-image source:** Wikimedia Commons "Echocardiogram apical four chamber"; EchoNet-Dynamic sample if license permits.

**Caption:** Ultrasound times echoes from a handheld probe — the image exists only where the operator points it, at video rate. | **Alt:** Illustration of a sonographer scanning a patient's chest with the heart displayed on the machine.

## 9. Endoscopy — slug `endo`

**(A) Prompt:** A simplified cutaway of a patient lying on their side with a thin flexible scope entering the colon, drawn as a smooth winding tube; the scope tip carries a tiny light and camera icon casting a soft cone of light ahead. A monitor beside the bed shows a stylized circular endoscopic view of pink mucosa with one small polyp bump highlighted by a subtle ring.

**(B) Fallback prompt:** A colonoscopy video frame: circular field of view, well-lit pink-red glistening mucosa with fine vessels, a small sessile polyp near the fold, lens reflections — no overlay text.
**(B) Real-image source:** Kvasir dataset samples (CC BY); Wikimedia Commons "Colonoscopy polyp".

**Caption:** Endoscopy is ordinary light from inside the body — a camera at the scope tip streaming HD video as the operator navigates. | **Alt:** Illustration of a flexible endoscope inside the colon with the video view on a monitor.

## 10. Surgical video — slug `surgvideo`

**(A) Prompt:** A minimal operating room: a patient draped on a table with three slim laparoscopic ports in the abdomen, one carrying a camera whose view-cone glows softly inside a cutaway of the abdominal cavity showing two stylized instruments near a gallbladder. A large monitor above the table displays the internal scene; a small recording-dot motif suggests the video stream. A surgeon silhouette watches the screen, not the patient.

**(B) Fallback prompt:** A laparoscopic cholecystectomy video frame: close-up internal view, glistening liver edge and gallbladder, two instrument tips (a grasper and a hook) entering from the frame edges, bright central illumination — no text overlays.
**(B) Real-image source:** Cholec80 dataset frame (research license — verify) or Wikimedia Commons "Laparoscopic surgery view".

**Caption:** In surgical video the image documents an activity, not just anatomy — hours of footage where the labels are events in time. | **Alt:** Illustration of laparoscopic surgery with the internal camera view shown on the OR monitor.

## 11. Fundus photography — slug `fundus`

**(A) Prompt:** A patient seated at a tabletop fundus camera, chin on the chin-rest and forehead against the bar, with the camera's lens barrel aligned to one eye; a gentle coral light path travels from the camera through the pupil to the back of a cutaway eye globe, illuminating the retina drawn as a warm orange inner surface with tiny vessels. The attached screen shows a stylized circular orange retina image.

**(B) Fallback prompt:** A color fundus photograph: circular orange-red retina, bright yellowish optic disc slightly off-center with vessels branching from it, darker macula spot, crisp focus.
**(B) Real-image source:** EyePACS/Kaggle DR sample (check terms) or Wikimedia Commons "Fundus photograph normal".

**Caption:** The fundus camera photographs the retina through the pupil — the only place the body's microvasculature can be imaged directly with visible light. | **Alt:** Illustration of a patient at a fundus camera with the light path into a cutaway eye.

## 12. OCT — slug `oct`

**(A) Prompt:** The same chin-rest tabletop device silhouette as fundus photography, but the beam is a thin indigo scanning line sweeping across the cutaway eye's retina, leaving behind a floating stack of thin cross-section slices beside the eye; one slice is enlarged showing distinct horizontal layers like sediment strata.

**(B) Fallback prompt:** A macular OCT B-scan: horizontal banded cross-section of the retina in grayscale-gold, distinct layered strata with a central foveal dip, dark vitreous above and choroid texture below — no measurement overlays.
**(B) Real-image source:** Kermany OCT dataset (CC BY) or Wikimedia Commons "OCT macula normal".

**Caption:** OCT is light's version of ultrasound — interferometry resolving the retina's layers in micron-scale cross-sections. | **Alt:** Illustration of an OCT scanner sweeping a beam across the retina producing layered cross-section slices.

## 13. Histopathology / WSI — slug `path`

**(A) Prompt:** A three-step left-to-right story: a small tissue block being sliced into an ultra-thin translucent sheet by a microtome, the sheet floating onto a glass slide picking up a pink-purple stain tint, then the slide entering a compact slide-scanner box that projects a huge zoomable mosaic grid on a monitor — a checkerboard of tiny pink-purple tiles with one tile enlarged.

**(B) Fallback prompt:** A hematoxylin-and-eosin histology field at medium magnification: pink cytoplasm and stroma, purple-blue nuclei, glandular tissue architecture, even illumination, sharp focus.
**(B) Real-image source:** CAMELYON16 patch (open) or Wikimedia Commons "H&E stain histology".

**Caption:** Pathology images extracted tissue: micron-thin stained sections digitized into gigapixel whole-slide images — far too large for any model to swallow whole. | **Alt:** Illustration of tissue sectioning, staining, and slide scanning into a tiled gigapixel image.

## 14. Dermoscopy — slug `derm`

**(A) Prompt:** A clinician holding a small handheld dermatoscope (like a short thick magnifier with an internal light ring) flat against the skin of a patient's forearm, a soft polarized-light glow at the contact point; a connected phone screen shows the magnified stylized view of a brown mole with subtle internal pattern.

**(B) Fallback prompt:** A dermoscopic image of a benign melanocytic nevus: circular illuminated field, brown pigment network with regular pattern, fine skin lines, slight oil-interface sheen — no rulers or markers.
**(B) Real-image source:** ISIC Archive (CC-0/CC-BY images available — filter by license).

**Caption:** Dermoscopy puts polarized magnification against the skin, revealing pigment structures invisible to the naked eye. | **Alt:** Illustration of a clinician examining a mole with a handheld dermatoscope linked to a phone.

## 15. Dental / CBCT — slug `dental`

**(A) Prompt:** A standing patient biting gently on a small positioning tab at the center of a panoramic dental machine whose C-shaped arm orbits the head, tracing a dashed indigo arc; beside it, a compact cone-beam unit with a coral cone of X-rays converging through the jaw onto a small square detector. A screen shows a stylized wide horseshoe-shaped panoramic teeth image.

**(B) Fallback prompt:** A dental panoramic radiograph (OPG): wide horseshoe layout of upper and lower teeth with roots, jaw bones and sinuses in grayscale, correct tooth count, no text.
**(B) Real-image source:** Wikimedia Commons "Orthopantomogram".

**Caption:** Dental imaging spans quick panoramic sweeps to cone-beam CT volumes for implant planning. | **Alt:** Illustration of a panoramic dental X-ray machine orbiting a standing patient's head.

---

## Insertion spec (for the coding agent)

Add each pair immediately **after the first paragraph of its modality's section** in `chapters/02-universe-of-medical-images.qmd`, as a side-by-side pair:

```markdown
::: {layout-ncol=2}
![<caption A>](../figures/ch02/<slug>-acquisition.png){#fig-<slug>-acq fig-alt="<alt A>"}

![<caption B>](../figures/ch02/<slug>-example.png){#fig-<slug>-ex fig-alt="Representative <modality> image."}
:::
```

Section mapping: xray → "Radiography (X-ray)", mammo → "Mammography and digital breast tomosynthesis", fluoro → "Fluoroscopy and angiography", dexa → "DEXA", ct → "Computed tomography (CT)", mri → "Magnetic resonance imaging (MRI)", pet → "Nuclear medicine: PET and SPECT", us → "Ultrasound and echocardiography", endo → "Endoscopy", surgvideo → "Surgical and interventional video", fundus → "Fundus photography", oct → "Optical coherence tomography (OCT)", path → "Histopathology and whole-slide imaging", derm/dental → the "Dermatology, dental and maxillofacial" section (stack all four images in one 2×2 layout).

Compress PNGs before committing (target < 400 KB each, e.g. `pngquant` or export at 1600px wide).
