# Program to check if two words are anagrams 
# Example:
# ("eat", "ate") - True 
# ("book", "look") - False

def find_anagram(str1, str2):
    
    if(len(str1)==len(str2)):
        string_1 = sorted(str1)
        string_2 = sorted(str2)

        if string_1 == string_2 :
            print("True")  
        else:
            print("False")
    else:
        print("False")

find_anagram("listen", "silent")
find_anagram("broke", "yoke")
