async function fetchResults() {
    const weeksInput = document.getElementById('weeks-to-fetch').value

    if (!navigator.onLine) {
        alert('you need an internet connection to use this feature')
        return
    }

    try {
        const response = await fetch(
            `https://calpy-server.vercel.app/api?weeks=${weeksInput}`
        )
        const data = await response.json()
        displayResults(data)
        return
    } catch (error) {
        console.error('Error fetching data:', error)
    }
}

function displayResults(filteredData) {
    const resultsGrid = document.getElementById('resultsGrid')
    resultsGrid.innerHTML = ''

    if (filteredData.length === 0) {
        resultsGrid.innerHTML = '<p>No results found.</p>'
    } else {
        const tableContainer = document.createElement('div')
        tableContainer.setAttribute(
            'style',
            'display: grid; grid-template-columns: auto auto;'
        )
        tableContainer.classList.add('grid')
        const table = document.createElement('table')
        const headerRow = table.insertRow()
        headerRow.innerHTML = `<th>High rate</th>
        <th>issue date</th>
        <th>Price per 100</th>
        <th>term day month</th>
        <th>cusip</th>
        `

        filteredData.forEach(item => {
            const row = table.insertRow()
            row.innerHTML = `<td>${parseFloat(item.highDiscountRate).toFixed(3) || '-'
                }</td>
        <td>${item.issueDate.substring(0, 10)}</td>
        <td>${item.pricePer100}</td>
        <td>${item.securityTermDayMonth}</td>
        <td>${item.cusip}</td>
        `
        })
        tableContainer.appendChild(table)
        resultsGrid.appendChild(tableContainer)
    }
}