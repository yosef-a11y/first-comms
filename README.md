# first-comms.com

Landing page for FirstComms — emergency responder radio coverage (ERRC / BDA)
testing, design, installation and yearly testing.

Static, no build step. Three self-contained HTML files; CSS and JS are inlined
and there are no webfonts, so the markup is a single request. Photographs are the
only other assets, and each viewport downloads only the crop it needs.

| File | Purpose |
| --- | --- |
| `index.html` | The landing page |
| `thank-you.html` | Post-submission page — fires the `generate_lead` conversion |
| `privacy.html` | Privacy policy (required for lead-gen ads) |
| `CNAME` | Tells GitHub Pages the custom domain |
| `robots.txt` | Crawl rules; points at the sitemap. AI crawlers allowed on purpose |
| `sitemap.xml` | One URL — the homepage. The other two pages are `noindex` |
| `llms.txt` | Plain-text brief for AI answer engines |
| `images/og-image.png` | 1200×630 share card. Regenerate if the H1 changes |
| `styles.css` | All styling, shared by every page |
| `errc-systems/`, `bda-systems/`, `rf-testing/` | Keyword pages, one per ad group |
| `build/` | **Generates the three keyword pages. Edit these, not the HTML.** |

## Deploying

Push to `main`. GitHub Pages serves it. That's the whole process.

## Local preview

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

## The keyword pages are generated — do not hand-edit them

`errc-systems/index.html`, `bda-systems/index.html` and `rf-testing/index.html` are
written by `build/build.py`. It lifts the header, footer, form, icon sprite and
tracking tags straight out of `index.html`, so the shell cannot drift out of sync
with the homepage — change the phone number or the form once and it propagates.

```bash
python3 build/build.py     # rewrites all three pages
```

Page copy and FAQs live in `build/build.py`. Anything you change directly in the
generated HTML is lost the next time it runs.

## Questions only FirstComms can answer

Content that is being held back because it would mean inventing a claim about
what the company does. Ask Dan, then the copy can be written:

- [ ] **FCC licensee consent.** Rebroadcasting a public safety frequency
      generally needs the licensee's permission. Does FirstComms handle that, or
      is it the building owner's job? This is a real buyer anxiety and nobody
      explains it — whoever does looks like the expert.
- [ ] **Interference liability.** If a system degrades the public safety network,
      who carries that? Worth stating plainly if the answer is favourable.
- [ ] **Warranty / guarantee.** What is actually promised if a system fails its
      final inspection? The site implies confidence but states no terms.
- [ ] **"Our own architect stamps the plans"** (in the `#why` section). For an
      RF/electrical system this is normally a professional engineer's stamp, not
      an architect's. Confirm the wording is right — it is a precise professional
      claim and worth getting exactly correct.

## Search Console

**Not connected yet.** Pick whichever of these is least painful:

1. **Google Analytics (easiest).** Search Console can verify through the GA4 tag
   already on the page. In Search Console choose **Add property → URL prefix →
   `https://first-comms.com/`**, then pick **Google Analytics** as the
   verification method. It works as long as you have Edit rights on property
   `G-6BRYRS4HPE` and you are signed in to the same Google account. Nothing to
   change on the site.
2. **DNS record.** Add the TXT record Search Console gives you at GoDaddy, same
   place the A records live. Verifies the whole domain including subdomains.
3. **HTML tag.** `index.html` has a commented-out `google-site-verification`
   meta tag in `<head>`. Uncomment it, paste the token in, push.

Once verified, submit `https://first-comms.com/sitemap.xml` under **Sitemaps**.

A brand-new domain takes weeks to show data, and this is a one-page site — the
organic ceiling is low until there is more than one page to rank. Search Console
is worth connecting mainly to confirm the page is indexed and to see which
queries it surfaces for, which is useful input for the ad keywords.

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
- [ ] **Search Console** — not connected. See the section above; the Google
      Analytics method needs nothing changed on the site.
- [ ] **Reviews** — the section is built and styled but deliberately left
      commented out rather than filled with invented testimonials. It needs three
      real quotes: the customer's own words, their name, and the month.
- [x] **Analytics** — reports to the FirstComms GA4 property `G-6BRYRS4HPE`.
      Two things still need doing inside GA4 itself: mark `generate_lead` as a
      key event (Admin > Events), or form submissions will not count as
      conversions; and link Google Ads to this property (Admin > Product links).
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

## Tags on the page

| Tag | ID | Pages |
| --- | --- | --- |
| GA4 | `G-6BRYRS4HPE` | all three |
| Google Ads | `AW-17861173083` | all three |
| WhatConverts | profile `170287` | all three |

GA4 and Google Ads share one `gtag.js` loader with two `config` lines. Pasting
the Ads snippet whole would load the same library twice, which Google does not
need and the visitor pays for.

**Conversion tracking is not finished.** The Ads tag alone gives remarketing and
lets Google Ads import GA4 conversions, but a Google Ads conversion action fires
its own event. Create the conversion action in Google Ads, take the send_to value
(`AW-17861173083/<label>`), and add to `thank-you.html`:

```js
gtag('event', 'conversion', { send_to: 'AW-17861173083/<label>' });
```

`thank-you.html` already fires GA4 `generate_lead` on load, so that page is the
right place for it — it is only reached after a real submission.

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
