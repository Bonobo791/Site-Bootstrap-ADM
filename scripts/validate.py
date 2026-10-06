"""Validate bundled skills, local links and the bootstrap test lockfile."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent.parent
BOOTSTRAP = ROOT / "skills/site-bootstrap-adm"
skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
assert BOOTSTRAP / "SKILL.md" in skills, "Missing bootstrap skill"
assert ROOT / "skills/plan-sites-and-apps-adm/SKILL.md" in skills, "Missing planner skill"
for main in skills:
    text = main.read_text()
    match = re.match(r"---\n(.*?)\n---\n", text, flags=re.S)
    assert match, f"Missing skill frontmatter: {main}"
    fields = dict(line.split(": ", 1) for line in match.group(1).splitlines())
    assert set(fields) == {"name", "description"}, f"Unexpected frontmatter: {main}"
    assert fields["name"] == main.parent.name, f"Skill name mismatch: {main}"
    assert fields["description"].startswith("Use when"), f"Missing trigger: {main}"
    assert len(text.splitlines()) < 500, f"Main skill too long: {main}"
    assert (main.parent / "agents/openai.yaml").exists(), f"Missing metadata: {main}"
for path in [ROOT / "README.md", ROOT / "AGENTS.md", *(ROOT / "skills").rglob("*.md")]:
    if "node_modules" in path.parts:
        continue
    for link in re.findall(r"\]\(([^)]+)\)", path.read_text()):
        if "://" in link or link.startswith("#"):
            continue
        target = (path.parent / link.split("#", 1)[0]).resolve()
        assert target.is_relative_to(ROOT), f"Escaping link: {path}: {link}"
        assert target.exists(), f"Broken link: {path}: {link}"
example = BOOTSTRAP / "assets/fast-check-example"
package = json.loads((example / "package.json").read_text())
lock = json.loads((example / "package-lock.json").read_text())
assert package["devDependencies"]["fast-check"] == lock["packages"][""]["devDependencies"]["fast-check"]
print(f"{len(skills)} skills: frontmatter, links, metadata and fast-check lockfile verified.")
