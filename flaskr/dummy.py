from flask import Blueprint, Response, request, jsonify
from flask import current_app as app
from werkzeug.utils import secure_filename
from PIL import Image
from math import floor
from datetime import datetime

import random
import numpy
import os


dummy_backend = Blueprint('dummy', __name__, url_prefix='/dummy')

UPLOAD_FOLDER = os.path.abspath('upload')
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}
TYPES = ['bird', 'tree', 'building', 'flower']


@dummy_backend.route('fetch', methods=['GET', 'POST'])
def dummy_fetch():
    if request.method != 'POST':
        return Response('Welcome to the dummy backend')
    else:
        image = request.files['image']
        image_save_name = secure_filename(
            str(datetime.now().strftime('%Y%m%d%H%M%S%f')) + '_' + image.filename)
        image.save(os.path.join(UPLOAD_FOLDER, image_save_name))

        # image processing (sample)
        file_path = os.path.join(UPLOAD_FOLDER, image_save_name)
        _, ext = os.path.splitext(file_path)
        ext = ext[1:]
        with Image.open(file_path) as im:
            width, height = im.size
            meta = dict(
                height=height,
                width=width,
                mode=im.mode,
                ext=ext,
            )
            image_array = numpy.array(im)

        refresh_upload_folder()

        return jsonify(
            dict(
                meta=meta,
                types=[random.choice(TYPES) for _ in range(2)],
                anchors=generate_anchors(width=width, height=height, n=2)
            )
        )


def generate_anchors(width, height, n=2):
    anchors = []
    for _ in range(n):
        x_1 = int(floor(random.random() * width))
        y_1 = int(floor(random.random() * height))
        x_2 = int(floor(random.random() * width))
        y_2 = int(floor(random.random() * height))
        anchors.append([dict(width=x_1, height=y_1),
                       dict(width=x_2, height=y_2)])
    return anchors


def refresh_upload_folder(limit=20):
    files_to_delete = sorted(os.listdir(UPLOAD_FOLDER), reverse=True)[limit:]
    for file_name in files_to_delete:
        file_path = os.path.join(UPLOAD_FOLDER, file_name)
        os.remove(file_path)
        app.logger.info(f'old file {file_name} removed')
