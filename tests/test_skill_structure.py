from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_public_skill_package_structure():
    assert (ROOT / "SKILL.md").is_file()
    assert (ROOT / "agents" / "openai.yaml").is_file()
    assert (ROOT / "references" / "workflow.md").is_file()
    assert (ROOT / "references" / "example-generic-product.md").is_file()
    assert (ROOT / "tests" / "trigger-cases.md").is_file()


def test_readme_has_install_and_boundary():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "npx skills add" in readme
    assert "Search terms" in readme
    assert "不是律师意见" in readme


if __name__ == "__main__":
    test_public_skill_package_structure()
    test_readme_has_install_and_boundary()
    print("design patent public package checks passed")
