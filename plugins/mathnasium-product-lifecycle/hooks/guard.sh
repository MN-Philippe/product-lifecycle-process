#!/usr/bin/env bash
# PreToolUse guard for the mathnasium-product-lifecycle plugin.
#
# Backs up the write policy in standards/jira-conventions.md so it does not depend on the
# model following instructions:
#   * GitHub issues and pull requests are read-only: GitHub connector writes, gh issue/PR
#     writes, GitHub API writes, and browser interaction on github.com are denied.
#     Local git (including git push) is not touched.
#   * Every Confluence write asks first: the handbook is the plugin's read-only reference.
#   * Every Jira write (create, edit, comment, transition, link, worklog) asks the user to
#     confirm, even when the connector is set to "always allow". A batch approval in chat
#     still produces one prompt per Jira write.
#
# Plain bash + grep/sed on purpose: no Python, so a Mac without developer tools never sees an
# install dialog. Fails open on unreadable input. Browser detection is best-effort: it cannot
# see what a coordinate click lands on.

payload=$(cat)
tool=$(printf '%s' "$payload" | sed -n 's/.*"tool_name"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -n 1)
[ -z "$tool" ] && exit 0
input="${payload#*\"tool_input\"}"

emit() { # decision reason
  printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"%s","permissionDecisionReason":"%s"}}\n' "$1" "$2"
  exit 0
}

GITHUB_DENY="GitHub issues and pull requests are read-only in this plugin. Reading repos, code and pull requests is fine; creating, commenting on, editing or closing GitHub issues or pull requests is not. Tell the user you will not do it and stop. Jira Stories are the work items here; a repo means a Code Dependency value."
JIRA_ASK="Jira write: confirm only if the user approved this exact draft or before/after in a later reply. A batch approval in chat still prompts once per Story. See the Write policy in the Jira Conventions page of the handbook."

CONFLUENCE_ASK="Confluence write: the Technology and Product Handbook is read-only for this plugin. Confirm only if the user explicitly asked to edit or create this page or comment."

server=""
name="$tool"
if [ "${tool#mcp__}" != "$tool" ]; then
  rest="${tool#mcp__}"
  server="${rest%%__*}"
  name="${rest#*__}"
fi
server_lc=$(printf '%s' "$server" | tr '[:upper:]' '[:lower:]')
name_lc=$(printf '%s' "$name" | tr '[:upper:]' '[:lower:]')
tool_lc=$(printf '%s' "$tool" | tr '[:upper:]' '[:lower:]')

# GitHub connector: reads only.
case "$server_lc" in
  *github*)
    if printf '%s' "$name" | grep -Eq '^(get_|list_|search_|issue_read$|pull_request_read$|actions_get$|actions_list$|run_secret_scanning$)'; then
      exit 0
    fi
    emit deny "$GITHUB_DENY"
    ;;
esac

# Command line: gh issue/PR writes and GitHub API writes. git push is deliberately allowed.
if [ "$tool" = "Bash" ]; then
  if printf '%s' "$input" | grep -Eq '(^|[^[:alnum:]_-])gh[[:space:]]+(issue|pr|release|repo|label|gist|project|discussion|workflow|run|ruleset|secret|variable)[[:space:]]+(create|comment|edit|close|reopen|merge|review|delete|transfer|lock|unlock|ready|rerun|cancel|fork|archive|rename|sync|run|enable|disable|set|add|remove)([^[:alnum:]_-]|$)'; then
    emit deny "$GITHUB_DENY"
  fi
  if printf '%s' "$input" | grep -Eq '(^|[^[:alnum:]_-])gh[[:space:]]+api([^[:alnum:]_-]|$)' &&
     printf '%s' "$input" | grep -Eqi '(-X|--method)[ =]*(POST|PATCH|PUT|DELETE)|[[:space:]]-[fF][[:space:]]|--field|--raw-field|--input'; then
    emit deny "$GITHUB_DENY"
  fi
  if printf '%s' "$input" | grep -Eqi 'api\.github\.com' &&
     printf '%s' "$input" | grep -Eqi '(-X|--request)[ =]*(POST|PATCH|PUT|DELETE)|[[:space:]]-d[[:space:]]|--data'; then
    emit deny "$GITHUB_DENY"
  fi
  exit 0
fi

# Browser tools: no interaction on github.com (reading and navigating are fine).
if printf '%s' "$tool_lc" | grep -Eq 'chrome|browser|playwright|puppeteer|computer'; then
  input_lc=$(printf '%s' "$input" | tr '[:upper:]' '[:lower:]')
  if printf '%s' "$input_lc" | grep -q 'github\.com' &&
     printf '%s %s' "$tool_lc" "$input_lc" | grep -Eq 'click|type|fill|form_input|press|submit|key|select|upload|drag|write'; then
    emit deny "$GITHUB_DENY"
  fi
fi

# Confluence writes: the handbook is read-only here, so always ask.
if [ -n "$server" ] &&
   printf '%s' "$name_lc" | grep -Eq 'confluence' &&
   printf '%s' "$name_lc" | grep -Eq '^(create|edit|update|add|delete|remove|set)'; then
  emit ask "$CONFLUENCE_ASK"
fi

# Jira writes: always ask.
if [ -n "$server" ] &&
   printf '%s' "$name_lc" | grep -Eq 'jira|issuelink' &&
   printf '%s' "$name_lc" | grep -Eq '^(create|edit|update|add|transition|delete|assign|link|remove|set)'; then
  emit ask "$JIRA_ASK"
fi

exit 0
