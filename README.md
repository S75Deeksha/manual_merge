# ⚔️ Manual Merge Demo - Conflict Resolution

## Why Manual Merge?
Both branches changed `draw_star(50, "cyan")` vs `draw_star(200, "lime")` on SAME LINE. Git: "You decide."

## The Battl
## Human Victory
1. Git added `<<<<<<< HEAD` markers
2. We chose `draw_star(150, "gold")` - compromise
3. `git add` + `git commit` sealed merge

## Run the Peace Treaty
```bash
python draw_star.py
e
