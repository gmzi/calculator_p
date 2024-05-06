# RUN


- Run python client:
    - `python3 -m http.server -d ./public/`
- Run from script: 
    - `npm run dev`

- server folder: calculator_server

- There are ./run.sh and ./stop.sh, backup in case we need to implement a local server. 

- To list files on folder, find ./public/listFiles.sh


Ports: 
- `http://localhost:8000` frontend.

## Development
Tackle tasks in this order from top to bottom:

- Nav active link color underline not working on prod version but working it localhost. Fix it. 
- Fix layout for mobile. (label and input as column in small screens, as row in larger. It's a media query I erased I think.)
- Add icons.
- Make an open source version:
    1. Implement mock data instead of fetching to TreasuryDirect. 
    2. Create new repo and make it public. 
    3. Tag pyscript, python, service workers. 
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