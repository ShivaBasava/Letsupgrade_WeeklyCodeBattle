'''
Solution to WEEKLY CODE BATTLE - WEEK 13

NOTE: This 'app.py' file, contains the following-
        1] Solution:- To the WEEKLY CODE BATTLE:- WEEK 13, A Language Translator.
        2] Code & Explaination:- to the written code, line-by-line as comments.
        3] Example Output

1] Solution-
    a] We have made use of 'googletrans' library a Google API Language Translator for Python.
       Command to install this, 
            pip install googletrans
    b] From 'googletrans' library we are importing the Class 'Translator'.
    c] We have created a Class name 'langTranslate', So that it can be reused.
    d] Inside this Class, we have defined two methods- langCode() and translateSentence().
    e] Method langCode() - Defined for handing the Menu and returning the respective Language Code.
    f] Method translateSentence() - Defined for translating the Sentence to respective language by making use of
       previous steps data(i.e, Language code).

2] Code & Explaination-
'''

#importing the Class module 'Translator' from 'googletrans library
from googletrans import Translator

#Creating a Class 'langTranslate'
class langTranslate():

    #This method of Class 'langTranslate', returns the language code.
    def langCode(self):
        print("""\nTo translate, Select the respective number from following menu,\n[ Example- To convert the entered scentance to Serbian, select 2 ]
            1. English
            2. Serbian
            3. Spanish""")
        strNumber = input()
        # We are maintaining a Dictonary (tempLangCode) for Lanugage code for selected number from the console
        tempLangCode = {'1': 'en','2': 'sr','3': 'es'}
        #Checking whether we have the respective number associated with Language code
        if strNumber in tempLangCode:
            #Returning the respective Language code
            return tempLangCode[strNumber]
        else:
            #If user enters other number apart from the numbers in Dictonary (tempLangCode)
            print("Please restart program and select available number from menu!!")
            exit()

    #This method of Class 'langTranslate', It'll accept two parameters - Language code 'toLang' and Sentence to be translated
    #returns the sentence after translation.
    def translateSentence(self, strSentence, strTolang):
        self.strString = strSentence
        self.strTolang = strTolang
        #Creating an Object 'translator', assigning a Class Translator() to it.
        translator = Translator()
        translation = translator.translate(self.strString, dest=self.strTolang)
        return (str(translation.text))

#Program Execution starts from here
if __name__ == "__main__":
    #Embedding the login inside the try-catch block
    try:
        #To get the sentance to be translated
        sentence = input("Enter your sentence to translate:\n")
        # Creating an Object 'objLang' of Class 'langTranslate'
        objLang = langTranslate()
        #Now we are calling Method langCode() to get the Input from the user
        toLang = objLang.langCode()
        #Pass the Language code 'toLang' and sentence to be translated to Method - translateSentence()
        strTranslatedText = objLang.translateSentence(sentence,toLang)
        print("\n{}".format(strTranslatedText))
    except Exception as e:
        print(e)

'''
3] Example Output:

a] Run the following command in the terminal,
    python3 app.py
b] Following are the series of interactive output.

Enter your sentence to translate:
Letsupgrade is Awesome <3 !!!

To translate, Select the respective number from following menu,
[ Example- To convert the entered scentance to Serbian, select 2 ]
            1. English
            2. Serbian
            3. Spanish
2

ЛетсУпграде је сјајан <3 !!!

'''