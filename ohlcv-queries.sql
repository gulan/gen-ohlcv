
-- View data with currency as US dollars and cents.
-- TBD: summerize data by month.

select
  datetime(opentime,'unixepoch') as 'Open Time', 
  printf("%d.%.2d", openp/100, openp%100) as 'Open Price',
  printf("%d.%.2d", highp/100, highp%100) as 'High Price',
  printf("%d.%.2d", lowp/100, lowp%100) as 'Low Price',
  printf("%d.%.2d", closep/100, closep%100) as 'Close Price',
  printf("%d.%.2d", volume/100, volume%100) as 'Volume'
from ohlcv limit 30;


