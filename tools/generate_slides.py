"""Generate class-facing PowerPoint decks for the Aviation merit badge sessions.

Outputs:
- slides/session-1.pptx
- slides/session-2.pptx

This script intentionally uses concise, class-facing bullets and puts extra detail
into speaker notes for the instructor.

Usage:
  .venv/bin/python tools/generate_slides.py
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional

from pptx import Presentation
from pptx.util import Inches, Pt


ROOT = Path(__file__).resolve().parents[1]
SLIDES_DIR = ROOT / "slides"


@dataclass(frozen=True)
class SlideSpec:
    title: str
    bullets: List[str]
    notes: Optional[str] = None


def _add_title_and_bullets(prs: Presentation, spec: SlideSpec) -> None:
    layout = prs.slide_layouts[1]  # Title and Content
    slide = prs.slides.add_slide(layout)

    slide.shapes.title.text = spec.title

    body = slide.shapes.placeholders[1].text_frame
    body.clear()
    for i, bullet in enumerate(spec.bullets):
        p = body.paragraphs[0] if i == 0 else body.add_paragraph()
        p.text = bullet
        p.level = 0

    # Typography tweaks for readability
    for p in body.paragraphs:
        for run in p.runs:
            run.font.size = Pt(28)

    if spec.notes:
        notes = slide.notes_slide.notes_text_frame
        notes.clear()
        notes.text = spec.notes


def _add_title_slide(prs: Presentation, title: str, subtitle: str) -> None:
    slide = prs.slides.add_slide(prs.slide_layouts[0])  # Title
    slide.shapes.title.text = title
    slide.placeholders[1].text = subtitle

    # Slightly larger title for room visibility
    for run in slide.shapes.title.text_frame.paragraphs[0].runs:
        run.font.size = Pt(44)


def _add_quick_activity_slide(prs: Presentation, title: str, steps: Iterable[str], notes: str) -> None:
    _add_title_and_bullets(
        prs,
        SlideSpec(
            title=title,
            bullets=[f"Step {i+1}: {s}" for i, s in enumerate(steps)],
            notes=notes,
        ),
    )


def build_session_1() -> Presentation:
    prs = Presentation()

    _add_title_slide(
        prs,
        title="Aviation Merit Badge – Session 1",
        subtitle="Aviation basics • How flight works • What pilots see in the cockpit",
    )

    slides: List[SlideSpec] = [
        SlideSpec(
            title="Today’s goals",
            bullets=[
                "What counts as an aircraft",
                "Fixed wing vs rotary wing",
                "Engines: piston vs turbine vs jet",
                "Four forces of flight",
                "Lift + airfoils (Bernoulli + downwash)",
                "Control surfaces (pitch/roll/yaw)",
                "Cockpit instruments (what they tell the pilot)",
            ],
            notes=(
                "Keep this fast. Mention that Session 2 is hands-on with model/drone flight.\n"
                "If running short on time later: compress history and keep time for forces/lift/controls/instruments."
            ),
        ),
        SlideSpec(
            title="What is an aircraft?",
            bullets=[
                "A machine that flies by being supported by air",
                "It can create lift with wings…",
                "…or lift/thrust with rotors",
            ],
            notes="Ask: name 3 aircraft you’ve seen and one thing it’s used for.",
        ),
        SlideSpec(
            title="Kinds of aircraft (examples)",
            bullets=[
                "Fixed-wing airplane (training, transport, cargo)",
                "Rotary-wing (helicopter) (EMS, rescue, lifting)",
                "Other: glider • balloon • jet airliner • drone/UAS",
            ],
            notes="Have scouts categorize examples quickly. Keep it concrete.",
        ),
        SlideSpec(
            title="A short history of flight (3 moments)",
            bullets=[
                "Balloons: first human flight (buoyancy)",
                "Wright era: powered + controlled flight",
                "Turbines/jets: speed, altitude, long-distance travel",
            ],
            notes="Story-driven, not date-driven. Ask: what enabled long-distance travel?",
        ),
        SlideSpec(
            title="Fixed wing vs rotary wing",
            bullets=[
                "Fixed wing: needs forward motion to make lift",
                "Efficient for long distance",
                "Rotary wing: rotors can hover",
                "Great for point-to-point access",
            ],
            notes="Common misconception: helicopters still generate lift; it’s just from rotor blades.",
        ),
        SlideSpec(
            title="Engines: big picture",
            bullets=[
                "Piston + prop: like a car engine turning a propeller",
                "Turbine: hot gases spin turbine blades",
                "Jet (turbofan): pushes air back to make thrust",
            ],
            notes="Keep it conceptual; avoid deep thermodynamics.",
        ),
        SlideSpec(
            title="The 4 forces of flight",
            bullets=[
                "Lift (up)",
                "Weight (down)",
                "Thrust (forward)",
                "Drag (back)",
            ],
            notes="Draw the arrows on a simple airplane sketch. In level cruise: lift≈weight, thrust≈drag.",
        ),
        SlideSpec(
            title="Lift: how wings make it",
            bullets=[
                "Air moves around an airfoil",
                "Pressure differences help create lift",
                "Wings also push air downward (downwash)",
            ],
            notes="Use paper-strip demo. Phrase it: pressure + downwash.",
        ),
        SlideSpec(
            title="Angle of attack (AOA) + stall",
            bullets=[
                "AOA = angle between wing and airflow",
                "Too high AOA → stall (lift drops, drag rises)",
                "Rule of thumb: many wings stall around ~15–20° AOA",
            ],
            notes=(
                "Clarify: 15–20° is a common rule-of-thumb, not universal; depends on airfoil, flaps, contamination, loading.\n"
                "Key point: stalls are caused by AOA, not speed alone."
            ),
        ),
        SlideSpec(
            title="Control surfaces",
            bullets=[
                "Ailerons → roll",
                "Elevator → pitch",
                "Rudder → yaw",
            ],
            notes="Use hand/airplane model to show roll/pitch/yaw. Mention coordinated turns (bank + appropriate rudder).",
        ),
        SlideSpec(
            title="Cockpit instruments (single-engine)",
            bullets=[
                "Airspeed • Altimeter • Attitude",
                "Heading • Turn/Bank • Vertical speed",
                "Compass • Navigation • Communication",
                "Engine indicators (RPM, temps, pressures, fuel)",
            ],
            notes="Explain what each tells the pilot; emphasize cross-checking multiple instruments.",
        ),
        SlideSpec(
            title="Wrap-up + next steps",
            bullets=[
                "Session 2: safety-first flight principles in action",
                "Drone option: complete FAA TRUST before next session",
                "Bring questions and your handouts",
            ],
            notes="Mention follow-up airport/tower/ARTCC visits if you’re offering them.",
        ),
    ]

    for spec in slides:
        _add_title_and_bullets(prs, spec)

    return prs


def build_session_2() -> Presentation:
    prs = Presentation()

    _add_title_slide(
        prs,
        title="Aviation Merit Badge – Session 2",
        subtitle="Safety briefing • How to fly • Walk out • Drone flight • Debrief",
    )

    slides: List[SlideSpec] = [
        SlideSpec(
            title="Pre-work (do before today)",
            bullets=[
                "Complete FAA TRUST (required to fly)",
                "Fill out preflight sections on the flight log",
                "Wear closed-toe shoes",
            ],
            notes="If someone doesn’t have TRUST, they can observe/record and schedule follow-up flight.",
        ),
        SlideSpec(
            title="Today’s goals",
            bullets=[
                "Fly safely (one pilot at a time)",
                "Successful takeoff → controlled hover → landing",
                "Connect what you see to the 4 forces",
                "Quick overview of aviation pathways (afterward / at home)",
            ],
            notes="Keep content brief; put most instruction before going outside.",
        ),
        SlideSpec(
            title="Safety rules (non-negotiable)",
            bullets=[
                "Visual line of sight (VLOS)",
                "No flying over people",
                "Stay inside the flight box",
                "No stunts—slow and smooth",
                "If anything feels unsafe: LAND",
            ],
            notes="Define the boundary and observer line. Use consistent callouts: taking off, landing, abort, clear.",
        ),
        SlideSpec(
            title="Roles (rotate each flight)",
            bullets=[
                "Pilot",
                "Visual observer",
                "Safety marshal",
                "Recorder",
            ],
            notes="Rotate roles every pilot so everyone participates even with 1 drone.",
        ),
        SlideSpec(
            title="How the controls move the drone",
            bullets=[
                "Throttle: up/down power",
                "Yaw: turn left/right",
                "Pitch/Roll: tilt → move",
            ],
            notes=(
                "Key teaching: tilt trades vertical lift for horizontal motion; that’s why altitude can change when you move.\n"
                "Coaching: small inputs, pause, then adjust."
            ),
        ),
        SlideSpec(
            title="What counts as success today",
            bullets=[
                "Safe takeoff",
                "Stable hover (3–5 seconds)",
                "Safe landing in the box",
            ],
            notes="If time allows, add a slow square pattern. If a scout struggles, shorten the attempt and prioritize safe landing.",
        ),
        SlideSpec(
            title="Walk out + set the flight box",
            bullets=[
                "Walk as a group",
                "Mark boundaries and observer line",
                "One group preflight check",
            ],
            notes="Budget ~10 minutes total for walk + boundary setup (adjust to your site).",
        ),
        SlideSpec(
            title="During flight: quick science callouts",
            bullets=[
                "More speed → more drag",
                "Tilt forward → some lift becomes horizontal motion",
                "Wind → drift and extra corrections",
            ],
            notes="Keep this as short callouts, not a lecture.",
        ),
        SlideSpec(
            title="Debrief questions",
            bullets=[
                "What safety rule mattered most?",
                "What helped stability?",
                "How is a drone like a helicopter?",
            ],
            notes="Use these while walking back or during sign-off time.",
        ),
        SlideSpec(
            title="After class: Requirement 5 (at home)",
            bullets=[
                "Pilot certificates ladder (student → private → instrument → commercial → ATP)",
                "Remote pilot certificate vs TRUST",
                "Choose 1 aviation career to research",
            ],
            notes="Point them to the Req 5 handout for deeper work during the week.",
        ),
        SlideSpec(
            title="Follow-up opportunities",
            bullets=[
                "Airport visit",
                "Control tower visit (if available)",
                "ZKC facility visit (if available)",
            ],
            notes="Mention scheduling constraints and behavior/ID/photo rules.",
        ),
    ]

    for spec in slides:
        _add_title_and_bullets(prs, spec)

    return prs


def main() -> None:
    SLIDES_DIR.mkdir(parents=True, exist_ok=True)

    session_1 = build_session_1()
    session_1_path = SLIDES_DIR / "session-1.pptx"
    session_1.save(session_1_path.as_posix())

    session_2 = build_session_2()
    session_2_path = SLIDES_DIR / "session-2.pptx"
    session_2.save(session_2_path.as_posix())

    print(f"Wrote {session_1_path.relative_to(ROOT)}")
    print(f"Wrote {session_2_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
