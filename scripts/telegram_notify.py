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


def build_ci_message() -> str:
    lint_status = required_env("LINT_STATUS")
    tests_status = required_env("TESTS_STATUS")
    branch = required_env("BRANCH")
    author = required_env("AUTHOR")
    run_url = required_env("GITHUB_RUN_URL")

    is_success = lint_status == "success" and tests_status == "success"
    title = "✅ <b>CI passed</b>" if is_success else "❌ <b>CI failed</b>"

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
    pr_number = required_env("PR_NUMBER")
    pr_title = required_env("PR_TITLE")
    author = required_env("PR_AUTHOR")
    branch = required_env("PR_BRANCH")
    pr_url = required_env("PR_URL")

    return "\n".join(
        [
            "🟡 <b>PR opened</b>",
            "",
            f"<b>PR:</b> #{html.escape(pr_number)} {html.escape(pr_title)}",
            f"<b>Author:</b> {html.escape(author)}",
            f"<b>Branch:</b> {html.escape(branch)}",
            "",
            f'<a href="{html.escape(pr_url)}">Open PR</a>',
        ]
    )


def build_pr_approved_message() -> str:
    pr_number = required_env("PR_NUMBER")
    pr_title = required_env("PR_TITLE")
    reviewer = required_env("REVIEW_AUTHOR")
    pr_url = required_env("PR_URL")

    return "\n".join(
        [
            "✅ <b>PR approved</b>",
            "",
            f"<b>PR:</b> #{html.escape(pr_number)} {html.escape(pr_title)}",
            f"<b>Approved by:</b> {html.escape(reviewer)}",
            "",
            f'<a href="{html.escape(pr_url)}">Open PR</a>',
        ]
    )


NOTIFICATION_BUILDERS: dict[str, Callable[[], str]] = {
    "ci": build_ci_message,
    "pr_opened": build_pr_opened_message,
    "pr_approved": build_pr_approved_message,
}


def build_message() -> str:
    notification_type = required_env("NOTIFICATION_TYPE")

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
