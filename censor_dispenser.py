# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#print(email_one)

def censor_phrase(input_text, phrase):
  return input_text.replace(phrase, "REDACTED")

#testing function
#print(censor_phrase(email_one, "learning algorithms"))
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her",  "herself", ]

#adds a caped list of each word 
def capitalize_each_word(lst):
    new_lst=[]
    for word in lst:
        new_lst.append(word.capitalize())
    return new_lst

proprietary_terms_add_caps = proprietary_terms + capitalize_each_word(proprietary_terms)

def censor_list_of_words(input_text, lst):
  for word in lst:
    input_text = censor_phrase(input_text, word)
  return input_text

#or this if you dont want to use the first function from email_one
def censor_list_of_words_two(input_text, lst):
    for word in lst:
        input_text = input_text.replace(word, "REDACTED")
    return input_text

#testing out both functions
#print(censor_list_of_words(email_two, proprietary_terms_add_caps))
#print(censor_list_of_words_two(email_two, proprietary_terms_add_caps))

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
negative_words_caped = capitalize_each_word(negative_words)+ negative_words

def censor_negative_words(input_text, negative_list):
    input_text=censor_list_of_words(email_three, proprietary_terms)
    negative_word_count=[]
    for word in negative_list:
        if input_text.find(word) >= 0:
            negative_word_count.append(word)
    if len(negative_word_count) > 2:
        for word in negative_word_count:
          input_text = censor_phrase(input_text, word)
    return input_text

#print(censor_negative_words(email_three, negative_words_caped))

all_words = negative_words_caped+proprietary_terms_add_caps



def censor_all_words(input_text, lst):
    word_list=[]
    for x in input_text.split(" "):
        x1= x.split("\n")
        for word in x1:
            word_list.append(word)
    for i in range(0,len(word_list)):
        checked_word = word_list[i]
        if checked_word in lst:
            word_list[i]= word_list[i].replace(checked_word, "REDACTED")
            word_before=word_list[i-1]
            word_list[i-1]=word_list[i-1].replace(word_before, "REDACTED")
            word_after=word_list[i+1]
            word_list[i+1]=word_list[i+1].replace(word_after, "REDACTED")

    return " ".join(word_list)
    





print(censor_all_words(email_four, all_words))