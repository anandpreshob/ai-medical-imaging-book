"""Rebuild exact, original CXR teaching diagrams (Python standard library)."""
from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parents[1] / 'figures' / 'ch11'
OUT.mkdir(parents=True, exist_ok=True)
NAVY, TEAL, CORAL, MUTED, BG = '#18354a', '#007f86', '#c75543', '#526779', '#fbfaf6'

def canvas(title, subtitle, height=600):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{height}" viewBox="0 0 1200 {height}" role="img"><title>{escape(title)}</title>',
            '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#526779"/></marker></defs>',
            f'<rect width="1200" height="{height}" fill="{BG}"/>',
            text(50, 58, title, 30, NAVY, 'bold'), text(50, 96, subtitle, 19, MUTED)]

def text(x, y, label, size=20, color=NAVY, weight='normal', anchor='start'):
    return f'<text x="{x}" y="{y}" font-family="Arial, Helvetica, sans-serif" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}">{escape(label)}</text>'

def line(x1,y1,x2,y2,color=MUTED,width=3,arrow=False):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"'+(' marker-end="url(#arrow)"' if arrow else '')+'/>'

def box(x,y,w,h,title,lines=(),color=TEAL):
    result=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="white" stroke="{color}" stroke-width="2"/>'
    result+=text(x+20,y+34,title,22,color,'bold')
    for i,t in enumerate(lines): result+=text(x+20,y+65+i*25,t,18)
    return result

def save(name, items):
    (OUT/name).write_text('\n'.join(items+['</svg>']),encoding='utf-8')

s=canvas('Why projection changes apparent size','Same object, same source-to-detector distance; only object position changes.')
for x0, obj, label, foot in [(60,370,'Object close to detector','PA positioning reduces cardiac magnification'),(650,840,'Object farther from detector','AP positioning can magnify the cardiac silhouette')]:
    source=x0+30; detector=x0+465; cy=300; half=40
    shadow=half*(detector-source)/(obj-source)
    s += [text(x0,155,label,24,TEAL,'bold'),f'<circle cx="{source}" cy="{cy}" r="9" fill="{CORAL}"/>',
          line(source,cy,detector,cy-shadow,CORAL,2),line(source,cy,detector,cy+shadow,CORAL,2),
          line(detector,180,detector,425,NAVY,6),line(obj,cy-half,obj,cy+half,TEAL,13),
          line(detector,cy-shadow,detector,cy+shadow,CORAL,13),
          text(source,455,'Source',17,anchor='middle'),text(obj,455,'Object',17,anchor='middle'),
          text(detector,455,'Detector',17,anchor='middle'),text(x0,510,foot,18)]
s += [text(50,566,'Geometry schematic • Not to scale • Patient positioning and inspiration also affect appearance.',18,MUTED)]
save('projection-geometry.svg',s)

s=canvas('Split the patients, then use their images','Paired views and repeated examinations stay with the same patient.',620)
s += [box(50,150,510,105,'Development patients',['Choose partitions before model fitting.']),
      box(650,150,500,105,'Independent evaluation',['No fitting or threshold selection here.']),
      line(200,255,185,310,arrow=True),line(420,255,450,310,arrow=True),
      line(790,255,785,310,arrow=True),line(1030,255,1050,310,arrow=True),
      box(50,325,260,155,'Training',['Fit model parameters.','All views stay together.']),
      box(340,325,260,155,'Validation',['Choose thresholds.','Tune model choices.']),
      box(650,325,235,155,'Internal test',['Locked patient cohort.','Same source setting.']),
      box(915,325,235,155,'External test',['Different site or time.','Check prior exposure.']),
      text(50,548,'One patient → one partition. MIMIC-CXR and MIMIC-CXR-JPG are overlapping resources.',21,TEAL,'bold'),
      text(50,584,'Also guard against future reports leaking into earlier predictions and public-benchmark pretraining.',18,MUTED)]
save('evaluation-splits.svg',s)

s=canvas('How 90% sensitivity can still create many false flags','Hypothetical example • 1,000 studies • 5% prevalence • 90% sensitivity and specificity',650)
s += [text(390,161,'Finding present (50)',22,NAVY,'bold','middle'),text(795,161,'Finding absent (950)',22,NAVY,'bold','middle'),
      text(50,260,'Flagged',21,TEAL,'bold'),text(50,409,'Not flagged',21,MUTED,'bold'),
      box(220,185,350,125,'45 true positives',['Correctly flagged'],TEAL),
      box(620,185,350,125,'95 false positives',['Flagged without the target finding'],CORAL),
      box(220,335,350,125,'5 false negatives',['Target finding missed'],CORAL),
      box(620,335,350,125,'855 true negatives',['Correctly unflagged'],TEAL),
      text(50,532,'140 flags = 45 true positives + 95 false positives',27,NAVY,'bold'),
      text(50,578,'Positive predictive value = 45 / 140 = 32.1%',26,TEAL,'bold'),
      text(50,620,'Calculated teaching example; not measured performance of any named model or product.',18,MUTED)]
save('triage-workload.svg',s)

s=canvas('An agent coordinates evidence and accountable actions','Proposed workflow • Every study retains the ordinary clinical reading pathway.',800)
s += [box(50,145,330,115,'Study arrives',['Validate identity, view and input.','Determine model eligibility.']),
      box(470,145,340,115,'Evidence + model',['Retrieve verified current / prior.','Record findings and provenance.']),
      line(380,200,455,200,arrow=True),text(396,179,'eligible',16),
      box(50,360,330,125,'Exception / routine reading',['Ineligible, missing data or failure.','Unavailable is not negative.'],CORAL),
      line(205,260,205,345,arrow=True),text(218,309,'exception',17,CORAL),
      box(470,360,340,125,'Evidence-grounded draft',['No invented comparisons.','No unsupported measurements.']),
      line(640,260,640,345,arrow=True),
      box(470,585,340,130,'Clinician review',['Edit or reject, then sign.','Approve communication / tasks.']),
      line(640,485,640,570,arrow=True),
      box(880,585,270,130,'Track approved actions',['Owner; acknowledgment.','Completion or resolution.']),
      line(810,650,865,650,arrow=True),
      text(50,768,'Maintain versioned state • Deduplicate events • Audit evidence and actions • Supersede stale results',20,TEAL)]
save('agent-workflow.svg',s)
print('Wrote four diagrams')
