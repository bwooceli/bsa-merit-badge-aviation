# bsa-aviation

This workspace contains ready-to-print lesson plans and handouts for a 2-session Aviation merit badge class (90 minutes each).

## Folders

- `curriculum/` – session plans (timed agendas)
- `handouts/` – scout-facing worksheets/handouts (print or share as PDF)
- `instructor-notes/` – prep checklists, sign-off trackers, logistics

## Instructor guides

- `instructor-notes/instructor-guide-session-1.md`
- `instructor-notes/instructor-guide-session-2.md`

## Slides (PowerPoint)

Generated decks:

- `slides/session-1.pptx`
- `slides/session-2.pptx`

To regenerate (requires `python-pptx` in the repo `.venv`):

- `./.venv/bin/python tools/generate_slides.py`

## How to use

1. Print the handouts in `handouts/` (or export to PDF).
2. Run Session 1 using `curriculum/session-1-plan.md`.
3. Run Session 2 using `curriculum/session-2-plan.md`.
4. Use `instructor-notes/signoff-tracker.md` to track completion.

> Note: Requirement wording is kept in `requirements.md`. The handouts reference requirement numbers and provide aligned checklists/exercises without reprinting long requirement text.
