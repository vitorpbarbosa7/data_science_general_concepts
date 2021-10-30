select
inteiro, 

-- MAIN
-- input: bigint yyyyMMdd; action: subtracts three months: returns: bigint yyyyMMdd
,cast(from_timestamp(date_sub(cast(from_unixtime(unix_timestamp(cast(inteiro as string), 'yyyyMMdd')) as timestamp), interval 3 months), 'yyyyMMdd') as bigint) as shift_left3

-- converts bigint yyyyMMdd to string, then to unix_timestamp than to string readable date in unixtime
from_unixtime(unix_timestamp(cast(inteiro as string), 'yyyyMMdd'), 'yyyyMMdd') as _data

-- input: bigint yyyyMMdd; action: subtracts three months: returns: string yyyyMMdd 
,from_timestamp(date_sub(cast(from_unixtime(unix_timestamp(cast(inteiro as string), 'yyyyMMdd'))as timestamp), interval 3 months), 'yyyyMMdd') as shift_left3

,date_sub(cast(from_unixtime(unix_timestamp(cast(inteiro as string), 'yyyyMMdd')) as timestamp), interval 3 months) as shift_left3_aux

,unix_timestamp(cast(inteiro as string), 'yyyyMMdd') as _unix_timestamp

,from_unixtime(unix_timestamp(cast(inteiro as string), 'yyyyMMdd')) as _unixtime

,cast(from_unixtime(unix_timestamp(cast(inteiro as string), 'yyyyMMdd')) as timestamp) as _stringtimestamp

,date_sub(cast(from_unixtime(unix_timestamp(cast(inteiro as string), 'yyyyMMdd')) as timestamp), interval 3 months) as shift_left3

,typeof(from_unixtime(unix_timestamp(cast(inteiro as string), 'yyyyMMdd'))) as _typeofunixtime

,typeof(from_unixtime(unix_timestamp(cast(inteiro as string), 'yyyyMMdd'), 'yyyyMMdd')) as _typeofunixtimestr

from

datas;