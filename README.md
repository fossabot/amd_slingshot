<h1 align="center">AI Privacy Compliance Agent</h1> <p align="center"> A Streamlit app using <b>RAG + LLM</b> to analyze company documents for privacy & compliance risks using standard framework references. </p> <hr/> <h2>📌 Quick Summary</h2> <ul> <li><b>Purpose:</b> Provide structured privacy compliance analysis using framework documents + uploaded company file</li> <li><b>Main Components:</b> <ul> <li>Document loader</li> <li>FAISS vector store</li> <li>Embeddings</li> <li>Prompt builder</li> <li>LLM service wrapper</li> </ul> </li> </ul> <hr/> <h2>⚙️ Prerequisites</h2> <ul> <li>Python 3.8+</li> <li>Install dependencies</li> </ul> <pre><code>pip install -r requirements.txt</code></pre> <p>Configure OpenAI API key in <code>config/settings.py</code> or environment variables.</p> <hr/> <h2>🔧 Configuration</h2> <table> <tr><th>Variable</th><th>Description</th></tr> <tr><td><code>DATA_PATH</code></td><td>Folder with framework documents (ex: data/frameworks)</td></tr> <tr><td><code>VECTOR_STORE_PATH</code></td><td>Location to store/load FAISS index</td></tr> <tr><td><code>OPENAI_API_KEY</code></td><td>API key for embeddings & LLM</td></tr> </table> <hr/> <h2>🧠 Build the Vector Store</h2> <pre><code>python build_index.py</code></pre> <p>Creates embeddings and saves FAISS index to configured path.</p> <hr/> <h2>🚀 Run the Application</h2> <pre><code>streamlit run app.py</code></pre> <h3>UI Features</h3> <ul> <li>Upload company document (.pdf, .docx, .txt)</li> <li>Ask privacy questions</li> <li>RAG search over framework docs</li> <li>Structured LLM analysis</li> </ul> <hr/> <h2>📂 Project Structure</h2> <pre><code>. ├── app.py ├── build_index.py ├── create_vector_store.py ├── config/settings.py ├── services/ │ ├── document_loader.py │ ├── rag_service.py │ ├── llm_service.py │ └── privacy_analyzer.py ├── utils/prompts.py ├── data/frameworks/ └── vector_store/ </code></pre> <hr/> <h2>🧩 File Responsibilities</h2>

<b>app.py</b>

<p>Streamlit UI — handles upload, chat, and orchestrates RAG + LLM calls</p>

<b>build_index.py</b>

<p>Creates embeddings using OpenAIEmbeddings and builds FAISS index</p>

<b>services/document_loader.py</b>

<p>Extracts text from PDF, DOCX, and TXT</p>

<b>services/rag_service.py</b>

<p>Loads FAISS index and retrieves top-k relevant framework passages</p>

<b>services/llm_service.py</b>

<p>Wrapper around OpenAI chat completion API</p>

<b>services/privacy_analyzer.py</b>

<p>Builds analysis prompt and sends to LLM</p>

<b>utils/prompts.py</b>

<p>Contains prompt templates and final prompt composer</p> <hr/> <h2>🔍 How It Works</h2> <ol> <li>Framework documents embedded and stored in FAISS</li> <li>User uploads company document</li> <li>User question embedded</li> <li>Relevant framework passages retrieved</li> <li>Context + document + question combined</li> <li>LLM generates structured privacy analysis</li> </ol> <hr/> <h2>🌐 Environment Variables</h2> <pre><code>$env:OPENAI_API_KEY="sk-..."</code></pre> <hr/> <h2>🛠 Troubleshooting</h2> <ul> <li><b>FAISS index fails</b> → Verify VECTOR_STORE_PATH</li> <li><b>PDF extraction bad</b> → Modify document_loader.py</li> <li><b>Embedding errors</b> → Check API key & internet</li> </ul> <hr/> <h2>📈 Future Improvements</h2> <ul> <li>Chunking & batching for large docs</li> <li>Limit upload size</li> <li>Add unit tests</li> <li>Improve prompt reliability</li> <li>Embedding caching</li> </ul> <hr/> <p align="center"><i>Built for automated privacy compliance analysis using retrieval-augmented generation.</i></p>
