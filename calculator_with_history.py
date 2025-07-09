print("------------------------------")
print("🎤WELCOME TO SIMPLE CALCULATOR🎤")
print("------------------------------")

# my file
HISTORY_FILE='myfile4.txt'

def show_history():
    """
Show all previous calculations from the history file.
Displays the history in reverse (latest at top).
    """
    file=open(HISTORY_FILE,'r')
    lines=file.readlines()
    if len(lines)==0:
        print("no history available")
    else:
        for line in reversed(lines):
            print(line.strip())
        file.close()
        
# clear allprevious history and make file new
def clear_history():
    """
Clear the contents of the history file.
Effectively resets the calculator history.
    """
    file=open(HISTORY_FILE,'w')
    file.close()
    print("file closed")

# save all the calculation in the history file

def save_to_history(equation, result):
    """
    Save the current equation and its result to the history file.
    Args:
        equation (str): The equation entered by the user.
        result (float/int): The calculated result.
    """
    file=open(HISTORY_FILE,'a')
    file.write(equation + "=" + str(result)+ "\n")
    file.close()

# required calculation
def calculation(user_input):
    """
    Handle the actual calculation logic.
    Supports: +, -, *, /, **, %, /2 (average)
    Args:
        user_input (str): Input string like '2 + 3'
    """
    parts= user_input.split()
    if len(parts)!= 3:
        print("invalid user input: plz take operator number (e.g- 2+3)")
        return
    
    num1 = float(parts[0])
    op =parts[1]
    num2 = float(parts[2])
    
    if op=="+":
        result=num1+num2
    elif op=="-":
        result=num1-num2
    elif op=="*":
        result=num1*num2
    elif op=="/":
        if num2==0:
            print("cannnot take denomenator as a zero or divided by zero")
            return
        else:
            result=num1/num2
    elif op=="**":
        result = num1 ** num2
    elif op=="%":
        result = num1 % num2
    elif op=="/2":
        result = (num1+num2)/2
    else:
        print("invalid operator use only (+,-,/,*) or (show, history, clear, exit)")
        return
    
    if int(result)==result:
        result=int(result)
        
# final result 7 save the calculation in history file
    print("👉result: ", result)
    save_to_history(user_input,result)
    
# calling main functiobn
def main():
    """
    The main loop for the calculator.
    Handles user commands and input processing.
    """
    print("🔤Type equations like: 5 + 3")
    print("♦️Or use commands: show, clear, exit\n")
    while True:
        user_input=input("enter your choice- calculation(➕,➖,✖️,➗,*️⃣) or command(exit,clear,show): ")
        if user_input=='exit':
            print("👍goodbyee")
            break
        elif user_input=='show':
            show_history()
        elif user_input=='clear':
            clear_history()
        else:
            calculation(user_input)
            
main()