1st project:-
Global CO₂ Emissions Tracker by Sector (2010–2023)
Introduction
The Global CO₂ Emissions Tracker is a data-driven project aimed at analyzing and visualizing carbon dioxide emissions across countries and sectors over multiple years. With growing concerns around climate change and environmental impact, this project provides an interactive tool for understanding emission trends globally. The analysis helps identify top emitters, emission hotspots by sector, and supports informed policy decisions.
Abstract
This project utilizes a multi-year dataset covering CO₂ emissions by sector (Energy, Transport, Industry, etc.) for various countries. Using Python for data preprocessing, Excel for data validation, and Tableau for interactive visualizations, the dashboard allows users to compare total emissions, per capita emissions, and per GDP emissions. Key patterns include high emissions in countries like China, USA, and India, and rising transport-related emissions in developing nations.
Tools Used
• Python – for data cleaning, merging, and metric calculation
• Excel – for organizing and inspecting the dataset
• Tableau – for building interactive maps and bar graphs of CO₂ emissions
• Dataset – Multi-year emissions data from Our World in Data, World Bank, UNFCCC
Steps Involved in Building the Project
1. Imported multi-year dataset containing emissions by country, year, and sector.
2. Cleaned the data using Python and checked for missing values.
3. Created new metrics: Total CO₂, CO₂ per Capita, CO₂ per GDP.
4. Exported the structured dataset into Excel.
5. Visualized the data in Tableau using:
   - Maps to display total and per capita emissions by country.
   - Bar charts to show sector-wise contributions.
6. Built an interactive dashboard with filters for year and country.
7. Wrote a PDF policy brief summarizing key insights and recommendations.
Conclusion
Based on the 2023 dataset, the following countries are identified as the top CO₂ emitters by total emissions volume:
•	China
•	United States
•	India
•	Russia
•	Japan
These countries contribute the most to global emissions due to large populations, industrial activity, and energy consumption. This insight helps in targeting key regions for emissions reduction policies.

2nd project:-
Startup Investment Analysis – Shark Tank US Data

Introduction
The "Startup Investment Analysis" project explores entrepreneurial trends and investor behaviors on the reality show Shark Tank US. Using historical pitch data, the goal is to discover which startup industries attract the most funding, what types of founder teams succeed more often, and how gender may influence investment outcomes. This analysis aids in understanding patterns that define success on the show.

Abstract
This project uses real-world data from Shark Tank US to analyze:
Investment patterns by industry
Founder success rates based on gender and team size
Insights into investor behavior and startup valuation
We cleaned, processed, and visualized the data using Python, Excel, and Tableau. The outcome is a visual dashboard showing industry-wise investments and founder patterns, along with summary tables for decision-making insights.

Tools Used
Python (Pandas) – Data cleaning, summarization, CSV export
Excel – Initial data review and formatting
Tableau Public – Dashboard for interactive visualization

Steps Involved in Building the Project
1.Data Loading and Exploration
oLoaded the Shark Tank US dataset using Python
oDisplayed structure, missing values, and key columns
2.Data Cleaning
oHandled missing values in relevant fields
oFocused on key columns: INDUSTRY, GOT_DEAL, PITCHERS_GENDER, MULTIPLE_ENTREPRENEURS, TOTAL_DEAL_AMOUNT
3.Data Analysis
oCreated 3 summary tables:
Industry-wise total investments
Founder gender success rate
Solo vs Team pitch success
4.Exporting for Visualization
oExported summaries as:
industry_summary.csv
gender_success.csv
team_success.csv
5.Dashboard Creation in Tableau
oBuilt 3 charts:
Bar Chart: Total Investment by Industry
Pie/Bar Chart: Success Rate by Founder Gender
Bar Chart: Team vs Solo Founder Success
oArranged charts in an interactive dashboard

Conclusion
The analysis revealed that Food & Beverage, Lifestyle/Home, and Fashion/Beauty industries receive the highest investments. Founders working in teams show a notably higher success rate than solo founders. Also, mixed-gender teams receive more deals than male-only or female-only teams. These insights can help future entrepreneurs understand how to increase their chances of success on Shark Tank.

2nd project files:-
Shark_Tank_us_Dataset_cleaned
Startup investment analysis
analysis.py
gender_success.csv
industry_success.csv
sharktank.twb
team_success.csv
