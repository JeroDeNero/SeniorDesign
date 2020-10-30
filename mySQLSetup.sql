CREATE USER 'roboto'@'localhost' IDENTIFIED BY 'password';
CREATE DATABASE SewerBot;

GRANT ALL PRIVILEGES ON SewerBot.* TO 'roboto'@'localhost';

USE SewerBot;

CREATE TABLE TaggedLocs(
  Id int unsigned not null auto_increment,
  Position smallint not null,
  Longi smallint not null,
  Lat smallint not null,
  VideoTime smallint not null,

  UNIQUE(Id, Position),

  primary key (Id)
);

CREATE Table Pipe (
  Id varchar(128) not null,
  Lat smallint not null,
  Longi smallint not null,

  primary key (Id)
);

CREATE TABLE Video (
  Id int unsigned not null auto_increment,
  Name varchar(32),
  Tagged smallint,
  DateTaken datetime not null,
  DriverName varchar(32),
  PipeID varchar(128) ,
  Direction varchar(8),
  
  primary key (Id),

  foreign key (PipeID)
          references Pipe (Id)
          ON DELETE SET NULL
          ON UPDATE CASCADE
);

CREATE TABLE VideoToTags (
  VideoID int unsigned not null,
  TagID int unsigned not null,

  primary key (VideoID, TagID),

  foreign key (VideoID)
          references Video (Id)
          ON DELETE CASCADE
          ON UPDATE CASCADE,

  foreign key   (TagID)
          references TaggedLocs(Id)
          ON DELETE CASCADE
          ON UPDATE CASCADE
);

exit;
