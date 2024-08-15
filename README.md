# Python

Python is a popular programming language. It was created by Guido van Rossum and released in 1991.

## Use Cases

Python is used for:

- Web development (server-side)
- Software development
- Mathematics
- System scripting

## Capabilities

Python can:

- Create web applications on servers
- Be used alongside software to create workflows
- Connect to database systems and read/modify files
- Handle big data and perform complex mathematics
- Be used for rapid prototyping or production-ready software development

## Advantages

- Cross-platform compatibility (Windows, Mac, Linux, Raspberry Pi, etc.)
- Simple syntax similar to the English language
- Concise code compared to some other programming languages
- Interpreter-based execution, allowing quick prototyping
- Supports procedural, object-oriented, and functional programming paradigms

## Version Information

- The most recent major version is Python 3, which is used in this tutorial
- Python 2, while only receiving security updates, remains popular

## Development Environments

Python can be written in:

- Text editors
- Integrated Development Environments (IDEs) like Thonny, Pycharm, Netbeans, or Eclipse

## Syntax Comparison

Compared to other programming languages, Python:

- Emphasizes readability
- Uses new lines to complete commands instead of semicolons or parentheses
- Relies on indentation (whitespace) to define scope for loops, functions, and classes

Would you like me to explain or break down any part of this README.md code?

# Important Notes

### 1. Indentation

Indentation refers to the spaces at the beginning of a code line. Python uses indentation to indicate a block of code. The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one. You have to use the same number of spaces in the same block of code, otherwise Python will give you an error.

### 2. Comments

- Comments can be used to explain Python code.
- Comments can be used to make the code more readable.
- Comments can be used to prevent execution when testing code.
- Python does not really have a syntax for multiline comments. To add a multiline comment you could insert a # for each line.
- Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it.

### 3. Single or Double Quotes

- String variables can be declared either by using single or double quotes.

### 4. Case-Sensitive

- Variable names are case-sensitive.

### 5. Variable Names

A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:

- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and \_ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)
- A variable name cannot be any of the [Python keywords](https://www.w3schools.com/python/python_ref_keywords.asp).

### Multi Words Variable Names

Variable names with more than one word can be difficult to read. There are several techniques you can use to make them more readable:

1. **Camel Case:** Each word, except the first, starts with a capital letter. Example: `myVariableName`.
2. **Pascal Case:** Each word starts with a capital letter. Example: `MyVariableName`.
3. **Snake Case:** Each word is separated by an underscore character. Example: `my_variable_name`.

### Unpack a Collection

If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

### Global Variables

- Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
  Global variables can be used by everyone, both inside of functions and outside.

- If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

- Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function. To create a global variable inside a function, you can use the `global` keyword.

### Built-in Data Types

1. **Text Type:** `str`
2. **Numeric Types:** `int`, `float`, `complex`
3. **Sequence Types:** `list`, `tuple`, `range`
4. **Mapping Type:** `dict`
5. **Set Types:** `set`, `frozenset`
6. **Boolean Type:** `bool`
7. **Binary Types:** `bytes`, `bytearray`, `memoryview`
8. **None Type:** `NoneType`

You can get the data type of any object by using the `type()` function

### Python - Slicing Strings

You can return a range of characters by using the slice syntax. Specify the start index and the end index, separated by a colon, to return a part of the string.

```bash
b = "Hello, World!"
print(b[2:5])
```

### F-Strings

F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an `f` in front of the string literal, and add curly brackets `{}` as placeholders for variables and other operations.

```bash
age = 36
txt = f"My name is John, I am {age}"
print(txt)
```
