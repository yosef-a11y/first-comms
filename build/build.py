import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shell

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIZ = 'https://first-comms.com/#business'

def page(slug, title, desc, h1, lede, crumb, body, faqs, service_name):
    url = f'https://first-comms.com/{slug}/'
    faq_ld = [{"@type":"Question","name":q,
               "acceptedAnswer":{"@type":"Answer","text":a}} for q, a in faqs]
    ld = {"@context":"https://schema.org","@graph":[
      {"@type":"WebPage","@id":url+"#webpage","url":url,"name":title,
       "description":desc,"isPartOf":{"@id":"https://first-comms.com/#website"},
       "about":{"@id":BIZ},"inLanguage":"en-US"},
      {"@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":"https://first-comms.com/"},
        {"@type":"ListItem","position":2,"name":crumb,"item":url}]},
      {"@type":"Service","name":service_name,"provider":{"@id":BIZ},
       "areaServed":{"@type":"State","name":"New Jersey"},"url":url},
      {"@type":"FAQPage","mainEntity":faq_ld}]}

    faq_html = '\n'.join(f'''        <div class="faq-item">
          <button class="faq-q" type="button" aria-expanded="false">
            {q}
            <svg class="chev" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>
          </button>
          <div class="faq-a"><p>{a}</p></div>
        </div>''' for q, a in faqs)

    others = [s for s in SLUGS if s[0] != slug]
    related = '\n'.join(
        f'        <li><a href="/{s}/"><strong>{n}</strong><span>{b}</span></a></li>'
        for s, n, b in others)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#240D07">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="format-detection" content="telephone=yes">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">

<meta property="og:type" content="website">
<meta property="og:site_name" content="FirstComms">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://first-comms.com/images/og-image.png">
<meta name="twitter:card" content="summary_large_image">

{shell.ICON}
<link rel="stylesheet" href="/styles.css">
{shell.JSCLASS}

{shell.GTAG}

<script type="application/ld+json">
{json.dumps(ld, indent=2)}
</script>

{shell.WC}
</head>

<body>
<a class="skip" href="#lead-form">Skip to the enquiry form</a>
{shell.SPRITE}

{shell.HEADER_SUB.replace(f'href="/{slug}/"', f'href="/{slug}/" aria-current="page"')}

<main id="top">

  <section class="hero">
    <div class="container hero-grid">
      <div class="hero-copy">
        <nav class="crumb" aria-label="Breadcrumb">
          <a href="/">FirstComms</a> <span aria-hidden="true">&rsaquo;</span> <span>{crumb}</span>
        </nav>
        <h1 id="hero-headline">{h1}</h1>
        <p class="hero-sub">{lede}</p>

        <ul class="hero-points">
          <li><svg width="17" height="17" viewBox="0 0 24 24"><use href="#i-check"/></svg>
            <span><strong>Testing</strong> that tells you whether you even need a system</span></li>
          <li><svg width="17" height="17" viewBox="0 0 24 24"><use href="#i-check"/></svg>
            <span><strong>Design and installation</strong> by our own crew</span></li>
          <li><svg width="17" height="17" viewBox="0 0 24 24"><use href="#i-check"/></svg>
            <span><strong>Yearly testing</strong> after, so you stay compliant</span></li>
        </ul>

        <div class="badge-row" aria-label="Standards we build to">
          <span class="badge">IFC 510</span>
          <span class="badge">NFPA 1225</span>
          <span class="badge">NFPA 72</span>
          <span class="badge">UL 2524</span>
          <span class="badge">14+ Years</span>
        </div>
      </div>

{shell.FORM}
    </div>
  </section>

{body}

  <section class="cta-band">
    <div class="container cta-inner">
      <div>
        <p class="cta-h">Tell us about the building.</p>
        <p>We&rsquo;ll tell you what&rsquo;s required and what it costs to find out. No obligation.</p>
      </div>
      <div class="cta-actions">
        <a class="btn" href="#lead-form">Ask about your building</a>
        <a class="btn btn-line phone-link" href="tel:+17323028992">732-302-8992</a>
      </div>
    </div>
  </section>

  <section class="section" id="faq">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Questions</span>
        <h2>What people ask us about this</h2>
      </div>
      <div class="faq" id="faqList">
{faq_html}
      </div>
    </div>
  </section>

  <section class="section bg-card">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Also on this site</span>
        <h2>Related</h2>
      </div>
      <ul class="related">
{related}
      </ul>
    </div>
  </section>

</main>

{shell.FOOTER_SUB}

{shell.CALLBAR}

{shell.TAIL}
</body>
</html>
'''

SLUGS = [
 ('errc-systems','ERRC systems','What the code asks for, and how a building proves it'),
 ('bda-systems','BDA systems','The equipment itself — what goes in and what it costs to run'),
 ('rf-testing','RF &amp; radio coverage testing','How a building is measured, and what the report says'),
]

def sec(id_, eyebrow, h2, lede, inner, cls='section'):
    return f'''  <section class="{cls}" id="{id_}">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">{eyebrow}</span>
        <h2>{h2}</h2>
        <p class="lede">{lede}</p>
      </div>
{inner}
    </div>
  </section>
'''

def cards(items):
    out = []
    for i, (t, p) in enumerate(items, 1):
        out.append(f'''        <div class="card reveal">
          <h3>{t}</h3>
          <p>{p}</p>
        </div>''')
    return '      <div class="grid-3">\n' + '\n'.join(out) + '\n      </div>'

def steps(items):
    out = []
    for i, (t, p) in enumerate(items, 1):
        out.append(f'''        <div class="step reveal"><b>{i:02d}</b><h3>{t}</h3>
          <p>{p}</p></div>''')
    return '      <div class="steps">\n' + '\n'.join(out) + '\n      </div>'

# ---------------------------------------------------------------- ERRC
errc_body = (
 sec('what','The short version','An ERRC system is how a building passes the radio test',
   'ERRC stands for Emergency Responder Radio Coverage. It is the requirement, and the equipment '
   'installed to meet it. If firefighters cannot talk on their handheld radios inside your building, '
   'the building does not comply — and an ERRC system is what fixes that.',
   cards([
     ('Why buildings fail','Concrete, steel, low-emissivity glass and anything below grade absorb radio signal. '
      'Modern energy-efficient construction is particularly good at it, which is why new buildings fail as often as old ones.'),
     ('What gets installed','A donor antenna on the roof, an amplifier, and antennas distributed through the building. '
      'You will see the same thing called a BDA or a public safety DAS.'),
     ('Who decides','Your local fire official. Codes set the benchmark, but the authority that signs off on your '
      'building is the one whose interpretation counts.'),
   ]))
 + sec('code','What the code asks for','The four standards that come up',
   'Which apply depends on your jurisdiction and when the building was permitted. These are the ones that '
   'appear on nearly every New Jersey project.', cards([
     ('IFC Section 510','The in-building radio coverage requirement itself: adequate coverage for emergency responders, '
      'and the testing to demonstrate it.'),
     ('NFPA 1225','Sets the coverage benchmark — signal strength and intelligibility — and the annual testing obligation. '
      'It absorbed the older NFPA 1221.'),
     ('NFPA 72','Covers supervision and monitoring: the system has to report its own faults rather than fail quietly.'),
     ('UL 2524','The product standard for the amplifier and enclosure. Equipment that is not listed to it will not be accepted.'),
     ('Annual testing','Required every year, and it is the building owner&rsquo;s obligation, not the installer&rsquo;s. '
      'Records have to be available to the fire official.'),
     ('12-hour backup','Systems are generally required to run on battery through a power loss, in a monitored enclosure.'),
   ]), cls='section bg-card')
 + sec('prove','How compliance is proven','Four steps from flagged to signed off',
   'Nothing here is guesswork. Each step produces a document the fire official can look at.',
   steps([
     ('Test the building as it stands','A grid test measures signal in every part of the building. '
      'The result is a written report, and some buildings pass without any equipment at all.'),
     ('Design to what the test found','If it fails, the test data says where and by how much. The design follows from that '
      '— not from a template, and not from a guess about the building.'),
     ('Install and commission','Our own crew installs it. Commissioning proves the installed system actually delivers the '
      'coverage the design promised.'),
     ('Certify, then test yearly','Final acceptance testing produces the certification. After that it is an annual test, '
      'battery checks and records kept current.'),
   ]), cls='section bg-dark')
)

# ---------------------------------------------------------------- BDA
bda_body = (
 sec('what','The equipment','A BDA is an amplifier, plus everything that makes it legal',
   'BDA stands for bi-directional amplifier. On its own it is one box on a wall. A system that passes inspection is '
   'that box plus the antenna that feeds it, the cabling that distributes it, the battery that keeps it alive and the '
   'panel that reports when something is wrong.',
   cards([
     ('Donor antenna','On the roof, aimed at the public safety tower. It picks up the signal the building is blocking. '
      'Aiming it is survey work, not guesswork — the wrong heading undoes everything downstream.'),
     ('The amplifier','The BDA itself, in a NEMA-rated enclosure. It boosts the signal in both directions: tower to handheld, '
      'and handheld back out to the tower.'),
     ('Distributed antennas','Coax and antennas carrying the signal to every floor, stairwell, elevator lobby and basement. '
      'This is most of the labour on a job.'),
     ('Battery backup','Generally 12 hours of standby, in a monitored enclosure, so the system survives the power loss '
      'that often accompanies the emergency.'),
     ('Annunciator panel','Usually in the fire command centre. It reports antenna failure, amplifier failure, low battery — '
      'so a dead system announces itself instead of being discovered during a fire.'),
     ('UL 2524 listing','The product standard for this equipment. Unlisted hardware fails inspection regardless of how well it performs.'),
   ]))
 + sec('class','Choosing equipment','Class A or Class B, and why it matters to you',
   'The distinction is the one specification question worth understanding before you buy, because it decides whether '
   'your system can be fixed when the radio landscape changes around it.', cards([
     ('Class A — channelised','Amplifies only the specific channels your responders use. Cleaner, far less likely to '
      'interfere with the public safety network, and easier to get approved. Costs more.'),
     ('Class B — broadband','Amplifies the whole band. Cheaper, quicker to configure, but it amplifies everything in the '
      'band including noise, and some jurisdictions will not accept it.'),
     ('What we do','We size it to the building and to what the local system actually uses. A Class B on a site that '
      'needed Class A is the kind of saving that gets paid back at the inspection.'),
   ]), cls='section bg-card')
 + sec('install','Installation','What the work actually looks like on site',
   'Mostly it is cabling. The schedule is driven by access to risers, stairwells and occupied floors far more than '
   'by the equipment itself.', steps([
     ('Survey and test','Before anything is specified, the building is measured. This tells us how much gain is needed '
      'and where the antennas have to go.'),
     ('Design and submittal','Drawings, equipment schedule and the cut sheets your fire official will want to see. '
      'We do not handle permitting in house, but we provide the documentation your permit needs.'),
     ('Rough-in and install','Our own crew — not subcontractors. Coax, antennas, the amplifier, the battery enclosure '
      'and the annunciator, co-ordinated around whoever else is in the building.'),
     ('Commission and certify','The installed system is tested against the same grid as the original survey. '
      'That comparison is the proof it works.'),
   ]), cls='section bg-dark')
)

# ---------------------------------------------------------------- RF testing
rf_body = (
 sec('what','What a test is','A measurement, not an opinion',
   'A radio coverage test measures whether a handheld radio works everywhere inside your building. It is done against '
   'a grid, with calibrated equipment, and it produces a document. The point is that nobody has to take anyone&rsquo;s '
   'word for it — including ours.',
   cards([
     ('Signal strength','Measured in dBm. There is a floor below which a radio simply will not hold a usable connection, '
      'inbound from the tower and outbound back to it. Both directions are tested.'),
     ('Intelligibility','Signal alone is not enough — the audio has to be understandable under stress. '
      'This is scored, and a building can have signal and still fail here.'),
     ('The grid','The floor plan is divided into roughly equal areas and each one is measured. Coverage is a percentage '
      'of areas passed, not an average, so one dead stairwell cannot be hidden by a strong lobby.'),
   ]))
 + sec('areas','Where it matters most','Critical areas are held to a higher bar',
   'Most of a building is judged on general coverage. A short list of places is judged more strictly, because they are '
   'where responders work when things go wrong.', cards([
     ('General areas','The bulk of the building — offices, corridors, tenant space. Judged on overall coverage across the grid.'),
     ('Critical areas','Fire command centre, exit stairs, elevators and lobbies, pump and generator rooms, '
      'and areas below grade. Held to a higher percentage.'),
     ('The places that fail','Basements, parking structures, concrete cores, lift shafts and anything surrounded by '
      'earth or steel. If a building fails, it usually fails here first.'),
   ]), cls='section bg-card')
 + sec('report','What you get','A report you can hand to the fire official',
   'The deliverable is a document, not a phone call. It states what was measured, where, and whether it passes.',
   steps([
     ('Grid results','Every measured area with its readings, so a fail can be located rather than argued about.'),
     ('Pass or fail, stated plainly','Against the benchmark your jurisdiction applies. If the building passes, '
      'that is the end of it — there is nothing to install and nothing to buy.'),
     ('If it fails, what it would take','The same data that shows the failure shows the fix: how much gain, '
      'and roughly where the antennas need to go. That becomes the design.'),
     ('Timing advice','Test before the inspection is booked, not the week of it. A failed test discovered late is the '
      'expensive version of this problem.'),
   ]), cls='section bg-dark')
)

PAGES = [
 dict(slug='errc-systems',
   title='ERRC Systems in New Jersey | Requirements &amp; Compliance | FirstComms',
   desc='What an ERRC system is, which codes apply, and how a building proves compliance. Emergency responder radio coverage testing and installation across New Jersey.',
   h1='ERRC systems: <span class="hl">what the code asks for</span>, and what that means for your building.',
   lede='If a fire official, architect or inspector has told you your building needs an ERRC system, this page explains '
        'what that is, which standard it comes from, and what it takes to satisfy it. Measurement first &mdash; some buildings '
        'already pass.',
   crumb='ERRC systems', body=errc_body, service_name='ERRC system compliance, testing and installation',
   faqs=[
     ('What does ERRC actually stand for?','Emergency Responder Radio Coverage. It describes both the requirement — that '
      'firefighters and police can use their handheld radios anywhere inside a building — and the system installed to meet it. '
      'You will hear the same system called a BDA or a public safety DAS.'),
     ('Who decides whether my building needs one?','Your local fire official has the final say. Codes such as IFC 510 and '
      'NFPA 1225 set the benchmark, but the authority signing off on your building applies it. That is why we test to the '
      'standard your jurisdiction actually uses rather than a generic one.'),
     ('Can my building pass without installing anything?','Yes, and some do. If the existing signal already meets the benchmark '
      'throughout, you get the report and install nothing. That is the honest reason to test before buying equipment.'),
     ('Will this hold up my certificate of occupancy?','It can. Radio coverage is commonly checked before final sign-off, so a '
      'missing or failed test is one of the few things that can keep a finished building empty. Testing early is much cheaper '
      'than testing late.'),
     ('Do you handle the permit?','No — permitting is not done in house. We provide the drawings, equipment schedules and test '
      'documentation your permit application needs, and work alongside whoever is filing it.'),
     ('Does this apply to existing buildings, or only new construction?','Both. It comes up most often on new construction, '
      'because coverage is checked before the certificate of occupancy and that gives it a hard deadline. But the requirement '
      'is about the building, not its age. Existing buildings get caught by it during renovations, a change of use, or simply '
      'when a fire official tests the building and it fails. If you own an occupied building that has never been tested, you '
      'do not currently know whether it passes.'),
   ]),
 dict(slug='bda-systems',
   title='BDA Systems &amp; Installation in New Jersey | FirstComms',
   desc='What a BDA system is made of, how Class A and Class B differ, and what installation involves. Bi-directional amplifier design and installation across New Jersey.',
   h1='BDA systems: <span class="hl">the equipment</span> that fixes in-building radio coverage.',
   lede='A bi-directional amplifier is what gets installed when a building cannot pass its radio coverage test. '
        'This page covers what is in one, the choice between Class A and Class B, and what the installation actually involves.',
   crumb='BDA systems', service_name='BDA system design and installation', body=bda_body,
   faqs=[
     ('Is a BDA the same thing as an ERRC system?','In everyday use, yes. ERRC is the requirement, BDA is the main piece of '
      'equipment used to meet it, and public safety DAS is another name for the same installation. If someone quoted you for '
      'one and someone else specified the other, they are talking about the same job.'),
     ('What does a BDA system cost?','It depends on the size of the building, how many floors need covering and how strong the '
      'outside signal is — a weak donor signal means more equipment. Anyone giving a firm number before testing is guessing. '
      'We price it once the test says what is actually needed.'),
     ('What is the difference between Class A and Class B?','Class A amplifies only the specific channels your responders use. '
      'Class B amplifies the whole band. Class A is cleaner, less likely to interfere with the public safety network and easier '
      'to get approved; Class B is cheaper. Some jurisdictions will not accept Class B at all.'),
     ('Does the equipment need to be UL listed?','Yes. UL 2524 is the product standard for this equipment, and hardware that is '
      'not listed to it will not be accepted at inspection no matter how it performs on the day.'),
     ('Do you use subcontractors?','No. Design and installation are done by our own crew. It is the main reason we can stand '
      'behind the commissioning results rather than pointing at someone else when a system does not perform.'),
     ('Can a BDA interfere with the public safety network?','A badly configured one can. An amplifier set too broad or driven '
      'too hard can raise the noise floor for the very network it is meant to support, which is why jurisdictions care so much '
      'about how these are specified and commissioned. It is also the practical argument for Class A over Class B — amplifying '
      'only the channels in use rather than the whole band. The protection is measurement: the finished system is commissioned '
      'against the same grid used to test the building, so what it actually does is documented rather than assumed.'),
     ('How disruptive is this in an occupied building?','Most of the work is cable — risers, ceilings, stairwells. The equipment '
      'itself goes in quickly. In an occupied building the schedule is driven by access rather than by the installation: which '
      'areas we can be in, at what hours, and how much notice tenants need. It is worth raising at the survey, because it '
      'changes the sequence of the work more than it changes the price.'),
   ]),
 dict(slug='rf-testing',
   title='RF &amp; Radio Coverage Testing in New Jersey | Grid Testing | FirstComms',
   desc='How radio coverage testing works: grid testing, signal strength, intelligibility and what the report contains. Emergency responder radio coverage testing across New Jersey.',
   h1='Radio coverage testing: <span class="hl">a measured answer</span> on whether your building passes.',
   lede='Before anyone can tell you what your building needs, it has to be measured. A grid test gives you a written, '
        'defensible answer — and if the building already passes, that is the end of it.',
   crumb='RF &amp; radio coverage testing', service_name='Emergency responder radio coverage testing', body=rf_body,
   faqs=[
     ('How long does a test take?','Most buildings are measured in a day; large or complex ones take longer. The written report '
      'usually follows within a few days.'),
     ('What happens if my building fails?','The same measurements that show the failure show the fix — how much gain is needed '
      'and roughly where antennas have to go. That data becomes the system design, so a failed test is not wasted money.'),
     ('Do I need to test every year?','Yes, annual testing is generally required once a system is in, and it is the building '
      'owner&rsquo;s responsibility rather than the installer&rsquo;s. We do the yearly test, replace batteries when due and keep '
      'the records ready for the fire official.'),
     ('When in a project should we test?','Before the inspection is booked. Testing during construction tells you whether you '
      'need to budget for a system at all, and avoids finding out the week your certificate of occupancy is due.'),
     ('What does the report contain?','Grid-by-grid readings, signal strength in both directions, intelligibility scoring, and a '
      'plain pass or fail against the benchmark your jurisdiction applies — in a form you can hand to the fire official.'),
     ('What if the county changes its radio system later?','It depends what changes. A move to different channels can mean a '
      'channelised system needs re-tuning; a wider change can mean more than that. This is one of the practical reasons the '
      'annual test matters — a system that has quietly stopped matching the network it is amplifying turns up at the yearly '
      'test rather than during an emergency.'),
   ]),
]

for p in PAGES:
    html = page(p['slug'], p['title'], p['desc'], p['h1'], p['lede'],
                p['crumb'], p['body'], p['faqs'], p['service_name'])
    d = os.path.join(OUT, p['slug']); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w').write(html)
    print(f"wrote {p['slug']}/index.html  {len(html)} bytes")
