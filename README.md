# Description

This application performs simple calculations by running python in the browser; it works offline once cached. 

## Tools and workflow

- [pyscript](https://github.com/pyscript/pyscript) runs a bare-bones Python interpreter (Pyodide) in the browser.
- A set of python methods make calculations and parse results in HTML format.
- Two [service workers](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Tutorials/js13kGames/Offline_Service_workers) cache app dependencies for offline operation. 
- A set of scripts handles pages navigation and input formatting with vanilla Javascript. 


## Usage

- Run `npm run dev` ( or `python3 -m http.server -d ./public/`) to find the app running at `http://localhost:8000`.