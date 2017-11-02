expense tracker (et)

- Credit (In) transaction logging
    ```
	ex:
	et in <amount> <description in quotes> <tags-comma seprated, optional>
	et in 30000 "Jun month Salary" salary,jun,2017
	et in 100 "interest for ICICI savings acct"
    ```

- Debit (Out) transaction logging
    ```
	ex:
	et out <amount> <description in quotes> <tags-comma seprated, optional>
	et out 3000 "Shopping" shopping,personal
    ```

- ability to add several Tags I/O transaction

- reports:
	- search transaction >, >=, <, <=, == given amount
        
        ```
		ex:
		et find txn amt > 2000
		et find txn amt >= 1000 and txn amt <= 5000
        ```

	- search transaction before/after/between certain date
		
        ```
        ex:
		et find txn date > 2017/05/12
		et find txn date >= 2017/06/01 and txn date <= 2017/07/15
        ```

	- combination of transaction amount + date
		
        ```
        ex:
		et find txn date >= 2017/06/01 and txn amt >= 5000
        ```

	- Filter which includes particular/certain Tag(s)
		
        ```
        ex:
		et find txn tagged "salary"
			- finds ALL transactions which are tagged with "salary"
		et find txn tagged "shopping,house" 
			- finds ALL transactions which are tagged with either "shopping" or "house" or both
        ```

	- Filter which does not includes particular/certain Tag(s)
		
        ```
        ex:
		et find txn tagged "shopping,house" not txn tagged "june,july"
			- finds ALL transactions which are tagged with either "shopping" or "house" or both, 
      but which are not tagged as either "june" or "july"
        ```

	- Top 10 higest transactions made tags wise
		
        ```
        ex:
			et find txn top 10 tagged "shopping,personal,medical"
				- finds top 10 (highest as per amount) transactions
        ```
