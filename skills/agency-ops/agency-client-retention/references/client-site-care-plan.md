# Client-Site Care Plan Specification

Parent skill: [agency-client-retention](../SKILL.md). Read when defining,
selling, delivering or auditing a website maintenance retainer, or when a
client declines a retainer and needs a self-care handbook.

A site is never finished. The care plan makes the hidden post-launch work
visible, owned and evidenced. The engine's `maintenance-calendar.md` governs
the engine itself; this file governs client websites.

## Components

### 1. Backups

1. List everything that needs backing up: site source and build, any database
   (CMS, cart, forms), uploaded media, email or subscriber lists, DNS records,
   and configuration.
2. Store backups **off the hosting server**, and keep a **second copy in a
   different place or provider**.
3. Name backups by date (`YYYYMMDD`) so they sort in order.
4. Match frequency to how often content changes.
5. **Check automated backups are still running** every month, and **test a
   restore** at least quarterly. An untested backup is `NOT_ASSESSED`.
6. Record who is responsible. Hosts rarely promise backups; if the client has
   no care plan, the client owns this duty and must be told so in writing.

Where power or connectivity interruptions are frequent, cloud and
second-location copies are essential, not optional.

### 2. Monthly functional inspection

Keep a spreadsheet of every URL and check at least monthly:

- pages load; images present; links working (use a link checker);
- forms: submit a real test and a deliberately invalid one; confirm the message
  arrives in a mailbox someone reads;
- embeds, galleries, facades and video still work;
- checkout, booking and payment buttons;
- WhatsApp and phone links still reach the business;
- security and platform updates applied; uptime monitor green.

Retest after major browser releases.

### 3. Content-update streams

Run three separate routines, each with an owner and a realistic cadence:

1. new articles or news items;
2. new pages (new service, new staff member, new location);
3. revisions to existing pages, with a dated update note where readers expect
   one; keep each page's single focus.

Trial a schedule for a month, then adjust. Starting small and increasing beats
an ambitious cadence that stops.

### 4. Contact-information audit (at least twice a year)

- Registrar, hosting, DNS and CMS account emails and phone numbers.
- Every place contact details appear: pages, footer, structured data, business
  listings, PDFs, archived pages, form recipient settings, email signatures.
- WhatsApp numbers (they change with staff turnover).
- Keep contact details in one shared snippet or data file so one edit updates
  every page.

### 5. Security and access hygiene

- Credentials rotated after staff or vendor changes; 2FA on; the
  [client asset ownership register](../../../orchestration/website-builder/references/client-asset-ownership-register.md)
  re-verified.
- Unused scripts, files, accounts and plugins removed; directory listing off;
  public error output off; form input validated and sanitised server-side.
- Security gate re-run after material changes (see `security-gate`).
- Sensitive data (card numbers, passwords) never stored in site files or sent
  by plain email; third-party processors disclosed in the privacy policy.

### 6. Content protection

Copyright notice with start and current year; usage terms or an explicit licence;
periodic searches for copied text or images.

### 7. Performance and search

Monthly field Core Web Vitals scorecard and regression run (see
[performance retainer service](performance-retainer-service.md)); Search
Console coverage and error review (see `seo-audit`).

### 8. Twice-yearly purpose review

Re-read the outcomes-and-jobs table from intake. Is each page still serving an
outcome? What should be added, merged or removed?

## Tiers (example structure; price by scope, not by these labels)

| Tier | Includes |
|---|---|
| Essential | Backups with quarterly restore test, uptime monitoring, security updates, monthly functional inspection, contact audit |
| Growth | Essential plus content-update streams, performance scorecard, search health review, quarterly report |
| Partner | Growth plus quarterly tune-up sprint, tag review, conversion experiments, twice-yearly strategy review |

Route commercial wording for care plans to the proposal engine; this file owns
the delivery specification and evidence.

## Evidence produced

| Evidence | Acceptance condition |
|---|---|
| Backup log | Dates, locations, restore-test result |
| Inspection sheet | Every URL, date checked, defects and fixes |
| Contact audit record | Locations checked and corrections made |
| Access review | Accounts reviewed, removed and rotated |

## Self-care handbook (clients without a care plan)

Hand over a one-page version of sections 1–5 with the client's named owner for
each duty. This protects the client and the agency's reputation.

## Sources

- Plumley, G. (2011) *Website Design and Development: 100 Questions to Ask
  Before Building a Website*, Wiley Publishing — backups, monthly checks,
  content-update routine, contact audit and security housekeeping.
