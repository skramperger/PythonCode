#Functions to decode and encode messages using keywords or offset-values
#Project from Coded Correspondence

#Stuff to fix
#---Capitalization

#Stuff to implement:
#---Input field for messages to decode using input()
#---Dictionary to automatically detect language
#---Include datetime for updatetimes

#Last updated: 23.05.2022



message_to_decode = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
message_to_encode = "you were able to decode this? nice work! you are becoming quite the expert at crytography!"
keyword = "friends"

alphabet = "abcdefghijklmnopqrstuvwxyz"
cap_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def keyword_decoder(message, keyword = "friends"):
    decoded_message = ""
    keyword_value = 0
    keyword_index = 0
    keyword_letter = ""

    for letter in message:
        if letter not in alphabet and letter not in cap_alphabet:
            decoded_message += letter
        else:
            if letter in alphabet:
                keyword_letter = keyword[keyword_index]
                keyword_value = alphabet.find(keyword_letter)
                letter_value = alphabet.find(letter)
                decoded_message += alphabet[(letter_value -keyword_value) % 26]

                if keyword_index > 5:
                    keyword_index = 0
                else:
                    keyword_index += 1
    return decoded_message



def keyword_encoder(message, keyword = "friends"):
    encoded_message = ""
    keyword_letter = ""
    keyword_value = 0
    letter_value = 0

    for letter in message:

        if letter in alphabet:
            letter_value = alphabet.find(letter)
            keyword_letter = keyword[keyword_value]
            encoded_message += alphabet[(letter_value + alphabet.find(keyword_letter)) % 26]
            if keyword_value > int(len(keyword)) - 2:
                keyword_value = 0
            else:
                keyword_value += 1
        else:
            encoded_message += letter
            
    return encoded_message    
    
#second parameter would allow a word with which the message letters would be offset (default is "friends")
print(keyword_encoder(message_to_encode, ))
print(keyword_decoder(message_to_decode, ))
