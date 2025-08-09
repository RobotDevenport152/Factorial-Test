class StringManipulator:

    def find_character(self, character):
        return self.text.find(character)

    def convert_text_to_uppercase(self,text):
        return text.upper()

    def count_text_length(self, text):
        return len(text)
    #Create an instance of StringManipulator Class
name = StringManipulator("example")

#Call the find_character method on the object
result = name.find_character('x')
print(result)


# Call the count_text_length method on the object
text_length = name.count_text_length('example')
print(text_length)

# Call the convert_text_to_uppercase method on the object
upper_case_text = name.convert_text_to_uppercase('example')
print(upper_case_text)

