# ChatBot
ChatBot developed using Spring AI, Ollama, StreamLit and DeepSeek-R1.


## 🚀 Spring Boot Chatbot with Streamlit UI  

This project integrates a **Spring Boot Chat API** with a **Streamlit-based UI**, allowing users to interact with a chatbot powered by the **DeepSeek model**.  

---

### **📌 Prerequisites**  
Ensure you have the following installed on your system:  
- **Java 17+** (For Spring Boot)  
- **Maven** (For dependency management)  
- **Python 3.8+** (For Streamlit UI)  
- **pip** (Python package manager)  

---

### **🔧 Setup & Installation**  

#### **1️⃣ Clone the Repository**  
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

#### **2️⃣ Run the Spring Boot Application**  
```bash
cd backend  # Navigate to the Spring Boot project directory
mvn clean install  # Build the project
mvn spring-boot:run  # Start the backend server
```
By default, the Spring Boot application runs on **`http://localhost:8080`**.

#### **3️⃣ Install Python Dependencies**  
Open a new terminal and navigate to the `frontend` folder:  
```bash
cd frontend
pip install streamlit

```

#### **4️⃣ Start the Streamlit UI**  
```bash
streamlit run chatbot.py
```

#### **5️⃣ Open the UI & Start Chatting! 🎉**  
After running the Streamlit app, open the following URL in your browser:  
```
http://localhost:8501
```
Now, test the chatbot powered by the **DeepSeek model**!

---

### **🛠 Troubleshooting**  
- **Port Conflict:** If port `8080` is in use, change the Spring Boot port in `application.properties`:  
  ```properties
  server.port=9090
  ```
- **Python Module Not Found?** Run:  
  ```bash
  pip install streamlit
  ```

---

### **📜 License**  
This project is licensed under **MIT License**. Feel free to contribute!  

---
