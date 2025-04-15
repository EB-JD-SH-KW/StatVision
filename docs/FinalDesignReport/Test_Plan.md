# Assignment #1 - Test Plan

## Part I. Description of Overall Test Plan

Our project uses a mix of testing methods to ensure accurate and efficient access to professional sports data. Black-box testing checks if the front end properly displays user-requested data, if the API correctly fetches league stats, and how the system handles errors like API failures or missing data. These tests help confirm that users always receive relevant and properly formatted information.

White-box testing focuses on backend processes, such as validating database queries, ensuring scheduled data updates run smoothly, and organizing fetched data correctly in our database. These tests make sure that the backend efficiently processes and stores sports statistics for quick retrieval.

We also run integration tests to verify that different parts of the system API, database, and frontend work together seamlessly. This includes testing search and filtering, ensuring accurate results for player statistics, and verifying the correct formatting of data in the UI. Functional tests confirm that each feature behaves as expected, while performance tests check the system’s speed and responsiveness and compare direct API calls versus database retrieval.

## Part II. Test Case Descriptions

### Test Case 1: Frontend Data Visualization
- **Identifier:** TC001
- **Purpose:** Validate that the front end correctly visualizes user-selected data.
- **Description:** Test if the UI properly renders data from the backend API or database.
- **Inputs:** Simulated API response with league data.
- **Expected Outputs:** Data correctly displayed in tables, graphs, or charts.
- **Case Type:** Normal case
- **Blackbox/Whitebox:** Blackbox test
- **Functional/Performance:** Functional test
- **Unit/Integration:** Integration test

### Test Case 2: API Data Fetching
- **Identifier:** TC002
- **Purpose:** Verify API fetch functionality.
- **Description:** Ensure API requests successfully retrieve league data.
- **Inputs:** API request with valid parameters.
- **Expected Outputs:** JSON response with accurate league data.
- **Case Type:** Normal case
- **Blackbox/Whitebox:** Blackbox test
- **Functional/Performance:** Functional test
- **Unit/Integration:** Integration test

### Test Case 3: API Error Handling
- **Identifier:** TC003
- **Purpose:** Ensure system handles API failures.
- **Description:** Test behavior when API returns an error or times out.
- **Inputs:** Invalid API request or network failure.
- **Expected Outputs:** Proper error message displayed.
- **Case Type:** Abnormal case
- **Blackbox/Whitebox:** Blackbox test
- **Functional/Performance:** Functional test
- **Unit/Integration:** Integration test

### Test Case 4: Database Connection
- **Identifier:** TC004
- **Purpose:** Validate database connection and accessibility.
- **Description:** Ensure backend can connect to the database.
- **Inputs:** Database connection request.
- **Expected Outputs:** Successful connection.
- **Case Type:** Normal case
- **Blackbox/Whitebox:** Whitebox test
- **Functional/Performance:** Functional test
- **Unit/Integration:** Integration test

### Test Case 5: SQL Query Generation
- **Identifier:** TC005
- **Purpose:** Ensure SQL query generation works correctly.
- **Description:** Test if user search inputs are converted into accurate SQL queries.
- **Inputs:** Sample user query input.
- **Expected Outputs:** Correct SQL query generated.
- **Case Type:** Normal case
- **Blackbox/Whitebox:** Whitebox test
- **Functional/Performance:** Functional test
- **Unit/Integration:** Unit test

### Test Case 6: Data Update Script
- **Identifier:** TC006
- **Purpose:** Validate scheduled data updates.
- **Description:** Test script that updates player/team stats at set frequency.
- **Inputs:** Trigger update function.
- **Expected Outputs:** Database reflects updated player/team data.
- **Case Type:** Boundary case
- **Blackbox/Whitebox:** Blackbox test
- **Functional/Performance:** Functional test
- **Unit/Integration:** Unit test

### Test Case 7: API Client Testing
- **Identifier:** TC007
- **Purpose:** Validate API request functionality using Postman/Bruno.
- **Description:** Test API endpoints with predefined requests.
- **Inputs:** API requests with valid/invalid parameters.
- **Expected Outputs:** Proper response handling.
- **Case Type:** Normal/abnormal case
- **Blackbox/Whitebox:** Blackbox test
- **Functional/Performance:** Functional test
- **Unit/Integration:** Integration test

### Test Case 8: UI Search and Filtering
- **Identifier:** TC008
- **Purpose:** Verify that users can search and filter data.
- **Description:** Test search and filtering functionalities.
- **Inputs:** Search query and filter options.
- **Expected Outputs:** Correctly filtered search results.
- **Case Type:** Normal case
- **Blackbox/Whitebox:** Whitebox test
- **Functional/Performance:** Functional test
- **Unit/Integration:** Integration test

### Test Case 9: Data Organization Technique
- **Identifier:** TC009
- **Purpose:** Ensure data is stored in an organized format.
- **Description:** Test database schema for logical structure.
- **Inputs:** Database schema validation.
- **Expected Outputs:** Properly structured tables and relationships.
- **Case Type:** Normal case
- **Blackbox/Whitebox:** Whitebox test
- **Functional/Performance:** Functional test
- **Unit/Integration:** Unit test

### Test Case 10: Frontend User Experience
- **Identifier:** TC010
- **Purpose:** Validate front-end usability.
- **Description:** Ensure the front end is user-friendly and responsive.
- **Inputs:** User interactions.
- **Expected Outputs:** Smooth and responsive UI behavior.
- **Case Type:** Normal case
- **Blackbox/Whitebox:** Blackbox test
- **Functional/Performance:** Performance test
- **Unit/Integration:** Integration test

### Test Case 11: Data Organization from Fetched Data
- **Identifier:** TC011
- **Purpose:** Verify data organization
- **Description:** Ensure the API fetched data is correctly organized in SQL database.
- **Inputs:** API call fetching NFL team data
- **Expected Outputs:** Database table updated with correct values.
- **Case Type:** Normal case
- **Blackbox/Whitebox:** Whitebox test
- **Functional/Performance:** Functional test
- **Unit/Integration:** Integration test

### Test Case 12: Accurate Search Results
- **Identifier:** TC012
- **Purpose:** Validate user search feature
- **Description:** Ensure search returns relevant results.
- **Inputs:** Query “Lebron James career assists” in search
- **Expected Outputs:** Player name with correct statistic.
- **Case Type:** Normal case
- **Blackbox/Whitebox:** Blackbox test
- **Functional/Performance:** Functional test
- **Unit/Integration:** Integration test

### Test Case 13: Frontend Output Handling
- **Identifier:** TC013
- **Purpose:** Validate front-end output.
- **Description:** Ensure the front end displays the correct output and is formatted correctly.
- **Inputs:** Query “Lebron James 30-point games” in search
- **Expected Outputs:** Correctly formatted results of player name with statistics.
- **Case Type:** Normal case
- **Blackbox/Whitebox:** Blackbox test
- **Functional/Performance:** Functional test
- **Unit/Integration:** Integration test

### Test Case 14: Handling Unavailable Data
- **Identifier:** TC014
- **Purpose:** Ensure UI handles missing data properly
- **Description:** Check how front-end reacts when data is unavailable/not stored in our database.
- **Inputs:** Query athlete from uncovered sport (e.g., Tennis player)
- **Expected Outputs:** Display “No data available”.
- **Case Type:** Abnormal case
- **Blackbox/Whitebox:** Blackbox test
- **Functional/Performance:** Functional test
- **Unit/Integration:** Integration test

## Part III. Test Case Matrix

| ID     | Case Type  | Blackbox/Whitebox | Functional/Performance | Unit/Integration |
|--------|-----------|------------------|----------------------|-----------------|
| TC001  | Normal    | Blackbox         | Functional          | Integration     |
| TC002  | Normal    | Blackbox         | Functional          | Integration     |
| TC003  | Abnormal  | Blackbox         | Functional          | Integration     |
| TC004  | Normal    | Whitebox         | Functional          | Integration     |
| TC005  | Normal    | Whitebox         | Functional          | Unit           |
| TC006  | Boundary  | Blackbox         | Functional          | Unit           |
| TC007  | Abnormal  | Blackbox         | Functional          | Integration     |
| TC008  | Normal    | Whitebox         | Functional          | Integration     |
| TC009  | Normal    | Whitebox         | Functional          | Unit           |
| TC010  | Normal    | Blackbox         | Performance         | Integration     |
| TC011  | Normal    | Whitebox         | Functional          | Integration     |
| TC012  | Normal    | Blackbox         | Functional          | Integration     |
| TC013  | Normal    | Blackbox         | Functional          | Integration     |
| TC014  | Abnormal  | Blackbox         | Functional          | Integration     |
