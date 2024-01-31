import os

def rename_files (position, extension):

    count = 1
    for filename in os.listdir(position):
        if filename.endswith(extension):
            new_filename = str(count).zfill(3) + extension
            old_path = os.path.join(position, filename)
            new_path = os.path.join(position, new_filename)
            os.rename(old_path, new_path)
            count += 1

position = "D:\Job-04---Batch-Rename"  # ตำแหน่งของ folder ที่เราต้องการจะเปลี่ยนชื่อ
extension = ".jpg"  # ตั้ง file name extension ของ file ที่ต้องการจะเปลี่ยนชื่อ
rename_files(position, extension)
