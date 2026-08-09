# Contributing to Caveman Linux

Thank you for helping make Linux easier to understand.

## Good Contributions

- Correct technical inaccuracies and unsafe examples.
- Simplify language without removing important meaning.
- Improve diagrams, accessibility, labs, verification, or troubleshooting.
- Add real production context while keeping beginner scope clear.
- Fix broken links, spelling, and inconsistent navigation.

For a large new chapter or a structural change, open an issue first so the learning path can be discussed before substantial work begins.

## Lesson Standard

Lessons should normally follow: Learning Objectives, Caveman Story, Big Concept Illustration, Concept Explained Simply (including “Why Should I Care?”), Real Linux Example, Commands Introduced, Caveman Tip, Common Mistakes, Hands-on Lab, Quick Recap, Interview Questions, and What's Next.

Use the analogy to introduce the concept, then state the accurate Linux model. Do not let the story imply behaviour Linux does not have.

## Command and Lab Safety

- Introduce a command in its owning lesson; later reuse should have a clear new context.
- Explain meaningful options and placeholders.
- Use disposable VM paths and accounts in labs.
- Mark privileged, destructive, network, firewall, mount, and recursive operations clearly.
- Include verification, troubleshooting clues, and cleanup.
- Never include real credentials, secrets, private IP details, or private keys.

## Images

Use the established flat educational Caveman style with warm earth colours. Prefer descriptive lowercase filenames, meaningful alt text, and a size appropriate for GitHub. Run `python scripts/optimize_images.py --check` before committing; use `--write` for safe lossless PNG optimisation.

## Validate Your Change

```bash
python scripts/check_markdown.py
python scripts/optimize_images.py --check
npx --yes markdownlint-cli2 "**/*.md"
```

Open a pull request explaining the learner problem addressed, validation performed, and screenshots when visuals changed.
