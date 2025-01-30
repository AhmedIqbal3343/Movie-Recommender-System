# 🎬 Movie Recommender System  

## 📌 Overview
Discover movies like never before! 🎬✨ The Movie Recommender System is an intelligent machine learning project developed in Python and deployed using Streamlit. It uses content-based filtering to analyze movie metadata and recommend five similar movies based on the selected title. Whether you love classics or the latest hits, this system ensures you always find the perfect movie! 🍿🚀
      
🌐 You can explore the live project [here](https://movie-recommender-system2.streamlit.app/).  


## Continuous Improvement:
This project has gone through over **40** iterations to refine and optimize its features. The goal is to continually improve the system’s performance, user experience, and overall efficiency. As I'm deeply connected to this project, I plan on making further enhancements to ensure it remains user-friendly and highly functional for everyone. Expect more updates as we aim for even better recommendations! 🚀💡


## 🚀 Features  
✔️ **Content-Based Filtering** – Recommends movies based on their metadata (genres, cast, crew, etc.).  
✔️ **TF-IDF Vectorization** – Processes text data to measure similarity.  
✔️ **Automatic Pickle File Loading** – Downloads and loads the trained model from **Google Drive**.  
✔️ **Fast Recommendations** – Instantly retrieves the top **5 most relevant movies**.  
✔️ **Movie Posters** – Fetches high-quality posters using the **TMDB API**.  
✔️ **Easy Web Interface** – Built with **Streamlit** for a smooth user experience.  

---

## 📂 Dataset  
The system is trained on a dataset of **5,000 movies**, including key attributes such as:  
🎭 **Genres** | 🎬 **Cast & Crew** | 📅 **Release Date** | 🏆 **Popularity & Ratings**  

🔗 **Dataset Sources:**  
- [TMDB 5000 Movies Dataset](https://drive.google.com/file/d/182mTWOKdg5UM7hx34RutzfWvGfHbomXu/view?usp=sharing)
- [TMDB 5000 Credits Dataset](https://drive.google.com/file/d/1od6EiA0AmOIq5867XAMUsyQ0-y3Eek_Y/view?usp=sharing)  

---

## 🤖 How It Works  
1️⃣ **Preprocessing**: The system processes and cleans movie data.  
2️⃣ **TF-IDF Vectorization**: Computes similarity between movies based on their descriptions.  
3️⃣ **Recommendation Engine**: Finds the **top 5 most similar movies** for the selected title.  
4️⃣ **Downloading Model**: The trained similarity model (`similarity.pkl`) is **automatically downloaded** from **Google Drive**.  
5️⃣ **Fetching Posters**: Retrieves movie posters from **TMDB API** for better visualization.  
6️⃣ **User Interface**: A **Streamlit-based web app** lets users select a movie and view recommendations instantly.  

---

## ⚡ Installation & Setup  
Follow these steps to run the project on your local machine:  

### **1️⃣ Install Dependencies**  
Ensure you have the required Python libraries:  
```bash
pip install streamlit numpy pandas scikit-learn requests gdown
```

### **2️⃣ Run the Streamlit Web App**  
```bash
streamlit run streamlit_app.py
```

### **3️⃣ Usage**  
- Select a movie from the dropdown list.  
- Click the **"Recommend"** button.  
- View **5 similar movies** with their **posters**.  

---

## 🏗️🏗 *Deployment on Streamlit Cloud*  
This project is deployed on Streamlit Cloud, making it accessible online without installation. You can check out the live project [here](https://movie-recommender-system2.streamlit.app/).  


---

## 🔗 Google Drive Model File  
The trained model (`similarity.pkl`) is automatically downloaded in the code using **Google Drive**.  

🔗 **Download Trained Model:** [Click Here](https://drive.google.com/uc?export=download&id=1ryKP6k1EYdBUTKMThTDChFt_GRRsSj_B)  

---

## 🤝 Contributing  
Contributions are welcome! To contribute:  
1️⃣ **Fork** the repository.  
2️⃣ **Create** a new branch (e.g., `feature-branch`).  
3️⃣ **Commit** and push changes.  
4️⃣ **Submit** a **pull request (PR)**.  

---

## 📜 License  
This project is released under the **MIT License** – feel free to modify and use it.  

---

## 📩 Contact  
For queries, suggestions, or contributions, feel free to reach out!  

🚀 **Unlock the power of personalized movie recommendations!** 🎥✨  

