# Client Asset Ownership Register

Parent skill: [website-builder](../SKILL.md). Read at kickoff (start the
register), before launch (verify it) and at handover or offboarding (hand it
over). Deploy's DNS and SSL checklist depends on it.

The client owns the website's foundations: domain, hosting account, email,
analytics, search console, business profiles, code, content and design files.
The agency may hold delegated access to do its work, never ownership. This
protects the client if the agency relationship ends and is a strong trust
signal in markets where "the designer registered the domain in his own name"
is a familiar story.

## Rules

1. **The client is the domain registrant**, using the organisation's legal
   name and address. The agency may be the technical contact so it can manage
   DNS and renewals on the client's behalf; it is never the registrant.
2. **Durable registrant email.** Use an address that will survive a lapsed
   domain or a staff change (not a mailbox on the same domain, not one
   employee's personal inbox). Record who reads it.
3. **Separate credentials** for registrar, hosting, DNS, CMS, email and
   analytics. Domain and hosting may sit with different providers.
4. **Named accounts, not shared logins.** Each contractor gets their own
   account with the least access needed, removed when the work ends.
5. **Rotate** every credential a departing staff member or vendor had.
6. **Two-factor authentication** on every account that supports it, with
   recovery codes stored by the client.
7. **One registrar** for all of the client's domains where practical; auto-renew
   on; transfer lock on; several expiry reminders to the durable email.
8. **Renewal-letter scams.** Warn the client that "renewal" notices from
   unfamiliar registrars are usually transfer requests; renew only inside the
   real registrar account.
9. **Exit rights.** For any hosted platform, record exactly what the client can
   take away on leaving (content, design, code, data, redirects).
10. **Unknown owner.** If nobody knows who holds the domain, check the public
    registration record (where not privacy-masked) and the registrar; recover
    it with proof of engagement where necessary. Registry dispute procedures
    differ by country code (for example `.ug`, `.ke`); check the current
    registry policy before advising.

## Register template

| Asset | Provider | Owner of record | Technical contact | Login holder(s) | 2FA method | Renewal date | Auto-renew | Paid by / method | Recovery email | Exit rights | Last verified |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Primary domain | | Client legal entity | Agency (optional) | | | | | | | | |
| Defensive domains (misspellings, campaign domains) | | | | | | | | | | | |
| DNS | | | | | | | | | | | |
| Hosting / CDN | | | | | | | | | | | |
| Email service | | | | | | | | | | | |
| Code repository | | | | | | | | | | | |
| CMS or content source | | | | | | | | | | | |
| Analytics property | | | | | | | | | | | |
| Search Console / webmaster tools | | | | | | | | | | | |
| Business profile listings (for example Google Business Profile) | | | | | | | | | | | |
| Social and ads business accounts | | | | | | | | | | | |
| WhatsApp Business number (whose SIM, whose phone) | | | | | | | | | | | |
| Payment gateway or merchant account | | | | | | | | | | | |
| Form endpoint and recipient mailboxes | | | | | | | | | | | |
| Design source files and font licences | | | | | | | | | | | |
| Photography and stock licences | | | | | | | | | | | |

Never store passwords in the register. Record where each credential is held
(the client's password manager) and who holds it.

## Gates

- **Kickoff:** register started; any asset held by a third party flagged as a
  delivery risk.
- **Pre-launch:** registrant checked against the client entity; durable email
  verified; test and temporary accounts removed; shared passwords rotated.
- **Handover / offboarding:** register handed to the client owner with a signed
  or recorded acknowledgement; agency access reduced to what the retainer
  requires.

## Client wording

- "You will be the registered owner of [domain]. We are listed as technical
  contact only, so we can help without holding the keys."
- "Everything we build is yours: content, design files, code and accounts. If
  you move to another provider, this is exactly what goes with you: [list]."

## Worked example

A Kampala school finds its domain registered to a former volunteer. Steps:
check the registration record, contact the registrant, escalate to the
registrar with proof of engagement if needed, set the school as registrant with
a durable admin email, list the agency as technical contact, rotate all
passwords and record the result in the register.

## Sources

- Plumley, G. (2011) *Website Design and Development: 100 Questions to Ask
  Before Building a Website*, Wiley Publishing — domain, hosting and access
  ownership questions; register structure and East African rows are this
  engine's own.
