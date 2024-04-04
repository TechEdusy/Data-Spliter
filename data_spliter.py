import os
import shutil
import threading
import sys  # Import sys module
from sklearn.model_selection import train_test_split

# Define paths
original_data_dir = 'data'
base_dir = 'splited_datasets'

def input_with_timeout(prompt, timeout=30):
    print(prompt)
    input_result = [None]

    def wait_for_input():
        try:
            input_result[0] = input()
        except EOFError:
            pass

    input_thread = threading.Thread(target=wait_for_input)
    input_thread.start()

    input_thread.join(timeout)
    if input_result[0] is None:
        print("\nNo response received within 30 seconds. Proceeding with dataset creation with a warning.")
    return input_result[0]

def check_samples():
    low_sample_classes = []
    for class_name in ['Good', 'Bad']:
        class_dir = os.path.join(original_data_dir, class_name)
        if len(os.listdir(class_dir)) < 10:
            low_sample_classes.append(class_name)
    return low_sample_classes

def confirm_proceeding(low_sample_classes):
    if low_sample_classes:
        class_list = ", ".join(low_sample_classes)
        message = f"The following classes have low sample counts: {class_list}. Proceed with dataset creation? (y/n): "
        response = input_with_timeout(message)
        if response and response.lower() in ['n', 'no']:
            print("User opted to halt the process due to insufficient samples in the following classes: " + class_list)
            sys.exit()  # Stop execution if user decides not to proceed
    return True

def create_directories_and_process():
    create_directories()
    for class_name in ['Good', 'Bad']:
        process_class(class_name)
    print("Dataset segregation complete.")

def create_directories():
    for category in ['train', 'val', 'test']:
        os.makedirs(os.path.join(base_dir, category, 'Good'), exist_ok=True)
        os.makedirs(os.path.join(base_dir, category, 'Bad'), exist_ok=True)

def process_class(class_name):
    source_dir = os.path.join(original_data_dir, class_name)
    files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]

    train_files, test_files = train_test_split(files, test_size=0.3, random_state=42)
    val_files, test_files = train_test_split(test_files, test_size=0.5, random_state=42)

    destinations = {
        'train': os.path.join(base_dir, 'train', class_name),
        'val': os.path.join(base_dir, 'val', class_name),
        'test': os.path.join(base_dir, 'test', class_name),
    }

    for file_list, destination in zip([train_files, val_files, test_files], destinations.values()):
        for file in file_list:
            shutil.copy(os.path.join(source_dir, file), destination)

if __name__ == "__main__":
    low_sample_classes = check_samples()
    if confirm_proceeding(low_sample_classes):
        os.makedirs(base_dir, exist_ok=True)
        create_directories_and_process()
    else:
        print("Process halted by user.")
    sys.exit()  # Ensure the script exits after completion
