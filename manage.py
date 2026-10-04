#!/usr/bin/env python
"""ابزار خط فرمان جنگو برای اجرای پروژه."""
import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vlogsite.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "جنگو نصب نیست یا در PYTHONPATH نمی‌باشد. لطفاً محیط مجازی را فعال کنید."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
