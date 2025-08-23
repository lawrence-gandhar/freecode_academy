"""
Build an Arithmetic Formatter Project
Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:

  235
+  52
-----
Finish the arithmetic_arranger function that receives a list of strings which are arithmetic problems, and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

Example
Function Call:

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
Output:

   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
Function Call:

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
Output:

  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
Rules
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

Situations that will return an error:
If there are too many problems supplied to the function. The limit is five, anything more will return: 'Error: Too many problems.'
The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: "Error: Operator must be '+' or '-'."
Each number (operand) should only contain digits. Otherwise, the function will return: 'Error: Numbers must only contain digits.'
Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: 'Error: Numbers cannot be more than four digits.'
If the user supplied the correct format of problems, the conversion you return will follow these rules:
There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
Numbers should be right-aligned.
There should be four spaces between each problem.
There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)
"""


def arithmetic_arranger(problems, show_answers=False):
    
    error_msg = None

    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    operator = "+"
    arrange_items = []

    for problem in problems:

        if error_msg:
            break

        if '+' in problem:
            operator = '+'
        elif '-' in problem:
            operator = '-'
        else:
            return "Error: Operator must be '+' or '-'."
            
        if error_msg is None:
            data, inner_error_msg = process_part(problem, operator)

            if inner_error_msg is None: 
                arrange_items.append(data)
            else:
                return inner_error_msg
        else:
            return error_msg

    if error_msg is not None: 
        return error_msg

    row_1 = []
    row_2 = []
    row_3 = []
    row_4 = []

    for idx, x in enumerate(arrange_items):
        append_str = ""
        start_str = ""
        
        if idx != 0:
            append_str = " "*4
            start_str = " "*6

        if len(str(x[0])) > len(str(x[1])):
            row_1.append(
                append_str+str(x[0]).rjust(x[-2]+2)
            )

            inner_space = " "*(
                len(str(x[0])) - len(str(x[1]))
            )
            row_2.append(
                append_str + x[-1] + " " + inner_space + str(x[1])
            ) 
            
            row_3.append(
                append_str + ("-"*(x[-2]+2))
            )

            row_4.append(
                append_str+str(x[2]).rjust(x[-2]+2)
            )
        else:
            row_1.append(
                append_str+str(x[0]).rjust(x[-2]+2)
            )

            row_2.append(
                append_str + x[-1] + " "+str(x[1])
            ) 
            
            row_3.append(
                append_str + ("-"*(x[-2]+2))
            )
            
            row_4.append(
                append_str+str(x[2]).rjust(x[-2]+2)
            )

    row_1 = ''.join(row_1)+"\n"
    row_2 = ''.join(row_2)+"\n"
    row_3 = ''.join(row_3)

    rows = row_1+row_2+row_3

    if show_answers:
        row_4 = "\n"+''.join(row_4)
        rows = row_1+row_2+row_3+row_4

    return rows



def process_part(problem, operator):
    value = 0
    error_msg = None

    j = problem.split(operator)
    prev_value = 0
    max_len = 0

    for x in j:

        x = x.strip()

        if max_len == 0:
            max_len = len(x)
        else:
            if len(x) > max_len:
                max_len = len(x)

        if len(x) > 4:
            error_msg = 'Error: Numbers cannot be more than four digits.'
            break

        try:
            x = int(x)
        except ValueError:
            error_msg = 'Error: Numbers must only contain digits.'
            break

        if operator == '+':
            value += x
        else:
            if prev_value == 0:
                prev_value = value = x
            else:
                x = -x
                value += x

    if error_msg is None:
        return [int(j[0]), int(j[1]), value, max_len, operator], error_msg
    return [], error_msg



    

print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')