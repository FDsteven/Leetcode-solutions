def fullJustify(words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """

    num_of_rows = 0
    output = []
    while len(words) > 0:
        current_length = -1
        word_length = 0
        index_list = []
        for j in range(len(words)):
            row_output = ""
            if current_length + len(words[j]) + 1 <= maxWidth:
                current_length = current_length + len(words[j]) + 1
                index_list.append(j)
                word_length += len(words[j])
            else:
                break
        additional_spaces = maxWidth - current_length
        number_of_words = len(index_list)
        if number_of_words == 1:
            row_output = row_output + words[0] + " " * (maxWidth - len(words[0]))
            words = words[1:]
        elif len(index_list) == len(words):
            for word_index in index_list:
                if word_index == index_list[-1]:
                    row_output = row_output + words[0]
                else:
                    row_output = row_output + words[0] + " "
                words = words[1:]
            row_output = row_output+ " " * (maxWidth - len(row_output))
        else:
            universal_extra_spaces, extra_space = divmod(additional_spaces, (number_of_words-1))
            for word_index in index_list:
                if word_index == index_list[-1]:
                    row_output = row_output + words[0]
                elif word_index < extra_space:
                    row_output = row_output + words[0] + " " * (2+universal_extra_spaces) 
                else:
                    row_output = row_output + words[0] + " " * (1+universal_extra_spaces) 
                words = words[1:]
        print(row_output)
        output.append(row_output)
        num_of_rows += 1
    print("Number of rows: " + str(num_of_rows))
    return output

words = ["This", "is", "an", "example", "of", "text", "justification."]
words = ["What","must","be","acknowledgment","shall","be"]
words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 16
maxWidth = 20
print(fullJustify(words, maxWidth))