import cv2
import numpy as np
import matplotlib.pyplot as plt
from mrcnn.config import Config
from mrcnn.model import MaskRCNN
from mrcnn.visualize import display_instances

# Configurations pour Mask R-CNN
class InferenceConfig(Config):
    NAME = "coco_inference"
    NUM_CLASSES = 1 + 80  # COCO contient 80 classes d'objets
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

# Charger le modèle pré-entraîné
config = InferenceConfig()
model = MaskRCNN(mode="inference", model_dir="./", config=config)

# Manually download or place the weights in your working directory
model.load_weights("mask_rcnn_coco.h5", by_name=True)

# Classes d'objets (COCO)
class_names = ["BG", "person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat", "traffic light",
               "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow", "elephant",
               "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard",
               "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle",
               "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
               "carrot", "hot dog", "pizza", "donut", "cake", "chair", "couch", "potted plant", "bed", "dining table",
               "toilet", "tv", "laptop", "mouse", "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink",
               "refrigerator", "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"]

# Charger l'image
def load_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

# Fonction principale
def remove_object(image_path):
    image = load_image(image_path)

    # Exécuter la détection d'objets
    results = model.detect([image], verbose=1)
    r = results[0]

    # Afficher les objets détectés
    display_instances(image, r['rois'], r['masks'], r['class_ids'], class_names, r['scores'])

    # Vérifier si des pommes ont été détectées
    apple_indices = [i for i, cls_id in enumerate(r['class_ids']) if class_names[cls_id] == "apple"]
    if not apple_indices:
        print("Aucune pomme détectée dans l'image.")
        return

    # Créer une copie de l'image pour l'affichage après suppression
    image_copy = image.copy()

    # Supprimer les pommes détectées
    for selected_object in apple_indices:
        mask = r['masks'][:, :, selected_object]

        # Remplissage de la région masquée avec OpenCV (inpainting)
        mask = (mask * 255).astype(np.uint8)
        inpainted_image = cv2.inpaint(image_copy, mask, inpaintRadius=7, flags=cv2.INPAINT_TELEA)

        # Afficher l'image avant et après la suppression
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.title("Image Originale")
        plt.imshow(image)
        plt.axis("off")

        plt.subplot(1, 2, 2)
        plt.title("Image Après Suppression des Pommes")
        plt.imshow(inpainted_image)
        plt.axis("off")
        plt.show()

# Appeler la fonction
image_path = "tofa7a.jpeg"  # Remplacez par le chemin de votre image
remove_object(image_path)
