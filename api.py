import requests
def currency_converter(amount, source_currency, target_currency):
 source_currency = source_currency.upper()
 target_currency = target_currency.upper()

 url=(f"https://v6.exchangerate-api.com/v6/ea74f9a0815a64d670fc5530/latest/{source_currency}")
 response=requests.get(url)
 sucess=response.status_code
 data=response.json()
 
 if sucess == 200 :
    if target_currency in data["conversion_rates"]:
        rate = data["conversion_rates"][target_currency]
        converted_amount = amount * rate
        print(f"{amount} {source_currency} = {converted_amount:.2f} {target_currency}")
    else:
        print("Enter correct Target Currency!!")
 else:
    print("API is not work properly!!")

while True:
   src=input("Enter your Source_Currency(or 'exit' to quit): ").upper()
   if src == 'EXIT':
      print("Thank you for using the Currency Converter!")
      break
   amt=int(input("Enter the Amount: "))
   trc=input("Enter target currency: ").upper()
   currency_converter(amt,src,trc)
