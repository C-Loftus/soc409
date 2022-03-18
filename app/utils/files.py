def allowed_image(app, filename):
    # We only want files with a . in the filename
    try:
        # Split the extension from the filename
        ext = filename.rsplit(".", 1)[1]
        # Check if the extension is in ALLOWED_IMAGE_EXTENSIONS
        if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
            return True
        else:
            return False
    except IndexError:
        # Extension was not provided
        return False

def allowed_image_filesize(app, filesize):
    return int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]