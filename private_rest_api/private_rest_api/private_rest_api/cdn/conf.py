import os

# Configuration for Digital Ocean staticfile storage:
AWS_ACCESS_KEY_ID=os.environ.get("AWS_ACCESS_KEY_ID ")
AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME="django-research-static"
AWS_S3_ENDPOINT_URL="https://nyc3.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400"
}

AWS_LOCATION = "https://django-research-static.nyc3.digitaloceanspaces.com"

DEFAULT_FILE_STORAGE = "research_site.cdn.backends.MediaRootS3Boto3Storage"
STATICFILES_STORAGE = "research_site.cdn.backends.StaticRootS3Boto3Storage"