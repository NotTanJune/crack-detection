from django.shortcuts import render,redirect
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
# Create your views here.


def index(request):
        return render(request, 'index.html')

def results(request):
    model = load_model('Crack-Detection/model.h5')
    if request.method == 'POST' and 'images' in request.FILES:
        uploaded_images = request.FILES.getlist('images')
        results = []
        for uploaded_image in uploaded_images:
            if uploaded_image is not None:
                img = Image.open(uploaded_image)
                img = img.convert('RGB')
                img = img.resize((227, 227))
                img_array = np.array(img)
                reshaped_img = img_array.reshape(1, 227, 227, 3)
                result = {
                     'image_url' : get_image_url(uploaded_image),
                     'confidence': model.predict(reshaped_img)
                }
                results.append(result)
                context = {'results': results}
        return render(request, 'results.html', context)
    return render(request, 'results.html')

def get_image_url(uploaded_image):
    # Generate a URL for the uploaded image
    # This assumes you have a 'media' directory in your project's root directory
    image_url = 'media/uploads/' + uploaded_image.name
    return image_url
