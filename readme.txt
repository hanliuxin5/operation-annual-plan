继续测试6


mysql -h annual-plan.cofpd3anyy8m.ap-southeast-1.rds.amazonaws.com -P 3306 -u lychee -p
 ssh -i lychee.pem ubuntu@ec2-52-221-243-200.ap-southeast-1.compute.amazonaws.com

sudo netstat -ntlp


CREATE TABLE user(
 id INT NOT NULL,
 avatar VARCHAR(100) NOT NULL,
 nickname VARCHAR(100) NOT NULL,
 pic VARCHAR(100),
 pics text,
 cTime VARCHAR(30),
 uTime VARCHAR(30),
 status int,
 PRIMARY KEY(id)
 );


 insert into user values(1,'touxiang.jpg','nicheng','diku.jpg','hudong.jpg;hudong.jpg','00','01',0);