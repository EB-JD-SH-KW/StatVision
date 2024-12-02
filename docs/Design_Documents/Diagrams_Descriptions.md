# Diagram Descriptions

## Top-Level Diagram
The top-level diagram provides a broad overview of the user experience from a code perspective. The general flow of our project is as follows:
1. A user enters a search query.
2. The query is run against a database to retrieve relevant results.
3. The results are displayed to the user.

---

## Intermediate Diagram
This diagram begins to break down the process further:
1. The app receives the query.
2. The query is processed using the search tool to locate relevant data.
3. Depending on how the user accessed the app:
   - **API Users**: The data is returned as code to integrate into their project.
   - **Web Users**: The data is displayed on the website interface.

Our sports metrics database can be accessed either programmatically (via API) or visually (via the website). The addition of API output ensures flexibility in how users interact with the data.

---

## Full Breakdown
1. **User Access**:
   - **Web Interface**: Users interact with a clean, user-friendly UI, primarily featuring a search box to utilize the search tool.
   - **API Access**: Users integrate the functionality into their own code using an API key.

2. **Data Request**:
   - Users submit a data request filtered by their chosen sports league, as defined in the database structure.
   - Python parses the request for the specified league and constructs a query.

3. **Database Interaction**:
   - The query searches through the weekly updated database, powered by MySQL and Azure/AWS infrastructure.
   - The database locates and organizes the requested data.

4. **Data Delivery**:
   - The user receives the exact data they requested, tailored to the method of access:
     - **API Users**: Data is formatted and returned programmatically.
     - **Web Users**: Data is displayed in the UI.

This process represents the expected start-to-finish user experience for our product.
