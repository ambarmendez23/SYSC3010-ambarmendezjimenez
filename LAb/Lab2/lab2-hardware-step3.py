def read_data_thingspeak():
	RL='https://thingspeak.com/channels/1161238/api_keys'
	KEY= '4UIUHDQEJ8VJJI5C'
	HEADER= '&results=2'
	NEW_URL= URL+KEY+HEADER
	print(NEW_URL)

	get_data=requests.get(NEW_URL).json()
	print(get_data)
	channel_ide=get_data('channel')('id')

	feild_l=get_data('feeds')
	print(feild_I)

	t=()
	for x in feild_1:
		print(x('field1'))
		t.append(x('field'))
		print(t)
	
if__name__== '__main__':
	thingspeak_post()
	read_data_thingspeak()
