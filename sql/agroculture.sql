create database agroculture;

use agroculture;

create table user(`id` int(255) primary key,
`username` varchar(255) NOT NULL,
`password` varchar(255) NOT NULL,
`cpassword` varchar(255) NOT NULL,
`email` varchar(255) unique not null,
`mobile` varchar(255) NOT NULL,
`address` text NOT NULL,image varchar(255),
`category` varchar(255) NOT NULL);


ALTER TABLE `user`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;
  
create table product(id int(255) primary key,email varchar(255),name varchar(255),phone bigint(255),pcategory varchar(255),pname varchar(255),pcost bigint(255),quantity int(255),pdesc varchar(60000),pic varchar(255),status varchar(255));

ALTER TABLE `product`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;
  
create table order_details(id int(255) primary key,pid int(255),quantity int(255),uid int(255),username varchar(255),email varchar(255),phone varchar(255),city varchar(255),pincode int(255),address varchar(255),total int(255),status varchar(255));


CREATE TABLE review(pid int(10) NOT NULL,pname varchar(255),user_mail varchar(255),name varchar(255) NOT NULL,rating int(10) NOT NULL,comment text NOT NULL);
  
create table tbl_session(email varchar(255),name varchar(255),category varchar(255));