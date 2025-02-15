# Crack Detection
## **Overview**
This project leverages **machine learning and computer vision** techniques to detect structural cracks in telecom tower infrastructure. Using a **Convolutional Neural Network (CNN)**, the model achieves **99% accuracy** in classifying images as "cracked" or "uncracked." A **Django-based web interface** has been developed to allow users to upload images and receive real-time classifications.

## **Features**
- ✅ **Deep Learning-Based Crack Detection** – Trained on a diverse dataset with CNNs  
- ✅ **High Accuracy (99%)** – Effective in identifying cracks under various conditions  
- ✅ **Django Web Interface** – Users can upload images for real-time classification  
- ✅ **Data Preprocessing & Augmentation** – Improved model performance through transformations  
- ✅ **Scalable Deployment** – Can be integrated into cloud-based monitoring systems  

## **Tech Stack**
- **Machine Learning:** TensorFlow/Keras, OpenCV, NumPy  
- **Web Framework:** Django  
- **Frontend:** HTML, CSS, Bootstrap 

## **Installation**

### **1. Clone the Repository**
```sh
git clone https://github.com/your-username/crack-detection
cd crack-detection
```

### **2. Update path for Dataset**
You can carry out this step in case you want to train a model using your own dataset.

In the [FP.ipynb](FP.ipynb) file, update cell 2 with your dataset path. 

To train this model, I have used an open-source dataset from Kaggle: [View the dataset](https://www.kaggle.com/datasets/arunrk7/surface-crack-detection)

In case you **do not want to** train the model, or have a trained model.h5 file, skip to cell 54. Load the model, and carry out the inference as you wish.

### **3. Install pre-requisites**
Run the following command in the project directory
```sh
pip install -r requirements.txt
```

### **4. Run the Django server**
Start the Django server using this command
```sh
python manage.py runserver
```
The app should now be running at http://127.0.0.1:8000



## Usage
**1. Open web interface**

**2. Upload as many images as you want to classify**

**3. Click "Predict" and after some time, the images will show up in a carousel of "Cracked" or "Uncracked" (performance and accuracy may vary)**

## Model Performance
The trained CNN model achieved:

- **Accuracy**: 98%
- **Precision**: 97%
- **Recall**: 97%
- **F1-Score**: 99%

Data augmentation techniques such as **rotation**, **flipping**, **zooming**, and **shifting** were used to handle dataset imbalances and improve model generalization.

## Challenges Faced & Solutions
### **1. Class Imbalance**
- **Issue**: Fewer images of cracked structures compared to uncracked ones.
- **Solution**: Applied data augmentation to generate more variations of cracked images.
  
### **2. Noisy Data**
- **Issue**: Shadows, reflections, and environmental noise affected model predictions.
- **Solution**: Used image preprocessing techniques like Gaussian blurring and adaptive thresholding.


## Future Scope
- 🚀 **Enhancing Model Robustness** – Incorporate more diverse datasets for better generalization.
- 🌐 **Real-Time Monitoring** – Deploy the model on edge devices for real-time infrastructure monitoring.
- 📊 **Multi-Class Classification** – Extend the system to detect corrosion, misalignments, and other defects.
- ☁ **Cloud Integration** – Deploy the system on AWS/GCP for large-scale automated inspections.

## License
This project is licensed under the **MIT License** - feel free to use, modify and distribute it

## Contact
For any queries, reach out via:
- 🐦 **Twitter**: @[nottanjune](https://x.com/nottanjune)
- 🔗 **LinkedIn**: [Tanmay Nargas](https://www.linkedin.com/in/tanmay-nargas-63b723147/)

