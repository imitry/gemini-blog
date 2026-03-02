#!/usr/bin/env bash
set -euo pipefail

# gemini-blog uninstaller
# Cleanly removes all blog skills, agents, templates, and scripts

main() {
    local SKILL_DIR="${HOME}/.gemini/skills"
    local AGENT_DIR="${HOME}/.gemini/agents"

    echo "=== Uninstalling gemini-blog ==="
    echo ""

    # Remove main skill (includes references, templates, scripts)
    if [ -d "${SKILL_DIR}/blog" ]; then
        rm -rf "${SKILL_DIR}/blog"
        echo "  Removed: ${SKILL_DIR}/blog/"
    fi

    # Remove sub-skills
    for skill in blog-write blog-rewrite blog-analyze blog-brief blog-calendar blog-strategy blog-outline blog-seo-check blog-schema blog-repurpose blog-geo blog-audit blog-chart; do
        if [ -d "${SKILL_DIR}/${skill}" ]; then
            rm -rf "${SKILL_DIR}/${skill}"
            echo "  Removed: ${SKILL_DIR}/${skill}/"
        fi
    done

    # Remove agents
    for agent in blog-researcher blog-writer blog-seo blog-reviewer; do
        if [ -f "${AGENT_DIR}/${agent}.md" ]; then
            rm -f "${AGENT_DIR}/${agent}.md"
            echo "  Removed: ${AGENT_DIR}/${agent}.md"
        fi
    done

    echo ""
    echo "=== gemini-blog uninstalled ==="
    echo ""
    echo "Restart Gemini CLI to complete removal."
}

main "$@"
