"""Validate this bundle's skill metadata and local Markdown references."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills/site-bootstrap-adm"
text = (SKILL / "SKILL.md").read_text()
match = re.match(r"---\n(.*?)\n---\n", text, flags=re.S)
assert match, "Missing skill frontmatter"
fields = dict(line.split(": ", 1) for line in match.group(1).splitlines())
assert set(fields) == {"name", "description"}, "Unexpected frontmatter fields"
assert fields["name"] == SKILL.name, "Skill name mismatch"
assert fields["description"].startswith("Use when"), "Missing trigger"
assert len(text.splitlines()) < 500, "Main skill too long"
for path in [ROOT / "README.md", *SKILL.rglob("*.md")]:
    if "node_modules" in path.parts:
        continue
    for link in re.findall(r"\]\(([^)]+)\)", path.read_text()):
        if "://" in link or link.startswith("#"):
            continue
        target = (path.parent / link.split("#", 1)[0]).resolve()
        assert target.is_relative_to(ROOT), f"Escaping link: {path}: {link}"
        assert target.exists(), f"Broken link: {path}: {link}"
example = SKILL / "assets/fast-check-example"
package = json.loads((example / "package.json").read_text())
lock = json.loads((example / "package-lock.json").read_text())
assert package["devDependencies"]["fast-check"] == lock["packages"][""]["devDependencies"]["fast-check"]
assert (SKILL / "agents/openai.yaml").exists(), "Missing interface metadata"
print("Skill frontmatter, local links, interface metadata and example lockfile verified.")
