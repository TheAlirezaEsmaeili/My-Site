from django.db import migrations
from django.utils.text import slugify


DEFAULT_TITLE = "اولین روز فیلم‌برداری در دل کویر"
DEFAULT_SUMMARY = (
    "روایت یک روز کامل از سفر به کویر مرکزی ایران؛ از طلوع آفتاب روی تپه‌های شنی "
    "تا شب‌نشینی زیر آسمان پر ستاره."
)
DEFAULT_CONTENT = (
    "این اولین پستی است که در این ولاگ منتشر می‌شود. قرار است در این سفر، تجربه‌ی "
    "سه روز اقامت در کویر مرکزی ایران را برایتان روایت کنم؛ از لحظه‌ای که ماشین را "
    "در جاده‌ی خاکی متوقف کردیم تا سکوت عجیب کویر را بشنویم، تا شب‌هایی که دوربین "
    "را روی سه‌پایه گذاشتم و مسیر ستاره‌ها را ثبت کردم.\n\n"
    "در قسمت‌های بعدی درباره‌ی تجهیزاتی که همراه بردم، نکات فیلم‌برداری در نور کم و "
    "تجربه‌ی اقامت در اقامتگاه‌های بومی کویر بیشتر می‌نویسم. اگر سوالی درباره‌ی این "
    "سفر دارید، در بخش نظرات همین پست بپرسید."
)


def create_default_post(apps, schema_editor):
    Post = apps.get_model("blog", "Post")
    if not Post.objects.exists():
        Post.objects.create(
            title=DEFAULT_TITLE,
            slug=slugify(DEFAULT_TITLE, allow_unicode=True),
            summary=DEFAULT_SUMMARY,
            content=DEFAULT_CONTENT,
        )


def remove_default_post(apps, schema_editor):
    Post = apps.get_model("blog", "Post")
    Post.objects.filter(slug=slugify(DEFAULT_TITLE, allow_unicode=True)).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_default_post, remove_default_post),
    ]
