
📧 **AI Cold Email Generator**

Generate personalized cold emails for Internships & Jobs in 10 seconds using AI + RAG.Tired of sending the same "Dear Hiring Manager" email to 100 companies? This tool reads any Job Description, extracts required skills, matches them with your portfolio, and writes a tailored cold email for you.✨ Demo
Part of this response isn't supported on this device yet. View the full response on your phone.
🚀 Key Features

<img width="1908" height="956" alt="Screenshot 2026-07-13 191902" src="https://github.com/user-attachments/assets/dd63d4de-6ed4-48ea-b96f-b2de63cb5549" />
<img width="1913" height="935" alt="Screenshot 2026-07-13 191917" src="https://github.com/user-attachments/assets/d7a993cc-219c-4bb5-a9b4-0b759e9d8f7d" />


AI-Powered JD Parsing: Automatically extracts Role, Experience, Skills from any Job DescriptionRAG-Based Portfolio Matching: Uses ChromaDB + Embeddings to find your 2-3 most relevant projects3 Email Tones: Switch between Professional, Friendly, and DirectOne-Click Download: Export generated email as.txtFast: Powered by Groq Llama 3.3 for sub-5s generation🛠️ Tech StackCategoryTechnologyFrontendStreamlitLLMGroq - Llama 3.3 70B VersatileFrameworkLangChain, LangChain-GroqVector DBChromaDBEmbeddingssentence-transformers/all-MiniLM-L6-v2LanguagePython 3.10+⚙️ Setup & Installation
Clone the repositorybashgit clone https://github.com/Akshayprabhe/cold-email-generator.git
cd cold-email-generatorCreate virtual environmentbashpython -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activateInstall dependenciesbashpip install -r requirements.txtAdd API Key
Create a .env file in the root directory and add:javascriptGROQ_API_KEY=your_groq_api_key_hereGet your free API key from Groq CloudBuild Vector Store
Add your portfolio projects to data/portfolio.csv with columns: Techstack, Links
Then run:bashpython app/portfolio.pyThis will create the vectorstore/ folderRun the Appbashstreamlit run app/main.pyOpen http://localhost:8501 in your browser📁
<img width="1911" height="905" alt="Screenshot 2026-07-13 191936" src="https://github.com/user-attachments/assets/767b4d58-06e7-4b22-8534-84b8a5a95f35" />


**Project Structurejavascriptcold-email-generator/**
<img width="515" height="422" alt="Screenshot 2026-07-13 210539" src="https://github.com/user-attachments/assets/8dfd4ae1-790b-49a0-b76b-bf4141b5538b" />


Input JD: "AI Intern role requiring Python, LangChain, RAG"
Output:javascriptSubject: Application for AI Intern Position

Hi Hiring Manager,

I came across your AI Intern role and was excited to see you're looking for skills in Python, LangChain, and RAG. As a 4th Year AIDS Engineering student, I recently built a Cold Email Generator using the exact same stack...

**Portfolio: [link1] [link2]**

Best regards,
Akshay Prabhe🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.📬 Contact
Akshay Prabhe - 4th Year AIDS Engineering StudentLinkedIn: linkedin.com/in/akshayprabheGitHub: @AkshayprabheEmail: your.email@gmail.com🙏 Acknowledgements
Groq for fast LLM inferenceLangChain communityBuilt as part of my job search journeyMade with ❤️ by Akshay Prabhe⭐ Star this repo if you found it helpful!javascript
### **Don't forget to also add `requirements.txt`**
```txt
streamlit==1.38.0
langchain==0.3.0
langchain-groq==0.1.5
langchain-community==0.3.0
chromadb==0.5.5
sentence-transformers==3.0.1
python-dotenv==1.0.1
