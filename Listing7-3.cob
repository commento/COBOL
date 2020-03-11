IDENTIFICATION DIVISION.
PROGRAM-ID. LISTING7-3.

ENVIRONMENT DIVISION.
INPUT-OUTPUT SECTION.
FILE-CONTROL.
       SELECT EMPLOYEEFILE ASSIGN TO "Employee.dat"
           ORGANIZATION IS LINE SEQUENTIAL.

DATA DIVISION.
FILE SECTION.
FD     EMPLOYEEFILE.
01     EMPLOYEEDETAILS.
       88  ENDOFEMPLOYEEFILE   VALUE HIGH-VALUES.
       02  EMPSSN              PIC 9(9).
       02  EMPNAME.
           03  EMPSURNAME      PIC X(15).
           03  EMPFORENAME     PIC X(10).
       02  EMPDATEOFBIRTH.
           03  EMPYOB          PIC 9(4).
           03  EMPMOB          PIC 99.
           03  EMPDOB          PIC 99.
       02  EMPGENDER           PIC X.

PROCEDURE DIVISION.
BEGIN.
       OPEN EXTEND EMPLOYEEFILE
       PERFORM GETEMPLOYEEDATA
       PERFORM UNTIL EMPLOYEEDETAILS = SPACES
           WRITE EMPLOYEEDETAILS
           PERFORM GETEMPLOYEEDATA
       END-PERFORM
       CLOSE EMPLOYEEFILE
       DISPLAY "*************************** END OF INPUT ***************************"

       OPEN INPUT EMPLOYEEFILE
       READ EMPLOYEEFILE
           AT END SET ENDOFEMPLOYEEFILE TO TRUE
       END-READ
       PERFORM UNTIL ENDOFEMPLOYEEFILE
           DISPLAY EMPFORENAME SPACE EMPSURNAME " - "
               EMPDOB "/" EMPMOB "/" EMPYOB
            READ EMPLOYEEFILE
               AT END SET ENDOFEMPLOYEEFILE TO TRUE
            END-READ
       END-PERFORM
       CLOSE EMPLOYEEFILE
       STOP RUN.

GETEMPLOYEEDATA.
       DISPLAY "ENTER SSN (9 DIGITS) SURNAME (15 ALPHANUMERIC) FORENAME (10 ALPHANUMERIC) YEAR OF BIRTH YYYYMMDD"
       ACCEPT EMPLOYEEDETAILS.
