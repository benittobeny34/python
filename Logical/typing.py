def typing(sentence):
    print(sentence)
    point = 0
    error_words = []
    print(len(sentence))
    typed_sentence = input()
    try:
        for i in range(len(sentence)):
                       print(i,end=' ')
                       if typed_sentence[i] == sentence[i]:
                           point += 1
                       else:
                           error_words.append(sentence[i])
        print('The number of corrrect typing words {} '.format(point))
        print('The number of mis typed words {}'.format(len(error_words)))
        print(error_words)
    except(Exception ):
        print('The number of corrrect typing words {} '.format(point))
        print('The number of mis typed words {}'.format(len(error_words)))
        print(error_words)
    
                   

string = 'this is the demo for typing class . Typing is essential when you enter into \
the programming '
typing (string)
