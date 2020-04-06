IDENTIFICATION DIVISION.
PROGRAM-ID. Listing4-2.
AUTHOR. Michael Coughlan.
*> Accepts two numbers from the user, multiplies them together
*> and then displays the result.

DATA DIVISION.
WORKING-STORAGE SECTION.
01	Num1	PIC 9  VALUE 5.
01	Num2	PIC 9  VALUE 4.

01  Operator PIC X VALUE SPACE.
       88  ValidOperator VALUE "*", "/", "+", "-".
       88  ExitProgram   VALUE "s".

01	Result  PIC S99V99 VALUE ZEROS.

PROCEDURE DIVISION.

Begin.
       DISPLAY "Enter an operator (*,/,-,+) - " WITH NO ADVANCING
       ACCEPT Operator
       PERFORM CalculateResult WITH TEST BEFORE UNTIL ExitProgram.
       STOP RUN.

CalculateResult.
       DISPLAY "Enter a single digit number - " WITH NO ADVANCING
       ACCEPT Num1
       DISPLAY "Enter a single digit number - " WITH NO ADVANCING
       ACCEPT Num2
       EVALUATE Operator
           WHEN "*"  MULTIPLY Num1 BY Num2 GIVING Result
           WHEN "/"   DIVIDE Num1 BY Num2 GIVING Result
           WHEN "+"  ADD Num1 TO Num2 GIVING Result
           WHEN "-"   SUBTRACT Num2 FROM Num1 GIVING Result
       END-EVALUATE

       IF ValidOperator
       DISPLAY "Result is = " Result
       END-IF

       DISPLAY "Enter an operator (*,/,-,+) - " WITH NO ADVANCING
       ACCEPT Operator.
