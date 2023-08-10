# DB excersises

```
CREATE TABLE SUBJECTS (SUB_ID serial PRIMARY KEY , F_ID integer REFERENCES FACULTY,D_ID integer REFERENCES DEPARTMENT , sub_name VARCHAR (50) NOT NULL , sub_code VARCHAR (50) UNIQUE ) ; 

 INSERT INTO SUBJECTS (SUB_ID, D_ID ,F_ID,sub_name,sub_code) VALUES (0,1,0,'Database Systems','AA11' );

INSERT INTO SUBJECTS (SUB_ID, D_ID ,F_ID,sub_name,sub_code) VALUES (1,1,0,'Database Systems 1','BB11' );

INSERT INTO SUBJECTS (SUB_ID, D_ID ,F_ID,sub_name,sub_code) VALUES (2,1,0,'Database Systems 2','CC11' );


 INSERT INTO SUBJECTS (SUB_ID, D_ID ,F_ID,sub_name,sub_code) VALUES (3,0,0,'Database 1','DD11' );

INSERT INTO SUBJECTS (SUB_ID, D_ID ,F_ID,sub_name,sub_code) VALUES (4,0,0,'Database 2','EE11' );


INSERT INTO SUBJECTS (SUB_ID, D_ID ,F_ID,sub_name,sub_code) VALUES (5,0,0,'Database advanced','FF11');


 INSERT INTO SUBJECTS (SUB_ID, D_ID ,F_ID,sub_name,sub_code) VALUES (6,3,0,'genetic','GG11');

INSERT INTO SUBJECTS (SUB_ID, D_ID ,F_ID,sub_name,sub_code) VALUES (7,3,0,'computional','HH11');

INSERT INTO SUBJECTS (SUB_ID, D_ID ,F_ID,sub_name,sub_code) VALUES (8,3,0,'bioinformatics','II11');

INSERT INTO PROFESSOR (P_ID,F_ID,D_ID,F_name,L_name,age,salary) VALUES (0,0,0,'mostafa','ali',40,5000 );


INSERT INTO PROFESSOR (P_ID,F_ID,D_ID,F_name,L_name,age,salary) VALUES (1,0,1,'mostafa','Abo bakr',45,6000 );


INSERT INTO PROFESSOR (P_ID,F_ID,D_ID,F_name,L_name,age,salary) VALUES (3,0,1,'taysir','hassan',50,10000 );


INSERT INTO PROFESSOR (P_ID,F_ID,D_ID,F_name,L_name,age,salary) VALUES (2,0,3,'ibrahem','al3ady',50,105000 );


INSERT INTO COURSES (C_ID, SUB_ID ,DURATION,P_ID) VALUES (0,1,'30 hours',1);


INSERT INTO COURSES (C_ID, SUB_ID ,DURATION,P_ID) VALUES (1,1,'40 hours',2);


INSERT INTO COURSES (C_ID, SUB_ID ,DURATION,P_ID) VALUES (2,3,'45 hours',3);


CREATE TABLE STUDENTS (STUD_ID serial PRIMARY KEY , F_NAME  VARCHAR (50) NOT NULL , L_NAME  VARCHAR (50) NOT NULL , F_PHONE  integer  NOT NULL, l_PHONE  integer  NOT NULL , birth_date DATE NOT NULL,D_ID integer REFERENCES DEPARTMENT) ;


INSERT INTO STUDENTS (STUD_ID, F_NAME ,L_NAME,F_PHONE,L_PHONE,birth_date,D_ID) VALUES (0,'david','ayman',0122,5555,'9/1/2001',3);


INSERT INTO STUDENTS (STUD_ID, F_NAME ,L_NAME,F_PHONE,L_PHONE,birth_date,D_ID) VALUES (1,'dodo','maged',0111,5555,'9/1/2014',1);


INSERT INTO STUDENTS (STUD_ID, F_NAME ,L_NAME,F_PHONE,L_PHONE,birth_date,D_ID) VALUES (2,'deo','maged',01155,5555,'9/1/2018',2);


INSERT INTO STUDENTS (STUD_ID, F_NAME ,L_NAME,F_PHONE,L_PHONE,birth_date,D_ID) VALUES (3,'arsany','osama',01122,5555,'9/1/2010',2);


 INSERT INTO STUDENTS (STUD_ID, F_NAME ,L_NAME,F_PHONE,L_PHONE,birth_date,D_ID) VALUES (4,'neno','mensa',01777,5555,'9/1/2000',0);


INSERT INTO STUDENTS (STUD_ID, F_NAME ,L_NAME,F_PHONE,L_PHONE,birth_date,D_ID) VALUES (5,'bebo','atef',019999,5555,'9/1/1998',0);

 INSERT INTO STUDENTS (STUD_ID, F_NAME ,L_NAME,F_PHONE,L_PHONE,birth_date,D_ID) VALUES (6,'gogo','nabil',019999,5555,'9/1/1995',0);
 
 INSERT INTO STUDENTS (STUD_ID, F_NAME ,L_NAME,F_PHONE,L_PHONE,birth_date,D_ID) VALUES (7,'kero','esmat',01229,5555,'9/1/1999',0);
 
 INSERT INTO STUDENTS (STUD_ID, F_NAME ,L_NAME,F_PHONE,L_PHONE,birth_date,D_ID) VALUES (8,'bassem','maher',012222,5555,'9/1/1995',3)
 
 INSERT INTO STUDENTS (STUD_ID, F_NAME ,L_NAME,F_PHONE,L_PHONE,birth_date,D_ID) VALUES (9,'batrick','peter',013322,5555,'9/1/1998',3);


INSERT INTO STUDENTS (STUD_ID, F_NAME ,L_NAME,F_PHONE,L_PHONE,birth_date,D_ID) VALUES (10,'geno','peter',013322,5555,'9/1/1995',3);


INSERT INTO STUDENTS (STUD_ID, F_NAME ,L_NAME,F_PHONE,L_PHONE,birth_date,D_ID) VALUES (10,'danial','maged',013662,5555,'9/1/1995',3);


INSERT INTO STUDENTS (STUD_ID, F_NAME ,L_NAME,F_PHONE,L_PHONE,birth_date,D_ID) VALUES (11,'danial','maged',013662,5555,'9/1/1995',3);


SELECT * FROM STUDENTS;

INSERT INTO STUDENTS (STUD_ID, F_NAME ,L_NAME,F_PHONE,L_PHONE,birth_date,D_ID) VALUES (12,'sosa','ayman',01552,5555,'6/10/2002',1);

INSERT INTO STUDENTS (STUD_ID, F_NAME ,L_NAME,F_PHONE,L_PHONE,birth_date,D_ID) VALUES (13,'boty','ayman',01552,5555,'5/11/2005',1);


INSERT INTO STUDENTS (STUD_ID, F_NAME ,L_NAME,F_PHONE,L_PHONE,birth_date,D_ID) VALUES (14,'tony','ayman',01552,5452,'5/11/2006',1);


SELECT * FROM STUDENTS;

 SELECT * FROM COURSES;

 INSERT INTO EXAMS (E_ID,C_ID,date,time,duration) VALUES (0,1,'9/10/2023','10.00','2' );

INSERT INTO EXAMS (E_ID,C_ID,date,time,duration) VALUES (0,1,'9/10/2023','10:00:00' ,'2' );

INSERT INTO EXAMS (E_ID,C_ID,date,time,duration) VALUES (1,2,'9/11/2023','11:00:00' ,'3' );

SELECT * FROM COURSES;


INSERT INTO EXAMS (E_ID,C_ID,date,time,duration) VALUES (2,0,'9/12/2023','12:00:00' ,'2' );


SELECT * FROM STUDENTS;

SELECT * FROM PROFESSOR;

SELECT * FROM SUBJECTS;

 SELECT * FROM COURSES;


SELECT * FROM EXAMS;

SELECT * FROM DEPARTMENT;

 FROM PROFESSOR WHERE age >=40; 

SELECt * FROM PROFESSOR WHERE age >=45; 

SELECt * FROM PROFESSOR WHERE salary >=10000; 

 SELECt * FROM PROFESSOR ORDER BY salary DESC;
 
 SELECt * FROM STUDENTS ORDER BY birth_date DESC; 
 
  SELECT salary FROM PROFESSOR GROUP BY salary;


 SELECT salary,  AVG(salary) FROM PROFESSOR GROUP BY salary;

UPDATE PROFESSOR SET salary = '100' WHERE salary >= 20000;


DELETE FROM PROFESSOR WHERE salary > 5000; 

ALTER TABLE STUDENTS ADD COLUMN age integer;

INSERT INTO STUDENTS (STUD_ID, F_NAME ,L_NAME,F_PHONE,L_PHONE,birth_date,D_ID,age) VALUES (15,'davd','ayman',0122,5555,'9/1/2001',3,20); 


SELECT * FROM cd.facilities

SELECT name, membercost FROM cd.facilities

SELECT * FROM cd.facilities WHERE membercost > 0 ;


SELECT facid , name , membercost,monthlymaintenance 
FROM cd.facilities 
WHERE
membercost > 0 and 
(membercost < monthlymaintenance/50.0);

SELECT *
	FROM cd.facilities 
	WHERE
			name like '%Tennis%';
			
			
SELECT * FROM cd.facilities WHERE facid in (1,5)


SELECT name , 
		case when (monthlymaintenance > 100)then 
						'expensive'
		else 
		 				'cheap '
		end as cost 
			from cd.facilities;          

 
 
 SELECT memid , surname, firstname , joindate FROM cd.members WHERE joindate >= '2012-9-1'
 
 
 SELECT DISTINCT surname 
	FROM cd.members 
ORDER BY surname
limit 10 ;



SELECT name FROM cd.facilities 
union 
SELECT surname FROM cd.members;


SELECT max(joindate) as latest
		from cd.members;
		
		
		

select firstname, surname, joindate
		from cd.members 
		where joindate= 
				(select max(joindate)
				from cd.members);
				
				
select bks.starttime 
	from 
		cd.bookings bks
		inner join cd.members mems
			on mems.memid = bks.memid
	where 
		mems.firstname='David' 
		and mems.surname='Farrell';        
		
		
insert into cd.facilities 
	(facid, name, membercost, guestcost, initialoutlay, monthlymaintenance) 
	select 9,'spa',20,30,100000,800
	union all
	select 10,'squash court 2', 3.5,17.5,5000,80 ; 

insert into cd.facilities
    (facid, name, membercost, guestcost, initialoutlay, monthlymaintenance)
    select (select max(facid) from cd.facilities)+1, 'Spa', 20, 30, 100000, 800;          
    
    
 update cd.facilities
    set initialoutlay = 10000;

update cd.facilities
    set
        membercost = 6,
        guestcost = 30
    where facid in (0,1);     
    
    






















```
