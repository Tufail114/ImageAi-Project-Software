from imageai.Detection.Custom import CustomVideoObjectDetection
import os
from numpy import ndarray
import pytest


#paths
main_folder = os.getcwd()
video_file = os.path.join(main_folder, "data-videos", "holo-micro.mp4")
video_file_output = os.path.join(main_folder, "data-temp", "holo-micro-detected")

model_path = os.path.join(main_folder, "data-models", "hololens-ex-60--loss-2.76.h5")
model_json = os.path.join(main_folder, "data-json", "detection_config.json")

#applying
def test_custom_video_detection_yolov3():


    detector = CustomVideoObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(model_path)
    detector.setJsonPath(model_json)
    detector.loadModel()
    video_path = detector.detectObjectsFromVideo(input_file_path=video_file, output_file_path=video_file_output, save_detected_video=True, frames_per_second=30, log_progress=True)

    assert os.path.exists(video_file_output + ".avi")
    assert isinstance(video_path, str)
    os.remove(video_file_output + ".avi")


#analysis
def test_custom_video_detection_yolov3_analysis():

    detector = CustomVideoObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(model_path)
    detector.setJsonPath(model_json)
    detector.loadModel()
    video_path = detector.detectObjectsFromVideo(input_file_path=video_file, output_file_path=video_file_output, save_detected_video=True, frames_per_second=30, log_progress=True, per_frame_function=forFrame, per_second_function=forSecond, return_detected_frame=True)

    assert os.path.exists(video_file_output + ".avi")
    assert isinstance(video_path, str)
    os.remove(video_file_output + ".avi")


#frame rates
def forFrame(frame_number, output_array, output_count, detected_frame):
    assert isinstance(detected_frame, ndarray)
    assert isinstance(frame_number, int)
    assert isinstance(output_array, list)
    assert isinstance(output_count, dict)


#detection
def forSecond(second_number, output_arrays, count_arrays, average_output_count, detected_frame):
    assert isinstance(detected_frame, ndarray)
    assert isinstance(second_number, int)
    assert isinstance(output_arrays, list)
    assert isinstance(count_arrays, list)

