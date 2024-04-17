## Setting Up Virtual Environment

1. Create a virtual environment by running:
    ```
    python -m venv venv
    ```
2. Activate the virtual environment:
    - **Windows**:
        ```
        venv\Scripts\activate
        ```
    - **Unix or MacOS**:
        ```
        source venv/bin/activate
        ```

## Installing Dependencies

1. With the virtual environment activated, install dependencies from the requirements.txt file:
    ```
    pip install -r requirements.txt
    ```


### Running in a simple ui(no restapi used)

1. Open a terminal or command prompt.
2. Navigate to the project directory if you haven't already.
3. Run the following command to start the Streamlit application:

    ```
    streamlit run simple_ui.py
    ```

   This will launch the application in your default web browser.

### Running in a simple ui(restapi used)
0.need to configure api server first and update the endpoint in simple_ui(restapi).py code 
1. Open a terminal or command prompt.
2. Navigate to the project directory if you haven't already.
3. Run the following command to start the Streamlit application:

    ```
    streamlit run simple_ui(restApi).py
    ```

## Running the RestApi server

1. Open a terminal.
2. Navigate to the project directory.
3. Run `python api_server.py`.

## Interacting with the ChatBot API

The Theatre ChatBot API has two endpoints:

1. **Initialize ChatBot**:

    - Endpoint: `/initialize_chatbot`
    - Method: `POST`
    - Payload: `{"location": "your_location"}`
    - Example: `POST http://localhost:5000/initialize_chatbot {"location": "kochi"}`

2. **Execute Result**:

    - Endpoint: `/execute_result`
    - Method: `POST`
    - Payload: `{"nl_question": "your_question"}`
    - Example: `POST http://localhost:5000/execute_result {"nl_question": "What are the upcoming shows?"}`

## Notes

- Initialize the ChatBot instance before executing queries.
- Replace `"your_location"` and `"your_question"` with actual values.
