# Project context: learning-toolkit

Advisory and research workspace for **Clare's Early Years Toolkit** (early-childhood-education product). Not a code project; this folder holds research, gap analysis, market analysis, retro notes, and Clare's source materials.

## Roles

- **Clare**, founder. Chrissy's sister-in-law.
- **Chrissy**, advisor and sounding board. Not the founder, not building, not the public face.

When drafting anything destined for Clare, use the family-relational tone: warm and sisterly, two deliverables (sendable message + private notes). Private notes always land in `_docs/clare-feedback-notes.md` (gitignored).

## Folder layout

```
_docs/
  *.md                                       strategic docs
  early-years-toolkit-project-pack.html      all-in-one project pack
  clare-feedback-notes.md                    private notes (gitignored, local only)
  retro/                                     weekly retros
  source-materials/                          Clare's source artefacts
                                             (PDFs, pitch deck, audio + transcripts, transcribe.py)
```

## Where things go

- New strategic doc, append to `_docs/<kebab-case-name>.md`
- New material from Clare (PDF, pitch update, voice memo), drop in `_docs/source-materials/`
- Weekly retro, run `/weekly-retro` (creates `_docs/retro/wk-N-YYYY-MM-DD.md`)
- Private feedback for Chrissy only, append to `_docs/clare-feedback-notes.md`

## Project-specific gitignore

- `*.mp4` Clare's voice memos, local only
- `/_docs/clare-feedback-notes.md` private notes

The matching `audioclip-*.transcript.txt` files **are** tracked. Only the source audio is local-only.

## Filename exception

Audio files and their matching transcripts under `_docs/source-materials/` keep their machine-generated names (`audioclip-<timestamp>-<id>.*`). The lowercase-kebab-case rule applies to human-curated names; auto-generated identifiers stay as recorded.

## Pointers

- Universal rules and voice conventions: [`c:\dev\playbook\rules.md`](file:///c:/dev/playbook/rules.md)
- Active projects index: [`c:\dev\playbook\projects.md`](file:///c:/dev/playbook/projects.md)
