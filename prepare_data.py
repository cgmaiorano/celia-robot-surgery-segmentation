"""
This code has been edited to run for the right frames and my labels that were created in hwk2pt1. Prior to editing the code was not changed from the 
original ternaus prepare_data. 
[1] Merge masks with different instruments into one binary mask
[2] Crop black borders from images and masks
"""
from pathlib import Path

from tqdm import tqdm
import cv2
import numpy as np

data_path = Path('../Dataset/')

train_path = data_path / 'instrument_1_4_training'
right_path = Path('../right_label')
cropped_train_path = data_path / 'cropped_train'

original_height, original_width = 1080, 1920
height, width = 1024, 1280
h_start, w_start = 28, 320

binary_factor = 255
parts_factor = 85
instrument_factor = 32


if __name__ == '__main__':
    for instrument_index in range(1, 5):
        instrument_folder = 'instrument_dataset_' + str(instrument_index)
        right_folder = 'right_label_' + str(instrument_index)
        (cropped_train_path / instrument_folder / 'images').mkdir(exist_ok=True, parents=True)

        binary_mask_folder = (cropped_train_path / instrument_folder / 'binary_masks')
        binary_mask_folder.mkdir(exist_ok=True, parents=True)

#         mask_folders = list((right_path / right_folder).glob('*'))
        # mask_folders = [x for x in mask_folders if 'Other' not in str(mask_folders)]

        for file_name in tqdm(list((train_path / instrument_folder / 'right_frames').glob('*'))):
            img = cv2.imread(str(file_name))
            old_h, old_w, _ = img.shape

            img = img[h_start: h_start + height, w_start: w_start + width]
            cv2.imwrite(str(cropped_train_path / instrument_folder / 'images' / (file_name.stem + '.jpg')), img,
                        [cv2.IMWRITE_JPEG_QUALITY, 100])

#             mask_binary = np.zeros((old_h, old_w))
#             mask_parts = np.zeros((old_h, old_w))
#             mask_instruments = np.zeros((old_h, old_w))

            for file_name in (list((right_path / right_folder).glob('*'))):
                mask_binary = cv2.imread(str(file_name))
                old_h, old_w, _ = mask_binary.shape
                
                mask_binary = (mask_binary[h_start: h_start + height, w_start: w_start + width] > 0).astype(
                np.uint8) * binary_factor
                cv2.imwrite(str(binary_mask_folder / (file_name.stem + '.jpg')), mask_binary)

#                 if 'Bipolar_Forceps' in str(mask_folder):
#                     mask_instruments[mask > 0] = 1
#                 elif 'Prograsp_Forceps' in str(mask_folder):
#                     mask_instruments[mask > 0] = 2
#                 elif 'Large_Needle_Driver' in str(mask_folder):
#                     mask_instruments[mask > 0] = 3
#                 elif 'Vessel_Sealer' in str(mask_folder):
#                     mask_instruments[mask > 0] = 4
#                 elif 'Grasping_Retractor' in str(mask_folder):
#                     mask_instruments[mask > 0] = 5
#                 elif 'Monopolar_Curved_Scissors' in str(mask_folder):
#                     mask_instruments[mask > 0] = 6
#                 elif 'Other' in str(mask_folder):
#                     mask_instruments[mask > 0] = 7

#                 if 'Other' not in str(mask_folder):
#                     mask_binary += mask

#                     mask_parts[mask == 10] = 1  # Shaft
#                     mask_parts[mask == 20] = 2  # Wrist
#                     mask_parts[mask == 30] = 3  # Claspers

#             mask_binary = (mask_binary[h_start: h_start + height, w_start: w_start + width] > 0).astype(
#                 np.uint8) * binary_factor
#             mask_parts = (mask_parts[h_start: h_start + height, w_start: w_start + width]).astype(
#                 np.uint8) * parts_factor
#             mask_instruments = (mask_instruments[h_start: h_start + height, w_start: w_start + width]).astype(
#                 np.uint8) * instrument_factor

#             cv2.imwrite(str(binary_mask_folder / file_name.name), mask_binary)
#             cv2.imwrite(str(parts_mask_folder / file_name.name), mask_parts)
#             cv2.imwrite(str(instrument_mask_folder / file_name.name), mask_instruments)
