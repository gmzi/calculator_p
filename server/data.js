const express = require('express')

const app = express()
const port = '3000'

app.get('/server/data', async (req, res) => {
  try {
    function filterData(data){
      const result = data.map((item) => ({
        cusip: item.cusip,
        issueDate: item.issueDate.substring(0, 10),
        highDiscountRate: item.highDiscountRate, 
        pricePer100: item.pricePer100,
        securityTermDayMonth: item.securityTermDayMonth
      }))
      return result
    }

    function getCurrentDate() {
      const currentDate = new Date();
      const month = String(currentDate.getMonth() + 1).padStart(2, '0'); // Adding 1 to month as it's zero-based
      const day = String(currentDate.getDate()).padStart(2, '0');
      const year = currentDate.getFullYear();
      return `${month}/${day}/${year}`;
    }

    const weeks = req.query.weeks
    if (!weeks){
      return res.status(400).json({error: "weeks parameter missing"})
    }

    const matcher = `${weeks}-Week`
    const currentDate = getCurrentDate();
    // const API_URL = "https://www.treasurydirect.gov/TA_WS/securities/auctioned?format=json&type=Bill"
    // const API_URL = `https://www.treasurydirect.gov/TA_WS/securities/search?type=Bill&securityTerm=${matcher}&format=json&pagenum=1&pagesize=100&reverse=true`
    // const API_URL = `https://www.treasurydirect.gov/TA_WS/securities/search?type=Bill&securityTerm=${matcher}&format=json&startDate=01/01/2015&endDate=${currentDate}&reverse=true`
    const API_URL = `https://www.treasurydirect.gov/TA_WS/securities/search?type=Bill&securityTerm=${matcher}&format=json&startDate=01/01/2015&endDate=${currentDate}`
    const API_NO_PAGESIZE = `https://www.treasurydirect.gov/TA_WS/securities/search?type=Bill&securityTerm=${matcher}&format=json&reverse=true`
    const response = await fetch(API_URL);
    const data = await response.json();
    // when results count under pagesize is empty array, so try a query without filters:
    if (!data.length){
      const resNoPageSize = await fetch(API_NO_PAGESIZE);
      const dataNoPageSize = await resNoPageSize.json();
      const resultData = filterData(dataNoPageSize)
      res.json(resultData)
      return;
    }

    const resultData = filterData(data)
    res.json(resultData)
  } catch (error) {
    console.error('Error fetching data:', error);
    res.status(500).json({error: error})
  }
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})