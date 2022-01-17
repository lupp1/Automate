import traceback

try:
    raise Exception('This is the error message.')
except:
    with open('errorInfo.txt', 'w') as errorFile:
        log = errorFile.write(traceback.format_exc())
        print('The traceback was written to errorInfo.txt.')
        #