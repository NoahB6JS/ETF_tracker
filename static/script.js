const lastPrices = {};

async function fetchPrices() {
    try {
        const res = await fetch("/prices");
        const data = await res.json();

        for (const stock in data) {
            const div = document.getElementById(stock);
            if (div) {
                const priceEl = div.querySelector(".price");
                let price = data[stock] || lastPrices[stock] || 0.0;
                priceEl.innerText = `$${price.toFixed(2)}`;
                lastPrices[stock] = price;
            }
        }
    } catch (err) {
        console.log("Error fetching prices:", err);
    }
}

fetchPrices();
setInterval(fetchPrices, 5000);