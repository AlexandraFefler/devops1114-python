import datetime
import os

str1 = input("Enter something to put into C://Users/sasha/journal.txt (enter exit to stop adding entries): ")
while str1 != "exit":
    with open("journal.txt", "a") as file: # was "w" instead of "a"
        file.write("["+(datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")+"] "+str1+"\n")
    #this 'with' closes the file by itself here (at end of iteration)
    f = open("journal.txt", "r") # needed?
    f.close() # needed. Makes sure we write (save) the files new contents to disk (without it it's mostly stored on cache/buffer)
    str1 = input("Enter something to put into C://Users/sasha/journal.txt (enter exit to stop adding entries): ")

if ("journal.txt" in os.listdir(os.getcwd())): # only if journal.txt is in list of files (os.listdir()) in current working directory (os.getcwd())
    f = open("journal.txt", "r")
    print(f.read()) # printing out the contents of journal.txt
    f.close()

    f = open("journal.txt", "r")
    cunt_entries = 0 #it's just the number of lines
    for line in f:
        cunt_entries += 1 #counting the number of lines
    print(f"number of entries: {cunt_entries}")
    f.close()

    f = open("journal.txt", "r") 
    content_file_str = f.read() # now we count the wordssss

    content_file_lst = content_file_str.split(" ") #TODO: either split not by " ", or split further by \n. Rn it splits wrong
    # temp_list = []  #TODO: טוב ניסיתי משהו שוב לא עובד אח"כ אסיים
    # for i in range(0,len(content_file_lst)):
    #     if "\n" in content_file_lst[i]:
    #         temp_list = content_file_lst[i].split("\n")
    #         print(temp_list)
    #     for actual_word in temp_list:
    #         # print(actual_word + "    added")
    #         content_file_lst.insert(i, actual_word)
        
    
    count_words = 0 #counting all the words I've split up
    for word in content_file_lst:
        count_words += 1
    print(f"number of words in file: {count_words}")
    f.close()
else:
    print("Journal.txt is not found")

