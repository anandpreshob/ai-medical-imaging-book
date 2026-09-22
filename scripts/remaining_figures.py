"""Rebuild original educational SVGs for chapters 12–22 (stdlib only).

These are conceptual diagrams, never diagnostic scans. Numeric examples are
explicitly illustrative. Output is deterministic and uses no external assets.
"""
from pathlib import Path
from html import escape
import math
import textwrap

ROOT=Path(__file__).resolve().parents[1]
NAVY='#17324d';TEAL='#087f8c';CORAL='#c65a46';BG='#f7fafb';PALE='#e4f2f2';GRAY='#526777';GOLD='#b17a14'
class SVG:
 def __init__(self,title,subtitle):
  self.parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="560" viewBox="0 0 1000 560" role="img"><title>{escape(title)}</title><desc>{escape(subtitle)}</desc><defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="{TEAL}"/></marker></defs><rect width="1000" height="560" fill="{BG}"/>']
  self.text(38,48,title,28,NAVY,True);self.text(38,80,subtitle,16,GRAY)
  self.line(38,100,962,100,TEAL,2)
 def text(self,x,y,s,size=18,color=NAVY,bold=False,anchor='start'):
  self.parts.append(f'<text x="{x}" y="{y}" font-family="Arial, Helvetica, sans-serif" font-size="{size}" fill="{color}" font-weight="{700 if bold else 400}" text-anchor="{anchor}">{escape(s)}</text>')
 def wrap(self,x,y,s,width=30,size=17,color=GRAY):
  for i,line in enumerate(textwrap.wrap(s,width=width)):self.text(x,y+i*25,line,size,color)
 def rect(self,x,y,w,h,fill=PALE,stroke='none',r=10):
  self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}"/>')
 def line(self,x1,y1,x2,y2,color=TEAL,width=3,arrow=False,dash=False):
  self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"'+(' marker-end="url(#arrow)"' if arrow else '')+(' stroke-dasharray="7 5"' if dash else '')+'/>')
 def circle(self,x,y,r,fill=TEAL):self.parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>')
 def path(self,d,color=TEAL,width=3,fill='none'):self.parts.append(f'<path d="{d}" stroke="{color}" stroke-width="{width}" fill="{fill}"/>')
 def box(self,x,y,w,h,title,body='',color=TEAL):
  self.rect(x,y,w,h,'white','#d4e1e6');self.rect(x,y,5,h,color,r=0)
  self.text(x+20,y+32,title,19,color,True)
  self.wrap(x+20,y+62,body,max(16,int((w-35)/8.5)))
 def save(self,ch,name,note='Original schematic • AI in Medical Imaging • Not a patient image'):
  self.line(38,510,962,510,'#d4e1e6',1);self.text(38,539,note,14,GRAY)
  p=ROOT/'figures'/f'ch{ch}'/f'{name}.svg';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(''.join(self.parts)+'</svg>')

def flow(ch,name,title,subtitle,items,note):
 s=SVG(title,subtitle); n=len(items)
 if n<=3:
  w=280;xs=[40+i*320 for i in range(n)];y=185
  for i,(head,body) in enumerate(items):
   s.box(xs[i],y,w,180,head,body)
   if i<n-1:s.line(xs[i]+w+6,y+90,xs[i+1]-8,y+90,arrow=True)
 else:
  # Two-column sequence, reading left to right, then down and back left.
  pos=[(60,135),(540,135),(540,325),(60,325)]
  for i,(head,body) in enumerate(items):s.box(*pos[i],400,140,f'{i+1}. {head}',body)
  s.line(465,205,525,205,arrow=True);s.line(740,280,740,313,arrow=True);s.line(530,395,475,395,arrow=True)
 s.text(500,490,note,17,CORAL,True,'middle');s.save(ch,name)

def comparison(ch,name,title,subtitle,items,note):
 s=SVG(title,subtitle);n=len(items);w=(920-20*(n-1))/n
 for i,(head,body) in enumerate(items):s.box(40+i*(w+20),155,w,280,head,body,TEAL if i%2==0 else CORAL)
 s.text(500,478,note,17,NAVY,True,'middle');s.save(ch,name)

# CT: exact display curves, physical grids, task routing, lesion identities.
s=SVG('CT windowing changes the display','Illustrative clipped linear mappings; these are not diagnostic presets.')
s.line(90,425,920,425,NAVY,2);s.line(90,425,90,145,NAVY,2)
for hu in [-1000,-500,0,500,1000]:
 x=90+(hu+1000)/2000*830;s.line(x,425,x,433,NAVY,1);s.text(x,457,str(hu),16,GRAY,anchor='middle')
s.text(500,488,'Input intensity (HU)',17,NAVY,anchor='middle');s.text(95,132,'Display brightness',17)
for center,width,color,label,yy in [(-500,1200,TEAL,'Wide / low center',170),(50,400,CORAL,'Narrow / near zero',200),(400,1200,GOLD,'Wide / high center',230)]:
 pts=[]
 for hu in range(-1000,1001,5):pts.append((90+(hu+1000)/2000*830,425-min(1,max(0,(hu-(center-width/2))/width))*270))
 s.path('M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in pts),color,4)
 s.line(640,yy-5,675,yy-5,color,4);s.text(686,yy,label,16,color)
s.save(12,'windows')
s=SVG('Geometry survives resampling','Array shape changes; physical position and orientation must remain traceable.')
for x,dx,dy,title in [(60,45,65,'Source: anisotropic'),(550,35,35,'Model: isotropic')]:
 s.text(x,145,title,22,TEAL,True)
 for i in range(int(315/dx)+1):s.line(x+i*dx,180,x+i*dx,390,'#88b5bd',1)
 for j in range(int(210/dy)+1):s.line(x,180+j*dy,x+315,180+j*dy,'#88b5bd',1)
 s.circle(x+135,310,9,CORAL)
s.line(405,250,525,250,arrow=True);s.text(465,231,'Resample',16,TEAL,anchor='middle')
s.line(530,352,407,352,arrow=True);s.text(468,382,'Map back',16,TEAL,anchor='middle')
s.text(500,466,'Keep origin, spacing, orientation, transforms, and source identifiers.',19,NAVY,True,'middle');s.save(12,'geometry')
comparison(12,'routing','One modality, different input contracts','Choose the series from acquisition evidence, not merely from the CT label.',[
('Head triage','Noncontrast head CT. Verify coverage and supported reconstruction before routing.'),('Vascular task','Supported angiographic acquisition. Verify anatomy, contrast timing, and coverage.'),('Abdominal task','Supported abdominal protocol. Preserve phase and reconstruction identity.')],'Missing or ambiguous prerequisites → explicit no-result state')
s=SVG('Longitudinal lesion identity','Matching is an evidence-based decision, not a forced nearest-neighbor assignment.')
s.text(170,145,'Baseline',23,TEAL,True);s.text(665,145,'Follow-up',23,TEAL,True)
for x in [200,730]:s.rect(x-100,170,200,270,'white','#d4e1e6')
for x,y,r,c in [(200,215,18,TEAL),(200,320,25,CORAL),(730,220,22,TEAL),(730,330,16,GOLD),(730,400,12,NAVY)]:s.circle(x,y,r,c)
s.line(240,215,685,220,arrow=True);s.text(458,202,'Supported match',18,TEAL,anchor='middle')
s.line(245,320,677,330,CORAL,2,dash=True);s.text(458,306,'Unresolved identity',18,CORAL,anchor='middle')
s.text(600,408,'New focus',18,NAVY,anchor='end');s.text(500,480,'Also represent resolved lesions; do not invent a numeric change for a new target.',17,NAVY,True,'middle');s.save(12,'longitudinal')

comparison(13,'sequences','MRI contrasts answer different questions','Sequence identity is part of the input, not an optional filename hint.',[
('T1','Anatomical contrast; pre- and post-contrast acquisitions have different roles.'),('T2 / FLAIR','Fluid-sensitive contrasts; FLAIR suppresses much of the CSF signal.'),('DWI / ADC','Diffusion-weighted signal interpreted with a derived ADC map.'),('Susceptibility','Sensitivity to local magnetic-field variation; task-specific interpretation.')],'A missing required sequence is an explicit state')
flow(13,'reconstruction','Measurement → reconstruction → interpretation','These stages need distinct reference standards.',[('Measured k-space','Sampling pattern, coils, complex signal, and acquisition metadata.'),('Image estimate','Reconstruction plus data-consistency checks and image-quality assessment.'),('Clinical task','Evaluate lesion visibility or measurement fidelity for the intended use.')],'Pixel similarity alone does not establish diagnostic fidelity')
flow(13,'alignment','Assemble a multi-sequence MRI input','Preserve the reference image and every spatial transformation.',[('Inventory','Identify T1, T2, FLAIR, diffusion, and any task-specific requirements.'),('Align','Register supported inputs and resample to a documented reference.'),('Infer','Apply the pinned preprocessing and model to the eligible inputs.'),('Return','Map outputs to source coordinates and inspect overlays.')],'Never interpolate categorical label IDs as continuous intensities')
flow(13,'longitudinal','Is this MRI change comparable?','A percentage requires a matched target and compatible measurements.',[('Two visits','Verify required sequences, timing, and image quality at both visits.'),('Match anatomy','Inspect registration, surgery-related changes, and lesion identity.'),('Review change','Keep new, unresolved, and noncomparable targets distinct.')],'Example: 2.0 → 2.3 mL is +15%; it is not a progression criterion')
flow(14,'acquisition','Ultrasound begins with acquisition','Operator decisions shape the input distribution.',[('Probe and window','Position, frequency, depth, focus, patient anatomy, and motion.'),('Signal processing','Beamforming and supported B-mode, M-mode, or Doppler processing.'),('Image or clip','Check task-specific adequacy and preserve timing and calibration.')],'A model cannot assess anatomy that was never adequately imaged')
s=SVG('Ejection fraction: inputs before arithmetic','Illustrative volumes; the figure does not validate contours or clinical interpretation.')
for x,vol,label,col in [(160,120,'End diastole',TEAL),(470,50,'End systole',CORAL)]:
 s.rect(x,175,150,240,'#e4eaed');s.rect(x,415-vol*2,150,vol*2,col)
 s.text(x+75,150,label,21,col,True,'middle');s.text(x+75,450,f'{vol} mL',24,col,True,'middle')
s.box(700,215,255,150,'EF ≈ 58%','(120 − 50) / 120 × 100')
s.text(500,487,'Verify the view, cardiac phase, contours, and volume method first.',18,NAVY,True,'middle');s.save(14,'ef')
comparison(14,'quality','Three acquisition outcomes','Quality is defined for the intended measurement or interpretation.',[('Missing view','Required anatomy was not obtained. Complete acquisition or follow the escalation path.'),('Inadequate view','View exists but fails the task requirements. Reacquire or report no valid result.'),('Adequate view','Supported anatomy and quality. Proceed to the defined measurement task.')],'Missing and inadequate are not negative diagnoses')
flow(14,'live-loop','Keep ultrasound feedback current','Separate the fast guidance loop from record completion.',[('Acquire','Timestamp live frames and maintain patient/session identity.'),('Bounded inference','Process supported current inputs; prevent stale queues.'),('Guide operator','Show timely, interpretable view and quality feedback.'),('Accept and save','Store reviewed clips and measurements in the clinical record.')],'A slow administrative task should not block live guidance')
s=SVG('The four-view mammography examination','Laterality and view identity remain attached to every image.')
for i,(label,sub) in enumerate([('R CC','Right • craniocaudal'),('L CC','Left • craniocaudal'),('R MLO','Right • mediolateral oblique'),('L MLO','Left • mediolateral oblique')]):
 x=55+(i%2)*480;y=130+(i//2)*180;s.box(x,y,410,150,label,sub)
 s.rect(x+300,y+25,85,95,PALE);s.path(f'M{x+312},{y+35} Q{x+390},{y+70} {x+312},{y+108}',TEAL,3)
s.text(500,487,'Extra views, repeats, implants, and unilateral examinations need explicit handling.',17,NAVY,True,'middle');s.save(15,'views')
flow(15,'dbt','Tomosynthesis: a correlated image stack','Limited-angle acquisition is not a set of independent examinations.',[('Projection set','Several X-ray views acquired across a limited angular range.'),('Depth planes','Reconstruction yields correlated planes with task-specific resolution.'),('Derived overview','A synthesized 2D image may accompany the stack; preserve its identity.')],'Do not split planes from one examination across train and test sets')
comparison(15,'tasks','Current detection and future risk are different tasks','Similar-looking scores can describe different events and time horizons.',[('Current examination','Detect or assess a lesion already represented in the images. Reference: the defined current finding or cancer outcome.'),('Future risk','Estimate a specified event over a stated follow-up horizon. Reference: time-aware outcomes and censoring.')],'A detection score is not automatically a calibrated future-risk estimate')
flow(15,'workflow','Evaluate the screening pathway','The reading strategy and follow-up process are part of the intervention.',[('Acquire','Review positioning, quality, laterality, views, and supported image type.'),('Assist reading','Display eligible model output with source images and prior studies.'),('Clinical assessment','Reader determines the appropriate diagnostic or routine pathway.'),('Ascertain outcomes','Track recalls, cancers, technical failures, and follow-up completeness.')],'Model discrimination alone does not establish pathway benefit')
flow(16,'acquisition','PET retains a measurement chain','Tracer and timing are essential context for the reconstructed image.',[('Administration','Link radiopharmaceutical identity, activity, and relevant times.'),('Acquire events','Record coincidence measurements under the intended protocol.'),('Correct and reconstruct','Apply supported corrections and preserve reconstruction identity.'),('Quantitative image','Document units, coverage, calibration, and anatomical pairing.')],'A different tracer is a different biological input domain')
comparison(16,'suv','SUV requires a consistent quantitative convention','The diagram lists prerequisites rather than an all-purpose conversion recipe.',[('Image concentration','Interpret quantitative units and correction status. Check whether values are already normalized.'),('Activity and time','Use a consistent administered-activity and decay reference. Preserve relevant timestamps.'),('Normalization','Specify body-weight or another convention and ensure compatible units.')],'SUVbw = activity concentration / (reference activity / body mass)')
s=SVG('Partial-volume effects blur small sources','Illustrative profiles: limited resolution broadens and lowers a narrow peak.')
s.line(90,425,915,425,NAVY,2);s.line(90,425,90,150,NAVY,2)
for sigma,amp,col in [(35,240,TEAL),(95,240*35/95,CORAL)]:
 pts=[(x,425-amp*math.exp(-((x-490)**2)/(2*sigma*sigma))) for x in range(95,910,3)]
 s.path('M'+' L'.join(f'{x},{y:.2f}' for x,y in pts),col,4)
s.text(620,175,'Narrow source profile',18,TEAL);s.text(620,207,'Limited-resolution profile',18,CORAL)
s.text(500,477,'Position (arbitrary units) • amplitude is illustrative',18,NAVY,anchor='middle');s.save(16,'partial-volume')
flow(16,'comparison','PET change needs compatible measurements','A decline in an uptake value is not, by itself, a response classification.',[('Check both visits','Tracer, preparation, timing, units, reconstruction, and coverage.'),('Review lesions','Inspect fusion, matching, uncertain foci, and the included lesion set.'),('Interpret change','Use the accepted measure and specified clinical response framework.')],'Example: 8.0 → 6.0 is −25%; comparability still needs review')
comparison(17,'modalities','Three ophthalmic representations','These are conceptual views, not interchangeable diagnostic inputs.',[('Fundus photograph','A surface view of retina, disc, and visible vessels. Preserve field of view and laterality.'),('OCT volume','Depth-resolved reflectivity assembled into B-scans and volumes. Preserve scan geometry.'),('OCT angiography','Derived vascular contrast from repeated acquisitions. Preserve processing and artifact context.')],'Camera image, depth section, and vascular map answer different questions')
comparison(17,'quality','Image adequacy is a screening outcome','An ungradable image must remain visible in the service denominator.',[('Adequate','Supported camera, field, and quality. Run the defined screening task.'),('Reacquire','Correct a remediable capture problem under the acquisition workflow.'),('Persistent failure','Return no valid result and use the defined clinical follow-up pathway.')],'No valid result ≠ target disease absent')
flow(17,'grouping','Preserve the ophthalmic hierarchy','Both eyes and every derivative remain linked to the patient.',[('Patient','Assign the appropriate research partition at patient level.'),('Visits','Keep dates and longitudinal relationships available under the data policy.'),('Eyes','Preserve right/left identity and the examination aggregation rule.'),('Images and volumes','Link fields, repeat captures, B-scans, and derived maps to their source.')],'Independent image splitting can leak patient and eye information')
flow(17,'referral','A screening result is not the end of care','Measure completion as well as classification.',[('Valid result','Use the supported patient-level aggregation and referral threshold.'),('Communicate','Record the accepted result and the applicable follow-up action.'),('Track completion','Distinguish completed care, unresolved referrals, and no-result cases.')],'Assess who receives the benefit, not just who receives a score')
s=SVG('Video tasks live on different time scales','Choose an evaluation unit that matches the clinical claim.')
for i,(label,detail,w,col) in enumerate([('Frame','Candidate location',160,TEAL),('Event','Persistent finding',330,CORAL),('Phase','Workflow interval',530,GOLD),('Procedure','Complete episode',735,NAVY)]):
 y=145+i*80;s.text(45,y+20,label,20,col,True);s.rect(190,y,w,36,col);s.text(200,y+25,detail,17,'white')
s.text(500,485,'Adjacent frames are correlated; a long false alarm is one important event.',17,NAVY,True,'middle');s.save(18,'timescales')
s=SVG('Capture-to-display latency','Illustrative 100 ms budget; not a clinical performance requirement.')
parts=[('Capture',20,TEAL),('Queue',10,GOLD),('Preprocess',15,CORAL),('Inference',35,NAVY),('Display',20,TEAL)];x=50
for label,ms,col in parts:
 w=ms*9;s.rect(x,220,w-3,85,col,r=0);s.text(x+w/2,205,label,16,col,True,'middle');s.text(x+w/2,271,f'{ms} ms',19,'white',True,'middle');x+=w
s.line(50,345,950,345,arrow=True);s.text(500,378,'Total latency includes every stage',23,NAVY,True,'middle')
s.box(165,415,670,75,'Freshness policy','Drop or suppress stale output; do not let queues grow indefinitely.');s.save(18,'latency')
comparison(18,'splits','Split procedures, not neighboring frames','Preserve relationships before extracting clips or stills.',[('Training procedures','Every frame, clip, and alternate encoding from a training procedure stays here.'),('Validation procedures','Tune models and operating policies using separate complete procedures.'),('Test procedures','Hold out patients/procedures; add site or operator evaluation as needed.')],'A new file name does not make a derivative an independent sample')
s=SVG('Causal versus offline video analysis','Real-time claims can use only information available at the decision time.')
s.line(65,260,940,260,NAVY,3,arrow=True)
for i in range(9):
 x=110+i*95;s.rect(x-27,232,54,54,PALE,NAVY);s.text(x,267,str(i-4),18,NAVY,True,'middle')
s.line(490,145,490,450,CORAL,3,dash=True);s.text(490,130,'Now',22,CORAL,True,'middle')
s.line(110,340,480,340,TEAL,8);s.text(265,380,'Causal window',20,TEAL,True,'middle')
s.line(110,420,870,420,GOLD,8);s.text(700,460,'Offline window may include future',17,GOLD,True,'middle')
s.text(170,195,'Past',19);s.text(795,195,'Future',19);s.save(18,'causality')
s=SVG('Whole-slide resolution pyramid','Read the scale needed for the task; preserve coordinates and physical sampling.')
for x,y,w,h,label in [(90,145,160,55,'Overview'),(55,225,230,80,'Intermediate'),(20,330,300,120,'Fine detail')]:
 s.rect(x,y,w,h,PALE,TEAL);s.text(170,y+h/2+7,label,20,TEAL,True,'middle')
s.line(345,380,455,380,arrow=True)
for r in range(3):
 for c in range(4):
  x=500+c*90;y=155+r*90;s.rect(x,y,70,70,'#f0e4ed','#b78ca9');s.circle(x+25,y+25,9,'#886c9b');s.circle(x+50,y+45,6,'#886c9b')
s.text(680,455,'Selected tiles + source coordinates',20,NAVY,True,'middle');s.save(19,'pyramid')
flow(19,'hierarchy','Pixels retain specimen provenance','Choose the split level before extracting tiles.',[('Patient and case','Clinical identity, accession, outcome, and episode of care.'),('Specimen and block','Sampled tissue and processing relationships.'),('Slide and scan','Stain, section, scanner, physical scale, and rescan version.'),('Tile and feature','Source coordinates, extraction parameters, encoder version.')],'A million tiles are not a million independent patients')
flow(19,'mil','Multiple-instance learning','A slide-level label supervises a bag of tile representations.',[('Tiles from one slide','Sample tissue at a documented physical scale with quality checks.'),('Shared encoder','Produce one representation per tile, preserving source coordinates.'),('Aggregate','Combine representations into a slide or case score under a defined rule.')],'Attention weights are not automatically lesion probabilities')
flow(19,'quality','Pathology processing remains auditable','Inspect the model output on the original source slide.',[('Source quality','Check tissue presence, focus, folds, stain, and supported specimen.'),('Optional processing','Record any stain normalization, tissue masking, and scale conversion.'),('Tile inference','Run the pinned encoder or task model with reproducible sampling.'),('Review original','Display regions and accepted measurements on the source scan.')],'Normalization cannot recover tissue that was not sampled or scanned')
comparison(20,'measurement','Three quantities that must remain distinct','A common numeric output does not make the evidence interchangeable.',[('Native measurement','A calibrated acquisition and defined analysis produce the measured quantity.'),('Cross-modal estimate','A model predicts a target from another acquisition; validate agreement and use.'),('Extracted report value','OCR or parsing retrieves an existing result; validate extraction and provenance.')],'Measurement validity, prediction validity, and extraction accuracy differ')
flow(20,'router','Route by representation and task','General orchestration still needs task-specific evidence.',[('Identify','Original signal or rendered derivative? Which acquisition and question?'),('Check prerequisites','Identity, units, geometry, quality, permissions, and supported inputs.'),('Choose action','Run a validated compatible tool, or return an explicit unsupported state.')],'Do not fabricate missing calibration or diagnostic competence')
flow(21,'architecture','A reviewable imaging AI architecture','Logical responsibilities; deployment boundaries can vary.',[('Browser viewer','Source images, geometry, interaction tools, review state.'),('Authenticated gateway','Authorized PACS retrieval and controlled result storage.'),('Orchestrator + workers','Eligible manifests, versioned jobs, models, quality checks.'),('Reviewed results','Source-linked outputs, user edits, acceptance, and controlled export.')],'Trace source → transforms → model → review → clinical record')
flow(21,'lifecycle','Computation and acceptance are separate states','Failures and cancellation remain part of the audit trail.',[('Eligible → queued','Freeze the source manifest and assign an idempotent job key.'),('Running','Record version and progress; support bounded retry and cancellation.'),('Draft → reviewed','Preserve original output, corrections, and accepted interpretation.'),('Exported','Use source references and duplicate-safe publication; retain supersession.')],'A completed model call is not yet a clinical result')
flow(22,'fairness','Evaluate benefit across the patient pathway','Unequal exclusions can disappear when only successful inference is counted.',[('Access + acquisition','Who gets examined, and whose images meet quality requirements?'),('Valid output','Who receives a usable result, and which errors occur?'),('Clinical action','How do alerts, recalls, delays, and review burden differ?'),('Completed care','Who obtains follow-up and experiences the intended benefit?')],'Report denominators, uncertainty, and unresolved cases at every stage')
flow(22,'lifecycle','Change control is a continuing process','A model update can change inputs, thresholds, interfaces, or workflow.',[('Propose change','State the intended benefit and which behaviors may change.'),('Evaluate evidence','Review technical, clinical, subgroup, and human-factors implications.'),('Controlled release','Assign ownership, versions, monitoring, and a rollback path.'),('Monitor + respond','Investigate adverse signals and correct or roll back when needed.')],'A stable intended use makes improvement measurable')
print('Generated',sum(len(list((ROOT/'figures'/f'ch{n}').glob('*.svg'))) for n in range(12,23)),'SVGs for chapters 12–22.')
