import unittest
from unittest.mock import patch
from io import StringIO
from functions import *

class TestCode(unittest.TestCase):
    #ex-01-01.py    
    def test_hello_world(self):
        self.assertEqual(hello_world(),"Hello World!")

    #ex-01-02.py    
    def test_hello_my_friend(self):
        self.assertEqual(hello_my_friend("Anne").lower(),"Hello Anne".lower())
        self.assertEqual(hello_my_friend("Jon").lower(),"Hello Jon".lower())
        self.assertEqual(hello_my_friend("Katixa").lower(),"Hello Katixa".lower())
        
    #ex-01-03.py    
    def test_next_number(self):
        self.assertEqual(next_number(1),2)
        self.assertEqual(next_number(11),12)
        #def test_next_number_neg(self):
        self.assertEqual(next_number(-11),-10)
        self.assertEqual(next_number(-2),-1)
        #def test_next_number_zero(self):
        self.assertEqual(next_number(-1),0)
        self.assertEqual(next_number(0),1)

    #ex-01-04.py    
    def test_year_of_birth(self):
        self.assertEqual(year_of_birth(34),1987)
        self.assertEqual(year_of_birth(30),1991)
        self.assertEqual(year_of_birth(4),2017)
        self.assertEqual(year_of_birth(0),2021)

    #ex-01-05.py    
    def test_degree_calculator(self):
        self.assertEqual(degree_calculator(0),32)
        #def test_degree_calculator_pos(self):
        self.assertEqual(degree_calculator(55),131)
        self.assertEqual(degree_calculator(20),68)
        self.assertEqual(degree_calculator(1),33.8)
        #def test_degree_calculator_neg(self):
        self.assertEqual(degree_calculator(-5),23)
        self.assertEqual(degree_calculator(-1),30.2)
        self.assertEqual(degree_calculator(-55),-67)

    #ex-01-06.py    
    def test_password(self):
        self.assertEqual(password("kukuakEgitenDuKuku").lower(),"Access allowed".lower())   
        #def test_password_deni(self):
        self.assertEqual(password("helloFriend").lower(),"Access denied".lower())
        self.assertEqual(password("kukuakEgitenDuKuk").lower(),"Access denied".lower())
        self.assertEqual(password("kukuakegitendukuku").lower(),"Access denied".lower())
        self.assertEqual(password("KUKUAKEGITENDUKUKU").lower(),"Access denied".lower())
        self.assertEqual(password("").lower(),"Access denied".lower())

    #ex-01-07.py    
    def test_is_positive(self):
        self.assertEqual(is_positive(5).lower(),"The number entered is positive".lower())
        self.assertEqual(is_positive(0).lower(),"The number entered is positive".lower())
        self.assertEqual(is_positive(999).lower(),"The number entered is positive".lower())
        #def test_is_positive_false(self):
        self.assertEqual(is_positive(-5).lower(),"The number entered is not positive".lower())
        self.assertEqual(is_positive(-555).lower(),"The number entered is not positive".lower())
        self.assertEqual(is_positive(-5999).lower(),"The number entered is not positive".lower())

    #ex-01-08.py    
    def test_positive_and_even(self):
        self.assertEqual(positive_and_even(2).lower(),"The number entered is positive and even".lower())
        self.assertEqual(positive_and_even(0).lower(),"The number entered is positive and even".lower())
        self.assertEqual(positive_and_even(1000).lower(),"The number entered is positive and even".lower())
        #def test_positive_and_even_odd(self):
        self.assertEqual(positive_and_even(5).lower(),"The number entered is positive and odd".lower())
        self.assertEqual(positive_and_even(11).lower(),"The number entered is positive and odd".lower())
        self.assertEqual(positive_and_even(999).lower(),"The number entered is positive and odd".lower())
        #def test_positive_and_even_false(self):
        self.assertEqual(positive_and_even(-5).lower(),"The number entered is not positive".lower())
        self.assertEqual(positive_and_even(-555).lower(),"The number entered is not positive".lower())
        self.assertEqual(positive_and_even(-5999).lower(),"The number entered is not positive".lower())

    #ex-01-09.py    
    def test_inhabitants(self):
        self.assertEqual(inhabitants("Donostia").lower(),"Hello Donostiarra!".lower())
        #def test_inhabitants_Sydney(self):
        self.assertEqual(inhabitants("Sydney").lower(),"Hello Sydneyite!".lower())
        #def test_inhabitants_Istanbul(self):
        self.assertEqual(inhabitants("Istanbul").lower(),"Hello Istanbulite!".lower())
        #def test_inhabitants_Sydney(self):
        self.assertEqual(inhabitants("Sydney").lower(),"Hello Sydneyite!".lower())
        #def test_inhabitants_Unknown(self):
        self.assertEqual(inhabitants("Azpeitia").lower().replace(",",""),"I'm sorry, I don't know your town...".lower().replace(",",""))
        self.assertEqual(inhabitants("Istambul").lower().replace(",",""),"I'm sorry, I don't know your town...".lower().replace(",",""))
        self.assertEqual(inhabitants("Donosti").lower().replace(",",""),"I'm sorry, I don't know your town...".lower().replace(",",""))
        self.assertEqual(inhabitants("Sidney").lower().replace(",",""),"I'm sorry, I don't know your town...".lower().replace(",",""))
        self.assertEqual(inhabitants("").lower().replace(",",""),"I'm sorry, I don't know your town...".lower().replace(",",""))

    #ex-01-10.py    
    def test_transportation(self):
        self.assertEqual(transportation("yes",-1),"Better to go by bus.")
        self.assertEqual(transportation("no",11),"Better to go by bus.")
        #def test_transportation_bike(self):
        self.assertEqual(transportation("no",2),"Better to ride a bike.")
        self.assertEqual(transportation("no",8),"Better to ride a bike.")
        self.assertEqual(transportation("no",5),"Better to ride a bike.")
        #def test_transportation_walk(self):
        self.assertEqual(transportation("no",1),"Better to walk.")
        self.assertEqual(transportation("no",0),"Better to walk.")


    ####################
    ######2 LOOPS#######
    ####################

    #ex-02-01.py
    def test_first_and_last_characters(self):
        self.assertEqual(first_and_last_characters("Home"),"First character: H\nLast character: e")
        #def test_first_and_last_character_elephant(self):
        self.assertEqual(first_and_last_characters("elephant"),"First character: e\nLast character: t")
        #def test_first_and_last_character_ELEPHANT(self):
        self.assertEqual(first_and_last_characters("ELEPHANT"),"First character: E\nLast character: T")
        #def test_first_and_last_character_elephan(self):
        self.assertEqual(first_and_last_characters("elephan"),"First character: e\nLast character: n")

    #ex-02-02.py
    def test_cheerleader(self):
        self.assertEqual(cheerleader("baskonia").lower(),"Give me a(n) b, b!\nGive me a(n) a, a!\nGive me a(n) s, s!\nGive me a(n) k, k!\nGive me a(n) o, o!\nGive me a(n) n, n!\nGive me a(n) i, i!\nGive me a(n) a, a!\nWhat's that spell?\nbaskonia! baskonia!".lower())
        #def test_cheerleader_osasuna(self):
        self.assertEqual(cheerleader("osasuna").lower(),"Give me a(n) o, o!\nGive me a(n) s, s!\nGive me a(n) a, a!\nGive me a(n) s, s!\nGive me a(n) u, u!\nGive me a(n) n, n!\nGive me a(n) a, a!\nWhat's that spell?\nosasuna! osasuna!".lower())
        #def test_cheerleader_alaves(self):
        self.assertEqual(cheerleader("alaves").lower(),"Give me a(n) a, a!\nGive me a(n) l, l!\nGive me a(n) a, a!\nGive me a(n) v, v!\nGive me a(n) e, e!\nGive me a(n) s, s!\nWhat's that spell?\nalaves! alaves!".lower())

    #ex-02-03.py
    def test_counter(self):
        self.assertEqual(counter(5).strip(),"0\n1\n2\n3\n4\n5")
        #def test_counter_0(self):
        self.assertEqual(counter(0).strip(),"0")
        #def test_counter_1(self):
        self.assertEqual(counter(1).strip(),"0\n1")
        #def test_counter_15(self):
        self.assertEqual(counter(15).strip(),"0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15")
    
    #ex-02-04.py
    def test_lift_only_up(self):
        self.assertEqual(lift_only_up(3,6).strip(),"Floor number: 3\nFloor number: 4\nFloor number: 5\nFloor number: 6")
        #def test_lift_only_up_0_2(self):
        self.assertEqual(lift_only_up(0,2).strip(),"Floor number: 0\nFloor number: 1\nFloor number: 2")
        #def test_lift_only_up_0_1(self):
        self.assertEqual(lift_only_up(0,1).strip(),"Floor number: 0\nFloor number: 1")
        #def test_lift_only_up_minus3_6(self):
        self.assertEqual(lift_only_up(-3,6).strip(),"Floor number: -3\nFloor number: -2\nFloor number: -1\nFloor number: 0\nFloor number: 1\nFloor number: 2\nFloor number: 3\nFloor number: 4\nFloor number: 5\nFloor number: 6")

    #ex-02-05.py
    def test_lift_up_and_down(self):
        self.assertEqual(lift_up_and_down(3,6).strip(),"Floor number: 3\nFloor number: 4\nFloor number: 5\nFloor number: 6")
        #def test_lift_up_and_down_0_2(self):
        self.assertEqual(lift_up_and_down(0,2).strip(),"Floor number: 0\nFloor number: 1\nFloor number: 2")
        #def test_lift_up_and_down_0_1(self):
        self.assertEqual(lift_up_and_down(0,1).strip(),"Floor number: 0\nFloor number: 1")
        #def test_lift_up_and_down_minus3_6(self):
        self.assertEqual(lift_up_and_down(-3,6).strip(),"Floor number: -3\nFloor number: -2\nFloor number: -1\nFloor number: 0\nFloor number: 1\nFloor number: 2\nFloor number: 3\nFloor number: 4\nFloor number: 5\nFloor number: 6")
        #def test_lift_up_and_down_6_3(self):
        self.assertEqual(lift_up_and_down(6,3).strip(),"Floor number: 6\nFloor number: 5\nFloor number: 4\nFloor number: 3")
        #def test_lift_up_and_down_2_0(self):
        self.assertEqual(lift_up_and_down(2,0).strip(),"Floor number: 2\nFloor number: 1\nFloor number: 0")
        #def test_lift_up_and_down_1_0(self):
        self.assertEqual(lift_up_and_down(1,0).strip(),"Floor number: 1\nFloor number: 0")
        #def test_lift_up_and_down_6_minus3(self):
        self.assertEqual(lift_up_and_down(6,-3).strip(),"Floor number: 6\nFloor number: 5\nFloor number: 4\nFloor number: 3\nFloor number: 2\nFloor number: 1\nFloor number: 0\nFloor number: -1\nFloor number: -2\nFloor number: -3")

    #ex-02-06.py
    def test_double_factorial(self):
        self.assertEqual(double_factorial(9),945)
        #def test_double_factorial_10(self):
        self.assertEqual(double_factorial(10),3840)
        #def test_double_factorial_0(self):
        self.assertEqual(double_factorial(0),1)
        #def test_double_factorial_1(self):
        self.assertEqual(double_factorial(1),1)
        #def test_double_factorial_5(self):
        self.assertEqual(double_factorial(5),15)

    #ex-02-07.py
    def test_lift_with_while(self):
        self.assertEqual(lift_with_while(3,6),"Floor number: 3\nFloor number: 4\nFloor number: 5\nFloor number: 6")
        #def test_lift_with_while_0_2(self):
        self.assertEqual(lift_with_while(0,2).strip(),"Floor number: 0\nFloor number: 1\nFloor number: 2")
        #def test_lift_with_whilen_0_1(self):
        self.assertEqual(lift_with_while(0,1).strip(),"Floor number: 0\nFloor number: 1")
        #def test_lift_with_while_minus3_6(self):
        self.assertEqual(lift_with_while(-3,6).strip(),"Floor number: -3\nFloor number: -2\nFloor number: -1\nFloor number: 0\nFloor number: 1\nFloor number: 2\nFloor number: 3\nFloor number: 4\nFloor number: 5\nFloor number: 6")
        #def test_lift_with_while_6_3(self):
        self.assertEqual(lift_with_while(6,3),"Floor number: 6\nFloor number: 5\nFloor number: 4\nFloor number: 3")
        #def test_lift_with_while_2_0(self):
        self.assertEqual(lift_with_while(2,0).strip(),"Floor number: 2\nFloor number: 1\nFloor number: 0")
        #def test_lift_with_while_1_0(self):
        self.assertEqual(lift_with_while(1,0).strip(),"Floor number: 1\nFloor number: 0")
        #def test_lift_with_while_6_minus3(self):
        self.assertEqual(lift_with_while(6,-3).strip(),"Floor number: 6\nFloor number: 5\nFloor number: 4\nFloor number: 3\nFloor number: 2\nFloor number: 1\nFloor number: 0\nFloor number: -1\nFloor number: -2\nFloor number: -3")

    #ex-02-08.py
    def run_guesTest(self,given_answer, expected_out):
        with patch('builtins.input', return_value=given_answer) as mock_in, patch('sys.stdout',new_callable=StringIO) as mock_out:
            if type(given_answer) != type(""):
                mock_in.side_effect = given_answer
                               
            guess_game()
            output = mock_out.getvalue().strip().replace("!","")
            ex_out = expected_out.replace("!","")
            self.assertEqual(output,ex_out)
    def test_guess_game(self):
        self.run_guesTest("chocolate","You guessed it!!!!!!!!!!!")
        #def test_guess_game_pas_choc(self):
        self.run_guesTest(["pasta","chocolate"],"You are wrong.\nYou guessed it!!!!!!!") 
        #def test_guess_game_pas_pas_kuku_choc(self):
        self.run_guesTest(["pasta","pasta","kuku","chocolate"],"You are wrong.\nYou are wrong.\nYou are wrong.\nYou guessed it!!!!!!!")

    #ex-02-09.py        
    def test_look_for_factors(self):
        self.assertEqual(look_for_factors(8).strip(),"1\n2\n4\n8")
        #def test_look_for_factors_24(self):
        self.assertEqual(look_for_factors(24).strip(),"1\n2\n3\n4\n6\n8\n12\n24")
        #def test_look_for_factors_5(self):
        self.assertEqual(look_for_factors(5).strip(),"1\n5")
        #def test_look_for_factors_1(self):
        self.assertEqual(look_for_factors(1).strip(),"1")

    #ex-02-10.py
    def test_steps(self):
        self.assertEqual(steps(1).strip(),"__\n__|")
        #def test_steps_5(self):
        self.assertEqual(steps(5).strip(),"__\n  |_\n    |_\n      |_\n        |_\n__________|")
        #def test_steps_7(self):
        self.assertEqual(steps(7).strip(),"__\n  |_\n    |_\n      |_\n        |_\n          |_\n            |_\n______________|")
        #def test_steps_8(self):
        self.assertEqual(steps(8).strip(),"__\n  |_\n    |_\n      |_\n        |_\n          |_\n            |_\n              |_\n________________|")


    ################################
    ######3 STRINGS and LISTS#######
    ################################

    #ex-03-01.py
    def test_text_info(self):
        self.assertEqual(text_info("kukuak udaberrian kuku").replace(" ",""),"Size of the text: 22\nNumber of kuku's:2\nIn lower case".replace(" ",""))
        self.assertEqual(text_info("a ze parea karakola ta barea"),"Size of the text: 28\nNo kuku this way\nIn lower case")
        self.assertEqual(text_info("kuku miku, txoriak umeak sasian ditu"),"Size of the text: 36\nNumber of kuku's:1\nIn lower case")
        self.assertEqual(text_info("kuku"),"Size of the text: 4\nNumber of kuku's:1\nIn lower case")
        self.assertEqual(text_info("kuku kuku kuku kukukuku"),"Size of the text: 23\nNumber of kuku's:5\nIn lower case")
        #def test_text_info_both(self):
        self.assertEqual(text_info("Kuku miku, txoriak umeak sasian ditu"),"Size of the text: 36\nNumber of kuku's:1\nBoth lower and upper case")
        self.assertEqual(text_info("kukuak udaberrian KUKU"),"Size of the text: 22\nNumber of kuku's:2\nBoth lower and upper case")
        self.assertEqual(text_info("a ze paRea karakola ta barea"),"Size of the text: 28\nNo kuku this way\nBoth lower and upper case")
        self.assertEqual(text_info("kukU"),"Size of the text: 4\nNumber of kuku's:1\nBoth lower and upper case")
        self.assertEqual(text_info("kuku kuku kuku kuKUKUku"),"Size of the text: 23\nNumber of kuku's:5\nBoth lower and upper case")
        #def test_text_info_upper(self):
        self.assertEqual(text_info("A ZE PAREA KARAKOLA TA BAREA"),"Size of the text: 28\nNo kuku this way\nIn upper case")
        self.assertEqual(text_info("KUKU MIKU, TXORIAK UMEAK SASIAN DITU"),"Size of the text: 36\nNumber of kuku's:1\nIn upper case")
        self.assertEqual(text_info("KUKUAK UDABERRIAN KUKU"),"Size of the text: 22\nNumber of kuku's:2\nIn upper case")
        self.assertEqual(text_info("KUKU"),"Size of the text: 4\nNumber of kuku's:1\nIn upper case")
        self.assertEqual(text_info("KUKU KUKU KUKU KUKUKUKU"),"Size of the text: 23\nNumber of kuku's:5\nIn upper case")

    #ex-03-02.py
    def test_broken_keyboard(self):
        self.assertEqual(broken_keyboard("I s###dd##nly brok## my k##ybo%%rd"),"I suddenly broke my keyboard")
        #def test_broken_keyboard_aeu(self):
        self.assertEqual(broken_keyboard("%% ## ###"),"a e u")
        #def test_broken_keyboard_aaeueuu(self):
        self.assertEqual(broken_keyboard("%%%% ## ### ## ######"),"aa e u e uu")

    #ex-03-03.py
    def test_language_of_the_word(self):
        self.assertEqual(language_of_the_word("action"),"English!")
        self.assertEqual(language_of_the_word("vaccinaction"),"English!")
        self.assertEqual(language_of_the_word("solution"),"English!")
        self.assertEqual(language_of_the_word("tion"),"English!")
        self.assertEqual(language_of_the_word("accion"),"Spanish!")
        self.assertEqual(language_of_the_word("vacunacion"),"Spanish!")
        self.assertEqual(language_of_the_word("solucion"),"Spanish!")
        self.assertEqual(language_of_the_word("animacion"),"Spanish!")
        self.assertEqual(language_of_the_word("cion"),"Spanish!")
        self.assertEqual(language_of_the_word("akzio"),"Basque!")
        self.assertEqual(language_of_the_word("burutazio"),"Basque!")
        self.assertEqual(language_of_the_word("bakunazio"),"Basque!")
        self.assertEqual(language_of_the_word("soluzio"),"Basque!")
        self.assertEqual(language_of_the_word("zio"),"Basque!")
        self.assertEqual(language_of_the_word("python"),"Ups... I don't know!")
        self.assertEqual(language_of_the_word("covid"),"Ups... I don't know!")
        self.assertEqual(language_of_the_word("fast test"),"Ups... I don't know!")

    #ex-03-04.py
    def test_rainy_days(self):
        self.assertEqual(rainy_days("Monday Tuesday Friday"),4)
        #def test_rainy_days_7(self):
        self.assertEqual(rainy_days(""),7)
        #def test_rainy_days_0(self):
        self.assertEqual(rainy_days("Monday Tuesday Wednesday Thursday Friday Saturday Sunday"),0)
        #def test_rainy_days_2(self):
        self.assertEqual(rainy_days("Monday Tuesday Thursday Friday Sunday"),2)
        #def test_rainy_days_3(self):
        self.assertEqual(rainy_days("Tuesday Thursday Friday Sunday"),3)

    #ex-03-05.py
    def test_order_students_names(self):
        self.assertEqual(order_students_names("Mikel Ane Mattin Jule Aintzane").strip(),"List of students:\nAintzane\nAne\nJule\nMattin\nMikel")
        #def test_order_students_names_2(self):
        self.assertEqual(order_students_names("Mikel Ane Mattin Jule Aintzane Izar Ander").strip(),"List of students:\nAintzane\nAnder\nAne\nIzar\nJule\nMattin\nMikel")
        #def test_order_students_names_3(self):
        self.assertEqual(order_students_names("w b c d a z").strip(),"List of students:\na\nb\nc\nd\nw\nz")

    #ex-03-06.py
    def test_palindromes(self):
        self.assertEqual(palindromes("animatuta bazen ezabatuta mina"),"Good!!")
        #def test_palindromes_madam(self):
        self.assertEqual(palindromes("madam"),"Good!!")
        #def test_palindromes_able(self):
        self.assertEqual(palindromes("Able was I ere I saw Elba".lower()),"Good!!")
        #def test_palindromes_zozoak(self):
        self.assertEqual(palindromes("zozoak beleari ipur beltz"),"No, you missed it...")
        #def test_palindromes_no(self):
        self.assertEqual(palindromes("kurrukukuku"),"No, you missed it...")

    #ex-03-07.py
    def test_total_spent(self):
        self.assertEqual(total_spent("12 15 10 5 3 8"),53)
        self.assertEqual(total_spent("8 15 10 5 3 12"),53)
        self.assertEqual(total_spent("8 3 5 10 15 12"),53)
        self.assertEqual(total_spent("5 3 8 12 15 10"),53)
        #def test_total_spent_100(self):
        self.assertEqual(total_spent("10 10 10 10 10 10 10 10 10 10"),100)
        self.assertEqual(total_spent("100 0 0 0"),100)
        self.assertEqual(total_spent("50 10 10 10 10 10"),100)
        self.assertEqual(total_spent("90 10"),100)
        #def test_total_spent_0(self):
        self.assertEqual(total_spent("0 0 0 0 0 0 0 0 0 0"),0)
        self.assertEqual(total_spent("0 0 0"),0)
        self.assertEqual(total_spent("0"),0)

    #ex-03-08.py
    def run_wordsTest(self,given_answer, expected_out):
        with patch('builtins.input', return_value=given_answer) as mock_in:
            if type(given_answer) != type(""):
                mock_in.side_effect = given_answer
                               
            output = how_many_words()
            self.assertEqual(output,expected_out)
    def test_how_many_words(self):
        self.run_wordsTest(["waaw","deedeet","jerejef","waaw","jerejef","barna",""],4)
        #def test_how_many_words_5(self):
        self.run_wordsTest(["rafiki","kinywaji","nzuri","kwaheri","moto",""],5)
        #def test_how_many_words_6(self):
        self.run_wordsTest(["kaixo","agur","eskerrik asko","ez horregatik","pintxo","garagardoa","garagardoa",""],6)

    #ex-03-09.py
    def test_red_and_blue_cars(self):
        self.assertEqual(red_and_blue_cars("blue blue blue grey"),(0,3))
        self.assertEqual(red_and_blue_cars("blue blue blue"),(0,3))
        self.assertEqual(red_and_blue_cars("yellow blue white blue black black blue grey"),(0,3))
        #def test_red_and_blue_cars_2_1(self):
        self.assertEqual(red_and_blue_cars("red red grey blue"),(2,1))
        self.assertEqual(red_and_blue_cars("red red blue"),(2,1))
        self.assertEqual(red_and_blue_cars("red grey red white white blue white black green yellow grey white"),(2,1))
        #def test_red_and_blue_cars_1_1(self):
        self.assertEqual(red_and_blue_cars("red gred grey blue"),(1,1))
        self.assertEqual(red_and_blue_cars("red blue"),(1,1))
        self.assertEqual(red_and_blue_cars("grey red white white blue white black green yellow grey white"),(1,1))

    #ex-03-10.py
    def test_secret_message(self):
        self.assertEqual(secret_message("tHIs PrOGRam teACheS To LeaRN pYThOn To cATs . IMPORTANT : Is baD pROGRAMING ExERcIsES aNd DoING trICKs").strip(),"doing exercises is important to learn to program")
        #def test_secret_message_eus(self):
        self.assertEqual(secret_message("oNDo Ikasteko pyTHoNeZ ProGRaMatZEN eZ Da GaRRaNTziTSua eZER EGiTea eTa ARikETaK eRE eZ").strip(),"ariketak egitea garrantzitsua da programatzen ikasteko")
        #def test_secret_message_zozoak(self):
        self.assertEqual(secret_message("IPuRbELtz BeleaRI ZOzoAk").strip(),"zozoak beleari ipurbeltz")
        #def test_secret_message_zozoak2(self):
        self.assertEqual(secret_message("IPuRbELtz iSDFS BeleaRI kukSFDSF ZOzoAk").strip(),"zozoak beleari ipurbeltz")

    #ex-03-11.py
    def test_super_anagrams(self):
        self.assertEqual(super_anagrams("leihoa","lehoia"),"Super Anagram!")
        self.assertEqual(super_anagrams("ondarroa","arraondo"),"What?")
        self.assertEqual(super_anagrams("bart","brat"),"Super Anagram!")
        self.assertEqual(super_anagrams("leihoa","lehoia"),"Super Anagram!")
        self.assertEqual(super_anagrams("paris","pairs"),"Super Anagram!")
        self.assertEqual(super_anagrams("kuku","kurruku"),"What?")

    #ex-03-12.py
    def test_number_info(self):
        self.assertEqual(average(2,6,4),4.0)
        self.assertEqual(average(2,4,6),4.0)
        self.assertEqual(average(4,6,2),4.0)
        self.assertEqual(average(6,4,2),4.0)
        #def test_average_2(self):
        self.assertEqual(average(-5,-7,3),-3.0)
        self.assertEqual(average(3,-5,-7),-3.0)
        self.assertEqual(average(-5,3,-7),-3.0)
        self.assertEqual(average(-7,-5,3),-3.0)
        #def test_average_3(self):
        self.assertEqual(average(2,2,2),2.0)
        self.assertEqual(average(4,4,4),4.0)
        self.assertEqual(average(6,6,6),6.0)
        self.assertEqual(average(0,0,0),0.0)
        self.assertEqual(average(100,100,100),100.0)
        self.assertEqual(average(-6,-6,-6),-6.0)
        self.assertEqual(average(-100,-100,-100),-100.0)
        #def test_middle_number_1(self):
        self.assertEqual(middle_number(2,6,4),4)
        self.assertEqual(middle_number(2,4,6),4)
        self.assertEqual(middle_number(4,6,2),4)
        self.assertEqual(middle_number(6,4,2),4)
        #def test_middle_number_2(self):
        self.assertEqual(middle_number(-5,-7,3),-5)
        self.assertEqual(middle_number(3,-5,-7),-5)
        self.assertEqual(middle_number(-5,3,-7),-5)
        self.assertEqual(middle_number(-7,-5,3),-5)
        #def test_middle_number_3(self):
        self.assertEqual(middle_number(1,2,3),2)
        self.assertEqual(middle_number(3,2,1),2)
        self.assertEqual(middle_number(1,3,2),2)
        self.assertEqual(middle_number(2,1,3),2)
        #def test_middle_number_4(self):
        self.assertEqual(middle_number(-1,-2,-3),-2)
        self.assertEqual(middle_number(-3,-2,-1),-2)
        self.assertEqual(middle_number(-2,-3,-1),-2)
        self.assertEqual(middle_number(-2,-1,-3),-2)
        #def test_str_odd_1(self):
        self.assertEqual(str_odd(2),"even")
        self.assertEqual(str_odd(12),"even")
        self.assertEqual(str_odd(222),"even")
        self.assertEqual(str_odd(24),"even")
        self.assertEqual(str_odd(20),"even")
        self.assertEqual(str_odd(1028),"even")
        #def test_str_odd_1(self):
        self.assertEqual(str_odd(1),"odd")
        self.assertEqual(str_odd(11),"odd")
        self.assertEqual(str_odd(221),"odd")
        self.assertEqual(str_odd(25),"odd")
        self.assertEqual(str_odd(29),"odd")
        self.assertEqual(str_odd(1027),"odd")
        #def test_number_info_1(self):
        self.assertEqual(number_info("2 6 4"),\
            "The average of the three numbers: 4.0\nMiddle number: 4\nIt is even")
        self.assertEqual(number_info("2 4 6"),\
            "The average of the three numbers: 4.0\nMiddle number: 4\nIt is even")
        self.assertEqual(number_info("4 6 2"),\
            "The average of the three numbers: 4.0\nMiddle number: 4\nIt is even")
        self.assertEqual(number_info("6 4 2"),\
            "The average of the three numbers: 4.0\nMiddle number: 4\nIt is even")
        #def test_number_info_2(self):
        self.assertEqual(number_info("-5 -7 3"),\
            "The average of the three numbers: -3.0\nMiddle number: -5\nIt is odd")
        self.assertEqual(number_info("-5 3 -7"),\
            "The average of the three numbers: -3.0\nMiddle number: -5\nIt is odd")
        self.assertEqual(number_info("3 -7 -5"),\
            "The average of the three numbers: -3.0\nMiddle number: -5\nIt is odd")
        self.assertEqual(number_info("-7 3 -5"),\
            "The average of the three numbers: -3.0\nMiddle number: -5\nIt is odd")
        #def test_number_info_3(self):
        self.assertEqual(number_info("5 4 9"),\
            "The average of the three numbers: 6.0\nMiddle number: 5\nIt is odd")
        self.assertEqual(number_info("5 9 4"),\
            "The average of the three numbers: 6.0\nMiddle number: 5\nIt is odd")
        self.assertEqual(number_info("4 9 5"),\
            "The average of the three numbers: 6.0\nMiddle number: 5\nIt is odd")
        self.assertEqual(number_info("9 5 4"),\
            "The average of the three numbers: 6.0\nMiddle number: 5\nIt is odd")
    
    
    #####################################
    ######4 DICTIONARIES and FILES#######
    #####################################
    #ex-04-01.py
    def test_word2sms(self):
        self.assertEqual(word2sms("KAIXO"),"52496")
        #def test_word2sms_2(self):
        self.assertEqual(word2sms("PYTHON"),"798466")
        #def test_word2sms_3(self):
        self.assertEqual(word2sms("KUKU"),"5858")
        #def test_word2sms_4(self):
        self.assertEqual(word2sms("OLATZ"),"65289")
    
    #ex-04-02.py
    def run_favouriteTest(self,given_answer, expected_out):
        with patch('builtins.input', return_value=given_answer) as mock_in:
            if type(given_answer) != type(""):
                mock_in.side_effect = given_answer
                               
            output = favourite_colour().strip()
            self.assertEqual(output,expected_out)
    def test_favourite_colour(self):
        self.run_favouriteTest(["Olatz Purple","Ane Pink","Mikel Pink",\
            "Izar Blue",""],"Ane Pink\nIzar Blue\nMikel Pink\nOlatz Purple")
        self.run_favouriteTest(["Ane Pink","Olatz Purple","Mikel Pink",\
            "Izar Blue",""],"Ane Pink\nIzar Blue\nMikel Pink\nOlatz Purple")
        self.run_favouriteTest(["Mikel Pink","Olatz Purple","Ane Pink",\
            "Izar Blue",""],"Ane Pink\nIzar Blue\nMikel Pink\nOlatz Purple")
        self.run_favouriteTest(["Olatz Purple","Ane Pink","Mikel Pink",\
            "Izar Blue","Olatz Purple","Ane Pink",""],"Ane Pink\nIzar Blue\nMikel Pink\nOlatz Purple")
        self.run_favouriteTest(["Izar Blue","Olatz Purple","Ane Pink",\
            "Mikel Pink",""],"Ane Pink\nIzar Blue\nMikel Pink\nOlatz Purple")
        #def test_favourite_colour_2(self):
        self.run_favouriteTest(["Olatz Purple","Ane Blue","Mikel Pink",\
            "Izar Black","Mattin Green",""],"Ane Blue\nIzar Black\nMattin Green\nMikel Pink\nOlatz Purple")
        self.run_favouriteTest(["Ane Blue","Olatz Purple","Mikel Pink",\
            "Izar Black","Mattin Green",""],"Ane Blue\nIzar Black\nMattin Green\nMikel Pink\nOlatz Purple")
        self.run_favouriteTest(["Mikel Pink","Ane Blue","Olatz Purple",\
            "Izar Black","Mattin Green",""],"Ane Blue\nIzar Black\nMattin Green\nMikel Pink\nOlatz Purple")
        self.run_favouriteTest(["Izar Black","Olatz Purple","Mattin Green",\
            "Ane Blue","Mikel Pink",""],"Ane Blue\nIzar Black\nMattin Green\nMikel Pink\nOlatz Purple")
        self.run_favouriteTest(["Mattin Green","Olatz Purple","Ane Blue",\
            "Mikel Pink","Izar Black",""],"Ane Blue\nIzar Black\nMattin Green\nMikel Pink\nOlatz Purple")

    #ex-04-03.py
    def run_carsTest(self,given_answer, expected_out):
        with patch('builtins.input', return_value=given_answer) as mock_in:
            if type(given_answer) != type(""):
                mock_in.side_effect = given_answer
                               
            output = cars_colours().strip()
            for e_o in expected_out:
                self.assertIn(e_o,output)
    def test_cars_colours(self):
        self.run_carsTest(["red","red","white","white","white","blue",""],\
            ["white 3","red 2","blue 1"])
        self.run_carsTest(["red","red","white","blue","white","white",""],\
            ["white 3","red 2","blue 1"])
        self.run_carsTest(["red","blue","white","red","white","white",""],\
            ["white 3","red 2","blue 1"])
        self.run_carsTest(["white","blue","white","white","red","red",""],\
            ["white 3","red 2","blue 1"])
        #def test_cars_colours_2(self):
        self.run_carsTest(["red","red","red","red","red","red","red",""],\
            ["red 7"])
        #def test_cars_colours_3(self):
        self.run_carsTest(["red",""],["red 1"])
        #def test_cars_colours_4(self):
        self.run_carsTest(["red","red","white","white","white","blue",\
            "yellow","pink",""],["white 3","red 2","blue 1","yellow 1",\
            "pink 1"])

    #ex-04-04.py
    def run_frequencyTest(self,given_answer, expected_out):
        with patch('builtins.input', return_value=given_answer) as mock_in:
            if type(given_answer) != type(""):
                mock_in.side_effect = given_answer
                               
            output = words_frequency().strip()
            self.assertEqual(output,expected_out)
    def test_words_frequency(self):
        self.run_frequencyTest(["hello hello hello hello how are you going friends",\
            ""],"you 1\nhow 1\nhello 4\ngoing 1\nfriends 1\nare 1")
        self.run_frequencyTest(["hello", "hello", "hello hello", "how are",\
            "you going friends",""],\
            "you 1\nhow 1\nhello 4\ngoing 1\nfriends 1\nare 1")
        self.run_frequencyTest(["hello", "hello", "hello", "hello", "how",\
            "are", "you", "going", "friends", ""],\
            "you 1\nhow 1\nhello 4\ngoing 1\nfriends 1\nare 1")
        self.run_frequencyTest(["are you going friends hello hello hello hello how",\
            ""],"you 1\nhow 1\nhello 4\ngoing 1\nfriends 1\nare 1")
        #def test_words_frequency_2(self):
        self.run_frequencyTest(["a b c d a a a b c",""],\
            "d 1\nc 2\nb 2\na 4")
        self.run_frequencyTest(["a", "b", "c", "d", "a", "a", "a", "b", "c",\
            ""],"d 1\nc 2\nb 2\na 4")
        self.run_frequencyTest(["a b", "c d", "a a a b c",\
            ""],"d 1\nc 2\nb 2\na 4")
        self.run_frequencyTest(["a a a b c","a b c d",\
            ""],"d 1\nc 2\nb 2\na 4")
    
    #ex-04-05.py
    def test_shout_requests(self):
        self.assertEqual(shout_requests("data/requests.txt").strip(),"TOMATO SALAD\nPUMPKIN PUREE\nROAST CHICKEN\nPUDDING WITH ICE CREAM")
        #def test_shout_requests_2(self):
        self.assertEqual(shout_requests("data/sayings.txt").strip(),"ABENDUA JAI HUTS ETA GAU HUTS\nTXAPELA BURUAN, IBILI MUNDUAN\nALFERRARENTZAT JANA ETA LANGILEARENTZAT LANA EZ DA INOIZ FALTAKO\nUSTEAK ERDIA USTEL\nZOZOAK BELEARI IPURBELTZ\nZENBAT BURU, HAINBAT ABURU\nBESTEEN FALTAK AURREKO ALDEAN, GEUREAK BIZKARREAN\nOGI GOGORRARI, HAGIN ZORROTZA\nA ZE PAREA, KARAKOLA TA BAREA!\nFESTAK AURREA EDERRAGO DU ATZEALDEAN")
        #def test_shout_requests_3(self):
        self.assertEqual(shout_requests("data/homework.txt").strip(),"ABENDUA JAI HUTS ETA GAU HUTS\nTXAPELA BURUAN, IBILI MUNDUAN\nALFERRARENTZAT JANA ETA LANGILEARENTZAT LANA EZ DA INOIZ FALTAKO\nVIRUS! ESCUCHAR Y CALLAR, AFIRMACIÓN TOTAL\nUSTEAK ERDIA USTEL\nZOZOAK BELEARI IPURBELTZ\nVIRUS! ESTATE DORMIDO Y COMERÁS FINO\nZENBAT BURU, HAINBAT ABURU\nOGI GOGORRARI, HAGIN ZORROTZA\nVIRUS! SI ESTÁS AGUSTO NO HAY CUESTAS\nA ZE PAREA, KARAKOLA TA BAREA!")
    
    #ex-04-06.py
    def test_virus(self):
        self.assertEqual(virus("data/homework.txt").strip().upper(),"ABENDUA JAI HUTS ETA GAU HUTS\nTXAPELA BURUAN, IBILI MUNDUAN\nALFERRARENTZAT JANA ETA LANGILEARENTZAT LANA EZ DA INOIZ FALTAKO\nUSTEAK ERDIA USTEL\nZOZOAK BELEARI IPURBELTZ\nZENBAT BURU, HAINBAT ABURU\nOGI GOGORRARI, HAGIN ZORROTZA\nA ZE PAREA, KARAKOLA TA BAREA!")
        #def test_virus_2(self):
        self.assertEqual(virus("data/homework.txt").strip(),"Abendua jai huts eta gau huts\nTxapela buruan, ibili munduan\nAlferrarentzat jana eta langilearentzat lana ez da inoiz faltako\nUsteak erdia ustel\nZozoak beleari ipurbeltz\nZenbat buru, hainbat aburu\nOgi gogorrari, hagin zorrotza\nA ze parea, karakola ta barea!")
    
    #ex-04-07.py
    def test_word_in_the_book(self):
        self.assertEqual(word_in_the_book("data/book.txt","eder").strip(), "Found in line: 3\nFound in line: 39\nFound in line: 44\nFound in line: 46\nFound in line: 71")
        #def test_word_in_the_book_2(self):
        self.assertEqual(word_in_the_book("data/book.txt","python"),"Not found")
        #def test_word_in_the_book_3(self):
        self.assertEqual(word_in_the_book("data/book.txt","kaixo"),"Not found")
        #def test_word_in_the_book_4(self):
        self.assertEqual(word_in_the_book("data/book.txt","lagun"),"Not found")
        #def test_word_in_the_book_5(self):
        self.assertEqual(word_in_the_book("data/book.txt","sendatzeko").strip(),"Found in line: 6\nFound in line: 25")

    #ex-04-08.py
    def test_spanish_elephant_in_file(self):
        self.assertEqual(spanish_elephant_in_file("data/sayings.txt").strip(),"Spanish elephant in this line: 3\nSpanish elephant in this line: 7\nSpanish elephant in this line: 10")
        #def test_spanish_elephant_in_file_2(self):
        self.assertEqual(spanish_elephant_in_file("data/homework.txt").strip(),"Spanish elephant in this line: 3")
        #def test_spanish_elephant_in_file_3(self):
        self.assertEqual(spanish_elephant_in_file("data/book.txt").strip(),"Spanish elephant in this line: 12\nSpanish elephant in this line: 50\nSpanish elephant in this line: 59\nSpanish elephant in this line: 62\nSpanish elephant in this line: 64")
    
    #######################################
    ##### 5 ADVANCED FILES AND OBJECTS
    #######################################
    #ex-05-01.py
    def test_scrabble_game(self):
        self.assertEqual(scrabble_game("kaixo"),(15,16))
        self.assertEqual(scrabble_game("hello"),(17,8))
        #def test_scrabble_game_2(self):
        self.assertEqual(scrabble_game("ordenagailu"),(22,13))
        self.assertEqual(scrabble_game("computer"),(22,14))
        #def test_scrabble_game_3(self):
        self.assertEqual(scrabble_game("house"),(13,8))
        self.assertEqual(scrabble_game("etxe"),(13,11))
        #def test_scrabble_game_4(self):
        self.assertEqual(scrabble_game("python"),(16,14))
        
    #ex-05-02.py
    def test_usernames(self):
        self.assertEqual(usernames("data/class_list.csv"),"malen\nmalena\nane\nanea\nanea1\nanea2\naimar\naitor\naitoro\naitoro1\njon\njonander")

    #ex-05-03.py
    def test_londons_weather(self):
        self.assertEqual(londons_weather(20,"data/weather.csv","data/weather_out.csv"),"Total entries: 43\nAverage temperature: 22.58\nTotal precipitation: 0.10\nAverage wind-speed: 12.72")
        #def test_londons_weather_2(self):
        self.assertEqual(londons_weather(10,"data/weather.csv","data/weather_out.csv"),"Total entries: 222\nAverage temperature: 15.20\nTotal precipitation: 14.30\nAverage wind-speed: 15.45")
        #def test_londons_weather_3(self):
        self.assertEqual(londons_weather(5,"data/weather.csv","data/weather_out.csv"),"Total entries: 346\nAverage temperature: 12.58\nTotal precipitation: 36.10\nAverage wind-speed: 16.40")

