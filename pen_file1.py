# class Pen Fixed


class Pen(object):
    def __init__(self, **kwargs):
        # The ink amount
        self.ink_container_value = int(kwargs.get('ink_container_value', 1000))
        # size of the letter (font)
        self.size_letter = float(kwargs.get('size_letter', 1.0))
        # ink color
        self.color = str(kwargs.get('color', 'blue'))

    def write(self, word):
        if not self.check_pen_state():
            return ''

        size_of_word = len(word) * self.size_letter
        if size_of_word <= self.ink_container_value:
            self.ink_container_value -= size_of_word
            return word

        # Calculate how many characters can be written
        chars_available = int(self.ink_container_value / self.size_letter)
        part_of_word = word[:chars_available] # I love slices
        # Correctly reduce the amount of ink for used characters
        self.ink_container_value -= chars_available * self.size_letter
        return part_of_word

    def get_color(self):
        return self.color  # Return current inc color

    def check_pen_state(self):
        return self.ink_container_value > 0

    def do_something_else(self):
        print(self.color)
