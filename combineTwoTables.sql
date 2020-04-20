Select FirstName, LastName, City, State 
From Person P 
Left Join Address A ON a.PersonId = p.PersonId
Union
Select FirstName, LastName, City, State
From Address A 
Right Join Person p ON p.personId = a.personId
