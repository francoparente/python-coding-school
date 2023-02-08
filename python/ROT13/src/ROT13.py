# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ... a b c d e f g h i j k l m n o p q r s t u v w x y z
# N O P Q R S T U V W X Y Z|A B C D E F G H I J K L M ... n o p q r s t u v w x y z|a b c d e f g h i j k l m


ALPHABET_MIDDLE = 13
ALPHABET_LENGTH = 26
FIRST_LOWER_LETTER = ord('a')
FIRST_UPPER_LETTER = ord('A')


class ROT13:
    def rotate(self, text):
        rotated_text = ''
        for character in text:
            rotated_text += self.rotate_character(character)
        return rotated_text

    def rotate_character(self, a_character):
        first_letter_as_ascii = FIRST_LOWER_LETTER if a_character.islower() else FIRST_UPPER_LETTER
        character_position_in_alphabet = ord(a_character) - first_letter_as_ascii

        if not self.is_english_letter(character_position_in_alphabet):
            return a_character

        if self.is_inside_second_half_of_alphabet(character_position_in_alphabet):
            return chr(character_position_in_alphabet - ALPHABET_MIDDLE + first_letter_as_ascii)
        return chr(character_position_in_alphabet + ALPHABET_MIDDLE + first_letter_as_ascii)

    def is_inside_second_half_of_alphabet(self, character_position_in_alphabet):
        return character_position_in_alphabet >= ALPHABET_MIDDLE

    def is_english_letter(self, character_as_ascii):
        return 0 <= character_as_ascii <= ALPHABET_LENGTH
