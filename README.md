# "The Bot that scrapes, the pipeline that moves, the WebPage that presents"

In one sentence: "A Selenium Bot with an integrated Data Pipeline whose process is presented in a localhost webpage"

Timeline:

* Start Date: September 21st, 2022
* Goal: complete full project by March 21st, 2023. (6 months)

Deadlines:

* Selenium Part  - November 5th, 2022 (1.5 months from start date)
* Data Engineering Part - January 21st, 2023 (4 months from start date) Note: learning required.
  * 2.5 months needed from start date to learn Data Engineering
  * 1.5 months needed to implement and use Data Engineering principles to build my data pipeline.
* WebDev Part - March 21st, 2023 (6 months from start date) Note: some learning required.

Project Overview:

1. Selenium Bot will automate "arrive to URL, search for keyword" and scrape data. (Selenium Bot Part)
    * Follow OOP best practices, Selenium Framework and Software Engineering Best Practices.
    * Documentation, testing, virtual env, deployment, DevOps in mind.
2. Data from Bot will get saved in a temp csv file or temp table, depending on Data Engineering best practices.
3. Data pipeline created to perform data transformation, cleaning steps before data is injected into PostgreSQL DB. (Data Engineering Part)
4. Create LocalHost webpage to present project. (WebDev part)
    * visually show the process.
    * overview of project structure and explain the why?
    * present the various tools, modules, frameworks, "present your project" section.
    * HTML and CSS - Log Process and Run's.
    * animate Data Pipeline process on localhost webpage.

## Selenium

For this project, we will be using Selenium to automate web-scrapping and keyword searching on [carmax](https://www.carmax.com/).

The Bot's process will be:

1. Arrive to carmax.com
2. Gather information:
    * What is my store location?
3. Enter "Honda" in the search box and select "Honda Accord" from the list of options.
4. Apply "Year" filter for years from 2019 to 2023.
5. Gather Information:
    * Summary sentence of search results.
    * Number of matches
6. See if we can view all results or if we need a "more_results?" function that will click on "See More Matches" button if found < number_of_matches.
7. For each result:
    * Save Year, Make and Model
    * Save Price
    * Save mileage
    * Save shipping information
8. Save results into a Pandas DataFrame
9. Email notification for both failed and completed runs.
