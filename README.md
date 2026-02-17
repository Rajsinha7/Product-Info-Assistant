🛍️ Product Info Assistant

AI-Powered Product Q&A & Comparison System using RAG

The Product Info Assistant is an AI-powered chatbot that enables users to query, explore, and compare product information using natural language.
Instead of manually browsing long product catalogs, users can upload a CSV file containing product data and ask intelligent questions such as:

“Which phone has the best camera under ₹20,000?”

“Compare OnePlus Nord CE 3 and Samsung Galaxy S23 in terms of charging speed.”

This project demonstrates a real-world GenAI use case by combining Retrieval-Augmented Generation (RAG) with LangChain and Hugging Face models, similar to Q&A systems used by e-commerce platforms like Amazon and Flipkart.

--> Key Features

- CSV Upload Support
Upload product catalogs dynamically (no hardcoded data).

- AI-Powered Natural Language Q&A
Ask product-related questions in plain English.

- Retrieval-Augmented Generation (RAG)
Retrieves only relevant product information before generating responses, improving accuracy.

- Product Comparison
Compare two or more products based on specifications, price, or features.

- No API Key Required
Uses Hugging Face local models (free & offline).

- Streamlit UI
Clean, interactive chatbot interface.

--> Tech Stack
Category	Tools
Language	Python
LLM Framework	LangChain
AI Models	Hugging Face (FLAN-T5)
AI Technique	Retrieval-Augmented Generation (RAG)
UI	Streamlit
Data Format	CSV
Embeddings / Retrieval	Vector-based document retrieval

--> Project Structure
Product-Info-Assistant/
│
├── app.py
├── products.csv
├── product.csv
├── codes/
├── docs/
├── README.md

⚙️ How to Run the Project
1️. Clone the Repository
git clone https://github.com/Rajsinha7/Product-Info-Assistant.git
cd Product-Info-Assistant

2️. Install Dependencies
pip install -r requirements.txt

3️. Run the Application
streamlit run app.py

--> Requirements
Python 3.8+
Internet only for first-time model download

--> How It Works (Architecture)

User uploads a CSV file containing product data
Data is split into documents and indexed
User asks a natural language query
RAG retrieves the most relevant product records

Hugging Face LLM generates a context-aware answer

Response is shown in the Streamlit chatbot UI
