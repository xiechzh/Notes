Note FOR SQL: 菜鸟|bilibili
  
NOTES JAXSTA
telecaster:
.role ro // role_name | ro.role_group_id = rog.id | ro.id = re.entity_role_id
.role_group rog // description
.recording
.recording_entity re
.release_variant
.release_variant_entity // credited_name | entity_role
.release_variant_genre // genre
.release_variant_deal // included_territory

hummingbird
.user_entity_link
.user_entity_contact

sql:
update (sqlite)

INPORTANT QUERY: -- ISRC --> role and description for Performer credited

select distinct 
	t.credited_name,
	t.isrc,
	rog.description,
	ro.role_name
	from telecaster.role ro
	join telecaster.role_group rog 
		on ro.role_group_id = rog.id 
	join (
		select distinct
			re.entity_role_id,re.entity_role, re.credited_name,
			r3.isrc
			from telecaster.recording_entity re
			left join telecaster.recording r3
				on re.recording_id = r3.id
			where re.recording_id in (
--				select r2.id  -- 扩展了recording_id
--					from telecaster.recording r2
--					where r2.group_id in (
						select distinct r.id from telecaster.recording r where r.isrc = 'USSM19902990' 
--						in (
--						)
--					)
			)
	) t 
		on ro.id = t.entity_role_id
--		and rog.description in ('Performers','Main Artist','Featured Artist')
		order by t.isrc,rog.description
;
select r.group_id from telecaster.recording r where isrc = 'USSM19902990';



--MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
--**************************************************************************************************************
--WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
show tables;
select database();

--****************************************************************
--****************************************************************
select 100;
SELECT 'join';
SELECT 100%98;
SELECT VERSION();

-- 函数
SELECT concat('a','b','c'); 
select concat(description ,id) as try from telecaster.role_group rg; -- concat(): 合并2个字段
select ifnull(description, 0) from telecaster.role_group rg ; -- ifnull(): postgresql没有这个功能？
select length('张');
select trim('a' from 'aaaaaaaaabcaaaaaloveaaaaaaaaaaaaa') as res; -- trim(): 去掉前后的a
select trim('a' from 'bcd');
select lpad('telecaster',15,'*'); -- lpad():左填充 

-- 日期
select now();
select extract; -- ??
select current_date; -- **
select now() + interval '2 years'; -- ** 2年后
select now() - interval '2 w'; -- 3周前
select now() + '10 min';  -- 10分钟后
select to_date('21-2-2020','dd-mm-yyyy'); -- postgre 不常用,分秒对不上
select to_date('21-2-2020 18:33:41','dd-mm-yyyy hh24:mi:ss'); -- postgre 不常用,分秒被吞了
select to_timestamp('21-2-2020 18:33:41','dd-mm-yyyy hh24:mi:ss') ; -- ** 尽量用这个
select age(now(), timestamp '1992-5-30'); -- AGE() 计算时间差

-- 流程控制函数
select if(description is null, 0, id*100) from telecaster.role_group rg; -- ??
select -- ** 类似于switch语句，可以实现等值判断
	id,
	description,
	case description 
		when 'Main Artist' then 'a'
		when 'Featured Artist' then 'b'
		else description
	end newrole_group
from
	telecaster.role_group ;

select -- ** 类似多重if语句，实现区间判断
	description,id,
	case
	when id <2 then 'a'
	when id >2  then 'b'
	else 'd'
	end test
from telecaster.role_group rg 
;

-- 聚合函数
sum()
avg()
max()
min()
count()

-- lead函数 和 lag函数
-- 按照column channel 分组，按照 column start_time排序，取start_time的后一行作为end_time
lead() 取后一行的值
select lead(start_time,1,null) over (partition by channel order by start_time) end_time
from tablename
;

-- Litz's sql, learn some time
SELECT count(re.*) AS count, 'recording credits'::text AS description, now()::timestamp without time zone AS updated
FROM telecaster.recording_entity re
JOIN telecaster.recording r ON r.id = re.recording_id
WHERE r.rank > 0
;


select COUNT(distinct role_name) from telecaster.role;

--****************************************************************
--****************************************************************
Note FOR SQL: 菜鸟

show tables;
select database();

select 100;
SELECT 'join';
SELECT 100%98;
SELECT VERSION();

SELECT concat('a','b','c');



--****************************************************************
--****************************************************************
select distinct 
'https://jaxsta.com/release/' || an.release_group_id as url, 
an.release_group_id,ane.* from esquire_riaa.award_nomination an
join esquire_riaa.award_nomination_entity ane on
an.id = ane.award_nomination_id
where an.release_group_id = '001dddae-4166-4787-805e-15bf5aa47899'
order by ane.entity_role_id
;



--MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
--HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
--WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
--can delete
select concat(FirstName,LastName) as name from Customer c ;
select * from telecaster.release_group rg where rg.description like (concat('%',rg.title,'%'))

