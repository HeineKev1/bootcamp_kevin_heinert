#SOFR Predictor
**Stage:** Problem Framing & Scoping (Stage 01)

##Problem Statement 
Many lendors and creditors rely on the SOFR to determine interest payments. As such, for budgeting purposes, knowing what the SOFR will be could prove to be very handy.

##Stakeholder & User
This project prioritizes stakeholder value over user value as they are the end-user. The stakeholders are CFOs. Users are analysts and the stakeholders. This project is best used right when the latest SOFR data has become available as it should be able to predict the SOFR rates for the next week.

##Useful Answer & Decision
This project is predictive and returns several estimation ranges of SOFR up to a week ahead and pulls the latest data daily.

##Assumptions and Constraints
This will be updated as the project undergoes development

##Known Unknowns / Risks
- Model is not entirely accurate, the outputs are estimations

##Lifecycle Mapping
- Goal 1: Problem Framing & Scoping 
    - artifact: README.md
- Goal 2: Acquiring, Ingesting, & Storing the Data 
    - artifact: raw data in data folder
- Goal 3: Data Preprocessing & Outlier Analysis
    - artifact: processed data in data folder
- Goal 4: Exploratory Data Analysis 
    - artifact: Report file in notebooks folder
- Goal 5: Feature Engineering & Modeling
    - artifact: Model is created and saved in project folder
- Goal 6: Communication
    - artifact: Assumptions part of README.md is completed, reports are created, and design notes are created and saved in the docs folder
- Goal 7: Deployment & Monitoring
    - artifact: Repo is published


##Repo Plan
data/, src/, notebooks/, docs/, cadence for updates