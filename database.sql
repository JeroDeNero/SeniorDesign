CREATE TABLE TaggedLocs(
  Id int unsigned not null auto_increment,
  Longi smallint not null,
  Lat smallint not null,
  VideoTime smallint not null,
  ImageLoc varchar(512),

  primary key (Id)
);

CREATE TABLE HighlightedZones (
  Id int unsigned not null auto_increment,
  XPos int not null,
  YPos int not null,
  raduis int not null,

  primary key (Id)
);

CREATE Table Pipe (
  Id varchar(128) not null,
  Lat smallint,
  Longi smallint,
  Direction varchar(8),

  UNIQUE(Lat, Longi, Direction),

  primary key (Id)
);

CREATE TABLE Video (
  Id int unsigned not null auto_increment,
  Name varchar(32),
  VideoLoc varchar(512),
  VideoClipLoc varchar(512),
  Tagged smallint,
  DateTaken datetime not null,
  DriverName varchar(32),
  PipeID varchar(128) ,
  
  primary key (Id),

  foreign key (PipeID)
          references Pipe (Id)
          ON DELETE SET NULL
          ON UPDATE CASCADE
);

CREATE TABLE RoughLocation (
  Id int not null auto_increment,
  Name varchar(64) not null,
  Lat smallint not null,
  Longi smallint not null,
  Raduis smallint not null,

  UNIQUE (Name),
  UNIQUE (Lat, Longi, Raduis),

  primary key (Id)
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

CREATE TABLE TagToHighlights (
  LocationID int unsigned not null,
  HighlightID int unsigned not null,

  primary key (LocationID, HighlightID),

  foreign key (LocationID)
          references TaggedLocs (Id)
          ON DELETE CASCADE
          ON UPDATE CASCADE,

  foreign key (HighlightID)
          references HighlightedZones (Id)
          ON DELETE CASCADE
          ON UPDATE CASCADE
);

CREATE TABLE PipeToRoughLoc (
  PipeID varchar(128) not null,
  RoughLocID int  not null,

  primary key (PipeID, RoughLocID),

  foreign key (PipeID)
          references Pipe (Id)
          ON DELETE CASCADE
          ON UPDATE CASCADE,

  foreign key (RoughLocID)
          references RoughLocation (Id)
          ON DELETE CASCADE
          ON UPDATE CASCADE
);