# Data Flow Diagram (DFD) Documentation

## Project Title

**An Intelligent Expense Tracker with Financial Advisory System**

## Level 0 DFD

### External Entity

**User**

The user interacts with the Expense Tracker System by providing expense details and receiving reports and financial advice.

---

### Process

**Expense Tracker System**

The system performs the following functions:

* User Login and Registration
* Expense Management
* Expense Analysis
* Report Generation
* Financial Recommendation Generation

---

### Data Store

**Expense Database**

Stores:

* User Information
* Expense Records
* Financial Reports
* Advisory Data

---

## Data Flow

### User → Expense Tracker System

Input Data:

* Login Details
* Registration Details
* Expense Information
* Profile Information

### Expense Tracker System → Expense Database

Stored Data:

* User Records
* Expense Records
* Transaction Details

### Expense Database → Expense Tracker System

Retrieved Data:

* Expense History
* User Information
* Financial Records

### Expense Tracker System → User

Output Data:

* Dashboard Information
* Expense Reports
* Financial Advice
* Profile Details

---

## DFD Components

### Entity

* User

### Process

* Expense Tracker System

### Data Store

* Expense Database

### Inputs

* Expense Details
* User Details

### Outputs

* Reports
* Financial Recommendations
* Dashboard Summary

---

## Conclusion

The Data Flow Diagram illustrates how data moves between the User, Expense Tracker System, and Expense Database. The system processes expense information and generates meaningful reports and financial recommendations for users.
