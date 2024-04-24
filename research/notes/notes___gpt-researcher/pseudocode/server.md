```pseudocode:backend/server.py
import necessary libraries and modules

define ResearchRequest class (Pydantic model)
    task: str
    report_type: str
    agent: str

create FastAPI app

mount frontend static files and templates
    "/site" -> "./frontend"
    "/static" -> "./frontend/static"

initialize Jinja2Templates with "./frontend" directory

initialize WebSocketManager

define startup_event function
    if "outputs" directory doesn't exist
        create "outputs" directory
    mount "/outputs" -> "outputs" directory

define read_root function (GET "/")
    render "index.html" template with provided request

define websocket_endpoint function (WebSocket "/ws")
    connect WebSocket using manager.connect(websocket)
    
    try
        while true
            receive data from WebSocket
            if data starts with "start"
                extract research request data from JSON
                if task and report_type are provided
                    start RAG process and generate report using manager.start_streaming(task, report_type, websocket)
                    save report as PDF using write_md_to_pdf(report)
                    save report as DOCX using write_md_to_word(report)
                    send report file paths to client via WebSocket using websocket.send_json(...)
                else
                    print error message
    
    except WebSocketDisconnect
        disconnect WebSocket using manager.disconnect(websocket)
```

This pseudocode represents the structure and flow of the `server.py` file in a simplified manner. It outlines the main components and logic of the FastAPI server, including:

1. Importing necessary libraries and modules
2. Defining the `ResearchRequest` Pydantic model
3. Creating the FastAPI app
4. Mounting frontend static files and templates
5. Initializing Jinja2Templates and WebSocketManager
6. Defining the startup event handler
7. Defining the root URL handler
8. Defining the WebSocket endpoint handler
   - Connecting the WebSocket
   - Receiving data from the WebSocket
   - Extracting research request data from JSON
   - Starting the RAG process and generating the report
   - Saving the report as PDF and DOCX
   - Sending report file paths to the client via WebSocket
   - Handling WebSocket disconnection

This pseudocode provides a high-level overview of the server's functionality and can serve as a starting point for understanding the RAG app's server-side implementation.