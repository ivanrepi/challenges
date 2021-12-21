--Relacionar nombre de productos con nombre de cliente

SELECT 
sc.FirstName, 
sc.LastName,
p.name as ProductName
FROM SalesLT.Customer as sc 
JOIN SalesLT.Product p 
ON pc.productcategoryid = p.productcategoryid
ORDER BY CategoryName