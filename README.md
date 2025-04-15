# StatVision – Sports Data Platform

## Final Design Report Table Of Contents

1.  [Project Description (updated to include 400-character abstract and should reflect final version of the project)](docs/FinalDesignReport/Project_Description.md)

2.  [User Interface Specification (optional inclusion of UI design)](docs/FinalDesignReport/UI Specification.pdf)

3.  [Test Plan and Results (describe execution and results of all tests)](docs/FinalDesignReport/Test_Plan.md)

4.  [User Manual (includes links and screenshots of online user manual; include FAQ in report)](docs/FinalDesignReport/User_Guide.md)

5.  [Spring Final PPT Presentation](docs/FinalDesignReport/Presentation.pdf)

6.  [Final Expo Poster](docs/FinalDesignReport/Copy of Expo Poster (48 x 42 in).pdf)

7.  [Assessments (JD)](docs/FinalDesignReport/JD)

7a.  [Assessments (EB)](docs/FinalDesignReport/EB)

7b.  [Assessments (KW)](docs/FinalDesignReport/KW)

8.  [Summary of Hours and Justification (one per individual team member)(See Team Member Initials Folders)](docs/FinalDesignReport/)

9.  [Summary of Expenses](docs/FinalDesignReport/ExpensesSummary.txt)

## Table of Contents

- [Team Names and Project Abstract](#team-names-and-project-abstract)
   - [Team Names](#team-names)
   - [Project Abstract](#project-abstract)
- [Vision](#vision)
  - [Who We Serve](#who-we-serve)
  - [Issues Addresses](#issues-addressed)
    - [Problem Statement](#problem-statement)
    - [Inadequacy of Current Solutions](#inadequacy-of-current-solutions)
    - [Problems Solved](#problems-solved)
  - [Competitions](#competition)
    - [Competitors](#competitors)
    - [Why Ours Is Different](#why-ours-is-different)
  - [Software Architecture](#software-architecture)
    - [Component Interactions](#component-interactions)
    - [Languages and Toolkits](#languages-and-toolkits)
    - [Data Accessed and Stored](#data-accessed-and-stored) 
  - [Challenges and Risks](#challenges-and-risks)
    - [What Might Affect the Development Schedule](#what-might-affect-the-development-schedule)
    - [Minimizing Risk](#minimizing-risk)
- [Additional Documentation](#additional-documentation)
  - [Project Description](#project-description)
  - [Project Tasks and Timeline](#project-tasks-and-timeline)
      - [Task Lists](#task-lists)
      - [Milestones](#milestones)
      - [Timeline](#timeline)
      - [Effort Matrix](#effort-matrix)
      - [Appendix](#appendix)
  - [Constraints](#constraints)
    - [Project Constraints](#project-constraints)
    - [Budget Analysis](#budget-analysis)
  - [Project Presentation](#project-presentation)
    - [PowerPoint Presentation](#powerpoint-presentation)
    - [Video Presentation](#video-presentation)
  - [Self-Assessment Essays](#self-assessment-essays)
    - [Eric Bridgens Assessment](#eric-bridgens-assessment)
    - [Joshua Dickens Assessment](#joshua-dickens-assessment)
    - [Kyle Willoughby Assessment](#kyle-willoughby-assessment)
  - [Professional Biographies](#professional-biographies)
    - [Eric Bridgens Assessment](#eric-bridgens-biography)
    - [Joshua Dickens Assessment](#joshua-dickens-biography)
    - [Kyle Willoughby Assessment](#kyle-willoughby-biography)

---



## Team Names and Project Abstract


### Team Names

- **Eric Bridgens** – BridgeEC@mail.UC.edu  
- **Joshua Dickins** – DickenJD@mail.UC.edu 
- **Kyle Willoughby** – WillouKM@mail.UC.edu  

- **Jillian Aurisano** (Advisor) – AurisaJM@mail.UC.edu  


### Project Abstract
Our project aims to create a dynamic sports tracking and analytics platform for casual fans, fantasy sports players, and analyst- Fans can view real-time stats for teams and players, while fantasy users access data for roster decision- Analysts benefit from league-wide dat- By blending real-time updates with analytics, the platform delivers actionable sports insights for all users—both casual and die-hard fans can find what they need quickly and easily.

---



## Vision
StatVision is a web application designed to track, report, and analyze sports data across multiple leagues and sport- By consolidating large volumes of data and presenting it in an intuitive format, StatVision empowers athletes, teams, analysts, and fans to make informed, data-driven decision- Users can visualize trends, evaluate player performances, compare statistics, and gain deeper insights into sports metrics.

---

### Who We Serve

- **Sports Fans:** Eager to track and compare players or team performances in real time.  
- **Coaches and Analysts:** Seeking efficient data collection and advanced reporting tools.  
- **Players and Organizations:** Looking to monitor individual or team performance metrics and historical data to inform strategies and improvements.

---


### Issues Addressed

---

#### Problem Statement

- Sports fans and analysts often struggle to find reliable, up-to-date data across multiple league- Existing resources may impose paywalls, limit the frequency of searches, or provide unwieldy user interfaces that confuse casual user- StatVision aims to solve this by consolidating sports data into an intuitive, feature-rich platform that remains free to use, offering advanced statistics and flexible queries in one place.

---

#### Inadequacy of Current Solutions

- **Single-League Focus:** Many websites concentrate on just one sport or league, forcing users to switch between platforms for different sports.  
- **Paywalls and Restricted Access:** Free usage often comes with limits on advanced statistics or daily search quotas.  
- **Complicated Interfaces:** Sites that do offer robust statistics can overwhelm non-expert users with overly busy layouts and multiple pages of data filtering.

---

#### Problems Solved

- **Fragmented Sports Data:** StatVision aggregates and standardizes complex sports information from various sources, eliminating the need to visit multiple league-specific or paywalled websites.
- **Difficulty in Identifying Trend:** Interactive dashboards and visual tools enable users to spot performance patterns, track progress, and compare statistics over time.
- **Limited Analytical Insights:**  By providing robust analytics and reporting, StatVision helps professionals and enthusiasts generate in-depth analyses to support data-driven decision-making.

---

### Competition

---

#### Competitors

- **Major Sports Websites:** Offer surface-level stats but lack deeper analytics or cross-sport coverage.  
- **Advanced Analytics Platforms:** Highly specialized, may be costly, and often require technical expertise.  
- **Team-Specific Data Systems:** Provide thorough stats for a single league or team but are not comprehensive across sports.

---

#### Why Ours Is Different

- **Cross-Sport Analytics:** StatVision unifies multiple leagues and sports under a single user experience.  
- **User-Friendly Dashboards:** Complex data is presented through intuitive visualizations, appealing to both casual fans and professional analysts.  
- **Data-Driven Insights:** StatVision’s analytical tools, reporting features, and real-time updates facilitate effective decision-making—from coaching strategies to fantasy sports lineups.

---

### Software Architecture

---

#### Component Interactions

- **Front-end:** A web interface that allows users to visualize and interact with sports data.  
- **Back-end:** A server-side application that processes requests, retrieves data from databases, performs analytics, and returns results to the front-end.  
- **Database:** Stores sports statistics, user queries, historical records, and any relevant metadata.  
- **APIs:** The front-end communicates with the back-end via RESTful or GraphQL APIs for data retrieval and analysis.  
- **Cloud-based Services:** Ensures high availability, reliability, and scalability in hosting and deployment.

---

#### Languages and Toolkits

- **Front-end Development:** HTML, CSS, JavaScript (possibly using React, Vue.js, or similar frameworks).  
- **Back-end Development:** Python (for data pipelines, analytics, and API services).  
- **Database:** SQLite (for initial development and testing) with a potential upgrade to PostgreSQL in production.  
- **Cloud-based Services:** Google Cloud or similar cloud platforms for hosting and scaling.

---

#### Data Accessed and Stored

- **Sports Data:** Player stats, team performance metrics, game outcomes, and historical records.  
- **User-Generated Analytics:** Custom queries, comparisons, saved reports, and visualized charts.  
- **Dashboard Configurations:** Personalized views and filters for ongoing analysis.  
- **Historical/Real-Time Updates:** Ability to ingest incremental or live data to keep analytics current.

---

### Challenges and Risks

#### What Might Affect the Development Schedule

- **Complex Data Ingestion:** Pulling from diverse sports data sources can introduce unexpected delays or require intricate parsing logic.  
- **Scalability Concerns:** Handling large or real-time data sets demands a robust infrastructure and thorough testing.  
- **User Interface Design:** Striking a balance between offering advanced analytics features and maintaining an intuitive, uncluttered layout.  
- **Third-Party Dependencies:** Reliance on external APIs, libraries, or data providers can introduce latency or availability issues.

#### Minimizing Risk

- **Clear Project Plan:** Define milestones, deadlines, and stages (design, development, testing, deployment) for better project management.  
- **Utilize Team Expertise:** Assign tasks based on front-end, back-end, and data-engineering strengths to accelerate problem-solving.  
- **User Research and Testing:** Gather feedback early and often, ensuring features and interfaces align with user needs.  
- **Scalable Infrastructure:** Employ cloud-based resources to dynamically adjust computing power as the user base grows.  
- **Continuous Monitoring and Updates:** Release timely patches, track performance metrics, and adapt to evolving user requirements.

---



## [Additional Documentation](docs/)


### [Project Description](docs/Project_Description.md)


### [Project Tasks and Timeline](docs/Timeline_Documentation/)

  - #### [Task Lists](docs/Timeline_Documentation/Task_Lists.md)

  - #### [Milestones](docs/Timeline_Documentation/Milestones.md)

  - #### [Timeline](docs/Timeline_Documentation/Timeline.md)

  - #### [Effort Matrix](docs/Timeline_Documentation/Effort_Matrix.md)

  - #### [Appendix](docs/Timeline_Documentation/Appendix.md)


### [Contstraints](docs/Constraints/)

  - #### [Project Constraints](docs/Constraints/Project_Contstraints.md)

  - #### [Budget Analysis](docs/Constraints/Budget_Analysis.md)


### [Project Presentation](#project-presentation)

  - #### [PowerPoint Presentation](docs/Project_Presentation/PowerPoint_Presenatation.pptx)

  - #### [Video Presentation](https://mailuc-my.sharepoint.com/personal/bridgeec_mail_uc_edu/_layouts/15/stream.aspx?id=%2Fpersonal%2Fbridgeec%5Fmail%5Fuc%5Fedu%2FDocuments%2FAssignment%5F8%5F%2D%5FSlide%5FShow%5F%2D%5FFall%5FDesign%5FPresenatations%20%281%29%2Emp4&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&ga=1&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E9fb0ca11%2Dfba1%2D4c1c%2D9d78%2D22b42090d69e)


### [Self-Assessment Essays](docs/Capstone_Assessments/)

  - #### [Eric Bridgens Assessment](docs/Capstone_Assessments/Bridgens_Assessment.md)

  - #### [Joshua Dickens Assessment](docs/Capstone_Assessments/Dickens_Assessment.md)

  - #### [Kyle Willoughby Assessment](docs/Capstone_Assessments/Willoughby_Assessment.md)


### [Professional Biographies](Professional_Biographies/)

  - #### [Eric Bridgens Biography](Professional_Biographies/Bridgens_Biography.md)

  - #### [Joshua Dickins Biography](Professional_Biographies/Dickens_Biography.md)

  - #### [Kyle Willoughby Biography](Professional_Biographies/Willoughby_Biography.md)
