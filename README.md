# bsa-aviation

Lesson plans, handouts, and instructor notes for a 2-session Aviation merit badge class (90 minutes each).

## What's in this repo

- `curriculum/` – timed session agendas
- `handouts/` – scout-facing worksheets/handouts (print or export to PDF)
- `instructor-notes/` – instructor guides, checklists, and sign-off tracking
- `slides/` – generated PowerPoint decks
- `tools/` – slide generation script

Reference material:

- `requirements.md` – full merit badge requirement wording
- `cug-complete_20260122.pdf` – supporting reference document

## Curriculum

- `curriculum/session-1-plan.md`
- `curriculum/session-2-plan.md`

## Handouts

- `handouts/req-1-flight-basics-handout.md`
- `handouts/req-2-drone-safety-flight-log.md`
- `handouts/req-5-opportunities-handout.md`
- `handouts/vfr-sectional-symbols-faq.md`

## Instructor notes

- `instructor-notes/instructor-guide-session-1.md`
- `instructor-notes/instructor-guide-session-2.md`
- `instructor-notes/instructor-guide-session-2-drone.md`
- `instructor-notes/instructor-guide-session-2-requirement-5.md`
- `instructor-notes/materials-checklist.md`
- `instructor-notes/signoff-tracker.md`

## Slides (PowerPoint)

Generated decks:

- `slides/session-1.pptx`
- `slides/session-2.pptx`
- `slides/session-2-req-5.pptx` (Requirement 5 classroom module; no drone flight)

To regenerate the slide decks:

1. Ensure you have Python 3 installed.
2. Install the generator dependency (`python-pptx`) into your preferred environment.
3. Run: `python tools/generate_slides.py`

## How to use

1. Print/share the handouts in `handouts/`.
2. Run Session 1 using `curriculum/session-1-plan.md` and the matching instructor guide.
3. Run Session 2 using `curriculum/session-2-plan.md` and the matching instructor guide(s) for the track you pick.
4. Use `instructor-notes/signoff-tracker.md` to track completion.
