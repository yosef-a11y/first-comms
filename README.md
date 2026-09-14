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

- [ ] **Hero photo** — a slot is wired up and commented out in `index.html`.
      Save a real photo as `images/hero.jpg` (~1600x460, under 250KB) and delete
      the comment wrapper around the `<figure class="hero-photo">` block.
- [ ] **Project gallery** — same idea, three images at `images/install-1..3.jpg`.
- [ ] **Reviews** — the section is built and styled but deliberately left
      commented out rather than filled with invented testimonials. It needs three
      real quotes: the customer's own words, their name, and the month.
- [ ] **Analytics** — currently reports to Steady Growth's GA4 property
      (`G-7BZ01Y3KFS`). Swap it in all three files if FirstComms wants their own.
- [ ] **Form** — posts to Web3Forms using Steady Growth's access key. Swap for
      the client's key if leads should go straight to them.

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
