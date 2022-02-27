from azure.cognitiveservices.vision.computervision import ComputerVisionClient

# from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
# from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from dotenv import load_dotenv

# from array import array
import os

# from PIL import Image
# import sys
# import time

load_dotenv()

subscription_key = os.getenv("COGNITIVE_SERVICE_KEY")
endpoint = os.getenv("COGNITIVE_SERVICE_ENDPOINT")

computervision_client = ComputerVisionClient(
    endpoint, CognitiveServicesCredentials(subscription_key)
)

# remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"
# remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/celebrities.jpg"


def describe_image():
    """
    Describe an Image - remote
    This example describes the contents of an image with the confidence score.
    """
    print("===== Describe an image - remote =====")
    remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"
    # Call API
    description_results = computervision_client.describe_image(remote_image_url)

    # Get the captions (descriptions) from the response, with confidence level
    print("Description of remote image: ")
    if len(description_results.captions) == 0:
        print("No description detected.")
    else:
        for caption in description_results.captions:
            print(
                "'{}' with confidence {:.2f}%".format(
                    caption.text, caption.confidence * 100
                )
            )


def get_image_categorize():
    """
    Categorize an Image - remote
    This example extracts (general) categories from a remote image with a confidence score.
    """
    print("===== Categorize an image - remote =====")
    remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"
    # Select the visual feature(s) you want.
    remote_image_features = ["categories"]
    # Call API with URL and features
    categorize_results_remote = computervision_client.analyze_image(
        remote_image_url, remote_image_features
    )

    # Print results with confidence score
    print("Categories from remote image: ")
    if len(categorize_results_remote.categories) == 0:
        print("No categories detected.")
    else:
        for category in categorize_results_remote.categories:
            print(
                "'{}' with confidence {:.2f}%".format(
                    category.name, category.score * 100
                )
            )


def get_image_tags():
    """
    Tag an Image - remote
    This example returns a tag (key word) for each thing in the image.
    """
    print("===== Tag an image - remote =====")
    remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"
    # Call API with remote image
    tags_result_remote = computervision_client.tag_image(remote_image_url)

    # Print results with confidence score
    print("Tags in the remote image: ")
    if len(tags_result_remote.tags) == 0:
        print("No tags detected.")
    else:
        for tag in tags_result_remote.tags:
            print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))


def find_faces():
    """
    Detect Domain-specific Content - remote
    This example detects celebrites and landmarks in remote images.
    """
    print("===== Detect Domain-specific Content - remote =====")
    # URL of one or more celebrities
    remote_image_url_celebs = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/celebrities.jpg"
    # Call API with content type (celebrities) and URL
    detect_domain_results_celebs_remote = computervision_client.analyze_image_by_domain(
        "celebrities", remote_image_url_celebs
    )

    # Print detection results with name
    print("Celebrities in the remote image:")
    if len(detect_domain_results_celebs_remote.result["celebrities"]) == 0:
        print("No celebrities detected.")
    else:
        for celeb in detect_domain_results_celebs_remote.result["celebrities"]:
            print(celeb["name"])


def get_user_choice():
    computer_vision_example_list = [
        "find_faces",
        "get_image_tags",
        "describe_image",
        "get_image_categorize",
    ]
    print("/n/n/nChoose from the below")
    for index, item in enumerate(computer_vision_example_list, start=1):
        print(f"{index} - {item}")

    user_input = int(input("\n\nEnter your choice (int): "))

    if user_input not in list(range(len(computer_vision_example_list))):
        exit("Choose from the provided list")

    func_name = computer_vision_example_list[user_input - 1]

    # get the function object from the global
    callable_func_name = globals()[func_name]

    # call teh desired function
    callable_func_name()


get_user_choice()

print("\n\n\n\n")
