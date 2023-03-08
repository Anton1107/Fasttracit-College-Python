def function_name(param):
    param.append(42)
    print(param)


answer_list = []
function_name(answer_list)
print(answer_list)


def function_name(param):
    param = 'new value'
    print(param)


answer_list = 'old value'
function_name(answer_list)
print(answer_list)
