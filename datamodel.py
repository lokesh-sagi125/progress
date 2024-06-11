import os
import cv2 as cv
import numpy as np
import xml.etree.ElementTree as ET

image_dir = 'test copy'
annotation_dir = 'test copy'


def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    objects = []
    for obj in root.iter('object'):
        class_name = obj.find('name').text
        bbox = obj.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)
        objects.append((class_name, xmin, ymin, xmax, ymax))
    return objects

def load_images_and_annotations(image_dir, annotation_dir):
    images = []
    annotations = []
    for image_file in os.listdir(image_dir):
        if image_file.endswith('.jpg'):  # Adjust extension if needed
            image_path = os.path.join(image_dir, image_file)
            annotation_file = os.path.join(annotation_dir, image_file.replace('.jpg', '.xml'))
            if os.path.exists(annotation_file):
                image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
                if image is None:
                    print(f"Error: Image {image_file} not found or unable to load.")
                    continue
                objects = parse_xml(annotation_file)
                images.append(image)
                annotations.append(objects)
    return images, annotations

def create_dataset(images, annotations, num_classes=10):
    cells = []
    labels = []
    for image, objects in zip(images, annotations):
        height, width = image.shape
        for obj in objects:
            class_name, xmin, ymin, xmax, ymax = obj
            cell = image[ymin:ymax, xmin:xmax]
            cell = cv.resize(cell, (20, 20))  # Resize to a fixed size if necessary
            cell = cell.flatten()
            cells.append(cell)
            label = int(class_name)  # Assuming class_name can be converted to an integer class label
            labels.append(label)
    
    cells = np.array(cells, dtype=np.float32)
    labels = np.array(labels, dtype=np.float32)
    
    # Split the data into training and testing sets
    training_percentage = 80
    train_size = int(len(cells) * training_percentage / 100)
    test_size = len(cells) - train_size

    train_data = cells[:train_size]
    test_data = cells[train_size:]

    train_labels = labels[:train_size]
    test_labels = labels[train_size:]

    return train_data, test_data, train_labels, test_labels

# Define paths to the image and annotation directories
image_dir = '/Users/lokeshsagi/Downloads/human_detection.v1i.voc/train/images/'  # Adjust this path
annotation_dir = '/Users/lokeshsagi/Downloads/human_detection.v1i.voc/train/annotations/'  # Adjust this path

# Load images and annotations
images, annotations = load_images_and_annotations(image_dir, annotation_dir)

# Create dataset
train_data, test_data, train_labels, test_labels = create_dataset(images, annotations)

# Train the KNN model
knn = cv.ml.KNearest_create()
knn.train(train_data, cv.ml.ROW_SAMPLE, train_labels)

# Test the model
ret, result, neighbors, dist = knn.findNearest(test_data, k=5)

# Calculate the accuracy
matches = result.flatten() == test_labels
correct = np.count_nonzero(matches)
accuracy = correct * 100.0 / result.size

print("Accuracy: {:.2f}%".format(accuracy))
