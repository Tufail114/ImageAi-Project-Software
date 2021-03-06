from imageai.Classification import ImageClassification
import os
import cv2
import pytest
from os.path import dirname

main_folder = os.getcwd()


def test_recognition_model_mobilenetv2(): #detecting model


    predictor = ImageClassification()
    predictor.setModelTypeAsMobileNetV2()
    predictor.setModelPath(os.path.join(main_folder, "data-models", "mobilenet_v2.h5"))
    predictor.loadModel()
    predictions, probabilities = predictor.classifyImage(image_input=os.path.join(main_folder, main_folder, "data-images", "1.jpg"))

    assert isinstance(predictions, list)
    assert isinstance(probabilities, list)
    assert isinstance(predictions[0], str)
    assert isinstance(probabilities[0], float)


def test_recognition_model_resnet():  #clearify model

    predictor = ImageClassification()
    predictor.setModelTypeAsResNet50()
    predictor.setModelPath(os.path.join(main_folder, "data-models", "resnet50_imagenet_tf.2.0.h5"))
    predictor.loadModel()
    predictions, probabilities = predictor.classifyImage(image_input=os.path.join(main_folder, main_folder, "data-images", "1.jpg"))

    assert isinstance(predictions, list)
    assert isinstance(probabilities, list)
    assert isinstance(predictions[0], str)
    assert isinstance(probabilities[0], float)


def test_recognition_model_inceptionv3(): #another model

    predictor = ImageClassification()
    predictor.setModelTypeAsInceptionV3()
    predictor.setModelPath(os.path.join(main_folder, "data-models", "inception_v3_weights_tf_dim_ordering_tf_kernels.h5"))
    predictor.loadModel()
    predictions, probabilities = predictor.classifyImage(image_input=os.path.join(main_folder, main_folder, "data-images", "1.jpg"))

    assert isinstance(predictions, list)
    assert isinstance(probabilities, list)
    assert isinstance(predictions[0], str)
    assert isinstance(probabilities[0], float)


def test_recognition_model_densenet():

    predictor = ImageClassification()
    predictor.setModelTypeAsDenseNet121()
    predictor.setModelPath(os.path.join(main_folder, "data-models", "DenseNet-BC-121-32.h5"))
    predictor.loadModel()
    predictions, probabilities = predictor.classifyImage(image_input=os.path.join(main_folder, main_folder, "data-images", "1.jpg"))

    assert isinstance(predictions, list)
    assert isinstance(probabilities, list)
    assert isinstance(predictions[0], str)
    assert isinstance(probabilities[0], float)



def test_recognition_model_resnet_array_input():

    predictor = ImageClassification()
    predictor.setModelTypeAsResNet50()
    predictor.setModelPath(os.path.join(main_folder, "data-models", "resnet50_imagenet_tf.2.0.h5"))
    predictor.loadModel()
    image_array = cv2.imread(os.path.join(main_folder, main_folder, "data-images", "1.jpg"))
    predictions, probabilities = predictor.classifyImage(image_input=image_array, input_type="array")

    assert isinstance(predictions, list)
    assert isinstance(probabilities, list)
    assert isinstance(predictions[0], str)
    assert isinstance(probabilities[0], float)


def test_recognition_model_inceptionv3_array_input():

    predictor = ImageClassification()
    predictor.setModelTypeAsInceptionV3()
    predictor.setModelPath(os.path.join(main_folder, "data-models", "inception_v3_weights_tf_dim_ordering_tf_kernels.h5"))
    predictor.loadModel()
    image_array = cv2.imread(os.path.join(main_folder, main_folder, "data-images", "1.jpg"))
    predictions, probabilities = predictor.classifyImage(image_input=image_array, input_type="array")

    assert isinstance(predictions, list)
    assert isinstance(probabilities, list)
    assert isinstance(predictions[0], str)
    assert isinstance(probabilities[0], float)


def test_recognition_model_densenet_array_input():  #arrays input

    predictor = ImageClassification()
    predictor.setModelTypeAsDenseNet121()
    predictor.setModelPath(os.path.join(main_folder, "data-models", "DenseNet-BC-121-32.h5"))
    predictor.loadModel()
    image_array = cv2.imread(os.path.join(main_folder, main_folder, "data-images", "1.jpg"))
    predictions, probabilities = predictor.classifyImage(image_input=image_array, input_type="array")

    assert isinstance(predictions, list)
    assert isinstance(probabilities, list)
    assert isinstance(predictions[0], str)
    assert isinstance(probabilities[0], float)

