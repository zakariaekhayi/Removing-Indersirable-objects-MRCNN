

---

# Removing-Undesirable-Objects-MRCNN

This project aims to remove undesirable objects from an image. It allows users to select an object in a photo and automatically remove it using advanced techniques such as instance segmentation (**Mask R-CNN**) and inpainting-based filling.

---

## Description

The project uses **Mask R-CNN** to detect and segment objects in an image. Once an object is selected, it is automatically removed and the empty region is filled using inpainting.

### Techniques Used:

- **Instance Segmentation (Mask R-CNN)**
- **Inpainting** to fill the removed areas.

---

## Prerequisites

1. **Python 3.7**: Ensure this version is installed.
2. **Git**: To download the required files.
3. **Mask R-CNN Repository**: The project depends on the Mask R-CNN library available on GitHub.

---

## Installation and Execution Instructions

### 1. Clone and Set Up the Mask R-CNN Repository

- Download the **Mask R-CNN** repository from the following link:
  [https://github.com/matterport/Mask\_RCNN.git](https://github.com/matterport/Mask_RCNN.git)

- Extract the contents of the repository and place it **in the same location** as your project's `rcnn.py` file.

### 2. Download the Pre-trained COCO Model

- Download the **mask\_rcnn\_coco.h5** file from the following link:
  [https://github.com/matterport/Mask\_RCNN/releases](https://github.com/matterport/Mask_RCNN/releases)

- Place the **mask\_rcnn\_coco.h5** file in the project folder.

### 3. Install Python 3.7 and Set Up a Virtual Environment

1. **Install Python 3.7**: Download and install Python 3.7 from the official website.

   - Make sure to add Python to the PATH during installation.

2. **Create a Virtual Environment**:

   - Open PowerShell or CMD.
   - Run the following commands:
     ```bash
     python -m venv myenv
     ```

3. **Configure Execution Permissions on Windows**:

   - In PowerShell, type:
     ```bash
     Get-ExecutionPolicy
     Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
     ```
   - Choose **"Yes to All"** if prompted.

4. **Activate the Virtual Environment**:

   - Run the following command:
     ```bash
     .\myenv\Scripts\Activate
     ```
   - Once activated, your terminal should display something like:
     ```bash
     (myenv)
     ```

### 4. Install Dependencies

- Once the environment is activated, install the required dependencies either from a `requirements.txt` file or manually:
  ```bash
  pip install tensorflow keras opencv-python numpy matplotlib
  ```

### 5. Run the Project

- Run the main script `rcnn.py`, ensuring you are in the virtual environment.
- ![WhatsApp Image 2024-12-17 at 14 29 10_e63babfa](https://github.com/user-attachments/assets/47639c2a-1da7-410a-8e4a-9c2eb04758e2)

  ```bash
  python rcnn.py
  ```

---

## Important Notes

- Ensure that the **Mask R-CNN** repository and the **mask\_rcnn\_coco.h5** file are correctly placed.
- The `rcnn.py` file heavily depends on the Mask R-CNN files to function properly.
- The project should be run in a Python 3.7 environment.

---

## Useful Links

- **Mask R-CNN Repository**: [https://github.com/matterport/Mask\_RCNN](https://github.com/matterport/Mask_RCNN)
- **Pre-trained COCO Model**: [https://github.com/matterport/Mask\_RCNN/releases](https://github.com/matterport/Mask_RCNN/releases)

---

## Contact

For any questions or assistance, feel free to contact me via GitHub or by email.
zakariae.khayi@uit.ac.ma

---

Thank you for using **Removing-Undesirable-Objects-MRCNN**!

---
