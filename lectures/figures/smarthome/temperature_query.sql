SELECT temperature, substr(timestamp, 12, 5)
FROM measurements
WHERE timestamp LIKE '2026-08-20 %'
ORDER BY timestamp
;
