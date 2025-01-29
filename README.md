# 🎬 Movie Recommender System  

## 📌 Overview  
Discover movies like never before! 🎬✨ The **Movie Recommender System** is an intelligent recommendation engine built with **Python** in **Jupyter Notebook**. Using advanced **content-based filtering**, it analyzes movie metadata to suggest **five highly relevant movies** based on your selection. Whether you're exploring classics or the latest hits, this system ensures you always find the perfect watch! 🍿🚀  

## 🚀 Features  
✔️ **Content-Based Filtering** – Uses movie metadata (genres, cast, crew, etc.) for recommendations.  
✔️ **TF-IDF Vectorization** – Processes text data to measure similarity.  
✔️ **Efficient Model Loading** – Saves and loads trained models using **Pickle**.  
✔️ **Fast Recommendations** – Instantly retrieves **top 5 similar movies**.  
✔️ **Customizable** – Modify the dataset or tweak the algorithm for improved accuracy.  

## 📂 Dataset  
The system is built on **5,000 movies' metadata**, including key attributes such as:  
🎭 **Genres** | 🎬 **Cast & Crew** | 📅 **Release Date** | 🏆 **Popularity & Ratings**  

🔗 **Download Dataset:**  
- [TMDB 5000 Movies Dataset](https://drive.google.com/file/d/182mTWOKdg5UM7hx34RutzfWvGfHbomXu/view?usp=sharing)  
- [TMDB 5000 Credits Dataset](https://drive.google.com/file/d/1od6EiA0AmOIq5867XAMUsyQ0-y3Eek_Y/view?usp=sharing)  

## 🤖 Model File  
To streamline the workflow, the trained **vectorized model** is stored as a **Pickle file**, enabling seamless reusability.  

🔗 **Download Trained Model:**  
- [Vectorized Model Pickle](https://drive.google.com/file/d/1ryKP6k1EYdBUTKMThTDChFt_GRRsSj_B/view?usp=sharing)  

## ⚡ Installation & Setup  
Follow these steps to run the project on your local machine:  

### **1️⃣ Install Dependencies**  
Ensure you have the required Python libraries:  
```bash
pip install numpy pandas scikit-learn nltk
```

### **2️⃣ Load Dataset & Model**  
- Download the datasets and the pickle file from the links above.  
- Place them in your **working directory**.  

### **3️⃣ Run Jupyter Notebook**  
```bash
jupyter notebook
```
- Open the **Movie Recommender System Notebook** and execute the cells.  

## 🛠️ How It Works  
1️⃣ **Preprocessing:** Movie data is cleaned, tokenized, and vectorized.  
2️⃣ **TF-IDF Similarity:** The model computes similarity between movies.  
3️⃣ **Recommendation Engine:** The system retrieves the **top 5 most relevant movies**.  
4️⃣ **Optimized Model:** The trained model is stored for quick access.  

## 🏗️ Usage  
🔹 Input any **movie title** → Get **5 similar movie recommendations**.  
🔹 Experiment with the dataset and improve the **recommendation algorithm**.  

## 🤝 Contributing  
Contributions are welcome! To contribute:  
1. **Fork** the repository.  
2. Create a **new branch** (`feature-branch`).  
3. Commit and push changes.  
4. Submit a **pull request** (PR).  

## 📜 License  
This project is released under the **MIT License** – feel free to modify and use it.  

## 📩 Contact  
For queries, suggestions, or contributions, feel free to reach out!  

---  
🚀 **Unlock the power of personalized movie recommendations!** 🎥✨  

