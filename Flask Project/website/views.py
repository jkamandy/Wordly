from flask import Blueprint, render_template, request
from PyDictionary import PyDictionary
from random import shuffle


import requests
from bs4 import BeautifulSoup

def synonyms(term):
    response = requests.get('https://www.thesaurus.com/browse/{}'.format(term))
    soup = BeautifulSoup(response.text, 'html.parser')
    soup.find('section', {'class': 'css-191l5o0-ClassicContentCard e1qo4u830'})
    return [span.text for span in soup.findAll('a', {'class': 'css-1kg1yv8 eh475bn0'})] 

views1 = Blueprint('views', __name__)
#BluePrint stores URLS
user = ''

@views1.route('/')
def home():
    print('home')
    return render_template("home.html")

# @views1.route('/', methods = ['POST', 'GET'])
# def my_form_post():
#     print('in nedw')
#     text = request.form('user_word')
#     processed_text = text.upper()
#     print(processed_text)
#     return processed_text

@views1.route('/find-word')
def success():
    return render_template("findword.html")

'''Login redirects to success which renders the findword template '''
'''Base html's form button redirects to /login b/c thats the link for the action.
Inside login, it handles the POST/GET of user's word, prints it to console, and returns findword.html.
This is a new page that shows resulting words. findwords.html include a {{word}} that uses
the passed 'word' from the render_template argument (really handy). -- i will need to pass a dictionary
of the words to be able to display up to 3 words. 
'''
@views1.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        print('post')
        masjid_group = {'yosuf':['Master-coder', 'NK786', 'bosuf', 'Destiny-Legend'], 
                        'rameen':['Banjan-rameen', 'Einshtein', 'Ritler', 'manny', 'Maher'], 
                        'arash':['Yollama26', 'Chungie', 'Arash Norway', 'Llama-King'], 
                        'seeyam':['Master-of-everything', 'NovaSeeq', 'Master-shifu', 'Yours-Truly'], 
                        'sameer':['Lady-killer', 'Novasamq', 'xxliljoe123xx', '5-piece-wings', 'Hussein-Charara'], 
                        'kumail':['Dictator', 'President-Von-Afshar', 'Mufti-Menk'],
                        'elias':['Italian', 'Mini-Cooper-Owner', 'Ex-Chipotle', 'Swagger-Pack'], 
                        'yoseph':['Future-actor', 'CIA-agent?', 'Marvel-superhero', 'Yoseph-Attaii-Afzali'], 
                        'harris':['Rat', 'Beautiful', 'AWARHRHAW'],
                        'zaid':['Zaido', 'Little-bro', 'Biologist'], 
                        'aligull':['Maggi', 'Best-at-fortnite', 'sexy'],
                        'arshia':['Daddy', "Coach's-son", 'Mazda-Miniata'], 
                        'milad':['Jametrious', 'is-it-bussin?', 'jit-trippin', 'folk-trippin', 'left-nut'],
                        'elyas':['Big-E', 'Mark-Henry', '315-bench', 'strongest-man-alive'],
                        'mursal':['Gong-Yoo', 'Sarah', 'Morsal'],
                        'aliyah':['Bahar', 'Naruto', 'Kukh']
                        }
        user = request.form['nm'].lower()
        if user in masjid_group:
            shuffle(masjid_group[user])
            return render_template("findword.html", word = masjid_group[user])
        else:
            dictionary = PyDictionary()
            print(dictionary.synonym('word'))
            print(user)
            word_list = synonyms(user)
            shuffle(word_list)
            
            print(word_list)
            return render_template("findword.html", word = word_list)
            #return redirect(url_for('views1.success',userword = user))
            #return success(user)
    else:
        user = request.args.get('nm')
        print(user)
        return render_template("findword.html", word = word_list)
        #return redirect(url_for('views1.success',userword = user))
        #return success(user)

# @views1.route('/test', methods = ['POST', 'GET'])
# def test():
#     print('wefwe')
#     print(request.method)
#     global user
#     user = request.args.get('user_word')
#     print(user)
#     if request.method == 'POST':
#         #version 1:
#         opt1 = request.form.to_dict()
#         print('op1', opt1)
#         for key in opt1:
#             if key == "user_word":
#                 string = opt1[key]
#         print(string)
#
#         return "success"
#     else :
#        return render_template("home.html")