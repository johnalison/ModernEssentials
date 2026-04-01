# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Course materials for **Modern Physics (33-211)** at Carnegie Mellon University — Special Relativity and Quantum Mechanics. The repo holds LaTeX source for homeworks and exams, Keynote-based lecture slides (distributed as PDFs), and a Python grade-management pipeline.

## Build

Compile the syllabus:
```
make syllabus   # runs: pdflatex Syllabus.tex
```

For homeworks and exams (no Makefile targets), compile directly from their subdirectory:
```
cd RelativityKinematics && pdflatex homework1.tex
```

Each subdirectory's `.tex` files use `\input{../latexSetup}` and `\input{../defs}`, so `pdflatex` must be run from within the subdirectory (not the repo root).

## LaTeX Architecture

- `latexSetup.tex` — shared preamble: KOMA-Script `scrartcl`, physics packages (`braket`, `txfonts`, `amsmath`), `fancyhdr`. Inputs `../defs`.
- `defs.tex` — shared macro library: physics notation shortcuts (`\GeV`, `\pt`, `\adagger`, etc.) and layout helpers (`\multiline`, `\lineTwo`, `\rmt`).
- All homeworks and exams `\input{../latexSetup}` at the top; they do **not** have their own `\documentclass`.

## Grade Pipeline

Student data lives in `Grades/` and flows through three stages:

1. **`makeGrades.sh`** — AWK script that transforms a Canvas CSV roster into Python dict format; output is pasted into `grades.py`.
2. **`grades.py`** — manually maintained dict: `{name: (m1, m2, m3, final, hw_percent)}`. Tuple length encodes how many assessments have occurred (1–5); `plotGrades.py` uses this to determine which plots to generate.
3. **`plotGrades.py`** — reads `grades`, computes stats, and writes plots to the current directory as both PDF and PNG.

Run grade analysis from `Grades/`:
```
cd Grades && python plotGrades.py
```

Grade weights (hardcoded in `plotGrades.py`): 10% homework, 45% combined midterms, 45% final.
Exam point totals (also hardcoded): Midterm 1 = 90 pts, Midterm 2 = 90 pts, Midterm 3 = 80 pts, Final = 200 pts.

## Course Structure

| Directory | Content |
|---|---|
| `RelativityKinematics/` | Lectures 1–10 (spacetime, Lorentz transforms, Doppler) + HW 1–3 |
| `RelativityDynamics/` | Lectures 11–18 (four-vectors, energy-momentum, GR intro) + HW 4 |
| `QuantumPhysics/` | Lectures 19–39 (blackbody → Schrödinger → periodic table) + HW 5–9 |
| `Exam{1,2,3}/`, `Final/` | Exam source and solutions |
| `Grades/` | Grade data and analysis scripts |
