#!/usr/bin/python
# -*- coding: UTF-8 -*-

# prepare for the parsing
from textx.metamodel import metamodel_from_file
python_meta = metamodel_from_file('Pseudocode_textX.tx')
example_python_model = python_meta.model_from_file('input.txt')

# the class for parse all our pseudocode to python code
class Python(object):

    # for testing the output of our model
    def _test_(self, model):
        for c in model.instruction:
            print (c)

    # we parse our code in this function
    def Instructions(self, model):

        show_declare = '\n'+'#you have not give values to these variables: '
        show_input = '\n'+'#you need to type in variable: '
        # we put the variables we have declared in the list, is easier to use and process
        declare_list = []
        input_list = []
        list_name = []  # save the list name
        need_value_list = []
        have_value_list = []
        list_already_have_value = []
        function_list = [] # save the function name which has been defined
        for_list = [] # specialized in for instruction
        if_num_1 = 0    # let us know the number of the if instruction
        for_num_1 = 0   # let us know the number of the for instruction
        error_for = 0   # let us konw if there is an error in for condition
        while_num_1 = 0
        indentation = ''


        # where we get the instructions from the model and process them
        for c in model.instruction:
            #print (c)

            # Basic instructions as below:
            # we have declare_variables, input_variables and print


            # we start to process the pseudocode from here:
            if c.__class__.__name__ == 'Declare_variable':
                var_declare = '{}'.format(c.variable.var)
                declare_list.append(var_declare)
                need_value_list.append(var_declare)

                # here we can show the user which variable they have declared
                #print ("//you have declared variable " + var_declare)
                print (indentation + var_declare+'= None')

            # we can declare list and print <variable = []>
            elif c.__class__.__name__ == 'Declare_list':
                list__name = '{}'.format(c.variable.var)
                list_name.append(list__name)
                print (indentation + list__name + " = []")


            # detect if the name of the list has been declared or not
            elif c.__class__.__name__ == 'Input_list':
                verify_name = '{}'.format(c.variable.var)
                add_to_list = []
                print_list = []

                for list_variables in c.list_variables:
                    final_list_variable = list_variables.list_var
                    add_to_list.append(final_list_variable.encode('raw_unicode_escape'))

                # assign values to the list
                # if the list has already declared, we put the elements in the list and print
                if verify_name in list_name:
                    right_name = verify_name
                    list_already_have_value.append(right_name)
                    for list_elements in add_to_list:
                        print_list.append(list_elements)
                    print (indentation + right_name + ' = %s' %print_list)
                else:
                    print ('# can not find the list name:"' + verify_name + '", please declare first')

            elif c.__class__.__name__ == 'Input_variable':
                var_input = '{}'.format(c.variable.var)

                # detect the list include the variable we want to input or not
                # if not we remind the user to declare the variable first
                # if yes we give the python code of input variables
                if var_input not in declare_list:
                    print ('\n'+"#please declare the variable '"+var_input+"' first")
                else:
                    show_input = show_input + var_input
                    input_list.append(var_input)
                    if var_input not in have_value_list:
                        need_value_list.remove(var_input)
                        have_value_list.append(var_input)

                    if if_num_1 != 0:
                        print (indentation + var_input + " = raw_input('input:"+var_input+"')" )
                    else:
                        if while_num_1 != 0:
                            print (indentation + var_input + " = raw_input('input:"+var_input+"')" )
                        else:
                            if for_num_1!= 0:
                                print (indentation + var_input + " = raw_input('input:"+var_input+"')" )
                            else:
                                print (indentation + var_input + " = raw_input('input:"+var_input+"')" )

            elif c.__class__.__name__ == 'Declare_value':
                # here we can assign the value to the variables we have declared
                var_value = '{}'.format(c.variable.var)
                if var_value not in declare_list:
                    print ('\n'+"#please declare the variable '"+var_value+"' first")
                else:
                    # isinstance function let us know the value we have assigned to the variable
                    # is a String or a integer or a float
                    if isinstance(c.value.val,int):
                        value = str(c.value.val)
                        if if_num_1 != 0:
                            print (indentation + var_value+' = '+value)
                        elif for_num_1!=0:
                            print (indentation + var_value+' = '+value)
                        elif while_num_1 != 0:
                            print (indentation + var_value+' = '+value)
                        else:
                            print (indentation + var_value+' = '+value)
                        # we use the list to know which variable we have declared but not assigned value
                        if var_value not in have_value_list:
                            need_value_list.remove(var_value)
                            have_value_list.append(var_value)
                    elif isinstance('{}'.format(c.value.val),str):
                        value = c.value.val
                        if value in declare_list:
                            print (indentation + var_value+' = '+value)
                        elif if_num_1 != 0:
                            print (indentation + var_value + " = '"+value+"'")
                        elif for_num_1!= 0:
                            print (indentation + var_value + " = '"+value+"'")
                        elif while_num_1!= 0:
                            print (indentation + var_value + " = '"+value+"'")
                        else:
                            print (indentation + var_value+" = '"+value+"'")
                        if var_value not in have_value_list:
                            need_value_list.remove(var_value)
                            have_value_list.append(var_value)

                    else:
                        return

            elif c.__class__.__name__ == 'Print_words':
                content = '{}'.format(c.content.con)

                # we can use the list to help us know the variable we want to print is
                # a variable in our declare list or just a String
                if error_for!=0:
                    print("#please check the pseudocode of <for condition>")
                elif content in for_list:
                    print(indentation + 'print '+content)
                elif content in declare_list and input_list:
                    if if_num_1 != 0:
                        print (indentation + 'print '+ content)
                    elif for_num_1 != 0:
                        print (indentation + 'print '+ content)
                    elif while_num_1 != 0:
                        print (indentation + 'print '+ content)
                    else:
                        print (indentation + 'print '+ content)
                elif content in list_name:   # print list
                    if content in list_already_have_value:
                        if if_num_1 != 0:
                            print (indentation + 'print '+ content)
                        elif for_num_1 != 0:
                            print (indentation + 'print '+ content)
                        elif while_num_1 != 0:
                            print (indentation + 'print '+ content)
                        else:
                            print (indentation + 'print '+ content)
                    else:
                        if if_num_1 != 0:
                            # remind the user if the list is empty or not existed
                            print (indentation + 'print '+ content)
                            print ('# can not print empty list, please assign values first')
                        elif for_num_1 != 0:
                            print (indentation + 'print '+ content)
                            print ('# can not print empty list, please assign values first')
                        elif while_num_1 != 0:
                            print (indentation + 'print '+ content)
                            print ('# can not print empty list, please assign values first')
                        else:
                            print (indentation + 'print '+ content)
                            print ('# can not print empty list, please assign values first')

                elif content in declare_list not in input_list:
                    print ('\n'+'#'+content+' is a variable, please give a value before print.')
                else:
                    if if_num_1 != 0:
                        print (indentation + 'print "'+ content +'"')
                    elif for_num_1!= 0:
                        print (indentation + 'print "'+ content+'"')
                    elif while_num_1!= 0:
                        print (indentation + 'print "'+ content+'"')
                    else:
                        print (indentation + 'print "'+ content +'"')

            elif c.__class__.__name__ == 'Print_string':
                content = '{}'.format(c.content_string.con)

                if if_num_1 != 0:
                    print (indentation + 'print '+'"'+content+'"')
                elif for_num_1 != 0:
                    print (indentation + 'print '+'"'+content+'"')
                elif while_num_1 != 0:
                    print (indentation + 'print '+'"'+content+'"')
                else:
                    print (indentation + 'print '+'"'+content+'"')

            elif c.__class__.__name__ == 'Calculation_simple':
                # we can print the simple calculations here
                variable_af = '{}'.format(c.variable_af.var_af)
                variable_be = '{}'.format(c.variable_af.var_be)
                if c.calculation_operator == 'plus':
                    print (indentation + variable_be + '+' + variable_af)
                elif c.calculation_operator == 'minus':
                    print (indentation + variable_be + '-' + variable_af)
                elif c.calculation_operator == 'multiply':
                    print (indentation + variable_be + '*' + variable_af)
                elif c.calculation_operator == 'divide':
                    print (indentation + variable_be + '/' + variable_af)
                elif c.calculation_operator == 'power':
                    print (indentation + variable_be + '**' + variable_af)

            # While instruction:

            elif c.__class__.__name__ == 'While_instruction_startline':

                if while_num_1 == 0:
                    print ('\n' + "# while instruction as below:")
                else:
                    while_num_1 = while_num_1

                a = 0   # use a variable to know the two variables in while are all declared
                while_num_1 = while_num_1 + 1  # let us know this is which while instruction
                variable_be = '{}'.format(c.variable_be.var_be)
                variable_af = '{}'.format(c.variable_af.var_af)
                comparasion_symbol = '{}'.format(c.comparasion)

                if comparasion_symbol == 'is greater than':
                    print(indentation + "while " + variable_be + ' ' + ">" + ' ' + variable_af + ":")
                elif comparasion_symbol == 'is lower than':
                    print (indentation + "while " + variable_be + ' ' + "<" + ' ' + variable_af + ":")
                elif comparasion_symbol == 'is more equal':
                    print (indentation + "while " + variable_be + ' ' + ">=" + ' ' + variable_af + ":")
                elif comparasion_symbol == 'is equal to':
                    print (indentation + "while " + variable_be + ' ' + "==" + ' ' + variable_af + ":")
                elif comparasion_symbol == 'is different from':
                    print (indentation + "while " + variable_be + ' ' + "!=" + ' ' + variable_af + ":")

                indentation += '    '

            elif c == 'end while':
                print("# The end of while")
                indentation = indentation[:-4]

            # If instruction is as below:

            elif c.__class__.__name__ == 'If_instruction_startline':

                if if_num_1 == 0:
                    print ("#If instruction as below:")
                else:
                    if_num_1 = if_num_1

                a = 0   # use a variable to know the two variables in IF are all declared
                if_num_1 = if_num_1 + 1  # let us know this is which if instruction
                variable_be = '{}'.format(c.variable_be.var_be)
                variable_af = '{}'.format(c.variable_af.var_af)
                comparasion_symbol = '{}'.format(c.comparasion)
                logic_operator = '{}'.format(c.logic_operator)

                if variable_be in have_value_list:
                    a = a + 1
                elif variable_be in declare_list:
                    print ("#" + variable_be + " is not a valued variable, please give a value first.")
                else:
                    print ("#" + variable_be + " is not a declared variable, please declare first.")

                if variable_af in have_value_list:
                    a = a + 1
                elif variable_af in declare_list:
                    print ("#" + variable_af + " is not a valued variable, please give a value first.")
                else:
                    print ("#" + variable_af + " is not a declared variable, please declare first.")

                if a == 2:

                    # comparasion in if instruction
                    if comparasion_symbol == 'is greater than':
                        print (indentation + "if " + variable_be + " > " + variable_af + ":" + "    #number " + str(if_num_1) + " if instruction start")
                    elif comparasion_symbol == 'is lower than':
                        print (indentation + "if " + variable_be + " < " + variable_af + ":" + "    #number " + str(if_num_1) + " if instruction start")
                    elif comparasion_symbol == 'is more equal':
                        print (indentation + "if " + variable_be + " >= " + variable_af + ":" + "    #number " + str(if_num_1) + " if instruction start")
                    elif comparasion_symbol == 'is equal to':
                        print (indentation + "if " + variable_be + " == " + variable_af + ":" + "    #number " + str(if_num_1) + " if instruction start")
                    elif comparasion_symbol == 'is different from':
                        print (indentation + "if " + variable_be + " != " + variable_af + ":" + "    #number " + str(if_num_1) + " if instruction start")

                    # logic operator in if instruction
                    elif logic_operator == 'and':
                        print (indentation + "if " + variable_be + " and " + variable_af + ":" + "    #number " + str(if_num_1) + " if instruction start")
                    elif logic_operator == 'or':
                        print (indentation + "if " + variable_be + " or " + variable_af + ":" + "    #number " + str(if_num_1) + " if instruction start")
                    elif logic_operator == 'not':
                        print (indentation + "if " + variable_be + " not " + variable_af + ":" + "    #number " + str(if_num_1) + " if instruction start")

                    indentation += '    '

            elif c.__class__.__name__ == 'If_instruction_elifline':

                a = 0   # use a variable to know the two variables in IF are all declared
                variable_be = '{}'.format(c.variable_be.var_be)
                variable_af = '{}'.format(c.variable_af.var_af)
                comparasion_symbol = '{}'.format(c.comparasion)
                logic_operator = '{}'.format(c.logic_operator)

                # we use the if_num_1 to control the indentation
                # if we just have 1 if instruction, we don't need indentation for "if" but one "Tab" for other basic instructions
                # if we have 2 if instructions, we need one "Tab" for "if" and two "Tabs" for basic instructions
                # if we have more than 3 instructions, we use for loop to control the indentation


                # we need to know the variables in the if instruction have been declared or not
                # if not we remind the user to declare, if yes we go into the next step
                if variable_be in have_value_list:
                    a = a + 1
                elif variable_be in declare_list:
                    print ("#" + variable_be + " is not a valued variable, please give a value first.")
                else:
                    print ("#" + variable_be + " is not a declared variable, please declare first.")

                if variable_af in have_value_list:
                    a = a + 1
                elif variable_af in declare_list:
                    print ("#" + variable_af + " is not a valued variable, please give a value first.")
                else:
                    print ("#" + variable_af + " is not a declared variable, please declare first.")

                # we use the symbol "a" to know if the two variables are both declared
                # if a=2, we go into the if instruction and print the python code

                indentation = indentation[:-4]

                if a == 2:
                    # comparasion in if instruction
                    if comparasion_symbol == 'is greater than':
                        print (indentation + "elif " + variable_be + " > " + variable_af + ":")
                    elif comparasion_symbol == 'is lower than':
                        print (indentation + "elif " + variable_be + " < " + variable_af + ":")
                    elif comparasion_symbol == 'is more equal':
                        print (indentation + "elif " + variable_be + " >= " + variable_af + ":")
                    elif comparasion_symbol == 'is equal to':
                        print (indentation + "elif " + variable_be + " == " + variable_af + ":")
                    elif comparasion_symbol == 'is different from':
                        print (indentation + "elif " + variable_be + " != " + variable_af + ":")

                    # logic operators in if instruction
                    elif logic_operator == 'and':
                        print (indentation + "elif " + variable_be + " and " + variable_af + ":")
                    elif logic_operator == 'or':
                        print (indentation + "elif " + variable_be + " or " + variable_af + ":")
                    elif logic_operator == 'not':
                        print (indentation + "elif " + variable_be + " not " + variable_af + ":")

                    indentation += '    '

            # if we detect the "else" we can jump directly into the basic instructions
            # but we still have to control the indentations
            elif c == 'else':
                indentation = indentation[:-4]
                print (indentation + "else:")
                indentation += '    '

            # detected end if, we will finish the corresponding if instruction
            # and remind us which if instructgion has been ended
            elif c == 'end if':

                print ("#number " + str(if_num_1) + " if instruction finished")
                if_num_1 = if_num_1 - 1
                indentation = indentation[:-4]

            # for conditions is below:
            # we define two different conditions in for
            #first one is related to list which has value:
            elif c.__class__.__name__ == 'For_instruction_startline_1':
                error_for=0
                a=0
                for_num_1= for_num_1+ 1
                variable_main = '{}'.format(c.variable_main.var_main)
                variable_list = '{}'.format(c.variable_list.var_list)

            # ensure the parameters is avaliable:
            # the former one shouled be charactors , and second one should be a valued list in this condition
                if isinstance(variable_main,str):
                    for_list.append(variable_main)
                    a = a + 1

                else:
                    print ("#" + variable_main + " is not a string, please use string")

                if variable_list in list_already_have_value:
                    a = a + 1
                elif variable_list in list_name:
                    print ("#"+ variable_list + " is not a declared variable, please give a value first.")
                    error_for=1
                else:
                    print ("#" + variable_list + " is not a valued variable, please declare first.")
                    error_for=1
                if a ==2:
                    print (indentation + "for "+variable_main+" in "+variable_list+":")

                indentation += '    '

            #second one is related to range (for example: numbers):
            elif c.__class__.__name__ == 'For_instruction_startline_2':
                error_for=0
                a=0
                for_num_1=for_num_1+ 1
                variable_main = '{}'.format(c.variable_main.var_main)
                variable_range = '{}'.format(c.variable_range.var_range)

                # ensure the parameters is avaliable
                if isinstance(variable_main,str):
                    a = a + 1
                    for_list.append(variable_main)

                else:
                    print ("#" + variable_main + " is not a string, please use string")

                if isinstance(variable_range,str):
                    a = a + 1
                else:
                    print ("#" + variable_range + " is not a number, please give a number firstly")

                if a ==2:
                    print (indentation + "for "+variable_main+" in range("+variable_range+"):")

                indentation += '    '

            elif c == 'end for':
                #if it is not a correct for instruction:
                if error_for!=0:
                    print("#wrong for instriuction finished")
                    for_num_1 = for_num_1 -1
                #if it is a correct for instruction:
                else:
                    print ("#for instruction finished")
                    for_num_1 = for_num_1 - 1
                #delete the temporary parameters in for instruction
                    for_list.pop()

                indentation = indentation[:-4]

            # Function instruction below:
            elif c.__class__.__name__ == 'Function_instruction_startline_1':
                error_function = 0
                function_var_list = []
                function_name = '{}'.format(c.function_name.fun_name)
                #To check whether we have defined the function or not
                if function_name in function_list:
                    print ('\n'+"#this function '"+function_name+"' has already been defined")
                    error_function = 1
                else:
                    #if not, add its name to list
                    function_list.append(function_name)

                for function_variables in c.function_variables:
                    final_function_variable = function_variables.fun_var
                    #To check whether we have declare the variable or not
                    if final_function_variable not in declare_list:
                        print ('\n'+"#please declare the variable '"+final_function_variable+"' first")
                        error_function = 1
                    else:
                        #if so, add it to list
                        function_var_list.append(final_function_variable.encode('raw_unicode_escape'))
                # we add the lenth of function_var_list of this function after its name, so we can find it easily when we need to know
                function_list.append(len(function_var_list))
                if error_function == 0:
                    print ('def '+function_name+'('),
                    print (",".join(str(i) for i in function_var_list)),
                    print ('):')
                    indentation += '    '


            elif c.__class__.__name__ == 'Function_instruction_startline_2':
                function_name = '{}'.format(c.function_name.fun_name)
                #To check whether we have defined the function or not
                if function_name in function_list:
                    print ('\n'+"#this function '"+function_name+"' has already been defined")
                    error_function = 1
                else:
                    #if not, add its name to list
                    function_list.append(function_name)
                if error_function == 0:
                    print ('def '+function_name+'():')
                    indentation += '    '

            elif c.__class__.__name__ == 'Function_instruction_return':
                return_variable = '{}'.format(c.return_variable.return_var)
                #To check whether we have declare the variable or not
                if return_variable not in declare_list:
                    print ('\n'+"#please declare the variable '"+return_variable+"' first")
                    error_function = 1
                if error_function == 0:
                    print (indentation + 'return '+return_variable)


            elif c == 'end function':
                print ("#function instruction finished"+'\n')
                error_function = 0
                indentation = indentation[:-4]

            elif c.__class__.__name__ == 'Function_instruction_call_1':
                function_name = '{}'.format(c.function_name.fun_name)
                function_var_list = []
                #This is the position of function_name in function_list
                position = 0
                #To check if we define the function when we call it
                if function_name not in function_list:
                    print ('\n'+"#please define the function '"+function_name+"' first")
                    error_function = 1
                else:
                    #position +1 represent the lenth of function_var_list
                    position = function_list.index(function_name)+1
                    for function_variables in c.function_variables:
                        final_function_variable = function_variables.fun_var
                        #To check whether we have declare the variable or not
                        if final_function_variable not in declare_list:
                            print ('\n'+"#please declare the variable '"+final_function_variable+"' first")
                            error_function = 1
                        else:
                            #if so, add it to list
                            function_var_list.append(final_function_variable.encode('raw_unicode_escape'))
                    # The function cannot be called if we use more formal parameters than its definition
                    if len(function_var_list) > function_list[position]:
                        print ('#Formal parameter over limit')
                        error_function = 1
                if error_function == 0:
                    print (indentation + function_name+'('),
                    print (",".join(str(i) for i in function_var_list)),
                    print (')')
                error_function = 0

            elif c.__class__.__name__ == 'Function_instruction_call_2':
                function_name = '{}'.format(c.function_name.fun_name)
                #To check if we define the function when we call it
                if function_name not in function_list:
                    print ('\n'+"#please define the function '"+function_name+"' first")
                    error_function = 1
                elif error_function == 0:
                    print (indentation + function_name+'()')
                error_function = 0


            elif c.__class__.__name__ == 'Function_instruction_declare_1':
                var_value = '{}'.format(c.variable.var)

                function_name = '{}'.format(c.function_name.fun_name)
                function_var_list = []
                #This is the position of function_name in function_list
                position = 0
                #To check if we define the variable when we call it
                if var_value not in declare_list:
                    print ('\n'+"#please declare the variable '"+var_value+"' first")
                    error_function = 1
                #To check if we define the function when we call it
                elif function_name not in function_list:
                    print ('\n'+"#please define the function '"+function_name+"' first")
                    error_function = 1
                else:
                    #position +1 represent the lenth of function_var_list
                    position = function_list.index(function_name)+1
                    for function_variables in c.function_variables:
                        final_function_variable = function_variables.fun_var
                        #To check whether we have declare the variable or not
                        if final_function_variable not in declare_list:
                            print ('\n'+"#please declare the variable '"+final_function_variable+"' first")
                            error_function = 1
                        else:
                            #if so, add it to list
                            function_var_list.append(final_function_variable.encode('raw_unicode_escape'))
                    # The function cannot be called if we use more formal parameters than its definition
                    if len(function_var_list) > function_list[position]:
                        print ('#Formal parameter over limit')
                        error_function = 1

                if error_function == 0:
                    print (indentation + var_value + ' = ' + function_name + '('),
                    print (",".join(str(i) for i in function_var_list)),
                    print (')')
                error_function = 0
                if var_value not in have_value_list:
                    need_value_list.remove(var_value)
                    have_value_list.append(var_value)


            elif c.__class__.__name__ == 'Function_instruction_declare_2':
                var_value = '{}'.format(c.variable.var)
                function_name = '{}'.format(c.function_name.fun_name)
                #To check if we define the function when we call it
                if var_value not in declare_list:
                    print ('\n'+"#please declare the variable '"+var_value+"' first")
                    error_function = 1
                #To check if we define the function when we call it
                elif function_name not in function_list:
                    print ('\n'+"#please define the function '"+function_name+"' first")
                    error_function = 1
                elif error_function == 0:
                    print (indentation + var_value + ' = ' + function_name + '()')
                error_function = 0
                if var_value not in have_value_list:
                    need_value_list.remove(var_value)
                    have_value_list.append(var_value)


        # show the values we have not given values at the last of the python code

        if len(need_value_list)>0:
            for vals in need_value_list[:-1]:
                show_declare = show_declare + vals + ','
            show_declare = show_declare + need_value_list[-1]
            print (show_declare)
        else:
            return

pyth = Python()
pyth.Instructions(example_python_model)
#pyth._test_(example_python_model)
# the test mode can allow us to know the pseudocode has been parsed or not, and where to find the variables in pseudocode
