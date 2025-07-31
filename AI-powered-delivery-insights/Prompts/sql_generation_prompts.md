# SQL Prompt Engineering Examples (ChatGPT)

## 🔍 Business Question 1:
> What are the top 5 delivery areas with the highest average delay this month?

**Prompt:**  
"Generate a SQL query to find the top 5 delivery areas with the highest average delay_minutes in June 2024 from a table named `deliveries`. Columns are: delivery_id, area, delivery_date, delay_minutes, status, customer_rating."

**ChatGPT Output SQL:**
```sql
SELECT area, AVG(delay_minutes) AS avg_delay
FROM deliveries
WHERE delivery_date BETWEEN '2024-06-01' AND '2024-06-30'
GROUP BY area
ORDER BY avg_delay DESC
LIMIT 5;
