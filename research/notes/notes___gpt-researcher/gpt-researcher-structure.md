Here's a breakdown of the core library code in the `gpt_researcher/` directory:

```shell
gpt_researcher/
│
├── scraper/             # Web scraping utilities
│   ├── base_scraper.py  # Base class for web scrapers
│   ├── google_scraper.py  # Google search scraper
│   └── ...             # Other scraper implementations
│
├── retrievers/          # Search APIs for retrieving information
│   ├── base_retriever.py  # Base class for retrievers
│   ├── google_retriever.py  # Google search retriever
│   ├── bing_retriever.py  # Bing search retriever
│   └── ...             # Other retriever implementations
│
├── context/             # Utilities for compressing and retrieving context
│   ├── context_compressor.py  # Compresses context into a condensed format
│   ├── context_retriever.py  # Retrieves relevant context based on a query
│   └── ...             # Other context-related utilities could go here
│
├── memory/              # Embedding storage for semantic search not implemented yet.
│   ├── base_memory.py   # Base class for memory storage
│   ├── faiss_memory.py  # FAISS-based memory storage
│   ├── annoy_memory.py  # Annoy-based memory storage
│   └── ...             # Other memory storage implementations
│
├── config/              # Configuration management
│   ├── config.py        # Configuration class for the library
│   └── ...             # Other configuration-related files
│
├── llm_provider/        # LLM integrations (OpenAI, Google, Azure)
│   ├── base_provider.py  # Base class for LLM providers
│   ├── openai_provider.py  # OpenAI LLM provider
│   ├── google_provider.py  # Google LLM provider
│   ├── azure_provider.py  # Azure LLM provider
│   └── ...             # Other LLM provider implementations
│
└── utils/               # Helper functions
    ├── logging.py       # Logging utilities
    ├── preprocessing.py  # Text preprocessing utilities
    └── ...             # Other utility functions
```



- `scraper/`: Contains web scraping utilities for extracting information from web pages.
- `retrievers/`: Implements search APIs for retrieving relevant information based on queries.
- `context/`: Provides utilities for compressing and retrieving context to support efficient search and retrieval.
- `memory/`: Handles embedding storage for semantic search using different storage backends like FAISS or Annoy.
- `config/`: Manages configuration settings for the library.
- `llm_provider/`: Integrates with different LLM providers such as OpenAI, Google, and Azure.
- `utils/`: Contains helper functions and utilities used throughout the library.

###################################################################################################



```shell
gpt_researcher/
│
├── scraper/             # Indexing (Document Preprocessing)
│   ├── base_scraper.py  # Indexing (Document Preprocessing)
│   ├── google_scraper.py  # Indexing (Document Preprocessing)
│   └── ...             # Indexing (Document Preprocessing)
│
├── retrievers/          # Retrieval
│   ├── base_retriever.py  # Retrieval
│   ├── google_retriever.py  # Retrieval
│   ├── bing_retriever.py  # Retrieval
│   └── ...             # Retrieval
│
├── context/             # Retrieval, Generation
│   ├── context_compressor.py  # Generation (Context Compression)
│   ├── context_retriever.py  # Retrieval
│
├── memory/              # Indexing (Embedding Storage)
│   ├── base_memory.py   # Indexing (Embedding Storage)
│   ├── faiss_memory.py  # Indexing (Embedding Storage)
│   ├── annoy_memory.py  # Indexing (Embedding Storage)
│
├── config/              # Configuration
│   ├── config.py        # Configuration
│
├── llm_provider/        # Generation (Language Model Integration)
│   ├── base_provider.py  # Generation (Language Model Integration)
│   ├── openai_provider.py  # Generation (Language Model Integration)
│   ├── google_provider.py  # Generation (Language Model Integration)
│   ├── azure_provider.py  # Generation (Language Model Integration)
│   └── ...             # Generation (Language Model Integration)
│
└── utils/               # Utility functions (used across components)
    ├── logging.py       # Utility functions
    ├── preprocessing.py  # Indexing (Document Preprocessing), Utility functions
    └── ...             # Utility functions
```


