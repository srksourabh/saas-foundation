# Functional Quality, UX and Accessibility

## Functional testing

For every entity and workflow test valid, invalid, empty, duplicate, boundary, long, Unicode and special-character input; CRUD/archive/restore/bulk; cancel/back/refresh/multiple tabs/repeated click/interruption/retry; stale/concurrent updates and optimistic rollback; correct audit/notification/integration behavior; consistency across list/detail/dashboard/report/export/API; permissions and cleanup.

## Forms

Check labels, required/optional indicators, defaults, placeholders, field types, masks, autocomplete, copy/paste, validation timing, server validation, inline errors, focus movement, unsaved-change protection, double-submit prevention, disabled state, error preservation, success feedback and keyboard operation. Test dates, timezones, DST, leap day, locale, phone/email/URL, decimals, currency, negative/zero/large values and uploads.

## Tables, search, reports and files

Check columns, values, alignment, truncation, tooltips, sort, filter, search, pagination, selection, bulk actions, empty/loading/error states, responsiveness and export consistency. Test exact/partial/case/diacritics/special characters/no result/multi-filter/clear/persistence/authorization.

For reports/exports verify accuracy, ranges, timezone, currency, totals, rounding, grouping, duplicates/missing rows, filters, masking, tenant isolation, permissions, filenames, large data and CSV formula injection.

For files test allowed/invalid types, MIME mismatch, double extension, size, empty/corrupt, long/Unicode/duplicate names, cancel/retry, preview, replacement, deletion, direct URL, expiry, cross-user/tenant access and content headers. Use harmless files only.

## User journeys and usability

Map role-specific onboarding, first value, recurring critical tasks, approvals, billing, reporting, recovery, role change, deactivation and offboarding. Record start, preconditions, steps, decisions, time, completion, recovery, friction, repeated entry, hidden actions, dead ends and support needs.

Evaluate system status visibility, real-world language, control/undo, consistency, error prevention/recovery, recognition over recall, repeat-user efficiency, hierarchy, cognitive load, contextual help and trustworthy destructive/financial/sensitive actions. Score 0–100 with evidence.

## UI and responsive quality

Review typography, hierarchy, spacing, alignment, grid, colors, contrast, component variants, icons, buttons, inputs, tables, cards, dialogs, toasts, navigation and all states. Detect overlap, clipping, horizontal scroll, sticky failures, layout shift, inconsistent widths, density, touch targets and overflow.

Test at least 320×568, 375×667, 390×844, 412×915, 768×1024, 1024×768, 1280×720, 1366×768, 1440×900 and 1920×1080, plus portrait/landscape, mobile keyboard, touch, 200% zoom and Chromium/Firefox/WebKit when available.

## Accessibility

Target WCAG 2.2 AA unless scope differs. Test keyboard completion/tab order/focus, skip links/landmarks/headings, semantic controls and names, screen-reader announcements, form labels/errors, contrast and non-color cues, zoom/reflow/text spacing/orientation/target size, dialog focus/Escape, menus/dropdowns, tables/charts/images/captions, timing/motion/flashing and accessible authentication.

Record criterion only when confidently identified, affected users, task impact and remediation.

## Content and localization

Check grammar, terminology, consistency, empty states, actionable errors, date/time/currency/number formats, pluralization, text expansion, RTL readiness where relevant, translated communications and timezone clarity.
