def correct_tail(body, tail):
    return body[len(body) - len(tail) :] == tail


print(correct_tail("dog_with_tail", "tail"))
