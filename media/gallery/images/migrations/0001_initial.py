# Generated by Django 4.2.4 on 2024-04-15 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("community", "0024_alter_communitysidebarmenu_module_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="GalleryImagesFileTypes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ext",
                    models.CharField(unique=True, verbose_name="Filename Extension"),
                ),
                ("mime", models.CharField(verbose_name="File Mimetype")),
                ("name", models.CharField(verbose_name="File Type Name")),
                (
                    "active",
                    models.BooleanField(default=True, verbose_name="File Type Active"),
                ),
            ],
            options={
                "db_table": "media_gallery_images_filetypes",
            },
        ),
        migrations.CreateModel(
            name="GalleryImagesSettings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "max_filesize",
                    models.IntegerField(
                        default=25,
                        help_text="The absolute maximum file size allowed in the Gallery in megabytes. All modules are limited by this parameter.",
                        verbose_name="Maximum File Size in MB",
                    ),
                ),
                (
                    "enable_exif",
                    models.BooleanField(
                        default=True,
                        help_text="Enable EXIF Parsing Features",
                        verbose_name="Enable EXIF Parsing",
                    ),
                ),
                (
                    "min_dpi",
                    models.IntegerField(
                        default=150,
                        help_text="Images with lower DPI values will generate a warning, they can still be uploaded.",
                        verbose_name="Minimum Recommended DPI",
                    ),
                ),
                (
                    "rescaler_enabled",
                    models.BooleanField(
                        default=True,
                        help_text="When enabled, the gallery will generate device-sized images for all major device resolutions, reducing bandwidth and data usage",
                        verbose_name="Rescale to target device screens",
                    ),
                ),
                (
                    "rescaler_factor",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Rescaler Factor to use in scaling down images (default is -0.10 or -10%: i.e. decrements of 10% from the max size)",
                        max_digits=4,
                        verbose_name="Rescaler Factor",
                    ),
                ),
                (
                    "downloads_enabled",
                    models.BooleanField(
                        default=False,
                        help_text="Allow users to enable downloading of their media files from their galleries.",
                        verbose_name="Enable Downloading Files",
                    ),
                ),
                (
                    "community",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="community.community",
                        unique=True,
                        verbose_name="Community",
                    ),
                ),
                (
                    "enabled_filetypes",
                    models.ManyToManyField(
                        help_text="Select which File types are allowed in this Gallery.",
                        to="images.galleryimagesfiletypes",
                        verbose_name="Enabled Filetypes",
                    ),
                ),
            ],
            options={
                "db_table": "media_gallery_images_settings",
            },
        ),
    ]
