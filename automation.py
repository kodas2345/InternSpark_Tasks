
import os
import shutil
import logging

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

folder_path = input("Enter folder path: ")

try:
    if not os.path.isdir(folder_path):
        print("Folder does not exist.")
        logging.error("Folder not found: %s", folder_path)
    else:
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)

            if os.path.isfile(file_path):
                extension = os.path.splitext(file)[1][1:] or "others"
                new_folder = os.path.join(folder_path, extension)
                os.makedirs(new_folder, exist_ok=True)

                shutil.move(
                    file_path,
                    os.path.join(new_folder, file)
                )
                logging.info("Organized file: %s", file)

        print("Files organized successfully!")
        logging.info("Organization completed.")

except OSError as error:
    print("Error:", error)
    logging.exception("An error occurred")
