def shout(text):
    return text.upper() + "!"


def whisper(text):
    return text.lower() + "..."


def speak(style, text):
    return style(text)  # a function passed in like any value


say = shout  # a second name for the same function
print(say("hello"))
print(speak(whisper, "Hello"))


def make_multiplier(factor):
    def multiply(n):
        return n * factor  # remembers factor: this is a closure

    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)
print(double(21), triple(7))
