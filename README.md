# Reducing A&E 4-Hour Breaches: A Patient Flow Improvement Case Study

**A Business Analysis case study using real NHS England performance data, built to demonstrate end-to-end BA delivery — from problem framing through to requirements, process redesign, and benefits tracking.**

---

## Why this project

The NHS has missed its 95% four-hour A&E standard every year since 2015. As of March 2026, the national breach rate stood at 36.2%, and 12-hour trolley waits hit a record 50,000+ patients in a single month — a real, current, high-priority problem in UK healthcare. I built this case study to practise the kind of analysis a contract BA would be asked to deliver on a Trust's Urgent & Emergency Care transformation programme: not a dashboard for its own sake, but a documented business case with stakeholder buy-in, defined requirements, and a measurable improvement target.

This sits alongside my [retail self-checkout case study](#) as the second project in a small portfolio built around one consistent BA pattern: **understand the business problem → engage stakeholders → define requirements → propose and measure a solution.**

## What's in this repo

| Folder | Contents |
|---|---|
| `docs/` | Business Requirements Document (BRD), Stakeholder Register |
| `diagrams/` | Current-state and future-state process maps (BPMN-style swimlanes) |
| `dashboard/` | Interactive HTML performance dashboard (Power BI-style KPIs and trend charts) |
| `data/` | Underlying dataset, build script, and full data dictionary / sourcing notes |

**Start here:** [`docs/BRD_Thameswood_AE_Patient_Flow.docx`](docs/BRD_Thameswood_AE_Patient_Flow.docx) — this is the primary deliverable.

## The approach, in brief

1. **Problem framing** — anchored the business case in real, cited NHS England statistics rather than a hypothetical scenario, so the "why this matters" section reflects an actual current pressure point in the UK health system.
2. **Stakeholder analysis** — mapped nine stakeholder groups against a Power/Interest (Mendelow) grid, with a RACI assignment and a tailored engagement approach for each — see `docs/Stakeholder_Register.xlsx`.
3. **Current-state process mapping** — broke the patient journey into four swimlanes (reception, triage/clinical, bed management, ward) and identified the two highest-risk handoff points causing delay.
4. **Requirements definition** — wrote functional and non-functional requirements for the highest-effort technical component (a real-time bed-board visibility tool), prioritised using MoSCoW.
5. **Future-state design** — redesigned the pathway around three interventions (rapid assessment triage, ambulatory care diversion, bed-board visibility), shown in a second process map.
6. **Benefits tracking** — defined success metrics with baselines, targets, and measurement frequency, and built a dashboard to track them.

## A note on the data

The national-level statistics cited throughout (36.2% breach rate, 7.2 million waiting list, etc.) are real and sourced — see `data/data_dictionary.md` for full citations to the House of Commons Library and Nuffield Trust. The trust-level monthly dataset (used for the dashboard and process analysis) is an **illustrative dataset modelled on those real national trends**, not an extract from any actual NHS Trust's system. I've been explicit about this distinction throughout the documents — full methodology is in the data dictionary.

## Tools used

`SQL` · `Python (pandas)` · `Power BI-style dashboarding (HTML/Chart.js for portfolio portability)` · `Microsoft Word / BRD documentation` · `Excel (stakeholder & RACI mapping)` · `BPMN-style process mapping`

## About me

I'm a Business Analyst based in London (MSc Data Science & Analytics, University of Hertfordshire; MBCS), with prior experience as a Data Analyst at NielsenIQ. I'm currently completing the IBM Business Analyst Professional Certificate ahead of IIBA ECBA. Open to BA/Data Analyst contract, freelance, and interim roles in the UK.

[LinkedIn](#) · [Portfolio](#) · [Other projects](#)
