import os
# from matplotlib.pyplot import text
import requests
import json
import pandas as pd

from flask import Flask, request, Response

# constants
TOKEN = ''

## Info about the Bot
#https://api.telegram.org/bot/getMe
#
## get updates
#https://api.telegram.org/bot/getUpdates

## Webhook
#https://api.telegram.org/bot/setWebhook?url=https://fad5663f726005.lhrtunnel.link

## Webhook Heroku
#https://api.telegram.org/bot/setWebhook?url=https://leassis-rossmann-bot.herokuapp.com
#
## send message
# https://api.telegram.org/bot/sendMessage?chat_id=1126325011&text=Hello Leandro! I'm doing great, how about you?


def send_message( chat_id, text ):
	url = 'https://api.telegram.org/bot{}/'.format( TOKEN )
	url = url + 'sendMessage?chat_id={}'.format( chat_id )

	r = requests.post( url, json={'text': text} )
	print( 'Status Code {}'.format(r.status_code) )

	return None

def loading_dataset( store_id ):
	# loading test dataset
	df_test_raw = pd.read_csv( 'test.csv' )
	df_store_raw = pd.read_csv( 'store.csv' )

	# merge test dataset + store
	df_test = pd.merge( df_test_raw, df_store_raw, how='left',on='Store' )

	# choose store for prediction
	df_test = df_test[ df_test['Store'] == store_id ]

	if not df_test.empty:
		# removed closed days
		df_test = df_test[ df_test['Open'] != 0 ]
		df_test = df_test[ ~df_test['Open'].isnull() ]
		df_test = df_test.drop( 'Id', axis = 1 )

		# convert DataFrame to json
		data = json.dumps( df_test.to_dict( orient='records' ) )

	else:
		data = 'error'

	return data

def predict( data ):
	# API Call
	url = 'https://leassis-rossmann-store.herokuapp.com/rossmann/predict'
	header = {'Content-type': 'application/json'}
	data = data

	r = requests.post( url, data=data, headers=header )
	print( 'Status Code {}'.format( r.status_code ) )

	# convert json to dataframe
	d1 = pd.DataFrame( r.json(), columns=r.json()[0].keys() )

	return d1

def parse_message( message ):

	try:
		chat_id = message['message']['chat']['id']
	except:
		chat_id = message['edited_message']['chat']['id']

	try:
		store_id = message['message']['text']
	except:
		store_id = message['edited_message']['text']

	store_id = store_id.replace( '/','' )

	try:
		store_id = int(store_id)

	except ValueError:
		
		if store_id.lower() == 'start':
			msg = 'Welcome to Rossmanns Sales Forecast Bot! Please, type "/" + the store number you want to know the sales forecast.'
			send_message(chat_id, msg)
		
		elif store_id.lower() == 'hi' or store_id.lower() == 'hello':
			send_message(chat_id, 'Hello there! How are you?')
		
		elif store_id.lower() == 'bye':
			send_message(chat_id, 'Bye bye!')
			
		else:
			send_message(chat_id, 'Store ID not typed correctly.')
			
		store_id = 'error'

	return chat_id, store_id


# API initialize
app = Flask( __name__ )

@app.route( '/', methods=['GET','POST'] )

def index():
    if request.method == 'POST':
        message = request.get_json()

        chat_id, store_id = parse_message( message )

        if store_id != 'error':
            # loading data
            data = loading_dataset( store_id )

            if data != 'error':
                # prediction
                d1 = predict(data)

                # calculation
                d2 = d1[['store','prediction']].groupby('store').sum().reset_index()

                # send message
                msg = 'Store number {} will sell R${:,.2f} in the next 6 weeks'.format( d2['store'].values[0], d2['prediction'].values[0] )

                send_message( chat_id, msg )
                return Response( 'Ok', status=200 )

            else:
                send_message( chat_id, 'Sorry, this store is currently not available.')
                return Response( 'Ok', status=200 )
        else:
            return Response( 'Ok', status=200 )

    else:
        return '<h1> Rossmann Telegram BOT by Leandro Destefani. </h1>'

if __name__ == '__main__':
	port = os.environ.get('PORT', 5000)
	app.run( host = '0.0.0.0', port=port)