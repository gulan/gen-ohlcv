
-- sqlite3 varient of sql

drop table if exists ohlcv;

create table ohlcv (
    opentime integer not null,    -- unix timestamp
    openp    integer not null,    -- all currency is in US cents
    highp    integer not null,
    lowp     integer not null,
    closep   integer not null,
    volume   integer not null);

