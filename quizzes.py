QUIZZES = {
    "Python": [
        # Easy Questions
        {
            "question": "What is the output of ```Python\nprint(2 + 2)```?",
            "title": "What is the output of print(2 + 2)",
            "options": ["4", "22", "2+2", "Error"],
            "answer": "4"
        },
        {
            "question":
            "Which keyword is used to create a function in Python?",
            "title": "Which keyword is used to create a function in Python?",
            "options": ["func", "define", "def", "function"],
            "answer": "def"
        },
        {
            "question":
            "What is the output of ```Python\nprint('Python'.find('o'))```?",
            "title": "What is the output of print('Python'.find('o'))",
            "options": ["4", "3", "5", "-1"],
            "answer": "4"
        },
        {
            "question":
            "What is the correct syntax to create a list in Python?",
            "title": "What is the correct syntax to create a list in Python?",
            "options": ["list = []", "list = ()", "list = {}", "list = ''"],
            "answer": "list = []"
        },
        {
            "question":
            "How do you insert an element at the end of a list in Python?",
            "title":
            "How do you insert an element at the end of a list in Python?",
            "options": [
                "list.append(element)", "list.add(element)",
                "list.insert(element)", "list.extend(element)"
            ],
            "answer":
            "list.append(element)"
        },

        # Medium Questions
        {
            "question":
            "What is the output of** ```Python\n print(3 ** 2)```**?",
            "title": "What is the output of print(3 ** 2)",
            "options": ["9", "6", "8", "27"],
            "answer": "9"
        },
        {
            "question":
            "How do you start a block of code in Python?",
            "title":
            "How do you start a block of code in Python?",
            "options": [
                "Using curly braces {}", "Using indentation",
                "Using semicolons ;", "Using parentheses ()"
            ],
            "answer":
            "Using indentation"
        },
        {
            "question":
            "Which method is used to remove any whitespace from the beginning and end of a string?",
            "title":
            "Which method is used to remove any whitespace from the beginning and end of a string?",
            "options": ["trim()", "strip()", "cut()", "remove()"],
            "answer": "strip()"
        },
        {
            "question":
            "What will** ```Python\ntype(5.0)``` **return?",
            "title":
            "What will type(5.0) return?",
            "options": [
                "<class 'int'>", "<class 'float'>", "<class 'str'>",
                "<class 'bool'>"
            ],
            "answer":
            "<class 'float'>"
        },
        {
            "question":
            "How do you comment a single line in Python?",
            "title":
            "How do you comment a single line in Python?",
            "options": [
                "# This is a comment", "// This is a comment",
                "/* This is a comment */", "-- This is a comment"
            ],
            "answer":
            "# This is a comment"
        },

        # Hard Questions
        {
            "question":
            "What is the output of ```Python\nprint([1, 2, 3] + [4, 5, 6])```?",
            "title":
            "What is the output of print([1, 2, 3] + [4, 5, 6])",
            "options": [
                "[1, 2, 3, 4, 5, 6]", "[5, 7, 9]", "[1, 2, 3] [4, 5, 6]",
                "[1, 2, 3] + [4, 5, 6]"
            ],
            "answer":
            "[1, 2, 3, 4, 5, 6]"
        },
        {
            "question":
            "Which of the following is used to handle exceptions in Python?",
            "title":
            "Which of the following is used to handle exceptions in Python?",
            "options": [
                "try...catch", "catch...finally", "try...except",
                "finally...except"
            ],
            "answer":
            "try...except"
        },
        {
            "question":
            "What does ```Python\nrange(5)``` function return?",
            "title":
            "What does the range(5) function return?",
            "options": [
                "[0, 1, 2, 3, 4]", "[1, 2, 3, 4, 5]",
                "range object with 5 elements", "[0, 1, 2, 3, 4, 5]"
            ],
            "answer":
            "[0, 1, 2, 3, 4]"
        },
        {
            "question": "What is the result of ```Python\nlen('Hello')```?",
            "title": "What is the result of len('Hello')?",
            "options": ["4", "5", "6", "None"],
            "answer": "5"
        },
        {
            "question":
            "Which method is used to add an element to the beginning of a list?",
            "title":
            "Which method is used to add an element to the beginning of a list?",
            "options": [
                "list.append(element)", "list.insert(0, element)",
                "list.add(element)", "list.extend(element)"
            ],
            "answer":
            "list.insert(0, element)"
        },

        # Very Hard Questions
        {
            "question":
            "What will **```Python\nlist(map(lambda x: x**2, [1, 2, 3]))``` **return?",
            "title":
            "What will list(map(lambda x: x**2, [1, 2, 3])) return?",
            "options":
            ["[1, 4, 9]", "[1, 2, 3]**2", "list of squares", "[1, 4, 9]"],
            "answer":
            "[1, 4, 9]"
        },
        {
            "question": "What is the output of ```Python\nprint('a' * 3)```?",
            "title": "What is the output of print('a' * 3)",
            "options": ["aaa", "a a a", "a3", "Error"],
            "answer": "aaa"
        },
        {
            "question":
            "What will the following code output? ```Python\nprint('hello'.capitalize())```?",
            "title": "What will print('hello'.capitalize()) output?",
            "options": ["Hello", "hello", "HELLO", "Error"],
            "answer": "Hello"
        },
        {
            "question":
            "What does ```Python\nzip([1, 2], ['a', 'b'])``` return?",
            "title":
            "What does zip([1, 2], ['a', 'b']) return?",
            "options": [
                "[(1, 'a'), (2, 'b')]", "[1, 'a', 2, 'b']",
                "[1, 2], ['a', 'b']", "None"
            ],
            "answer":
            "[(1, 'a'), (2, 'b')]"
        },
        {
            "question": "How do you declare a dictionary in Python?",
            "title": "How do you declare a dictionary in Python?",
            "options": ["dict = {}", "dict = []", "dict = ()", "dict = ''"],
            "answer": "dict = {}"
        },

        # Expert Questions
        {
            "question":
            "What is the output of ```Python\nprint({1: 'a', 2: 'b', 2: 'c'})```?",
            "title":
            "What is the output of print({1: 'a', 2: 'b', 2: 'c'})",
            "options": [
                "{1: 'a', 2: 'c'}", "{1: 'a', 2: 'b', 2: 'c'}",
                "{1: 'a', 2: 'b'}", "Error"
            ],
            "answer":
            "{1: 'a', 2: 'c'}"
        },
        {
            "question":
            "What does ```Python\nglobal x``` do inside a function?",
            "title":
            "What does global x do inside a function?",
            "options": [
                "It makes x local to the function",
                "It creates a new global variable x",
                "It accesses the global variable x",
                "It deletes the global variable x"
            ],
            "answer":
            "It accesses the global variable x"
        },
        {
            "question":
            "What is the output of ```Python\nprint(sorted([3, 1, 2]))```?",
            "title": "What is the output of print(sorted([3, 1, 2]))",
            "options": ["[1, 2, 3]", "[3, 1, 2]", "[2, 1, 3]", "Error"],
            "answer": "[1, 2, 3]"
        },
        {
            "question": "How do you create a generator in Python?",
            "title": "How do you create a generator in Python?",
            "options":
            ["Using `[]`", "Using `{}`", "Using `()`", "Using `lambda`"],
            "answer": "Using `()`"
        },
        {
            "question":
            "What will ```Python\nprint(list('hello'))``` output?",
            "title":
            "What will print(list('hello')) output?",
            "options":
            ["['h', 'e', 'l', 'l', 'o']", "'hello'", "['hello']", "Error"],
            "answer":
            "['h', 'e', 'l', 'l', 'o']"
        }
    ],
    "Lua": [
        # Easy Questions
        {
            "question": "Which function is used to print output to the console in Lua?",
            "title": "Which function is used to print output to the console in Lua?",
            "options": ["print()", "echo()", "output()", "write()"],
            "answer": "print()"
        },
        {
            "question": "What is the correct syntax to create a loop in Lua that runs 5 times?",
            "title": "What is the correct syntax to create a loop in Lua that runs 5 times?",
            "options": ["for i=1,5 do", "while i < 5 do", "repeat 5 times", "loop(5)"],
            "answer": "for i=1,5 do"
        },
        {
            "question": "How do you check if a variable `x` is equal to 10 in Lua?",
            "title": "How do you check if a variable `x` is equal to 10 in Lua?",
            "options": ["if x == 10 then", "if x = 10 then", "if x === 10 then", "if x eq 10 then"],
            "answer": "if x == 10 then"
        },
        {
            "question": "How do you declare a local variable in Lua?",
            "title": "How do you declare a local variable in Lua?",
            "options": ["local x = 5", "var x = 5", "int x = 5", "x := 5"],
            "answer": "local x = 5"
        },
        {
            "question": "Which of the following is used to concatenate strings in Lua?",
            "title": "Which of the following is used to concatenate strings in Lua?",
            "options": ["..", "+", "&", "++"],
            "answer": ".."
        },

        # Medium Questions
        {
            "question": "What is the result of the expression `type(nil)` in Lua?",
            "title": "What is the result of the expression `type(nil)` in Lua?",
            "options": ["'nil'", "'none'", "'null'", "'type'"],
            "answer": "'nil'"
        },
        {
            "question": "Which function is used to calculate the length of a table in Lua?",
            "title": "Which function is used to calculate the length of a table in Lua?",
            "options": ["#table", "table.size()", "len(table)", "table.length()"],
            "answer": "#table"
        },
        {
            "question": "In Lua, how do you define an anonymous function?",
            "title": "In Lua, how do you define an anonymous function?",
            "options": ["function() ... end", "anonymous() ... end", "lambda() ... end", "def() ... end"],
            "answer": "function() ... end"
        },
        {
            "question": "What is the purpose of the `pairs()` function in Lua?",
            "title": "What is the purpose of the `pairs()` function in Lua?",
            "options": ["To iterate over all key-value pairs in a table", "To get the length of a table", "To sort a table", "To reverse a table"],
            "answer": "To iterate over all key-value pairs in a table"
        },
        {
            "question": "How do you exit a loop early in Lua?",
            "title": "How do you exit a loop early in Lua?",
            "options": ["break", "exit", "stop", "return"],
            "answer": "break"
        },

        # Hard Questions
        {
            "question": "What does the `os.time()` function return in Lua?",
            "title": "What does the `os.time()` function return in Lua?",
            "options": ["Current time in seconds since epoch", "Current time as a string", "Current date and time", "Milliseconds since epoch"],
            "answer": "Current time in seconds since epoch"
        },
        {
            "question": "How do you handle errors in Lua using protected calls?",
            "title": "How do you handle errors in Lua using protected calls?",
            "options": ["pcall()", "try...catch", "error()", "trap()"],
            "answer": "pcall()"
        },
        {
            "question": "What will the function `table.insert()` do in Lua?",
            "title": "What will the function `table.insert()` do in Lua?",
            "options": ["Insert an element into a table", "Remove an element from a table", "Sort a table", "Find an element in a table"],
            "answer": "Insert an element into a table"
        },
        {
            "question": "How do you check the type of a variable in Lua?",
            "title": "How do you check the type of a variable in Lua?",
            "options": ["type(variable)", "typeof(variable)", "class(variable)", "checktype(variable)"],
            "answer": "type(variable)"
        },
        {
            "question": "Which of the following is a valid way to declare a table in Lua with both keys and values?",
            "title": "Which of the following is a valid way to declare a table in Lua with both keys and values?",
            "options": ["{a = 1, b = 2}", "{1: 'a', 2: 'b'}", "['a'] = 1, ['b'] = 2", "table a = {'a': 1, 'b': 2}"],
            "answer": "{a = 1, b = 2}"
        },

        # Very Hard Questions
        {
            "question": "What will the following code return? ```Lua\nfunction f() return 'Hello' end\nprint(f())```",
            "title": "What will the following code return?",
            "options": ["Hello", "nil", "Error", "f()"],
            "answer": "Hello"
        },
        {
            "question": "What is the purpose of the `coroutine.resume()` function in Lua?",
            "title": "What is the purpose of the `coroutine.resume()` function in Lua?",
            "options": ["To resume a suspended coroutine", "To create a new coroutine", "To end a coroutine", "To pause a coroutine"],
            "answer": "To resume a suspended coroutine"
        },
        {
            "question": "In Lua, what does the `require()` function do?",
            "title": "In Lua, what does the `require()` function do?",
            "options": ["Loads and runs a module", "Includes another Lua script", "Creates a new function", "Declares a variable"],
            "answer": "Loads and runs a module"
        },
        {
            "question": "How do you remove an element from a table in Lua?",
            "title": "How do you remove an element from a table in Lua?",
            "options": ["table.remove(t, index)", "t.pop(index)", "t.delete(index)", "table.delete(t, index)"],
            "answer": "table.remove(t, index)"
        },
        {
            "question": "What does the `collectgarbage()` function do in Lua?",
            "title": "What does the `collectgarbage()` function do in Lua?",
            "options": ["Performs memory management tasks", "Deletes all variables", "Closes the program", "Cleans up the stack"],
            "answer": "Performs memory management tasks"
        },

        # Expert Questions
        {
            "question": "What will the following Lua code output? ```Lua\nprint((10 > 5) and (5 < 10))```",
            "title": "What will the following Lua code output?",
            "options": ["true", "false", "nil", "1"],
            "answer": "true"
        },
        {
            "question": "In Lua, how do you define a metatable for a table?",
            "title": "In Lua, how do you define a metatable for a table?",
            "options": ["setmetatable(t, mt)", "t.metatable = mt", "table.metatable(t, mt)", "define_metatable(t, mt)"],
            "answer": "setmetatable(t, mt)"
        },
        {
            "question": "What is the purpose of the `__index` metamethod in Lua?",
            "title": "What is the purpose of the `__index` metamethod in Lua?",
            "options": ["To handle table indexing", "To sort a table", "To perform arithmetic operations", "To delete a table element"],
            "answer": "To handle table indexing"
        },
        {
            "question": "What will the following code return? ```Lua\nprint(math.floor(3.14))```",
            "title": "What will the following code return?",
            "options": ["3", "4", "3.1", "Error"],
            "answer": "3"
        },
        {
            "question": "What does the `ipairs()` function do in Lua?",
            "title": "What does the `ipairs()` function do in Lua?",
            "options": ["Iterates over a table with integer keys", "Iterates over all key-value pairs", "Returns the size of the table", "Creates a new table"],
            "answer": "Iterates over a table with integer keys"
        }
    ]
}