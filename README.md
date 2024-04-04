
# Dataset Preparation Script

This script is designed to prepare your dataset for machine learning tasks by segregating it into training, validation, and testing sets. It also handles datasets with classes that might have insufficient samples.

## How It Works

The script operates by:
1. Checking each class in your dataset for the number of samples.
2. If any class has fewer than 10 samples, it prompts the user for confirmation to proceed with the dataset preparation.
3. Based on user input, it either proceeds to prepare the dataset or halts the operation.
4. It automatically segregates the dataset into training, validation, and testing directories while preserving class labels.

### Key Components

- **Thread-based Input Timeout**: The script uses a threading mechanism to wait for user input with a timeout. If no input is received within the specified timeout, it proceeds with a warning.
- **Sample Count Check**: Before proceeding, it checks if any class has insufficient samples and informs the user which specific classes are affected.
- **User Confirmation**: It requires user confirmation to proceed with the dataset preparation when low sample counts are detected. The process halts if the user inputs 'no'.
- **Dataset Segregation**: Upon receiving confirmation to proceed, it segregates the dataset into specified directories for training, validation, and testing.

## Usage

To use this script, follow these steps:
1. Ensure you have Python installed on your system.
2. Place your dataset in a known directory, structured with subdirectories for each class.
3. Update the `original_data_dir` variable in the script to point to your dataset's location.
4. Specify the `base_dir` where you want the segregated datasets to be stored.
5. Run the script. It will automatically prompt you if any action is required.
6. Follow the on-screen instructions to proceed with or halt the dataset preparation.

### Example Directory Structure Before Running the Script

```
original_data_dir/
│
├── Class1/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
└── Class2/
    ├── image1.jpg
    ├── image2.jpg
    └── ...
```

### Directory Structure After Running the Script

```
base_dir/
│
├── train/
│   ├── Class1/
│   ├── Class2/
│   └── ...
├── val/
│   ├── Class1/
│   ├── Class2/
│   └── ...
└── test/
    ├── Class1/
    ├── Class2/
    └── ...
```

**Note**: If the script is halted due to insufficient samples and the user's decision not to proceed, no directories or files will be created or modified.

## Requirements

- Python 3.x
- `sklearn` library for `train_test_split` function

## Installation

- Ensure Python and pip are installed.
- Install `sklearn` using pip: `pip install scikit-learn`

## License

This script is provided "as is", without warranty of any kind, express or implied.
