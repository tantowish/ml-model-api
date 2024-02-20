from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

def classify(image_path):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model(r"./model/keras_Model.h5", compile=False)

    # Load the labels
    class_names = open(r"./model/labels.txt", "r").readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open(f"./static/img/{image_path}").convert("RGB")

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    elaboration = [
        "Tooth decay resulting in cavities, treated with dental fillings or crowns to restore tooth structure and prevent further damage. Regular dental check-ups are essential for early detection and intervention. Prevention includes maintaining good oral hygiene, limiting sugary foods, and applying fluoride treatments.",
        "Digital communication about tooth decay, managed with dental education, promotion of oral hygiene practices, and the recommendation of fluoride products to prevent cavities. Emphasizing regular dental visits and proper home care can help address potential oral health issues before they lead to cavities.",
        "Enjoy optimal dental health by maintaining diligent oral hygiene practices such as brushing with fluoride toothpaste, flossing, and using mouthwash. Regular dental cleanings and check-ups every six months ensure that your teeth stay strong and cavity-free. Embrace a balanced diet and limit sugary snacks to promote overall wellness and a radiant smile.",
        "Tooth wear addressed through lifestyle modifications like avoiding hard foods and abrasive toothbrushes. Dental interventions such as mouthguards may be recommended for those with bruxism (teeth grinding). Fluoride treatments can strengthen enamel against erosion. Regular dental visits allow for monitoring and early intervention to prevent further wear.",
        "Managed through professional dental cleanings to remove tartar and plaque buildup, along with polishing to reduce surface stains. Teeth whitening treatments may be offered for discoloration caused by food, beverages, or smoking, enhancing the appearance of the smile. Good oral hygiene practices, including brushing twice a day and flossing daily, can help prevent tartar and plaque buildup."
    ]

    result = {
        'classification': class_name[2:].replace('\n', ''),
        'elaboration': elaboration[index],
        'confident_score': confidence_score,
        'image_path':image_path
    }
    return result