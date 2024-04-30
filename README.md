# RUN


- Run python client:
    - `python3 -m http.server -d ./public/`
- Run node server: 
    - `node ./server/data.js`
- Run from script: 
    - `npm run dev`
- Stop:
    - `npm run stop`

Ports: 
- `http://localhost:8000` frontend.
- `http://localhost:3000/server/data` data api.

## Development

- Remember this tool must be super dumb, very simple functions that perform very simple tasks, because this tool is a complement to other tools, for now my treasuries spreadsheet only, but I'm sure it will get more complex. But all the complexities and hypothesis drafting will be handled in spreadsheets, that seem to be super handy and the bes tool to handle treasuries, this tool has to handle these 3 very simple things:
1. Calculate interest to be accrued. 
2. Calculate dates of maturity. 
3. Display things in a calendar?

That's it. It can show all the information together or splitted, but that's all. 


Tackle tasks in this order from top to bottom:

- A "security filter" endpoint. You can select 4, 8, 26, etc. week security. The page will fetch TD API, bring auction history, loop over the data and extract your selected type of security and display the "high rate", price, etc, So you can check auction results for one type of bill instead of having to go through all of them or having to download the .csv file and process it. 
This is the API endpoint to fetch: https://www.treasurydirect.gov/TA_WS/securities/auctioned?format=json&type=Bill
If it's not too heavy, displaying a graphic would be cool, but not necessary. If there's no internet connection just return a warning and suspend the whole process, that's all there is, so it won't brake the app offline.
Implementation: try a node express server route. If it doesn't work, use a cloudflare worker.
- add a separate maturity date calculator (display a calendar, pick a date and a time span, and the calculator will show you maturity highlighted in the calendar. You can then click on the new date, set a new term, and will do it again so you can handle reinvestmentes in a super dumb and useful way. )
- Implement workers for offline operation. Here are the docs:
    - [master docs](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Offline_and_background_operation)
    - more mozilla resources on safari reading list. 
- Implement calendars:  
    - PUT A CALENDAR SOMEWHERE, WITH COLORS FOR AUCTIONS AND ISSUANCE DATES, WHEN YOU CLICK ON AN ISSUANCE DATE IT WILL COLOR ALL DAYS UNTIL MATURITY.
    - Add a calendar with all my maturity dates highlighted and a list of them.
- Take the workers approach to FIXIE app. Is it viable to wrap the whole thing with a worker, would Java work? Goes without saying that will have to use Pyodide instead of mocripython. Maybe there's a java extension there or something, do some research, but don't get too carried over. 

## Goals and constraints

- It should run on a browser, 
- It should work offline. 
- It should be installable accross platforms, desktop and mobile, and specially mobile. 
- It has to be downloadable as a bookmark in any device. 
- Features: find calculators and its functions in Desktop/rates_calculator + Percentage calculator (if it’s not too hard to build, else link to the existing one). 
- Approach 1: Run python in the browser. 
- Approach 2: run frontend in javascript/rect and backend in python. 
- Tools to explore: 
	- https://blog.cloudflare.com/python-workers?utm_source=tldrnewsletter
	- https://pyscript.net.
	- https://github.com/piercefreeman/mountaineer
    - micropython (implemented as interpreter from pyscript). 
- Should perform NUMERIC calculations and derivations (interest rates, price, yield, percentage, etc.).
- Should perform TIME calculations (maturity dates, month spans, days amounts, days of inactivity between auction and issuance).
- Should display time calculations as a calendar and as a list. 
- Should support calendar interactions (mark issue date in red, get maturity date in blue and days highlighted). 
- Hypothetic scenarios. 
    - Create a Reinvestments calculator, that takes original price, hypothetic reinvestmen price. Reuse maturity dates and number of reinvestments logic.  Sum up the separate results, display the sum along with the maturity after reinvestments date. 

# APIs and docs

## Search by CUSIP

Ways to look up a Treasury security by CUSIP number: 
1. [TD website](https://www.treasurydirect.gov/auctions/auction-query/)
2. [TD API request](https://www.treasurydirect.gov/TA_WS/securities/search?cusip=912810TJ7&format=json)
3. [TD API docs](https://www.treasurydirect.gov/legal-information/developers/web-api-security/)