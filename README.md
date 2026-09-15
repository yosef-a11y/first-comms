# first-comms.com

Landing page for FirstComms — emergency responder radio coverage (ERRC / BDA)
testing, design, installation and yearly testing.

Static, no build step. Three self-contained HTML files; CSS and JS are inlined,
there are no webfonts and no images, so the whole page is one request.

| File | Purpose |
| --- | --- |
| `index.html` | The landing page |
| `thank-you.html` | Post-submission page — fires the `generate_lead` conversion |
| `privacy.html` | Privacy policy (required for lead-gen ads) |
| `CNAME` | Tells GitHub Pages the custom domain |

## Deploying

Push to `main`. GitHub Pages serves it. That's the whole process.

## Local preview

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

## Still to do

- [x] **Photos** — three in the equipment section. There is deliberately no
      photo in the hero: it was tried three ways (band beneath, above the form,
      filling the right side) and none of them improved on the plain
      headline-and-form hero, so the hero stays text. `images/hero.jpg` and
      `images/install-4.jpg` are kept in the repo, unused, if that changes.
- [ ] **Photo provenance** — the equipment section is titled "What actually goes
      on your wall" and captioned descriptively, because these images are not
      documented as FirstComms' own projects. If they ARE photos of your installs,
      retitle it "Recent work" and caption each with the building type and town;
      that is a stronger proof section. If they are stock or generated, leave the
      wording as it is — claiming them as your projects would not be true.
      `images/install-4.jpg` is a spare, currently unused.
- [ ] **Reviews** — the section is built and styled but deliberately left
      commented out rather than filled with invented testimonials. It needs three
      real quotes: the customer's own words, their name, and the month.
- [ ] **Analytics** — currently reports to Steady Growth's GA4 property
      (`G-7BZ01Y3KFS`). Swap it in all three files if FirstComms wants their own.
- [ ] **Form recipient — ONE ACTION OUTSTANDING.** Leads are meant to go to
      dan@cellsignalsolutions.com. In Web3Forms the recipient is the address the
      access key was issued to; it cannot be set from the markup. So:
      1. Go to web3forms.com and enter `dan@cellsignalsolutions.com`.
      2. Web3Forms emails the access key to that address.
      3. Put it in `index.html` in place of the current `access_key` value.
      Until that happens the form still works, but submissions go to
      yosef@steadygrowthmarketing.com — the key is left in place deliberately so
      no lead is dropped in the meantime. Send a live test afterwards and confirm
      Dan receives it.

- [x] **WhatConverts** — installed in the `<head>` of all three pages
      (profile 170287). Verify two things on the live site: that dynamic number
      insertion swaps all three `tel:` placements on the landing page (header,
      footer, mobile call bar), and that the tracking number forwards to
      732-302-8992. Form capture hooks the submit event before the redirect.

## Google Ads notes

- Final URLs must point at `https://first-comms.com/` — the display URL domain
  has to match, which is the reason this page has its own domain at all.
- `?kw=` on the URL swaps the H1 to match the ad group. Supported values:
  `bda-install`, `errcs`, `testing`, `failed-test`, `annual`, `das`. Only keys in
  that table render, so query text never reaches the page.
- `gclid`, `wbraid` and `gbraid` are captured on arrival and kept for 90 days, so
  a visitor who lands from an ad and submits days later still attributes.
- Negative keywords matter on these terms: `cell booster`, `weboost`,
  `cell phone signal`, `wifi`, `jobs`, `salary`, `training`, `diy`.
