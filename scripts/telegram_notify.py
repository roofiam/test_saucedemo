import html
import os
import sys
import urllib.parse
import urllib.request
from collections.abc import Callable


def required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Required environment variable is missing: {name}")
    return value


def send_telegram_message(text: str) -> None:
    token = required_env("TELEGRAM_BOT_TOKEN")
    chat_id = required_env("TELEGRAM_CHAT_ID")

    payload = urllib.parse.urlencode(
        {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML",
            "disable_web_page_preview": "true",
        }
    ).encode()

    request = urllib.request.Request(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data=payload,
        method="POST",
    )

    with urllib.request.urlopen(request, timeout=10) as response:
        if response.status != 200:
            raise RuntimeError(f"Telegram API returned status: {response.status}")


def status_icon(status: str) -> str:
    return "✅" if status == "success" else "❌"


def common_pr_data() -> dict[str, str]:
    return {
        "repository": required_env("REPOSITORY"),
        "number": required_env("PR_NUMBER"),
        "title": required_env("PR_TITLE"),
        "url": required_env("PR_URL"),
        "branch": required_env("PR_BRANCH"),
        "author": required_env("PR_AUTHOR"),
    }


def build_ci_message() -> str:
    event_name = required_env("CI_EVENT_NAME")
    lint_status = required_env("LINT_STATUS")
    tests_status = required_env("TESTS_STATUS")
    branch = required_env("BRANCH")
    author = required_env("AUTHOR")
    run_url = required_env("GITHUB_RUN_URL")

    is_success = lint_status == "success" and tests_status == "success"

    titles = {
        ("pull_request", True): "✅ <b>PR checks passed</b>",
        ("pull_request", False): "❌ <b>PR checks failed</b>",
        ("push", True): "✅ <b>Main branch checks passed</b>",
        ("push", False): "❌ <b>Main branch checks failed</b>",
    }

    try:
        title = titles[(event_name, is_success)]
    except KeyError as error:
        raise RuntimeError(f"Unsupported CI event: {event_name}") from error

    return "\n".join(
        [
            title,
            "",
            f"<b>Branch:</b> {html.escape(branch)}",
            f"<b>Author:</b> {html.escape(author)}",
            "",
            f"<b>Lint:</b> {status_icon(lint_status)} {html.escape(lint_status)}",
            f"<b>UI tests:</b> {status_icon(tests_status)} {html.escape(tests_status)}",
            "",
            f'<a href="{html.escape(run_url)}">Open GitHub Actions</a>',
        ]
    )


def build_pr_opened_message() -> str:
    pr = common_pr_data()

    return "\n".join(
        [
            "🟣 <b>PR opened</b>",
            "",
            f"<b>Repository:</b> {html.escape(pr['repository'])}",
            (f"<b>PR:</b> #{html.escape(pr['number'])} {html.escape(pr['title'])}"),
            f"<b>Author:</b> {html.escape(pr['author'])}",
            f"<b>Branch:</b> {html.escape(pr['branch'])}",
            "",
            f'<a href="{html.escape(pr["url"])}">Open PR</a>',
        ]
    )


def build_pr_updated_message() -> str:
    pr = common_pr_data()
    updated_by = required_env("UPDATED_BY")

    return "\n".join(
        [
            "✏️ <b>PR updated</b>",
            "",
            f"<b>Repository:</b> {html.escape(pr['repository'])}",
            (f"<b>PR:</b> #{html.escape(pr['number'])} {html.escape(pr['title'])}"),
            f"<b>PR author:</b> {html.escape(pr['author'])}",
            f"<b>Updated by:</b> {html.escape(updated_by)}",
            f"<b>Branch:</b> {html.escape(pr['branch'])}",
            "",
            f'<a href="{html.escape(pr["url"])}">Open PR</a>',
        ]
    )


def build_pr_approved_message() -> str:
    pr = common_pr_data()
    reviewer = required_env("REVIEW_AUTHOR")

    return "\n".join(
        [
            "✅ <b>PR approved</b>",
            "",
            f"<b>Repository:</b> {html.escape(pr['repository'])}",
            (f"<b>PR:</b> #{html.escape(pr['number'])} {html.escape(pr['title'])}"),
            f"<b>PR author:</b> {html.escape(pr['author'])}",
            f"<b>Approved by:</b> {html.escape(reviewer)}",
            f"<b>Branch:</b> {html.escape(pr['branch'])}",
            "",
            f'<a href="{html.escape(pr["url"])}">Open PR</a>',
        ]
    )


def build_pr_merged_message() -> str:
    pr = common_pr_data()
    merged_by = required_env("MERGED_BY")

    return "\n".join(
        [
            "🔄 <b>PR merged</b>",
            "",
            f"<b>Repository:</b> {html.escape(pr['repository'])}",
            (f"<b>PR:</b> #{html.escape(pr['number'])} {html.escape(pr['title'])}"),
            f"<b>PR author:</b> {html.escape(pr['author'])}",
            f"<b>Merged by:</b> {html.escape(merged_by)}",
            f"<b>Branch:</b> {html.escape(pr['branch'])}",
            "",
            f'<a href="{html.escape(pr["url"])}">Open PR</a>',
        ]
    )


PR_EVENT_TYPES = {
    ("pull_request", "opened", "", False): "pr_opened",
    ("pull_request", "synchronize", "", False): "pr_updated",
    ("pull_request", "closed", "", True): "pr_merged",
    (
        "pull_request_review",
        "submitted",
        "approved",
        False,
    ): "pr_approved",
}


def resolve_pr_notification_type() -> str:
    event_name = required_env("EVENT_NAME")
    event_action = required_env("EVENT_ACTION")
    review_state = os.getenv("REVIEW_STATE", "")
    pr_merged = os.getenv("PR_MERGED", "").lower() == "true"

    event_key = (
        event_name,
        event_action,
        review_state,
        pr_merged,
    )

    try:
        return PR_EVENT_TYPES[event_key]
    except KeyError as error:
        raise RuntimeError(
            "Unsupported pull request event: "
            f"name={event_name}, "
            f"action={event_action}, "
            f"review_state={review_state}, "
            f"merged={pr_merged}"
        ) from error


NOTIFICATION_BUILDERS: dict[str, Callable[[], str]] = {
    "ci": build_ci_message,
    "pr_opened": build_pr_opened_message,
    "pr_updated": build_pr_updated_message,
    "pr_approved": build_pr_approved_message,
    "pr_merged": build_pr_merged_message,
}


def resolve_notification_type() -> str:
    return os.getenv("NOTIFICATION_TYPE") or resolve_pr_notification_type()


def build_message() -> str:
    notification_type = resolve_notification_type()

    try:
        builder = NOTIFICATION_BUILDERS[notification_type]
    except KeyError as error:
        supported_types = ", ".join(sorted(NOTIFICATION_BUILDERS))
        raise RuntimeError(
            f"Unsupported notification type: {notification_type}. "
            f"Supported types: {supported_types}"
        ) from error

    return builder()


def main() -> int:
    send_telegram_message(build_message())
    return 0


if __name__ == "__main__":
    sys.exit(main())
