class ABC:
    def __init__(self):
        self.input_text: str = ''
        self.position_list: [int] = []
        self.string_alphabet: [str] = \
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'y', 'z']
        self.sum_of_items: int = 0
        self.tuple_of_words: tuple = ()

    def insert_text(self, input_text: str):
        self.input_text = input_text

    def alphabet(self):
        assert not len(self.input_text) == 0, "<< Error >> Please insert string with the length more than 0."

        for index in range(0, len(self.input_text)):
            if self.input_text[index] not in self.input_text:
                return "<< WARNING >> Insert ONLY English aplhabets."

            symbol: str = self.input_text[index]
            index_of: int = self.string_alphabet.index(symbol) + 1
            self.position_list.append(index_of)

        print("Position of alphabets are:", self.position_list)

    def statistics(self) -> None:
        print(
            f"Sum is: {sum(self.position_list)}, Min is: {min(self.position_list)}, Max is: {max(self.position_list)}, Length is: {len(self.position_list)}")

    def digit(self):
        self.sum_of_items = sum(self.position_list)
        print("Sum of alphabet symbols is: ", self.sum_of_items)
        return self.sum_of_items

    def words(self):
        if len(self.input_text) == self.sum_of_items:
            self.tuple_of_words += (self.input_text,)
        print("Tuple of words: ", self.tuple_of_words)


class Compare:
    def __init__(self, first_input: int, second_input: int):
        self.a: int = first_input
        self.b: int = second_input

    def compare_digits(self) -> None:
        if self.a > self.b:
            print("The first_input length is greater than the second_input")
        if self.a < self.b:
            print("The first_input length is less than the second_input")
        if self.a == self.b:
            print("The first_input length is equal than the second_input")


if __name__ == "__main__":
    print("----- The first object class -----")
    first_class_call = ABC()
    # input the text of the first class object
    first_class_call.insert_text("a")
    first_class_call.alphabet()
    first_class_call.statistics()
    compare_first: int = first_class_call.digit()
    first_class_call.words()
    print("----- The second object class -----")
    # input of the second class object
    second_class_object = ABC()
    second_class_object.insert_text("bc")
    second_class_object.alphabet()
    second_class_object.statistics()
    second_class_object.words()

    compare_second: int = second_class_object.digit()

    # comparing digits
    print("----- Compared ----- ")
    Compare(compare_first, compare_second).compare_digits()
