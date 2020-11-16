import random

outputFile = open("./train_data.txt",'w')
outputFile.write('version: "2.0"\n nlu:\n')

def checkout_data():
	outputFile.write('intent:faq_checkout\n')
	outputFile.write('examples:\n')
	filepath = './checkout.txt'

	with open(filepath,'r',encoding = 'utf-8') as infile:
    	sents = infile.read().strip().split('\n')

    for sent in sents:
    	sent = sent.replace("[check-out]",  "[check-in]")
    	outputFile.write(sent+'\n')

    for sent in sents:
    	sent = sent.lower()
    	outputFile.write(sent)



def cancel_data():
	outputFile.write('intent:cancel_rules\n')
	outputFile.write('examples:\n')
	filepath = './cancel.txt'

	with open(filepath,'r',encoding = 'utf-8') as infile:
    	sents = infile.read().strip().split('\n')

    for sent in sents:
    	sent = sent.lower()
    	outputFile.write(sent)



def room_booking_data():
	outputFile.write('intent:room_booking\n')
	outputFile.write('examples:\n')
	filepath = './room_booking.txt'

	with open(filepath,'r',encoding = 'utf-8') as infile:
    	sents = infile.read().strip().split('\n')

    for sent in sents:
		if "[room_numbers]" in sent:
			room_numbers= random.randrange(1, 100, 3)
			sent = sent.replace("[room_numbers]", '[' + room_numbers + ']')

		if "[room_type]" in sent:
			room_numbers= random.randrange(1, 100, 3)
			sent = sent.replace("[room_type]",  '[super rooms]')
		sent = sent.lower()
    	outputFile.write(sent+'\n')

    for sent in sents:
		if "[room_numbers]" in sent:
			room_numbers= random.randrange(1, 100, 3)
			sent = sent.replace("[room_numbers]",  '[' + room_numbers + ']')

		if "[room_type]" in sent:
			room_numbers= random.randrange(1, 100, 3)
			sent = sent.replace("[room_type]",  '[deluxe rooms]')
		sent = sent.lower()
    	outputFile.write(sent+'\n')



def clean_room_now_data():
	outputFile.write('intent:clean_room_now\n')
	outputFile.write('examples:\n')
	filepath = './clean_room_now.txt'

	with open(filepath,'r',encoding = 'utf-8') as infile:
    	sents = infile.read().strip().split('\n')

    for sent in sents:
    	sent = sent.lower()
    	outputFile.write(sent)

def clean_room():
	outputFile.write('intent:clean_room\n')
	outputFile.write('examples:\n')
	filepath = './clean_room.txt'

	with open(filepath,'r',encoding = 'utf-8') as infile:
    	sents = infile.read().strip().split('\n')

    for sent in sents:
    	if "[time]" in sent:
			time= '[' + random.randrange(1, 13, 3) + ':' + random.randrange(1, 60, 3) + 'am' + ']'
			sent = sent.replace("[time]",  time)
    	sent = sent.lower()
    	outputFile.write(sent)

    for sent in sents:
    	if "[time]" in sent:
			time= '[' + random.randrange(1, 13, 3) + 'pm' + ']'
			sent = sent.replace("[time]",  time)
    	sent = sent.lower()
    	outputFile.write(sent)


checkout_data()
cancel_data()
room_booking_data()
clean_room_now_data()
clean_room()