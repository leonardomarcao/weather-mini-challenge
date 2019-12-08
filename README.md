# Weather Mini Challenge
#### Description
Suppose you live in Ribeirão Preto. Should you take an umbrella?

You tell us!

If the air humidity on a given day is greater than 70%, it is a good idea to take an umbrella with you. Your goal is to fetch the Ribeirão Preto air humidity forecast for the next five days from https://openweathermap.org/api and display the following message template:

You should take an umbrella in these days: ....

For instance, if on the next five days air humidity will be greater than 70% on Monday, Tuesday and Wednesday, you must display the message:

You should take an umbrella in these days: Monday, Tuesday and Wednesday.
## How to Install

1. Create virtual environment
```
    python3.x -m venv venv    
```
2. Enter to created environment
```
    . venv/bin/activate
```
3. Install all requirements
```
    pip install -r requirements.txt
```
4. Create .env file 

Env Example: 
```
api_url=http://api.openweathermap.org/data/2.5
api_key=42d388f8b1db997faaf7dab487f11290
city_name=Ribeirão Preto
country_id=BRA
factor_to_rain=70
message_body=You should take an umbrella in these days:
```
Ps: Dont forget to change api key

#### Output Example

![image](https://app.gitkraken.com/api/glo/boards/5dec34ad57c9d3000fc44f65/attachments/5ded5eb4f01b3f000f17d41d)
