CO1 AT2 - 24 SEPARATE PYTHON PROGRAMS

Install once: python -m pip install pandas
Run any program in VS Code terminal: python 01_student_admission_data_cleaning.py
Change the filename to run another question.

Each script includes its own sample data, so no external CSV/JSON/XML files are needed.

======================================================================
01 Student Admission Data Cleaning
FILE: 01_student_admission_data_cleaning.py
OUTPUT:
Name       Department        Phone
Arun Kumar COMPUTER SCIENCE   9876543210
     Priya      ELECTRONICS Not Provided
\nSaved clean_admissions.csv

======================================================================
02 Employee Data Integration
FILE: 02_employee_data_integration.py
OUTPUT:
Employees without a matching department: 1
 EmployeeID   Name  DepartmentID Department
        101    Anu             1         HR
        102   Bala             2         IT
        103 Charan             4        NaN

======================================================================
03 Product Inventory Processing
FILE: 03_product_inventory_processing.py
OUTPUT:
Missing or invalid prices: 2
Product  Price
    Pen   10.0
   Book    7.5
    Bag    7.5
 Pencil    5.0

======================================================================
04 Hospital Patient Data Validation
FILE: 04_hospital_patient_data_validation.py
OUTPUT:
Invalid patient records:
 PatientID  Age Gender BloodGroup
         2  150 Female         B+
         3   -4  Other          X
\nValid patient records:
 PatientID  Age Gender BloodGroup
         1   25   Male         A+
         4   42   Male         O+

======================================================================
05 Library Database Preparation
FILE: 05_library_database_preparation.py
OUTPUT:
BookID         Title  Author  Year
      1 Python Basics    Ravi  2020
      2  Data Science   Meena  2022
      4      AI Guide Unknown  2019
\nSaved clean_books.csv

======================================================================
06 Banking Transaction Analysis
FILE: 06_banking_transaction_analysis.py
OUTPUT:
Invalid transactions: 0
\nTransactions:
 TransactionID Account  Amount       Type
             1    A101    5000    Deposit
             2    A102   -2000 Withdrawal
             3    A101    1500    Deposit
             4    A103       0   Transfer
\nTotal transaction amount: 4500

======================================================================
07 Online Shopping Order Processing
FILE: 07_online_shopping_order_processing.py
OUTPUT:
Completed orders:
 OrderID Customer  Amount    Status
    1001     Asha    1200 Delivered
    1003   Charan    2500 Delivered
\nTotal completed sales: 3700

======================================================================
08 University Course Information Management
FILE: 08_university_course_information_management.py
OUTPUT:
Valid course details:
CourseID Course  Credits Department
     C01 Python        4        CSE
     C02   DBMS        3        CSE
     C04     AI        4         AI

======================================================================
09 Vehicle Registration Data Processing
FILE: 09_vehicle_registration_data_processing.py
OUTPUT:
RegistrationNo Owner VehicleType  Year
    TN01AB1234  Arun         Car  2020
    TN02CD5678  Bala        Bike  2022
    TN03EF9012 Divya       Truck  2018

======================================================================
10 Retail Sales Data Transformation
FILE: 10_retail_sales_data_transformation.py
OUTPUT:
Product  Quantity  UnitPrice  TotalSales
    PEN        10         10         100
   BOOK         5         50         250
    BAG         2        500        1000
 PENCIL        20          5         100
\nTotal retail sales: 1450

======================================================================
11 College Attendance Management
FILE: 11_college_attendance_management.py
OUTPUT:
Student  Present  TotalClasses  AttendancePercent       Status
   Asha       22            25               88.0     Eligible
   Bala       18            25               72.0 Not Eligible
 Charan       25            25              100.0     Eligible
  Divya       15            25               60.0 Not Eligible

======================================================================
12 Electricity Consumption Analysis
FILE: 12_electricity_consumption_analysis.py
OUTPUT:
Average consumption: 1070.0
\nTotal consumption by city:
City
Chennai    2550
Madurai    2000
Salem       800

======================================================================
13 School Examination Records
FILE: 13_school_examination_records.py
OUTPUT:
Student  Maths  Science  English  Total  Average Result
    Anu     85       90       78    253    84.33   Pass
   Bala     42       38       55    135    45.00   Fail
 Charan     76       81       69    226    75.33   Pass
  Divya     91       88       95    274    91.33   Pass

======================================================================
14 Weather Monitoring System
FILE: 14_weather_monitoring_system.py
OUTPUT:
Average temperature: 31.5
      City  Temperature  Humidity TemperatureStatus
   Chennai           32        70     Above Average
   Madurai           35        65     Above Average
Coimbatore           28        80            Normal
     Salem           31        75            Normal

======================================================================
15 Hotel Reservation Management
FILE: 15_hotel_reservation_management.py
OUTPUT:
Confirmed bookings:
 BookingID  Guest RoomType  Nights    Status
         1   Arun   Single       2 Confirmed
         3 Charan    Suite       1 Confirmed
\nTotal confirmed room nights: 3

======================================================================
16 Hospital Appointment Scheduling
FILE: 16_hospital_appointment_scheduling.py
OUTPUT:
Booked appointments:
 AppointmentID Patient   Doctor       Date Status
           101     Anu   Dr Rao 2026-11-05 Booked
           104   Divya Dr Mehta 2026-11-06 Booked
           103  Charan   Dr Rao 2026-11-06 Booked

======================================================================
17 Online Examination System
FILE: 17_online_examination_system.py
OUTPUT:
Student   Exam  Marks  TotalMarks  Percentage Result
   Asha Python     88         100        88.0   Pass
   Bala Python     34         100        34.0   Fail
 Charan   DBMS     76         100        76.0   Pass
  Divya   DBMS     91         100        91.0   Pass

======================================================================
18 Railway Ticket Reservation
FILE: 18_railway_ticket_reservation.py
OUTPUT:
Confirmed tickets:
 TicketID Passenger     Train  Fare    Status
        1       Anu Express A   450 Confirmed
        3    Charan Express A   450 Confirmed
\nTotal confirmed fare: 900

======================================================================
19 Insurance Claim Processing
FILE: 19_insurance_claim_processing.py
OUTPUT:
Valid approved claims:
 ClaimID Customer  ClaimAmount   Status
     501     Asha        25000 Approved
     504    Divya        18000 Approved
\nTotal approved amount: 43000

======================================================================
20 Mobile Phone Sales Analysis
FILE: 20_mobile_phone_sales_analysis.py
OUTPUT:
Sales by brand:
Brand
Apple      1690000
Samsung    1010000
Vivo        360000
\nTotal sales revenue: 3060000

======================================================================
21 Employee Payroll Preparation
FILE: 21_employee_payroll_preparation.py
OUTPUT:
Employee  BasicSalary  Allowance  Deduction  GrossSalary  NetSalary
     Anu        25000       5000       2000        30000      28000
    Bala        30000       6000       2500        36000      33500
  Charan        28000       4000       1500        32000      30500
\nSaved payroll_report.csv

======================================================================
22 Movie Database Management
FILE: 22_movie_database_management.py
OUTPUT:
Average movie rating: 7.88
\nHighest-rated movies:
  Movie Genre  Rating  Year
Movie C Drama     9.0  2021
Movie A Drama     8.2  2020

======================================================================
23 University Placement Records
FILE: 23_university_placement_records.py
OUTPUT:
Placed students:
Student Company  PackageLPA Status
   Asha     TCS         4.5 Placed
   Bala Infosys         3.8 Placed
 Charan  Google        18.0 Placed
\nAverage placement package: 8.77 LPA

======================================================================
24 Public Library Membership Analysis
FILE: 24_public_library_membership_analysis.py
OUTPUT:
Members with borrowing records:
 MemberID MemberName  BooksBorrowed MembershipType
        1        Anu              5         Annual
        2       Bala              3        Monthly
        3     Charan              8         Annual
        4      Divya              2        Monthly
\nTotal books borrowed: 18
\nBorrowed by membership type:
MembershipType
Annual     13
Monthly     5
