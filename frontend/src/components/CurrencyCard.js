const CurrencyCard = async () => {
  let res = await fetch('http://127.0.0.1:8000/currency/USD')
    .then(response => response.json())
  console.log(res)
  return <div>
    {res.name}
  </div>
}

export default CurrencyCard