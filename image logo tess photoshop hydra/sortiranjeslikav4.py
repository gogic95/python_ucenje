#  Copyright (c) Filip Gogic 2022.

import pathlib
import shutil
from PIL import Image
import os
import win32com.client
import cekiranjeprostorav2
import ubacivanjelogotipav2


def sortiranjeSlika(src_directory, photoshop_enabled, template_path):
    dest_directory_non_square = os.path.join(src_directory, 'Non Squares')
    dest_directory_all_done = os.path.join(src_directory, 'All Done')
    dest_directory_bad_square = os.path.join(src_directory, 'Bad Squares')

    resize_to = (1000, 1000)

    for path in pathlib.Path(src_directory).iterdir():
        if path.is_file() and path.name.endswith('.png') or path.name.endswith('.jpg') or path.name.endswith('.jpeg'):
            image = Image.open(path)
            width, height = image.size

            if width == height:
                if width != 1000:
                    image = image.resize(resize_to)
                    # image.save(path)

                check_for_text = cekiranjeprostorav2.cekiranje(image)
                # image.close()
                if check_for_text:
                    try:
                        os.makedirs(dest_directory_bad_square)  # create destination directory
                    except OSError:
                        # The directory already existed, nothing to do
                        pass
                    image.save(dest_directory_bad_square+'\\'+path.name, quality=95)

                else:
                    try:
                        os.makedirs(dest_directory_all_done)  # create destination directory
                    except OSError:
                        # The directory already existed, nothing to do
                        pass
                    image_with_logo = ubacivanjelogotipav2.ubacivanje(image, template_path)
                    image_with_logo.save(dest_directory_all_done+'\\'+path.name, quality=95)
                image.close()

            else:
                image.close()
                try:
                    os.makedirs(dest_directory_non_square)  # create destination directory
                except OSError:
                    # The directory already existed, nothing to do
                    pass
                shutil.copy(path, dest_directory_non_square)

    if photoshop_enabled == 1 and os.path.isdir(dest_directory_non_square):
        for path in pathlib.Path(dest_directory_non_square).iterdir():
            if path.name.endswith('.png') or path.name.endswith('.jpg') or path.name.endswith('.jpeg'):
                win32com.client.Dispatch("Photoshop.Application").Open(path)
