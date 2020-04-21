select 
(
    select distinct salary 
    from Employee e 
    order by salary desc
    limit 1, 1
)
as SecondHighestSalary;

