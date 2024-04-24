```shell
gpt-researcher/
│
├── backend/                 # Server-side code
│   ├── server.py            # FastAPI server handling requests and WebSocket communication
│   ├── websocket_manager.py # Manages WebSocket connections
│   └── utils.py             # Utility functions for file conversion
│
├── docs/                    # Documentation files
│   ├── docs/                # User guides, examples, and API references
│   ├── blog/                # Blog posts
│   ├── src/                 # Docusaurus source files
│   ├── package.json         # Docusaurus dependencies and scripts
│   └── ...                  # Other Docusaurus configuration files
│
├── examples/                # Sample code demonstrating usage
│
├── frontend/                # Client-side web interface code
│   ├── index.html           # Main HTML file
│   ├── styles.css           # CSS styles
│   ├── scripts.js           # JavaScript for interactivity
│   └── static/              # Static assets (images, etc.)
│
├── gpt_researcher/          # Core library code
│   ├── scraper/             # Web scraping utilities
│   ├── retrievers/          # Search APIs for retrieving information
│   ├── context/             # Utilities for compressing and retrieving context
│   ├── memory/              # Embedding storage for semantic search
│   ├── config/              # Configuration management
│   ├── llm_provider/        # LLM integrations (OpenAI, Google, Azure)
│   └── utils/               # Helper functions
│
├── notes/                   # Jupyter notebooks for development
│
├── .dockerignore            # Files and directories ignored by Docker
├── .gitignore               # Files and directories ignored by Git
├── CODE_OF_CONDUCT.md       # Code of conduct for contributors
├── CONTRIBUTING.md          # Contribution guidelines
├── Dockerfile               # Instructions for building a Docker image
├── LICENSE                  # MIT license
├── README.md                # Project overview and setup instructions
├── README-zh_CN.md          # Chinese translation of README
├── cli.py                   # Command-line interface entry point
├── docker-compose.yml       # Docker Compose configuration
├── main.py                  # Main entry point of the application
├── poetry.lock              # Lock file for Poetry dependencies
├── poetry.toml              # Poetry configuration
├── pyproject.toml           # Python project configuration
├── requirements.txt         # Python dependencies
└── setup.py                 # Python package setup script
```