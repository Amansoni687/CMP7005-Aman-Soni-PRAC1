import streamlit as st
import os
from PIL import Image

# Function to display images from a folder along with descriptions
def display_images_from_folder(folder_path, descriptions):
    # List all images (PNG format in your case)
    images = [f for f in os.listdir(folder_path) if f.endswith(('.png'))]
    
    for image_name in images:
        # Open and display the image
        image_path = os.path.join(folder_path, image_name)
        img = Image.open(image_path)

        # Display image with heading
        st.subheader(f"{image_name.split('.')[0].replace('_', ' ').title()}")
        st.image(img, caption=image_name, use_container_width=True)  # Display the image in original size (no resizing)

        # Display the corresponding description
        description = descriptions.get(image_name, "No description available.")
        st.write(description)  # Display a description after each image

# Set up the Streamlit app layout
st.set_page_config(page_title="Air Quality Analysis Project", layout="wide")

# Create a sidebar for page navigation
page = st.sidebar.radio("Select Page", ["Introduction", "Task 1", "Task 2", "Task 3"])

# Introduction Page - Display Title and Project Introduction
if page == "Introduction":
    st.title("Project Title: Beijing Air Quality Analysis")

    # Student details
    st.subheader("Student Information:")
    st.write("""
        **Aman Soni**  
        **Student ID**: st20312962  
        **Cardiff Metropolitan University**  
        **Module Code**: CMP7005  
        **Module Title**: Programming for Data Analysis
    """)

    # Project Introduction
    st.subheader("Project Introduction:")
    st.write("""
    This project involves analyzing the Beijing Multi-Site Air Quality dataset and developing solutions to a real-world problem using programming-driven analytical techniques. The dataset contains hourly air pollutants data from 12 nationally controlled air-quality monitoring sites in Beijing, along with corresponding meteorological data. The task includes:

    - Data handling and preprocessing
    - Exploratory data analysis (EDA)
    - Model building and prediction
    - Development of a multipage application with a Graphical User Interface (GUI)

    The goal is to implement data analysis, model-building, and visualization techniques while also demonstrating the ability to develop a functional application.
    """)

# Task 1 - Display Task 1 images and explanations
elif page == "Task 1":
    st.header("Task 1: Data Handling Results")

    # Explanation of Task 1 dataset head before preprocessing
    st.write("""
    The image below shows the 'merged dataset head' that includes the first few records of the dataset after merging multiple data sources. 
    This is the dataset **before any preprocessing** is applied. Preprocessing steps such as handling missing values, feature scaling, and encoding variables are to be performed in later stages.
    """)

    # Display Task 1 images
    description_1 = "This image presents the 'merged dataset head', showing the first few records of the dataset after merging."
    display_images_from_folder("Task 1", {'merged dataset head.png': description_1})

# Task 2 - Display Task 2 images and explanations in a row (no repetition)
elif page == "Task 2":
    st.header("Task 2: Exploratory Data Analysis (EDA) Results")

    # Descriptions for each image in Task 2
    descriptions = {
        'boxplot.png': "The 'boxplot' image shows the distribution of PM2.5 levels by station. It helps visualize the spread and detect any outliers in the data.",
        'dataset information.png': "The 'dataset information' image provides an overview of the dataset, including the number of rows, columns, and data types for each feature.",
        'heatmap.png': "The 'heatmap' represents the correlation between different features in the dataset, helping to identify relationships between variables.",
        'histogram.png': "This 'histogram' shows the distribution of one feature (PM2.5) across all records in the dataset, providing insight into its frequency distribution.",
        'pairplot.png': "The 'pairplot' shows pairwise relationships between features, useful for identifying trends and potential correlations between them.",
        'statistics summary 1.png': "This 'statistics summary' image presents the basic statistical analysis of the dataset, including count, mean, std, min, and max for each feature.",
        'statistics summary 2.png': "This 'statistics summary' image shows additional percentile and range information for the dataset features."
    }

    # Display images one at a time, ensuring no repetition
    display_images_from_folder("Task 2", descriptions)

# Task 3 - Display Task 3 images and results (no repetition)
elif page == "Task 3":
    st.header("Task 3: Model Building Results")

    # Descriptions for Task 3 images
    descriptions_task3 = {
        'actual vs predicted.png': "The 'Actual vs Predicted' plot shows the comparison between the actual and predicted PM2.5 values from the initial model.",
        'residual distribution.png': "The 'Residual Distribution' plot shows the distribution of residuals from the initial model, which helps to assess model errors.",
        'tuned actual vs predicted.png': "The 'Tuned Actual vs Predicted' plot shows the results of the model after hyperparameter tuning with GridSearchCV."
    }

    # Display Task 3 images once
    display_images_from_folder("Task 3", descriptions_task3)

    # Evaluation Results Section
    st.write("### Model Evaluation (Initial Model) ###")
    st.write("""
        **R² Score**: 0.9324  
        **MAE (Mean Absolute Error)**: 10.84  
        **MSE (Mean Squared Error)**: 301.81  
        **RMSE (Root Mean Squared Error)**: 17.37
    """)

    st.write("### Cross-validation Scores (5-Fold) ###")
    st.write("""
        **R² Scores**: [0.92394325 0.92745426 0.92542702 0.90776381 0.90894051]  
        **Mean R²**: 0.9187057705113373
    """)

    st.write("### Hyperparameter Tuning with GridSearchCV ###")
    st.write("""
        **Best Parameters**:  
        {'regressor__max_depth': None, 'regressor__min_samples_split': 2, 'regressor__n_estimators': 200}
    """)

    st.write("### Evaluation of Tuned Model ###")
    st.write("""
        **R² Score**: 0.9328  
        **MAE (Mean Absolute Error)**: 10.81  
        **MSE (Mean Squared Error)**: 299.76  
        **RMSE (Root Mean Squared Error)**: 17.31
    """)

    # Additional Explanation
    st.write("""
    **Explanation of Results:**
    - The **R² Score** indicates how well the model is performing, with values closer to 1 being better. The model is performing well with an R² score of 0.9324 for the initial model, and 0.9328 after tuning.
    - **MAE** and **RMSE** are the errors the model makes. Lower values are preferred. After tuning, the MAE and RMSE slightly improved, showing better performance.
    - The **Cross-validation scores** show the model's consistency across different folds in the dataset. The average R² score across the 5 folds is 0.9187, showing that the model is generalizing well.
    - **Hyperparameter tuning** using GridSearchCV found the best parameters for the model, optimizing its performance.
    """)
